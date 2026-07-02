---
page_id: javascriptallonge-cross-stateful-function
page_kind: concept
summary: Cross Stateful Function: 1 statement(s) and 0 atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-cross-stateful-function@83e1cb2c897877f602e121169f9d21c1
---

# Cross Stateful Function

What [[javascriptallonge]] covers about cross stateful function:

## Statements

### Interactive Generators / representing naughts and crosses as a stateful function

- Our statelessNaughtsAndCrosses function pushes the work of tracking the game's state onto us, the player. What if we want to exchange moves with the function? In that case, we need a stateful function. Our 'API' will work like this: When we want a new game, we'll call a function that will return a game function, We'll call the game function repeatedly, passing our moves, and get the opponent's moves from it. _(javascriptallonge.pdf (source-range-0e12e052-01918))_


## Related pages

### Shared claims

- [[javascriptallonge-interactive-generator]] - shared statements: Interactive Generators shares source evidence from Interactive Generators / representing naughts and crosses as a stateful function: Our statelessNaughtsAndCrosses function pushes the work of tracking the game's state onto us, the player. What if we want to exchange moves with the function? In tha ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
