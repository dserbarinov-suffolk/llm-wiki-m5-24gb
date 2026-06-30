---
page_id: rpg-cairn-2e-core-terrain
page_kind: concept
summary: Terrain: 4 statement(s) and 4 atom(s) from raw/rpg_cairn_2e_core.pdf.
page_family: topic-concept
sources: raw/rpg_cairn_2e_core.pdf
updated: 2026-06-30
domain: rpg-cairn-2e-core
category_path: concepts
projection_coverage: topic-rpg-cairn-2e-core-terrain@aaa0e3155a8d02c417715128e4caeda1
---

# Terrain

What [[rpg-cairn-2e-core]] covers about terrain:

## Statements

### Procedures / Dungeon Exploration / Actions

- Larger rooms and difficult or complex dungeon terrain may take a few turns to properly search. _(rpg_cairn_2e_core.pdf (source-range-9b4fff26-00280))_

### Procedures / Wilderness Exploration / Travel Duration

- The weather, terrain, darkness, injured party members, and other obstacles can impact travel or even make it impossible! In some cases, the party may need to add Fatigue or expend resources in order to sustain their pace. Mounts, guides, and maps can increase the party's travel speed or even negate certain penalties. _(rpg_cairn_2e_core.pdf (source-range-9b4fff26-00316))_

### Procedures / Terrain Difficulty / Wilderness Elements

- Some terrain and weather may be easier to traverse at night (desert, for example). The Warden should balance these challenges along with any other. _(rpg_cairn_2e_core.pdf (source-range-9b4fff26-00357))_

### Procedures / Terrain Difficulty / Wilderness Actions

- Travel begins. Obvious locations, features, and terrain of nearby areas are revealed according to their distance. This action is typically taken by the entire party as one. _(rpg_cairn_2e_core.pdf (source-range-9b4fff26-00371))_


## Technical atoms

### Technical frame 1: Procedures / Terrain Difficulty

**Atom:** _(rpg_cairn_2e_core.pdf (source-range-9b4fff26-00341))_

| Diﬀiculty | Terrain | Penalty | Factors |
| --- | --- | --- | --- |
| Easy | Plains, plateaus, valleys | none | Safe areas for rest, fellow travelers, good visibility |
| Tough | Forests, deserts, hills | +1 Watch | Wild animals, ﬂooding, broken equipment, falling rocks, unsafe shelters, hunter's traps |
| Perilous | Mountains, jungles, swamp | +2 Watches | Quicksand, sucking mud, choking vines, unclean water, poisonous plants and animals, poor navigation |

<details>
<summary>Raw table text</summary>

```text
Terrain Difficulty
| Diﬀiculty | Terrain | Penalty | Factors |
| --- | --- | --- | --- |
| Easy | Plains, plateaus, valleys | none | Safe areas for rest, fellow travelers, good visibility |
| Tough | Forests, deserts, hills | +1 Watch | Wild animals, ﬂooding, broken equipment, falling rocks, unsafe shelters, hunter's traps |
| Perilous | Mountains, jungles, swamp | +2 Watches | Quicksand, sucking mud, choking vines, unclean water, poisonous plants and animals, poor navigation |
```

</details>

### Technical frame 2: Procedures / Terrain Difficulty / Weather

**Atom:** _(rpg_cairn_2e_core.pdf (source-range-9b4fff26-00343))_

