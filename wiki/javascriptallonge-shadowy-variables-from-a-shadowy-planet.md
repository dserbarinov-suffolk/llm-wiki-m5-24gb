---
page_id: javascriptallonge-shadowy-variables-from-a-shadowy-planet
page_kind: concept
summary: topic-concept: 11 supported fragment(s) and 2 related link(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: page-projection-pgp_08ad775113d9e565@2b435e7176060db1c48be365b4ef0017
---

# shadowy variables from a shadowy planet

Source: [[javascriptallonge]]

## Statements

- An interesting thing happens when a variable has the same name as an ancestor environment's variable. (javascriptallonge.pdf p.47)
- The function (x, y) => x + y is a pure function, because its x is defined within its own environment. (javascriptallonge.pdf p.47)
- Although its parent also defines an x , it is ignored when evaluating x + y . (javascriptallonge.pdf p.47)
- When evaluating x + y + z , JavaScript will find x and y in the great-grandparent scope and z in the parent scope. (javascriptallonge.pdf p.47)
- The x in the great-great-grandparent scope is ignored, as are both w s. (javascriptallonge.pdf p.47)
- When a variable has the same name as an ancestor environment's binding, it is said to shadow the ancestor. (javascriptallonge.pdf p.47)
- This is often a good thing. (javascriptallonge.pdf p.47)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

```
(x) =>
(x, y) => x + y
```

<a id="atom-2"></a>
**Atom:** code block

```
(x) =>
(x, y) =>
(w, z) =>
(w) =>
x + y + z
```


## Related pages

- [[javascriptallonge-it-s-always-the-environment]] - contextualizes: source-supported topic dependency
- [[javascriptallonge-which-came-first-the-chicken-or-the-egg]] - contextualizes: source-supported topic dependency
