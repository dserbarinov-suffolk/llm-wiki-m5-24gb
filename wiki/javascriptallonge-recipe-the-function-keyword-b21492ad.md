---
page_id: javascriptallonge-recipe-the-function-keyword-b21492ad
page_kind: recipe
summary: the function keyword: reusable source-backed pattern with 6 statement(s) and 4 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-01
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: the-function-keyword
projection_coverage: recipe-javascriptallonge-recipe-the-function-keyword-b21492ad@b669a47cb90d97a11c52fcc77cb1a44f
---

# the function keyword

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-and-also-magic-names-the-function-keyword-b21492ad]].
- Evidence roles: decision, procedure, constraint, example, structured-state.

## Applicability And Rationale

- There are two separate rules for these 'magic' names, one for when you invoke a function using the function keyword, and another for functions defined with 'fat arrows.' We'll begin with how things work for functions defined with the function keyword. _(javascriptallonge.pdf (source-range-0e12e052-00602))_
- The first magic name is this , and it is bound to something called the function's context. _(javascriptallonge.pdf (source-range-0e12e052-00603))_
- The second magic name is very interesting, it's called arguments , and the most interesting thing about it is that it contains a list of arguments passed to a function: _(javascriptallonge.pdf (source-range-0e12e052-00603))_
- arguments always contains all of the arguments passed to a function, regardless of how many are declared. _(javascriptallonge.pdf (source-range-0e12e052-00607))_
- We'll see it used in many of the recipes, starting off with partial application and ellipses. _(javascriptallonge.pdf (source-range-0e12e052-00612))_
- The most common use of the arguments binding is to build functions that can take a variable number of arguments. _(javascriptallonge.pdf (source-range-0e12e052-00612))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-00604)_

```
const plus = function (a, b) {
return arguments[0] + arguments[1];
}
plus(2,3)
//=> 5
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-00606)_

```
const args = function (a, b) {
return arguments;
}
args(2,3)
//=> { '0': 2, '1': 3 }
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-00609)_

```
const plus = function () {
return arguments[0] + arguments[1];
}
plus(2,3)
//=> 5
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-00611)_

```
const howMany = function () {
return arguments['length'];
}
howMany()
//=> 0
howMany('hello')
//=> 1
howMany('sharks', 'are', 'apex', 'predators')
//=> 4
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-and-also-magic-names-the-function-keyword-b21492ad]]
