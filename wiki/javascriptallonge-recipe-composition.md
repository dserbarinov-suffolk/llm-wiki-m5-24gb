---
page_id: javascriptallonge-recipe-composition
page_kind: recipe
summary: composition: reusable source-backed pattern with 8 statement(s) and 3 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-01
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: composition
projection_coverage: recipe-javascriptallonge-recipe-composition@2de5e86157902cfdf12aad038af85d4d
---

# composition

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-and-also-building-blocks-composition-b488e601]].
- Evidence roles: decision, constraint, procedure, explanation, example, structured-state.

## Applicability And Rationale

- It's really that simple: Whenever you are chaining two or more functions together, you're composing them. _(javascriptallonge.pdf (source-range-0e12e052-00579))_
- You can compose them with explicit JavaScript code as we've just done. _(javascriptallonge.pdf (source-range-0e12e052-00579))_
- If that was all there was to it, composition wouldn't matter much. _(javascriptallonge.pdf (source-range-0e12e052-00581))_
- But like many patterns, using it when it applies is only 20% of the benefit. _(javascriptallonge.pdf (source-range-0e12e052-00581))_
- We'll also look at maybe: It ensures that a function does nothing if it is given nothing (like null or undefined ) as an argument. _(javascriptallonge.pdf (source-range-0e12e052-00582))_
- Once is useful for ensuring that certain side effects are not repeated. _(javascriptallonge.pdf (source-range-0e12e052-00582))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-00578)_

```
const cookAndEat = (food) => eat(cook(food));
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-00580)_

```
const compose = (a, b) => (c) => a(b(c));
const cookAndEat = compose(eat, cook);
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-00584)_

```
const actuallyTransfer= (from, to, amount) =>
// do something
const invokeTransfer = once(maybe(actuallyTransfer(...)));
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-and-also-building-blocks-composition-b488e601]]
