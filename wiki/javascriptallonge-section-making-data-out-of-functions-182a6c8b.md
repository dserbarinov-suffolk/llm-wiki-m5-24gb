---
page_id: javascriptallonge-section-making-data-out-of-functions-182a6c8b
page_kind: source
summary: Making Data Out Of Functions: 12 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-making-data-out-of-functions-182a6c8b@ad9b574213b98304e5461c3d87719593
---

# Making Data Out Of Functions

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-recipes-with-data-4b3e2c99]] - next source section: Recipes with Data

### Source structure

- [[javascriptallonge-section-making-data-out-of-functions-a-return-to-backward-thinking-0d028ef6]] - narrower source section: Making Data Out Of Functions / a return to backward thinking
- [[javascriptallonge-section-making-data-out-of-functions-backwardness-05f902ef]] - narrower source section: Making Data Out Of Functions / backwardness
- [[javascriptallonge-section-making-data-out-of-functions-functions-are-not-the-real-point-0ee51da0]] - narrower source section: Making Data Out Of Functions / functions are not the real point
- [[javascriptallonge-section-making-data-out-of-functions-lists-with-functions-as-data-e74e34a2]] - narrower source section: Making Data Out Of Functions / lists with functions as data
- [[javascriptallonge-section-making-data-out-of-functions-say-please-f8da9670]] - narrower source section: Making Data Out Of Functions / say 'please'
- [[javascriptallonge-section-making-data-out-of-functions-the-kestrel-and-the-idiot-203dea45]] - narrower source section: Making Data Out Of Functions / the kestrel and the idiot
- [[javascriptallonge-section-making-data-out-of-functions-the-vireo-1b2dccd1]] - narrower source section: Making Data Out Of Functions / the vireo

## Statements

- In our code so far, we have used arrays and objects to represent the structure of data, and we have extensively used the ternary operator to write algorithms that terminate when we reach a base case. For example, this length function uses a functions to bind values to names, POJOs to structure nodes, and the ternary function to detect the base case, the empty list. _(javascriptallonge.pdf (source-range-c98ab3e6-01302))_
- A very long time ago, mathematicians like Alonzo Church, Moses Schönfinkel, Alan Turning, and Haskell Curry and asked themselves if we really needed all these features to perform computations. They searched for a radically simpler set of tools that could accomplish all of the same things. _(javascriptallonge.pdf (source-range-c98ab3e6-01304))_
- They established that arbitrary computations could be represented a small set of axiomatic components. For example, we don't need arrays to represent lists, or even POJOs to represent nodes in a linked list. We can model lists just using functions. _(javascriptallonge.pdf (source-range-c98ab3e6-01305))_
- The oscin.es 77 library contains code for all of the standard combinators and for experimenting using the standard notation. _(javascriptallonge.pdf (source-range-c98ab3e6-01307))_
- For example, this length function uses a functions to bind values to names, POJOs to structure nodes, and the ternary function to detect the base case, the empty list. _(javascriptallonge.pdf (source-range-c98ab3e6-01302))_
- For example, we don't need arrays to represent lists, or even POJOs to represent nodes in a linked list. _(javascriptallonge.pdf (source-range-c98ab3e6-01305))_

## Technical atoms

### Technical frame 1: Making Data Out Of Functions

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01304))_

> A very long time ago, mathematicians like Alonzo Church, Moses Schönfinkel, Alan Turning, and Haskell Curry and asked themselves if we really needed all these features to perform computations. They searched for a radically simpler set of tools that could accomplish all of the same things.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01303))_

<a id="atom-technical-atom-99dd059e4394fcc2"></a>
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
