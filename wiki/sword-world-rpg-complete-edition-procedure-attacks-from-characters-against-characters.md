---
page_id: sword-world-rpg-complete-edition-procedure-attacks-from-characters-against-characters
page_kind: procedure
summary: Complete Attacks From Characters Against Characters: 2 ordered step(s), 3 decision point(s), 10 authoritative dependency reference(s), 1 review-only dependency reference(s), projection partial from raw/Sword World RPG - Complete Edition.pdf.
page_family: procedure-guide
sources: raw/Sword World RPG - Complete Edition.pdf
updated: 2026-07-07
domain: sword-world-rpg-complete-edition
category_path: procedures/sword-world-rpg-complete-edition
source_id: Sword World RPG - Complete Edition.pdf
aliases: complete-attacks-from-characters-against-characters, attacks-from-characters-against-characters
projection_coverage: procedure-sword-world-rpg-complete-edition-procedure-attacks-from-characters-against-characters@3db26b169efc0fdf67d986d530f9ca74
---

# Attacks From Characters Against Characters

From [[sword-world-rpg-complete-edition]].

## Goal

- Complete Attacks From Characters Against Characters.

## Procedure Steps

1. **Hit Checks** (`validate`) - evidence section [[sword-world-rpg-complete-edition-section-4-7-attacks-from-characters-against-characters-4-7-1-hit-checks-9c205d1f]].
   - The attacker adds their roll to their attack power , and the defender adds their roll to their evasion speed . _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01311))_
   - If there is a tie or the defender's is greater, the attack fails . _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01314))_
   - Ducard II 's attack power is 4 , while Bucky's evasion speed is 5 . _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01319))_
   - Ducard II has higher agility, so he attacks first. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01319))_
   - Ducard II rolls a 7 , and Bucky rolls a 6 . _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01320))_
   - Ducard II's final score is 4+7= 11 , while Bucky's final score is 5+6= 11 . _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01321))_
   - In combat between characters, a tie is considered an attack failure. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01322))_
   - Ducard II 's attack was narrowly dodged. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01322))_
   - Evidence dependencies:
     - `rule`: [[sword-world-rpg-complete-edition-section-4-7-attacks-from-characters-against-characters-4-7-1-hit-checks-9c205d1f]]#atom-technical-atom-5e5c1a85579c1d58 To make a hit check, both sides must roll the dice (2D). _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01311))_
     - `formula`: [[sword-world-rpg-complete-edition-section-4-7-attacks-from-characters-against-characters-4-7-1-hit-checks-9c205d1f]]#atom-technical-atom-af83bcae79e26c97 attacker's final score = attack power + 2D _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01312))_
     - `formula`: [[sword-world-rpg-complete-edition-section-4-7-attacks-from-characters-against-characters-4-7-1-hit-checks-9c205d1f]]#atom-technical-atom-f0e9338f7fe6f6c2 defender's final score = evasion speed + 2D _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01313))_
     - `formula`: [[sword-world-rpg-complete-edition-section-4-7-attacks-from-characters-against-characters-4-7-1-hit-checks-9c205d1f]]#atom-technical-atom-119f8c9d93437d07 attacker's attack power + 2D ≤ defender's evasion speed +2D → attack fails _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01317))_
2. **Damage Checks** (`validate`) - evidence section [[sword-world-rpg-complete-edition-section-4-7-attacks-from-characters-against-characters-4-7-2-damage-checks-dcc87885]].
   - This procedure is exactly the same for characters as it was during combat with monsters. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01331))_
   - The difference is the damage dealt to the defender. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01334))_
   - Bucky dodges Ducard II's attack, then counterattacks. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01336))_
   - Bucky is wielding a battle-ax (required strength 15) with both hands, so he has a strike power of 20 . _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01337))_
   - The result of his strike roll is 11 (base damage 9 ). _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01337))_
   - His following 2D roll is 9 (base damage 7 ). _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01337))_
   - His bonus damage is 5 (fighter skill level 3, strength bonus +2), which brings the total amount of damage to 9+7+5= 21 . _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01337))_
   - Bucky then determines the damage he deals. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01337))_
   - After adding his damage reduction of 2 , 3+2= 5 points is the final amount of damage Ducard II is able to reduce. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01338))_
   - As a result, the damage that Ducard II suffers is 21-5= 16 points . _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01339))_
   - Evidence dependencies:
     - `rule`: [[sword-world-rpg-complete-edition-section-4-7-attacks-from-characters-against-characters-4-7-2-damage-checks-dcc87885]]#atom-technical-atom-d2c98b7665321901 If your attack hits, you must then determine damage. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01331))_
     - `rule`: [[sword-world-rpg-complete-edition-section-4-7-attacks-from-characters-against-characters-4-7-2-damage-checks-dcc87885]]#atom-technical-atom-a9ee5b97c7b7c5e1 The attacker must make a strike roll to determine their base damage, then add their bonus damage. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01332))_
     - `rule`: [[sword-world-rpg-complete-edition-section-4-7-attacks-from-characters-against-characters-4-7-2-damage-checks-dcc87885]]#atom-technical-atom-620f5efd3d18d599 The defender must make a defense roll, then add their damage reduction to the result to determine how much damage they r _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01333))_

