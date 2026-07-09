---
page_id: javascriptallonge-gathering
page_kind: concept
summary: gathering: 4 accepted assertion(s) and 4 technical atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-state-tps_3bf979d4be9bcbcc@1e808ea7d9f6a2cea8d90a8da2aa1ccf
---

# gathering

Source: [[javascriptallonge]]

## Statements

- Here is the most common pattern: Extracting the head and gathering everything but the head from an array:. (javascriptallonge.pdf p.104)
- Sometimes we need to extract arrays from arrays. (javascriptallonge.pdf p.104)
- car and cdr 57 are archaic terms that go back to an implementation of Lisp running on the IBM 704 computer. (javascriptallonge.pdf p.104)
- notation does not provide a universal patten-matching capability. (javascriptallonge.pdf p.104)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

```
const [car, ...cdr] = [1, 2, 3, 4, 5];
car
//=> 1
cdr
//=> [2, 3, 4, 5]
```

<a id="atom-2"></a>
**Atom:** table

```text
57 https://en.wikipedia.org/wiki/CAR_and_CDR
58 Kyle Simpson is the author of You Don't Know JS, available here
```

<a id="atom-3"></a>
**Atom:** code block

```
const [...butLast, last] = [1, 2, 3, 4, 5];
//=> ERROR
const [first, ..., last] = [1, 2, 3, 4, 5];
//=> ERROR
Now, when we introduced destructuring, we saw that it is kind-of-sort-of the reverse of array literals.
So if
const wrapped = [something];
Then:
const [unwrapped] = something;
What is the reverse of gathering? We know that:
const [car, ...cdr] = [1, 2, 3, 4, 5];
What is the reverse? It would be:
const cons = [car, ...cdr];
Let’s try it:
const oneTwoThree = ["one", "two", "three"];
```

<a id="atom-4"></a>
**Atom:** code block

```
Let’s try it:
const oneTwoThree = ["one", "two", "
["zero", ...oneTwoThree]
//=> ["zero","one","two","three"]
```
