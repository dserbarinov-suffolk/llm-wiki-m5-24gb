---
page_id: javascriptallonge-section-interactive-generators-representing-naughts-and-crosses-as-a-stateless-function-566c2092
page_kind: source
summary: Interactive Generators / representing naughts and crosses as a stateless function: 18 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-interactive-generators-representing-naughts-and-crosses-as-a-stateless-function-566c2092@0a21772d84a182e224320bf7af18c8d3
---

# Interactive Generators / representing naughts and crosses as a stateless function

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-interactive-generators-representing-naughts-and-crosses-as-a-stateful-function-50fe6464]] - next source section: Interactive Generators / representing naughts and crosses as a stateful function

### Source structure

- [[javascriptallonge-section-interactive-generators-a0db0ac4]] - broader source section: Interactive Generators
- [[javascriptallonge-section-interactive-generators-representing-naughts-and-crosses-as-a-stateless-function-we-get-5a2b4c84]] - narrower source section: Interactive Generators / representing naughts and crosses as a stateless function / We get:
- [[javascriptallonge-section-interactive-generators-representing-naughts-and-crosses-as-a-stateless-function-will-be-represen-f1dabfc6]] - narrower source section: Interactive Generators / representing naughts and crosses as a stateless function / Will be represented as:
- [[javascriptallonge-section-interactive-generators-representing-naughts-and-crosses-as-a-stateless-function-would-be-3-produ-63632d5b]] - narrower source section: Interactive Generators / representing naughts and crosses as a stateless function / Would be 3 , producing:

## Statements

- We could plays naughts and crosses as a stateless function. We encode each position of the board in some fashion, and then we build a dictionary from positions to moves. For example, the entry for: _(javascriptallonge.pdf (source-range-0e12e052-01891))_
- We encode each position of the board in some fashion, and then we build a dictionary from positions to moves. _(javascriptallonge.pdf (source-range-0e12e052-01891))_

## Statements by subsection

### Interactive Generators / representing naughts and crosses as a stateless function / Would be 3 , producing:

- We can encode the board in several different ways. We could use multiline strings with formatting just as we've written it here, but it is a design smell to couple presentation with modelling. Our function should be just as useful on a teletype as it would be backing a DOM game that uses a table, or a browser game that draws on Canvas. _(javascriptallonge.pdf (source-range-0e12e052-01899))_

### Interactive Generators / representing naughts and crosses as a stateless function / Will be represented as:

- We can use a POJO to make a map from positions to moves. We'll use the [] notation for keys, it allows us to use any expression as a key, and JavaScript will convert it to a string. So if we write: _(javascriptallonge.pdf (source-range-0e12e052-01908))_

## Technical atoms

### Technical frame 1: Interactive Generators / representing naughts and crosses as a stateless function

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01891))_

> We could plays naughts and crosses as a stateless function. We encode each position of the board in some fashion, and then we build a dictionary from positions to moves. For example, the entry for:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01892))_

<a id="atom-technical-atom-7366fb0c3b05bd59"></a>
> [Figure] (p.275)

### Technical frame 2: Interactive Generators / representing naughts and crosses as a stateless function / We get:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01916))_

<a id="atom-technical-atom-9fcf1a3c35e563fa"></a>
```
statelessNaughtsAndCrosses([
'o', 'x', ' ',
' ', ' ', ' ',
'o', 'x', ' '
])
//=> 3
```
