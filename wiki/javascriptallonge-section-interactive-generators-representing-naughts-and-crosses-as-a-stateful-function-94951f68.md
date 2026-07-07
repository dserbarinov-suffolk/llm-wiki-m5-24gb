---
page_id: javascriptallonge-section-interactive-generators-representing-naughts-and-crosses-as-a-stateful-function-94951f68
page_kind: source
summary: Interactive Generators / representing naughts and crosses as a stateful function: 6 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-interactive-generators-representing-naughts-and-crosses-as-a-stateful-function-94951f68@bca1419cc877cfdfb3c68f8ba5a0ee1b
---

# Interactive Generators / representing naughts and crosses as a stateful function

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-interactive-generators-representing-naughts-and-crosses-as-a-stateless-function-e2c2d97f]] - previous source section: Interactive Generators / representing naughts and crosses as a stateless function
- [[javascriptallonge-section-interactive-generators-this-seems-familiar-ca8bdeb5]] - next source section: Interactive Generators / this seems familiar

### Source structure

- [[javascriptallonge-section-interactive-generators-c6339bc5]] - broader source section: Interactive Generators

### Recipes

- [[javascriptallonge-recipe-representing-naughts-and-crosses-as-a-stateful-function]] - recipe pattern: representing naughts and crosses as a stateful function

## Statements

- Our statelessNaughtsAndCrosses function pushes the work of tracking the game's state onto us, the player. What if we want to exchange moves with the function? In that case, we need a stateful function. Our 'API' will work like this: When we want a new game, we'll call a function that will return a game function, We'll call the game function repeatedly, passing our moves, and get the opponent's moves from it. _(javascriptallonge.pdf (source-range-c98ab3e6-01874))_
- Let's recap what we have: We have a stateful function, but we built it by wrapping a stateless function in a function that updates state based on the moves we provide. The state is encoded entirely in data. _(javascriptallonge.pdf (source-range-c98ab3e6-01880))_
