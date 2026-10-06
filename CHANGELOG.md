# Changelog

## 1.2.0

First release on GitHub: the mod as a downloadable zip for **Mods → Install Mods** (`release/reo-cheats-1.2.0.zip`).
The mod's code and manifest are unchanged.

- **Every cheat of the regular cheat list is its own option** (1.1.0 had seven): 102 cheats, grouped as in the list,
  each with its device code(s), the plain code, its status on the v2.00 disc and the evidence in its description.
- **Saved settings keep their meaning**: `infinite_health` (Codejunkies' Infinite Health), `infinite_ammo`,
  `infinite_items`, `one_hit_kills` (Code Master's codes), `unlock_all_scenarios` (MadCatz' Unlock All Levels, now
  labelled with its own name) and the three master codes. `no_infection` switches both Don't Become A Zombie codes as in
  1.1.0, and with `infection_freeze_value` 0 (the default) and the Action Replay MAX master code On it also holds
  Player 1's virus gauge at 0. `max_inventory` still does nothing. bungholio's Player 1 Virus Gauge Modifier #1 has its
  own value (0-99 % of the game's own maximum). The virus gauge is now written only while Player 1 is set up in a
  scenario, like every Player 1 cheat.
- **New master codes**: Alternate [M] Must Be On and Must Be On by MadCatz (either enables the GameShark cheats, like
  [M] Must Be On), and the AR Max Below 3.14 Fix (a device firmware fix; does nothing here).
- **Save data: only valid bits**; Unlock All Levels adds the five scenario bits instead of replacing the word.

## 1.1.0 and earlier

- Seven switches of the regular cheat set (Infinite Health, Infinite Ammo, Infinite Items, Unlock All Scenarios, Max
  Inventory, No Infection with its freeze value, One-Hit Kills), each mapped to one regular code, for the SLUS-20765
  v2.00 disc.
