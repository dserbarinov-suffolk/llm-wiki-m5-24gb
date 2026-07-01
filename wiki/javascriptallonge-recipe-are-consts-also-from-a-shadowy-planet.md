---
page_id: javascriptallonge-recipe-are-consts-also-from-a-shadowy-planet
page_kind: recipe
summary: are consts also from a shadowy planet?: reusable source-backed pattern with 16 statement(s) and 10 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-01
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: are-consts-also-from-a-shadowy-planet
projection_coverage: recipe-javascriptallonge-recipe-are-consts-also-from-a-shadowy-planet@ecc0213b797f44962b370bcf503b8c2e
---

# are consts also from a shadowy planet?

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-and-also-that-constant-coffee-craving-are-consts-also-from-a-shadowy-planet-f4ab49ce]].
- Evidence roles: decision, constraint, explanation, example, structured-state.

## Applicability And Rationale

- Parameters are declared when we create functions, so it makes sense that parameters are bound to environments created when we invoke functions. _(javascriptallonge.pdf (source-range-0e12e052-00459))_
- They are looked up in the environment where they are declared. _(javascriptallonge.pdf (source-range-0e12e052-00459))_
- We just saw that values bound with const use lexical scope, just like values bound with parameters. _(javascriptallonge.pdf (source-range-0e12e052-00459))_
- But const statements can appear inside blocks, and we saw that blocks can appear inside of other blocks, including function bodies. _(javascriptallonge.pdf (source-range-0e12e052-00460))_
- But instead of binding two different variables to the same name in two different places, we'll bind two different values to the same name, but one environment will be completely enclosed by the other. _(javascriptallonge.pdf (source-range-0e12e052-00461))_
- And we can see that our diameter * PI expression uses the binding for PI in the closest parent environment. _(javascriptallonge.pdf (source-range-0e12e052-00468))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-00463)_

```
((PI) =>
(diameter) => diameter * PI
)(3.14159265)
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-00465)_

```
((PI) =>
((PI) =>
(diameter) => diameter * PI
)(3.14159265)
)(3)
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-00467)_

```
((PI) =>
((PI) =>
(diameter) => diameter * PI
)(3.14159265)
)(3)(2)
//=> 6.2831853
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-00469)_

```
((PI) => {
((PI) => {})(3);
return (diameter) => diameter * PI;
})(3.14159265)
```

### Atom 5: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-00471)_

```
((PI) => {
((PI) => {})(3);
return (diameter) => diameter * PI;
})(3.14159265)(2)
//=> 6.2831853
```

### Atom 6: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-00474)_

```
((diameter) => {
const PI = 3.14159265;
(() => {
const PI = 3;
})();
return diameter * PI;
})(2)
//=> 6.2831853
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-and-also-that-constant-coffee-craving-are-consts-also-from-a-shadowy-planet-f4ab49ce]]
