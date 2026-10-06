#include "recomp_api.h"
#include "reo_mem.h"
#include "reo_master.h"
#include "reo_cheats.h"
#include "gen_cheats.h"

// The data cheats: plain RAM writes at every frame, like a pnach patch=1 line (they cost nothing in the recompiled
// game). Every address is the verified one on the owner's disc (README, the table of every cheat):
//   Player 1 block 0x004A5C30 (the original release has it 0x80 lower), the results data 0x003B84xx, the save block
//   0x0031FB60-0x00323D94 (0x980 lower on the original release), the pad halfword 0x002B081C (0xA00 lower there).
// Save data only ever gets valid values: bits are only added, and only bits the game itself sets (the masks in
// gen_cheats.h come from the game's own tables); numbers stay within the game's display range.
// Where two options write the same word, the first one listed below that is on wins.

#define ON(key) (Reo_Opt(key) != 0)

// ---- held parameters -------------------------------------------------------------------------------------------------
// A value the game sets up once per scenario (speed and size factors, damage factor, character, model...). The mod
// remembers what the game had when it started writing and puts it back when the option (or its master code) goes Off,
// if the value is still the mod's. Outside a scenario nothing is held and nothing is restored: the next scenario sets
// its own values up.
typedef struct {
    u32 addr;
    u32 width;
    u32 saved;
    u32 value;
    u32 active;
} Reo_Hold;

static Reo_Hold sHoldFast = { 0x004A5D20, 4, 0, 0, 0 };
static Reo_Hold sHoldSpeed2 = { 0x004A67F0, 4, 0, 0, 0 };
static Reo_Hold sHoldScale[3] = { { 0x004A5CE4, 4, 0, 0, 0 }, { 0x004A5CE8, 4, 0, 0, 0 }, { 0x004A5CEC, 4, 0, 0, 0 } };
static Reo_Hold sHoldDamage = { 0x004A67F4, 4, 0, 0, 0 };
static Reo_Hold sHoldVirus2 = { 0x004A67E8, 4, 0, 0, 0 };
static Reo_Hold sHoldModel = { 0x004A67E4, 2, 0, 0, 0 };
static Reo_Hold sHoldAltCostume = { 0x004A67EC, 1, 0, 0, 0 };
static Reo_Hold sHoldCharType = { 0x004A67C8, 1, 0, 0, 0 };
static Reo_Hold sHoldPlayers = { 0x004BAEA0, 1, 0, 0, 0 };

static void Reo_HoldSet(Reo_Hold* h, u32 ready, u32 on, u32 value) {
    if (!ready) {
        h->active = 0;
        return;
    }
    if (on) {
        if (!h->active) {
            h->saved = Reo_Read(h->addr, h->width);
            h->active = 1;
        }
        h->value = value;
        Reo_Write(h->addr, h->width, value);
    } else if (h->active) {
        h->active = 0;
        if (Reo_Read(h->addr, h->width) == h->value) {
            Reo_Write(h->addr, h->width, h->saved);
        }
    }
}

// A choice option's value: 0 = Off, otherwise the table entry (a value past the table counts as Off).
static u32 Reo_ChoiceValue(const char* key, const u32* values, u32 count, u32* out) {
    u32 v = Reo_Opt(key);

    if (v == 0 || v >= count) {
        return 0;
    }
    *out = values[v];
    return 1;
}

// ---- Player 1 Item Slot Modifiers ------------------------------------------------------------------------------------
// The slot option picks an item name (or "past the table +N"); the value written is the item's number in the chosen
// Item Values table (the first number with that name).
static void Reo_ItemSlots(void) {
    u32 table = Reo_Opt(REO_KEY_ITEM_TABLE);
    const u8* names;
    u32 len;
    u32 s;

    if (table >= REO_ITEM_TABLE_COUNT) {
        return;
    }
    names = kReoItemTables[table];
    len = kReoItemTableLen[table];
    for (s = 0; s < REO_ARRAY_COUNT(kReoSlots); s++) {
        u32 v = Reo_Opt(kReoSlots[s].key);
        u32 i;

        if (v == 0) {
            continue;
        }
        if (v <= REO_ITEM_NAME_COUNT) {
            for (i = 0; i < len; i++) {
                if (names[i] == v - 1) {
                    Reo_Write(kReoSlots[s].addr, 1, i);
                    break;
                }
            }
        } else if (v <= REO_ITEM_NAME_COUNT + REO_ITEM_PAST_COUNT) {
            u32 n = len + (v - REO_ITEM_NAME_COUNT - 1);
            if (n <= 0xFF) {
                Reo_Write(kReoSlots[s].addr, 1, n);
            }
        }
    }
}

