"""The single list every generated file of REO_Cheats comes from (tools/gen_manifests.py): one entry per option, in the
order of the owner's regular cheat list (its groups), with the owner's device code(s) (verbatim, from owner_codes.py),
the plain pnach form, the status on this disc and its evidence.

Status values:
  WORKS   works as written: the code already targets this disc's layout (verified).
  ADAPTED adapted to your disc: moved only to a proven equivalent (the same instruction or game variable on this disc,
          effect verified in a probe of the game or proven by the game's own code).
  SUBST   not decodable, substitute from the name: the owner's code could not be decoded and has no plain form, so
          what it writes is not known and no equivalent can be proven; the option does what the cheat's name says,
          with only valid data from the game's own tables. Not a proven equivalent, so not counted as adapted.
  NOT     not working on your disc: the reason is given; the option does nothing.
  MASTER  a master code (device hook): the switch that enables its device's cheats; no hook is written.
  PARAM   a value the cheat above it uses (not a cheat of its own).
  LEGACY  a switch kept for a saved setting of an older version of this mod (with the meaning it had there).

Masters: 'armax' = (M) Must Be On by Codejunkies; 'cb' = Enable Code (Must Be On) by Code Master et al.; 'gs' = any of
the MadCatz GameShark master codes ([M] Must Be On, Alternate [M] Must Be On, Must Be On)."""

# The runs/files named in the evidence are in the verification folder of this version (see README, "Testing").

WORKS, ADAPTED, SUBST, NOT, MASTER, PARAM, LEGACY = 'works', 'adapted', 'subst', 'not', 'master', 'param', 'legacy'

CM = 'Code Master, Lajos Szalay, Jay007, VirusPunk, Jarnold83'


def E(name, author='', nth=0):
    """A reference to an entry of the owner's list (owner_codes.ENTRIES): name, author prefix, occurrence."""
    return (name, author, nth)


def opt(key, group, label, master, status, what, evidence, forms=(), pnach=(), kind='bool', choices=None,
        default=False, save='No.', vmin=None, vmax=None, note='', count=True):
    return dict(key=key, group=group, label=label, master=master, status=status, what=what, evidence=evidence,
                forms=list(forms), pnach=list(pnach), kind=kind, choices=choices, default=default, save=save,
                min=vmin, max=vmax, note=note, count=count)


# ---- choice value lists (label, value) -------------------------------------------------------------------------------

CHAR_TYPES = [('00 = Kevin', 0), ('01 = Mark', 1), ('02 = Jim', 2), ('03 = George', 3), ('04 = David', 4),
              ('05 = Alyssa', 5), ('06 = Yoko', 6), ('07 = Cindy', 7)]

# bungholio's list for Player 1 Character Model Modifier, without the entries he marks "CANNOT LOAD" and the empty 0050.
_MODELS = """0000 - Normal|0001 - Mac|0002 - Rodrigez|0003 - Conrad|0004 - Hunk:B|0005 - Hunk|0006 - Miguel|0007 - "UNFINISHED CHARACTER"|0008 - U.S.S.1|000a - Arnold|000b - Matt|000c - Billy|000d - Hursh|000e - "DOCTOR"|0011 - Peter|0012 - Marvin|0013 - Fred|0014 - Andy|0016 - Jean|0017 - Tonny|0018 - "INJURED COP"|0019 - Keeper1|001a - Keeper2|001b - Austin|001c - Clint|001d - Bone|001e - Bob|001f - "BLOODY GUY"|0020 - Nathan|0021 - Samuel|0023 - Will|0024 - "ZOMBIE WILL?"|0025 - Roger|0027 - Carter|0028 - Greg|0029 - Scholar1|002a - Scholar2|002b - Jake|002c - Gary|002d - Man9|002f - Micky|0030 - Al|0031 - Maskman|0032 - Al:B|0033 - Ben|0034 - "LITTLE GIRL"|0035 - Regan|0036 - Regan:B|0037 - Monica|0038 - Rinda|0039 - Rita|003b - Mary|003c - Kate|003f - Danny|0040 - Danny:B|0041 - Gill|0042 - Gill:B|0046 - "BALD DOCTOR"|0049 - "CINDY"|004a - Doctor4|0051 - Kurt|0052 - Kurt:B"""
MODELS = [(s, int(s[:4], 16)) for s in _MODELS.split('|')]

STATUS = [('00 - Fine, when knocked down you keep looping the falling down animation forever', 0x00),
          ('01 - Poison, same looping', 0x01), ('02 - Bleeding, same looping', 0x02),
          ('03 - Bleeding again?, same looping', 0x03), ('04 - Fine, same looping', 0x04),
          ('05 - poison, the game skipped the picking me up animation', 0x05), ('06 - bleed, same', 0x06),
          ('07 - bleed, same', 0x07), ("08 - fine, dying animation keeps repeating when you're crawling", 0x08),
          ('09 - poison, same', 0x09), ('0C - fine, same dying animation loop', 0x0C),
          ('10 - Fine, knocked down skips to crawling, the AI ignores you, dying loops forever', 0x10),
          ('14 - fine', 0x14), ('18 - fine', 0x18), ('1c - fine', 0x1C),
          ("20 - fine, couldn't access start menu", 0x20), ("24 - fine, couldn't access start menu", 0x24),
          ('28 - (no description)', 0x28), ("ff - instantly fell to the floor and couldn't move", 0xFF)]

SPEED1 = [('3FF00000 - Super Slow', 0x3FF00000), ('40000000 - Slow', 0x40000000), ('40400000 - Medium', 0x40400000),
          ('40800000 - Fast', 0x40800000), ('4FFFFFFF - Super Fast, you can go through walls even', 0x4FFFFFFF)]

SPEED2 = [('0.5 (3F000000)', 0x3F000000), ('1.5 (3FC00000, as Fast Hero)', 0x3FC00000),
          ('2.0 (40000000, as Super Fast Hero)', 0x40000000), ('3.0 (40400000)', 0x40400000),
          ('4.0 (40800000)', 0x40800000)]

DAMAGE = [('x0.5 (3F000000)', 0x3F000000), ('x2 (40000000)', 0x40000000), ('x3 (40400000)', 0x40400000),
          ('x5 (40A00000)', 0x40A00000), ('x10 (41200000)', 0x41200000), ('x100 (42C80000)', 0x42C80000),
          ('4FFFFFFF - the author\'s value: every enemy dies', 0x4FFFFFFF)]

VIRUS2 = [('4FFFFFFF = Virus Gauge at 0% and the cells didn\'t move', 0x4FFFFFFF),
          ('00000001 = About the same, but after a movie it went to .02% and stayed there', 0x00000001)]

ALT_COSTUME = [('00 = Didn\'t notice anything', 0), ('01 = alternative clothes (Kevin: white t-shirt and blue jeans)', 1),
               ('02 (not described by the author)', 2), ('03 (not described by the author)', 3),
               ('04 (not described by the author)', 4), ('05 (not described by the author)', 5)]

PLAYERS = [('1 player', 1), ('2 players', 2), ('3 players (the value in single play)', 3), ('4 players', 4)]
RANK = [('0 - F Rank', 0), ('1 - E Rank', 1), ('2 - D Rank', 2), ('3 - C Rank', 3), ('4 - B Rank', 4),
        ('5 - A Rank', 5), ('6 - S Rank', 6)]
SURVIVORS = [('0 - 0/3', 0), ('1 - 1/3', 1), ('2 - 2/3', 2), ('3 - 3/3', 3)]
BEST_POINTS = [("0 - result points aren't a new best record", 0x00), ('ff - result points are a new best record', 0xFF)]
BEST_TIME = [("0 - play time isn't a new best record", 0x00), ('ff - play time is a new best record', 0xFF)]
CB_HEALTH = [('On (16-bit store: HP 9999, max HP kept)', 1), ('On as written (32-bit store: HP 9999, max HP 0)', 2)]

G_MASTER = 'Master Codes'
G_COLL = 'Collection Codes'
G_HEALTH = 'Health Codes'
G_SLOTS = 'Player 1 Item Slot Modifiers'
G_RESULTS = 'Scenario Completion Codes'
G_SINGLE = 'Single Play Codes'
G_SPEED = 'Speed Codes'
G_COSTUME = 'Unlock Costume Codes'
G_OTHER = 'Other Codes'
G_KEPT = 'Kept from older versions'

HOOK_NOTE = ('No hook is written: the recompiled game has no cheat device, and writing a hook into the game\'s code '
             'would take it out of native execution. This switch enables the cheats of its device instead.')

