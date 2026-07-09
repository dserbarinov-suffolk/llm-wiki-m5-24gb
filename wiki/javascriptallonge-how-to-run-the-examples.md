---
page_id: javascriptallonge-how-to-run-the-examples
page_kind: concept
summary: How to run the examples: 8 accepted assertion(s) and 7 technical atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-state-tps_989e8480a100fc92@976ebe5b78626e5e14cde88b141ed4d2
---

# How to run the examples

Source: [[javascriptallonge]]

## Statements

- All of the examples in this book were tested using either Google Traceur Compiler 100 , Babel 101 , or both. (javascriptallonge.pdf p.289)
- Traceur and Babel are both transpilers , they work by parsing ECMAScript 2015 code, then emitting valid ECMAScript-5 code that produces the same semantics. (javascriptallonge.pdf p.289)
- At the time this book was written, ECMAScript 2015 was not yet widely available. (javascriptallonge.pdf p.289)
- To see the result of your expressions, you may have to use the console in your web browser. (javascriptallonge.pdf p.290)
- Both tools offer an online area where you can type ECMAScript code into a web browser and see the ECMAScript-5 equivalent, and you can run the code as well. (javascriptallonge.pdf p.290)
- And 4 would appear in your browser's development console. (javascriptallonge.pdf p.290)
- The care and feeding of node and npm are beyond the scope of this book, but both tools offer clear instructions for those who have already installed node . (javascriptallonge.pdf p.290)
- You can also install the transpilers on your development system and use them with Node 102 on the command line 103 . (javascriptallonge.pdf p.290)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

```
const before = (decoration) =>
(method) =>
function () {
decoration.apply(this, arguments);
return method.apply(this, arguments)
};
```

<a id="atom-2"></a>
**Atom:** code block

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

<a id="atom-3"></a>
**Atom:** code block

```
100https://github.com
101http://babeljs.io/
```

<a id="atom-4"></a>
**Atom:** code block

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

<a id="atom-5"></a>
**Atom:** code block

```
(() => 2 + 2)()
```

<a id="atom-6"></a>
**Atom:** code block

```
console.log(
(() => 2 + 2)()
)
```

<a id="atom-7"></a>
**Atom:** table

```text
102 http://nodejs.org/
103 https://en.wikipedia.org/wiki/REPL
```
