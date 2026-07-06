---
page_id: javascriptallonge-section-interactive-generators-c6339bc5
page_kind: source
summary: Interactive Generators: 8 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-interactive-generators-c6339bc5@915f2b1a3f76f97442a958aa4a64562c
---

# Interactive Generators

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-after-another-drink-7aeb48ed]] - previous source section: after another drink
- [[javascriptallonge-section-representing-naughts-and-crosses-as-a-stateless-function-c813b1aa]] - next source section: representing naughts and crosses as a stateless function

## Statements

- We used generators to build iterators that maintain implicit state. We saw how to use them for recursive unfolds and state machines. But there are other times we want to build functions that maintain implicit state. Let's start by looking at a very simple example of a function that can be written statefully. _(javascriptallonge.pdf (source-range-c98ab3e6-01840))_
- Consider, for example, the moves in a game. The moves a player makes are a stream of values, just like the contents of an array can be consider a stream of values. But of course, iterating over a stream of moves requires us to wait for the game to be over so we know what moves were made. _(javascriptallonge.pdf (source-range-c98ab3e6-01842))_
- The first player will always be o , and they will always place their chequer in the top-left corner, coincidentally numbered o : _(javascriptallonge.pdf (source-range-c98ab3e6-01844))_
- x has six possible moves, but they are really just two choices: 3 and anything else: _(javascriptallonge.pdf (source-range-c98ab3e6-01849))_
- Consider, for example, the moves in a game. _(javascriptallonge.pdf (source-range-c98ab3e6-01842))_