OPTIONS = [
    # ---------------------------------------------------------------------------------------------------------- masters
    opt('master_armax_codejunkies', G_MASTER, 'Master Code (Action Replay MAX): (M) Must Be On by Codejunkies',
        'none', MASTER,
        'Enables the Codejunkies cheats (Health Codes, Speed Codes). ' + HOOK_NOTE,
        'Decrypted here (the DES layer: every line passes its parity check and the code CRC matches; game id '
        '0x059B, code id 0x17B68, master flag set). Its values decode with the fixed byte transform that turns '
        'every Codejunkies code of your list into its pnach line (42 of 42 lines): j 0x00239368 (a jump into the '
        'code table the Speed/Health codes fill), j 0x001BA16C (back into the game), lui at,0x0031 and two data '
        'words. The hook address itself sits in the address layer, which was not decoded.',
        forms=[E('(M) Must Be On', 'Codejunkies')], default=True, count=False),
    opt('cj_armax_below_314_fix', G_MASTER, 'AR Max Below 3.14 Fix by Codejunkies', 'armax', NOT,
        'Nothing: this is a firmware fix for Action Replay MAX devices older than 3.14.',
        'Decrypted: its five lines are exactly the pnach lines (2011CD00 3C03200F ... 2011CD14 0000000C). They '
        'rewrite the executable\'s own code at 0x0011CD00 (on your disc bnez v0 / move a1,s0 / jal 0x00116848 / '
        'b 0x0011CDA4) with a system call the old device firmware needed. There is no device here, and the '
        'recompiled executable never runs rewritten code, so it has nothing to do and the option does nothing.',
        forms=[E('AR Max Below 3.14 Fix', 'Codejunkies')], pnach=['AR Max Below 3.14 Fix'], count=False),
    opt('master_codebreaker_codemaster', G_MASTER,
        'Master Code (CodeBreaker v7+): Enable Code (Must Be On) by Code Master, Lajos Szalay, Jay007, VirusPunk, '
        'Jarnold83', 'none', MASTER,
        'Enables the Code Master (CodeBreaker) cheats. ' + HOOK_NOTE,
        'Not decoded: CodeBreaker v7 encryption needs 1,280 bytes of fixed seed tables that are only in the public '
        'tools\' source files, which were not downloaded.',
        forms=[E('Enable Code (Must Be On)', 'Code Master')], default=True, count=False),
    opt('master_gameshark_madcatz', G_MASTER, 'Master Code (GameShark v3-4 / Xploder v4): [M] Must Be On by MadCatz',
        'none', MASTER,
        'Enables the MadCatz and bungholio (GameShark) cheats; any of the three GameShark master codes does. '
        + HOOK_NOTE,
        'Decoded with the GameShark v3 key-2 decoder: 94D0B9FE B46E0F4E = 9012D460 0C04939E, bit for bit the pnach\'s '
        '"Must Be On" by MadCatz. A type-9 hook on the jal 0x00124E78 at 0x0012D460, which your disc has.',
        forms=[E('[M] Must Be On', 'MadCatz')], pnach=['Must Be On'], default=True, count=False),
    opt('master_gameshark_madcatz_alternate', G_MASTER,
        'Master Code (GameShark v3-4 / Xploder v4): Alternate [M] Must Be On by MadCatz', 'none', MASTER,
        'Enables the MadCatz and bungholio (GameShark) cheats, like [M] Must Be On. ' + HOOK_NOTE,
        'Decoded (GameShark v3 key 2): 94D03AFA BDEE5344 = 9013FC80 0C041EAC, the pnach\'s "Alternate [M] Must Be On". '
        'A hook on the jal 0x00107AB0 at 0x0013FC80, which your disc has.',
        forms=[E('Alternate [M] Must Be On', 'MadCatz')], pnach=['Alternate [M] Must Be On'], count=False),
    opt('master_gameshark_madcatz_must_be_on', G_MASTER,
        'Master Code (GameShark v3-4 / Xploder v4): Must Be On by MadCatz', 'none', MASTER,
        'Enables the MadCatz and bungholio (GameShark) cheats, like [M] Must Be On. Your list has it twice, with '
        'and without its two extra lines: one master code. ' + HOOK_NOTE,
        'Not decoded: its lines use GameShark v3 keys 3 and 4, and only key 2 was reconstructed here. The pnach '
        'has one raw "Must Be On" by MadCatz, the hook 9012D460 0C04939E.',
        forms=[E('Must Be On', 'MadCatz', 0), E('Must Be On', 'MadCatz', 1)], count=False),

    # ------------------------------------------------------------------------------------------------ collection codes
    opt('cb_have_all_collection_available', G_COLL, 'Have All Collection Available For Purchase', 'cb', ADAPTED,
        'Every collection item can be bought: the "available" bits of all 172 collection items (save data '
        '0x00323BF4, six words) are set.',
        'Regular address 0x00323274 + 0x980 (the save block of your disc starts 0x980 higher; your disc\'s demo.bin '
        'reads this bitset at 0x0057C4F0). Only the bits of items that exist (the ids in the game\'s five collection '
        'tables) are set, not all 192. Probe m_coll_avail_mask: every tab shows every item with its price '
        '(sheet_coll_avail.png).',
        forms=[E('Have All Collection Available For Purchase', 'Code Master')],
        pnach=['Collection Codes\\Have All Collection Available For Purchase'],
        save='Yes: written to the save and kept when the game saves; the bits of real items only.'),
    opt('cb_have_all_collection_purchased', G_COLL, 'Have All Collection Purchased', 'cb', ADAPTED,
        'Every collection item shows as owned ("You already have this"): the "owned" bits of all collection items '
        '(0x00323C54, six words).',
        'Regular 0x003232D4 + 0x980. Only the bits of items that exist are set. Probe m_coll_owned_mask: every tab '
        'shows "You already have this" (sheet_coll_opened_owned.png, lower row). The game then applies owned '
        'costumes, NPCs and extra modes itself, as after a purchase.',
        forms=[E('Have All Collection Purchased', 'Code Master')],
        pnach=['Collection Codes\\Have All Collection Purchased'],
        save='Yes: kept when the game saves; the bits of real items only.'),
    opt('cb_infinite_reward_points', G_COLL, 'Infinite Reward Points', 'cb', ADAPTED,
        'The collection points are held at xx,x65,535 (the low 16 bits of the points word set to 0xFFFF).',
        'Regular 0x0031F1E0 + 0x980 = 0x0031FB60, the points word. Probe m_coll_owned_mask: the collection shows '
        '65535 Pts. Never written when the result would be above 99,999,999 (the display maximum).',
        forms=[E('Infinite Reward Points', 'Code Master')], pnach=['Collection Codes\\Infinite Reward Points'],
        save='Yes: the points are saved.'),
    opt('cb_infinite_rewards_points_usage', G_COLL, 'Infinite Rewards Points Usage', 'cb', NOT,
        'Nothing.',
        'Its guard (the halfword 0x0833 at 0x0057ADF4) occurs nowhere in your disc\'s demo.bin (searched), so the '
        'place it patches cannot be found. Its first write happens to land on the points subtraction '
        '(0x0057AE08 subu a0,a0,a1), but its second write would turn sw a0,0xc(s0) into a branch. Not applied.',
        forms=[E('Infinite Rewards Points Usage', 'Code Master')],
        pnach=['Collection Codes\\Infinite Rewards Points Usage']),
    opt('cb_max_reward_points', G_COLL, 'Max Reward Points', 'cb', ADAPTED,
        'The collection points are set to 99,999,999.',
        'Regular 0x0031F1E0 + 0x980 = 0x0031FB60. The same word and value as probe m1 of the cheat analysis '
        '(RESULT 99999999 Pts). 99,999,999 is the display maximum.',
        forms=[E('Max Reward Points', 'Code Master')], pnach=['Collection Codes\\Max Reward Points'],
        save='Yes: the points are saved.'),

    # ---------------------------------------------------------------------------------------------------- health codes
    opt('infinite_health', G_HEALTH, 'Infinite Health', 'armax', ADAPTED,
        'Player 1\'s HP is kept at Player 1\'s max HP (what the installed code does: lh max HP / sh HP).',
        'The installed code (decoded, the same as the pnach lines) reads 0x004A60F6 and writes 0x004A60F4; the '
        'Player 1 block is 0x80 higher on your disc (HP 0x004A6174, max HP 0x004A6176). Probe reg_health (1.1.0): '
        'Kevin hit 12 times, back to 2300/2300 each time.',
        forms=[E('Infinite Health', 'Codejunkies')], pnach=['Health Codes\\Infinite Health']),
    opt('cj_infinite_health_max_health', G_HEALTH, 'Infinite Health & Max Health (Never Bleed)', 'armax', ADAPTED,
        'Player 1\'s HP and max HP are both held at 9999.',
        'Installed code: li v0,9999 / sh HP / sh max HP at 0x004A60F4/F6, +0x80 = 0x004A6174/76. Probe g_combo: '
        '9999/9999 held through the zombie phase (Kevin was bitten; without the cheat his HP drops to 1055).',
        forms=[E('Infinite Health & Max Health (Never Bleed)', 'Codejunkies')],
        pnach=['Health Codes\\Infinite Health & Max Health (Never Bleed)']),
]

# ------------------------------------------------------------------------------------------------ item slot modifiers
SLOTS = [('bh_p1_item_slot_1', 'Player 1 Item Slot 1', 0x004A68B4),
         ('bh_p1_item_slot_2', 'Player 1 Item Slot 2', 0x004A68B5),
         ('bh_p1_item_slot_3', 'Player 1 Item Slot 3', 0x004A68B6),
         ('bh_p1_item_slot_4', 'Player 1 Item Slot 4', 0x004A68B7),
         ('bh_p1_special_item_slot', 'Player 1 Special Item Slot', 0x004A68B8),
         ('bh_p1_yoko_item_slot_5', 'Player 1 Yoko Item Slot 5', 0x004A68B9),
         ('bh_p1_yoko_item_slot_6', 'Player 1 Yoko Item Slot 6', 0x004A68BA),
         ('bh_p1_yoko_item_slot_7', 'Player 1 Yoko Item Slot 7', 0x004A68BB),
         ('bh_p1_yoko_item_slot_8', 'Player 1 Yoko Item Slot 8', 0x004A68BC)]

OPTIONS.append(opt(
    'bh_item_values_table', G_SLOTS, 'Item Values table (for the Player 1 Item Slot codes)', 'none', PARAM,
    'Which of your "Item Values" tables (by nobody) the item slot options look their item up in: pick the scenario '
    'and difficulty you play. The slot value is the item\'s number in that table.',
    'Your tables are used as written. The item numbers are the game\'s item records of the scenario (probe '
    'g_giant_slots: in Outbreak on Normal, 0x42 gave a Shotgun (7) and 0x39 a Magnum Revolver (6), as your '
    '"Outbreak - Normal" table says). The scenario and difficulty are not read from memory: no address for them '
    'was proven, so you pick the table.',
    kind='choice', choices='ITEM_TABLES', default='Outbreak - Normal', count=False))
for key, name, addr in SLOTS:
    OPTIONS.append(opt(
        key, G_SLOTS, name, 'gs', WORKS,
        f'Holds the item you pick in this slot (byte 0x{addr:08X}), like the code\'s ?? value: the mod writes the '
        'number the picked item has in the chosen Item Values table. An item that is not in that table leaves the '
        'slot alone. "Past the table +N" are the numbers after the table: your list\'s note says those are the '
        'characters\' own items (in Outbreak on Normal, +0 is "45 Auto for Kevin").',
        f'0x{addr:08X} is Player 1\'s block (0x004A5C30) + 0x{addr - 0x004A5C30:X}, your disc\'s own item slots '
        '(game.bin reads and writes them, e.g. lbu a1,0xc84(v1)). Probe g_giant_slots: slot 1 = 0x42 and slot 2 = '
        '0x39 showed a Shotgun (7) and a Magnum Revolver (6) in Kevin\'s inventory; the Special slot held 0x51, '
        '"45 Auto for Kevin" (sheet_giant_slots.png).',
        forms=[E(name, 'bungholio')], pnach=['Player 1 Item Slot Modifiers\\' + name], kind='choice',
        choices='ITEMS', default='Off', note='The slot is held while the option is on: you cannot drop or use up '
        'that slot\'s item until you turn it off.'))

