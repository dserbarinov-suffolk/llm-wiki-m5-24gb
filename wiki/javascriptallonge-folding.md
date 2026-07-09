---
page_id: javascriptallonge-folding
page_kind: concept
summary: topic-concept: 10 supported fragment(s) and 1 related link(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: page-projection-pgp_e4b1a71d07903b78@69361ad51a5121715304ea3a6440c092
---

# folding

Source: [[javascriptallonge]]

## Statements

- Our foldWith function is a generalization of our mapWith function. (javascriptallonge.pdf p.115)
- And to return to our first example, our version of length can be written as a fold:. (javascriptallonge.pdf p.116)

## Rules

- And to return to our first example, our version of length can be written as a fold:. (javascriptallonge.pdf p.116)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

```
const sumSquares = ([first, ...rest]) => first === undefined
? 0
: first * first + sumSquares(rest);
sumSquares([1, 2, 3, 4, 5])
//=> 55
```

<a id="atom-2"></a>
**Atom:** code block

```
const foldWith = (fn, terminalValue, [first, ...rest]) =>
first === undefined
? terminalValue
: fn(first, foldWith(fn, terminalValue, rest));
```

<a id="atom-3"></a>
**Atom:** code block

```
foldWith((number, rest) => number * number + rest, 0, [1, 2, 3, 4, 5])
//=> 55
```

<a id="atom-4"></a>
**Atom:** code block

```
const squareAll = (array) => foldWith((first, rest) => [first * first, ...rest],\
[], array);
squareAll([1, 2, 3, 4, 5])
//=> [1,4,9,16,25]
```

<a id="atom-5"></a>
**Atom:** code block

```
const mapWith = (fn, array) => foldWith((first, rest) => [fn(first), ...rest], [\
], array),
squareAll = (array) => mapWith((x) => x * x, array);
squareAll([1, 2, 3, 4, 5])
//=> [1,4,9,16,25]
```

<a id="atom-6"></a>
**Atom:** code block

```
const length = (array) => foldWith((first, rest) => 1 + rest, 0, array);
length([1, 2, 3, 4, 5])
//=> 5
```


## Related pages

- [[javascriptallonge-mapping]] - contextualizes: source-supported topic dependency
