---
category: source
summary: Iteration and Iterables from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.206-223
updated: 2026-06-18
domain: javascriptallonge
category_path: source-sections
source_id: javascriptallonge.pdf
---

## Iteration and Iterables

This page summarizes the content from `raw/javascriptallonge.pdf` pages 206-223, which discusses iteration and iterables in JavaScript.

### Key Concepts
- **Iteration**: The process of acting on elements of a collection one at a time.
- **Functional Iterators**: Functions that allow iteration over collections, such as the `iterator()` method for objects.
- **Iterator Objects**: Objects with a `.next()` method for iteration, providing a more structured approach compared to functional iterators.

### Example: Functional Iterator
A stack object with an `iterator()` method returns a function that yields elements one by one. This function can be used with a `sum` function to compute the sum of elements in the stack.

### Example: Iterator Object
An alternative approach uses an iterator object with a `.next()` method to iterate over elements. This is useful for large collections and allows for more structured iteration mechanics.

### Benefits
- **Lazy Evaluation**: Iteration is done lazily, improving efficiency.
- **Flexibility**: Functions can work on any object that implements an `.iterator` method, without needing to know the internal implementation.

### Related Pages
- [[iterable]]
- [[javascriptallonge-recipes-with-basic-functions]]
- [[ordered-collection]]
- [[javascriptallonge-copy-on-write]]
- [[javascriptallonge-chapter-5]]
