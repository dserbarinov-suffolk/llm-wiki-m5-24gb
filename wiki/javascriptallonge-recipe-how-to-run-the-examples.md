---
page_id: javascriptallonge-recipe-how-to-run-the-examples
page_kind: recipe
summary: How to run the examples: reusable source-backed pattern with 8 statement(s) and 6 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: how-to-run-the-examples
projection_coverage: recipe-javascriptallonge-recipe-how-to-run-the-examples@c970f987e4c1e21b7a951c7f2c9860d1
---

# How to run the examples

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-the-golden-crema-appendices-and-afterwords-how-to-run-the-examples-9fa9748b]].
- Evidence roles: decision, procedure, explanation, constraint, example, technical-atom, structured-state.

## Applicability And Rationale

- At the time this book was written, ECMAScript 2015 was not yet widely available. _(javascriptallonge.pdf (source-range-c98ab3e6-01961))_
- Traceur and Babel are both transpilers , they work by parsing ECMAScript 2015 code, then emitting valid ECMAScript-5 code that produces the same semantics. _(javascriptallonge.pdf (source-range-c98ab3e6-01961))_
- All of the examples in this book were tested using either Google Traceur Compiler 100 , Babel 101 , or both. _(javascriptallonge.pdf (source-range-c98ab3e6-01961))_
- To see the result of your expressions, you may have to use the console in your web browser. _(javascriptallonge.pdf (source-range-c98ab3e6-01972))_
- Both tools offer an online area where you can type ECMAScript code into a web browser and see the ECMAScript-5 equivalent, and you can run the code as well. _(javascriptallonge.pdf (source-range-c98ab3e6-01972))_
- And 4 would appear in your browser's development console. _(javascriptallonge.pdf (source-range-c98ab3e6-01977))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01963)_

```
const before = (decoration) =>
(method) =>
function () {
decoration.apply(this, arguments);
return method.apply(this, arguments)
};
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01965)_

```
"use strict"
var before = function (decoration) {
return function (method) {
return function () {
decoration.apply(this, arguments);
return method.apply(this, arguments);
};
};
};
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01970)_

```
100https://github.com
101http://babeljs.io/
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01971)_

```
const before = (decoration) =>
(method) =>
function (...args) {
decoration.apply(this, args);
return method.apply(this, args)
};
And it would be “transpiled” into:
var before = function (decoration) {
return function (method) {
return function () {
for (let _len = arguments.length, args = Array(_len), _key = 0; _key < _le\
n; _key++) {
args[_key] = arguments[_key];
}
decoration.apply(this, args);
return method.apply(this, args);
};
};
};
```

### Atom 5: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01974)_

```
(() => 2 + 2)()
```

### Atom 6: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01976)_

```
console.log(
(() => 2 + 2)()
)
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-the-golden-crema-appendices-and-afterwords-how-to-run-the-examples-9fa9748b]]