```text
Weather
Each	day,	the	Warden	should	roll	on	the	weather	table	for	the appropriate	season.	If	the	" Extreme "	weather	result	is	rolled	twice	in a	row,	the	weather	turns	to	" Catastrophic ".	A	squall	becomes	a hurricane,	a	storm	floods	the	valley,	etc.
1 Nice d6 Spring Summer Fall Winter Nice Fair Fair
2 Fair Nice Fair Unpleasant
3 Fair Fair Unpleasant Inclement
4 Unpleasant Unpleasant Inclement Inclement
5 Inclement Inclement Inclement Extreme
6 Extreme Extreme Extreme Extreme
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 1 | Nice d6 Spring Summer Fall Winter Nice Fair Fair |
| 2 | Fair Nice Fair Unpleasant |
| 3 | Fair Fair Unpleasant Inclement |
| 4 | Unpleasant Unpleasant Inclement Inclement |
| 5 | Inclement Inclement Inclement Extreme |
| 6 | Extreme Extreme Extreme Extreme |

</details>

### Technical frame 3: Procedures / Terrain Difficulty / Weather

**Atom:** _(rpg_cairn_2e_core.pdf (source-range-9b4fff26-00347))_

| Weather | Eﬀect | Examples |
| --- | --- | --- |
| Nice | Favorable conditions for travel. | Clear skies, sunny |
| Fair | Favorable conditions for travel. | Overcast, breezy |
| Unpleasant | Add a Fatigue or add one watch to the journey. | Gusting winds, rain showers, sweltering heat, chill air |
|  | Add a Fatigue or add +1 | Thunderstorms, |
| Inclement | watch. Increase terrain | lightning, rain, |
|  | Diﬀiculty by a step. | muddy ground |
|  | Add a Fatigue and add +1 | Blizzards, freezing |
| Extreme | watch. Increase terrain | winds, ﬂooding, mud |
|  | Diﬀiculty by a step. | slides |
| Catastrophic | Most parties cannot travel under these conditions. | Tornados, tidal waves, hurricane, volcanic eruption |

<details>
<summary>Raw table text</summary>

```text
| Weather | Eﬀect | Examples |
| --- | --- | --- |
| Nice | Favorable conditions for travel. | Clear skies, sunny |
| Fair | Favorable conditions for travel. | Overcast, breezy |
| Unpleasant | Add a Fatigue or add one watch to the journey. | Gusting winds, rain showers, sweltering heat, chill air |
|  | Add a Fatigue or add +1 | Thunderstorms, |
| Inclement | watch. Increase terrain | lightning, rain, |
|  | Diﬀiculty by a step. | muddy ground |
|  | Add a Fatigue and add +1 | Blizzards, freezing |
| Extreme | watch. Increase terrain | winds, ﬂooding, mud |
|  | Diﬀiculty by a step. | slides |
| Catastrophic | Most parties cannot travel under these conditions. | Tornados, tidal waves, hurricane, volcanic eruption |
```

</details>

### Technical frame 4: Procedures / Terrain Difficulty / Wilderness Exploration Cycle

**Context:** _(rpg_cairn_2e_core.pdf (source-range-9b4fff26-00351))_

> The players and the Warden record any loss of resources and new conditions (i.e. torch use, deprivation , etc), and the cycle repeats.

**Atom:** _(rpg_cairn_2e_core.pdf (source-range-9b4fff26-00352))_

```text
Wilderness Events
1
Encounter
Roll on an encounter table for that terrain type
or location. Don't forget to roll for NPC reactions
if applicable.
2
Sign
The party discovers a clue, spoor, or indication
of a nearby encounter, locality, hidden feature,
or information about a nearby area.
3
Environment
A shift in weather or terrain.
4
Loss
The party is faced with a choice that costs them
a resource (rations, tools, etc), time, or eﬀort.
5
Exhaustion
The party encounters a barrier, forcing eﬀort,
care or delays. This might mean spending extra
time (and an additional Wilderness Action) or
adding Fatigue to the PC's inventory to
represent their diﬀiculties.
6
Discovery
The party ﬁnds food, treasure, or other useful
resources. The Warden can instead choose to
reveal the primary feature of the area.
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 1 | Encounter Roll on an encounter table for that terrain type or location. Don't forget to roll for NPC reactions if applicable. |
| 2 | Sign The party discovers a clue, spoor, or indication of a nearby encounter, locality, hidden feature, or information about a nearby area. |
| 3 | Environment A shift in weather or terrain. |
| 4 | Loss The party is faced with a choice that costs them a resource (rations, tools, etc), time, or eﬀort. |
| 5 | Exhaustion The party encounters a barrier, forcing eﬀort, care or delays. This might mean spending extra time (and an additional Wilderness Action) or adding Fatigue to the PC's inventory to represent their diﬀiculties. |
| 6 | Discovery The party ﬁnds food, treasure, or other useful resources. The Warden can instead choose to reveal the primary feature of the area. |

</details>


## Related pages

- [[rpg-cairn-2e-core-travel]] - shared technical atoms: Travel shares technical record from Procedures / Terrain Difficulty / Weather: | Weather | Eﬀect | Examples | | --- | --- | --- | | Nice | Favorable conditions for travel. | Clear skies, sunny | | Fair | Favorable conditions for travel. | Overc ... [truncated] (1 shared atom(s))
- [[rpg-cairn-2e-core-warden]] - shared technical atoms: Warden shares technical record from Procedures / Terrain Difficulty / Weather: Weather Each	day,	the	Warden	should	roll	on	the	weather	table	for	the appropriate	season.	If	the	" Extreme "	weather	result	is	rolled	twice	in a	row,	the	weather	tur ... [truncated] (1 shared atom(s))
- [[rpg-cairn-2e-core-dungeon]] - shared statements: Dungeon shares source evidence from Procedures / Dungeon Exploration / Actions: Larger rooms and difficult or complex dungeon terrain may take a few turns to properly search. (1 shared statement(s))
- [[rpg-cairn-2e-core-dungeon-exploration]] - shared statements: Dungeon Exploration shares source evidence from Procedures / Dungeon Exploration / Actions: Larger rooms and difficult or complex dungeon terrain may take a few turns to properly search. (1 shared statement(s))

## Source

- [[rpg-cairn-2e-core]]
