---
page_id: sword-world-rpg-complete-edition-procedure-attacks-from-characters-against-monsters
page_kind: procedure
summary: Complete Attacks From Characters Against Monsters: 5 ordered step(s), 0 decision point(s), 11 authoritative dependency reference(s), 3 review-only dependency reference(s), projection partial from raw/Sword World RPG - Complete Edition.pdf.
page_family: procedure-guide
sources: raw/Sword World RPG - Complete Edition.pdf
updated: 2026-07-07
domain: sword-world-rpg-complete-edition
category_path: procedures/sword-world-rpg-complete-edition
source_id: Sword World RPG - Complete Edition.pdf
aliases: complete-attacks-from-characters-against-monsters, attacks-from-characters-against-monsters
projection_coverage: procedure-sword-world-rpg-complete-edition-procedure-attacks-from-characters-against-monsters@a36c4614089277aa1ac381bec36932b5
---

# Attacks From Characters Against Monsters

From [[sword-world-rpg-complete-edition]].

## Goal

- Complete Attacks From Characters Against Monsters.

## Procedure Steps

1. **Hit Checks** (`validate`) - evidence section [[sword-world-rpg-complete-edition-section-attacks-from-characters-against-monsters-4-5-1-hit-checks-40e2447c]].
   - In other words, you roll 2D and add the result to your attack power (fighter/thief/ranger skill level + dexterity bonus) in order to meet or exceed a certain target score. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01207))_
   - In the monsters' data, there is a score called evasion points , which becomes the target score. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01208))_
   - character's attack power + 2D < monster's evasion points → attack fails ※ Double sixes will automatically hit, and double ones will automatically fail. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01210))_
   - Since a hit check is also a type of success roll, double ones is an automatic failure and double sixes is an automatic success . _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01211))_
   - His attack power is 4 (fighter skill level 2, dexterity bonus 2) and the goblin's evasion points are 10. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01213))_
   - Ducard II is fighting a goblin. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01213))_
   - His player rolls the dice to make a hit check. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01214))_
   - 4+8= 12 , which is more than 10. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01214))_
   - Evidence dependencies:
     - `rule`: [[sword-world-rpg-complete-edition-section-attacks-from-characters-against-monsters-4-5-1-hit-checks-40e2447c]]#atom-technical-atom-bdfa8e5b7aaeb6a3 When a character attacks a monster, they must make a success roll hit check, using attack power as the baseline score. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01206))_
     - `formula`: [[sword-world-rpg-complete-edition-section-attacks-from-characters-against-monsters-4-5-1-hit-checks-40e2447c]]#atom-technical-atom-66ad7b9b1ae8ae23 character's attack power + 2D ≥ monster's evasion points → attack hits _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01209))_
     - `table`: [[sword-world-rpg-complete-edition-section-attacks-from-characters-against-monsters-4-5-1-hit-checks-40e2447c]]#atom-technical-atom-a30d8a7949c8d44e 4.5.1 Hit Checks _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01216))_