OPTIONS += [
    # ---------------------------------------------------------------------------------------- scenario completion codes
    opt('bh_completed_events_1', G_RESULTS, 'Completed Events Modifier 1 Of 2', 'gs', WORKS,
        'The first word of the scenario\'s completed-events bits (0x003B84F8) is held at the value below.',
        'Your disc\'s own events word: submain sets bit N of 0x003B84F8/0x003B84FC for event N (0x0037C470). '
        'Only visible on the results screen at the end of a scenario; not observed in a probe.',
        forms=[E('Completed Events Modifier 1 Of 2', 'bungholio')],
        pnach=['Scenario Completion Codes\\Completed Events Modifier 1 Of 2'],
        save='Indirect: at the end of a scenario the results (completion ratio) are recorded. The author: all F\'s '
             'probably gives more than a 100% completion ratio.'),
    opt('bh_completed_events_1_value', G_RESULTS, 'Completed Events Modifier 1 Of 2: value', 'none', PARAM,
        'The ???????? value of Completed Events Modifier 1 Of 2 (bits of completed events). Author: "Just set both '
        'of them to all F\'s to have all events completed and probably get more than a 100% completion ratio".',
        '', kind='int', default=0, vmin=0, vmax=0xFFFFFFFF, count=False),
    opt('bh_completed_events_2', G_RESULTS, 'Completed Events Modifier 2 Of 2', 'gs', WORKS,
        'The second word of the completed-events bits (0x003B84FC) is held at the value below.',
        'As Modifier 1 Of 2 (submain reads it at 0x0037E88C). Not observed in a probe.',
        forms=[E('Completed Events Modifier 2 Of 2', 'bungholio')],
        pnach=['Scenario Completion Codes\\Completed Events Modifier 2 Of 2'],
        save='Indirect, as Modifier 1 Of 2.'),
    opt('bh_completed_events_2_value', G_RESULTS, 'Completed Events Modifier 2 Of 2: value', 'none', PARAM,
        'The ???????? value of Completed Events Modifier 2 Of 2.', '', kind='int', default=0, vmin=0,
        vmax=0xFFFFFFFF, count=False),
    opt('bh_result_points_best_record', G_RESULTS, 'Determines Whether Your Result Points Are A New Best Record',
        'gs', WORKS, 'The results screen\'s "new best record" flag for result points (byte 0x003B8505).',
        'The results code of your disc reads this byte (single.bin 0x00827AD4, game.bin 0x006016E0). Visible only '
        'on the results screen; not observed in a probe.',
        forms=[E('Determines Whether Your Result Points Are A New Best Record', 'bungholio')],
        pnach=['Scenario Completion Codes\\Determines Whether Your Result Points Are A New Best Record'],
        kind='choice', choices=BEST_POINTS, default='Off', save='Indirect: the results decide what is recorded.'),
    opt('bh_completion_time_best_record', G_RESULTS,
        'Determines Whether Your Scenario Completion Time is A New Best Record', 'gs', WORKS,
        'The results screen\'s "new best record" flag for the play time (byte 0x003B8506).',
        'Read by the results code (single.bin 0x00827AAC); reset by submain at 0x0037C518. Not observed in a probe.',
        forms=[E('Determines Whether Your Scenario Completion Time is A New Best Record', 'bungholio')],
        pnach=['Scenario Completion Codes\\Determines Whether Your Scenario Completion Time is A New Best Record'],
        kind='choice', choices=BEST_TIME, default='Off', save='Indirect.'),
    opt('bh_no_damage_clear', G_RESULTS, 'No Damage Clear', 'gs', WORKS,
        'The "damage taken" flag of the scenario (byte 0x003B84F4) is held at 0, so it ends as a no-damage clear.',
        'game.bin sets it when you are hurt (0x00660F4C sb a0,0x84F4); the results code reads it (single.bin '
        '0x00827B64). Not observed in a probe.',
        forms=[E('No Damage Clear', 'bungholio')], pnach=['Scenario Completion Codes\\No Damage Clear'],
        save='Indirect.'),
    opt('bh_no_weapon_clear', G_RESULTS, 'No Weapon Clear', 'gs', WORKS,
        'The "weapon used" flag (byte 0x003B84F5) is held at 0, so it ends as a no-weapon clear.',
        'game.bin sets it when a weapon is used (e.g. 0x0065E7B0 sb v1,0x84F5); the results code reads it (single.bin '
        '0x00827BA4). Not observed in a probe.',
        forms=[E('No Weapon Clear', 'bungholio')], pnach=['Scenario Completion Codes\\No Weapon Clear'],
        save='Indirect.'),
    opt('bh_result_points_modifier', G_RESULTS, 'Result Points Modifier', 'gs', WORKS,
        'The scenario\'s result points (0x003B84B4) are held at the value below.',
        'Read by the results code (single.bin 0x00827E04, game.bin 0x00601990) and submain (0x0037E7EC). Not '
        'observed in a probe.',
        forms=[E('Result Points Modifier', 'bungholio')], pnach=['Scenario Completion Codes\\Result Points Modifier'],
        save='Indirect: the results add the points to your collection points. The value is limited to 99,999,999, '
             'the display maximum.'),
    opt('bh_result_points_modifier_value', G_RESULTS, 'Result Points Modifier: value', 'none', PARAM,
        'The ???????? value of Result Points Modifier (points, 0 to 99,999,999).', '', kind='int', default=0, vmin=0,
        vmax=99999999, count=False),
    opt('bh_completion_time_rank', G_RESULTS, 'Scenario Completion Time Rank Modifier', 'gs', WORKS,
        'The play-time rank of the results (byte 0x003B8507).',
        'Read by the results code (single.bin 0x00827D24) and written by submain (0x0037E0C4..0x0037E168). Not '
        'observed in a probe.',
        forms=[E('Scenario Completion Time Rank Modifier', 'bungholio')],
        pnach=['Scenario Completion Codes\\Scenario Completion Time Rank Modifier'], kind='choice', choices=RANK,
        default='Off', save='Indirect.'),
    opt('bh_survivor_modifier', G_RESULTS, 'Survivor Modifier', 'gs', WORKS,
        'The number of survivors of the results (byte 0x003B84F6).',
        'Written by game.bin at 0x0068EFB4 and read by submain (0x0037D384 ...). Not observed in a probe.',
        forms=[E('Survivor Modifier', 'bungholio')], pnach=['Scenario Completion Codes\\Survivor Modifier'],
        kind='choice', choices=SURVIVORS, default='Off', save='Indirect.'),

    # ----------------------------------------------------------------------------------------------- single play codes
    opt('mc_infinite_ammo_all_weapons', G_SINGLE, 'Infinite Ammo (All Weapons)', 'gs', WORKS,
        'Firing does not use up rounds: the count stays (the "count - 1" at 0x005B2008 becomes "count - 0").',
        'Written for your disc: 0x005B2008 holds addiu v0,a0,-1 (the new round count) and the code makes it '
        'addiu v0,a0,0. Probe ammo_madcatz (cheat analysis): 7 rounds stay 7. The colon form in your list '
        '(Single Play Codes: Infinite: Ammo (All Weapons), 205B1FD8) is the original release\'s address: on your disc '
        '0x005B1FD8 is jal 0x005B2590, so as written it would break that call; moved by the +0x30 of this code it '
        'is this same write.',
        forms=[E('Infinite Ammo (All Weapons)', 'MadCatz', 0), E('Infinite Ammo (All Weapons)', 'MadCatz', 1),
               E('Single Play Codes: Infinite: Ammo (All Weapons)', 'MadCatz')],
        pnach=['Single Play Codes\\Infinite Ammo (All Weapons)', 'Single Play Codes: Infinite: Ammo (All Weapons)']),
    opt('mc_infinite_health', G_SINGLE, 'Infinite Health', 'gs', WORKS,
        'Player 1\'s HP and max HP are held at 2300 each (0x004A6174 = 08FC08FC).',
        'Written for your disc (Player 1\'s HP word 0x004A6174). 2300 is Kevin\'s value: as written, another '
        'character also gets HP and max HP 2300. The colon form (204A60F4) is the original release\'s address, '
        '0x80 lower, the same word.',
        forms=[E('Infinite Health', 'MadCatz', 0), E('Infinite Health', 'MadCatz', 1),
               E('Single Play Codes: Infinite: Health', 'MadCatz')],
        pnach=['Single Play Codes\\Infinite Health', 'Single Play Codes: Infinite: Health']),
    opt('mc_max_result_points', G_SINGLE, 'Max Result Points', 'gs', WORKS,
        'The collection points are set to 99,999.',
        'Written for your disc: the points word 0x0031FB60. The colon form (2031F1E0) is the original release\'s '
        'address, 0x980 lower, the same word.',
        forms=[E('Max Result Points', 'MadCatz', 0), E('Max Result Points', 'MadCatz', 1),
               E('Single Play Codes: Max: Result Points', 'MadCatz')],
        pnach=['Single Play Codes\\Max Result Points', 'Single Play Codes: Max: Result Points'],
        save='Yes: the points are saved.'),
    opt('mc_freeze_escape_time_l2', G_SINGLE, 'Press And Hold L2 To Freeze Escape Time', 'gs', ADAPTED,
        'While you hold L2 (and nothing else), the game\'s event timers stop counting down.',
        'The joker (pad halfword 0x002B081C == FEFF) is your disc\'s pad: probe base_a read FEFF there while L2 was '
        'held. The write, 2068C77C 24630000, keeps the original release\'s address: on your disc 0x0068C77C is '
        'addu v1,v1,a0 in the online event-script interpreter, which never runs offline (trace t1). The code\'s '
        'addiu v1,v1,0 replaces the timer countdown addiu v1,v1,-1, which is at 0x0068C7DC on your disc (+0x60, the '
        'move of this function: the Code Master Infinite Time guard 1821 is at 0x0068C71C there and 0x0068C77C '
        'here). Probe g_timer_mc: with that write the timers at 0x004BAD8A/0x004BAD8E stop (0x0544, 0x0D78) '
        'instead of counting down. Released, the original instruction is put back (the name says hold).',
        forms=[E('Press And Hold L2 To Freeze Escape Time', 'MadCatz'),
               E('Infinite Press And Hold L2 To Freeze Escape Time', 'MadCatz')],
        pnach=['Single Play Codes\\Infinite Press And Hold L2 To Freeze Escape Time']),
    opt('mc_ultimate_ammo_code', G_SINGLE, 'Ultimate Ammo Code', 'gs', NOT,
        'Nothing.',
        'It writes sh v0,0x24(s0) (A6020024) to 0x005B1FDC, the original release\'s address of the round-count '
        'store, i.e. the instruction that is already there. On your disc 0x005B1FDC is move a0,s0, the argument of '
        'jal 0x005B2590: as written it would break that call. Moved by +0x30 it lands on 0x005B200C, which already '
        'holds exactly sh v0,0x24(s0): no change. No effect can be made from it.',
        forms=[E('Ultimate Ammo Code', 'MadCatz', 0), E('Ultimate Ammo Code', 'MadCatz', 1)],
        pnach=['Single Play Codes\\Ultimate Ammo Code']),
    opt('unlock_all_scenarios', G_SINGLE, 'Unlock All Levels', 'gs', WORKS,
        'All five scenarios can be selected: the scenario bits of your save (0x00323BD8) are set.',
        'Written for your disc (0x00323BD8, the word the scenario select reads, demo.bin 0x00581C04). The code '
        'writes FFFFFFFF; the game uses bits 0-4 only, so only 0x0000001F is written (save safety), and only once '
        'the game has set your save data up. Probe u1 (cheat analysis): all five scenarios. The colon form '
        '(Single Play Codes: Unlock: Levels, 20323258) is the original release\'s address, 0x980 lower.',
        forms=[E('Unlock All Levels', 'MadCatz', 0), E('Unlock All Levels', 'MadCatz', 1),
               E('Single Play Codes: Unlock: Levels', 'MadCatz')],
        pnach=['Single Play Codes\\Unlock All Levels', 'Single Play Codes: Unlock: Levels'],
        save='Yes: kept when the game saves (a normal unlock); only the five scenario bits.'),
    opt('mc_unlock_entire_collection', G_SINGLE, 'Unlock Entire Collection', 'gs', WORKS,
        'Every collection item shows as owned: the owned bits of all collection items (0x00323C54, six words).',
        'Written for your disc (the owned bitset demo.bin reads at 0x0057C560). The code writes FFFFFFFF; only the '
        'bits of items that exist are set. Probe m_coll_owned_mask: "You already have this" everywhere. The other '
        'form in your list, Unlock: Entire Collection (six 203232xx lines), is the original release\'s address, '
        '0x980 lower: the same six words.',
        forms=[E('Unlock Entire Collection', 'MadCatz', 0), E('Unlock Entire Collection', 'MadCatz', 1),
               E('Unlock: Entire Collection', 'MadCatz')],
        pnach=['Single Play Codes\\Unlock Entire Collection', 'Unlock: Entire Collection'],
        save='Yes: kept when the game saves; the bits of real items only.'),
    opt('mc_unlock_infinity_mode', G_SINGLE, 'Unlock Infinity Mode', 'gs', WORKS,
        'Unlocks the Infinity mode: the extra-mode flags the collection\'s Infinity (item 0xB0) and its neighbour '
        'item 0xAF set (0x0031FB7F bits 0x01 and 0x04).',
        'Written for your disc (0x0031FB7C, four flag bytes). The code writes FFFFFFFF into all four bytes; the '
        'game itself only ever sets 0x0031FB7C = 1 and bits 0x01 / 0x04 of 0x0031FB7F (demo.bin 0x0057C364..84), '
        'so only those two bits are set; 0x0031FB7D/7E are settings and are left alone. Probe m_char_masks: the '
        'character select offers PARTNER MODE: DEFAULT / LONE WOLF MODE (sheet_char.png). The other form, '
        'Unlock: Infinity Mode (2031F1FC), is the original release\'s address.',
        forms=[E('Unlock Infinity Mode', 'MadCatz', 0), E('Unlock Infinity Mode', 'MadCatz', 1),
               E('Unlock: Infinity Mode', 'MadCatz')],
        pnach=['Single Play Codes\\Unlock Infinity Mode', 'Unlock: Infinity Mode'],
        save='Yes: kept when the game saves; two valid bits only.'),
    opt('mc_virus_level_never_goes_up', G_SINGLE, 'Virus Level Never Goes Up', 'gs', ADAPTED,
        'The virus gauge of every character stays at 0 (the gauge update stores 0).',
        'Both forms write 34100000 (li s0,0) to 0x00667DF8, the original release\'s address: on your disc that is '
        'move a0,s1, the argument of a call into single.bin, so as written it would break it. +0x60 (the move of this '
        'function: the regular Don\'t Become A Zombie Over Time guard 0x9F8C is jal 0x00667E30 there, your disc has '
        'jal 0x00667E90 at 0x00667E54) gives 0x00667E58, move a2,s0 in the delay slot of that jal, which the code '
        'replaces so the store after it writes 0. Probe g_combo: all three gauges stay 0 through the zombie phase '
        '(without it: 11330 / 6060 / 8655).',
        forms=[E('Virus Level Never Goes Up', 'MadCatz', 0), E('Virus Level Never Goes Up', 'MadCatz', 1),
               E('Single Play Codes: Virus Level Never Goes Up', 'MadCatz')],
        pnach=['Single Play Codes\\Virus Level Never Goes Up', 'Single Play Codes: Virus Level Never Goes Up']),
    opt('mc_infinite_escape_time', G_SINGLE, 'Single Play Codes: Infinite: Escape Time', 'gs', ADAPTED,
        'The game\'s event timers (the escape countdowns) never count down.',
        'The original release\'s 0x0068C77C (the timer countdown addiu v1,v1,-1 there) is 0x0068C7DC on your disc '
        '(+0x60). Probe g_timer_mc: the timers stop.',
        forms=[E('Single Play Codes: Infinite: Escape Time', 'MadCatz')],
        pnach=['Single Play Codes: Infinite: Escape Time']),

    # ----------------------------------------------------------------------------------------------------- speed codes
    opt('cj_collection_opened', G_SPEED, 'Collection Opened', 'armax', ADAPTED,
        'Every collection item can be bought while this is on (the game\'s "is it available" check always says yes).',
        'Installed code (decoded, = the pnach lines): if the halfword at 0x0057C3E8 is 0x100A, store 0 there, i.e. '
        'replace the movz v0,zero,v1 (0003100A) that ends demo.bin\'s "available" check. Your disc has that '
        'function 0x130 higher: 0x0057C518 (it reads the available bitset 0x00323BF4). Probe m_coll_opened: every '
        'item priced, the save bits untouched (sheet_coll_opened_owned.png, upper row).',
        forms=[E('Collection Opened', 'Codejunkies')], pnach=['Speed Codes\\Collection Opened'],
        save='No: it changes the menu\'s check, nothing is written to the save.'),
    opt('cj_fast_hero', G_SPEED, 'Fast Hero', 'armax', ADAPTED,
        'Player 1 moves faster: two speed factors (0x004A5D20 and 0x004A67F0, normally 1.0) are set to 1.5.',
        'Installed code: sw 1.5 to 0x004A5CA0 and 0x004A6770, +0x80 (the Player 1 block) = 0x004A5D20 and '
        '0x004A67F0. Probe g_speed: 150 units in 50 vblanks instead of 62 (the two factors multiply).',
        forms=[E('Fast Hero', 'Codejunkies')], pnach=['Speed Codes\\Fast Hero']),
    opt('cj_giant_hero', G_SPEED, 'Giant Hero', 'armax', ADAPTED,
        'Player 1 is drawn 1.5 times as big (the three scale factors 0x004A5CE4/E8/EC, normally 1.05).',
        'Installed code: sw 1.5 to 0x004A5C64/68/6C, +0x80 = 0x004A5CE4/E8/EC. Probe g_giant_slots: a bigger Kevin '
        '(sheet_giant_slots.png, top right).',
        forms=[E('Giant Hero', 'Codejunkies')], pnach=['Speed Codes\\Giant Hero']),
    opt('cj_infinite_ammo', G_SPEED, 'Infinite Ammo', 'armax', ADAPTED,
        'Firing does not use up rounds (the round-count store is removed).',
        'Installed code: sw zero to 0x005B1FDC (the count store sh v0,0x24(s0) of the original release), +0x30 = '
        '0x005B200C on your disc, the same site as the Code Master Infinite Ammo. Probe ammo_inf (cheat analysis): '
        '7 stays 7 over 12 shots.',
        forms=[E('Infinite Ammo', 'Codejunkies')], pnach=['Speed Codes\\Infinite Ammo']),
    opt('cj_infinite_time', G_SPEED, 'Infinite Time', 'armax', ADAPTED,
        'The game\'s event timers never count down (their store is removed).',
        'Installed code: sw zero to 0x0068C780 (original release), +0x60 = 0x0068C7E0 sh v1,0xa8(a0), the store of '
        'the timer countdown (it runs every frame in single play: trace t1). Probe g_timers: the timers at '
        '0x004BAD8A/0x004BAD8E stop at 0x0544/0x0D78.',
        forms=[E('Infinite Time', 'Codejunkies')], pnach=['Speed Codes\\Infinite Time']),
    opt('cj_max_collection_pts', G_SPEED, 'Max Collection Pts', 'armax', ADAPTED,
        'The collection points are set to 3,276,800 (the code stores 0x00320000).',
        'Installed code: lui at,0x0032 / sw at,-0xE20(at) = 0x00320000 into 0x0031F1E0, +0x980 = the points word '
        '0x0031FB60.',
        forms=[E('Max Collection Pts', 'Codejunkies')], pnach=['Speed Codes\\Max Collection Pts'],
        save='Yes: the points are saved.'),
    opt('cj_scenarii_opened', G_SPEED, 'Scenarii Opened', 'armax', ADAPTED,
        'All five scenarios can be selected while this is on (the scenario select skips its lock check).',
        'Installed code: sw zero to 0x00581AE0 (original release). Your disc has the scenario select\'s lock check, '
        'beqz v0 after lw v0,0x4078(v0) (the scenario bits), at 0x00581C14 (+0x134, next to the +0x130 of '
        'Collection Opened). Probe m_scen_opened: all five scenarios in the select while the save word stays '
        '0x00000001 (sheet_scen_opened.png).',
        forms=[E('Scenarii Opened', 'Codejunkies')], pnach=['Speed Codes\\Scenarii Opened'],
        save='No: nothing is written to the save.'),
    opt('cj_super_fast_hero', G_SPEED, 'Super Fast Hero', 'armax', ADAPTED,
        'Player 1 moves much faster: the two speed factors are set to 2.0.',
        'As Fast Hero, with 2.0 (lui at,0x4000).',
        forms=[E('Super Fast Hero', 'Codejunkies')], pnach=['Speed Codes\\Super Fast Hero']),
    opt('cj_zero_virus_gauge', G_SPEED, 'Zero Virus Gauge', 'armax', ADAPTED,
        'Player 1\'s virus gauge is held at 0.',
        'Installed code: sw zero to 0x004A675C, +0x80 = 0x004A67DC (Player 1 block + 0xBAC, where game.bin stores the '
        'gauge). Probe gauge_zero (cheat analysis): 0.00 %.',
        forms=[E('Zero Virus Gauge', 'Codejunkies')], pnach=['Speed Codes\\Zero Virus Gauge']),
    opt('cj_zombies_dont_move', G_SPEED, 'Zombies Don\'t Move', 'armax', ADAPTED,
        'Enemies stay where they are (they still attack you when you are next to them).',
        'Installed code: sw zero to 0x006964B4 (original release). +0x60 gives 0x00696514 lbu v0,0xc82(s0) in the '
        'enemy update: without it v0 keeps 1 and the call to the movement routine (jal 0x0065E3A0) is skipped. '
        'Probe g_zombies: the three zombies\' positions stay fixed from 10300 on (without it they walk); Kevin '
        'still got bitten where he walked past them.',
        forms=[E('Zombies Don\'t Move', 'Codejunkies')], pnach=['Speed Codes\\Zombies Don\'t Move']),

    # -------------------------------------------------------------------------------------------- unlock costume codes
    opt('cb_all_costumes', G_COSTUME, 'All Costumes', 'cb', ADAPTED,
        'Every costume the game has can be chosen: Type B for all eight characters, Type C for Alyssa, Yoko and '
        'Cindy.',
        'Regular 0x0031F1E4/E8 + 0x980 = 0x0031FB64/68, one byte per character (bit 0 = Type B, bit 1 = Type C; '
        'demo.bin\'s character select, 0x00584F44). The code writes FFFFFFFF; only the bits the game itself sets '
        '(its costume table, collection items No. 001-011) are set. Probe m_char_masks: "Select A Type"; probe '
        'm_costume_names: the collection lists Type B for all eight and a second new costume for Alyssa, Yoko and '
        'Cindy only.',
        forms=[E('All Costumes', 'Code Master')], pnach=['Unlock Costume Codes\\All Costumes'],
        save='Yes: kept when the game saves; valid bits only.'),
]

