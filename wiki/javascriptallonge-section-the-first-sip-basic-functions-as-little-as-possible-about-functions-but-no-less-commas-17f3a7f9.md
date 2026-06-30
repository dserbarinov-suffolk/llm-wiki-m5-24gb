---
page_id: javascriptallonge-section-the-first-sip-basic-functions-as-little-as-possible-about-functions-but-no-less-commas-17f3a7f9
page_kind: source
summary: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / commas: 5 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-06-30
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-the-first-sip-basic-functions-as-little-as-possible-about-functions-but-no-less-commas-17f3a7f9@156ba3ec6f49fef44d35fc3b91d2c72b
---

# The first sip: Basic Functions / As Little As Possible About Functions, But No Less / commas

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-the-first-sip-basic-functions-as-little-as-possible-about-functions-but-no-less-40f8e29e]] - broader source section: The first sip: Basic Functions / As Little As Possible About Functions, But No Less
- [[javascriptallonge-section-the-first-sip-basic-functions-as-little-as-possible-about-functions-but-no-less-functions-that-r-5f549e47]] - previous source section: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions that return values and evaluate expressions

## Statements

- The comma operator in JavaScript is interesting. It takes two arguments, evaluates them both, and itself evaluates to the value of the right-hand argument. In other words: _(javascriptallonge.pdf (source-range-0e12e052-00203))_

## Technical atoms

### Technical frame 1: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / commas

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00203))_

> The comma operator in JavaScript is interesting. It takes two arguments, evaluates them both, and itself evaluates to the value of the right-hand argument. In other words:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00204))_

```
//=> 2
(1 + 1, 2 + 2)
```

### Technical frame 2: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / commas

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00203))_

> The comma operator in JavaScript is interesting. It takes two arguments, evaluates them both, and itself evaluates to the value of the right-hand argument. In other words:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00206))_

```
(() => (1 + 1, 2 + 2))()
//=> 4
```

### Technical frame 3: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / commas

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00203))_

> The comma operator in JavaScript is interesting. It takes two arguments, evaluates them both, and itself evaluates to the value of the right-hand argument. In other words:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00207))_

> This is useful when trying to do things that might involve side-effects , but we'll get to that later.
