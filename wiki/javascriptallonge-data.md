---
page_id: javascriptallonge-data
page_kind: concept
summary: Data: 7 statement(s) and 6 atom(s) from raw/javascriptallonge.pdf.
page_family: broad-topic
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-data@417d52dc648f7fe84939424e6aeb9650
---

# Data

What [[javascriptallonge]] covers about data:

## Statements

### Composing and Decomposing Data / Self-Similarity

- Let's be more specific. Some data structures, like lists, can obviously be seen as a collection of items. Some are empty, some have three items, some forty-two, some contain numbers, some contain strings, some a mixture of elements, there are all kinds of lists. _(javascriptallonge.pdf (source-range-c98ab3e6-00866))_

### Garbage, Garbage Everywhere / some history

- Thus, CONS put two values together, CAR extracted one, and CDR extracted the other. Lisp's basic data type is often said to be the list, but in actuality it was the 'cons cell,' the term used to describe two 15-bit values stored in one word. The 15-bit values were used as pointers that could refer to a location in memory, so in effect, a cons cell was a little data structure with two pointers to other cons cells. _(javascriptallonge.pdf (source-range-c98ab3e6-01011))_

### Copy on Write / Functional Iterators

- What we've done is turn an array into a function that folds an array with const foldArray = (array) => callRight(foldArrayWith, array); . The sumFoldable function doesn't care what kind of data structure we have, as long as it's foldable. _(javascriptallonge.pdf (source-range-c98ab3e6-01255))_

### Making Data Out Of Functions / backwardness

- In both cases, the functions first and second know how the data is represented, whether it be an array or an object. You pass the data to these functions, and they extract it. _(javascriptallonge.pdf (source-range-c98ab3e6-01332))_

- Our latin data structure is no longer a dumb data structure, it's a function. And instead of passing latin to first or second , we pass first or second to latin . It's exactly backwards of the way we write functions that operate on data. _(javascriptallonge.pdf (source-range-c98ab3e6-01336))_

### Making Data Out Of Functions / the vireo

- Given that our latin data is represented as the function (selector) => selector("primus")("secundus") , our obvious next step is to make a function that makes data. For arrays, we'd write cons = (first, second) => [first, second] . For objects we'd write: cons = (first, second) => {first, second} . In both cases, we take two parameters, and return the form of the data. _(javascriptallonge.pdf (source-range-c98ab3e6-01338))_

- For 'data' we access with K and K(I) , our 'structure' is the function (selector) => selector("primus")("secundus") . Let's extract those into parameters: _(javascriptallonge.pdf (source-range-c98ab3e6-01339))_


## Technical atoms

### Technical frame 1: Making Data Out Of Functions / backwardness

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01332))_

> In both cases, the functions first and second know how the data is represented, whether it be an array or an object. You pass the data to these functions, and they extract it.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01329))_

<a id="atom-technical-atom-66fc28ff3c959742"></a>
```
const first = ([first, second]) => first,
second = ([first, second]) => second;
const latin = ["primus", "secundus"];
first(latin)
//=> "primus"
second(latin)
//=> "secundus"
```


## Related pages

### Source structure

- [[javascriptallonge-section-composing-and-decomposing-data-99b4771a]] - source section: Composing and Decomposing Data
- [[javascriptallonge-section-composing-and-decomposing-data-arrays-and-destructuring-arguments-2a38bfc8]] - source section: Composing and Decomposing Data / Arrays and Destructuring Arguments
- [[javascriptallonge-section-composing-and-decomposing-data-arrays-and-destructuring-arguments-array-literals-f2f1b6ec]] - source section: Composing and Decomposing Data / Arrays and Destructuring Arguments / array literals
- [[javascriptallonge-section-composing-and-decomposing-data-arrays-and-destructuring-arguments-destructuring-and-return-value-0323454e]] - source section: Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring and return values
- [[javascriptallonge-section-composing-and-decomposing-data-arrays-and-destructuring-arguments-destructuring-arrays-327f6ba9]] - source section: Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring arrays
- [[javascriptallonge-section-composing-and-decomposing-data-arrays-and-destructuring-arguments-destructuring-is-not-pattern-m-27d4b226]] - source section: Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring is not pattern matching
- [[javascriptallonge-section-composing-and-decomposing-data-arrays-and-destructuring-arguments-destructuring-parameters-1a788a19]] - source section: Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring parameters
- [[javascriptallonge-section-composing-and-decomposing-data-arrays-and-destructuring-arguments-element-references-75756e27]] - source section: Composing and Decomposing Data / Arrays and Destructuring Arguments / element references

### Shared technical atoms

- [[javascriptallonge-structure]] - shared statements and technical atoms: Structure shares source evidence from Composing and Decomposing Data / Self-Similarity: Let's be more specific. Some data structures, like lists, can obviously be seen as a collection of items. Some are empty, some have three items, some forty-two, some ... [truncated]; Structure shares technical record from Making Data Out Of Functions / the vireo: (first, second) => (selector) => selector(first)(second) (4 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-list]] - shared statements and technical atoms: List shares source evidence from Composing and Decomposing Data / Self-Similarity: Let's be more specific. Some data structures, like lists, can obviously be seen as a collection of items. Some are empty, some have three items, some forty-two, some ... [truncated]; List shares technical record from Garbage, Garbage Everywhere / some history: car(oneToFive) //=> 1 (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-allong]] - shared technical atoms: Allong shares technical record from JavaScript Allongé, the 'Six' Edition / Reg 'raganwald' Braithwaite: Contents | Composing and Decomposing Data . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 77 | | --- | --- | --- | | Arrays and Destructuring Argum ... [truncated] (1 shared atom(s))
- [[javascriptallonge-edition]] - shared technical atoms: Edition shares technical record from JavaScript Allongé, the 'Six' Edition / Reg 'raganwald' Braithwaite: Contents | Composing and Decomposing Data . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 77 | | --- | --- | --- | | Arrays and Destructuring Argum ... [truncated] (1 shared atom(s))
- [[javascriptallonge-javascript]] - shared technical atoms: Javascript shares technical record from JavaScript Allongé, the 'Six' Edition / Reg 'raganwald' Braithwaite: Contents | Composing and Decomposing Data . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 77 | | --- | --- | --- | | Arrays and Destructuring Argum ... [truncated] (1 shared atom(s))
- [[javascriptallonge-parameter]] - shared technical atoms: Parameter shares technical record from Making Data Out Of Functions / the vireo: (first, second) => (selector) => selector(first)(second) (1 shared atom(s))
- [[javascriptallonge-reference]] - shared technical atoms: Reference shares technical record from Garbage, Garbage Everywhere / some history: car(oneToFive) //=> 1 (1 shared atom(s))

### Shared claims

- [[javascriptallonge-copy-write]] - shared statements: Copy on Write shares source evidence from Copy on Write / Functional Iterators: What we've done is turn an array into a function that folds an array with const foldArray = (array) => callRight(foldArrayWith, array); . The sumFoldable function do ... [truncated] (1 shared statement(s))
- [[javascriptallonge-functional-iterator]] - shared statements: Functional Iterators shares source evidence from Copy on Write / Functional Iterators: What we've done is turn an array into a function that folds an array with const foldArray = (array) => callRight(foldArrayWith, array); . The sumFoldable function do ... [truncated] (1 shared statement(s))
- [[javascriptallonge-type]] - shared statements: Type shares source evidence from Garbage, Garbage Everywhere / some history: Thus, CONS put two values together, CAR extracted one, and CDR extracted the other. Lisp's basic data type is often said to be the list, but in actuality it was the ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
