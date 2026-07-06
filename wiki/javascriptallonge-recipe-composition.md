---
page_id: javascriptallonge-recipe-composition
page_kind: recipe
summary: composition: reusable source-backed pattern with 8 statement(s) and 3 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: composition
projection_coverage: recipe-javascriptallonge-recipe-composition@05885d239bb499e4619b0d483e2d05d8
---

# composition

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-and-also-building-blocks-composition-8e5c0651]].
- Evidence roles: decision, constraint, procedure, explanation, example, structured-state.

## Applicability And Rationale

- You can compose them with explicit JavaScript code as we've just done. _(javascriptallonge.pdf (source-range-c98ab3e6-00579))_
- It's really that simple: Whenever you are chaining two or more functions together, you're composing them. _(javascriptallonge.pdf (source-range-c98ab3e6-00579))_
- But like many patterns, using it when it applies is only 20% of the benefit. _(javascriptallonge.pdf (source-range-c98ab3e6-00581))_
- If that was all there was to it, composition wouldn't matter much. _(javascriptallonge.pdf (source-range-c98ab3e6-00581))_
- We'll also look at maybe: It ensures that a function does nothing if it is given nothing (like null or undefined ) as an argument. _(javascriptallonge.pdf (source-range-c98ab3e6-00582))_
- In the recipes, we'll look at a decorator called once: It ensures that a function can only be executed once. _(javascriptallonge.pdf (source-range-c98ab3e6-00582))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00578)_

```
const cookAndEat = (food) => eat(cook(food));
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00580)_

```
const compose = (a, b) => (c) => a(b(c));
const cookAndEat = compose(eat, cook);
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00584)_

```
const actuallyTransfer= (from, to, amount) =>
// do something
const invokeTransfer = once(maybe(actuallyTransfer(...)));
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-and-also-building-blocks-composition-8e5c0651]]
