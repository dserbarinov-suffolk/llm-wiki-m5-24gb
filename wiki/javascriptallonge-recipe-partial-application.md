---
page_id: javascriptallonge-recipe-partial-application
page_kind: recipe
summary: partial application: reusable source-backed pattern with 9 statement(s) and 5 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-01
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: partial-application
projection_coverage: recipe-javascriptallonge-recipe-partial-application@c36aa26bbf932c0a1bb27fd8c9b0004b
---

# partial application

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-and-also-building-blocks-partial-application-a5e29ef2]].
- Evidence roles: decision, constraint, example, structured-state.

## Applicability And Rationale

- Another basic building block is partial application . _(javascriptallonge.pdf (source-range-0e12e052-00586))_
- In that case, we can't get the final value, but we can get a function that represents part of our application. _(javascriptallonge.pdf (source-range-0e12e052-00586))_
- The Underscore 39 library provides a higher-order function called map . _(javascriptallonge.pdf (source-range-0e12e052-00587))_
- Code is easier than words for this. _(javascriptallonge.pdf (source-range-0e12e052-00587))_
- We can abstract this one level higher. _(javascriptallonge.pdf (source-range-0e12e052-00592))_
- mapWith takes any function as an argument and returns a partially applied map function. _(javascriptallonge.pdf (source-range-0e12e052-00592))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-00588)_

```
_.map([1, 2, 3], (n) => n * n)
//=> [1, 4, 9]
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-00591)_

```
const squareAll = (array) => map(array,
(n) => n * n);
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-00593)_

```
const mapWith = (fn) =>
(array) => map(array, fn);
const squareAll = mapWith((n) => n * n);
squareAll([1, 2, 3])
//=> [1, 4, 9]
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-00596)_

```
const safeSquareAll = mapWith(maybe((n) => n * n));
```

### Atom 5: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-00597)_

```
safeSquareAll([1, null, 2, 3])
//=> [1, null, 4, 9]
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-and-also-building-blocks-partial-application-a5e29ef2]]
