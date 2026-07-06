---
page_id: javascriptallonge-recipe-function-decorators
page_kind: recipe
summary: function decorators: reusable source-backed pattern with 3 statement(s) and 4 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: function-decorators
projection_coverage: recipe-javascriptallonge-recipe-function-decorators@ff7378e133a4417860114c51f1e43407
---

# function decorators

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-and-also-combinators-and-function-decorators-function-decorators-a89378c3]].
- Evidence roles: decision, constraint, explanation, structured-state, example.

## Applicability And Rationale

- So instead of writing !someFunction(42) , we can write not(someFunction)(42) . _(javascriptallonge.pdf (source-range-c98ab3e6-00567))_
- not is a function decorator because it modifies a function while remaining strongly related to the original function's semantics. _(javascriptallonge.pdf (source-range-c98ab3e6-00573))_
- Function decorators aren't strict about being pure functions, so there's more latitude for making decorators than combinators. _(javascriptallonge.pdf (source-range-c98ab3e6-00573))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00566)_

```
const not = (fn) => (x) => !fn(x)
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00568)_

```
const something = (x) => x != null;
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00570)_

```
const nothing = (x) => !something(x);
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00572)_

```
const nothing = not(something);
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-and-also-combinators-and-function-decorators-function-decorators-a89378c3]]
