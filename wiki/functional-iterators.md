---
category: concept
summary: Functional iterators separate traversal from operations, enabling lazy evaluation and composition. See (raw/javascriptallonge.pdf p.158-176) for implementation examples.
sources: raw/javascriptallonge.pdf, raw/javascriptallonge.pdf p.158-176
updated: 2026-06-11
---

## Functional Iterators

Functional iterators decouple data traversal from operations, enabling **lazy evaluation** and **composable transformations**. They are implemented as functions that return `{ done, value }` objects.

### Key Concepts:
- **Lazy Evaluation**: Data is generated on-demand rather than precomputed.
- **Composition**: Iterators can be mapped, filtered, or transformed without modifying the original data structure.

### Example: Array Iterator
```javascript
const arrayIterator = (array) => {
  let i = 0;
  return () => ({
    done: i === array.length,
    value: i < array.length ? array[i++] : undefined
  });
};
```

### Example: Linked List Iterator
```javascript
const listIterator = (aPair) => () => {
  const done = isEmpty(aPair);
  if (done) return { done };
  const { first, rest } = aPair;
  aPair = aPair.rest;
  return { done, value: first };
};
```

### Unfolding
An *unfold* generates data on-the-fly (opposite of folding). Example: Infinite number generator:
```javascript
const NumberIterator = (number = 0) => () => ({ done: false, value: number++ });
```

### Benefits:
- **Memory Efficiency**: Only processes needed elements.
- **Modularity**: Transformations like `mapIteratorWith` and `filterIteratorWith` can be reused.

### Sources:
- (raw/javascriptallonge.pdf p.158-176)
