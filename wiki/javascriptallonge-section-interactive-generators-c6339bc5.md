---
page_id: javascriptallonge-section-interactive-generators-c6339bc5
page_kind: source
summary: Interactive Generators: 9 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-interactive-generators-c6339bc5@08b1c492b568acf862c46d2571e2e3d7
---

# Interactive Generators

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-interlude-the-carpenter-interviews-for-a-job-9cc5ffd7]] - previous source section: Interlude: The Carpenter Interviews for a Job
- [[javascriptallonge-section-operations-that-transform-one-iterable-into-another-9f8c6529]] - next source section: operations that transform one iterable into another

### Source structure

- [[javascriptallonge-section-interactive-generators-representing-naughts-and-crosses-as-a-stateful-function-94951f68]] - narrower source section: Interactive Generators / representing naughts and crosses as a stateful function
- [[javascriptallonge-section-interactive-generators-representing-naughts-and-crosses-as-a-stateless-function-e2c2d97f]] - narrower source section: Interactive Generators / representing naughts and crosses as a stateless function
- [[javascriptallonge-section-interactive-generators-this-seems-familiar-ca8bdeb5]] - narrower source section: Interactive Generators / this seems familiar

### Collections

- [[javascriptallonge-collection-interactive-generators-c6339bc5]] - collection page: Interactive Generators

### Topics

- [[javascriptallonge-interactive-generator]] - topic hub: opens the topic page for Interactive Generator

## Statements

- We used generators to build iterators that maintain implicit state. We saw how to use them for recursive unfolds and state machines. But there are other times we want to build functions that maintain implicit state. Let's start by looking at a very simple example of a function that can be written statefully. _(javascriptallonge.pdf (source-range-c98ab3e6-01840))_
- Consider, for example, the moves in a game. The moves a player makes are a stream of values, just like the contents of an array can be consider a stream of values. But of course, iterating over a stream of moves requires us to wait for the game to be over so we know what moves were made. _(javascriptallonge.pdf (source-range-c98ab3e6-01842))_
- The first player will always be o , and they will always place their chequer in the top-left corner, coincidentally numbered o : _(javascriptallonge.pdf (source-range-c98ab3e6-01844))_
- x has six possible moves, but they are really just two choices: 3 and anything else: _(javascriptallonge.pdf (source-range-c98ab3e6-01849))_
- Consider, for example, the moves in a game. _(javascriptallonge.pdf (source-range-c98ab3e6-01842))_

## Statements by subsection

### Interactive Generators / Basic Operations on Iterables

- Here are the operations we've defined on Iterables. As discussed, they preserve the collection semantics of the iterable they are given: _(javascriptallonge.pdf (source-range-c98ab3e6-01900))_
