---
page_id: javascriptallonge-recipe-commas
page_kind: recipe
summary: commas: reusable source-backed pattern with 1 statement(s) and 3 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: commas
projection_coverage: recipe-javascriptallonge-recipe-commas@358f2bc6edcf47766c8dd2e321c871c5
---

# commas

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-the-first-sip-basic-functions-as-little-as-possible-about-functions-but-no-less-commas-b207d7ab]].
- Evidence roles: decision, example, structured-state.

## Applicability And Rationale

- The comma operator in JavaScript is interesting. _(javascriptallonge.pdf (source-range-c98ab3e6-00203))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00204)_

```
//=> 2
(1 + 1, 2 + 2)
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00206)_

```
(() => (1 + 1, 2 + 2))()
//=> 4
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00208)_

```
() =>
(1 + 1, 2 + 2)
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-the-first-sip-basic-functions-as-little-as-possible-about-functions-but-no-less-commas-b207d7ab]]
