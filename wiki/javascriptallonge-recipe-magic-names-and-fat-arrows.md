---
page_id: javascriptallonge-recipe-magic-names-and-fat-arrows
page_kind: recipe
summary: magic names and fat arrows: reusable source-backed pattern with 17 statement(s) and 4 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-01
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: magic-names-and-fat-arrows
projection_coverage: recipe-javascriptallonge-recipe-magic-names-and-fat-arrows@e934ce576f62f145760b605285b50255
---

# magic names and fat arrows

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-and-also-magic-names-magic-names-and-fat-arrows-0831b561]].
- Evidence roles: decision, definition, explanation, procedure, constraint, example.

## Applicability And Rationale

- The magic names this and arguments have a different behaviour when you invoke a function that was defined with a fat arrow: Instead of being bound when the function is invoked, the fat arrow function always acquires the bindings for this and arguments from its enclosing scope, just like any other binding. _(javascriptallonge.pdf (source-range-0e12e052-00614))_
- For example, when this expression's inner function is defined with function , arguments[0] refers to its only argument, "inner" : _(javascriptallonge.pdf (source-range-0e12e052-00615))_
- But if we use a fat arrow, arguments will be defined in the outer environment, the one defined with function . _(javascriptallonge.pdf (source-range-0e12e052-00617))_
- Although it seems quixotic for the two syntaxes to have different semantics, it makes sense when you consider the design goal: Fat arrow functions are designed to be very lightweight and are often used with constructs like mapping or callbacks to emulate syntax. _(javascriptallonge.pdf (source-range-0e12e052-00619))_
- It uses mapWith , which we discussed in Building Blocks. _(javascriptallonge.pdf (source-range-0e12e052-00620))_
- To give a contrived example, this function takes a number and returns an array representing a row in a hypothetical multiplication table. _(javascriptallonge.pdf (source-range-0e12e052-00620))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-00616)_

```
(function () {
return (function () { return arguments[0]; })('inner');
})('outer')
//=> "inner"
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-00618)_

```
(function () {
return (() => arguments[0])('inner');
})('outer')
//=> "outer"
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-00621)_

```
const row = function () {
return mapWith(
(column) => column * arguments[0],
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
)
}
row(3)
//=> [3,6,9,12,15,18,21,24,27,30,33,36]
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-00624)_

```
const row = function () {
return mapWith(
function (column) { return column * arguments[0] },
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
)
}
row(3)
//=> [1,4,9,16,25,36,49,64,81,100,121,144]
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-and-also-magic-names-magic-names-and-fat-arrows-0831b561]]
