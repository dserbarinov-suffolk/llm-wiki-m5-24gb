---
category: source
summary: Garbage, Garbage Everywhere from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.126-140
updated: 2026-06-18
domain: javascriptallonge
category_path: source-sections
source_id: javascriptallonge.pdf
---

## Garbage, Garbage Everywhere

This section discusses the performance issues with the `mapWith` function in JavaScript and how it creates a lot of temporary arrays, leading to significant memory copying and garbage collection overhead.

### Key Points:
- The `mapWith` function creates new arrays at each recursive call, which leads to memory copying and garbage collection overhead.
- This approach is slow because it creates a lot of temporary arrays and spends a lot of time copying elements into them.
- The issue arises from the use of `[first, ...rest]` in recursion, which creates new arrays at each step.

### Example:
```javascript
const mapWith = (fn, [first, ...rest], prepend = []) => 
  first === undefined 
    ? prepend 
    : mapWith(fn, rest, [...prepend, fn(first)]);
```

### Performance Considerations:
- Each call to `mapWith` creates a new array, which is then discarded after the function call, leading to frequent garbage collection.
- This is inefficient compared to built-in methods like `.map`.

### Historical Context:
- The section also touches on the history of Lisp and the IBM 704 computer, explaining how early programming languages were influenced by hardware limitations.
- It describes how Lisp used cons cells to represent data structures efficiently, which is analogous to using linked lists in JavaScript.

### Linked List Example:
```javascript
const cons = (a, d) => [a, d], car = ([a, d]) => a, cdr = ([a, d]) => d;
const oneToFive = cons(1, cons(2, cons(3, cons(4, cons(5, null)))));
```

This example demonstrates how linked lists can be represented using arrays in JavaScript, though they are not as efficient as specialized data structures.