CHARS = [('Alyssa', 5), ('Cindy', 7), ('David', 4), ('George', 3), ('Jim', 2), ('Kevin', 0), ('Mark', 1), ('Yoko', 6)]
FEMALE = {5, 6, 7}
for cname, ci in CHARS:
    for suffix, tkey in (('All Types', 'all'), ('Type B', 'b'), ('Type C', 'c')):
        name = f'{cname}-{suffix}'
        key = f'cb_costume_{cname.lower()}_{tkey}'
        forms = [E(name, 'Code Master')]
        pn = ['Unlock Costume Codes\\Yoko-Type C'] if name == 'Yoko-Type C' else []
        undecoded = ('Your code for it is CodeBreaker v7 encrypted and could not be decoded here (the encryption '
                     'needs seed tables that were not available), and your pnach has no plain form of it. ')
        if name == 'Yoko-Type C':
            undecoded = ('Your list gives it as a CodeBreaker v1-6 code, and your pnach\'s plain form 21FDD36C 68BEFB9F '
                         '(a 32-bit write into the stack area at 0x01FDD36C) is what decoding it as v1-6 gives: '
                         'garbage, so it is most likely a CodeBreaker v7 code like its neighbours and was not '
                         'decoded. ')
        if tkey == 'c' and ci not in FEMALE:
            OPTIONS.append(opt(
                key, G_COSTUME, name, 'cb', NOT, 'Nothing.',
                undecoded + f'Your disc\'s game has no Type C costume for {cname}: its costume table (collection items '
                'No. 001-011) unlocks Type C only for Alyssa, Yoko and Cindy, and nothing in the game sets that bit '
                f'for {cname}. Setting it would put a value into your save the game never writes.',
                forms=forms, pnach=pn))
            continue
        if tkey == 'all':
            what = (f'Unlocks {cname}\'s costumes: Type B and Type C.' if ci in FEMALE
                    else f'Unlocks {cname}\'s costumes: Type B (the game has no Type C for {cname}).')
        elif tkey == 'b':
            what = f'Unlocks {cname}\'s Type B costume.'
        else:
            what = f'Unlocks {cname}\'s Type C costume.'
        what += (' This is a substitute taken from the cheat\'s name, not your code: your code could not be decoded, '
                 'so what it writes is not known.')
        OPTIONS.append(opt(
            key, G_COSTUME, name, 'cb', SUBST, what,
            undecoded + 'So what your code writes on your disc is not known and no equivalent of it can be proven '
            '(it is not "adapted to your disc"). The mod does what the cheat\'s name says instead, with only the '
            f'bits the game itself sets: {cname}\'s costume byte is 0x{0x0031FB64 + ci:08X} (0x0031FB64 + character '
            f'{ci}; bit 0 = Type B, bit 1 = Type C, read by the character select at demo.bin 0x00584F44 and set by the '
            'collection purchase at 0x0057C1C4, the same byte All Costumes writes, +0x980 from the original release). '
            'Probe m_char_alyssa_c: with only Alyssa\'s Type C bit set, only Alyssa offers a costume type at the '
            'character select, whose order (Kevin, Mark, Jim, George, David, Alyssa, Yoko, Cindy) is the byte order '
            '(sheet_char_alyssa_c.png).',
            forms=forms, pnach=pn, save='Yes: kept when the game saves; valid bits only.'))

