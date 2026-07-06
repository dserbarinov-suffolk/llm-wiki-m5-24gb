---
page_id: javascriptallonge-section-interactive-generators-representing-naughts-and-crosses-as-a-stateless-function-45305bce
page_kind: source
summary: Interactive Generators / representing naughts and crosses as a stateless function: 18 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-interactive-generators-representing-naughts-and-crosses-as-a-stateless-function-45305bce@b6302183d7993aafdde72e83ba8b2991
---

# Interactive Generators / representing naughts and crosses as a stateless function

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-interactive-generators-representing-naughts-and-crosses-as-a-stateful-function-2e75ec69]] - next source section: Interactive Generators / representing naughts and crosses as a stateful function

### Source structure

- [[javascriptallonge-section-interactive-generators-21aeba33]] - broader source section: Interactive Generators
- [[javascriptallonge-section-interactive-generators-representing-naughts-and-crosses-as-a-stateless-function-we-get-ce93398d]] - narrower source section: Interactive Generators / representing naughts and crosses as a stateless function / We get:
- [[javascriptallonge-section-interactive-generators-representing-naughts-and-crosses-as-a-stateless-function-will-be-represen-e113ddff]] - narrower source section: Interactive Generators / representing naughts and crosses as a stateless function / Will be represented as:
- [[javascriptallonge-section-interactive-generators-representing-naughts-and-crosses-as-a-stateless-function-would-be-3-produ-257c1d9a]] - narrower source section: Interactive Generators / representing naughts and crosses as a stateless function / Would be 3 , producing:

## Statements

- We could plays naughts and crosses as a stateless function. We encode each position of the board in some fashion, and then we build a dictionary from positions to moves. For example, the entry for: _(javascriptallonge.pdf (source-range-c98ab3e6-01891))_
- We encode each position of the board in some fashion, and then we build a dictionary from positions to moves. _(javascriptallonge.pdf (source-range-c98ab3e6-01891))_

## Statements by subsection

### Interactive Generators / representing naughts and crosses as a stateless function / Would be 3 , producing:

- We can encode the board in several different ways. We could use multiline strings with formatting just as we've written it here, but it is a design smell to couple presentation with modelling. Our function should be just as useful on a teletype as it would be backing a DOM game that uses a table, or a browser game that draws on Canvas. _(javascriptallonge.pdf (source-range-c98ab3e6-01899))_

### Interactive Generators / representing naughts and crosses as a stateless function / Will be represented as:

- We can use a POJO to make a map from positions to moves. We'll use the [] notation for keys, it allows us to use any expression as a key, and JavaScript will convert it to a string. So if we write: _(javascriptallonge.pdf (source-range-c98ab3e6-01908))_

## Technical atoms

### Technical frame 1: Interactive Generators / representing naughts and crosses as a stateless function

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01891))_

> We could plays naughts and crosses as a stateless function. We encode each position of the board in some fashion, and then we build a dictionary from positions to moves. For example, the entry for:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01892))_

<a id="atom-technical-atom-2cbe2ed78dcdcd6e"></a>
> [Figure] (p.275)

### Technical frame 2: Interactive Generators / representing naughts and crosses as a stateless function / We get:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01916))_

<a id="atom-technical-atom-e8bd210dde564a7c"></a>
```
statelessNaughtsAndCrosses([
'o', 'x', ' ',
' ', ' ', ' ',
'o', 'x', ' '
])
//=> 3
```
