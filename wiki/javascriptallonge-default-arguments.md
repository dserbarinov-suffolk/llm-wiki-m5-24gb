---
page_id: javascriptallonge-default-arguments
page_kind: concept
summary: default arguments: 5 accepted assertion(s) and 4 technical atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-state-tps_e117e65a8fc5fb83@800ac37f7fd9bb33eaf02696bd2aec85
---

# default arguments

Source: [[javascriptallonge]]

## Statements

- But when it calls itself, it will call factorial(5, 6) and that will not mean factorial(5, 1) . (javascriptallonge.pdf p.123)
- What we really want is this: We want to write something like factorial(6) , and have JavaScript automatically know that we really mean factorial(6, 1) . (javascriptallonge.pdf p.123)
- By writing our parameter list as (n, work = 1) => , we're stating that if a second parameter is not provided, work is to be bound to 1 . (javascriptallonge.pdf p.124)
- A default argument is concise and readable. (javascriptallonge.pdf p.124)
- Now we don't need to use two functions. (javascriptallonge.pdf p.124)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

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

<a id="atom-2"></a>
**Atom:** rule

```
But it is hideous to have to always add a 1 parameter, we'd be demanding that everyone using the factorial function know that we are using a tail-recursive implementation.
```

<a id="atom-3"></a>
**Atom:** code block

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

<a id="atom-4"></a>
**Atom:** code block

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