OPTIONS += [
    # ----------------------------------------------------------------------------------------------------- other codes
    opt('one_hit_kills', G_OTHER, '1-Hit Deaths (Enemies)', 'cb', ADAPTED,
        'Any hit kills an enemy.',
        'Guard D0640794 882D and write 206407A0 +0x60: guard 0x006407F4 move s1,a2 (0x00C0882D, the same '
        'instruction), 0x00640800 beq v1,v0 -> sh v0,0x138(s3). Probe one_hit (cheat analysis): hit enemies die '
        'on the first hit.',
        forms=[E('1-Hit Deaths (Enemies)', 'Code Master')], pnach=['1-Hit Deaths (Enemies)']),
    opt('bh_animation_picker', G_OTHER, 'Animation Sequence Picker Player 1', 'gs', WORKS,
        'Player 1\'s animation byte (0x004A67CB) is held at the value below. Author: "Use a joker with it. '
        'Different values made different things happen. With Cindy I made her throw nothing, limp, collapse, walk '
        'backwards, and whatever else. Mostly useless."',
        'Player 1 block + 0xB9B, your disc\'s own field (game.bin: 72 reads, 93 writes, e.g. lbu v0,0xb9b(s0)). '
        'Not observed in a probe.',
        forms=[E('Animation Sequence Picker Player 1', 'bungholio')], pnach=['Animation Sequence Picker Player 1']),
    opt('bh_animation_picker_value', G_OTHER, 'Animation Sequence Picker Player 1: value', 'none', PARAM,
        'The ?? value (0-255) of Animation Sequence Picker Player 1.', '', kind='int', default=0, vmin=0, vmax=255,
        count=False),
    opt('cb_zombie_after_death', G_OTHER, 'Become A Zombie After Death (Offline Mode)', 'cb', ADAPTED,
        'When you die offline you turn into a playable zombie instead of "YOU DIED".',
        'D065FCB5 202D / 1065FCDA 1000: the guard address is odd (a slip); +0x60 and aligned it is 0x0065FD14 '
        'move a0,s1 (0x0220202D). The 16-bit write 0x1000 at 0x0065FD3A (+0x60) makes the bne v0,v1 at 0x0065FD38 '
        'always taken. Probe zombie_after_death (cheat analysis): the game continues with the zombie.',
        forms=[E('Become A Zombie After Death (Offline Mode)', 'Code Master')],
        pnach=['Become A Zombie After Death (Offline Mode)']),
    opt('cb_no_zombie_over_time', G_OTHER, 'Don\'t Become A Zombie Over Time', 'cb', ADAPTED,
        'The virus gauge no longer rises with time (all characters).',
        'D0667DF4 9F8C / 20667DFC 0, +0x60: guard 0x00667E54 jal 0x00667E90 (9FA4: the jal target moved by 0x60 '
        'too), 0x00667E5C sw s0,0xbac(s1) -> nop. Probe no_zombie (cheat analysis): the gauges stay 0.',
        forms=[E('Don\'t Become A Zombie Over Time', 'Code Master')], pnach=['Don\'t Become A Zombie Over Time']),
    opt('cb_no_zombie_when_bitten', G_OTHER, 'Don\'t Become A Zombie When Bitten', 'cb', ADAPTED,
        'Bites no longer raise the virus gauge (all characters).',
        'D06600FC 9FCC / 20660100 0, +0x60: guard 0x0066015C jal 0x00667F90 (9FE4), 0x00660160 sw v0,0xbac(s1) -> '
        'nop. Probe no_zombie (cheat analysis).',
        forms=[E('Don\'t Become A Zombie When Bitten', 'Code Master')], pnach=['Don\'t Become A Zombie When Bitten']),
    opt('bh_enemies_cant_touch', G_OTHER, 'Enemies Can\'t Touch Player 1', 'gs', WORKS,
        'Enemies cannot hit or grab Player 1 (byte 0x004A67D2 = 0x20).',
        'Player 1 block + 0xBA2 (a byte of the flags word game.bin reads with lw 0xba0). Probe g_touch: through the '
        'whole zombie phase Kevin kept 2300 HP and his gauge rose only with time (3030); without it he drops to '
        '1055 HP and the gauge reaches 11330.',
        forms=[E('Enemies Can\'t Touch Player 1', 'bungholio')], pnach=['Enemies Can\'t Touch Player 1']),
    opt('cb_enemies_dont_damage', G_OTHER, 'Enemies Don\'t Damage You With Attacks', 'cb', ADAPTED,
        'Enemy attacks do no HP damage (player and partners); grabs and bites still infect.',
        'D0660AAC 802D / 20660AB8 0, +0x60: guard 0x00660B0C move s0,a0 (0x0080802D), 0x00660B18 beqz v1 -> nop. '
        'Probe no_damage (cheat analysis): all HP unchanged through the zombie phase.',
        forms=[E('Enemies Don\'t Damage You With Attacks', 'Code Master')],
        pnach=['Enemies Don\'t Damage You With Attacks']),
    opt('bh_enemies_dont_notice', G_OTHER,
        'Enemies Don\'t Notice Player 1 (Because you are dead) (L2+UP=ON, L2+DOWN=OFF)', 'gs', WORKS,
        'L2+Up (exactly) sets byte 0x004A67D1 to 1, L2+Down sets it to 0, as written. Author: "WARNING! THIS IS '
        'BUGGY": zombies ignore you, other players don\'t; you cannot open the start menu or fire while it is set; '
        'you die if a movie plays.',
        'The joker address 0x002B081C is your disc\'s pad: probe base_a read FEEF with L2+Up and FEBF with L2+Down '
        'there. 0x004A67D1 is Player 1 block + 0xBA1 (game.bin: lbu 0xba1, 142 reads). The effect was not observed '
        'in a probe.',
        forms=[E('Enemies Don\'t Notice Player 1 (Because you are dead) (L2+UP=ON, L2+DOWN=OFF)', 'bungholio')],
        pnach=['Enemies Don\'t Notice Player 1 (Because you are dead) (L2+UP=ON, L2+DOWN=OFF)']),
    opt('cb_extra_ammo', G_OTHER, 'Extra Ammo', 'cb', ADAPTED,
        'Each shot adds a round instead of using one.',
        'D05B1FC8 1E3C / 105B1FD8 0001, +0x30: guard 0x005B1FF8 dsll32 v1,s2,0x18 (0x1E3C, the same), 16-bit 0x0001 '
        'into 0x005B2008 addiu v0,a0,-1 -> addiu v0,a0,1. Probe ammo_extra (cheat analysis): 7 -> 19 over 12 shots.',
        forms=[E('Extra Ammo', 'Code Master')], pnach=['Extra Ammo']),
    opt('bh_have_all_files', G_OTHER, 'Have All Files', 'gs', WORKS,
        'All 16 files of the current scenario are yours (16-bit 0x004B9C80 = FFFF). Author: they count as completed '
        'events at the end.',
        'Your disc\'s files word: game.bin and submain address 0x004B9C80 (addiu 0x9C80 at 0x00570984, '
        '0x0068E3E0, 0x0037EC20 ...); 0 in J\'s Bar in probe base_a. The effect was not observed in a probe.',
        forms=[E('Have All Files', 'bungholio')], pnach=['Have All Files'],
        save='Indirect: they count as completed events in the results.'),
    opt('infinite_ammo', G_OTHER, 'Infinite Ammo', 'cb', ADAPTED,
        'Firing does not use up rounds.',
        'D05B1FC8 1E3C / 205B1FDC 0, +0x30: guard 0x005B1FF8 (0x1E3C), 0x005B200C sh v0,0x24(s0) -> nop. Probes '
        'ammo_inf and ammo_inf_off (cheat analysis).',
        forms=[E('Infinite Ammo', 'Code Master')], pnach=['Infinite Ammo']),
    opt('cb_infinite_health', G_OTHER, 'Infinite Health', 'cb', ADAPTED,
        'Every character\'s HP is set to 9999 while its death check runs (players and partners).',
        'E0023881 00660794 / 206607A0 2403270F / 206607A8 AE030544, +0x60: 0x00660800 lh v1,0x544(s0) -> li '
        'v1,9999; 0x00660808 nop -> the store. The guard: 0x006607F4 holds lh v1,0x4200(at) on your disc (the '
        'original release has the same load of a save word 0x980 lower, 0x3880); the published 0x3881 is one too '
        'high, so the adapted guard is 0x4200. The code\'s own store is 32-bit (sw): it also sets max HP to 0, and '
        'after turning it off the next hit leaves HP 0 (probe health_fix_off). "On (16-bit store)" writes HP only '
        '(probe health_sh_off: safe on and off). Probe health_fix: HP back to 9999 after every hit.',
        forms=[E('Infinite Health', 'Code Master')], pnach=['Infinite Health'], kind='choice', choices=CB_HEALTH,
        default='Off'),
    opt('infinite_items', G_OTHER, 'Infinite Item Usage', 'cb', ADAPTED,
        'Using a consumable item does not use it up (everyone).',
        'E0031E3D 005B2148 / 205B215C, 205B2170, 205B5184 = 0, +0x30: guard 0x005B2178 dsll32 v1,s2,0x18 = 0x1E3C '
        '(the published 0x1E3D is one too high), 0x005B218C sh v0,0x24(s0), 0x005B21A0 bne v0,v1, 0x005B51B4 move '
        'v0,zero -> nop. Probe items_fix (cheat analysis): Cindy\'s herb stays 1.',
        forms=[E('Infinite Item Usage', 'Code Master')], pnach=['Infinite Item Usage']),
    opt('cb_infinite_time', G_OTHER, 'Infinite Time', 'cb', NOT,
        'Nothing in single play.',
        'D068C71C 1821 / 2068C724 0, +0x60: the guard matches your disc (0x0068C77C addu v1,v1,a0), and the write '
        'removes 0x0068C784 sw v1,(s3), the program-counter store of the online event-script interpreter. Offline, '
        'the game runs another interpreter: that store never ran in 7,300 vblanks of single play (trace t1). Online '
        'play is not available, so there is nothing to apply (patching it would only stop online scripts).',
        forms=[E('Infinite Time', 'Code Master')], pnach=['Infinite Time']),
    opt('mc_reset_escape_time_l2', G_OTHER, 'Infinite: Press L2 To Reset Escape Time', 'gs', ADAPTED,
        'While you hold L2 (and nothing else), the event timers stop counting down.',
        'D02AFE1C FEFF / 2068C77C 24630000 are both the original release\'s addresses. The pad: 0x002AFE1C + 0xA00 '
        '= 0x002B081C, your disc\'s pad halfword (the joker address bungholio\'s codes and MadCatz\' other code use; '
        'probe base_a: FEFF with L2). The write: +0x60 = 0x0068C7DC, the timer countdown (probe g_timer_mc). '
        'Released, the original instruction is put back.',
        forms=[E('Infinite: Press L2 To Reset Escape Time', 'MadCatz')],
        pnach=['Infinite: Press L2 To Reset Escape Time']),
    opt('cb_max_infinite_ammo', G_OTHER, 'Max Infinite Ammo', 'cb', ADAPTED,
        'The loaded rounds drop to 1 and then stay at 1 (not 99).',
        'D05B1FC8 1E3C / 205B1FD8 24030063, +0x30: guard 0x005B1FF8, 0x005B2008 addiu v0,a0,-1 -> li v1,99. The '
        'store after it writes v0, which is 1 there, so the count is held at 1: the code\'s own effect (the same '
        'code on the original release). Probe ammo_max (cheat analysis).',
        forms=[E('Max Infinite Ammo', 'Code Master')], pnach=['Max Infinite Ammo']),
    opt('bh_number_of_players', G_OTHER, 'Number Of Players Present', 'gs', WORKS,
        'The number of players (byte 0x004BAEA0). Author: "Set it to 1 for 1 player, 2 for 2 players, and so on. '
        'I doubt 5 works though ... It\'s basically like controlling 2 of yourself."',
        'Your disc\'s player count: 3 in single play (probe base_a), read by 100+ places in game.bin (lw/lb '
        '-0x5160 from 0x004C0000). The effect was not observed in a probe.',
        forms=[E('Number Of Players Present', 'bungholio')], pnach=['Number Of Players Present'], kind='choice',
        choices=PLAYERS, default='Off'),
    opt('cb_l1_select_infection', G_OTHER, 'P1 Press L1+Select For Infection 100%', 'cb', ADAPTED,
        'L1+Select (exactly) makes the gauge update store a huge value: the gauge goes to 100 % and the character '
        'dies ("YOU DIED", unless Become A Zombie After Death is on). With nothing pressed the original instruction '
        'is put back, as written. It acts on every character whose gauge updates meanwhile.',
        'The pad: 0x002AFE9C + 0xA00 = 0x002B089C, your disc\'s second copy of the pad (probe base_a: FBFE there '
        'with L1+Select). The write: 0x00667DC8 + 0x60 = 0x00667E28, which holds mfc1 s0,$f23 (4410B800), exactly '
        'the code\'s own restore value. Probe g_l1select: Kevin\'s gauge went to 0x24EA0 (100 %), HP 0; Mark\'s too.',
        forms=[E('P1 Press L1+Select For Infection 100%', 'Code Master')],
        pnach=['P1 Press L1+Select For Infection 100%']),
    opt('bh_p1_alt_costume', G_OTHER, 'Player 1 Alternative Costume Modifier', 'gs', WORKS,
        'Player 1\'s alternative-costume byte (0x004A67EC). Author: "There\'s probably a few more higher values, but '
        'I doubt it goes above 5."',
        'Player 1 block + 0xBBC (game.bin: lbu/sb 0xbbc). 0 in J\'s Bar (probe base_a). Not observed in a probe.',
        forms=[E('Player 1 Alternative Costume Modifier', 'bungholio')], pnach=['Player 1 Alternative Costume Modifier'],
        kind='choice', choices=ALT_COSTUME, default='Off'),
    opt('bh_p1_model', G_OTHER, 'Player 1 Character Model Modifier', 'gs', WORKS,
        'Player 1\'s model (16-bit 0x004A67E4). Author: "this only modifies your character\'s appearance, you\'ll '
        'still sound like and have the same animations of the player you pick." The entries he marks "CANNOT LOAD" '
        '(0009, 000f, 0010, 0015, 0022, 0026, 002e, 003a, 003d, 003e, 0043-0045, 0047, 0048, 004b-004f) and the '
        'empty 0050 are left out.',
        'Player 1 block + 0xBB4 (game.bin: lhu 0xbb4, 75 reads). 0 in J\'s Bar (probe base_a). Not observed in a '
        'probe.',
        forms=[E('Player 1 Character Model Modifier', 'bungholio')], pnach=['Player 1 Character Model Modifier'],
        kind='choice', choices=MODELS, default='Off'),
    opt('bh_p1_char_type', G_OTHER, 'Player 1 Character Type Modifier', 'gs', WORKS,
        'Player 1\'s character (byte 0x004A67C8). Author: "08 or higher = don\'t try it, they don\'t exist so the '
        'game won\'t start": only 00-07 are offered.',
        'Player 1 block + 0xB98 (game.bin: lbu 0xb98, 707 reads; it indexes the gauge maximum table 0x0071ADB0, '
        'Kevin = 0). 0 with Kevin in probe base_a. Not observed in a probe.',
        forms=[E('Player 1 Character Type Modifier', 'bungholio')], pnach=['Player 1 Character Type Modifier'],
        kind='choice', choices=CHAR_TYPES, default='Off'),
    opt('bh_p1_damage', G_OTHER, 'Player 1 Damage Modifier [Or is It Multiplier?]', 'gs', WORKS,
        'Player 1\'s damage multiplier (float 0x004A67F4, normally 1.0). Author: "I set it to 4FFFFFFF and every '
        'enemy died no matter how I hit them ... You can\'t use this to open doors in 1 hit though".',
        'Player 1 block + 0xBC4 (game.bin: lwc1 0xbc4): 1.0 in probe base_a, so it is a multiplier. Probe g_combo: '
        'with 2.0 Kevin\'s hits took 20 HP instead of 10. Probe damage_mod (cheat analysis): 4FFFFFFF kills.',
        forms=[E('Player 1 Damage Modifier [Or is It Multiplier?]', 'bungholio')],
        pnach=['Player 1 Damage Modifier [Or is It Multiplier?]'], kind='choice', choices=DAMAGE, default='Off'),
    opt('bh_p1_speed_1', G_OTHER, 'Player 1 Speed Modifier #1', 'gs', WORKS,
        'Player 1\'s speed value #1 (float 0x004A67D8, normally 1.0). Author: "If you turn while moving you will '
        'move at normal speed."',
        'Player 1 block + 0xBA8 (game.bin: lwc1 0xba8, 186 reads). 1.0 in probe base_a. The values are the '
        'author\'s. Not observed in a probe.',
        forms=[E('Player 1 Speed Modifier #1', 'bungholio')], pnach=['Player 1 Speed Modifier #1'], kind='choice',
        choices=SPEED1, default='Off'),
    opt('bh_p1_speed_2', G_OTHER, 'Player 1 Speed Modifier #2', 'gs', WORKS,
        'Player 1\'s speed factor #2 (float 0x004A67F0, normally 1.0). Author: "Also a speed code, but you don\'t '
        'move at normal speed while turning."',
        'Player 1 block + 0xBC0: 1.0 in probe base_a; it is the second word Codejunkies\' Fast Hero sets to 1.5 '
        '(probe g_speed: faster), so it is a speed multiplier and the values are multipliers.',
        forms=[E('Player 1 Speed Modifier #2', 'bungholio')], pnach=['Player 1 Speed Modifier #2'], kind='choice',
        choices=SPEED2, default='Off'),
    opt('bh_p1_status', G_OTHER, 'Player 1 Status Modifier', 'gs', WORKS,
        'Player 1\'s status byte (0x004A67D0). Author: "Some of them even killed me instantly, but I don\'t '
        'remember which ones. It\'s useless."',
        'Player 1 block + 0xBA0 (game.bin: 614 lw / 287 sw of the word). 0 in J\'s Bar (probe base_a). Not observed '
        'in a probe.',
        forms=[E('Player 1 Status Modifier', 'bungholio')], pnach=['Player 1 Status Modifier'], kind='choice',
        choices=STATUS, default='Off'),
    opt('bh_p1_virus_gauge_1', G_OTHER, 'Player 1 Virus Gauge Modifier #1', 'gs', WORKS,
        'Player 1\'s virus gauge (0x004A67DC) is held at the percentage below, computed from the game\'s own maximum '
        'for the character. Author: "this forces your virus gauge to 0 always" (with 0).',
        'Player 1 block + 0xBAC, where game.bin stores the gauge (sw s0,0xbac(s1) at 0x00667E5C). The maximum per '
        'character is the game\'s table at 0x0071ADB0 (Kevin 151200); 100 % is the death threshold (probe '
        'virus_death_base of the cheat analysis: "YOU DIED"), so at most 99 % is offered. Probes gauge_zero / '
        'gauge_99: 0.00 % and 99.00 % held.',
        forms=[E('Player 1 Virus Gauge Modifier #1', 'bungholio')], pnach=['Player 1 Virus Gauge Modifier #1']),
    opt('bh_p1_virus_gauge_1_value', G_OTHER, 'Player 1 Virus Gauge Modifier #1: value (%)', 'none', PARAM,
        'The gauge value for Player 1 Virus Gauge Modifier #1, in percent of the character\'s maximum (0-99; '
        '100 % kills the character, so it is not offered).', '', kind='int', default=0, vmin=0, vmax=99,
        count=False),
    opt('bh_p1_virus_gauge_2', G_OTHER, 'Player 1 Virus Gauge Modifier #2', 'gs', WORKS,
        'Player 1\'s virus word #2 (0x004A67E8) is held at the value you pick. Author: "I think it stops the virus '
        'gauge from increasing ... but it\'s still useless."',
        'Player 1 block + 0xBB8 (game.bin: lhu/sh 0xbb8). 0 in J\'s Bar (probe base_a). The values are the author\'s. '
        'Not observed in a probe.',
        forms=[E('Player 1 Virus Gauge Modifier #2', 'bungholio')], pnach=['Player 1 Virus Gauge Modifier #2'],
        kind='choice', choices=VIRUS2, default='Off'),
    opt('bh_walk_through_walls', G_OTHER, 'Player 1 Walk Through Walls', 'gs', WORKS,
        'Player 1 walks through walls (0x004A68E0 and 0x004A68FC = FFFFFFFF). Author: if a room keeps pushing you '
        'back out of the door you came in, run the other way when you enter.',
        'Player 1 block + 0xCB0 / 0xCCC. Probe walls_data (cheat analysis): Kevin passes the wall that stops him '
        'at x = 7947.',
        forms=[E('Player 1 Walk Through Walls', 'bungholio')], pnach=['Player 1 Walk Through Walls']),
    opt('bh_rapid_fire', G_OTHER, 'Rapid Fire Player 1', 'gs', WORKS,
        'While you hold R1+Cross (exactly), Player 1 fires continuously (byte 0x004A67D3 = FF).',
        'The joker 0x002B081C == B7FF is your disc\'s pad (probe base_a: B7FF with R1+Cross). 0x004A67D3 is Player 1 '
        'block + 0xBA3 (game.bin: 154 sb / 173 lbu). Probe g_rapid: with FF there the whole magazine (7 rounds) '
        'went within 20 vblanks of aiming; without it one round per press.',
        forms=[E('Rapid Fire Player 1', 'bungholio')], pnach=['Rapid Fire Player 1']),
    opt('cb_unlock_all_npcs', G_OTHER, 'Unlock All NPC\'s', 'cb', ADAPTED,
        'The extra (NPC) characters can be chosen at the character select.',
        'Regular 0x0031F1EC (three words) + 0x980 = 0x0031FB6C, the NPC bits the character select reads (demo.bin '
        '0x00584ED0, 128 bits). The code writes FFFFFFFF; only the 40 bits the game itself sets (its collection '
        'table) are set. Probe m_char_masks: an extra character in the select (sheet_char.png).',
        forms=[E('Unlock All NPC\'s', 'Code Master')], pnach=['Unlock All NPC\'s'],
        save='Yes: kept when the game saves; valid bits only.'),
    opt('cb_unlock_all_scenarios', G_OTHER, 'Unlock All Scenarios', 'cb', NOT,
        'Nothing. (MadCatz\' Unlock All Levels above does unlock all scenarios.)',
        'It writes 0x00323260 on the original release; +0x980 (the shift of every save code) that is 0x00323BE0 on '
        'your disc, 8 bytes past the scenario word 0x00323BD8 (MadCatz\' code for the same thing writes 0x00323258 '
        '= 0x00323BD8 - 0x980). The scenario select reads 0x00323BD8 only (bits 0-4), so this word does nothing, '
        'and writing FFFFFFFF into an unused save word is not safe. Not applied.',
        forms=[E('Unlock All Scenarios', 'Code Master')], pnach=['Unlock All Scenarios']),
    opt('cb_unlock_infinity_mode', G_OTHER, 'Unlock Infinity Mode', 'cb', ADAPTED,
        'Unlocks the Infinity mode (0x0031FB7F bits 0x01 and 0x04, see MadCatz\' Unlock Infinity Mode).',
        'Regular 0x0031F1FC + 0x980 = 0x0031FB7C. Valid bits only, as MadCatz\' code. Probe m_char_masks.',
        forms=[E('Unlock Infinity Mode', 'Code Master')], pnach=['Unlock Infinity Mode'],
        save='Yes: kept when the game saves; two valid bits only.'),

    # ---------------------------------------------------------------------------------------------- kept for settings
    opt('no_infection', G_KEPT, 'No Infection / Freeze Infection', 'cb', LEGACY,
        'Your saved switch from 1.0/1.1, with the meaning it had in 1.1.0: turns on Don\'t Become A Zombie Over Time '
        'and When Bitten together (the virus gauge can no longer rise), and with Infection Freeze Value 0 (below, '
        'the default) and the Action Replay MAX master code On it also holds Player 1\'s virus gauge at 0 '
        '(Codejunkies\' Zero Virus Gauge). With another freeze value the gauge stays where it is.',
        'The two Code Master codes and the Codejunkies code above, each of which also has its own option; the same '
        'sites and word (0x00667E5C, 0x00660160, 0x004A67DC = 0) as 1.1.0 (simulator: the owner\'s saved settings '
        'change the same words in 1.1.0 and this version). The gauge is written only while Player 1 is set up in a '
        'scenario, like every Player 1 cheat of this version (1.1.0 wrote it in every state, also where the Player 1 '
        'block is not set up).', count=False),
    opt('infection_freeze_value', G_KEPT, 'Infection Freeze Value (%)', 'none', LEGACY,
        'Your saved value from 1.0/1.1, with the meaning it had in 1.1.0: with No Infection / Freeze Infection On, '
        '0 also holds the virus gauge at 0 (Codejunkies\' Zero Virus Gauge; needs the Action Replay MAX and the '
        'CodeBreaker master code). 1-100: the gauge stays where it is (the two Don\'t Become A Zombie codes stop it '
        'rising). To hold the gauge at a chosen value use Player 1 Virus Gauge Modifier #1 and its own value above.',
        '', kind='int', default=0, vmin=0, vmax=100, count=False),
    opt('max_inventory', G_KEPT, 'Max Inventory', 'none', LEGACY,
        'Does nothing: there is no such code in your list. Kept so your saved setting stays valid.', '',
        count=False),
]

