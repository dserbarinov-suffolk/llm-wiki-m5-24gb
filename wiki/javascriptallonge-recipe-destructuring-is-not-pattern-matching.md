---
page_id: javascriptallonge-recipe-destructuring-is-not-pattern-matching
page_kind: recipe
summary: destructuring is not pattern matching: reusable source-backed pattern with 7 statement(s) and 3 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: destructuring-is-not-pattern-matching
projection_coverage: recipe-javascriptallonge-recipe-destructuring-is-not-pattern-matching@f791a84d6b89f7aa01161fb5f94da4ec
---

# destructuring is not pattern matching

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-destructuring-is-not-pattern-matching-385525f3]].
- Evidence roles: decision, explanation, constraint, definition, example.

## Applicability And Rationale

- If it does, assignments are made where appropriate. _(javascriptallonge.pdf (source-range-c98ab3e6-00842))_
- That match would fail because the array doesn't have an element to assign to what . _(javascriptallonge.pdf (source-range-c98ab3e6-00845))_
- But this is not how JavaScript works. _(javascriptallonge.pdf (source-range-c98ab3e6-00845))_
- JavaScript tries its best to assign things, and if there isn't something that fits, JavaScript binds undefined to the name. _(javascriptallonge.pdf (source-range-c98ab3e6-00845))_
- From its very inception, JavaScript has striven to avoid catastrophic errors. _(javascriptallonge.pdf (source-range-c98ab3e6-00849))_
- As a result, it often coerces values, passes undefined around, or does whatever it can to keep executing without failing. _(javascriptallonge.pdf (source-range-c98ab3e6-00849))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00844)_

```
const [what] = [];
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00846)_

```
const [what] = [];
what
//=> undefined
const [which, what,
who
//=> undefined
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00847)_

```
const [...they] = [];
they
//=> []
const [which, what, .
they
//=> []
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-destructuring-is-not-pattern-matching-385525f3]]
