---
page_id: javascriptallonge-recipe-default-arguments
page_kind: recipe
summary: default arguments: reusable source-backed pattern with 5 statement(s) and 3 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: default-arguments
projection_coverage: recipe-javascriptallonge-recipe-default-arguments@3917efb117fedc59e96dd5f0b55b9e4c
---

# default arguments

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-composing-and-decomposing-data-default-arguments-363804ac]].
- Evidence roles: decision, example, structured-state.

## Applicability And Rationale

- But when it calls itself, it will call factorial(5, 6) and that will not mean factorial(5, 1) . _(javascriptallonge.pdf (source-range-c98ab3e6-00985))_
- What we really want is this: We want to write something like factorial(6) , and have JavaScript automatically know that we really mean factorial(6, 1) . _(javascriptallonge.pdf (source-range-c98ab3e6-00985))_
- By writing our parameter list as (n, work = 1) => , we're stating that if a second parameter is not provided, work is to be bound to 1 . _(javascriptallonge.pdf (source-range-c98ab3e6-00988))_
- A default argument is concise and readable. _(javascriptallonge.pdf (source-range-c98ab3e6-00990))_
- Now we don't need to use two functions. _(javascriptallonge.pdf (source-range-c98ab3e6-00990))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00983)_

```
const factorial = (n, work) =>
n === 1
? work
: factorial(n - 1, n * work);
factorial(1, 1)
//=> 1
factorial(5, 1)
//=> 120
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00987)_

```
const factorial = (n, work = 1) =>
n === 1
? work
: factorial(n - 1, n * work);
factorial(1)
//=> 1
factorial(6)
//=> 720
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00989)_

```
const length = ([first, ...rest], numberToBeAdded = 0) =>
first === undefined
? numberToBeAdded
: length(rest, 1 + numberToBeAdded)
length(["foo", "bar", "baz"])
//=> 3
const mapWith = (fn, [first, ...rest], prepend = []) =>
first === undefined
? prepend
: mapWith(fn, rest, [...prepend, fn(first)]);
mapWith((x) => x * x, [1, 2, 3, 4, 5])
//=> [1,4,9,16,25]
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-composing-and-decomposing-data-default-arguments-363804ac]]
