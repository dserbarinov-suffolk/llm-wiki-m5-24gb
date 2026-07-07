---
page_id: javascriptallonge-structure
page_kind: concept
summary: Structure: 5 statement(s) and 2 atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-structure@58da36475201a7cc875e3a6e8ad3b4c4
---

# Structure

What [[javascriptallonge]] covers about structure:

## Statements

### Composing and Decomposing Data / Self-Similarity

- Let's be more specific. Some data structures, like lists, can obviously be seen as a collection of items. Some are empty, some have three items, some forty-two, some contain numbers, some contain strings, some a mixture of elements, there are all kinds of lists. _(javascriptallonge.pdf (source-range-c98ab3e6-00866))_

### Garbage, Garbage Everywhere / some history

- Again, it's just extracting a reference from a cons cell, it's very fast. In Lisp, it's blazingly fast because it happens in hardware. There's no making copies of arrays, the time to cdr a list with five elements is the same as the time to cdr a list with 5,000 elements, and no temporary arrays are needed. In JavaScript, it's still much, much, much faster to get all the elements except the head from a linked list than from an array. Getting one reference to a structure that already exists is faster than copying a bunch of elements. _(javascriptallonge.pdf (source-range-c98ab3e6-01026))_

### Copy on Write / Functional Iterators

- What we've done is turn an array into a function that folds an array with const foldArray = (array) => callRight(foldArrayWith, array); . The sumFoldable function doesn't care what kind of data structure we have, as long as it's foldable. _(javascriptallonge.pdf (source-range-c98ab3e6-01255))_

### Making Data Out Of Functions / backwardness

- Our latin data structure is no longer a dumb data structure, it's a function. And instead of passing latin to first or second , we pass first or second to latin . It's exactly backwards of the way we write functions that operate on data. _(javascriptallonge.pdf (source-range-c98ab3e6-01336))_

### Making Data Out Of Functions / the vireo

- For 'data' we access with K and K(I) , our 'structure' is the function (selector) => selector("primus")("secundus") . Let's extract those into parameters: _(javascriptallonge.pdf (source-range-c98ab3e6-01339))_


## Technical atoms

### Technical frame 1: Garbage, Garbage Everywhere / some history

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01026))_

> Again, it's just extracting a reference from a cons cell, it's very fast. In Lisp, it's blazingly fast because it happens in hardware. There's no making copies of arrays, the time to cdr a list with five elements is the same as the time to cdr a list with 5,000 elements, and no temporary arrays are needed. In JavaScript, it's still much, much, much faster to get all the elements except the head from a linked list than from an array. Getting one reference to a structure that already exists is fas

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01025))_

<a id="atom-technical-atom-26303fe469ee0e47"></a>
```
cdr(oneToFive)
//=> [2,[3,[4,[5,null]]]]
```

### Technical frame 2: Making Data Out Of Functions / the vireo

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01341))_

> For consistency with the way combinators are written as functions taking just one parameter, we'll curry 78 the function:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01340))_

<a id="atom-technical-atom-590de5a88990b16d"></a>
```
(first, second) => (selector) => selector(first)(second)
```


## Related pages

### Shared technical atoms

- [[javascriptallonge-data]] - shared statements and technical atoms: Data shares source evidence from Composing and Decomposing Data / Self-Similarity: Let's be more specific. Some data structures, like lists, can obviously be seen as a collection of items. Some are empty, some have three items, some forty-two, some ... [truncated]; Data shares technical record from Making Data Out Of Functions / the vireo: (first, second) => (selector) => selector(first)(second) (4 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-list]] - shared statements and technical atoms: List shares source evidence from Composing and Decomposing Data / Self-Similarity: Let's be more specific. Some data structures, like lists, can obviously be seen as a collection of items. Some are empty, some have three items, some forty-two, some ... [truncated]; List shares technical record from Garbage, Garbage Everywhere / some history: cdr(oneToFive) //=> [2,[3,[4,[5,null]]]] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-reference]] - shared statements and technical atoms: Reference shares source evidence from Garbage, Garbage Everywhere / some history: Again, it's just extracting a reference from a cons cell, it's very fast. In Lisp, it's blazingly fast because it happens in hardware. There's no making copies of ar ... [truncated]; Reference shares technical record from Garbage, Garbage Everywhere / some history: cdr(oneToFive) //=> [2,[3,[4,[5,null]]]] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-copy]] - shared technical atoms: Copy shares technical record from Garbage, Garbage Everywhere / some history: cdr(oneToFive) //=> [2,[3,[4,[5,null]]]] (1 shared atom(s))
- [[javascriptallonge-element]] - shared technical atoms: Element shares technical record from Garbage, Garbage Everywhere / some history: cdr(oneToFive) //=> [2,[3,[4,[5,null]]]] (1 shared atom(s))
- [[javascriptallonge-javascript]] - shared technical atoms: Javascript shares technical record from Garbage, Garbage Everywhere / some history: cdr(oneToFive) //=> [2,[3,[4,[5,null]]]] (1 shared atom(s))
- [[javascriptallonge-parameter]] - shared technical atoms: Parameter shares technical record from Making Data Out Of Functions / the vireo: (first, second) => (selector) => selector(first)(second) (1 shared atom(s))

### Shared claims

- [[javascriptallonge-copy-write]] - shared statements: Copy on Write shares source evidence from Copy on Write / Functional Iterators: What we've done is turn an array into a function that folds an array with const foldArray = (array) => callRight(foldArrayWith, array); . The sumFoldable function do ... [truncated] (1 shared statement(s))
- [[javascriptallonge-functional-iterator]] - shared statements: Functional Iterators shares source evidence from Copy on Write / Functional Iterators: What we've done is turn an array into a function that folds an array with const foldArray = (array) => callRight(foldArrayWith, array); . The sumFoldable function do ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
