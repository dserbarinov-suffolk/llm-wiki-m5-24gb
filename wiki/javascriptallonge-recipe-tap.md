---
page_id: javascriptallonge-recipe-tap
page_kind: recipe
summary: Tap: reusable source-backed pattern with 4 statement(s) and 3 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: tap
projection_coverage: recipe-javascriptallonge-recipe-tap@5b56beb7662be5f16ea3c75441cfa3a5
---

# Tap

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-recipes-with-basic-functions-tap-7702e150]].
- Evidence roles: decision, constraint, example.

## Applicability And Rationale

- It has some surprising applications. _(javascriptallonge.pdf (source-range-c98ab3e6-00680))_
- One is when you want to do something with a value for sideeffects, but keep the value around. _(javascriptallonge.pdf (source-range-c98ab3e6-00680))_
- tap is a traditional name borrowed from various Unix shell commands. _(javascriptallonge.pdf (source-range-c98ab3e6-00682))_
- tap can do more than just act as a debugging aid. _(javascriptallonge.pdf (source-range-c98ab3e6-00688))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00679)_

```
const K = (x) => (y) => x;
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00681)_

```
const tap = (value) =>
(fn) => (
typeof(fn) === 'function' && fn(value),
value
)
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00686)_

```
const tap = (value, fn) => {
const curried = (fn) => (
typeof(fn) === 'function' && fn(value),
value
);
return fn === undefined
? curried
: curried(fn);
}
Now we can write:
tap('espresso')((it) => {
console.log(`Our drink is '${it}'`)
});
//=> Our drink is 'espresso'
'espresso'
Or:
tap('espresso', (it) => {
console.log(`Our drink is '${it}'`)
});
//=> Our drink is 'espresso'
'espresso'
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-recipes-with-basic-functions-tap-7702e150]]
