---
page_id: sword-world-rpg-complete-edition-hit-check
page_kind: concept
summary: 4.5.1 Hit Checks: 16 statement(s) and 7 atom(s) from raw/Sword World RPG - Complete Edition.pdf.
page_family: topic-concept
sources: raw/Sword World RPG - Complete Edition.pdf
updated: 2026-07-07
domain: sword-world-rpg-complete-edition
category_path: concepts
projection_coverage: topic-sword-world-rpg-complete-edition-hit-check@7898b2331ffb44a05fc4fe9f93c5c76d
---

# 4.5.1 Hit Checks

What [[sword-world-rpg-complete-edition]] covers about 4.5.1 hit checks:

## Statements

### Chapter 3: / 3.4.4 Actions You Can Take While Standing Still / Attacks From Characters Against Monsters / 4.5.1 Hit Checks

- In other words, you roll 2D and add the result to your attack power (fighter/thief/ranger skill level + dexterity bonus) in order to meet or exceed a certain target score. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01207))_

- The target score at this time varies depending on the monster. In the monsters' data, there is a score called evasion points , which becomes the target score. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01208))_

- character's attack power + 2D < monster's evasion points → attack fails ※ Double sixes will automatically hit, and double ones will automatically fail. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01210))_

- Since a hit check is also a type of success roll, double ones is an automatic failure and double sixes is an automatic success . _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01211))_

- Ducard II is fighting a goblin. His attack power is 4 (fighter skill level 2, dexterity bonus 2) and the goblin's evasion points are 10. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01213))_

- His player rolls the dice to make a hit check. The roll is 8. 4+8= 12 , which is more than 10. The attack hit the target perfectly. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01214))_

### 4.7 Attacks From Characters Against Characters / 4.7.1 Hit Checks

- To make a hit check, both sides must roll the dice (2D). The attacker adds their roll to their attack power , and the defender adds their roll to their evasion speed . _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01311))_

- If the attacker's final score exceeds that of the defender, the attack hits . If there is a tie or the defender's is greater, the attack fails . _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01314))_

- Ducard II suddenly found himself in a dispute with another adventurer, Bucky. Ducard II has higher agility, so he attacks first. Ducard II 's attack power is 4 , while Bucky's evasion speed is 5 . _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01319))_

- Ducard II rolls a 7 , and Bucky rolls a 6 . _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01320))_

- Ducard II's final score is 4+7= 11 , while Bucky's final score is 5+6= 11 . It's a tie. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01321))_

- In combat between characters, a tie is considered an attack failure. Ducard II 's attack was narrowly dodged. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01322))_


## Technical atoms

### Technical frame 1: Chapter 3: / 3.4.4 Actions You Can Take While Standing Still / Attacks From Characters Against Monsters / 4.5.1 Hit Checks

**Context:** _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01207))_

> In other words, you roll 2D and add the result to your attack power (fighter/thief/ranger skill level + dexterity bonus) in order to meet or exceed a certain target score.

**Atom:** _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01206))_

<a id="atom-technical-atom-bdfa8e5b7aaeb6a3"></a>
> When a character attacks a monster, they must make a success roll hit check, using attack power as the baseline score.

### Technical frame 2: Chapter 3: / 3.4.4 Actions You Can Take While Standing Still / Attacks From Characters Against Monsters / 4.5.1 Hit Checks

**Context:** _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01210))_

> character's attack power + 2D < monster's evasion points → attack fails ※ Double sixes will automatically hit, and double ones will automatically fail.

**Atom:** _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01209))_

<a id="atom-technical-atom-66ad7b9b1ae8ae23"></a>
> character's attack power + 2D ≥ monster's evasion points → attack hits

### Technical frame 3: Chapter 3: / 3.4.4 Actions You Can Take While Standing Still / Attacks From Characters Against Monsters / 4.5.1 Hit Checks

**Context:** _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01214))_

> His player rolls the dice to make a hit check. The roll is 8. 4+8= 12 , which is more than 10. The attack hit the target perfectly.

**Atom:** _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01216))_

