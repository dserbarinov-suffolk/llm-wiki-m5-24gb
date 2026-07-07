---
page_id: sword-world-rpg-complete-edition-procedure-attacks-from-monsters-against-characters
page_kind: procedure
summary: Complete Attacks From Monsters Against Characters: 5 ordered step(s), 2 decision point(s), and 9 table/formula/example reference(s) from raw/Sword World RPG - Complete Edition.pdf.
page_family: procedure-guide
sources: raw/Sword World RPG - Complete Edition.pdf
updated: 2026-07-07
domain: sword-world-rpg-complete-edition
category_path: procedures/sword-world-rpg-complete-edition
source_id: Sword World RPG - Complete Edition.pdf
aliases: complete-attacks-from-monsters-against-characters, attacks-from-monsters-against-characters
projection_coverage: procedure-sword-world-rpg-complete-edition-procedure-attacks-from-monsters-against-characters@1cbfde6e856c433ee7345b775cf85919
---

# Attacks From Monsters Against Characters

From [[sword-world-rpg-complete-edition]].

## Goal

- Complete Attacks From Monsters Against Characters.

## Procedure Steps

1. **Hit (Evasion) Checks** (`validate`) - evidence section [[sword-world-rpg-complete-edition-section-attacks-from-monsters-against-characters-4-6-1-hit-evasion-checks-50862aac]].
   - This check is also made with a success roll. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01284))_
   - The baseline score is the character's evasion speed . _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01285))_
   - The target score is still different for each monster, but it's called the monster's attack points . _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01285))_
2. **Damage Dealt by Monsters** (`step`) - evidence section [[sword-world-rpg-complete-edition-section-attacks-from-monsters-against-characters-monsters-da96211d]].
   - Strike points are fixed and do not change. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01296))_
   - A goblin has 7 strike points. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01298))_
3. **Defense Rolls** (`generate`) - evidence section [[sword-world-rpg-complete-edition-section-attacks-from-monsters-against-characters-4-6-3-defense-rolls-76f9adb4]].
   - For example, if your defense power is 7, you would look at key number column 7 with on the Rating Table . _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01300))_
   - This process is specifically called a defense roll . _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01302))_
   - Then, look for the number under the appropriate column. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01302))_
4. **Damage Reduction** (`generate`) - evidence section [[sword-world-rpg-complete-edition-section-attacks-from-monsters-against-characters-4-6-4-damage-reduction-6a1ec021]].
   - The result of your defense roll plus this damage reduction equals the fi nal amount of damage your character can reduce. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01312))_
   - Characters can also reduce damage using their adventurer level . _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01312))_
   - No matter how high your character's damage reduction (adventurer level), that damage cannot be reduced at all. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01313))_
5. **Final Damage** (`generate`) - evidence section [[sword-world-rpg-complete-edition-section-attacks-from-monsters-against-characters-4-6-5-final-damage-e115436c]].
   - The final damage your character suffers from a monster equals the monster's strike points minus the result of your defense roll plus your character's damage reduction . _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01315))_
   - Final damage = monster's strike points - (defense roll result + damage reduction) _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01316))_
   - If the result of Ducard II's defense roll is 0 (roll 3) or 6 (roll 12), respectively, the final damage he will suffer is calculated to be: _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01318))_

## Decision Points

- Characters can also reduce damage using their adventurer level . The result of your defense roll plus this damage reduction equals the fi nal amount of damage your character can reduce. However, if the result of your defense roll is double ones , your character's damage reduction is meaningless . No matter how high your character's damage reduction (adventurer level), that damage cannot be reduced at all. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01312, source-range-e5870dca-01313))_
- If the defense roll came up double ones , no such calculation would be made, and the goblin's 7 strike points would be the damage. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01320))_

## Tables And Formulas

- `formula`: [[sword-world-rpg-complete-edition-section-attacks-from-monsters-against-characters-033cf8f5]]#atom-technical-atom-c69504e08ba002bd evasion speed + 2D ≥ monster's attack points → evasion success (monster's attack fails) _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01286))_
- `rule`: [[sword-world-rpg-complete-edition-section-attacks-from-monsters-against-characters-033cf8f5]]#atom-technical-atom-6fbe8df285f74f14 Characters can reduce the damage they receive from monsters by means of armor. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01300))_
- `table`: [[sword-world-rpg-complete-edition-section-attacks-from-monsters-against-characters-033cf8f5]]#atom-technical-atom-83ad89087c79a40d Table 4-3: Rating Table, Key Number _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01301))_
- `table`: [[sword-world-rpg-complete-edition-section-attacks-from-monsters-against-characters-033cf8f5]]#atom-technical-atom-359adc15fff571da 7 (goblin's strike points) - {0 (defense roll) +2 (damage reduction)} = 5 _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01319))_
- `rule`: [[sword-world-rpg-complete-edition-section-attacks-from-monsters-against-characters-033cf8f5]]#atom-technical-atom-05a3cbbd7f350b20 If a monster's attack hits (or if a character fails to evade), you must look for the base damage dealt by the monster. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01295))_
- `rule`: [[sword-world-rpg-complete-edition-section-attacks-from-monsters-against-characters-033cf8f5]]#atom-technical-atom-d76016fe39ffe28a When making a defense roll, if your roll is double ones, that means that you've been hit extremely hard. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01306))_
- `rule`: [[sword-world-rpg-complete-edition-section-attacks-from-monsters-against-characters-033cf8f5]]#atom-technical-atom-57d2212b25b347e8 When making a defense roll, criticals do not occur like they do with a strike roll. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01308))_
- `worked-example`: [[sword-world-rpg-complete-edition-section-attacks-from-monsters-against-characters-033cf8f5]]#atom-technical-atom-49ef67efed28776a Suppose Ducard II's defense roll came up 12 (double sixes!). The number on row 12 under key number column 7 is 6 . Unlik _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01310))_
- `rule`: [[sword-world-rpg-complete-edition-section-attacks-from-monsters-against-characters-033cf8f5]]#atom-technical-atom-2f1efcd18a64b95b You cannot roll the dice again to increase this number further. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01310))_

## Completion Check

- The procedure is complete when every step output has been recorded or validated.

## Source Trail

- Source manifest: [[sword-world-rpg-complete-edition]]
- Source section: [[sword-world-rpg-complete-edition-section-attacks-from-monsters-against-characters-033cf8f5]]
