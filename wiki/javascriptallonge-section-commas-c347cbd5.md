---
page_id: javascriptallonge-section-commas-c347cbd5
page_kind: source
summary: commas: 5 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-commas-c347cbd5@61c63691e42660a4316c51bdb07de17d
---

# commas

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-functions-that-return-values-and-evaluate-expressions-6ffa5875]] - previous source section: functions that return values and evaluate expressions
- [[javascriptallonge-section-or-even-dff7248d]] - next source section: Or even:

## Statements

- The comma operator in JavaScript is interesting. It takes two arguments, evaluates them both, and itself evaluates to the value of the right-hand argument. In other words: _(javascriptallonge.pdf (source-range-c98ab3e6-00195))_

## Technical atoms

### Technical frame 1: commas

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00195))_

> The comma operator in JavaScript is interesting. It takes two arguments, evaluates them both, and itself evaluates to the value of the right-hand argument. In other words:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00196))_

<a id="atom-technical-atom-f6e57dd43b3f2e06"></a>
```
//=> 2
(1 + 1, 2 + 2)
```

### Technical frame 2: commas

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00195))_

> The comma operator in JavaScript is interesting. It takes two arguments, evaluates them both, and itself evaluates to the value of the right-hand argument. In other words:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00198))_

<a id="atom-technical-atom-71e263739b17d95f"></a>
```
(() => (1 + 1, 2 + 2))()
//=> 4
```

### Technical frame 3: commas

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00195))_

> The comma operator in JavaScript is interesting. It takes two arguments, evaluates them both, and itself evaluates to the value of the right-hand argument. In other words:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00199))_

<a id="atom-technical-atom-f6b614bc05a9f73a"></a>
> This is useful when trying to do things that might involve side-effects , but we'll get to that later.
