---
page_id: javascriptallonge-recipe-shadowy-variables-from-a-shadowy-planet
page_kind: recipe
summary: shadowy variables from a shadowy planet: reusable source-backed pattern with 8 statement(s) and 2 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-01
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: shadowy-variables-from-a-shadowy-planet
projection_coverage: recipe-javascriptallonge-recipe-shadowy-variables-from-a-shadowy-planet@2132e4ec9f9cc5f8f45884798bad4d4f
---

# shadowy variables from a shadowy planet

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-and-also-closures-and-scope-shadowy-variables-from-a-shadowy-planet-71d66043]].
- Evidence roles: decision, explanation, example.

## Applicability And Rationale

- An interesting thing happens when a variable has the same name as an ancestor environment's variable. _(javascriptallonge.pdf (source-range-0e12e052-00366))_
- Although its parent also defines an x , it is ignored when evaluating x + y . _(javascriptallonge.pdf (source-range-0e12e052-00368))_
- The function (x, y) => x + y is a pure function, because its x is defined within its own environment. _(javascriptallonge.pdf (source-range-0e12e052-00368))_
- JavaScript always searches for a binding starting with the functions own environment and then each parent in turn until it finds one. _(javascriptallonge.pdf (source-range-0e12e052-00368))_
- The x in the great-great-grandparent scope is ignored, as are both w s. _(javascriptallonge.pdf (source-range-0e12e052-00370))_
- When a variable has the same name as an ancestor environment's binding, it is said to shadow the ancestor. _(javascriptallonge.pdf (source-range-0e12e052-00370))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-00367)_

```
(x) =>
(x, y) => x + y
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-00369)_

```
(x) =>
(x, y) =>
(w, z) =>
(w) =>
x + y + z
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-and-also-closures-and-scope-shadowy-variables-from-a-shadowy-planet-71d66043]]
