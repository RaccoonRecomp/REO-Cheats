#ifndef __REO_CHEATS_H__
#define __REO_CHEATS_H__

#include "recomp_api.h"

// One frame of the mod, called from the game's per-frame callback (src/main.c), in this order:
//   Reo_Sites_Frame: the code-patch cheats (guard + writes + restore of every site in gen_cheats.h);
//   Reo_Data_Frame:  the data cheats (Player 1, results, save data, jokers), src/data.c.
void Reo_Sites_Frame(void);
void Reo_Data_Frame(void);

#endif