// ---- save data -------------------------------------------------------------------------------------------------------
static void Reo_SaveData(u32 armax, u32 cb, u32 gs) {
    u32 i;
    u32 costume[2] = { 0, 0 };

    // Collection bitsets (group 0: six words). Only the bits of items that exist.
    if (cb && ON("cb_have_all_collection_available")) {
        for (i = 0; i < 6; i++) {
            Reo_SetBits(0x00323BF4 + 4 * i, kReoCollectionMask[i]);
        }
    }
    if ((cb && ON("cb_have_all_collection_purchased")) || (gs && ON("mc_unlock_entire_collection"))) {
        for (i = 0; i < 6; i++) {
            Reo_SetBits(0x00323C54 + 4 * i, kReoCollectionMask[i]);
        }
    }

    // Scenarios: the five scenario bits (the code's FFFFFFFF would also save 27 bits the game never sets).
    if (gs && ON("unlock_all_scenarios")) {
        Reo_SetBits(REO_SAVE_SCENARIOS, 0x0000001Fu);
    }

    // Points (0x0031FB60): at most 99,999,999, the display maximum.
    if (cb && ON("cb_max_reward_points")) {
        Reo_Write(0x0031FB60, 4, 99999999u);
    } else if (armax && ON("cj_max_collection_pts")) {
        Reo_Write(0x0031FB60, 4, 0x00320000u);
    } else if (gs && ON("mc_max_result_points")) {
        Reo_Write(0x0031FB60, 4, 99999u);
    } else if (cb && ON("cb_infinite_reward_points")) {
        u32 points = (REO_EE_U32(0x0031FB60) & 0xFFFF0000u) | 0x0000FFFFu;
        if (points <= 99999999u) {
            Reo_Write(0x0031FB60, 4, points);
        }
    }

    // Costumes: one byte per character from 0x0031FB64 (bit 0 Type B, bit 1 Type C), only the bits the game sets.
    if (cb && ON("cb_all_costumes")) {
        costume[0] |= kReoCostumeMask[0];
        costume[1] |= kReoCostumeMask[1];
    }
    for (i = 0; i < REO_ARRAY_COUNT(kReoCostumes); i++) {
        if (cb && ON(kReoCostumes[i].key)) {
            u32 byte = kReoCostumes[i].addr - 0x0031FB64;
            costume[byte >> 2] |= kReoCostumes[i].bits << ((byte & 3) * 8);
        }
    }
    Reo_SetBits(0x0031FB64, costume[0]);
    Reo_SetBits(0x0031FB68, costume[1]);

    // NPCs (0x0031FB6C, three words): the bits the game's collection table sets.
    if (cb && ON("cb_unlock_all_npcs")) {
        for (i = 0; i < 3; i++) {
            Reo_SetBits(0x0031FB6C + 4 * i, kReoNpcMask[i]);
        }
    }

    // Infinity mode: 0x0031FB7F bits 0x01 and 0x04, the two bits the game sets there.
    if ((cb && ON("cb_unlock_infinity_mode")) || (gs && ON("mc_unlock_infinity_mode"))) {
        Reo_SetBits(0x0031FB7C, REO_INFINITY_BITS);
    }
}

