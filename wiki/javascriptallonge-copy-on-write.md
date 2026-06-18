---
category: source
summary: Copy on Write from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.158-176
updated: 2026-06-18
domain: javascriptallonge
category_path: source-sections
source_id: javascriptallonge.pdf
---

## Copy on Write

**The Coffee Cow**

When working with data structures like arrays and linked lists, there's a key difference in how they handle modifications:

- **Arrays**: Taking the rest of an array with destructuring creates a copy of the elements. Modifications to the parent array do not affect the child array, and vice versa.
- **Linked Lists**: Taking the rest of a linked list shares the same nodes. Modifications to the parent list affect the child list and vice versa.

This can lead to unexpected behavior. For example, if you modify the parent list, the child list also changes, and vice versa.

### a few utilities

To work at a higher level of abstraction, we can define a few utilities:

- `copy(node, head = null, tail = null)`: Creates a copy of a linked list.
- `first(node)`: Gets the first element of a list.
- `rest(node)`: Gets the rest of a list.
- `reverse(node, delayed = EMPTY)`: Reverses a list.
- `mapWith(fn, node, delayed = EMPTY)`: Applies a function to each element of a list.
- `at(index, list)`: Gets the element at a specific index.
- `set(index, value, list, originalList = list)`: Sets the value at a specific index.

### copy-on-read

One strategy to avoid problems with structure sharing is to be pessimistic. Whenever we take the rest of a list, make a copy. This is called **copy-on-read**. However, this approach can be expensive.

### copy-on-write

An alternative is to make the copy only when we know we are modifying the list. This is called **copy-on-write**. We can achieve this by modifying the `set` function to create a copy only when needed.

This approach avoids unnecessary copying and ensures that modifications to the list do not interfere with other references to the same list.
