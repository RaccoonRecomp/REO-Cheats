# Resident Evil Outbreak — Cheats

A cheat mod for **Resident Evil Outbreak Recompiled**, the unofficial PC port of Resident Evil Outbreak (File #1, USA).
It puts the **regular (original release) cheat set** on the game's Mods tab: every cheat is its own option, you turn
cheats on and off while you play, and a cheat you switch off is completely off again.

- Mod id `reo-cheats`, version **1.2.0**.
- **102 cheats**, each its own option: 40 work as written, 34 are adapted to the v2.00 disc, 19 could not be decoded
  (per-character costume codes: the option does what the cheat's name says instead, not a proven equivalent), and 9
  cannot work on this disc and do nothing. With the master codes, the value settings, the Item Values table choice and
  three switches kept from older versions: 117 options.

> Unofficial fan project, not affiliated with or endorsed by Capcom. See [Legal](#legal).

## Which disc it is for

**Resident Evil Outbreak (USA), SLUS-20765, disc version 2.00** - the release Resident Evil Outbreak Recompiled runs.
In the words of the mod's manifest: "All of the regular release's cheats for Resident Evil Outbreak, each its own
option, on the NTSC-U v2.00 disc". The v2.00 disc's game code has the Greatest Hits memory layout, so many of the
original release's codes point at other instructions and data there. Each code is either used as written (where it
already fits this disc), moved to a proven equivalent ("adapted to this disc"), or marked as not working with the
reason.

There are two cheat mods for this disc. **Enable only one of them**: both change the same game code.

| Mod | Cheats |
|---|---|
| **Resident Evil Outbreak — Cheats** (this one, `reo-cheats`) | the regular (original release) cheat set, adapted to this disc |
| Resident Evil Outbreak — Greatest Hits Cheats (`reo-greatest-hits-cheats`, repository REO-GreatestHits-Cheats) | the Greatest Hits cheat set, made for this disc's layout |

The two mods declare the conflict: if both are switched on, the Mods tab keeps only the one later in the load order
active and says so.

## Requirements

- **Resident Evil Outbreak Recompiled 1.5.0 or newer.**
- **Your own legal copy** of Resident Evil Outbreak (USA), SLUS-20765, disc version 2.00. This mod contains no disc
  image and no game files.

> **Status.** Resident Evil Outbreak Recompiled 1.5.0 cannot start the game yet: the game's code still has to be
> prepared from your own disc on your PC, and that automatic preparation comes in an update. You can install this mod
> and set its options now; they are saved. Once your copy of the game is prepared, the cheats marked **game data** or
> **save data** take effect. The cheats marked **game code** also need their code sites compiled into the prepared
> game: this download does not carry those sites, and the preparation update has to provide them. Until it does, the
> Mods tab reports these cheats as changes of the game's code that are not in this game build.

The cheats marked **game code** in the table below never write the game's code directly: the program switches the
matching code sites compiled into the prepared game code, so they act only in a game build that has this mod's sites.
For every option that is on, the Mods tab says whether it acts in your game (active, waiting for the game, not in this
game build). Cheats marked **game data** or **save data** need nothing more than the mod.

## Install

1. Download `reo-cheats-1.2.0.zip` from this repository's **Releases** page (it is also in the [`release`](release)
   folder). Do not unpack it.
2. In Resident Evil Outbreak Recompiled, open **Mods**, choose **Install Mods** and pick the zip.
3. Make sure the mod is switched on in the list, then press **Configure** and switch on the cheats you want. Every
   cheat starts Off.

The Mods tab checks the whole archive before it writes anything and installs the mod into its own folder,
`mods\reo-cheats\`. To install by hand instead, unpack the zip into your mods folder so that `mods\reo-cheats\mod.json`
exists (the mods folder is `%APPDATA%\Resident Evil Outbreak Recompiled\mods\`, or `mods\` next to the program in a
portable copy).

**Updating:** install the new zip the same way. The Mods tab asks before it replaces the installed version, moves the
old one into `mods\.trash\` (nothing is deleted) and keeps your options, settings and place in the load order.

## Using it

The options are grouped as in the original cheat list: Master Codes, Collection Codes, Health Codes, Player 1 Item
Slot Modifiers, Scenario Completion Codes, Single Play Codes, Speed Codes, Unlock Costume Codes, and Other Codes. Each
option's description on the Mods tab shows what it does on this disc, the device code(s) as published, the plain
code, its status and the evidence for it, what it does to your save, and the master code it needs. Changes apply at
the next game frame.

- **Master codes.** A cheat applies only while the master code of its device is On: Codejunkies' codes need (M) Must
  Be On (Action Replay MAX); Code Master's need Enable Code (Must Be On) (CodeBreaker v7+); MadCatz' and bungholio's
  (GameShark v3-4 / Xploder v4) need any of the three MadCatz master codes. (M) Must Be On, Enable Code and [M] Must Be
  On start On; Alternate [M] Must Be On and Must Be On start Off. No device hook is ever written: the recompiled game
  has no cheat device, and its code runs as native, precompiled code. The master codes are switches instead.
- **Value codes** (`??` / `????????`) are real choices: the nine Player 1 Item Slot codes pick an item by name from
  the Item Values table you choose in **Item Values table** (pick the scenario and difficulty you play); Character
  Type, Character Model, Alternative Costume, Status, the speed and virus-gauge codes, Number Of Players and the
  results-screen codes offer the values their author describes; a few take a raw number, with the author's note.
- **Jokers respond to the pad as written**: only the code's buttons may be held. Rapid Fire: R1+Cross. Enemies Don't
  Notice: L2+Up on, L2+Down off. Escape time: hold L2. P1 L1+Select: L1+Select on, nothing pressed off.
- **Several options on one value** (points, HP, the virus gauge, the speed factor, the ammo instruction): the first one
  in the list that is on wins.

## Off means completely off

- Switching a cheat off, switching its master code off, or switching the whole mod off takes the cheat out of the game
  at the next game frame: the game's own instructions run again, and data the cheat changed gets the game's own value
  back.
- **Save data too.** What a cheat writes into your save is recorded next to your memory card, in its undo file
  (`MemoryCard_01.ps2.undo.json`, never inside the card), and put back when the cheat is off - also after a restart.
  Before the first change of save data in a session the program copies your memory card once
  (`MemoryCard_01.ps2.before-cheats-<date>`).
- What the game itself changed in the meantime stays: what you earned, or bought with a cheat's points, is not taken
  away.
- Values the game's own code stored while a code cheat was on are the game's own until the game changes them.
- The results-screen codes (Scenario Completion Codes, Have All Files) change what the game records at the end of a
  scenario: what the results screen then saves is the game's own doing and stays.

Save-data cheats only ever set values the game itself can write (for example the five scenario bits, the bits of the
172 collection items, the costume bits the game has), they write only once your save has been loaded or created, and
points never go above 99,999,999.

## The cheats

Status on SLUS-20765 v2.00: **works as written** (verified on this disc), **adapted to this disc** (moved only to a
proven equivalent), **code not decodable: substitute from the name** (the published code could not be decoded, so
the option does what the name says, with only the bits the game itself sets: not a proven equivalent), **does not work
on this disc** (the option does nothing; the reason is given). "Changes" says what the option changes: the game's code
(through the compiled code sites), the game's data, or your save data.

| Group | Option (key) | Author | Status on SLUS-20765 v2.00 | What it does | Changes | Master code it needs | Default |
|---|---|---|---|---|---|---|---|
| Master Codes | **Master Code (Action Replay MAX): (M) Must Be On by Codejunkies** (`master_armax_codejunkies`) | Codejunkies | master code | Enables the Codejunkies cheats (Health Codes, Speed Codes). No hook is written: the recompiled game has no cheat device, and writing a hook into the game's code would take it out of native execution. This switch enables the cheats of its device instead. | - |  | On |
| Master Codes | **AR Max Below 3.14 Fix by Codejunkies** (`cj_armax_below_314_fix`) | Codejunkies | device fix: does nothing here | Nothing: a firmware fix for Action Replay MAX devices older than 3.14. There is no cheat device here, so it has nothing to do. | - | Action Replay MAX | Off |
| Master Codes | **Master Code (CodeBreaker v7+): Enable Code (Must Be On) by Code Master, Lajos Szalay, Jay007, VirusPunk, Jarnold83** (`master_codebreaker_codemaster`) | Code Master, Lajos Szalay, Jay007, VirusPunk, Jarnold83 | master code | Enables the Code Master (CodeBreaker) cheats. No hook is written: the recompiled game has no cheat device, and writing a hook into the game's code would take it out of native execution. This switch enables the cheats of its device instead. | - |  | On |
| Master Codes | **Master Code (GameShark v3-4 / Xploder v4): [M] Must Be On by MadCatz** (`master_gameshark_madcatz`) | MadCatz | master code | Enables the MadCatz and bungholio (GameShark) cheats; any of the three GameShark master codes does. No hook is written: the recompiled game has no cheat device, and writing a hook into the game's code would take it out of native execution. This switch enables the cheats of its device instead. | - |  | On |
| Master Codes | **Master Code (GameShark v3-4 / Xploder v4): Alternate [M] Must Be On by MadCatz** (`master_gameshark_madcatz_alternate`) | MadCatz | master code | Enables the MadCatz and bungholio (GameShark) cheats, like [M] Must Be On. No hook is written: the recompiled game has no cheat device, and writing a hook into the game's code would take it out of native execution. This switch enables the cheats of its device instead. | - |  | Off |
| Master Codes | **Master Code (GameShark v3-4 / Xploder v4): Must Be On by MadCatz** (`master_gameshark_madcatz_must_be_on`) | MadCatz | master code | Enables the MadCatz and bungholio (GameShark) cheats, like [M] Must Be On. The list has it twice, with and without its two extra lines: one master code. No hook is written: the recompiled game has no cheat device, and writing a hook into the game's code would take it out of native execution. This switch enables the cheats of its device instead. | - |  | Off |
| Collection Codes | **Have All Collection Available For Purchase** (`cb_have_all_collection_available`) | Code Master, Lajos Szalay, Jay007, VirusPunk, Jarnold83 | adapted to this disc | Every collection item can be bought: the "available" bits of all 172 collection items (save data 0x00323BF4, six words) are set. | save data | CodeBreaker | Off |
| Collection Codes | **Have All Collection Purchased** (`cb_have_all_collection_purchased`) | Code Master, Lajos Szalay, Jay007, VirusPunk, Jarnold83 | adapted to this disc | Every collection item shows as owned ("You already have this"): the "owned" bits of all collection items (0x00323C54, six words). | save data | CodeBreaker | Off |
| Collection Codes | **Infinite Reward Points** (`cb_infinite_reward_points`) | Code Master, Lajos Szalay, Jay007, VirusPunk, Jarnold83 | adapted to this disc | The collection points are held at xx,x65,535 (the low 16 bits of the points word set to 0xFFFF). | save data | CodeBreaker | Off |
| Collection Codes | **Infinite Rewards Points Usage** (`cb_infinite_rewards_points_usage`) | Code Master, Lajos Szalay, Jay007, VirusPunk, Jarnold83 | **does not work on this disc** | Nothing: its guard matches no code on this disc, so the place it patches cannot be found (and its second write would break a store). | - | CodeBreaker | Off |
| Collection Codes | **Max Reward Points** (`cb_max_reward_points`) | Code Master, Lajos Szalay, Jay007, VirusPunk, Jarnold83 | adapted to this disc | The collection points are set to 99,999,999. | save data | CodeBreaker | Off |
| Health Codes | **Infinite Health** (`infinite_health`) | Codejunkies | adapted to this disc | Player 1's HP is kept at Player 1's max HP (what the installed code does: lh max HP / sh HP). | game data | Action Replay MAX | Off |
| Health Codes | **Infinite Health & Max Health (Never Bleed)** (`cj_infinite_health_max_health`) | Codejunkies | adapted to this disc | Player 1's HP and max HP are both held at 9999. | game data | Action Replay MAX | Off |
| Player 1 Item Slot Modifiers | **Item Values table (for the Player 1 Item Slot codes)** (`bh_item_values_table`) |  | setting | Which of the "Item Values" tables (by nobody) the item slot options look their item up in: pick the scenario and difficulty you play. The slot value is the item's number in that table. | - |  | Outbreak - Normal |
| Player 1 Item Slot Modifiers | **Player 1 Item Slot 1** (`bh_p1_item_slot_1`) | bungholio | works as written | Holds the item you pick in this slot (byte 0x004A68B4), like the code's ?? value: the mod writes the number the picked item has in the chosen Item Values table. An item that is not in that table leaves the slot alone. "Past the table +N" are the numbers after the table: the list's note says those are the characters' own items (in Outbreak on Normal, +0 is "45 Auto for Kevin"). | game data | GameShark | Off |
| Player 1 Item Slot Modifiers | **Player 1 Item Slot 2** (`bh_p1_item_slot_2`) | bungholio | works as written | Holds the item you pick in this slot (byte 0x004A68B5), like the code's ?? value: the mod writes the number the picked item has in the chosen Item Values table. An item that is not in that table leaves the slot alone. "Past the table +N" are the numbers after the table: the list's note says those are the characters' own items (in Outbreak on Normal, +0 is "45 Auto for Kevin"). | game data | GameShark | Off |
| Player 1 Item Slot Modifiers | **Player 1 Item Slot 3** (`bh_p1_item_slot_3`) | bungholio | works as written | Holds the item you pick in this slot (byte 0x004A68B6), like the code's ?? value: the mod writes the number the picked item has in the chosen Item Values table. An item that is not in that table leaves the slot alone. "Past the table +N" are the numbers after the table: the list's note says those are the characters' own items (in Outbreak on Normal, +0 is "45 Auto for Kevin"). | game data | GameShark | Off |
| Player 1 Item Slot Modifiers | **Player 1 Item Slot 4** (`bh_p1_item_slot_4`) | bungholio | works as written | Holds the item you pick in this slot (byte 0x004A68B7), like the code's ?? value: the mod writes the number the picked item has in the chosen Item Values table. An item that is not in that table leaves the slot alone. "Past the table +N" are the numbers after the table: the list's note says those are the characters' own items (in Outbreak on Normal, +0 is "45 Auto for Kevin"). | game data | GameShark | Off |
| Player 1 Item Slot Modifiers | **Player 1 Special Item Slot** (`bh_p1_special_item_slot`) | bungholio | works as written | Holds the item you pick in this slot (byte 0x004A68B8), like the code's ?? value: the mod writes the number the picked item has in the chosen Item Values table. An item that is not in that table leaves the slot alone. "Past the table +N" are the numbers after the table: the list's note says those are the characters' own items (in Outbreak on Normal, +0 is "45 Auto for Kevin"). | game data | GameShark | Off |
| Player 1 Item Slot Modifiers | **Player 1 Yoko Item Slot 5** (`bh_p1_yoko_item_slot_5`) | bungholio | works as written | Holds the item you pick in this slot (byte 0x004A68B9), like the code's ?? value: the mod writes the number the picked item has in the chosen Item Values table. An item that is not in that table leaves the slot alone. "Past the table +N" are the numbers after the table: the list's note says those are the characters' own items (in Outbreak on Normal, +0 is "45 Auto for Kevin"). | game data | GameShark | Off |
| Player 1 Item Slot Modifiers | **Player 1 Yoko Item Slot 6** (`bh_p1_yoko_item_slot_6`) | bungholio | works as written | Holds the item you pick in this slot (byte 0x004A68BA), like the code's ?? value: the mod writes the number the picked item has in the chosen Item Values table. An item that is not in that table leaves the slot alone. "Past the table +N" are the numbers after the table: the list's note says those are the characters' own items (in Outbreak on Normal, +0 is "45 Auto for Kevin"). | game data | GameShark | Off |
| Player 1 Item Slot Modifiers | **Player 1 Yoko Item Slot 7** (`bh_p1_yoko_item_slot_7`) | bungholio | works as written | Holds the item you pick in this slot (byte 0x004A68BB), like the code's ?? value: the mod writes the number the picked item has in the chosen Item Values table. An item that is not in that table leaves the slot alone. "Past the table +N" are the numbers after the table: the list's note says those are the characters' own items (in Outbreak on Normal, +0 is "45 Auto for Kevin"). | game data | GameShark | Off |
| Player 1 Item Slot Modifiers | **Player 1 Yoko Item Slot 8** (`bh_p1_yoko_item_slot_8`) | bungholio | works as written | Holds the item you pick in this slot (byte 0x004A68BC), like the code's ?? value: the mod writes the number the picked item has in the chosen Item Values table. An item that is not in that table leaves the slot alone. "Past the table +N" are the numbers after the table: the list's note says those are the characters' own items (in Outbreak on Normal, +0 is "45 Auto for Kevin"). | game data | GameShark | Off |
| Scenario Completion Codes | **Completed Events Modifier 1 Of 2** (`bh_completed_events_1`) | bungholio | works as written | The first word of the scenario's completed-events bits (0x003B84F8) is held at the value below. | save data, through the results screen | GameShark | Off |
| Scenario Completion Codes | **Completed Events Modifier 1 Of 2: value** (`bh_completed_events_1_value`) |  | setting | The ???????? value of Completed Events Modifier 1 Of 2 (bits of completed events). Author: "Just set both of them to all F's to have all events completed and probably get more than a 100% completion ratio". | - |  | 0 |
| Scenario Completion Codes | **Completed Events Modifier 2 Of 2** (`bh_completed_events_2`) | bungholio | works as written | The second word of the completed-events bits (0x003B84FC) is held at the value below. | save data, through the results screen | GameShark | Off |
| Scenario Completion Codes | **Completed Events Modifier 2 Of 2: value** (`bh_completed_events_2_value`) |  | setting | The ???????? value of Completed Events Modifier 2 Of 2. | - |  | 0 |
| Scenario Completion Codes | **Determines Whether Your Result Points Are A New Best Record** (`bh_result_points_best_record`) | bungholio | works as written | The results screen's "new best record" flag for result points (byte 0x003B8505). | save data, through the results screen | GameShark | Off |
| Scenario Completion Codes | **Determines Whether Your Scenario Completion Time is A New Best Record** (`bh_completion_time_best_record`) | bungholio | works as written | The results screen's "new best record" flag for the play time (byte 0x003B8506). | save data, through the results screen | GameShark | Off |
| Scenario Completion Codes | **No Damage Clear** (`bh_no_damage_clear`) | bungholio | works as written | The "damage taken" flag of the scenario (byte 0x003B84F4) is held at 0, so it ends as a no-damage clear. | save data, through the results screen | GameShark | Off |
| Scenario Completion Codes | **No Weapon Clear** (`bh_no_weapon_clear`) | bungholio | works as written | The "weapon used" flag (byte 0x003B84F5) is held at 0, so it ends as a no-weapon clear. | save data, through the results screen | GameShark | Off |
| Scenario Completion Codes | **Result Points Modifier** (`bh_result_points_modifier`) | bungholio | works as written | The scenario's result points (0x003B84B4) are held at the value below. | save data, through the results screen | GameShark | Off |
| Scenario Completion Codes | **Result Points Modifier: value** (`bh_result_points_modifier_value`) |  | setting | The ???????? value of Result Points Modifier (points, 0 to 99,999,999). | - |  | 0 |
| Scenario Completion Codes | **Scenario Completion Time Rank Modifier** (`bh_completion_time_rank`) | bungholio | works as written | The play-time rank of the results (byte 0x003B8507). | save data, through the results screen | GameShark | Off |
| Scenario Completion Codes | **Survivor Modifier** (`bh_survivor_modifier`) | bungholio | works as written | The number of survivors of the results (byte 0x003B84F6). | save data, through the results screen | GameShark | Off |
| Single Play Codes | **Infinite Ammo (All Weapons)** (`mc_infinite_ammo_all_weapons`) | MadCatz | works as written | Firing does not use up rounds: the count stays (the "count - 1" at 0x005B2008 becomes "count - 0"). | game code | GameShark | Off |
| Single Play Codes | **Infinite Health** (`mc_infinite_health`) | MadCatz | works as written | Player 1's HP and max HP are held at 2300 each (0x004A6174 = 08FC08FC). | game data | GameShark | Off |
| Single Play Codes | **Max Result Points** (`mc_max_result_points`) | MadCatz | works as written | The collection points are set to 99,999. | save data | GameShark | Off |
| Single Play Codes | **Press And Hold L2 To Freeze Escape Time** (`mc_freeze_escape_time_l2`) | MadCatz | adapted to this disc | While you hold L2 (and nothing else), the game's event timers stop counting down. | game code | GameShark | Off |
| Single Play Codes | **Ultimate Ammo Code** (`mc_ultimate_ammo_code`) | MadCatz | **does not work on this disc** | Nothing: as written it would break a call on this disc; moved to this disc it writes the instruction that is already there, so no effect can be made from it. | - | GameShark | Off |
| Single Play Codes | **Unlock All Levels** (`unlock_all_scenarios`) | MadCatz | works as written | All five scenarios can be selected: the scenario bits of your save (0x00323BD8) are set. | save data | GameShark | Off |
| Single Play Codes | **Unlock Entire Collection** (`mc_unlock_entire_collection`) | MadCatz | works as written | Every collection item shows as owned: the owned bits of all collection items (0x00323C54, six words). | save data | GameShark | Off |
| Single Play Codes | **Unlock Infinity Mode** (`mc_unlock_infinity_mode`) | MadCatz | works as written | Unlocks the Infinity mode: the extra-mode flags the collection's Infinity (item 0xB0) and its neighbour item 0xAF set (0x0031FB7F bits 0x01 and 0x04). | save data | GameShark | Off |
| Single Play Codes | **Virus Level Never Goes Up** (`mc_virus_level_never_goes_up`) | MadCatz | adapted to this disc | The virus gauge of every character stays at 0 (the gauge update stores 0). | game code | GameShark | Off |
| Single Play Codes | **Single Play Codes: Infinite: Escape Time** (`mc_infinite_escape_time`) | MadCatz | adapted to this disc | The game's event timers (the escape countdowns) never count down. | game code | GameShark | Off |
| Speed Codes | **Collection Opened** (`cj_collection_opened`) | Codejunkies | adapted to this disc | Every collection item can be bought while this is on (the game's "is it available" check always says yes). | game code | Action Replay MAX | Off |
| Speed Codes | **Fast Hero** (`cj_fast_hero`) | Codejunkies | adapted to this disc | Player 1 moves faster: two speed factors (0x004A5D20 and 0x004A67F0, normally 1.0) are set to 1.5. | game data | Action Replay MAX | Off |
| Speed Codes | **Giant Hero** (`cj_giant_hero`) | Codejunkies | adapted to this disc | Player 1 is drawn 1.5 times as big (the three scale factors 0x004A5CE4/E8/EC, normally 1.05). | game data | Action Replay MAX | Off |
| Speed Codes | **Infinite Ammo** (`cj_infinite_ammo`) | Codejunkies | adapted to this disc | Firing does not use up rounds (the round-count store is removed). | game code | Action Replay MAX | Off |
| Speed Codes | **Infinite Time** (`cj_infinite_time`) | Codejunkies | adapted to this disc | The game's event timers never count down (their store is removed). | game code | Action Replay MAX | Off |
| Speed Codes | **Max Collection Pts** (`cj_max_collection_pts`) | Codejunkies | adapted to this disc | The collection points are set to 3,276,800 (the code stores 0x00320000). | save data | Action Replay MAX | Off |
| Speed Codes | **Scenarii Opened** (`cj_scenarii_opened`) | Codejunkies | adapted to this disc | All five scenarios can be selected while this is on (the scenario select skips its lock check). | game code | Action Replay MAX | Off |
| Speed Codes | **Super Fast Hero** (`cj_super_fast_hero`) | Codejunkies | adapted to this disc | Player 1 moves much faster: the two speed factors are set to 2.0. | game data | Action Replay MAX | Off |
| Speed Codes | **Zero Virus Gauge** (`cj_zero_virus_gauge`) | Codejunkies | adapted to this disc | Player 1's virus gauge is held at 0. | game data | Action Replay MAX | Off |
| Speed Codes | **Zombies Don't Move** (`cj_zombies_dont_move`) | Codejunkies | adapted to this disc | Enemies stay where they are (they still attack you when you are next to them). | game code | Action Replay MAX | Off |
| Unlock Costume Codes | **All Costumes** (`cb_all_costumes`) | Code Master, Lajos Szalay, Jay007, VirusPunk, Jarnold83 | adapted to this disc | Every costume the game has can be chosen: Type B for all eight characters, Type C for Alyssa, Yoko and Cindy. | save data | CodeBreaker | Off |
| Unlock Costume Codes | **Alyssa-All Types** (`cb_costume_alyssa_all`) | Code Master, Lajos Szalay, Jay007, VirusPunk, Jarnold83 | code not decodable: substitute from the name | Unlocks Alyssa's costumes: Type B and Type C. (a substitute that does what the name says; the original code could not be decoded) | save data | CodeBreaker | Off |
| Unlock Costume Codes | **Alyssa-Type B** (`cb_costume_alyssa_b`) | Code Master, Lajos Szalay, Jay007, VirusPunk, Jarnold83 | code not decodable: substitute from the name | Unlocks Alyssa's Type B costume. (a substitute that does what the name says; the original code could not be decoded) | save data | CodeBreaker | Off |
| Unlock Costume Codes | **Alyssa-Type C** (`cb_costume_alyssa_c`) | Code Master, Lajos Szalay, Jay007, VirusPunk, Jarnold83 | code not decodable: substitute from the name | Unlocks Alyssa's Type C costume. (a substitute that does what the name says; the original code could not be decoded) | save data | CodeBreaker | Off |
| Unlock Costume Codes | **Cindy-All Types** (`cb_costume_cindy_all`) | Code Master, Lajos Szalay, Jay007, VirusPunk, Jarnold83 | code not decodable: substitute from the name | Unlocks Cindy's costumes: Type B and Type C. (a substitute that does what the name says; the original code could not be decoded) | save data | CodeBreaker | Off |
| Unlock Costume Codes | **Cindy-Type B** (`cb_costume_cindy_b`) | Code Master, Lajos Szalay, Jay007, VirusPunk, Jarnold83 | code not decodable: substitute from the name | Unlocks Cindy's Type B costume. (a substitute that does what the name says; the original code could not be decoded) | save data | CodeBreaker | Off |
| Unlock Costume Codes | **Cindy-Type C** (`cb_costume_cindy_c`) | Code Master, Lajos Szalay, Jay007, VirusPunk, Jarnold83 | code not decodable: substitute from the name | Unlocks Cindy's Type C costume. (a substitute that does what the name says; the original code could not be decoded) | save data | CodeBreaker | Off |
| Unlock Costume Codes | **David-All Types** (`cb_costume_david_all`) | Code Master, Lajos Szalay, Jay007, VirusPunk, Jarnold83 | code not decodable: substitute from the name | Unlocks David's costumes: Type B (the game has no Type C for David). (a substitute that does what the name says; the original code could not be decoded) | save data | CodeBreaker | Off |
| Unlock Costume Codes | **David-Type B** (`cb_costume_david_b`) | Code Master, Lajos Szalay, Jay007, VirusPunk, Jarnold83 | code not decodable: substitute from the name | Unlocks David's Type B costume. (a substitute that does what the name says; the original code could not be decoded) | save data | CodeBreaker | Off |
| Unlock Costume Codes | **David-Type C** (`cb_costume_david_c`) | Code Master, Lajos Szalay, Jay007, VirusPunk, Jarnold83 | **does not work on this disc** | Nothing: the game has no Type C costume for David (only Alyssa, Yoko and Cindy have one), so there is nothing to unlock; the published code could not be decoded either. | - | CodeBreaker | Off |
| Unlock Costume Codes | **George-All Types** (`cb_costume_george_all`) | Code Master, Lajos Szalay, Jay007, VirusPunk, Jarnold83 | code not decodable: substitute from the name | Unlocks George's costumes: Type B (the game has no Type C for George). (a substitute that does what the name says; the original code could not be decoded) | save data | CodeBreaker | Off |
| Unlock Costume Codes | **George-Type B** (`cb_costume_george_b`) | Code Master, Lajos Szalay, Jay007, VirusPunk, Jarnold83 | code not decodable: substitute from the name | Unlocks George's Type B costume. (a substitute that does what the name says; the original code could not be decoded) | save data | CodeBreaker | Off |
| Unlock Costume Codes | **George-Type C** (`cb_costume_george_c`) | Code Master, Lajos Szalay, Jay007, VirusPunk, Jarnold83 | **does not work on this disc** | Nothing: the game has no Type C costume for George (only Alyssa, Yoko and Cindy have one), so there is nothing to unlock; the published code could not be decoded either. | - | CodeBreaker | Off |
| Unlock Costume Codes | **Jim-All Types** (`cb_costume_jim_all`) | Code Master, Lajos Szalay, Jay007, VirusPunk, Jarnold83 | code not decodable: substitute from the name | Unlocks Jim's costumes: Type B (the game has no Type C for Jim). (a substitute that does what the name says; the original code could not be decoded) | save data | CodeBreaker | Off |
| Unlock Costume Codes | **Jim-Type B** (`cb_costume_jim_b`) | Code Master, Lajos Szalay, Jay007, VirusPunk, Jarnold83 | code not decodable: substitute from the name | Unlocks Jim's Type B costume. (a substitute that does what the name says; the original code could not be decoded) | save data | CodeBreaker | Off |
| Unlock Costume Codes | **Jim-Type C** (`cb_costume_jim_c`) | Code Master, Lajos Szalay, Jay007, VirusPunk, Jarnold83 | **does not work on this disc** | Nothing: the game has no Type C costume for Jim (only Alyssa, Yoko and Cindy have one), so there is nothing to unlock; the published code could not be decoded either. | - | CodeBreaker | Off |
| Unlock Costume Codes | **Kevin-All Types** (`cb_costume_kevin_all`) | Code Master, Lajos Szalay, Jay007, VirusPunk, Jarnold83 | code not decodable: substitute from the name | Unlocks Kevin's costumes: Type B (the game has no Type C for Kevin). (a substitute that does what the name says; the original code could not be decoded) | save data | CodeBreaker | Off |
| Unlock Costume Codes | **Kevin-Type B** (`cb_costume_kevin_b`) | Code Master, Lajos Szalay, Jay007, VirusPunk, Jarnold83 | code not decodable: substitute from the name | Unlocks Kevin's Type B costume. (a substitute that does what the name says; the original code could not be decoded) | save data | CodeBreaker | Off |
| Unlock Costume Codes | **Kevin-Type C** (`cb_costume_kevin_c`) | Code Master, Lajos Szalay, Jay007, VirusPunk, Jarnold83 | **does not work on this disc** | Nothing: the game has no Type C costume for Kevin (only Alyssa, Yoko and Cindy have one), so there is nothing to unlock; the published code could not be decoded either. | - | CodeBreaker | Off |
| Unlock Costume Codes | **Mark-All Types** (`cb_costume_mark_all`) | Code Master, Lajos Szalay, Jay007, VirusPunk, Jarnold83 | code not decodable: substitute from the name | Unlocks Mark's costumes: Type B (the game has no Type C for Mark). (a substitute that does what the name says; the original code could not be decoded) | save data | CodeBreaker | Off |
| Unlock Costume Codes | **Mark-Type B** (`cb_costume_mark_b`) | Code Master, Lajos Szalay, Jay007, VirusPunk, Jarnold83 | code not decodable: substitute from the name | Unlocks Mark's Type B costume. (a substitute that does what the name says; the original code could not be decoded) | save data | CodeBreaker | Off |
| Unlock Costume Codes | **Mark-Type C** (`cb_costume_mark_c`) | Code Master, Lajos Szalay, Jay007, VirusPunk, Jarnold83 | **does not work on this disc** | Nothing: the game has no Type C costume for Mark (only Alyssa, Yoko and Cindy have one), so there is nothing to unlock; the published code could not be decoded either. | - | CodeBreaker | Off |
| Unlock Costume Codes | **Yoko-All Types** (`cb_costume_yoko_all`) | Code Master, Lajos Szalay, Jay007, VirusPunk, Jarnold83 | code not decodable: substitute from the name | Unlocks Yoko's costumes: Type B and Type C. (a substitute that does what the name says; the original code could not be decoded) | save data | CodeBreaker | Off |
| Unlock Costume Codes | **Yoko-Type B** (`cb_costume_yoko_b`) | Code Master, Lajos Szalay, Jay007, VirusPunk, Jarnold83 | code not decodable: substitute from the name | Unlocks Yoko's Type B costume. (a substitute that does what the name says; the original code could not be decoded) | save data | CodeBreaker | Off |
| Unlock Costume Codes | **Yoko-Type C** (`cb_costume_yoko_c`) | Code Master, Lajos Szalay, Jay007, VirusPunk, Jarnold83 | code not decodable: substitute from the name | Unlocks Yoko's Type C costume. (a substitute that does what the name says; the original code could not be decoded) | save data | CodeBreaker | Off |
| Other Codes | **1-Hit Deaths (Enemies)** (`one_hit_kills`) | Code Master, Lajos Szalay, Jay007, VirusPunk, Jarnold83 | adapted to this disc | Any hit kills an enemy. | game code | CodeBreaker | Off |
| Other Codes | **Animation Sequence Picker Player 1** (`bh_animation_picker`) | bungholio | works as written | Player 1's animation byte (0x004A67CB) is held at the value below. Author: "Use a joker with it. Different values made different things happen. With Cindy I made her throw nothing, limp, collapse, walk backwards, and whatever else. Mostly useless." | game data | GameShark | Off |
| Other Codes | **Animation Sequence Picker Player 1: value** (`bh_animation_picker_value`) |  | setting | The ?? value (0-255) of Animation Sequence Picker Player 1. | - |  | 0 |
| Other Codes | **Become A Zombie After Death (Offline Mode)** (`cb_zombie_after_death`) | Code Master, Lajos Szalay, Jay007, VirusPunk, Jarnold83 | adapted to this disc | When you die offline you turn into a playable zombie instead of "YOU DIED". | game code | CodeBreaker | Off |
| Other Codes | **Don't Become A Zombie Over Time** (`cb_no_zombie_over_time`) | Code Master, Lajos Szalay, Jay007, VirusPunk, Jarnold83 | adapted to this disc | The virus gauge no longer rises with time (all characters). | game code | CodeBreaker | Off |
| Other Codes | **Don't Become A Zombie When Bitten** (`cb_no_zombie_when_bitten`) | Code Master, Lajos Szalay, Jay007, VirusPunk, Jarnold83 | adapted to this disc | Bites no longer raise the virus gauge (all characters). | game code | CodeBreaker | Off |
| Other Codes | **Enemies Can't Touch Player 1** (`bh_enemies_cant_touch`) | bungholio | works as written | Enemies cannot hit or grab Player 1 (byte 0x004A67D2 = 0x20). | game data | GameShark | Off |
| Other Codes | **Enemies Don't Damage You With Attacks** (`cb_enemies_dont_damage`) | Code Master, Lajos Szalay, Jay007, VirusPunk, Jarnold83 | adapted to this disc | Enemy attacks do no HP damage (player and partners); grabs and bites still infect. | game code | CodeBreaker | Off |
| Other Codes | **Enemies Don't Notice Player 1 (Because you are dead) (L2+UP=ON, L2+DOWN=OFF)** (`bh_enemies_dont_notice`) | bungholio | works as written | L2+Up (exactly) sets byte 0x004A67D1 to 1, L2+Down sets it to 0, as written. Author: "WARNING! THIS IS BUGGY": zombies ignore you, other players don't; you cannot open the start menu or fire while it is set; you die if a movie plays. | game data | GameShark | Off |
| Other Codes | **Extra Ammo** (`cb_extra_ammo`) | Code Master, Lajos Szalay, Jay007, VirusPunk, Jarnold83 | adapted to this disc | Each shot adds a round instead of using one. | game code | CodeBreaker | Off |
| Other Codes | **Have All Files** (`bh_have_all_files`) | bungholio | works as written | All 16 files of the current scenario are yours (16-bit 0x004B9C80 = FFFF). Author: they count as completed events at the end. | save data, through the results screen | GameShark | Off |
| Other Codes | **Infinite Ammo** (`infinite_ammo`) | Code Master, Lajos Szalay, Jay007, VirusPunk, Jarnold83 | adapted to this disc | Firing does not use up rounds. | game code | CodeBreaker | Off |
| Other Codes | **Infinite Health** (`cb_infinite_health`) | Code Master, Lajos Szalay, Jay007, VirusPunk, Jarnold83 | adapted to this disc | Every character's HP is set to 9999 while its death check runs (players and partners). | game code | CodeBreaker | Off |
| Other Codes | **Infinite Item Usage** (`infinite_items`) | Code Master, Lajos Szalay, Jay007, VirusPunk, Jarnold83 | adapted to this disc | Using a consumable item does not use it up (everyone). | game code | CodeBreaker | Off |
| Other Codes | **Infinite Time** (`cb_infinite_time`) | Code Master, Lajos Szalay, Jay007, VirusPunk, Jarnold83 | **does not work on this disc** | Nothing in single play: its instruction is in the game's online event-script code, which offline play never runs (online play is not available yet). | - | CodeBreaker | Off |
| Other Codes | **Infinite: Press L2 To Reset Escape Time** (`mc_reset_escape_time_l2`) | MadCatz | adapted to this disc | While you hold L2 (and nothing else), the event timers stop counting down. | game code | GameShark | Off |
| Other Codes | **Max Infinite Ammo** (`cb_max_infinite_ammo`) | Code Master, Lajos Szalay, Jay007, VirusPunk, Jarnold83 | adapted to this disc | The loaded rounds drop to 1 and then stay at 1 (not 99). | game code | CodeBreaker | Off |
| Other Codes | **Number Of Players Present** (`bh_number_of_players`) | bungholio | works as written | The number of players (byte 0x004BAEA0). Author: "Set it to 1 for 1 player, 2 for 2 players, and so on. I doubt 5 works though ... It's basically like controlling 2 of yourself." | game data | GameShark | Off |
| Other Codes | **P1 Press L1+Select For Infection 100%** (`cb_l1_select_infection`) | Code Master, Lajos Szalay, Jay007, VirusPunk, Jarnold83 | adapted to this disc | L1+Select (exactly) makes the gauge update store a huge value: the gauge goes to 100 % and the character dies ("YOU DIED", unless Become A Zombie After Death is on). With nothing pressed the original instruction is put back, as written. It acts on every character whose gauge updates meanwhile. | game code | CodeBreaker | Off |
| Other Codes | **Player 1 Alternative Costume Modifier** (`bh_p1_alt_costume`) | bungholio | works as written | Player 1's alternative-costume byte (0x004A67EC). Author: "There's probably a few more higher values, but I doubt it goes above 5." | game data | GameShark | Off |
| Other Codes | **Player 1 Character Model Modifier** (`bh_p1_model`) | bungholio | works as written | Player 1's model (16-bit 0x004A67E4). Author: "this only modifies your character's appearance, you'll still sound like and have the same animations of the player you pick." The entries he marks "CANNOT LOAD" (0009, 000f, 0010, 0015, 0022, 0026, 002e, 003a, 003d, 003e, 0043-0045, 0047, 0048, 004b-004f) and the empty 0050 are left out. | game data | GameShark | Off |
| Other Codes | **Player 1 Character Type Modifier** (`bh_p1_char_type`) | bungholio | works as written | Player 1's character (byte 0x004A67C8). Author: "08 or higher = don't try it, they don't exist so the game won't start": only 00-07 are offered. | game data | GameShark | Off |
| Other Codes | **Player 1 Damage Modifier [Or is It Multiplier?]** (`bh_p1_damage`) | bungholio | works as written | Player 1's damage multiplier (float 0x004A67F4, normally 1.0). Author: "I set it to 4FFFFFFF and every enemy died no matter how I hit them ... You can't use this to open doors in 1 hit though". | game data | GameShark | Off |
| Other Codes | **Player 1 Speed Modifier #1** (`bh_p1_speed_1`) | bungholio | works as written | Player 1's speed value #1 (float 0x004A67D8, normally 1.0). Author: "If you turn while moving you will move at normal speed." | game data | GameShark | Off |
| Other Codes | **Player 1 Speed Modifier #2** (`bh_p1_speed_2`) | bungholio | works as written | Player 1's speed factor #2 (float 0x004A67F0, normally 1.0). Author: "Also a speed code, but you don't move at normal speed while turning." | game data | GameShark | Off |
| Other Codes | **Player 1 Status Modifier** (`bh_p1_status`) | bungholio | works as written | Player 1's status byte (0x004A67D0). Author: "Some of them even killed me instantly, but I don't remember which ones. It's useless." | game data | GameShark | Off |
| Other Codes | **Player 1 Virus Gauge Modifier #1** (`bh_p1_virus_gauge_1`) | bungholio | works as written | Player 1's virus gauge (0x004A67DC) is held at the percentage below, computed from the game's own maximum for the character. Author: "this forces your virus gauge to 0 always" (with 0). | game data | GameShark | Off |
| Other Codes | **Player 1 Virus Gauge Modifier #1: value (%)** (`bh_p1_virus_gauge_1_value`) |  | setting | The gauge value for Player 1 Virus Gauge Modifier #1, in percent of the character's maximum (0-99; 100 % kills the character, so it is not offered). | - |  | 0 |
| Other Codes | **Player 1 Virus Gauge Modifier #2** (`bh_p1_virus_gauge_2`) | bungholio | works as written | Player 1's virus word #2 (0x004A67E8) is held at the value you pick. Author: "I think it stops the virus gauge from increasing ... but it's still useless." | game data | GameShark | Off |
| Other Codes | **Player 1 Walk Through Walls** (`bh_walk_through_walls`) | bungholio | works as written | Player 1 walks through walls (0x004A68E0 and 0x004A68FC = FFFFFFFF). Author: if a room keeps pushing you back out of the door you came in, run the other way when you enter. | game data | GameShark | Off |
| Other Codes | **Rapid Fire Player 1** (`bh_rapid_fire`) | bungholio | works as written | While you hold R1+Cross (exactly), Player 1 fires continuously (byte 0x004A67D3 = FF). | game data | GameShark | Off |
| Other Codes | **Unlock All NPC's** (`cb_unlock_all_npcs`) | Code Master, Lajos Szalay, Jay007, VirusPunk, Jarnold83 | adapted to this disc | The extra (NPC) characters can be chosen at the character select. | save data | CodeBreaker | Off |
| Other Codes | **Unlock All Scenarios** (`cb_unlock_all_scenarios`) | Code Master, Lajos Szalay, Jay007, VirusPunk, Jarnold83 | **does not work on this disc** | Nothing: on this disc it would write an unused save word next to the scenario word. MadCatz' Unlock All Levels does unlock all scenarios. | - | CodeBreaker | Off |
| Other Codes | **Unlock Infinity Mode** (`cb_unlock_infinity_mode`) | Code Master, Lajos Szalay, Jay007, VirusPunk, Jarnold83 | adapted to this disc | Unlocks the Infinity mode (0x0031FB7F bits 0x01 and 0x04, see MadCatz' Unlock Infinity Mode). | save data | CodeBreaker | Off |
| Kept from older versions | **No Infection / Freeze Infection** (`no_infection`) |  | kept from older versions | A switch kept from 1.0 / 1.1, with the meaning it had in 1.1.0: turns on Don't Become A Zombie Over Time and When Bitten together (the virus gauge can no longer rise), and with Infection Freeze Value 0 (below, the default) and the Action Replay MAX master code On it also holds Player 1's virus gauge at 0 (Codejunkies' Zero Virus Gauge). With another freeze value the gauge stays where it is. | game code | CodeBreaker | Off |
| Kept from older versions | **Infection Freeze Value (%)** (`infection_freeze_value`) |  | kept from older versions | A value kept from 1.0 / 1.1, with the meaning it had in 1.1.0: with No Infection / Freeze Infection On, 0 also holds the virus gauge at 0 (Codejunkies' Zero Virus Gauge; needs the Action Replay MAX and the CodeBreaker master code). 1-100: the gauge stays where it is (the two Don't Become A Zombie codes stop it rising). To hold the gauge at a chosen value use Player 1 Virus Gauge Modifier #1 and its own value above. | - |  | 0 |
| Kept from older versions | **Max Inventory** (`max_inventory`) |  | kept from older versions | Does nothing: there is no such code in the list. Kept so your saved setting stays valid. | - |  | Off |

## Building from source

The release zip holds the built mod; building it yourself is only needed to change it. You need clang with the MIPS
target (LLVM 18.1.8 is the last official Windows release that has it), `ld.lld`, and `RecompModTool` from
[N64Recomp](https://github.com/N64Recomp/N64Recomp). From Git Bash, in this folder:

```bash
mingw32-make OS=Linux CC=<path to clang.exe> LD=<path to ld.lld.exe> RECOMP_MOD_TOOL=<path to RecompModTool.exe>
```

The output is `build/REO_Cheats.nrm`. To try a build, use **Mods → Install Mods** and pick this folder's `mod.json`
(the folder is copied into the mods folder), or pack `mod.json`, `icon.png` and the `.nrm` into a zip as in the
release. `syms/reo.syms.toml` lists no functions: the mod calls no game functions.

`mod.json`, `mod.toml`, `manifest.json` and `src/gen_cheats.h` are generated by `tools/gen_manifests.py` from
`tools/cheat_list.py` (every option, its status and its evidence) and from the cheat list files the codes were copied
from. Those list files are not part of this repository, so the generated files are included as they are; the mod
builds from them with `make` alone.

## Credits

- **Cheat codes** (GameHacking.org): **Codejunkies**; **Code Master, Lajos Szalay, Jay007, VirusPunk, Jarnold83**;
  **MadCatz**; **bungholio**; the Item Values tables by **nobody**.
- The mod's layout is modeled on ProxyMM's
  [Cheats](https://github.com/garrettjoecox/ProxyMM_RecompMods/tree/main/packages/Cheats) for Zelda 64: Recompiled. No
  code or cheats are taken from it.
- **Capcom** - Resident Evil Outbreak, the original game.
- This mod was built by RaccoonRecomp with AI-assisted programming (Claude, Anthropic).

## Legal

- This is an **unofficial fan project**. It is **not affiliated with, endorsed or sponsored by Capcom**.
- *Resident Evil*, *Resident Evil Outbreak* and all related names, characters and content are trademarks and property
  of Capcom. **All copyright and credit for the game belong to Capcom.** The names are used only to say which game this
  mod works with.
- **You need your own legal copy of the game.** This mod contains **no disc image and no game files**. Like the cheat
  codes it is made from, it holds the game addresses it changes and the few original instruction words it puts back
  when a cheat is switched off.
