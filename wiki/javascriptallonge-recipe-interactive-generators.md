---
page_id: javascriptallonge-recipe-interactive-generators
page_kind: recipe
summary: interactive generators: reusable source-backed pattern with 6 statement(s) and 1 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: interactive-generators
projection_coverage: recipe-javascriptallonge-recipe-interactive-generators@abd6482767a735ee0f2b8d01608239a1
---

# interactive generators

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-interactive-generators-this-seems-familiar-interactive-generators-0e36e551]].
- Evidence roles: decision, explanation, example.

## Applicability And Rationale

- So far, we have called iterators (and generators) with .next() . _(javascriptallonge.pdf (source-range-c98ab3e6-01890))_
- Thereafter, we call .next(...) and pass in our moves (The very first call has to be .next() without any arguments, because the generator hasn't started yet. _(javascriptallonge.pdf (source-range-c98ab3e6-01893))_
- If we wanted to pass some state to the generator before it begins, we'd do that with parameters.): aNaughtsAndCrossesGame.next().value //=> 0 aNaughtsAndCrossesGame.next(1).value //=> 6 aNaughtsAndCrossesGame.next(3).value //=> 8 aNaughtsAndCrossesGame.next(7).value //=> 4 _(javascriptallonge.pdf (source-range-c98ab3e6-01893))_
- It isn't a collection, it has no meaning if we try to spread it into parameters or as the subject of a for...of block. _(javascriptallonge.pdf (source-range-c98ab3e6-01894))_
- And sometimes, we want to use implicit state instead of explicitly storing state in our data. _(javascriptallonge.pdf (source-range-c98ab3e6-01895))_
- But the generator function allows us to maintain state implicitly. _(javascriptallonge.pdf (source-range-c98ab3e6-01895))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01892)_

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

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-interactive-generators-this-seems-familiar-interactive-generators-0e36e551]]
