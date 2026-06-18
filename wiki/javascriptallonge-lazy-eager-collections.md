---
category: source
summary: Lazy and Eager Collections from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.246-260
updated: 2026-06-18
domain: javascriptallonge
category_path: source-sections
source_id: javascriptallonge.pdf
---

## Lazy and Eager Collections

This page summarizes the discussion on lazy and eager collections from *JavaScript Allongé* (raw/javascriptallonge.pdf p.246-260).

### Key Concepts
- **Lazy vs. Eager Collections**: Lazy collections defer computation until needed, while eager collections compute immediately.
- **Iterables**: Using iterables helps separate the responsibility of mapping, reducing, filtering, and finding from the specific implementation of collections.
- **Mixin Pattern**: LazyCollection is a mixin that can be used with any iterable object to add lazy evaluation methods like `map`, `reduce`, `filter`, and `find`.

### Example: LazyCollection
LazyCollection provides methods for lazy evaluation, such as:
- `map(fn)`: Applies a function to each element lazily.
- `reduce(fn, seed)`: Reduces the collection to a single value using a function.
- `filter(fn)`: Filters elements based on a function.
- `find(fn)`: Finds the first element that satisfies a function.

### Implementation
LazyCollection is implemented using the iterable protocol and can be mixed into any iterable object. It delegates the implementation details to the iterable itself, allowing for reusable and composable code.

### Benefits
- **Modularity**: Separates concerns, making code more modular and easier to maintain.
- **Reusability**: Common logic for collection operations can be reused across different types of collections.
- **Efficiency**: Lazy evaluation can improve performance by deferring computation until necessary.

### Related Pages
- [[javascriptallonge-recipes-with-basic-functions]]
- [[iterable]]
- [[javascriptallonge-copy-on-write]]
