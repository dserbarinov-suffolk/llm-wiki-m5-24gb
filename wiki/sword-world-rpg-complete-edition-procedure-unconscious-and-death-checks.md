---
page_id: sword-world-rpg-complete-edition-procedure-unconscious-and-death-checks
page_kind: procedure
summary: Complete Unconscious and Death Checks: 4 ordered step(s), 6 decision point(s), 9 authoritative dependency reference(s), 0 review-only dependency reference(s), projection ready from raw/Sword World RPG - Complete Edition.pdf.
page_family: procedure-guide
sources: raw/Sword World RPG - Complete Edition.pdf
updated: 2026-07-07
domain: sword-world-rpg-complete-edition
category_path: procedures/sword-world-rpg-complete-edition
source_id: Sword World RPG - Complete Edition.pdf
aliases: complete-unconscious-and-death-checks, unconscious-and-death-checks
projection_coverage: procedure-sword-world-rpg-complete-edition-procedure-unconscious-and-death-checks@c4aec5746e1d89dcc86c610df48b15a2
---

# Unconscious and Death Checks

From [[sword-world-rpg-complete-edition]].

## Goal

- Complete Unconscious and Death Checks.

## Procedure Steps

1. **Adventurer Death Checks** (`validate`) - evidence section [[sword-world-rpg-complete-edition-section-4-9-unconscious-and-death-checks-4-9-1-adventurer-death-checks-20a869aa]].
   - Any adventurer who falls to 0 or negative life force is now at risk of dying . _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01378))_
   - The baseline score is life force resistance (adventurer level + life force bonus) and the target score is 7 . _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01379))_
   - This check is made using a life force resistance roll . _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01379))_
   - If the character's life force is negative , the negative amount will be used as a penalty . _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01379))_
   - life force resistance + 2D -(damage applied beyond life force) < 7 → death _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01381))_
   - His life force resistance is 5 (adventurer level 2, life force bonus +3). _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01383))_
   - Since Ducard II has a life force of -4 , that will also be the penalty. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01383))_
   - His result after rolling 2D is 7 . _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01383))_
   - If the result of this death check had been 6 or lower, Ducard II would have met an untimely end . _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01384))_
   - 5 (life force resistance) + 7 (roll) - 4 (penalty) = 8 , which is greater or equal than 7. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01384))_
   - Evidence dependencies:
     - `rule`: [[sword-world-rpg-complete-edition-section-4-9-unconscious-and-death-checks-4-9-1-adventurer-death-checks-20a869aa]]#atom-technical-atom-5c0f3503f46b4ceb You must roll the dice to determine if your character survives. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01378))_
     - `formula`: [[sword-world-rpg-complete-edition-section-4-9-unconscious-and-death-checks-4-9-1-adventurer-death-checks-20a869aa]]#atom-technical-atom-a5c8d5b73f3394cb life force resistance + 2D - (damage applied beyond life force) ≥ 7 → survival _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01380))_
     - `rule`: [[sword-world-rpg-complete-edition-section-4-9-unconscious-and-death-checks-4-9-1-adventurer-death-checks-20a869aa]]#atom-technical-atom-68c6fe0a0136f544 Ducard II, with a life force of -4 , must make a death check . _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01383))_
2. **Death Checks Every Hour** (`validate`) - evidence section [[sword-world-rpg-complete-edition-section-4-9-unconscious-and-death-checks-4-9-2-death-checks-every-hour-523e5511]].
   - Characters with 0 or negative life force remain unconscious, even if they successfully survived a death check. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01386))_
   - and have their life force increased by up to at least 1 (positive) point, they will regain consciousness, but if they're left unconscious, they may die. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01386))_
   - The target score is still 7 , and if their life force is still negative , it' s still a penalty . _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01387))_
   - At this time, their life force becomes 1 point. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01388))_
   - If the result is double sixes (automatic success), the character will regain consciousness on their own. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01388))_
   - If the result is any success other than double sixes, the character is alive _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01389))_
   - Ducard II has 18 life force. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01391))_
   - If the result is failure, the character will die. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01393))_
   - Evidence dependencies:
     - `rule`: [[sword-world-rpg-complete-edition-section-4-9-unconscious-and-death-checks-4-9-2-death-checks-every-hour-523e5511]]#atom-technical-atom-e3a5d42d5426123f Characters with 0 or negative life force must make a death check every hour . _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01387))_
     - `rule`: [[sword-world-rpg-complete-edition-section-4-9-unconscious-and-death-checks-4-9-2-death-checks-every-hour-523e5511]]#atom-technical-atom-60caf840338650d8 In one hour , they must make another death check. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01392))_
3. **Monster Death Check** (`validate`) - evidence section [[sword-world-rpg-complete-edition-section-4-9-unconscious-and-death-checks-4-9-3-monster-death-check-3690271a]].
   - A score called the monster's life point resistance is used instead. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01395))_
   - Subtract the amount of negative life points, if any, from life point resistance, and if the result is 7 or greater , the monster is alive . _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01395))_
   - If the result is 6 or lower , the monster is dead . _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01395))_
   - A goblin's life point resistance score is 10 . _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01397))_
   - 10-6= 4 , which is less than 7 . _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01397))_
   - If it's alive after a death check, it recovers 1 life point every hour , and will regain consciousness when it reaches (positive) 1 life point. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01398))_
   - Evidence dependencies:
     - `rule`: [[sword-world-rpg-complete-edition-section-4-9-unconscious-and-death-checks-4-9-3-monster-death-check-3690271a]]#atom-technical-atom-eddf10cd6080c6de Monsters with 0 or negative life points must also make a check to see if they live or die. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01395))_
