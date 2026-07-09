---
page_id: javascriptallonge-making-data-out-of-functions
page_kind: concept
summary: Making Data Out Of Functions: 8 accepted assertion(s) and 3 technical atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-state-tps_a0f7927f7b77cc8f@102a2323dabd8bbe1950f4d691c94001
---

# Making Data Out Of Functions

Source: [[javascriptallonge]]

## Statements

- For example, this length function uses a functions to bind values to names, POJOs to structure nodes, and the ternary function to detect the base case, the empty list. (javascriptallonge.pdf p.177)
- In our code so far, we have used arrays and objects to represent the structure of data, and we have extensively used the ternary operator to write algorithms that terminate when we reach a base case. (javascriptallonge.pdf p.177)
- They searched for a radically simpler set of tools that could accomplish all of the same things. (javascriptallonge.pdf p.178)
- A very long time ago, mathematicians like Alonzo Church, Moses Schönfinkel, Alan Turning, and Haskell Curry and asked themselves if we really needed all these features to perform computations. (javascriptallonge.pdf p.178)
- We can model lists just using functions. (javascriptallonge.pdf p.178)
- For example, we don't need arrays to represent lists, or even POJOs to represent nodes in a linked list. (javascriptallonge.pdf p.178)
- They established that arbitrary computations could be represented a small set of axiomatic components. (javascriptallonge.pdf p.178)
- The oscin.es 77 library contains code for all of the standard combinators and for experimenting using the standard notation. (javascriptallonge.pdf p.178)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

```
const EMPTY = {};
const OneTwoThree = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY \
} } };
OneTwoThree.first
//=> 1
OneTwoThree.rest.first
//=> 2
OneTwoThree.rest.rest.first
//=> 3
const length = (node, delayed = 0) =>
node === EMPTY
? delayed
: length(node.rest, delayed + 1);
length(OneTwoThree)
//=> 3
```

<a id="atom-2"></a>
**Atom:** table

```text
76 http://www.amazon.com/gp/product/0192801422/ref=as_li_ss_tl?ie=UTF8&tag=raganwald001-20&linkCode=as2&camp=1789&creative= 390957&creativeASIN=0192801422
77 http://oscin.es
```

<a id="atom-3"></a>
**Atom:** code block

```
const K = (x) => (y) => x;
const I = (x) => (x);
const V = (x) => (y) => (z) => z(x)(y);
```
