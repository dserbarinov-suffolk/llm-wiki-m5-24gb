---
page_id: javascriptallonge-magic-names-and-fat-arrows
page_kind: concept
summary: magic names and fat arrows: 16 accepted assertion(s) and 4 technical atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-state-tps_0dc63a88f1c371db@f0cf0867b9cecb48783b919112267ba7
---

# magic names and fat arrows

Source: [[javascriptallonge]]

## Statements

- The magic names this and arguments have a different behaviour when you invoke a function that was defined with a fat arrow: Instead of being bound when the function is invoked, the fat arrow function always acquires the bindings for this and arguments from its enclosing scope, just like any other binding. (javascriptallonge.pdf p.75)
- For example, when this expression's inner function is defined with function , arguments[0] refers to its only argument, "inner" :. (javascriptallonge.pdf p.75)
- But if we use a fat arrow, arguments will be defined in the outer environment, the one defined with function . (javascriptallonge.pdf p.76)
- Although it seems quixotic for the two syntaxes to have different semantics, it makes sense when you consider the design goal: Fat arrow functions are designed to be very lightweight and are often used with constructs like mapping or callbacks to emulate syntax. (javascriptallonge.pdf p.76)
- To give a contrived example, this function takes a number and returns an array representing a row in a hypothetical multiplication table. (javascriptallonge.pdf p.76)
- It uses mapWith , which we discussed in Building Blocks. (javascriptallonge.pdf p.76)
- Our 'fat arrow' function (column) => column * arguments[0] doesn't bind arguments when it's invoked . (javascriptallonge.pdf p.76)
- This works just fine, because arguments[0] refers to the 3 we passed to the function row . (javascriptallonge.pdf p.76)
- If we were writing a library of functions, we would have to disambiguate the two kinds of mapping functions with special names, namespaces, or modules. (javascriptallonge.pdf p.76)
- 44 Yes, we also used the name mapWith for working with ordinary collections elsewhere. (javascriptallonge.pdf p.76)
- But for the purposes of discussing ideas, we can use the same name twice in two different contexts. (javascriptallonge.pdf p.76)
- Sometimes, a function is meant to be used as a Big-F function. (javascriptallonge.pdf p.77)
- Although this example is clearly unrealistic, there is a general design principle that deserves attention. (javascriptallonge.pdf p.77)
- It's a simple representation of an expression to be computed. (javascriptallonge.pdf p.77)
- In our example above, row is a Big-F function, but (column) => column * arguments[0] is a small-f function, it exists just to give mapWith something to apply. (javascriptallonge.pdf p.77)
- Having magic variables apply to Big-F functions but not to small-G functions makes it much easier to use small-F functions as syntax, treating them as expressions or blocks that can be passed to functions like mapWith . (javascriptallonge.pdf p.77)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

```
(function () {
return (function () { return arguments[0]; })('inner');
})('outer')
//=> "inner"
```

<a id="atom-2"></a>
**Atom:** code block

```
(function () {
return (() => arguments[0])('inner');
})('outer')
//=> "outer"
```

<a id="atom-3"></a>
**Atom:** code block

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

<a id="atom-4"></a>
**Atom:** code block

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