// ---- Player 1 --------------------------------------------------------------------------------------------------------
static void Reo_Player1(u32 armax, u32 cb, u32 gs, u32 ready, u32 pad) {
    u32 v = 0;
    u32 on;

    // Holds (restored when switched off).
    on = armax && ON("cj_super_fast_hero");
    v = 0x40000000u;
    if (!on && armax && ON("cj_fast_hero")) {
        on = 1;
        v = 0x3FC00000u;
    }
    Reo_HoldSet(&sHoldFast, ready, on, v);
    if (!on && gs) {
        on = Reo_ChoiceValue("bh_p1_speed_2", kVal_bh_p1_speed_2, REO_ARRAY_COUNT(kVal_bh_p1_speed_2), &v);
    }
    Reo_HoldSet(&sHoldSpeed2, ready, on, v);

    on = armax && ON("cj_giant_hero");
    Reo_HoldSet(&sHoldScale[0], ready, on, 0x3FC00000u);
    Reo_HoldSet(&sHoldScale[1], ready, on, 0x3FC00000u);
    Reo_HoldSet(&sHoldScale[2], ready, on, 0x3FC00000u);

    on = gs && Reo_ChoiceValue("bh_p1_damage", kVal_bh_p1_damage, REO_ARRAY_COUNT(kVal_bh_p1_damage), &v);
    Reo_HoldSet(&sHoldDamage, ready, on, v);

    on = gs && Reo_ChoiceValue("bh_p1_virus_gauge_2", kVal_bh_p1_virus_gauge_2, REO_ARRAY_COUNT(kVal_bh_p1_virus_gauge_2),
                          &v);
    Reo_HoldSet(&sHoldVirus2, ready, on, v);

    on = gs && Reo_ChoiceValue("bh_p1_model", kVal_bh_p1_model, REO_ARRAY_COUNT(kVal_bh_p1_model), &v);
    Reo_HoldSet(&sHoldModel, ready, on, v);

    on = gs && Reo_ChoiceValue("bh_p1_alt_costume", kVal_bh_p1_alt_costume, REO_ARRAY_COUNT(kVal_bh_p1_alt_costume), &v);
    Reo_HoldSet(&sHoldAltCostume, ready, on, v);

    on = gs && Reo_ChoiceValue("bh_p1_char_type", kVal_bh_p1_char_type, REO_ARRAY_COUNT(kVal_bh_p1_char_type), &v);
    Reo_HoldSet(&sHoldCharType, ready, on, v);

    if (!ready) {
        return;
    }

    // HP word 0x004A6174 (HP low half, max HP high half).
    if (armax && ON("cj_infinite_health_max_health")) {
        Reo_Write(0x004A6174, 4, 0x270F270Fu);
    } else if (gs && ON("mc_infinite_health")) {
        Reo_Write(0x004A6174, 4, 0x08FC08FCu);
    } else if (armax && ON("infinite_health")) {
        u32 maxHp = Reo_Read(0x004A6176, 2);
        if (maxHp != 0) {
            Reo_Write(0x004A6174, 2, maxHp);
        }
    }

    // Virus gauge 0x004A67DC. The saved No Infection / Freeze Infection of 1.0/1.1 keeps its 1.1.0 meaning: with
    // Infection Freeze Value 0 it also clears the gauge (Codejunkies' Zero Virus Gauge), which needs both the
    // CodeBreaker master code (No Infection is a CodeBreaker cheat) and the Action Replay MAX master code.
    if ((armax && ON("cj_zero_virus_gauge")) ||
        (armax && cb && ON("no_infection") && Reo_Opt("infection_freeze_value") == 0)) {
        Reo_Write(0x004A67DC, 4, 0);
    } else if (gs && ON("bh_p1_virus_gauge_1")) {
        u32 type = Reo_Read(0x004A67C8, 1);
        u32 pct = Reo_Opt("bh_p1_virus_gauge_1_value");

        if (pct > 99) {
            pct = 99;
        }
        if (type < 8) {
            // The game's own maximum for the character (game.bin table 0x0071ADB0, Kevin 151200); 100 % kills.
            u32 max = REO_EE_U32(0x0071ADB0 + 4 * type);
            Reo_Write(0x004A67DC, 4, max / 100 * pct);
        }
    }

    // Speed #1 (0x004A67D8): the game sets it again itself while you move and turn, so it is written, not held.
    if (gs && Reo_ChoiceValue("bh_p1_speed_1", kVal_bh_p1_speed_1, REO_ARRAY_COUNT(kVal_bh_p1_speed_1), &v)) {
        Reo_Write(0x004A67D8, 4, v);
    }

    // Bytes of the flags word 0x004A67D0.
    if (gs && Reo_ChoiceValue("bh_p1_status", kVal_bh_p1_status, REO_ARRAY_COUNT(kVal_bh_p1_status), &v)) {
        Reo_Write(0x004A67D0, 1, v);
    }
    if (gs && ON("bh_enemies_cant_touch")) {
        Reo_Write(0x004A67D2, 1, 0x20);
    }
    if (gs && ON("bh_enemies_dont_notice")) {
        if (pad == 0xFEEF) {
            Reo_Write(0x004A67D1, 1, 1);  // L2+Up
        } else if (pad == 0xFEBF) {
            Reo_Write(0x004A67D1, 1, 0);  // L2+Down
        }
    }
    if (gs && ON("bh_rapid_fire") && pad == 0xB7FF) {
        Reo_Write(0x004A67D3, 1, 0xFF);  // R1+Cross
    }
    if (gs && ON("bh_animation_picker")) {
        Reo_Write(0x004A67CB, 1, Reo_Opt("bh_animation_picker_value") & 0xFFu);
    }
    if (gs && ON("bh_walk_through_walls")) {
        Reo_Write(0x004A68E0, 4, 0xFFFFFFFFu);
        Reo_Write(0x004A68FC, 4, 0xFFFFFFFFu);
    }
    if (gs) {
        Reo_ItemSlots();
    }
}