2. **Determining Base Damage (Strike Roll)** (`generate`) - evidence section [[sword-world-rpg-complete-edition-section-attacks-from-characters-against-monsters-4-5-2-determining-base-damage-strike-roll-08758977]].
   - Damage calculation takes three steps: ① Determine base damage , ② Add bonus damage , and ③ Subtract the monster's defense points . _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01221))_
   - The first step is to determine base damage. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01222))_
   - The numbers are listed in a row, but of course there is no need to memorize them at all. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01223))_
   - For example, if your character's strike power is 14, you only need to look at key number column 14. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01224))_
   - This process is called a strike roll . _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01226))_
   - His weapon is a broadsword (a one-handed weapon) with required strength 14, so his strike power is 14 . _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01228))_
   - The result of his 2D roll is 6, so the number on row 6 under key number column 14 on the Rating Table is 4 . _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01229))_
   - Base damage is 4 points . _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01229))_
   - This means your attack hit the target, but failed to deal any damage! _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01232))_
   - Maybe it hit the hardest part of their armor, or maybe it only hit the hilt of a spear or ax, but no damage was dealt. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01233))_
   - In other words, you have landed a greater strike than would normally be expected. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01236))_
   - Then, roll 2D again and look under the same key number on the Rating Table. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01237))_
   - This is your base damage. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01237))_
   - This process can continue as long as you keep rolling greater than or equal to the critical target. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01238))_
   - In theory, this could deal an infinite amount of damage. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01238))_
   - We'll make a note of the 6 and roll the dice a second time. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01241))_
   - Ducard II's critical target is 10. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01241))_
   - Suppose that Ducard Ⅱ , having hit the goblin with an attack, rolls a 10 when determining base damage. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01241))_
   - The number on row 10 under key number column 14 on the Rating Table is 6 . _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01241))_
   - The number on row 12 is 8 , so we'll make a note of the 8 and roll a third time. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01242))_
   - This did not reach the critical target, so the base damage check ends here. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01242))_
   - If the third roll were a 2 (double ones), the base damage would instead be 6+8+0= 14 . _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01243))_
   - Evidence dependencies:
     - `rule`: [[sword-world-rpg-complete-edition-section-attacks-from-characters-against-monsters-4-5-2-determining-base-damage-strike-roll-08758977]]#atom-technical-atom-439afe3151657b1b If your hit check is a success and you're able to hit your target, the damage dealt to your opponent can be determined n _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01220))_
     - `rule`: [[sword-world-rpg-complete-edition-section-attacks-from-characters-against-monsters-4-5-2-determining-base-damage-strike-roll-08758977]]#atom-technical-atom-3d53ef370e89d424 The player should then roll 2D. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01226))_
     - `rule`: [[sword-world-rpg-complete-edition-section-attacks-from-characters-against-monsters-4-5-2-determining-base-damage-strike-roll-08758977]]#atom-technical-atom-3f1dc6cf2f3cffbb Now that he's hit the goblin, Ducard II must determine how much damage his strike dealt. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01228))_
     - `rule`: [[sword-world-rpg-complete-edition-section-attacks-from-characters-against-monsters-4-5-2-determining-base-damage-strike-roll-08758977]]#atom-technical-atom-95a675743f21f183 When making a strike roll, if your 2D roll is equal to or greater than the critical target (usually 10 , 9 if using the _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01236))_
     - `rule`: [[sword-world-rpg-complete-edition-section-attacks-from-characters-against-monsters-4-5-2-determining-base-damage-strike-roll-08758977]]#atom-technical-atom-8d1ff6fc8ecf8dc6 If the second 2D roll is also greater than or equal to the critical target, you can make a third roll to add even more d _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01238))_
     - `rule`: [[sword-world-rpg-complete-edition-section-attacks-from-characters-against-monsters-4-5-2-determining-base-damage-strike-roll-08758977]]#atom-technical-atom-3d5c986568247838 If a critical occurs, but you roll double ones on the second and subsequent damage checks, 0 is added to the previous re _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01239))_
3. **Bonus Damage** (`step`) - evidence section [[sword-world-rpg-complete-edition-section-attacks-from-characters-against-monsters-4-5-3-bonus-damage-66d7239b]].
   - This will be the total amount of damage the character deals the monster. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01245))_
   - Ducard II's bonus damage is 4 (fighter skill level 2, strength bonus 2). _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01247))_
   - If base damage is 14, the total damage is 14+4= 18 . _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01250))_
   - No matter how much bonus damage you have, it means nothing. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01251))_
   - Evidence dependencies:
     - `rule`: [[sword-world-rpg-complete-edition-section-attacks-from-characters-against-monsters-4-5-3-bonus-damage-66d7239b]]#atom-technical-atom-9c0b1cb995ef27e2 Once you've determined base damage, you must then add your character's bonus damage. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01245))_
4. **Monster Defense Points** (`record`) - evidence section [[sword-world-rpg-complete-edition-section-attacks-from-characters-against-monsters-4-5-4-monster-defense-points-c48dcc4c]].
   - Monsters can repel and hold off attacks with their thick skins and hard scales. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01254))_
   - This indicates the amount of damage a monster can reduce. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01254))_
   - Please note that a monster's defense points are treated differently from a character's defense power . _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01254))_
   - A goblin has 4 defense points. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01256))_
   - The goblin can prevent 4 points of damage with its skin. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01256))_
5. **Final Damage** (`step`) - evidence section [[sword-world-rpg-complete-edition-section-attacks-from-characters-against-monsters-4-5-5-final-damage-3ad5f07b]].
   - Evidence dependencies:
     - `formula`: [[sword-world-rpg-complete-edition-section-attacks-from-characters-against-monsters-4-5-5-final-damage-3ad5f07b]]#atom-technical-atom-7d932c992bb48dbe final damage = base damage + bonus damage - monster's defense points _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01259))_

