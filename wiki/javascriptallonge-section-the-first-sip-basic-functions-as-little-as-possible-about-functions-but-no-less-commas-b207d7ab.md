---
page_id: javascriptallonge-section-the-first-sip-basic-functions-as-little-as-possible-about-functions-but-no-less-commas-b207d7ab
page_kind: source
summary: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / commas: 5 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-the-first-sip-basic-functions-as-little-as-possible-about-functions-but-no-less-commas-b207d7ab@112d2a7c0d4e67773a1ddb7a1cc16fd9
---

# The first sip: Basic Functions / As Little As Possible About Functions, But No Less / commas

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-the-first-sip-basic-functions-as-little-as-possible-about-functions-but-no-less-functions-that-r-5e2fa23b]] - previous source section: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions that return values and evaluate expressions

### Source structure

- [[javascriptallonge-section-the-first-sip-basic-functions-as-little-as-possible-about-functions-but-no-less-adfe6790]] - broader source section: The first sip: Basic Functions / As Little As Possible About Functions, But No Less

## Statements

- The comma operator in JavaScript is interesting. It takes two arguments, evaluates them both, and itself evaluates to the value of the right-hand argument. In other words: _(javascriptallonge.pdf (source-range-c98ab3e6-00203))_

## Technical atoms

### Technical frame 1: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / commas

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00203))_

> The comma operator in JavaScript is interesting. It takes two arguments, evaluates them both, and itself evaluates to the value of the right-hand argument. In other words:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00204))_

<a id="atom-technical-atom-55a14751ee8c81fe"></a>
```
//=> 2
(1 + 1, 2 + 2)
```

### Technical frame 2: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / commas

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00203))_

> The comma operator in JavaScript is interesting. It takes two arguments, evaluates them both, and itself evaluates to the value of the right-hand argument. In other words:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00206))_

<a id="atom-technical-atom-9ef63e44956bc182"></a>
```
(() => (1 + 1, 2 + 2))()
//=> 4
```

### Technical frame 3: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / commas

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00203))_

> The comma operator in JavaScript is interesting. It takes two arguments, evaluates them both, and itself evaluates to the value of the right-hand argument. In other words:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00207))_

<a id="atom-technical-atom-e4f6493023a2e69a"></a>
> This is useful when trying to do things that might involve side-effects , but we'll get to that later.
