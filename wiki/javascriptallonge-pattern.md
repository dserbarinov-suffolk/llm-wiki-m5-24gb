---
page_id: javascriptallonge-pattern
page_kind: concept
summary: Pattern: 8 statement(s) and 2 atom(s) from raw/javascriptallonge.pdf.
page_family: broad-topic
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-pattern@3d246c3391ada56761efb6d35cc9abc4
---

# Pattern

What [[javascriptallonge]] covers about pattern:

## Statements

### That Constant Coffee Craving / inside-out

- 29 JavaScript programmers regularly use the idea of writing an expression that denotes a function and then immediately applying it to arguments. Explaining the pattern, Ben Alman coined the term [Immediately Invoked Function Expression][iife] for it, often abbreviated 'IIFE.' _(javascriptallonge.pdf (source-range-c98ab3e6-00389))_

### Building Blocks

- When you look at functions within functions in JavaScript, there's a bit of a 'spaghetti code' look to it. The strength of JavaScript is that you can do anything. The weakness is that you will. There are ifs, fors, returns, everything thrown higgledy piggledy together. Although you needn't restrict yourself to a small number of simple patterns, it can be helpful to understand the patterns so that you can structure your code around some basic building blocks. _(javascriptallonge.pdf (source-range-c98ab3e6-00565))_

### Building Blocks / composition

- If that was all there was to it, composition wouldn't matter much. But like many patterns, using it when it applies is only 20% of the benefit. The other 80% comes from organizing your code such that you can use it: Writing functions that can be composed in various ways. _(javascriptallonge.pdf (source-range-c98ab3e6-00571))_

### Mutation / mutation and data structures

- One pattern many people follow is to be liberal with mutation when constructing data, but conservative with mutation when consuming data. Let's recall linked lists from Plain Old JavaScript Objects. While we're executing the mapWith function, we're constructing a new linked list. By this pattern, we would be happy to use mutation to construct the list while running mapWith . _(javascriptallonge.pdf (source-range-c98ab3e6-01119))_

### Copy on Write / a few utilities / copy-on-write

- Looking at the code again, you see that the copy function doesn't copy on write: It follows the pattern that while constructing something, we own it and can be liberal with mutation. Once we're done with it and give it to someone else, we need to be conservative and use a strategy like copy-on-read or copy-on-write. _(javascriptallonge.pdf (source-range-c98ab3e6-01230))_

### Served by the Pot: Collections / Iteration and Iterables / operations on ordered collections

- This illustrates the general pattern of working with ordered collections: We make them iterables , meaning that they have a [Symbol.iterator] method, that returns an iterator . An iterator is also an object, but with a .next() method that is invoked repeatedly to obtain the elements in order. _(javascriptallonge.pdf (source-range-c98ab3e6-01560))_

### Served by the Pot: Collections / Generating Iterables / generators and iterables

- This pattern is encouraged, so much so that JavaScript provides a concise syntax for writing generator methods for objects: _(javascriptallonge.pdf (source-range-c98ab3e6-01682))_


## Related pages

### Source structure

- [[javascriptallonge-section-composing-and-decomposing-data-arrays-and-destructuring-arguments-destructuring-is-not-pattern-m-27d4b226]] - source section: Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring is not pattern matching

### Shared technical atoms

- [[javascriptallonge-javascript]] - shared technical atoms: Javascript shares technical record from That Constant Coffee Craving / inside-out: (diameter) => // ... (2 shared atom(s))
- [[javascriptallonge-generator]] - shared statements and technical atoms: Generator shares source evidence from Served by the Pot: Collections / Generating Iterables / generators and iterables: This pattern is encouraged, so much so that JavaScript provides a concise syntax for writing generator methods for objects:; Generator shares technical record from Served by the Pot: Collections / Generating Iterables / generators and iterables: const ThreeNumbers = { *[Symbol.iterator] () { yield 1; yield 2; yield 3 } } (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-iterable]] - shared statements and technical atoms: Iterable shares source evidence from Served by the Pot: Collections / Iteration and Iterables / operations on ordered collections: This illustrates the general pattern of working with ordered collections: We make them iterables , meaning that they have a [Symbol.iterator] method, that returns an ... [truncated]; Iterable shares technical record from Served by the Pot: Collections / Generating Iterables / generators and iterables: const ThreeNumbers = { *[Symbol.iterator] () { yield 1; yield 2; yield 3 } } (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-expression]] - shared technical atoms: Expression shares technical record from That Constant Coffee Craving / inside-out: (diameter) => // ... (1 shared atom(s))
- [[javascriptallonge-iterator]] - shared technical atoms: Iterator shares technical record from Served by the Pot: Collections / Generating Iterables / generators and iterables: const ThreeNumbers = { *[Symbol.iterator] () { yield 1; yield 2; yield 3 } } (1 shared atom(s))
- [[javascriptallonge-method]] - shared technical atoms: Method shares technical record from Served by the Pot: Collections / Generating Iterables / generators and iterables: const ThreeNumbers = { *[Symbol.iterator] () { yield 1; yield 2; yield 3 } } (1 shared atom(s))
- [[javascriptallonge-object]] - shared technical atoms: Object shares technical record from Served by the Pot: Collections / Generating Iterables / generators and iterables: const ThreeNumbers = { *[Symbol.iterator] () { yield 1; yield 2; yield 3 } } (1 shared atom(s))

### Shared claims

- [[javascriptallonge-mutation]] - shared statements: Mutation shares source evidence from Mutation / mutation and data structures: One pattern many people follow is to be liberal with mutation when constructing data, but conservative with mutation when consuming data. Let's recall linked lists f ... [truncated] (2 shared statement(s))
- [[javascriptallonge-copy]] - shared statements: Copy shares source evidence from Copy on Write / a few utilities / copy-on-write: Looking at the code again, you see that the copy function doesn't copy on write: It follows the pattern that while constructing something, we own it and can be liber ... [truncated] (1 shared statement(s))
- [[javascriptallonge-copy-write]] - shared statements: Copy on Write shares source evidence from Copy on Write / a few utilities / copy-on-write: Looking at the code again, you see that the copy function doesn't copy on write: It follows the pattern that while constructing something, we own it and can be liber ... [truncated] (1 shared statement(s))
- [[javascriptallonge-write]] - shared statements: Write shares source evidence from Copy on Write / a few utilities / copy-on-write: Looking at the code again, you see that the copy function doesn't copy on write: It follows the pattern that while constructing something, we own it and can be liber ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