// ---- scenario (game.bin loaded) --------------------------------------------------------------------------------------
static void Reo_Scenario(u32 gs, u32 game) {
    u32 v = 0;
    u32 on;

    on = gs && Reo_ChoiceValue("bh_number_of_players", kVal_bh_number_of_players, REO_ARRAY_COUNT(kVal_bh_number_of_players),
                          &v);
    Reo_HoldSet(&sHoldPlayers, game, on, v);

    if (!game || !gs) {
        return;
    }
    if (ON("bh_have_all_files")) {
        Reo_Write(0x004B9C80, 2, 0xFFFF);
    }
    // Scenario Completion Codes: the results data the results screen reads.
    if (ON("bh_completed_events_1")) {
        Reo_Write(0x003B84F8, 4, Reo_Opt("bh_completed_events_1_value"));
    }
    if (ON("bh_completed_events_2")) {
        Reo_Write(0x003B84FC, 4, Reo_Opt("bh_completed_events_2_value"));
    }
    if (Reo_ChoiceValue("bh_result_points_best_record", kVal_bh_result_points_best_record,
                   REO_ARRAY_COUNT(kVal_bh_result_points_best_record), &v)) {
        Reo_Write(0x003B8505, 1, v);
    }
    if (Reo_ChoiceValue("bh_completion_time_best_record", kVal_bh_completion_time_best_record,
                   REO_ARRAY_COUNT(kVal_bh_completion_time_best_record), &v)) {
        Reo_Write(0x003B8506, 1, v);
    }
    if (ON("bh_no_damage_clear")) {
        Reo_Write(0x003B84F4, 1, 0);
    }
    if (ON("bh_no_weapon_clear")) {
        Reo_Write(0x003B84F5, 1, 0);
    }
    if (ON("bh_result_points_modifier")) {
        v = Reo_Opt("bh_result_points_modifier_value");
        Reo_Write(0x003B84B4, 4, v > 99999999u ? 99999999u : v);
    }
    if (Reo_ChoiceValue("bh_completion_time_rank", kVal_bh_completion_time_rank, REO_ARRAY_COUNT(kVal_bh_completion_time_rank),
                   &v)) {
        Reo_Write(0x003B8507, 1, v);
    }
    if (Reo_ChoiceValue("bh_survivor_modifier", kVal_bh_survivor_modifier, REO_ARRAY_COUNT(kVal_bh_survivor_modifier), &v)) {
        Reo_Write(0x003B84F6, 1, v);
    }
}

void Reo_Data_Frame(void) {
    u32 armax = Reo_MasterArmax();
    u32 cb = Reo_MasterCodeBreaker();
    u32 gs = Reo_MasterGameShark();
    u32 game = Reo_GameBinLoaded();

    Reo_Player1(armax, cb, gs, Reo_P1Ready(), Reo_Pad(REO_PAD));
    Reo_Scenario(gs, game);
    if (Reo_SaveReady()) {
        Reo_SaveData(armax, cb, gs);
    }
}
