---
page_id: javascriptallonge-recipe-the-function-keyword-c5591d39
page_kind: recipe
summary: the function keyword: reusable source-backed pattern with 17 statement(s) and 13 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: the-function-keyword
projection_coverage: recipe-javascriptallonge-recipe-the-function-keyword-c5591d39@dc4e11f36eda2e3ddaa15fad2283256c
---

# the function keyword

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-and-also-naming-functions-the-function-keyword-c5591d39]].
- Evidence roles: decision, constraint, definition, explanation, procedure, example.

## Applicability And Rationale

- JavaScript does have a syntax for naming a function, we use the function keyword. _(javascriptallonge.pdf (source-range-c98ab3e6-00498))_
- Until ECMAScript 2015 was created, function was the usual syntax for writing functions. _(javascriptallonge.pdf (source-range-c98ab3e6-00498))_
- - Something else we're about to discuss is optional. _(javascriptallonge.pdf (source-range-c98ab3e6-00505))_
- - We have arguments in parentheses, just like fat arrow functions. _(javascriptallonge.pdf (source-range-c98ab3e6-00506))_
- - We do not have a fat arrow, we go directly to the body. _(javascriptallonge.pdf (source-range-c98ab3e6-00507))_
- - We always use a block, we cannot write function (str) str + str . _(javascriptallonge.pdf (source-range-c98ab3e6-00508))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00500)_

```
(str) => str + str
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00502)_

```
function (str) { return str + str }
```

### Atom 3: `worked-example`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00509)_

```
If we leave out the 'something optional' that comes after the function keyword, we can translate all of the fat arrow functions that we've seen into function keyword functions, e.g.
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00510)_

```
(n) => (1.618**n - -1.618**-n) / 2.236
```

### Atom 5: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00512)_

```
function (n) {
return (1.618**n - -1.618**-n) / 2.236;
}
```

### Atom 6: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00515)_

```
const repeat = function repeat (str) {
return str + str;
};
const fib = function fib (n) {
return (1.618**n - -1.618**-n) / 2.236;
};
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-and-also-naming-functions-the-function-keyword-c5591d39]]
