---
page_id: javascriptallonge-section-representing-naughts-and-crosses-as-a-stateful-function-44ba54ff
page_kind: source
summary: representing naughts and crosses as a stateful function: 6 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-representing-naughts-and-crosses-as-a-stateful-function-44ba54ff@6c152bea40f7f5d1a5c8c4e029b1b1f2
---

# representing naughts and crosses as a stateful function

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-we-get-b98bd7dc]] - previous source section: We get:
- [[javascriptallonge-section-this-seems-familiar-42bba055]] - next source section: this seems familiar

## Statements

- Our statelessNaughtsAndCrosses function pushes the work of tracking the game's state onto us, the player. What if we want to exchange moves with the function? In that case, we need a stateful function. Our 'API' will work like this: When we want a new game, we'll call a function that will return a game function, We'll call the game function repeatedly, passing our moves, and get the opponent's moves from it. _(javascriptallonge.pdf (source-range-c98ab3e6-01874))_
- Let's recap what we have: We have a stateful function, but we built it by wrapping a stateless function in a function that updates state based on the moves we provide. The state is encoded entirely in data. _(javascriptallonge.pdf (source-range-c98ab3e6-01880))_