# ---- code-patch sites ------------------------------------------------------------------------------------------------
# Every word of game code the mod can write, on the owner's disc. The mod writes a site only while all its guard words
# hold (the overlay is the one the code was made for) and the site holds its original word or one of its replacements;
# the first replacement whose condition is on wins; with none on, the original word is put back. patches_sites.json
# lists the same sites for the build (the game's switchable sites).
#   kind: the site kind of the build's feature mechanism (docs/FEATURES.md): subst, substAccess, branchNever,
#         branchAlways.
SITES = [
    dict(pc=0x005B200C, image='game.bin', original=0xA6020024, kind='subst', asm='sh v0,0x24(s0)',
         guards=[(0x005B1FF8, 0x00121E3C)], choices=[('infinite_ammo', 0x00000000), ('cj_infinite_ammo', 0x00000000)],
         pnach_guard='Infinite Ammo: D05B1FC8 00001E3C (+0x30: 0x005B1FF8 == 0x1E3C)'),
    dict(pc=0x005B2008, image='game.bin', original=0x2482FFFF, kind='subst', asm='addiu v0,a0,-1 (delay slot)',
         guards=[(0x005B1FF8, 0x00121E3C)],
         choices=[('cb_extra_ammo', 0x24820001), ('cb_max_infinite_ammo', 0x24030063),
                  ('mc_infinite_ammo_all_weapons', 0x24820000)],
         pnach_guard='Extra Ammo / Max Infinite Ammo: D05B1FC8 00001E3C (+0x30: 0x005B1FF8 == 0x1E3C); '
                     'Infinite Ammo (All Weapons): none',
         note='Three options write this one instruction with different words: the first one switched on wins, in '
              'this order (Extra Ammo, Max Infinite Ammo, Infinite Ammo (All Weapons)). A build with one site per '
              'instruction can only compile one of them as a plain subst; they are mutually exclusive.'),
    dict(pc=0x005B218C, image='game.bin', original=0xA6020024, kind='subst', asm='sh v0,0x24(s0)',
         guards=[(0x005B2178, 0x00121E3C)], choices=[('infinite_items', 0x00000000)],
         pnach_guard='Infinite Item Usage: E0031E3D 005B2148 (+0x30, value fixed: 0x005B2178 == 0x1E3C)'),
    dict(pc=0x005B21A0, image='game.bin', original=0x14430003, kind='branchNever', asm='bne v0,v1,0x005B21B0',
         guards=[(0x005B2178, 0x00121E3C)], choices=[('infinite_items', 0x00000000)],
         pnach_guard='Infinite Item Usage (as above)'),
    dict(pc=0x005B51B4, image='game.bin', original=0x0000102D, kind='subst', asm='move v0,zero',
         guards=[(0x005B2178, 0x00121E3C)], choices=[('infinite_items', 0x00000000)],
         pnach_guard='Infinite Item Usage (as above)'),
    dict(pc=0x00667E5C, image='game.bin', original=0xAE300BAC, kind='subst', asm='sw s0,0xbac(s1)',
         guards=[(0x00667E54, 0x0C199FA4)], choices=[('cb_no_zombie_over_time', 0x00000000)],
         pnach_guard="Don't Become A Zombie Over Time: D0667DF4 00009F8C (+0x60: 0x00667E54 == 0x9FA4)"),
    dict(pc=0x00660160, image='game.bin', original=0xAE220BAC, kind='subst', asm='sw v0,0xbac(s1) (delay slot)',
         guards=[(0x0066015C, 0x0C199FE4)], choices=[('cb_no_zombie_when_bitten', 0x00000000)],
         pnach_guard="Don't Become A Zombie When Bitten: D06600FC 00009FCC (+0x60: 0x0066015C == 0x9FE4)"),
    dict(pc=0x00640800, image='game.bin', original=0x1062000C, kind='branchNever', asm='beq v1,v0,0x00640834',
         guards=[(0x006407F4, 0x00C0882D)], choices=[('one_hit_kills', 0xA6620138)],
         pnach_guard='1-Hit Deaths (Enemies): D0640794 0000882D (+0x60: 0x006407F4 == 0x882D)',
         note='branchNever with the replacement sh v0,0x138(s3).'),
    dict(pc=0x00660B18, image='game.bin', original=0x10600003, kind='branchNever', asm='beqz v1,0x00660B28',
         guards=[(0x00660B0C, 0x0080802D)], choices=[('cb_enemies_dont_damage', 0x00000000)],
         pnach_guard="Enemies Don't Damage You With Attacks: D0660AAC 0000802D (+0x60: 0x00660B0C == 0x802D)"),
    dict(pc=0x0065FD38, image='game.bin', original=0x1443001D, kind='branchAlways', asm='bne v0,v1,0x0065FDB0',
         guards=[(0x0065FD14, 0x0220202D)], choices=[('cb_zombie_after_death', 0x1000001D)],
         pnach_guard='Become A Zombie After Death: D065FCB5 0000202D (+0x60 and aligned: 0x0065FD14 == 0x202D); '
                     'the code writes the halfword 0x1000 at 0x0065FD3A'),
    dict(pc=0x00660800, image='game.bin', original=0x86030544, kind='subst', asm='lh v1,0x544(s0)',
         guards=[(0x006607F4, 0x84234200)], choices=[('cb_infinite_health_on', 0x2403270F)],
         pnach_guard='Infinite Health: E0023881 00660794 (+0x60, value fixed: 0x006607F4 == 0x4200)'),
    dict(pc=0x00660808, image='game.bin', original=0x00000000, kind='substAccess', asm='nop (delay slot)',
         guards=[(0x006607F4, 0x84234200)],
         choices=[('cb_infinite_health_32', 0xAE030544), ('cb_infinite_health_16', 0xA6030544)],
         pnach_guard='Infinite Health (as above)',
         note='As written the store is sw (AE030544: HP 9999 and max HP 0); the option\'s 16-bit choice writes '
              'sh (A6030544: HP only).'),
    dict(pc=0x0068C7DC, image='game.bin', original=0x2463FFFF, kind='subst', asm='addiu v1,v1,-1',
         guards=[(0x0068C7D0, 0x848300A8)],
         choices=[('mc_freeze_escape_time_l2', 0x24630000), ('mc_reset_escape_time_l2', 0x24630000),
                  ('mc_infinite_escape_time', 0x24630000)],
         pnach_guard='none (the jokers D02B081C 0000FEFF / D02AFE1C 0000FEFF gate two of them)',
         note='The rate profile (config/rate_profiles/outbreak_ntsc_u_v2.00.json, site R1 "event-script timers") '
              'patches this same instruction with the same word 0x24630000 under SubTick. A build with one site per '
              'instruction must merge them: the replacement applies when SubTick OR one of these options is on.'),
    dict(pc=0x0068C7E0, image='game.bin', original=0xA48300A8, kind='subst', asm='sh v1,0xa8(a0)',
         guards=[(0x0068C7D0, 0x848300A8)], choices=[('cj_infinite_time', 0x00000000)], pnach_guard='none'),
    dict(pc=0x00667E58, image='game.bin', original=0x0200302D, kind='subst', asm='move a2,s0 (delay slot)',
         guards=[(0x00667E54, 0x0C199FA4)], choices=[('mc_virus_level_never_goes_up', 0x34100000)],
         pnach_guard='none'),
    dict(pc=0x00667E28, image='game.bin', original=0x4410B800, kind='subst', asm='mfc1 s0,$f23',
         guards=[(0x00667E24, 0x4600BDE4), (0x00667E54, 0x0C199FA4)], choices=[('cb_l1_select_infection', 0x24900000)],
         pnach_guard='joker D02AFE9C 0000FBFE writes it, D02AFE9C 0000FFFF writes the original back (+0xA00: pad copy '
                     '0x002B089C)'),
    dict(pc=0x00696514, image='game.bin', original=0x92020C82, kind='subst', asm='lbu v0,0xc82(s0)',
         guards=[(0x0069650C, 0x0C16061C)], choices=[('cj_zombies_dont_move', 0x00000000)], pnach_guard='none'),
    dict(pc=0x0057C518, image='demo.bin', original=0x0003100A, kind='subst', asm='movz v0,zero,v1',
         guards=[(0x0057C4F0, 0x24423BF4), (0x0057C510, 0x8CA30000)], choices=[('cj_collection_opened', 0x00000000)],
         pnach_guard='the installed code\'s own: lhu == 0x100A at the site'),
    dict(pc=0x00581C14, image='demo.bin', original=0x10400072, kind='branchNever', asm='beqz v0,0x00581DE0',
         guards=[(0x00581C04, 0x8C424078)], choices=[('cj_scenarii_opened', 0x00000000)], pnach_guard='none'),
]

