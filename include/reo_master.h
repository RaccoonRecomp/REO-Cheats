#ifndef __REO_MASTER_H__
#define __REO_MASTER_H__

#include "recomp_api.h"

// The owner's master codes, each its own option (verbatim in the option descriptions and the README). On a cheat
// device the master code installs the device's hook so that its code engine runs every frame; a device's codes only
// work while its master code is on. The recompiled game has no cheat device, and writing a hook into the game's code
// would take it out of native execution, so no hook is ever written. Each master code is instead the master enable of
// the codes of its device:
//
//   Action Replay MAX, (M) Must Be On by Codejunkies:            the Codejunkies codes (Health Codes, Speed Codes)
//   CodeBreaker v7+, Enable Code (Must Be On) by Code Master...:  the Code Master codes
//   GameShark v3-4 / Xploder v4, [M] Must Be On, Alternate [M] Must Be On or Must Be On by MadCatz (any of the three):
//                                                                the MadCatz and bungholio codes
#define REO_MASTER_ARMAX "master_armax_codejunkies"
#define REO_MASTER_CODEBREAKER "master_codebreaker_codemaster"
#define REO_MASTER_GAMESHARK "master_gameshark_madcatz"
#define REO_MASTER_GAMESHARK_ALT "master_gameshark_madcatz_alternate"
#define REO_MASTER_GAMESHARK_MBO "master_gameshark_madcatz_must_be_on"

static inline u32 Reo_Opt(const char* key) {
    return recomp_get_config_u32(key);
}

static inline u32 Reo_MasterArmax(void) {
    return Reo_Opt(REO_MASTER_ARMAX) != 0;
}

static inline u32 Reo_MasterCodeBreaker(void) {
    return Reo_Opt(REO_MASTER_CODEBREAKER) != 0;
}

static inline u32 Reo_MasterGameShark(void) {
    return Reo_Opt(REO_MASTER_GAMESHARK) != 0 || Reo_Opt(REO_MASTER_GAMESHARK_ALT) != 0 ||
           Reo_Opt(REO_MASTER_GAMESHARK_MBO) != 0;
}

#endif
