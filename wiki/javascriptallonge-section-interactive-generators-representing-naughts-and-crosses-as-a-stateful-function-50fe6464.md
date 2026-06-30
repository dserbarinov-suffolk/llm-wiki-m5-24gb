---
page_id: javascriptallonge-section-interactive-generators-representing-naughts-and-crosses-as-a-stateful-function-50fe6464
page_kind: source
summary: Interactive Generators / representing naughts and crosses as a stateful function: 6 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-06-30
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-interactive-generators-representing-naughts-and-crosses-as-a-stateful-function-50fe6464@5a5e01cee6c7e721d9895173624cfb5c
---

# Interactive Generators / representing naughts and crosses as a stateful function

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-interactive-generators-a0db0ac4]] - broader source section: Interactive Generators
- [[javascriptallonge-section-interactive-generators-representing-naughts-and-crosses-as-a-stateless-function-566c2092]] - previous source section: Interactive Generators / representing naughts and crosses as a stateless function
- [[javascriptallonge-section-interactive-generators-this-seems-familiar-4e1f58a1]] - next source section: Interactive Generators / this seems familiar

## Statements

- Our statelessNaughtsAndCrosses function pushes the work of tracking the game's state onto us, the player. What if we want to exchange moves with the function? In that case, we need a stateful function. Our 'API' will work like this: When we want a new game, we'll call a function that will return a game function, We'll call the game function repeatedly, passing our moves, and get the opponent's moves from it. _(javascriptallonge.pdf (source-range-0e12e052-01918))_
- Let's recap what we have: We have a stateful function, but we built it by wrapping a stateless function in a function that updates state based on the moves we provide. The state is encoded entirely in data. _(javascriptallonge.pdf (source-range-0e12e052-01924))_