# ---- the conditions the sites use ------------------------------------------------------------------------------------
# master: 'armax' | 'cb' | 'gs'. opts: the options any of which switches it on: (key, None) = on when non-zero,
# (key, n) = on when the option's value is n. joker: (pad address, value) = only while the pad halfword equals value.
# latch: (pad address, on value, off value) = the pnach's pair of jokers: set when the pad equals the first, cleared when
# it equals the second, unchanged otherwise.
CONDS = {
    'infinite_ammo': dict(master='cb', opts=[('infinite_ammo', None)]),
    'cj_infinite_ammo': dict(master='armax', opts=[('cj_infinite_ammo', None)]),
    'cb_extra_ammo': dict(master='cb', opts=[('cb_extra_ammo', None)]),
    'cb_max_infinite_ammo': dict(master='cb', opts=[('cb_max_infinite_ammo', None)]),
    'mc_infinite_ammo_all_weapons': dict(master='gs', opts=[('mc_infinite_ammo_all_weapons', None)]),
    'infinite_items': dict(master='cb', opts=[('infinite_items', None)]),
    'cb_no_zombie_over_time': dict(master='cb', opts=[('cb_no_zombie_over_time', None), ('no_infection', None)]),
    'cb_no_zombie_when_bitten': dict(master='cb', opts=[('cb_no_zombie_when_bitten', None), ('no_infection', None)]),
    'one_hit_kills': dict(master='cb', opts=[('one_hit_kills', None)]),
    'cb_enemies_dont_damage': dict(master='cb', opts=[('cb_enemies_dont_damage', None)]),
    'cb_zombie_after_death': dict(master='cb', opts=[('cb_zombie_after_death', None)]),
    'cb_infinite_health_on': dict(master='cb', opts=[('cb_infinite_health', None)]),
    'cb_infinite_health_32': dict(master='cb', opts=[('cb_infinite_health', 2)]),
    'cb_infinite_health_16': dict(master='cb', opts=[('cb_infinite_health', 1)]),
    'mc_freeze_escape_time_l2': dict(master='gs', opts=[('mc_freeze_escape_time_l2', None)],
                                     joker=(0x002B081C, 0xFEFF)),
    'mc_reset_escape_time_l2': dict(master='gs', opts=[('mc_reset_escape_time_l2', None)],
                                    joker=(0x002B081C, 0xFEFF)),
    'mc_infinite_escape_time': dict(master='gs', opts=[('mc_infinite_escape_time', None)]),
    'cj_infinite_time': dict(master='armax', opts=[('cj_infinite_time', None)]),
    'mc_virus_level_never_goes_up': dict(master='gs', opts=[('mc_virus_level_never_goes_up', None)]),
    'cb_l1_select_infection': dict(master='cb', opts=[('cb_l1_select_infection', None)],
                                   latch=(0x002B089C, 0xFBFE, 0xFFFF)),
    'cj_zombies_dont_move': dict(master='armax', opts=[('cj_zombies_dont_move', None)]),
    'cj_collection_opened': dict(master='armax', opts=[('cj_collection_opened', None)]),
    'cj_scenarii_opened': dict(master='armax', opts=[('cj_scenarii_opened', None)]),
}