<a id="atom-technical-atom-a30d8a7949c8d44e"></a>
```text
4.5.1 Hit Checks
Key Number
0 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 2D ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **
3 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1
4 0 0 0 0 0 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2
5 0 0 0 1 1 1 1 1 2 2 2 2 2 3 3 3 3 3 3 3
6 1 1 1 1 2 2 2 2 2 3 3 3 3 3 4 4 4 4 4 4
7 2 2 2 2 2 2 3 3 3 3 3 3 4 4 4 4 4 5 5 5
8 2 3 3 3 3 3 3 4 4 4 4 4 4 4 4 5 5 5 6 6
9 3 3 4 4 4 4 4 4 4 4 5 5 5 5 5 5 6 6 6 7
10 3 3 4 4 4 5 5 5 5 5 5 6 6 6 6 6 7 7 7 7
11 4 4 4 4 5 5 5 5 6 6 6 6 6 7 7 7 7 7 7 8
12 4 4 4 5 5 5 5 6 6 7 7 7 7 7 8 8 8 8 8 9 Key Number
20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 2D ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **
3 1 1 1 2 2 2 2 2 2 2 2 2 3 3 3 3 3 3 3 4
4 2 2 2 2 3 3 3 3 3 3 4 4 4 4 4 4 5 5 5 5
5 3 3 3 3 4 4 4 4 4 4 4 5 5 5 5 5 5 6 6 6
6 4 4 5 5 5 5 5 6 6 6 6 6 6 6 6 7 7 7 7 7
7 5 6 6 6 6 6 6 6 6 7 7 7 7 8 8 8 8 8 8 8
8 6 6 6 7 7 7 8 8 8 8 8 8 8 8 9 9 9 9 10 10
9 7 7 7 7 7 8 8 8 9 9 9 9 10 10 10 10 10 10 10 11
10 8 8 8 8 8 8 9 9 9 9 10 10 10 10 10 10 11 11 11 11
11 9 9 9 9 9 9 9 9 10 10 10 10 10 10 11 11 11 12 12 12
12 10 10 10 10 10 10 10 10 10 10 10 10 10 11 12 12 12 13 13
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 4 | 5.1 Hit Checks |
| 0 | Key Number 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 2D ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** |
| 3 | 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 |
| 4 | 0 0 0 0 0 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 |
| 5 | 0 0 0 1 1 1 1 1 2 2 2 2 2 3 3 3 3 3 3 3 |
| 6 | 1 1 1 1 2 2 2 2 2 3 3 3 3 3 4 4 4 4 4 4 |
| 7 | 2 2 2 2 2 2 3 3 3 3 3 3 4 4 4 4 4 5 5 5 |
| 8 | 2 3 3 3 3 3 3 4 4 4 4 4 4 4 4 5 5 5 6 6 |
| 9 | 3 3 4 4 4 4 4 4 4 4 5 5 5 5 5 5 6 6 6 7 |
| 10 | 3 3 4 4 4 5 5 5 5 5 5 6 6 6 6 6 7 7 7 7 |
| 11 | 4 4 4 4 5 5 5 5 6 6 6 6 6 7 7 7 7 7 7 8 |
| 12 | 4 4 4 5 5 5 5 6 6 7 7 7 7 7 8 8 8 8 8 9 Key Number |
| 20 | 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 2D ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** |
| 3 | 1 1 1 2 2 2 2 2 2 2 2 2 3 3 3 3 3 3 3 4 |
| 4 | 2 2 2 2 3 3 3 3 3 3 4 4 4 4 4 4 5 5 5 5 |
| 5 | 3 3 3 3 4 4 4 4 4 4 4 5 5 5 5 5 5 6 6 6 |
| 6 | 4 4 5 5 5 5 5 6 6 6 6 6 6 6 6 7 7 7 7 7 |
| 7 | 5 6 6 6 6 6 6 6 6 7 7 7 7 8 8 8 8 8 8 8 |
| 8 | 6 6 6 7 7 7 8 8 8 8 8 8 8 8 9 9 9 9 10 10 |
| 9 | 7 7 7 7 7 8 8 8 9 9 9 9 10 10 10 10 10 10 10 11 |
| 10 | 8 8 8 8 8 8 9 9 9 9 10 10 10 10 10 10 11 11 11 11 |
| 11 | 9 9 9 9 9 9 9 9 10 10 10 10 10 10 11 11 11 12 12 12 |
| 12 | 10 10 10 10 10 10 10 10 10 10 10 10 10 11 12 12 12 13 13 |

</details>

### Technical frame 4: 4.7 Attacks From Characters Against Characters / 4.7.1 Hit Checks

**Context:** _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01314))_

> If the attacker's final score exceeds that of the defender, the attack hits . If there is a tie or the defender's is greater, the attack fails .

**Atom:** _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01311))_

<a id="atom-technical-atom-5e5c1a85579c1d58"></a>
> To make a hit check, both sides must roll the dice (2D).

### Technical frame 5: 4.7 Attacks From Characters Against Characters / 4.7.1 Hit Checks

**Context:** _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01314))_

> If the attacker's final score exceeds that of the defender, the attack hits . If there is a tie or the defender's is greater, the attack fails .

**Atoms:** _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01312, source-range-e5870dca-01313))_

<a id="atom-technical-atom-af83bcae79e26c97"></a>
> attacker's final score = attack power + 2D

<a id="atom-technical-atom-f0e9338f7fe6f6c2"></a>
> defender's final score = evasion speed + 2D

### Technical frame 6: 4.7 Attacks From Characters Against Characters / 4.7.1 Hit Checks

**Context:** _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01319))_

> Ducard II suddenly found himself in a dispute with another adventurer, Bucky. Ducard II has higher agility, so he attacks first. Ducard II 's attack power is 4 , while Bucky's evasion speed is 5 .

**Atom:** _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01317))_

<a id="atom-technical-atom-119f8c9d93437d07"></a>
> attacker's attack power + 2D ≤ defender's evasion speed +2D → attack fails


## Related pages

### Source structure

- [[sword-world-rpg-complete-edition-section-4-7-attacks-from-characters-against-characters-4-7-1-hit-checks-9c205d1f]] - source section: 4.7 Attacks From Characters Against Characters / 4.7.1 Hit Checks shares source evidence from 4.7 Attacks From Characters Against Characters / 4.7.1 Hit Checks: To make a hit check, both sides must roll the dice (2D). The attacker adds their roll to their attack power , and the defender adds their roll to their evasion speed .; 4.7 Attacks From Characters Against Characters / 4.7.1 Hit Checks shares technical record from 4.7 Attacks From Characters Against Characters / 4.7.1 Hit Checks: To make a hit check, both sides must roll the dice (2D). (8 shared statement(s), 4 shared atom(s))
- [[sword-world-rpg-complete-edition-section-chapter-3-3-4-4-actions-you-can-take-while-standing-still-attacks-from-characters-against-monste-40e2447c]] - source section: Chapter 3: / 3.4.4 Actions You Can Take While Standing Still / Attacks From Characters Against Monsters / 4.5.1 Hit Checks shares source evidence from Chapter 3: / 3.4.4 Actions You Can Take While Standing Still / Attacks From Characters Against Monsters / 4.5.1 Hit Checks: In other words, you roll 2D and add the result to your attack power (fighter/thief/ranger skill level + dexterity bonus) in order to meet or exceed a certain target score.; Chapter 3: / 3.4.4 Actions You Can Take While Standing Still / Attacks From Characters Against Monsters / 4.5.1 Hit Checks shares technical record from Chapter 3: / 3.4.4 Actions You Can Take While Standing Still / Attacks From Characters Against Monsters / 4.5.1 Hit Checks: When a character attacks a monster, they must make a success roll hit check, using attack power as the baseline score. (8 shared statement(s), 3 shared atom(s))

### Shared technical atoms

- [[sword-world-rpg-complete-edition-attack-character-monster]] - shared statements and technical atoms: Attacks From Characters Against Monsters shares source evidence from Chapter 3: / 3.4.4 Actions You Can Take While Standing Still / Attacks From Characters Against Monsters / 4.5.1 Hit Checks: In other words, you roll 2D and add the result to your attack power (fighter/thief/ranger skill level + dexterity bonus) in order to meet or exceed a certain target score.; Attacks From Characters Against Monsters shares technical record from Chapter 3: / 3.4.4 Actions You Can Take While Standing Still / Attacks From Characters Against Monsters / 4.5.1 Hit Checks: When a character attacks a monster, they must make a success roll hit check, using attack power as the baseline score. (8 shared statement(s), 3 shared atom(s))

## Source

- [[sword-world-rpg-complete-edition]]