## Decisions And Constraints

- If a roll comes up double sixes or double ones during combat between characters, the situation is resolved as follows: _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01324))_
- If the attacker's roll is double sixes , it' s basically an automatic hit. However, if the defender's roll is also double sixes, the attack fails . If the defender's roll is double ones , it' s basically an automatic hit. However, if the attacker's roll is also double ones, the attack fails . _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01326, source-range-e5870dca-01327))_
- If the attacker's roll is double sixes , it' s basically an automatic hit. However, if the defender's roll is also double sixes, the attack fails . If the defender's roll is double ones , it' s basically an automatic hit. However, if the attacker's roll is also double ones, the attack fails . _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01326, source-range-e5870dca-01327))_

## Authoritative Dependencies

### Formula
- [[sword-world-rpg-complete-edition-section-4-7-attacks-from-characters-against-characters-4-7-1-hit-checks-9c205d1f]]#atom-technical-atom-af83bcae79e26c97 attacker's final score = attack power + 2D _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01312))_
- [[sword-world-rpg-complete-edition-section-4-7-attacks-from-characters-against-characters-4-7-1-hit-checks-9c205d1f]]#atom-technical-atom-f0e9338f7fe6f6c2 defender's final score = evasion speed + 2D _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01313))_
- [[sword-world-rpg-complete-edition-section-4-7-attacks-from-characters-against-characters-4-7-1-hit-checks-9c205d1f]]#atom-technical-atom-119f8c9d93437d07 attacker's attack power + 2D ≤ defender's evasion speed +2D → attack fails _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01317))_

### Rule
- [[sword-world-rpg-complete-edition-section-4-7-attacks-from-characters-against-characters-112572a5]]#atom-technical-atom-b38a3c8031abeb09 Sometimes, especially when the mastermind behind an incident is a dark priest, you'll have to fight against someone whos _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01308))_
- [[sword-world-rpg-complete-edition-section-4-7-attacks-from-characters-against-characters-112572a5]]#atom-technical-atom-a71fb6908aeedeb1 The defender doesn't even have to roll the dice. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01325))_
- [[sword-world-rpg-complete-edition-section-4-7-attacks-from-characters-against-characters-112572a5]]#atom-technical-atom-69d6505c34ac6971 If the defender's roll is double sixes , the attack will always fail. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01328))_
- [[sword-world-rpg-complete-edition-section-4-7-attacks-from-characters-against-characters-4-7-2-damage-checks-dcc87885]]#atom-technical-atom-a9ee5b97c7b7c5e1 The attacker must make a strike roll to determine their base damage, then add their bonus damage. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01332))_
- [[sword-world-rpg-complete-edition-section-4-7-attacks-from-characters-against-characters-4-7-1-hit-checks-9c205d1f]]#atom-technical-atom-5e5c1a85579c1d58 To make a hit check, both sides must roll the dice (2D). _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01311))_
- [[sword-world-rpg-complete-edition-section-4-7-attacks-from-characters-against-characters-4-7-2-damage-checks-dcc87885]]#atom-technical-atom-d2c98b7665321901 If your attack hits, you must then determine damage. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01331))_
- [[sword-world-rpg-complete-edition-section-4-7-attacks-from-characters-against-characters-4-7-2-damage-checks-dcc87885]]#atom-technical-atom-620f5efd3d18d599 The defender must make a defense roll, then add their damage reduction to the result to determine how much damage they r _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01333))_

## Review-Only Dependencies

- `table`: Table 4-4: Attack Checks _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01340); technical-atom-trust: table-parse-incomplete, table-raw-text-contaminated-by-prose)_

## Execution Readiness

- Projection status: `partial`.
- Authoritative dependencies: 10.
- Review-only dependencies: 1.
- Missing dependencies: 0.
- The procedure is complete when every step output has been recorded or validated.

## Source Trail

- Source manifest: [[sword-world-rpg-complete-edition]]
- Source section: [[sword-world-rpg-complete-edition-section-4-7-attacks-from-characters-against-characters-112572a5]]
