---
page_id: javascriptallonge-section-the-first-sip-basic-functions-as-little-as-possible-about-functions-but-no-less-commas-53801ea8
page_kind: source
summary: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / commas: 4 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-the-first-sip-basic-functions-as-little-as-possible-about-functions-but-no-less-commas-53801ea8@46cc3d52ca35368de0e48c96fa7f88c7
---

# The first sip: Basic Functions / As Little As Possible About Functions, But No Less / commas

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-the-first-sip-basic-functions-as-little-as-possible-about-functions-but-no-less-functions-that-r-a65d460b]] - previous source section: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions that return values and evaluate expressions

### Source structure

- [[javascriptallonge-section-the-first-sip-basic-functions-as-little-as-possible-about-functions-but-no-less-a62974a6]] - broader source section: The first sip: Basic Functions / As Little As Possible About Functions, But No Less

## Statements

- The comma operator in JavaScript is interesting. It takes two arguments, evaluates them both, and itself evaluates to the value of the right-hand argument. In other words: _(javascriptallonge.pdf (source-range-c98ab3e6-00195))_

## Technical atoms

### Technical frame 1: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / commas

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00195))_

> The comma operator in JavaScript is interesting. It takes two arguments, evaluates them both, and itself evaluates to the value of the right-hand argument. In other words:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00196))_

<a id="atom-technical-atom-f6e57dd43b3f2e06"></a>
```
//=> 2
(1 + 1, 2 + 2)
```

### Technical frame 2: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / commas

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00195))_

> The comma operator in JavaScript is interesting. It takes two arguments, evaluates them both, and itself evaluates to the value of the right-hand argument. In other words:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00198))_

<a id="atom-technical-atom-71e263739b17d95f"></a>
```
(() => (1 + 1, 2 + 2))()
//=> 4
```