# ---- data words the mod can write (for the README and the tests; the code is src/data.c) -----------------------------
# (option key, address, width in bytes, what)
DATA = [
    ('cb_have_all_collection_available', 0x00323BF4, 24, 'OR the valid collection bits (save)'),
    ('cb_have_all_collection_purchased', 0x00323C54, 24, 'OR the valid collection bits (save)'),
    ('mc_unlock_entire_collection', 0x00323C54, 24, 'OR the valid collection bits (save)'),
    ('cb_infinite_reward_points', 0x0031FB60, 2, '0xFFFF (save; only if the total stays <= 99,999,999)'),
    ('cb_max_reward_points', 0x0031FB60, 4, '99,999,999 (save)'),
    ('cj_max_collection_pts', 0x0031FB60, 4, '0x00320000 = 3,276,800 (save)'),
    ('mc_max_result_points', 0x0031FB60, 4, '99,999 (save)'),
    ('infinite_health', 0x004A6174, 2, 'HP = max HP'),
    ('cj_infinite_health_max_health', 0x004A6174, 4, 'HP = max HP = 9999'),
    ('mc_infinite_health', 0x004A6174, 4, '0x08FC08FC'),
    ('bh_p1_item_slot_1', 0x004A68B4, 1, 'item number'),
    ('bh_p1_item_slot_2', 0x004A68B5, 1, 'item number'),
    ('bh_p1_item_slot_3', 0x004A68B6, 1, 'item number'),
    ('bh_p1_item_slot_4', 0x004A68B7, 1, 'item number'),
    ('bh_p1_special_item_slot', 0x004A68B8, 1, 'item number'),
    ('bh_p1_yoko_item_slot_5', 0x004A68B9, 1, 'item number'),
    ('bh_p1_yoko_item_slot_6', 0x004A68BA, 1, 'item number'),
    ('bh_p1_yoko_item_slot_7', 0x004A68BB, 1, 'item number'),
    ('bh_p1_yoko_item_slot_8', 0x004A68BC, 1, 'item number'),
    ('bh_completed_events_1', 0x003B84F8, 4, 'value'),
    ('bh_completed_events_2', 0x003B84FC, 4, 'value'),
    ('bh_result_points_best_record', 0x003B8505, 1, '0 / 0xFF'),
    ('bh_completion_time_best_record', 0x003B8506, 1, '0 / 0xFF'),
    ('bh_no_damage_clear', 0x003B84F4, 1, '0'),
    ('bh_no_weapon_clear', 0x003B84F5, 1, '0'),
    ('bh_result_points_modifier', 0x003B84B4, 4, 'value (<= 99,999,999)'),
    ('bh_completion_time_rank', 0x003B8507, 1, '0-6'),
    ('bh_survivor_modifier', 0x003B84F6, 1, '0-3'),
    ('unlock_all_scenarios', 0x00323BD8, 4, 'OR 0x1F (save)'),
    ('mc_unlock_infinity_mode', 0x0031FB7C, 4, 'OR 0x05000000: byte 0x0031FB7F bits 0x01, 0x04 (save)'),
    ('cb_unlock_infinity_mode', 0x0031FB7C, 4, 'OR 0x05000000 (save)'),
    ('cj_fast_hero', 0x004A5D20, 4, '1.5f'), ('cj_fast_hero', 0x004A67F0, 4, '1.5f'),
    ('cj_super_fast_hero', 0x004A5D20, 4, '2.0f'), ('cj_super_fast_hero', 0x004A67F0, 4, '2.0f'),
    ('cj_giant_hero', 0x004A5CE4, 12, '1.5f x3'),
    ('cj_zero_virus_gauge', 0x004A67DC, 4, '0'),
    ('no_infection', 0x004A67DC, 4, '0 (with infection_freeze_value 0 and the Action Replay MAX master, as 1.1.0)'),
    ('cb_all_costumes', 0x0031FB64, 8, 'OR 0x01010101, 0x03030301 (save)'),
    ('bh_animation_picker', 0x004A67CB, 1, 'value'),
    ('bh_enemies_cant_touch', 0x004A67D2, 1, '0x20'),
    ('bh_enemies_dont_notice', 0x004A67D1, 1, '1 on L2+Up, 0 on L2+Down'),
    ('bh_have_all_files', 0x004B9C80, 2, '0xFFFF'),
    ('bh_number_of_players', 0x004BAEA0, 1, '1-4'),
    ('bh_p1_alt_costume', 0x004A67EC, 1, '0-5'),
    ('bh_p1_model', 0x004A67E4, 2, 'model'),
    ('bh_p1_char_type', 0x004A67C8, 1, '0-7'),
    ('bh_p1_damage', 0x004A67F4, 4, 'float'),
    ('bh_p1_speed_1', 0x004A67D8, 4, 'float'),
    ('bh_p1_speed_2', 0x004A67F0, 4, 'float'),
    ('bh_p1_status', 0x004A67D0, 1, 'status'),
    ('bh_p1_virus_gauge_1', 0x004A67DC, 4, 'N % of the maximum'),
    ('bh_p1_virus_gauge_2', 0x004A67E8, 4, 'value'),
    ('bh_walk_through_walls', 0x004A68E0, 4, '0xFFFFFFFF'), ('bh_walk_through_walls', 0x004A68FC, 4, '0xFFFFFFFF'),
    ('bh_rapid_fire', 0x004A67D3, 1, '0xFF on R1+Cross'),
    ('cb_unlock_all_npcs', 0x0031FB6C, 12, 'OR 0x72400C40, 0xFF03C200, 0x03FFC0FB (save)'),
]
for _ch, _ci in CHARS:
    for _t in ('all', 'b', 'c'):
        if _t == 'c' and _ci not in FEMALE:
            continue
        DATA.append((f'cb_costume_{_ch.lower()}_{_t}', 0x0031FB64 + _ci, 1, 'OR costume bits (save)'))

# Valid save bits, derived from the game's own tables on the owner's disc (demo.bin: the collection tables at
# 0x0058B1F0, the unlock table at 0x0058B580; see README "Save safety").
COLLECTION_MASK = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFBFE1FFF, 0x00079FFF]
COSTUME_MASK = [0x01010101, 0x03030301]
NPC_MASK = [0x72400C40, 0xFF03C200, 0x03FFC0FB]
INFINITY_BITS = 0x05000000
