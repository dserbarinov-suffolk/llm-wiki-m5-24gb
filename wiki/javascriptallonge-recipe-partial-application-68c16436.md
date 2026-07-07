---
page_id: javascriptallonge-recipe-partial-application-68c16436
page_kind: recipe
summary: partial application: reusable source-backed pattern with 9 statement(s) and 5 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: partial-application
projection_coverage: recipe-javascriptallonge-recipe-partial-application-68c16436@1676d9f1919dea9e2fb1bfd102de02ae
---

# partial application

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-and-also-building-blocks-partial-application-68c16436]].
- Evidence roles: decision, constraint, example, structured-state.

## Applicability And Rationale

- In that case, we can't get the final value, but we can get a function that represents part of our application. _(javascriptallonge.pdf (source-range-c98ab3e6-00576))_
- Another basic building block is partial application . _(javascriptallonge.pdf (source-range-c98ab3e6-00576))_
- Code is easier than words for this. _(javascriptallonge.pdf (source-range-c98ab3e6-00577))_
- The Underscore 39 library provides a higher-order function called map . _(javascriptallonge.pdf (source-range-c98ab3e6-00577))_
- We can abstract this one level higher. _(javascriptallonge.pdf (source-range-c98ab3e6-00582))_
- The resulting functionsquareAll -is still the map function, it's just that we've applied one of its two arguments already. _(javascriptallonge.pdf (source-range-c98ab3e6-00582))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00578)_

```
_.map([1, 2, 3], (n) => n * n)
//=> [1, 4, 9]
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00581)_

```
const squareAll = (array) => map(array,
(n) => n * n);
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00583)_

```
const mapWith = (fn) =>
(array) => map(array, fn);
const squareAll = mapWith((n) => n * n);
squareAll([1, 2, 3])
//=> [1, 4, 9]
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00586)_

```
const safeSquareAll = mapWith(maybe((n) => n * n));
```

### Atom 5: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00587)_

```
safeSquareAll([1, null, 2, 3])
//=> [1, null, 4, 9]
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-and-also-building-blocks-partial-application-68c16436]]
