---
page_id: javascriptallonge-evaluate
page_kind: concept
summary: Evaluate: 10 statement(s) and 2 atom(s) from raw/javascriptallonge.pdf.
page_family: broad-topic
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-evaluate@fee9c4e3f2a962c509c1583e61a862df
---

# Evaluate

What [[javascriptallonge]] covers about evaluate:

## Statements

### Prelude: Values and Expressions over Coffee / values are expressions / reference types

- They look the same, but if you examine them with === , you see that they are different. Every time you evaluate an expression (including typing something in) to create an array, you're creating a new, distinct value even if it appears to be the same as some other array value. As we'll see, this is true of many other kinds of values, including functions , the main subject of this book. _(javascriptallonge.pdf (source-range-c98ab3e6-00134))_

### The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions and identities

- Like arrays, every time you evaluate an expression to produce a function, you get a new function that is not identical to any other function, even if you use the same expression to generate it. 'Function' is a reference type. _(javascriptallonge.pdf (source-range-c98ab3e6-00173))_

### Or even: / the simplest possible block / undefined

- No matter how you evaluate undefined , you get an identical value back. undefined is a value that means 'I don't have a value.' But it's still a value :-) _(javascriptallonge.pdf (source-range-c98ab3e6-00216))_

### Or even: / back on the block

- But no matter how we arrange them, a block with one or more expressions still evaluates to undefined : _(javascriptallonge.pdf (source-range-c98ab3e6-00237))_

### And also: / Closures and Scope / it's always the environment

- The first function is the result of currying a the second function. Calling a curried function with only some of its arguments is sometimes called partial application b . Some programming languages automatically curry and partially evaluate functions without the need to manually nest them. _(javascriptallonge.pdf (source-range-c98ab3e6-00351))_

### And also: / Summary / Functions

- Block bodies evaluate to whatever is returned with the return keyword, or to undefined . _(javascriptallonge.pdf (source-range-c98ab3e6-00629))_

### Picking the Bean: Choice and Truthiness / truthiness and the ternary operator

- JavaScript inherited an operator from the C family of languages, the ternary operator. It's the only operator that takes three arguments. It looks like this: first ? second : third . It evaluates first , and if first is 'truthy', it evaluates second and that is its value. If first is not truthy, it evaluates third and that is its value. _(javascriptallonge.pdf (source-range-c98ab3e6-00750))_

- Wecertainly don't want JavaScript trying to evaluate deleteRecord(currentRecord) unless isAuthorized(currentUser) returns true . _(javascriptallonge.pdf (source-range-c98ab3e6-00756))_

### A Warm Cup: Basic Strings and Quasi-Literals / evaluation time

- JavaScript evaluates the quasi-literal when the function is invoked and the quasi-literal inside the function's body is evaluated. Thus, name is not bound to "Harry" , it is bound to 'Arthur Dent' , the value of the parameter when the function is invoked. _(javascriptallonge.pdf (source-range-c98ab3e6-01491))_

### Served by the Pot: Collections / Iteration and Iterables / iterables

- The expression Symbol.iterator evaluates to a special symbol representing the name of the method that objects should use if they return an iterator object. _(javascriptallonge.pdf (source-range-c98ab3e6-01527))_


## Technical atoms

### Technical frame 1: Or even: / the simplest possible block / undefined

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00216))_

> No matter how you evaluate undefined , you get an identical value back. undefined is a value that means 'I don't have a value.' But it's still a value :-)

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00215))_

<a id="atom-technical-atom-68dc26441ffd855a"></a>
```
undefined === undefined
//=> true
(() => {})() === (() => {})()
//=> true
(() => {})() === undefined
//=> true
```


## Related pages

### Shared technical atoms

- [[javascriptallonge-programming]] - shared statements and technical atoms: Programming shares source evidence from And also: / Closures and Scope / it's always the environment: The first function is the result of currying a the second function. Calling a curried function with only some of its arguments is sometimes called partial applicatio ... [truncated]; Programming shares technical record from And also: / Closures and Scope / it's always the environment: (x, y, z) => x + y + z (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-scope]] - shared technical atoms: Scope shares technical record from And also: / Closures and Scope / it's always the environment: (x, y, z) => x + y + z (1 shared atom(s))

### Shared claims

- [[javascriptallonge-expression]] - shared statements: Expression shares source evidence from Prelude: Values and Expressions over Coffee / values are expressions / reference types: They look the same, but if you examine them with === , you see that they are different. Every time you evaluate an expression (including typing something in) to crea ... [truncated] (4 shared statement(s))
- [[javascriptallonge-javascript]] - shared statements: Javascript shares source evidence from Picking the Bean: Choice and Truthiness / truthiness and the ternary operator: Wecertainly don't want JavaScript trying to evaluate deleteRecord(currentRecord) unless isAuthorized(currentUser) returns true . (2 shared statement(s))
- [[javascriptallonge-body]] - shared statements: Body shares source evidence from And also: / Summary / Functions: Block bodies evaluate to whatever is returned with the return keyword, or to undefined . (1 shared statement(s))
- [[javascriptallonge-iterator]] - shared statements: Iterator shares source evidence from Served by the Pot: Collections / Iteration and Iterables / iterables: The expression Symbol.iterator evaluates to a special symbol representing the name of the method that objects should use if they return an iterator object. (1 shared statement(s))
- [[javascriptallonge-literal]] - shared statements: Literal shares source evidence from A Warm Cup: Basic Strings and Quasi-Literals / evaluation time: JavaScript evaluates the quasi-literal when the function is invoked and the quasi-literal inside the function's body is evaluated. Thus, name is not bound to "Harry" ... [truncated] (1 shared statement(s))
- [[javascriptallonge-method]] - shared statements: Method shares source evidence from Served by the Pot: Collections / Iteration and Iterables / iterables: The expression Symbol.iterator evaluates to a special symbol representing the name of the method that objects should use if they return an iterator object. (1 shared statement(s))
- [[javascriptallonge-object]] - shared statements: Object shares source evidence from Served by the Pot: Collections / Iteration and Iterables / iterables: The expression Symbol.iterator evaluates to a special symbol representing the name of the method that objects should use if they return an iterator object. (1 shared statement(s))
- [[javascriptallonge-quasi]] - shared statements: Quasi shares source evidence from A Warm Cup: Basic Strings and Quasi-Literals / evaluation time: JavaScript evaluates the quasi-literal when the function is invoked and the quasi-literal inside the function's body is evaluated. Thus, name is not bound to "Harry" ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
