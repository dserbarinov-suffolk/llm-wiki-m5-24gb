---
page_id: javascriptallonge-recipe-const-and-lexical-scope
page_kind: recipe
summary: const and lexical scope: reusable source-backed pattern with 8 statement(s) and 4 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: const-and-lexical-scope
projection_coverage: recipe-javascriptallonge-recipe-const-and-lexical-scope@c8bfe5c855abac5538ec42f55bdb50c7
---

# const and lexical scope

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-that-constant-coffee-craving-const-and-lexical-scope-bbfe0b3d]].
- Evidence roles: decision, constraint, explanation, example.

## Applicability And Rationale

- This seems very straightforward, but alas, there are some semantics of binding names that we need to understand if we're to place const anywhere we like. _(javascriptallonge.pdf (source-range-c98ab3e6-00433))_
- It's more than a bit convoluted, but it binds ((PI) => (diameter) => diameter * PI)(3.14159265) to diameter_fn and evaluates the expression that we've elided. _(javascriptallonge.pdf (source-range-c98ab3e6-00437))_
- We can use any expression in there, and that expression can invoke diameter_fn . _(javascriptallonge.pdf (source-range-c98ab3e6-00437))_
- We know this from the chapter on closures, but even though PI is not bound when we invoke diameter_fn by evaluating diameter_fn(2) , PI is bound when we evaluated (diameter) => diameter * PI , and thus the expression diameter * PI is able to access values for PI and diameter when we evaluate diameter_fn . _(javascriptallonge.pdf (source-range-c98ab3e6-00439))_
- We can see that PI is bound in an environment surrounding (diameter) => diameter * PI , we don't need to know where diameter_fn is invoked. _(javascriptallonge.pdf (source-range-c98ab3e6-00440))_
- Although we have bound 3 to PI in the environment surrounding diameter_fn(2) , the value that counts is 3.14159265 , the value we bound to PI in the environment surrounding (diameter) ⇒ diameter * PI. _(javascriptallonge.pdf (source-range-c98ab3e6-00443))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00436)_

```
((diameter_fn) =>
// ...
)(
((PI) =>
(diameter) => diameter * PI
)(3.14159265)
)
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00438)_

```
((diameter_fn) =>
diameter_fn(2)
)(
((PI) =>
(diameter) => diameter * PI
)(3.14159265)
)
//=> 6.2831853
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00442)_

```
((diameter_fn) =>
((PI) =>
diameter_fn(2)
)(3)
)(
((PI) =>
(diameter) => diameter * PI
)(3.14159265)
)
//=> 6.2831853
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00446)_

```
((diameter_fn) => {
const PI = 3;
return diameter_fn(2)
})(
(() => {
const PI = 3.14159265;
return (diameter) => diameter * PI
})()
)
//=> 6.2831853
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-that-constant-coffee-craving-const-and-lexical-scope-bbfe0b3d]]
