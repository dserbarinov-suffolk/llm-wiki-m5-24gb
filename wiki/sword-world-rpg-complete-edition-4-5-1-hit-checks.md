---
page_id: sword-world-rpg-complete-edition-4-5-1-hit-checks
page_kind: concept
summary: 4.5.1 Hit Checks: 8 accepted assertion(s) and 4 technical atom(s) from raw/Sword World RPG - Complete Edition.pdf.
page_family: topic-concept
sources: raw/Sword World RPG - Complete Edition.pdf
updated: 2026-07-09
domain: sword-world-rpg-complete-edition
category_path: concepts
projection_coverage: topic-state-tps_2e9bf314bfce4bf7@192238c3b2a070088783f57fb961ee35
---

# 4.5.1 Hit Checks

Source: [[sword-world-rpg-complete-edition]]

## Statements

- In other words, you roll 2D and add the result to your attack power (fighter/thief/ranger skill level + dexterity bonus) in order to meet or exceed a certain target score. (Sword World RPG - Complete Edition.pdf p.43)
- In the monsters' data, there is a score called evasion points , which becomes the target score. (Sword World RPG - Complete Edition.pdf p.43)
- character's attack power + 2D < monster's evasion points → attack fails ※ Double sixes will automatically hit, and double ones will automatically fail. (Sword World RPG - Complete Edition.pdf p.43)
- Since a hit check is also a type of success roll, double ones is an automatic failure and double sixes is an automatic success . (Sword World RPG - Complete Edition.pdf p.43)
- His attack power is 4 (fighter skill level 2, dexterity bonus 2) and the goblin's evasion points are 10. (Sword World RPG - Complete Edition.pdf p.43)
- Ducard II is fighting a goblin. (Sword World RPG - Complete Edition.pdf p.43)
- His player rolls the dice to make a hit check. (Sword World RPG - Complete Edition.pdf p.43)
- 4+8= 12 , which is more than 10. (Sword World RPG - Complete Edition.pdf p.43)

## Technical atoms

<a id="atom-1"></a>
**Atom:** rule

```
When a character attacks a monster, they must make a success roll hit check, using attack power as the baseline score.
```

<a id="atom-2"></a>
**Atom:** formula

```
character's attack power + 2D ≥ monster's evasion points → attack hits
```

<a id="atom-3"></a>
**Atom:** table

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

<a id="atom-4"></a>
**Atom:** table

```text
Table 4-2: Rating Table, Key Number
   8  6  6  6 7  7  7 8  8  8  8 8  8  8  8  9  9  9  9 10 10
                                                                    Column  14
   9  7  7  7 7  7  8 8  8  9  9 9  9  10 10 10 10 10 10 10 11
                                                                                    14
   10 8  8  8 8  8  8 9  9  9  9 10 10 10 10 10 10 11 11 11 11
                                                                                    **
   11 9  9  9 9  9  9 9  9 10 10 10 10 10 10 11 11 11 12 12 12
                                                                                    1
   12 10 10 10 10 10 10 10 10 10 10 10 10 10 10 11 12 12 12 13 13
                                                                                    2
                                                                                    3
      Key Number
                                                                                    4
      40 41 42 43 44 45 46 47 48 49 50
                                                                                    4
 2D 2  ** ** ** ** ** ** ** ** ** ** **
                                                                                    4
   3  4  4  4 4  4  4 4  4  4 4  4
                                                                                    5
   4  5  6  6 6  6  6 6  6  6 6  6
                                                                                    6
   5  6  6  7 7  7  7 7  7  7 7  8
                                                                                    7
   6  7  7  7 8  8  9 9  9  9 10 10
                                                                                    8
   7  9  9  9 9 10 10 10 10 10 10 10
   8  10 10 10 10 10 10 10 11 12 12 12                                    The  player should then roll 2D.
   9  11 11 11 11 11 11 12 12 12 12 12                                 Follow along the row next to the result
                                                                    and look for the number under the key
   10 11 12 12 12 12 12 13 13 13 13 13
                                                                    number  column  that matches your
   11 12 12 13 13 13 13 13 13 13 14 15
                                                                    character's strike power. That's the base
```
