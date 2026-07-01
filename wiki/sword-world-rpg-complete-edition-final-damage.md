---
page_id: sword-world-rpg-complete-edition-final-damage
page_kind: concept
summary: 4.5.5 Final Damage: 11 statement(s) and 4 atom(s) from raw/Sword World RPG - Complete Edition.pdf.
page_family: broad-topic
sources: raw/Sword World RPG - Complete Edition.pdf
updated: 2026-07-01
domain: sword-world-rpg-complete-edition
category_path: concepts
projection_coverage: topic-sword-world-rpg-complete-edition-final-damage@3d3cfd3c530a7960fc2e4e19fb34bd20
---

# 4.5.5 Final Damage

What [[sword-world-rpg-complete-edition]] covers about 4.5.5 final damage:

## Statements

### Attacks From Monsters Against Characters / 4.6.5 Final Damage

- The final damage your character suffers from a monster equals the monster's strike points minus the result of your defense roll plus your character's damage reduction . _(Sword World RPG - Complete Edition.pdf (source-range-0d48087c-01347))_

- If the result of Ducard II's defense roll is 0 (roll 3) or 6 (roll 12), respectively, the final damage he will suffer is calculated to be: _(Sword World RPG - Complete Edition.pdf (source-range-0d48087c-01350))_

- If the defense roll came up double ones , no such calculation would be made, and the goblin's 7 strike points would be the damage. _(Sword World RPG - Complete Edition.pdf (source-range-0d48087c-01352))_

### 4.7 Attacks From Characters Against Characters / 4.7.2 Damage Checks

- Ducard II now determines how much damage his armor prevents. His defense roll result is 7 , and his armor's defense power is 7, so the damage that'll be reduced by his armor is 3 . After adding his damage reduction of 2 , 3+2= 5 points is the final amount of damage Ducard II is able to reduce. _(Sword World RPG - Complete Edition.pdf (source-range-0d48087c-01387))_

### 《 Effect Expansion 》

- Suppose a sorcerer casts an Energy Bolt on three enemies ( x 3 expansion) with a +1 to his final score ( x 2 expansion) and he makes 4 damage checks for each ( x 4 expansion). In this case, the multiplied rate of mental power consumed is 3 x 2 x 4 = 24! _(Sword World RPG - Complete Edition.pdf (source-range-0d48087c-01725))_

### 5.1.12 Ancient Magic List / [ Lightning ]

- Base Mental Power Cost=15 Distance=Caster Area=A space 1 meter high and wide and 20 meters long Duration=Instant Effect=Emits strike power 20 lightning Type=Damage (Electric-type) Expansion=Final score, area length (see description), damage certainty Resist=Reduced effect _(Sword World RPG - Complete Edition.pdf (source-range-0d48087c-02189))_

### 5.1.12 Ancient Magic List / Blizzard ]

- Expansion=Final score, distance, area, damage certainty Resist=Reduced effect This spell creates a sudden storm containing countless pieces of ice the size of pebbles, in a space within a 5 meter radius centered on a point, dealing cold damage to everything within range. Its strike power is 20. _(Sword World RPG - Complete Edition.pdf (source-range-0d48087c-02365))_

### 5.1.14 Spirit Magic List / 2nd Level Spirit Magic List [ Will-O-Wisp ] (Will-O-Wisp/Light Spirit) / [ Shade ] (Shade/Dark Spirit)

- Expansion=Final score, duration, distance, targets, damage certainty Resist=Reduced effect Shade is the spirit of darkness that opposes will-o-wisp, and is also the spirit that controls fear. It is said to have a spherical shape like the will-o-wisp, but this is not certain (because like a crow in the pitch-black night, it cannot be seen). All natural light within a 5 meter radius of this spirit is negated, closing it in complete darkness. The darkness created by a shade has no effect in a space where the ancient magic Light is at work. In addition, if the light emitted by a will-owisp and the darkness produced by a shade overlap, the powers of both will be negated. The shade will fly freely in the air according to the caster's commands, but can no longer be controlled if it moves more than 20 meters away from the caster. The shade is also very fragile and will easily disintegrate with the slightest force. At this time, it emits an energy completely different from a willo-wisp. This has no physical effect, but it impairs mental activity and has the effect of reducing mental power (points). Make a strike power 10 damage check, and subtract the result from mental power (points). The damage is only dealt to mental power (points), the rest of the check is the same as for magic that deals normal damage. If mental power (points) becomes 0 or negative, the target loses consciousness. Furthermore, if an opponent destroys a shade with a weapon they're holding, the one who took that action will also suffer the same damage. _(Sword World RPG - Complete Edition.pdf (source-range-0d48087c-02893))_

