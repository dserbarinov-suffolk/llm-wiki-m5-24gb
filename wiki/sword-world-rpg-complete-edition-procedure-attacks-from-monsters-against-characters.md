---
page_id: sword-world-rpg-complete-edition-procedure-attacks-from-monsters-against-characters
page_kind: procedure
summary: Complete Attacks From Monsters Against Characters: 5 ordered step(s), 1 decision point(s), 4 authoritative dependency reference(s), 5 review-only dependency reference(s), projection partial from raw/Sword World RPG - Complete Edition.pdf.
page_family: procedure-guide
sources: raw/Sword World RPG - Complete Edition.pdf
updated: 2026-07-07
domain: sword-world-rpg-complete-edition
category_path: procedures/sword-world-rpg-complete-edition
source_id: Sword World RPG - Complete Edition.pdf
aliases: complete-attacks-from-monsters-against-characters, attacks-from-monsters-against-characters
projection_coverage: procedure-sword-world-rpg-complete-edition-procedure-attacks-from-monsters-against-characters@cae03056e6079bbf28d8beb57f28d08d
---

# Attacks From Monsters Against Characters

From [[sword-world-rpg-complete-edition]].

## Goal

- Complete Attacks From Monsters Against Characters.

## Procedure Steps

1. **Hit (Evasion) Checks** (`validate`) - evidence section [[sword-world-rpg-complete-edition-section-attacks-from-monsters-against-characters-4-6-1-hit-evasion-checks-20bd7e57]].
   - This check is also made with a success roll. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01267))_
   - The target score is still different for each monster, but it's called the monster's attack points . _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01268))_
   - The baseline score is the character's evasion speed . _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01268))_
   - evasion speed + 2D < monster's attack points → evasion failure (monster's attack hits) _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01270))_
   - ※ Double sixes will automatically evade, and double ones will automatically fail _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01271))_
   - Since this is a success roll, double sixes and double ones are automatic successes and automatic failures , respectively. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01272))_
   - Ducard II has an evasion speed of 5 (fighter level 2, agility bonus +2, has a shield). _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01274))_
   - On the other hand, the goblin has 10 attack points. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01274))_
   - 5+4= 9 , which is short of the target score (the goblin's attack points) of 10. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01275))_
   - The player rolls the dice to determine if they evade the goblin's attack. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01275))_
   - Evidence dependencies:
     - `formula`: [[sword-world-rpg-complete-edition-section-attacks-from-monsters-against-characters-4-6-1-hit-evasion-checks-20bd7e57]]#atom-technical-atom-da97de2c158d3794 evasion speed + 2D ≥ monster's attack points → evasion success (monster's attack fails) _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01269))_
2. **Damage Dealt by Monsters** (`step`) - evidence section [[sword-world-rpg-complete-edition-section-attacks-from-monsters-against-characters-monsters-8c7835a7]].
   - Strike points are fixed and do not change. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01279))_
   - A goblin has 7 strike points. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01281))_
   - Evidence dependencies:
     - `rule`: [[sword-world-rpg-complete-edition-section-attacks-from-monsters-against-characters-monsters-8c7835a7]]#atom-technical-atom-9c5043656ae75f0a If a monster's attack hits (or if a character fails to evade), you must look for the base damage dealt by the monster. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01278))_
3. **Defense Rolls** (`generate`) - evidence section [[sword-world-rpg-complete-edition-section-attacks-from-monsters-against-characters-4-6-3-defense-rolls-caf97a1f]].
   - For example, if your defense power is 7, you would look at key number column 7 with on the Rating Table . _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01283))_
   - This process is specifically called a defense roll . _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01285))_
   - Then, look for the number under the appropriate column. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01285))_
   - Since Ducard II has a defense power of 7 , we'll use key number column 7. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01287))_
   - This is the damage that Ducard II is able to prevent with his armor. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01287))_
   - The number on row 3 under key number column 7 is 0 . _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01287))_
   - In this case, your character cannot reduce the monster's damage (strike points) at all. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01289))_
   - Evidence dependencies:
     - `rule`: [[sword-world-rpg-complete-edition-section-attacks-from-monsters-against-characters-4-6-3-defense-rolls-caf97a1f]]#atom-technical-atom-36e2d85a1dff3d90 Characters can reduce the damage they receive from monsters by means of armor. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01283))_
     - `rule`: [[sword-world-rpg-complete-edition-section-attacks-from-monsters-against-characters-4-6-3-defense-rolls-caf97a1f]]#atom-technical-atom-2640ab7439ba915d When making a defense roll, if your roll is double ones, that means that you've been hit extremely hard. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01289))_
