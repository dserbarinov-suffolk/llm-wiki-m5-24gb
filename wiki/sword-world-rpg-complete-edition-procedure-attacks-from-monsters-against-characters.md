---
page_id: sword-world-rpg-complete-edition-procedure-attacks-from-monsters-against-characters
page_kind: procedure
summary: Complete Attacks From Monsters Against Characters: 5 ordered step(s), 1 decision point(s), and 10 table/formula/example reference(s) from raw/Sword World RPG - Complete Edition.pdf.
page_family: procedure-guide
sources: raw/Sword World RPG - Complete Edition.pdf
updated: 2026-07-06
domain: sword-world-rpg-complete-edition
category_path: procedures/sword-world-rpg-complete-edition
source_id: Sword World RPG - Complete Edition.pdf
aliases: complete-attacks-from-monsters-against-characters, attacks-from-monsters-against-characters
projection_coverage: procedure-sword-world-rpg-complete-edition-procedure-attacks-from-monsters-against-characters@ef8fade12d952b8cff31a9050834d167
---

# Attacks From Monsters Against Characters

From [[sword-world-rpg-complete-edition]].

## Goal

- Complete Attacks From Monsters Against Characters.

## Procedure Steps

1. **Hit (Evasion) Checks** (`validate`) - evidence section [[sword-world-rpg-complete-edition-section-attacks-from-monsters-against-characters-4-6-1-hit-evasion-checks-2573af2b]].
   - This check is also made with a success roll. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01315))_
   - The baseline score is the character's evasion speed . _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01316))_
   - The target score is still different for each monster, but it's called the monster's attack points . _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01316))_
2. **Damage Dealt by Monsters** (`step`) - evidence section [[sword-world-rpg-complete-edition-section-attacks-from-monsters-against-characters-monsters-7c4009e9]].
   - Strike points are fixed and do not change. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01327))_
   - A goblin has 7 strike points. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01329))_
3. **Defense Rolls** (`generate`) - evidence section [[sword-world-rpg-complete-edition-section-attacks-from-monsters-against-characters-4-6-3-defense-rolls-4d667a1e]].
   - For example, if your defense power is 7, you would look at key number column 7 with on the Rating Table . _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01331))_
   - This process is specifically called a defense roll . _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01334))_
   - Then, look for the number under the appropriate column. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01334))_
4. **Damage Reduction** (`generate`) - evidence section [[sword-world-rpg-complete-edition-section-attacks-from-monsters-against-characters-4-6-4-damage-reduction-50ad179f]].
   - Characters can also reduce damage using their adventurer level . _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01344))_
   - The result of your defense roll plus this damage reduction equals the fi nal amount of damage your character can reduce. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01344))_
   - No matter how high your character's damage reduction (adventurer level), that damage cannot be reduced at all. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01345))_
5. **Final Damage** (`generate`) - evidence section [[sword-world-rpg-complete-edition-section-attacks-from-monsters-against-characters-4-6-5-final-damage-e3f2c80c]].
   - The final damage your character suffers from a monster equals the monster's strike points minus the result of your defense roll plus your character's damage reduction . _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01347))_
   - If the result of Ducard II's defense roll is 0 (roll 3) or 6 (roll 12), respectively, the final damage he will suffer is calculated to be: _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01350))_
   - If the defense roll came up double ones , no such calculation would be made, and the goblin's 7 strike points would be the damage. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01352))_

## Decision Points

- Characters can also reduce damage using their adventurer level . The result of your defense roll plus this damage reduction equals the fi nal amount of damage your character can reduce. However, if the result of your defense roll is double ones , your character's damage reduction is meaningless . No matter how high your character's damage reduction (adventurer level), that damage cannot be reduced at all. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01344, source-range-e5870dca-01345))_

## Tables And Formulas

- `formula`: [[sword-world-rpg-complete-edition-section-attacks-from-monsters-against-characters-b80c17b0]]#atom-technical-atom-b4c7cd046c7b408e evasion speed + 2D ≥ monster's attack points → evasion success (monster's attack fails) _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01317))_
- `table`: [[sword-world-rpg-complete-edition-section-attacks-from-monsters-against-characters-b80c17b0]]#atom-technical-atom-2e8355d4c556f4f6 Table 4-3: Rating Table, Key Number _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01332))_
- `formula`: [[sword-world-rpg-complete-edition-section-attacks-from-monsters-against-characters-b80c17b0]]#atom-technical-atom-d041994e3272798f Final damage = monster's strike points - (defense roll result + damage reduction) _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01348))_
- `table`: [[sword-world-rpg-complete-edition-section-attacks-from-monsters-against-characters-b80c17b0]]#atom-technical-atom-ae2227d2b1a0bbb3 7 (goblin's strike points) - {0 (defense roll) +2 (damage reduction)} = 5 _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01351))_
- `rule`: [[sword-world-rpg-complete-edition-section-attacks-from-monsters-against-characters-b80c17b0]]#atom-technical-atom-3d380bee0ed56709 If a monster's attack hits (or if a character fails to evade), you must look for the base damage dealt by the monster. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01326))_
- `rule`: [[sword-world-rpg-complete-edition-section-attacks-from-monsters-against-characters-b80c17b0]]#atom-technical-atom-2088dd14041b22e6 Characters can reduce the damage they receive from monsters by means of armor. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01331))_
- `rule`: [[sword-world-rpg-complete-edition-section-attacks-from-monsters-against-characters-b80c17b0]]#atom-technical-atom-281b8ed0ce7ef210 When making a defense roll, if your roll is double ones, that means that you've been hit extremely hard. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01338))_
- `rule`: [[sword-world-rpg-complete-edition-section-attacks-from-monsters-against-characters-b80c17b0]]#atom-technical-atom-a81e2ce848646ac2 When making a defense roll, criticals do not occur like they do with a strike roll. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01340))_
- `worked-example`: [[sword-world-rpg-complete-edition-section-attacks-from-monsters-against-characters-b80c17b0]]#atom-technical-atom-b90b4b8d1546ace3 Suppose Ducard II's defense roll came up 12 (double sixes!). The number on row 12 under key number column 7 is 6 . Unlik _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01342))_
- `rule`: [[sword-world-rpg-complete-edition-section-attacks-from-monsters-against-characters-b80c17b0]]#atom-technical-atom-e93f513a1b1c3b45 You cannot roll the dice again to increase this number further. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01342))_

## Completion Check

- The procedure is complete when every step output has been recorded or validated.

## Source Trail

- Source manifest: [[sword-world-rpg-complete-edition]]
- Source section: [[sword-world-rpg-complete-edition-section-attacks-from-monsters-against-characters-b80c17b0]]
