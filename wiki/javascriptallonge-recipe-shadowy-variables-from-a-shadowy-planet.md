---
page_id: javascriptallonge-recipe-shadowy-variables-from-a-shadowy-planet
page_kind: recipe
summary: shadowy variables from a shadowy planet: reusable source-backed pattern with 8 statement(s) and 2 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: shadowy-variables-from-a-shadowy-planet
projection_coverage: recipe-javascriptallonge-recipe-shadowy-variables-from-a-shadowy-planet@0bc6944e929f2d292893ee054caf03a8
---

# shadowy variables from a shadowy planet

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-shadowy-variables-from-a-shadowy-planet-55213f04]].
- Evidence roles: decision, explanation, example.

## Applicability And Rationale

- An interesting thing happens when a variable has the same name as an ancestor environment's variable. _(javascriptallonge.pdf (source-range-c98ab3e6-00356))_
- The function (x, y) => x + y is a pure function, because its x is defined within its own environment. _(javascriptallonge.pdf (source-range-c98ab3e6-00358))_
- Although its parent also defines an x , it is ignored when evaluating x + y . _(javascriptallonge.pdf (source-range-c98ab3e6-00358))_
- JavaScript always searches for a binding starting with the functions own environment and then each parent in turn until it finds one. _(javascriptallonge.pdf (source-range-c98ab3e6-00358))_
- When evaluating x + y + z , JavaScript will find x and y in the great-grandparent scope and z in the parent scope. _(javascriptallonge.pdf (source-range-c98ab3e6-00360))_
- The x in the great-great-grandparent scope is ignored, as are both w s. _(javascriptallonge.pdf (source-range-c98ab3e6-00360))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00357)_

```
(x) =>
(x, y) => x + y
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00359)_

```
(x) =>
(x, y) =>
(w, z) =>
(w) =>
x + y + z
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-shadowy-variables-from-a-shadowy-planet-55213f04]]
