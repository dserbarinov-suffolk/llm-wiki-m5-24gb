---
page_id: javascriptallonge-recipe-flip
page_kind: recipe
summary: Flip: reusable source-backed pattern with 1 statement(s) and 8 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: flip
projection_coverage: recipe-javascriptallonge-recipe-flip@165cce5140c0a9425985e4d1633bb491
---

# Flip

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-flip-869ff826]].
- Evidence roles: decision, explanation, example, structured-state.

## Applicability And Rationale

- What we have now is a function that takes a function and 'flips' the order of arguments around, then curries it. _(javascriptallonge.pdf (source-range-c98ab3e6-01435))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01422)_

```
const mapWith = (fn) => (list) => list.map(fn);
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01424)_

```
const mapWith = (fn) => (list) => map(list, fn);
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01426)_

```
const mapWith = (fn, list) => map(list, fn);
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01428)_

```
const mapper = (list) => (fn) => map(list, fn);
```

### Atom 5: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01430)_

```
const mapWith = (fn) => (list) => map(list, fn);
```

### Atom 6: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01432)_

```
const mapWith = (first) => (second) => map(second, first);
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-flip-869ff826]]
