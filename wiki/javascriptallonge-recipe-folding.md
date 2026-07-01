---
page_id: javascriptallonge-recipe-folding
page_kind: recipe
summary: folding: reusable source-backed pattern with 2 statement(s) and 6 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-01
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: folding
projection_coverage: recipe-javascriptallonge-recipe-folding@fa8c0b5e98abfd19b1b04f5e71c4e588
---

# folding

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-composing-and-decomposing-data-self-similarity-folding-f9fb03a1]].
- Evidence roles: decision, constraint, example.

## Applicability And Rationale

- Our foldWith function is a generalization of our mapWith function. _(javascriptallonge.pdf (source-range-0e12e052-00939))_
- And to return to our first example, our version of length can be written as a fold: _(javascriptallonge.pdf (source-range-0e12e052-00943))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-00931)_

```
const sumSquares = ([first, ...rest]) => first === undefined
? 0
: first * first + sumSquares(rest);
sumSquares([1, 2, 3, 4, 5])
//=> 55
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-00936)_

```
const foldWith = (fn, terminalValue, [first, ...rest]) =>
first === undefined
? terminalValue
: fn(first, foldWith(fn, terminalValue, rest));
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-00938)_

```
foldWith((number, rest) => number * number + rest, 0, [1, 2, 3, 4, 5])
//=> 55
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-00940)_

```
const squareAll = (array) => foldWith((first, rest) => [first * first, ...rest],\
[], array);
squareAll([1, 2, 3, 4, 5])
//=> [1,4,9,16,25]
```

### Atom 5: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-00942)_

```
const mapWith = (fn, array) => foldWith((first, rest) => [fn(first), ...rest], [\
], array),
squareAll = (array) => mapWith((x) => x * x, array);
squareAll([1, 2, 3, 4, 5])
//=> [1,4,9,16,25]
```

### Atom 6: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-00944)_

```
const length = (array) => foldWith((first, rest) => 1 + rest, 0, array);
length([1, 2, 3, 4, 5])
//=> 5
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-composing-and-decomposing-data-self-similarity-folding-f9fb03a1]]
