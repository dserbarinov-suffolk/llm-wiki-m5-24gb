---
page_id: javascriptallonge-interactive-generators
page_kind: concept
summary: topic-concept: 15 supported fragment(s) and 0 related link(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: page-projection-pgp_f9a769a89a243d94@39384152603a8b91116c96755ec5e05f
---

# Interactive Generators

Source: [[javascriptallonge]]

## Statements

- We used generators to build iterators that maintain implicit state. (javascriptallonge.pdf p.273)
- But there are other times we want to build functions that maintain implicit state. (javascriptallonge.pdf p.273)
- We saw how to use them for recursive unfolds and state machines. (javascriptallonge.pdf p.273)
- The moves a player makes are a stream of values, just like the contents of an array can be consider a stream of values. (javascriptallonge.pdf p.273)
- But of course, iterating over a stream of moves requires us to wait for the game to be over so we know what moves were made. (javascriptallonge.pdf p.273)
- The first player will always be o , and they will always place their chequer in the top-left corner, coincidentally numbered o :. (javascriptallonge.pdf p.273)
- x has six possible moves, but they are really just two choices: 3 and anything else:. (javascriptallonge.pdf p.274)
- So far, we have called iterators (and generators) with .next() . (javascriptallonge.pdf p.282)
- Thereafter, we call .next(..) and pass in our moves (The very first call has to be .next() without any arguments, because the generator hasn't started yet. (javascriptallonge.pdf p.283)
- If we wanted to pass some state to the generator before it begins, we'd do that with parameters.): aNaughtsAndCrossesGame.next().value //=> 0 aNaughtsAndCrossesGame.next(1).value //=> 6 aNaughtsAndCrossesGame.next(3).value //=> 8 aNaughtsAndCrossesGame.next(7).value //=> 4. (javascriptallonge.pdf p.283)
- It isn't a collection, it has no meaning if we try to spread it into parameters or as the subject of a for..of block. (javascriptallonge.pdf p.283)
- And sometimes, we want to use implicit state instead of explicitly storing state in our data. (javascriptallonge.pdf p.283)
- But the generator function allows us to maintain state implicitly. (javascriptallonge.pdf p.283)

## Rules

- The moves a player makes are a stream of values, just like the contents of an array can be consider a stream of values. (javascriptallonge.pdf p.273)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

```
function* generatorNaughtsAndCrosses () {
const x1 = yield 0;
switch (x1) {
case 1:
const x2 = yield 6;
switch (x2) {
case 2:
case 4:
case 5:
case 7:
case 8:
yield 3;
break;
case 3:
const x3 = yield 8;
switch (x3) {
case 2:
case 5:
case 7:
yield 4;
break;
case 4:
yield 7;
break;
```