## Authoritative Dependencies

### Table
- [[sword-world-rpg-complete-edition-section-attacks-from-characters-against-monsters-4-5-1-hit-checks-40e2447c]]#atom-technical-atom-a30d8a7949c8d44e 4.5.1 Hit Checks _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01216))_

### Formula
- [[sword-world-rpg-complete-edition-section-attacks-from-characters-against-monsters-4-5-1-hit-checks-40e2447c]]#atom-technical-atom-66ad7b9b1ae8ae23 character's attack power + 2D ≥ monster's evasion points → attack hits _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01209))_
- [[sword-world-rpg-complete-edition-section-attacks-from-characters-against-monsters-4-5-5-final-damage-3ad5f07b]]#atom-technical-atom-7d932c992bb48dbe final damage = base damage + bonus damage - monster's defense points _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01259))_

### Rule
- [[sword-world-rpg-complete-edition-section-attacks-from-characters-against-monsters-4-5-1-hit-checks-40e2447c]]#atom-technical-atom-bdfa8e5b7aaeb6a3 When a character attacks a monster, they must make a success roll hit check, using attack power as the baseline score. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01206))_
- [[sword-world-rpg-complete-edition-section-attacks-from-characters-against-monsters-4-5-2-determining-base-damage-strike-roll-08758977]]#atom-technical-atom-3d53ef370e89d424 The player should then roll 2D. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01226))_
- [[sword-world-rpg-complete-edition-section-attacks-from-characters-against-monsters-4-5-2-determining-base-damage-strike-roll-08758977]]#atom-technical-atom-3f1dc6cf2f3cffbb Now that he's hit the goblin, Ducard II must determine how much damage his strike dealt. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01228))_
- [[sword-world-rpg-complete-edition-section-attacks-from-characters-against-monsters-4-5-2-determining-base-damage-strike-roll-08758977]]#atom-technical-atom-95a675743f21f183 When making a strike roll, if your 2D roll is equal to or greater than the critical target (usually 10 , 9 if using the _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01236))_
- [[sword-world-rpg-complete-edition-section-attacks-from-characters-against-monsters-4-5-2-determining-base-damage-strike-roll-08758977]]#atom-technical-atom-8d1ff6fc8ecf8dc6 If the second 2D roll is also greater than or equal to the critical target, you can make a third roll to add even more d _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01238))_
- [[sword-world-rpg-complete-edition-section-attacks-from-characters-against-monsters-4-5-2-determining-base-damage-strike-roll-08758977]]#atom-technical-atom-3d5c986568247838 If a critical occurs, but you roll double ones on the second and subsequent damage checks, 0 is added to the previous re _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01239))_
- [[sword-world-rpg-complete-edition-section-attacks-from-characters-against-monsters-4-5-2-determining-base-damage-strike-roll-08758977]]#atom-technical-atom-439afe3151657b1b If your hit check is a success and you're able to hit your target, the damage dealt to your opponent can be determined n _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01220))_
- [[sword-world-rpg-complete-edition-section-attacks-from-characters-against-monsters-4-5-3-bonus-damage-66d7239b]]#atom-technical-atom-9c0b1cb995ef27e2 Once you've determined base damage, you must then add your character's bonus damage. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01245))_

## Review-Only Dependencies

- `table`: Table 4-2: Rating Table, Key Number _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01217); technical-atom-trust: table-parse-incomplete, table-raw-text-contaminated-by-prose)_
- `rule`: When determining base damage (strike roll), if you suddenly roll double ones, the damage will always be 0 . _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01251); source-unit-ownership: source unit ownership is ambiguous for authoritative atom projection: boundary-adjacent-prose)_
- `table`: 4 (base damage) +4 (bonus damage) -4 (goblin's defense points) = 4 _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01262); technical-atom-trust: table-parse-incomplete)_

## Execution Readiness

- Projection status: `partial`.
- Authoritative dependencies: 11.
- Review-only dependencies: 3.
- Missing dependencies: 0.
- The procedure is complete when every step output has been recorded or validated.

## Source Trail

- Source manifest: [[sword-world-rpg-complete-edition]]
- Source section: [[sword-world-rpg-complete-edition-section-attacks-from-characters-against-monsters-2a2d8681]]
