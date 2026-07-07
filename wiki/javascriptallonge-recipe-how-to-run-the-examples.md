---
page_id: javascriptallonge-recipe-how-to-run-the-examples
page_kind: recipe
summary: How to run the examples: reusable source-backed pattern with 8 statement(s) and 5 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: how-to-run-the-examples
projection_coverage: recipe-javascriptallonge-recipe-how-to-run-the-examples@b24c1040dd0435162a558205d22f0019
---

# How to run the examples

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-the-golden-crema-appendices-and-afterwords-how-to-run-the-examples-b92670cf]].
- Evidence roles: decision, procedure, explanation, constraint, example.

## Applicability And Rationale

- All of the examples in this book were tested using either Google Traceur Compiler 100 , Babel 101 , or both. _(javascriptallonge.pdf (source-range-c98ab3e6-01916))_
- Traceur and Babel are both transpilers , they work by parsing ECMAScript 2015 code, then emitting valid ECMAScript-5 code that produces the same semantics. _(javascriptallonge.pdf (source-range-c98ab3e6-01916))_
- At the time this book was written, ECMAScript 2015 was not yet widely available. _(javascriptallonge.pdf (source-range-c98ab3e6-01916))_
- To see the result of your expressions, you may have to use the console in your web browser. _(javascriptallonge.pdf (source-range-c98ab3e6-01926))_
- Both tools offer an online area where you can type ECMAScript code into a web browser and see the ECMAScript-5 equivalent, and you can run the code as well. _(javascriptallonge.pdf (source-range-c98ab3e6-01926))_
- And 4 would appear in your browser's development console. _(javascriptallonge.pdf (source-range-c98ab3e6-01931))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01918)_

```
const before = (decoration) =>
(method) =>
function () {
decoration.apply(this, arguments);
return method.apply(this, arguments)
};
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01920)_

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

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01924)_

```
100https://github.com
101http://babeljs.io/
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01928)_

```
(() => 2 + 2)()
```

### Atom 5: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01930)_

```
console.log(
(() => 2 + 2)()
)
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-the-golden-crema-appendices-and-afterwords-how-to-run-the-examples-b92670cf]]
