#include "recomp_api.h"
#include "reo_mem.h"
#include "reo_master.h"
#include "reo_cheats.h"
#include "gen_cheats.h"

// The code-patch cheats. Every site (gen_cheats.h, generated from tools/cheat_list.py; patches_sites.json lists the same
// sites for the build) is one instruction of game code on the owner's disc:
//   guard:   all its guard words hold, so the overlay in memory is the one the code was made for (game.bin or
//            demo.bin); otherwise nothing is written, not even to restore (the code is not there);
//   write:   the first replacement whose condition is on (option On, its device's master code On, and for a joker the
//            pad as the code says) is written;
//   restore: with no condition on, the original instruction is written back.
// A site holding a word that is neither its original nor one of its replacements is never touched.
//
// In the recompiled game these writes are not executed as memory writes into code: the game's mod runtime turns a
// write of a listed replacement into switching that site on, and a write of the original into switching it off.

static u32 sCond[REO_COND_COUNT];
static u32 sLatch[REO_COND_COUNT];

static u32 Reo_SiteGuardsHold(const Reo_Site* site) {
    u32 i;

    for (i = 0; i < site->guardCount; i++) {
        const Reo_Guard* g = &kReoGuards[site->guardFirst + i];
        if (REO_EE_U32(g->addr) != g->word) {
            return 0;
        }
    }
    return 1;
}

void Reo_Sites_Frame(void) {
    u32 s;
    u32 i;

    Reo_ComputeConds(sCond, sLatch);

    for (s = 0; s < REO_ARRAY_COUNT(kReoSites); s++) {
        const Reo_Site* site = &kReoSites[s];
        u32 cur;
        u32 desired = site->original;
        u32 known;

        if (!Reo_SiteGuardsHold(site)) {
            continue;
        }
        for (i = 0; i < site->choiceCount; i++) {
            const Reo_Choice* c = &kReoChoices[site->choiceFirst + i];
            if (sCond[c->cond]) {
                desired = c->value;
                break;
            }
        }
        cur = REO_EE_U32(site->pc);
        if (cur == desired) {
            continue;
        }
        known = cur == site->original;
        for (i = 0; i < site->choiceCount && !known; i++) {
            known = cur == kReoChoices[site->choiceFirst + i].value;
        }
        if (known) {
            REO_EE_U32(site->pc) = desired;
        }
    }
}
