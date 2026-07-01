---
page_id: javascriptallonge-recipe-function-decorators
page_kind: recipe
summary: function decorators: reusable source-backed pattern with 3 statement(s) and 4 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-01
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: function-decorators
projection_coverage: recipe-javascriptallonge-recipe-function-decorators@f2b05088d15900c0173cc4c9b07e4cc1
---

# function decorators

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-and-also-combinators-and-function-decorators-function-decorators-989cc9e8]].
- Evidence roles: decision, constraint, explanation, structured-state, example.

## Applicability And Rationale

- So instead of writing !someFunction(42) , we can write not(someFunction)(42) . _(javascriptallonge.pdf (source-range-0e12e052-00567))_
- Function decorators aren't strict about being pure functions, so there's more latitude for making decorators than combinators. _(javascriptallonge.pdf (source-range-0e12e052-00573))_
- not is a function decorator because it modifies a function while remaining strongly related to the original function's semantics. _(javascriptallonge.pdf (source-range-0e12e052-00573))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-00566)_

```
const not = (fn) => (x) => !fn(x)
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-00568)_

```
const something = (x) => x != null;
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-00570)_

```
const nothing = (x) => !something(x);
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-00572)_

```
const nothing = not(something);
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-and-also-combinators-and-function-decorators-function-decorators-989cc9e8]]