### 5.1.14 Spirit Magic List / 8th Level Spirit Magic List [ Ice Coffin ] / [ Ice Storm ] (Fenrir/Greater Ice Spirit)

- Base Mental Power Cost=40 Distance=30 meters Area=A space with a 10 meter radius Duration=Instant Effect=Creates an ice storm, dealing strike power 30 damage to targets within range Type=Damage (Cold-type) Expansion=Final score, distance, area, damage certainty Resist=Reduced effect _(Sword World RPG - Complete Edition.pdf (source-range-0d48087c-03274))_

### Chapter 11: Notes on Magic / 11.2 Dark Magic / 3rd Level Basic Dark Magic List [ Poison ]

- Deals damage to the opponent's life force (points). First, make a strike roll with a strike power of 20. Magic power should be added to damage as usual. Also, your opponent cannot reduce this damage using adventurer level. This poison's damage is not applied immediately, but in the form of 1 point at the end of each round, starting on the round in which the spell is used. The poison then lasts until the final determined damage is dealt. In this case, if the poison is removed by a spell such as Cure Poison , etc. midway, the damage will stop accumulating at that point. However, the damage suffered up to that point will not be recovered. _(Sword World RPG - Complete Edition.pdf (source-range-0d48087c-04847))_

- If final damage is 0 or negative , that means you took no damage at all. _(Sword World RPG - Complete Edition.pdf (source-range-0d48087c-01353))_

## Technical atoms

### Technical frame 1: 4.5.5 Final Damage

**Atom:** _(Sword World RPG - Complete Edition.pdf (source-range-0d48087c-01306))_

> final damage = base damage + bonus damage - monster's defense points

### Technical frame 2: 4.5.5 Final Damage

**Atom:** _(Sword World RPG - Complete Edition.pdf (source-range-0d48087c-01309))_

