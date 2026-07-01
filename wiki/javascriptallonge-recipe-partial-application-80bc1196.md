---
page_id: javascriptallonge-recipe-partial-application-80bc1196
page_kind: recipe
summary: Partial Application: reusable source-backed pattern with 5 statement(s) and 2 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-01
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: partial-application
projection_coverage: recipe-javascriptallonge-recipe-partial-application-80bc1196@9ee26d08ca1343bb618c44d551a6cb91
---

# Partial Application

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-recipes-with-basic-functions-partial-application-80bc1196]].
- Evidence roles: decision, constraint, procedure, structured-state, example.

## Applicability And Rationale

- These two recipes are for quickly and simply applying a single argument, either the leftmost or rightmost. _(javascriptallonge.pdf (source-range-0e12e052-00655))_
- 48 If you want to bind more than one argument, or you want to leave a 'hole' in the argument list, you will need to either use a generalized partial recipe, or you will need to repeatedly apply arguments. _(javascriptallonge.pdf (source-range-0e12e052-00655))_
- As noted above, our partial recipe allows us to create functions that are partial applications of functions that are context aware. _(javascriptallonge.pdf (source-range-0e12e052-00657))_
- We'd need a different recipe if we wish to create partial applications of object methods. _(javascriptallonge.pdf (source-range-0e12e052-00657))_
- We take it a step further, and can use gathering and spreading to allow for partial application with more than one argument: _(javascriptallonge.pdf (source-range-0e12e052-00660))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-00656)_

```
const callFirst = (fn, larg) =>
function (...rest) {
return fn.call(this, larg, ...rest);
}
const callLast = (fn, rarg) =>
function (...rest) {
return fn.call(this, ...rest, rarg);
}
const greet = (me, you) =>
`Hello, ${you}, my name is ${me}`;
const heliosSaysHello = callFirst(greet, 'Helios');
heliosSaysHello('Eartha')
//=> 'Hello, Eartha, my name is Helios'
const sayHelloToCeline = callLast(greet, 'Celine');
sayHelloToCeline('Eartha')
//=> 'Hello, Celine, my name is Eartha'
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-00661)_

```
const callLeft = (fn, ...args) =>
(...remainingArgs) =>
fn(...args, ...remainingArgs);
const callRight = (fn, ...args) =>
(...remainingArgs) =>
fn(...remainingArgs, ...args);
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-recipes-with-basic-functions-partial-application-80bc1196]]