4. **Damage Reduction** (`generate`) - evidence section [[sword-world-rpg-complete-edition-section-attacks-from-monsters-against-characters-4-6-4-damage-reduction-42ac6233]].
   - The result of your defense roll plus this damage reduction equals the fi nal amount of damage your character can reduce. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01295))_
   - Characters can also reduce damage using their adventurer level . _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01295))_
   - No matter how high your character's damage reduction (adventurer level), that damage cannot be reduced at all. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01296))_
   - However, if the result of your defense roll is double ones , your character's damage reduction is meaningless . _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01296))_
5. **Final Damage** (`generate`) - evidence section [[sword-world-rpg-complete-edition-section-attacks-from-monsters-against-characters-4-6-5-final-damage-bb968207]].
   - The final damage your character suffers from a monster equals the monster's strike points minus the result of your defense roll plus your character's damage reduction . _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01298))_
   - Final damage = monster's strike points - (defense roll result + damage reduction) _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01299))_
   - If the result of Ducard II's defense roll is 0 (roll 3) or 6 (roll 12), respectively, the final damage he will suffer is calculated to be: _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01301))_
   - If the defense roll came up double ones , no such calculation would be made, and the goblin's 7 strike points would be the damage. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01303))_
   - If final damage is 0 or negative , that means you took no damage at all. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01304))_

## Decisions And Constraints

- Characters can also reduce damage using their adventurer level . The result of your defense roll plus this damage reduction equals the fi nal amount of damage your character can reduce. However, if the result of your defense roll is double ones , your character's damage reduction is meaningless . No matter how high your character's damage reduction (adventurer level), that damage cannot be reduced at all. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01295, source-range-e5870dca-01296))_

## Authoritative Dependencies

### Formula
- [[sword-world-rpg-complete-edition-section-attacks-from-monsters-against-characters-4-6-1-hit-evasion-checks-20bd7e57]]#atom-technical-atom-da97de2c158d3794 evasion speed + 2D ≥ monster's attack points → evasion success (monster's attack fails) _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01269))_

### Rule
- [[sword-world-rpg-complete-edition-section-attacks-from-monsters-against-characters-4-6-3-defense-rolls-caf97a1f]]#atom-technical-atom-36e2d85a1dff3d90 Characters can reduce the damage they receive from monsters by means of armor. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01283))_
- [[sword-world-rpg-complete-edition-section-attacks-from-monsters-against-characters-4-6-3-defense-rolls-caf97a1f]]#atom-technical-atom-2640ab7439ba915d When making a defense roll, if your roll is double ones, that means that you've been hit extremely hard. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01289))_
- [[sword-world-rpg-complete-edition-section-attacks-from-monsters-against-characters-monsters-8c7835a7]]#atom-technical-atom-9c5043656ae75f0a If a monster's attack hits (or if a character fails to evade), you must look for the base damage dealt by the monster. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01278))_

## Review-Only Dependencies

- `table`: Table 4-3: Rating Table, Key Number _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01284); technical-atom-trust: table-header-suspicious)_
- `rule`: When making a defense roll, criticals do not occur like they do with a strike roll. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01291); source-unit-ownership: source unit ownership is ambiguous for authoritative atom projection: boundary-adjacent-prose)_
- `rule`: You cannot roll the dice again to increase this number further. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01293); source-unit-ownership: source unit ownership is ambiguous for authoritative atom projection: boundary-adjacent-prose)_
- `worked-example`: Suppose Ducard II's defense roll came up 12 (double sixes!). The number on row 12 under key number column 7 is 6 . Unlik _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01293); source-unit-ownership: source unit ownership is ambiguous for authoritative atom projection: boundary-adjacent-prose)_
- `table`: 7 (goblin's strike points) - {0 (defense roll) +2 (damage reduction)} = 5 _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01302); technical-atom-trust: table-parse-incomplete)_

## Execution Readiness

- Projection status: `partial`.
- Authoritative dependencies: 4.
- Review-only dependencies: 5.
- Missing dependencies: 0.
- The procedure is complete when every step output has been recorded or validated.

## Source Trail

- Source manifest: [[sword-world-rpg-complete-edition]]
- Source section: [[sword-world-rpg-complete-edition-section-attacks-from-monsters-against-characters-36abcdc4]]
