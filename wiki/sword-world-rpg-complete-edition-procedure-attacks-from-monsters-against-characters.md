---
page_id: sword-world-rpg-complete-edition-procedure-attacks-from-monsters-against-characters
page_kind: procedure
summary: Complete Attacks From Monsters Against Characters: 5 ordered step(s), 0 decision point(s), and 10 table/formula/example reference(s) from raw/Sword World RPG - Complete Edition.pdf.
page_family: procedure-guide
sources: raw/Sword World RPG - Complete Edition.pdf
updated: 2026-07-01
domain: sword-world-rpg-complete-edition
category_path: procedures/sword-world-rpg-complete-edition
source_id: Sword World RPG - Complete Edition.pdf
aliases: complete-attacks-from-monsters-against-characters, attacks-from-monsters-against-characters
projection_coverage: procedure-sword-world-rpg-complete-edition-procedure-attacks-from-monsters-against-characters@5a336fde2114b9914ebbb2f7a5827a0b
---

# Attacks From Monsters Against Characters

From [[sword-world-rpg-complete-edition]].

## Goal

- Complete Attacks From Monsters Against Characters.

## Procedure Steps

1. **Hit (Evasion) Checks** (`validate`) - evidence section [[sword-world-rpg-complete-edition-section-attacks-from-monsters-against-characters-4-6-1-hit-evasion-checks-6637c605]].
   - This check is also made with a success roll. _(Sword World RPG - Complete Edition.pdf (source-range-0d48087c-01315))_
   - The target score is still different for each monster, but it's called the monster's attack points . _(Sword World RPG - Complete Edition.pdf (source-range-0d48087c-01316))_
   - The baseline score is the character's evasion speed . _(Sword World RPG - Complete Edition.pdf (source-range-0d48087c-01316))_
2. **Damage Dealt by Monsters** (`step`) - evidence section [[sword-world-rpg-complete-edition-section-attacks-from-monsters-against-characters-monsters-77a3fb28]].
   - Strike points are fixed and do not change. _(Sword World RPG - Complete Edition.pdf (source-range-0d48087c-01327))_
   - A goblin has 7 strike points. _(Sword World RPG - Complete Edition.pdf (source-range-0d48087c-01329))_
3. **Defense Rolls** (`generate`) - evidence section [[sword-world-rpg-complete-edition-section-attacks-from-monsters-against-characters-4-6-3-defense-rolls-6e7df75a]].
   - For example, if your defense power is 7, you would look at key number column 7 with on the Rating Table . _(Sword World RPG - Complete Edition.pdf (source-range-0d48087c-01331))_
   - This process is specifically called a defense roll . _(Sword World RPG - Complete Edition.pdf (source-range-0d48087c-01334))_
   - Then, look for the number under the appropriate column. _(Sword World RPG - Complete Edition.pdf (source-range-0d48087c-01334))_
4. **Damage Reduction** (`generate`) - evidence section [[sword-world-rpg-complete-edition-section-attacks-from-monsters-against-characters-4-6-4-damage-reduction-b3691cec]].
   - Characters can also reduce damage using their adventurer level . _(Sword World RPG - Complete Edition.pdf (source-range-0d48087c-01344))_
   - The result of your defense roll plus this damage reduction equals the fi nal amount of damage your character can reduce. _(Sword World RPG - Complete Edition.pdf (source-range-0d48087c-01344))_
   - However, if the result of your defense roll is double ones , your character's damage reduction is meaningless . _(Sword World RPG - Complete Edition.pdf (source-range-0d48087c-01345))_
5. **Final Damage** (`generate`) - evidence section [[sword-world-rpg-complete-edition-section-attacks-from-monsters-against-characters-4-6-5-final-damage-cb8f53e4]].
   - The final damage your character suffers from a monster equals the monster's strike points minus the result of your defense roll plus your character's damage reduction . _(Sword World RPG - Complete Edition.pdf (source-range-0d48087c-01347))_
   - If the result of Ducard II's defense roll is 0 (roll 3) or 6 (roll 12), respectively, the final damage he will suffer is calculated to be: _(Sword World RPG - Complete Edition.pdf (source-range-0d48087c-01350))_
   - If the defense roll came up double ones , no such calculation would be made, and the goblin's 7 strike points would be the damage. _(Sword World RPG - Complete Edition.pdf (source-range-0d48087c-01352))_

## Tables And Formulas

- `formula`: evasion speed + 2D ≥ monster's attack points → evasion success (monster's attack fails) _(Sword World RPG - Complete Edition.pdf (source-range-0d48087c-01317))_
- `table`: Table 4-3: Rating Table, Key Number _(Sword World RPG - Complete Edition.pdf (source-range-0d48087c-01332))_
- `formula`: Final damage = monster's strike points - (defense roll result + damage reduction) _(Sword World RPG - Complete Edition.pdf (source-range-0d48087c-01348))_
- `table`: 7 (goblin's strike points) - {0 (defense roll) +2 (damage reduction)} = 5 _(Sword World RPG - Complete Edition.pdf (source-range-0d48087c-01351))_
- `rule`: If a monster's attack hits (or if a character fails to evade), you must look for the base damage dealt by the monster. _(Sword World RPG - Complete Edition.pdf (source-range-0d48087c-01326))_
- `rule`: Characters can reduce the damage they receive from monsters by means of armor. _(Sword World RPG - Complete Edition.pdf (source-range-0d48087c-01331))_
- `rule`: When making a defense roll, if your roll is double ones, that means that you've been hit extremely hard. _(Sword World RPG - Complete Edition.pdf (source-range-0d48087c-01338))_
- `rule`: When making a defense roll, criticals do not occur like they do with a strike roll. _(Sword World RPG - Complete Edition.pdf (source-range-0d48087c-01340))_
- `worked-example`: Suppose Ducard II's defense roll came up 12 (double sixes!). The number on row 12 under key number column 7 is 6 . Unlik _(Sword World RPG - Complete Edition.pdf (source-range-0d48087c-01342))_
- `rule`: You cannot roll the dice again to increase this number further. _(Sword World RPG - Complete Edition.pdf (source-range-0d48087c-01342))_

## Completion Check

- The procedure is complete when every step output has been recorded or validated.

## Source Trail

- Source manifest: [[sword-world-rpg-complete-edition]]
- Source section: [[sword-world-rpg-complete-edition-section-attacks-from-monsters-against-characters-a9a9211c]]
