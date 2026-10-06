#include "recomp_api.h"
#include "reo_cheats.h"

// The owner's regular cheat list (the original release's codes: Codejunkies, Code Master et al., MadCatz, bungholio),
// every cheat its own option, on SLUS-20765 v2.00 (the Greatest Hits memory layout). See README.
//
// recomp_on_play_main's arguments are not used, so none are declared.
RECOMP_CALLBACK("*", recomp_on_play_main)
void Reo_Main_OnPlayMain(void) {
    Reo_Sites_Frame();
    Reo_Data_Frame();
}