4. **Mercy** (`step`) - evidence section [[sword-world-rpg-complete-edition-section-4-9-unconscious-and-death-checks-4-9-4-mercy-f2205b71]].
   - On Table 1-8: Weapons, maces , clubs , and staves are classified as dull weapons. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01400))_
   - However, even if an item is classified as one of these, if you throw it, you cannot declare mercy. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01400))_
   - However, to do so, their weapon must be a dull weapon (a bludgeoning weapon). _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01400))_
   - It cannot be done after a hit or after damage check. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01402))_
   - mercy when using a barehanded attack. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01402))_
   - On any other roll, the character remains alive . _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01403))_
   - A character who falls down with 0 or negative life force due to an attack that was declared to be mercy , will only fail their death check if double ones are rolled. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01403))_
   - Evidence dependencies:
     - `rule`: [[sword-world-rpg-complete-edition-section-4-9-unconscious-and-death-checks-4-9-4-mercy-f2205b71]]#atom-technical-atom-04a0eaddcefce05c If a character does not want to kill their opponent, they can declare mercy . _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01400))_
     - `rule`: [[sword-world-rpg-complete-edition-section-4-9-unconscious-and-death-checks-4-9-4-mercy-f2205b71]]#atom-technical-atom-a7436a2b358339c4 You must declare mercy before you make a hit check for your attack. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01402))_
     - `rule`: [[sword-world-rpg-complete-edition-section-4-9-unconscious-and-death-checks-4-9-4-mercy-f2205b71]]#atom-technical-atom-1b6efc39f5e3d37d If left untreated, they must make another death check after 1 hour , and _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01404))_

## Decisions And Constraints

- This check is made using a life force resistance roll . The baseline score is life force resistance (adventurer level + life force bonus) and the target score is 7 . If the character's life force is negative , the negative amount will be used as a penalty . _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01379))_
- 5 (life force resistance) + 7 (roll) - 4 (penalty) = 8 , which is greater or equal than 7. Ducard II survives. If the result of this death check had been 6 or lower, Ducard II would have met an untimely end . _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01384))_
- Monsters with 0 or negative life points must also make a check to see if they live or die. Do not roll the dice at this time. A score called the monster's life point resistance is used instead. Subtract the amount of negative life points, if any, from life point resistance, and if the result is 7 or greater , the monster is alive . If the result is 6 or lower , the monster is dead . _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01395))_
- A monster's first death check determines whether or not it survives. If it's alive after a death check, it recovers 1 life point every hour , and will regain consciousness when it reaches (positive) 1 life point. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01398))_
- mercy when using a barehanded attack. You must declare mercy before you make a hit check for your attack. It cannot be done after a hit or after damage check. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01402))_
- A character who falls down with 0 or negative life force due to an attack that was declared to be mercy , will only fail their death check if double ones are rolled. On any other roll, the character remains alive . _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01403))_

## Authoritative Dependencies

### Formula
- [[sword-world-rpg-complete-edition-section-4-9-unconscious-and-death-checks-4-9-1-adventurer-death-checks-20a869aa]]#atom-technical-atom-a5c8d5b73f3394cb life force resistance + 2D - (damage applied beyond life force) ≥ 7 → survival _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01380))_

### Rule
- [[sword-world-rpg-complete-edition-section-4-9-unconscious-and-death-checks-4-9-1-adventurer-death-checks-20a869aa]]#atom-technical-atom-68c6fe0a0136f544 Ducard II, with a life force of -4 , must make a death check . _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01383))_
- [[sword-world-rpg-complete-edition-section-4-9-unconscious-and-death-checks-4-9-2-death-checks-every-hour-523e5511]]#atom-technical-atom-e3a5d42d5426123f Characters with 0 or negative life force must make a death check every hour . _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01387))_
- [[sword-world-rpg-complete-edition-section-4-9-unconscious-and-death-checks-4-9-2-death-checks-every-hour-523e5511]]#atom-technical-atom-60caf840338650d8 In one hour , they must make another death check. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01392))_
- [[sword-world-rpg-complete-edition-section-4-9-unconscious-and-death-checks-4-9-4-mercy-f2205b71]]#atom-technical-atom-1b6efc39f5e3d37d If left untreated, they must make another death check after 1 hour , and _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01404))_
- [[sword-world-rpg-complete-edition-section-4-9-unconscious-and-death-checks-4-9-1-adventurer-death-checks-20a869aa]]#atom-technical-atom-5c0f3503f46b4ceb You must roll the dice to determine if your character survives. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01378))_
- [[sword-world-rpg-complete-edition-section-4-9-unconscious-and-death-checks-4-9-3-monster-death-check-3690271a]]#atom-technical-atom-eddf10cd6080c6de Monsters with 0 or negative life points must also make a check to see if they live or die. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01395))_
- [[sword-world-rpg-complete-edition-section-4-9-unconscious-and-death-checks-4-9-4-mercy-f2205b71]]#atom-technical-atom-04a0eaddcefce05c If a character does not want to kill their opponent, they can declare mercy . _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01400))_
- [[sword-world-rpg-complete-edition-section-4-9-unconscious-and-death-checks-4-9-4-mercy-f2205b71]]#atom-technical-atom-a7436a2b358339c4 You must declare mercy before you make a hit check for your attack. _(Sword World RPG - Complete Edition.pdf (source-range-e5870dca-01402))_

## Execution Readiness

- Projection status: `ready`.
- Authoritative dependencies: 9.
- Review-only dependencies: 0.
- Missing dependencies: 0.
- The procedure is complete when every step output has been recorded or validated.

## Source Trail

- Source manifest: [[sword-world-rpg-complete-edition]]
- Source section: [[sword-world-rpg-complete-edition-section-4-9-unconscious-and-death-checks-351dfe08]]