```text
4 (base damage) +4 (bonus damage) -4 (goblin's defense points) = 4
18 (base damage) +4 (bonus damage)
-4 (goblin's defense points) = 18
14 (base damage) +4 (bonus damage) -4 (goblin's defense points) = 14
If  final  damage  is 0  or  negative ,  it means  that no  damage was  dealt.  The attack  was  prevented  by  thick  skin  or hard scales.
4.6
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 4 | (base damage) +4 (bonus damage) -4 (goblin's defense points) = 4 |
| 18 | (base damage) +4 (bonus damage) |
| 4 | (goblin's defense points) = 18 |
| 14 | (base damage) +4 (bonus damage) -4 (goblin's defense points) = 14 If final damage is 0 or negative, it means that no damage was dealt. The attack was prevented by thick skin or hard scales. |
| 4 | 6 |

</details>

### Technical frame 3: Attacks From Monsters Against Characters / 4.6.5 Final Damage

**Context:** _(Sword World RPG - Complete Edition.pdf (source-range-0d48087c-01350))_

> If the result of Ducard II's defense roll is 0 (roll 3) or 6 (roll 12), respectively, the final damage he will suffer is calculated to be:

**Atom:** _(Sword World RPG - Complete Edition.pdf (source-range-0d48087c-01348))_

> Final damage = monster's strike points - (defense roll result + damage reduction)

### Technical frame 4: Attacks From Monsters Against Characters / 4.6.5 Final Damage

**Context:** _(Sword World RPG - Complete Edition.pdf (source-range-0d48087c-01352))_

> If the defense roll came up double ones , no such calculation would be made, and the goblin's 7 strike points would be the damage.

**Atom:** _(Sword World RPG - Complete Edition.pdf (source-range-0d48087c-01351))_

```text
7 (goblin's strike points) - {0 (defense roll) +2 (damage reduction)} = 5
7 (goblin's strike points) - {6 (defense roll) +2 (damage reduction)} = -1
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 7 | (goblin's strike points) - {0 (defense roll) +2 (damage reduction)} = 5 |
| 7 | (goblin's strike points) - {6 (defense roll) +2 (damage reduction)} = -1 |

</details>


## Related pages

- [[sword-world-rpg-complete-edition-attack-monster-character]] - shared statements and technical atoms: Attacks From Monsters Against Characters shares source evidence from Attacks From Monsters Against Characters / 4.6.5 Final Damage: The final damage your character suffers from a monster equals the monster's strike points minus the result of your defense roll plus your character's damage reduction .; Attacks From Monsters Against Characters shares technical record from Attacks From Monsters Against Characters / 4.6.5 Final Damage: Final damage = monster's strike points - (defense roll result + damage reduction) (4 shared statement(s), 2 shared atom(s))
- [[sword-world-rpg-complete-edition-attack-character-monster]] - shared statements and technical atoms: Attacks From Characters Against Monsters shares source evidence from Attacks From Monsters Against Characters / 4.6.5 Final Damage: The final damage your character suffers from a monster equals the monster's strike points minus the result of your defense roll plus your character's damage reduction .; Attacks From Characters Against Monsters shares technical record from Attacks From Monsters Against Characters / 4.6.5 Final Damage: Final damage = monster's strike points - (defense roll result + damage reduction) (1 shared statement(s), 2 shared atom(s))
- [[sword-world-rpg-complete-edition-damage-reduction]] - shared statements and technical atoms: 【 Damage Reduction 】 shares source evidence from Attacks From Monsters Against Characters / 4.6.5 Final Damage: The final damage your character suffers from a monster equals the monster's strike points minus the result of your defense roll plus your character's damage reduction .; 【 Damage Reduction 】 shares technical record from Attacks From Monsters Against Characters / 4.6.5 Final Damage: Final damage = monster's strike points - (defense roll result + damage reduction) (2 shared statement(s), 1 shared atom(s))
- [[sword-world-rpg-complete-edition-target-score]] - shared statements: Target Scores shares source evidence from 5.1.14 Spirit Magic List / 2nd Level Spirit Magic List [ Will-O-Wisp ] (Will-O-Wisp/Light Spirit) / [ Shade ] (Shade/Dark Spirit): Expansion=Final score, duration, distance, targets, damage certainty Resist=Reduced effect Shade is the spirit of darkness that opposes will-o-wisp, and is also the ... [truncated] (2 shared statement(s))
- [[sword-world-rpg-complete-edition-control-spirit-lesser]] - shared statements: [ Control Spirit ] (Various lesser spirits) shares source evidence from 5.1.14 Spirit Magic List / 2nd Level Spirit Magic List [ Will-O-Wisp ] (Will-O-Wisp/Light Spirit) / [ Shade ] (Shade/Dark Spirit): Expansion=Final score, duration, distance, targets, damage certainty Resist=Reduced effect Shade is the spirit of darkness that opposes will-o-wisp, and is also the ... [truncated] (1 shared statement(s))
- [[sword-world-rpg-complete-edition-shade]] - shared statements: Shade shares source evidence from 5.1.14 Spirit Magic List / 2nd Level Spirit Magic List [ Will-O-Wisp ] (Will-O-Wisp/Light Spirit) / [ Shade ] (Shade/Dark Spirit): Expansion=Final score, duration, distance, targets, damage certainty Resist=Reduced effect Shade is the spirit of darkness that opposes will-o-wisp, and is also the ... [truncated] (1 shared statement(s))
- [[sword-world-rpg-complete-edition-section-4-5-5-final-damage-0c099f84]] - source section: 4.5.5 Final Damage shares technical record from 4.5.5 Final Damage: final damage = base damage + bonus damage - monster's defense points (2 shared atom(s))
- [[sword-world-rpg-complete-edition-section-attacks-from-monsters-against-characters-4-6-5-final-damage-cb8f53e4]] - source section: Attacks From Monsters Against Characters / 4.6.5 Final Damage shares source evidence from Attacks From Monsters Against Characters / 4.6.5 Final Damage: The final damage your character suffers from a monster equals the monster's strike points minus the result of your defense roll plus your character's damage reduction .; Attacks From Monsters Against Characters / 4.6.5 Final Damage shares technical record from Attacks From Monsters Against Characters / 4.6.5 Final Damage: Final damage = monster's strike points - (defense roll result + damage reduction) (4 shared statement(s), 2 shared atom(s))

## Source

- [[sword-world-rpg-complete-edition]]
