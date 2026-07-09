---
page_id: javascriptallonge-var
page_kind: concept
summary: topic-concept: 15 supported fragment(s) and 0 related link(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: page-projection-pgp_397e268523c0144c@2dfb27b7e4f2bcf6cc4ed0ad2b68853a
---

# var

Source: [[javascriptallonge]]

## Statements

- JavaScript has one more way to bind a name to a value, var . (javascriptallonge.pdf p.151)
- First, var is not block scoped, it's function scoped, just like function declarations:. (javascriptallonge.pdf p.152)
- Declaring age twice does not cause an error(!), and the inner declaration does not shadow the outer declaration. (javascriptallonge.pdf p.152)
- But, again, it is unwise to expect consistency. (javascriptallonge.pdf p.152)
- A function declaration can appear anywhere within a function, but the declaration and the definition are hoisted. (javascriptallonge.pdf p.152)
- In that way, var is a little like const and let , we should always declare and bind names before using them. (javascriptallonge.pdf p.154)
- But it's not like const and let in that it's function scoped , not block scoped. (javascriptallonge.pdf p.154)

## Rules

- A function declaration can appear anywhere within a function, but the declaration and the definition are hoisted. (javascriptallonge.pdf p.152)
- In that way, var is a little like const and let , we should always declare and bind names before using them. (javascriptallonge.pdf p.154)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

```
const factorial = (n) => {
let x = n;
if (x === 1) {
return 1;
}
else {
--x;
return n * factorial(x);
}
}
factorial(5)
//=> 120
const factorial2 = (n) => {
var x = n;
if (x === 1) {
return 1;
}
else {
--x;
```

<a id="atom-2"></a>
**Atom:** code block

```
return n * factorial2(x);
}
}
factorial2(5)
//=> 120
```

<a id="atom-3"></a>
**Atom:** code block

```
(() => {
var age = 49;
if (true) {
var age = 50;
}
return age;
})()
//=> 50
```

<a id="atom-4"></a>
**Atom:** code block

```
const factorial = (n) => {
return innerFactorial(n, 1);
function innerFactorial (x, y) {
if (x == 1) {
return y;
}
else {
return innerFactorial(x-1, x * y);
}
}
}
factorial(4)
//=> 24
```

<a id="atom-5"></a>
**Atom:** code block

```
const factorial = (n) => {
let innerFactorial = function innerFactorial (x, y) {
if (x == 1) {
return y;
}
else {
return innerFactorial(x-1, x * y);
}
}
return innerFactorial(n, 1);
}
JavaScript hoists the let and the assignment. But not so with var:
const factorial = (n) => {
return innerFactorial(n, 1);
var innerFactorial = function innerFactorial (x, y) {
if (x == 1) {
return y;
}
else {
return innerFactorial(x-1, x * y);
}
}
}
factorial(4)
//=> undefined is not a function (evaluating 'innerFactorial(n, 1)')
```

<a id="atom-6"></a>
**Atom:** code block

```
const factorial = (n) => {
let innerFactorial = undefined;
return innerFactorial(n, 1);
innerFactorial = function innerFactorial (x, y) {
if (x == 1) {
return y;
}
else {
return innerFactorial(x-1, x * y);
}
}
}
factorial(4)
//=> undefined is not a function (evaluating 'innerFactorial(n, 1)')
```
