---
page_id: javascriptallonge-section-interactive-generators-this-seems-familiar-interactive-generators-3de32faa
page_kind: source
summary: Interactive Generators / this seems familiar / interactive generators: 9 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-06-30
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-interactive-generators-this-seems-familiar-interactive-generators-3de32faa@fdce218f0cb66b7a4b04167ecf26631d
---

# Interactive Generators / this seems familiar / interactive generators

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-interactive-generators-this-seems-familiar-4e1f58a1]] - broader source section: Interactive Generators / this seems familiar
- [[javascriptallonge-section-interactive-generators-this-seems-familiar-summary-46445b98]] - next source section: Interactive Generators / this seems familiar / summary
- [[javascriptallonge-interactive-generator]] - topic hub: opens the topic page for Interactive Generator

## Statements

- So far, we have called iterators (and generators) with .next() . But what if we pass a value to .next() ? If we could do that, a generator function that played naughts and crosses would look like this: _(javascriptallonge.pdf (source-range-0e12e052-01934))_
- Served by the Pot: Collections 260 } } break ; // ... } } const aNaughtsAndCrossesGame = generatorNaughtsAndCrosses(); We can then get the first move by calling .next() . Thereafter, we call .next(...) and pass in our moves (The very first call has to be .next() without any arguments, because the generator hasn't started yet. If we wanted to pass some state to the generator before it begins, we'd do that with parameters.): aNaughtsAndCrossesGame.next().value //=> 0 aNaughtsAndCrossesGame.next(1).value //=> 6 aNaughtsAndCrossesGame.next(3).value //=> 8 aNaughtsAndCrossesGame.next(7).value //=> 4 _(javascriptallonge.pdf (source-range-0e12e052-01937))_
- Our generator function maintains state implicitly in its control flow, but returns an iterator that we call, it doesn't call us. It isn't a collection, it has no meaning if we try to spread it into parameters or as the subject of a for...of block. _(javascriptallonge.pdf (source-range-0e12e052-01938))_
- But the generator function allows us to maintain state implicitly. And sometimes, we want to use implicit state instead of explicitly storing state in our data. _(javascriptallonge.pdf (source-range-0e12e052-01939))_
- Thereafter, we call .next(...) and pass in our moves (The very first call has to be .next() without any arguments, because the generator hasn't started yet. _(javascriptallonge.pdf (source-range-0e12e052-01937))_
- If we wanted to pass some state to the generator before it begins, we'd do that with parameters.): aNaughtsAndCrossesGame.next().value //=> 0 aNaughtsAndCrossesGame.next(1).value //=> 6 aNaughtsAndCrossesGame.next(3).value //=> 8 aNaughtsAndCrossesGame.next(7).value //=> 4 _(javascriptallonge.pdf (source-range-0e12e052-01937))_
