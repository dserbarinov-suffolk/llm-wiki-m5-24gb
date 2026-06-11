---
category: concept
summary: Functional data structures use closures and higher-order functions to represent lists, pairs, and other structures without arrays/objects. Key example: using combinator V to create data.
sources: raw/javascriptallonge.pdf
updated: 2026-06-11
---

Functional data structures are implemented using closures and higher-order functions rather than traditional arrays or objects. In *JavaScript Allonge*, this is demonstrated through combinators like V (Vireo) to create linked lists and pairs:

```javascript
const pair = V;
const list = pair(1)(pair(2)(pair(3)(EMPTY)));
```

This approach hides implementation details from consumers, allowing data structures to self-manage operations like `length` or `map`. See [[javascriptallonge-making-data-out-of-functions]] for implementation details and comparisons to object-based approaches.
