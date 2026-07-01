---
page_id: javascriptallonge-recipe-var
page_kind: recipe
summary: var: reusable source-backed pattern with 7 statement(s) and 6 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-01
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: var
projection_coverage: recipe-javascriptallonge-recipe-var@45fbb972e83e0bb7168b8a32e0a4e102
---

# var

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-reassignment-mixing-let-and-const-var-9446c873]].
- Evidence roles: decision, constraint, explanation, procedure, example.

## Applicability And Rationale

- JavaScript has one more way to bind a name to a value, var . _(javascriptallonge.pdf (source-range-0e12e052-01182))_
- First, var is not block scoped, it's function scoped, just like function declarations: _(javascriptallonge.pdf (source-range-0e12e052-01186))_
- Declaring age twice does not cause an error(!), and the inner declaration does not shadow the outer declaration. _(javascriptallonge.pdf (source-range-0e12e052-01188))_
- But, again, it is unwise to expect consistency. _(javascriptallonge.pdf (source-range-0e12e052-01189))_
- A function declaration can appear anywhere within a function, but the declaration and the definition are hoisted. _(javascriptallonge.pdf (source-range-0e12e052-01189))_
- But it's not like const and let in that it's function scoped, not block scoped. _(javascriptallonge.pdf (source-range-0e12e052-01195))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-01183)_

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

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-01185)_

```
return n * factorial2(x);
}
}
factorial2(5)
//=> 120
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-01187)_

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

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-01190)_

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

### Atom 5: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-01192)_

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

### Atom 6: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-01194)_

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

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-reassignment-mixing-let-and-const-var-9446c873]]
