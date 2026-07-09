---
page_id: javascriptallonge-revisiting-linked-lists
page_kind: concept
summary: revisiting linked lists: 12 accepted assertion(s) and 6 technical atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-state-tps_55c1a51c7d02da67@852e8b272f9b39eca9f7c030cf73ec5d
---

# revisiting linked lists

Source: [[javascriptallonge]]

## Statements

- But now that we've looked at objects, we can use an object instead of a two-element array. (javascriptallonge.pdf p.137)
- In essence, this simple implementation used functions to create an abstraction with named elements. (javascriptallonge.pdf p.137)
- As we saw above, and discussed in Garbage, Garbage Everywhere, it is fast to iterate forward through a linked list. (javascriptallonge.pdf p.138)
- The problem here is that linked lists are constructed back-to-front, but we iterate over them frontto-back. (javascriptallonge.pdf p.138)
- So to copy a list, we have to save all the bits on the call stack and then construct the list from back-to-front as all the recursive calls return. (javascriptallonge.pdf p.138)
- We could follow the strategy of delaying the work. (javascriptallonge.pdf p.138)
- We have unwittingly reversed the list. (javascriptallonge.pdf p.139)
- This makes sense, if lists are constructed from back to front, and we make a linked list out of items as we iterate through it, we're going to get a backwards copy of the list. (javascriptallonge.pdf p.139)
- Likewise, it takes twice as much memory, because it constructs a reverse of the desired result before throwing it away. (javascriptallonge.pdf p.140)
- Mind you, this is still much, much faster than making partial copies of arrays. (javascriptallonge.pdf p.140)
- For a list of length n , wecreated n superfluous nodes and copied n superfluous values. (javascriptallonge.pdf p.140)
- Whereas our naïve array algorithm created 2 n superfluous arrays and copied n 2 superfluous values. (javascriptallonge.pdf p.140)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

```
const cons = (a, d) => [a, d],
car
= ([a, d]) => a,
cdr
= ([a, d]) => d;
```

<a id="atom-2"></a>
**Atom:** code block

```
In that case, a linked list of the numbers 1, 2, and 3 will look like this: { first: 1, rest: { first:
2, rest: { first: 3, rest: EMPTY } } }.
We can then perform the equivalent of [first, ...rest] with direct property accessors:
```

<a id="atom-3"></a>
**Atom:** code block

```
const EMPTY = {};
const OneTwoThree = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY \
} } };
OneTwoThree.first
//=> 1
OneTwoThree.rest
//=> {"first":2,"rest":{"first":3,"rest":{}}}
OneTwoThree.rest.rest.first
//=> 3
Taking the length of a linked list is easy:
const length = (node, delayed = 0) =>
node === EMPTY
? delayed
: length(node.rest, delayed + 1);
length(OneTwoThree)
//=> 3
```

<a id="atom-4"></a>
**Atom:** code block

```
const slowcopy = (node) =>
node === EMPTY
? EMPTY
: { first: node.first, rest: slowcopy(node.rest)};
slowcopy(OneTwoThree)
//=> {"first":1,"rest":{"first":2,"rest":{"first":3,"rest":{}}}}
```

<a id="atom-5"></a>
**Atom:** code block

```
const copy2 = (node, delayed = EMPTY) =>
node === EMPTY
? delayed
: copy2(node.rest, { first: node.first, rest: delayed });
copy2(OneTwoThree)
//=> {"first":3,"rest":{"first":2,"rest":{"first":1,"rest":{}}}}
```

<a id="atom-6"></a>
**Atom:** code block

```
const reverse = (node, delayed = EMPTY) =>
node === EMPTY
? delayed
: reverse(node.rest, { first: node.first, rest: delayed });
And now, we can make a reversing map:
const reverseMapWith = (fn, node, delayed = EMPTY) =>
node === EMPTY
? delayed
: reverseMapWith(fn, node.rest, { first: fn(node.first), rest: delayed });
reverseMapWith((x) => x * x, OneTwoThree)
//=> {"first":9,"rest":{"first":4,"rest":{"first":1,"rest":{}}}}
And a regular mapWith follows:
const reverse = (node, delayed = EMPTY) =>
node === EMPTY
? delayed
: reverse(node.rest, { first: node.first, rest: delayed });
const mapWith = (fn, node, delayed = EMPTY) =>
node === EMPTY
? reverse(delayed)
: mapWith(fn, node.rest, { first: fn(node.first), rest: delayed });
mapWith((x) => x * x, OneTwoThree)
//=> {"first":1,"rest":{"first":4,"rest":{"first":9,"rest":{}}}}
```
