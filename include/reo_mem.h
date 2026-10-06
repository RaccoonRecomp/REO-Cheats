#ifndef __REO_MEM_H__
#define __REO_MEM_H__

#include "recomp_api.h"

// The regular cheat set: every code comes from the owner's regular cheat list ("Resident Evil - Outbreak (NTSC-U)",
// the original release), on SLUS-20765 v2.00, the disc this recompilation runs, whose game code has the Greatest Hits
// memory layout. Each address used here is the verified address on that disc (see README).

// EE RAM mapping: an aligned EE word (0x00000000-0x01FFFFFF) is dereferenced directly. If mod code sees EE RAM at a
// different base, this macro is the only thing that changes.
#define REO_EE_U32(addr) (*(volatile u32*)(addr))

#define REO_ARRAY_COUNT(arr) (sizeof(arr) / sizeof((arr)[0]))

// EE RAM is little-endian, but N64Recomp translates a mod's byte and halfword loads/stores with big-endian (N64) byte
// order, so they would land on the wrong bytes of the word. Every EE access goes through the aligned 32-bit word, and
// bytes/halfwords are shifted in and out of it. addr must be naturally aligned for its width.
static inline u32 Reo_Read(u32 addr, u32 width) {
    u32 word = REO_EE_U32(addr & ~3u);
    u32 shift = (addr & 3u) * 8;

    switch (width) {
        case 1: return (word >> shift) & 0xFFu;
        case 2: return (word >> shift) & 0xFFFFu;
        default: return word;
    }
}

// Writes only when the value differs, so an unchanged word is never stored (a pnach line would store it again every
// frame; the result in RAM is the same).
static inline void Reo_Write(u32 addr, u32 width, u32 value) {
    u32 shift = (addr & 3u) * 8;
    u32 mask;
    u32 old;
    u32 next;

    switch (width) {
        case 1: mask = 0xFFu << shift; break;
        case 2: mask = 0xFFFFu << shift; break;
        default: mask = 0xFFFFFFFFu; break;
    }
    old = REO_EE_U32(addr & ~3u);
    next = (old & ~mask) | ((value << shift) & mask);
    if (next != old) {
        REO_EE_U32(addr & ~3u) = next;
    }
}

// Sets bits of a save word (never clears any): a valid unlock only adds the bits the game itself sets.
static inline void Reo_SetBits(u32 addr, u32 bits) {
    u32 old = REO_EE_U32(addr);

    if ((old & bits) != bits) {
        REO_EE_U32(addr) = old | bits;
    }
}

// The pad halfword the jokers test (D02B081C ... in the codes): 0xFFFF with nothing pressed, a pressed button clears
// its bit (L2 0x0100, Up 0x0010, Down 0x0040, R1 0x0800, Cross 0x4000, L1 0x0400, Select 0x0001). Verified in a
// probe of the game on the owner's disc (base_a). 0x002B089C holds a second copy of the same halfword.
#define REO_PAD 0x002B081Cu
#define REO_PAD_COPY 0x002B089Cu

static inline u32 Reo_Pad(u32 addr) {
    return Reo_Read(addr, 2);
}

// game.bin (BIN\2.DAT, the in-scenario overlay at 0x00570000) is in memory: its "dsll32 v1,s2,0x18" at 0x005B1FF8, the
// instruction the Infinite Ammo guard tests (no other overlay has it there).
static inline u32 Reo_GameBinLoaded(void) {
    return REO_EE_U32(0x005B1FF8) == 0x00121E3Cu;
}

// Player 1's character is set up: game.bin loaded and Player 1's max HP (0x004A6176) not 0.
#define REO_P1_BLOCK 0x004A5C30u
static inline u32 Reo_P1Ready(void) {
    return Reo_GameBinLoaded() && Reo_Read(0x004A6176, 2) != 0;
}

// The save data is set up (created or loaded): bit 0 (Outbreak) of the scenario word is set by the game then.
#define REO_SAVE_SCENARIOS 0x00323BD8u
static inline u32 Reo_SaveReady(void) {
    return (REO_EE_U32(REO_SAVE_SCENARIOS) & 1u) != 0;
}

#endif
