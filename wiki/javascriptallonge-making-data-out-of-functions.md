---
category: source
summary: Making Data Out Of Functions from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.177-197
updated: 2026-06-18
domain: javascriptallonge
category_path: source-sections
source_id: javascriptallonge.pdf
---

## Making Data Out Of Functions

This section discusses how data can be represented using functions rather than traditional data structures like arrays or objects. It introduces combinatory logic and several key combinators, including the K (Kestrel), I (Idiot Bird), and V (Vireo) combinators.

### The Kestrel and the Idiot Bird

- **K (Kestrel)**: A constant function that always returns the first value provided. For example, `K(42)(anything)` will return `42`.
- **I (Idiot Bird)**: An identity function that returns its input. For example, `I(42)` returns `42`.
- **K(I)**: A function that returns the second value provided. For example, `K(I)("primus")("secundus")` returns `"secundus"`.

These combinators are used to build more complex functions and data structures without relying on traditional data structures.

### Backwardness

The functions built from K and I operate in a way that is different from conventional data access functions. Instead of passing data to functions to extract values, these functions are passed to the data structure to retrieve values. This approach is described as being "exactly backwards" compared to traditional function usage.

### The Vireo

The V combinator is introduced as a more complex function that takes three arguments and returns the third one applied to the first two. It is used to build more complex data structures and operations.

This section highlights the potential of using functions to model data and computations, inspired by the work of mathematicians like Alonzo Church and Haskell Curry. It also references the oscin.es library for experimenting with combinators.
