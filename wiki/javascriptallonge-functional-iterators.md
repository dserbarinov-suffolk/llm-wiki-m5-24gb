---
page_id: javascriptallonge-functional-iterators
page_kind: concept
summary: topic-concept: 15 supported fragment(s) and 2 related link(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: page-projection-pgp_91a74968d6f73b3c@3d592e7d4f75a08144b00d95f678e42f
---

# Functional Iterators

Source: [[javascriptallonge]]

## Statements

- But it still relies on foldArrayWith , so it can only sum arrays. (javascriptallonge.pdf p.167)
- The nice thing about this is that the definition for arraySum mostly concerns itself with summing, and not with traversing over a collection of data. (javascriptallonge.pdf p.167)
- Perhaps we could extract both of those things. (javascriptallonge.pdf p.167)
- Well, we call arraySum with an array, and it has baked into it a method for traversing the array. (javascriptallonge.pdf p.167)
- What we've done is turn an array into a function that folds an array with const foldArray = (array) => callRight(foldArrayWith, array); . (javascriptallonge.pdf p.168)
- The sumFoldable function doesn't care what kind of data structure we have , as long as it's foldable. (javascriptallonge.pdf p.168)
- We've found another way to express the principle of separating traversing a data structure from the operation we want to perform on that data structure, we've completely separated the knowledge of how to sum from the knowledge of how to fold an array or tree (or anything else, really). (javascriptallonge.pdf p.168)

## Rules

- But it still relies on foldArrayWith , so it can only sum arrays. (javascriptallonge.pdf p.167)
- Perhaps we could extract both of those things. (javascriptallonge.pdf p.167)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

```
const arraySum = ([first, ...rest], accumulator = 0) =>
first === undefined
? accumulator
: arraySum(rest, first + accumulator)
arraySum([1, 4, 9, 16, 25])
//=> 55
```

<a id="atom-2"></a>
**Atom:** code block

```
const callLeft = (fn, ...args) =>
(...remainingArgs) =>
fn(...args, ...remainingArgs);
const foldArrayWith = (fn, terminalValue, [first, ...rest]) =>
first === undefined
? terminalValue
: fn(first, foldArrayWith(fn, terminalValue, rest));
const arraySum = callLeft(foldArrayWith, (a, b) => a + b, 0);
arraySum([1, 4, 9, 16, 25])
//=> 55
```

<a id="atom-3"></a>
**Atom:** code block

```
const callRight = (fn, ...args) =>
(...remainingArgs) =>
fn(...remainingArgs, ...args);
const foldArrayWith = (fn, terminalValue, [first, ...rest]) =>
first === undefined
? terminalValue
: fn(first, foldArrayWith(fn, terminalValue, rest));
const foldArray = (array) => callRight(foldArrayWith, array);
const sumFoldable = (folder) => folder((a, b) => a + b, 0);
sumFoldable(foldArray([1, 4, 9, 16, 25]))
//=> 55
```

<a id="atom-4"></a>
**Atom:** code block

```
const callRight = (fn, ...args) =>
(...remainingArgs) =>
fn(...remainingArgs, ...args);
const foldTreeWith = (fn, terminalValue, [first, ...rest]) =>
first === undefined
? terminalValue
: Array.isArray(first)
? fn(foldTreeWith(fn, terminalValue, first), foldTreeWith(fn, terminalValu\
e, rest))
: fn(first, foldTreeWith(fn, terminalValue, rest));
const foldTree = (tree) => callRight(foldTreeWith, tree);
const sumFoldable = (folder) => folder((a, b) => a + b, 0);
sumFoldable(foldTree([1, [4, [9, 16]], 25]))
//=> 55
```


## Related pages

- [[javascriptallonge-tortoises-hares-and-teleporting-turtles]] - contextualizes: source-supported topic dependency
- [[javascriptallonge-making-data-out-of-functions]] - contextualizes: source-supported topic dependency
