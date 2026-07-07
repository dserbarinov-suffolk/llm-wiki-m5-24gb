---
page_id: javascriptallonge-section-interactive-generators-representing-naughts-and-crosses-as-a-stateless-function-e2c2d97f
page_kind: source
summary: Interactive Generators / representing naughts and crosses as a stateless function: 5 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-interactive-generators-representing-naughts-and-crosses-as-a-stateless-function-e2c2d97f@155d065e09a0131a53b409ed0addabc9
---

# Interactive Generators / representing naughts and crosses as a stateless function

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-interactive-generators-representing-naughts-and-crosses-as-a-stateful-function-94951f68]] - next source section: Interactive Generators / representing naughts and crosses as a stateful function

### Source structure

- [[javascriptallonge-section-interactive-generators-c6339bc5]] - broader source section: Interactive Generators
- [[javascriptallonge-section-interactive-generators-representing-naughts-and-crosses-as-a-stateless-function-will-be-represen-66494cc9]] - narrower source section: Interactive Generators / representing naughts and crosses as a stateless function / Will be represented as:

## Statements

- We could plays naughts and crosses as a stateless function. We encode each position of the board in some fashion, and then we build a dictionary from positions to moves. For example, the entry for: _(javascriptallonge.pdf (source-range-c98ab3e6-01854))_
- We encode each position of the board in some fashion, and then we build a dictionary from positions to moves. _(javascriptallonge.pdf (source-range-c98ab3e6-01854))_

## Statements by subsection

### Interactive Generators / representing naughts and crosses as a stateless function / Would be 3 , producing:

- We can encode the board in several different ways. We could use multiline strings with formatting just as we've written it here, but it is a design smell to couple presentation with modelling. Our function should be just as useful on a teletype as it would be backing a DOM game that uses a table, or a browser game that draws on Canvas. _(javascriptallonge.pdf (source-range-c98ab3e6-01858))_

## Technical atoms

### Technical frame 1: Interactive Generators / representing naughts and crosses as a stateless function / We get:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01872))_

<a id="atom-technical-atom-807e66e77775b368"></a>
```
statelessNaughtsAndCrosses([
'o', 'x', ' ',
' ', ' ', ' ',
'o', 'x', ' '
])
//=> 3
```
