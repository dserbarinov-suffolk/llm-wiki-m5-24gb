---
page_id: javascriptallonge-section-garbage-garbage-everywhere-so-why-arrays-270c6428
page_kind: source
summary: Garbage, Garbage Everywhere / so why arrays: 7 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-06-30
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-garbage-garbage-everywhere-so-why-arrays-270c6428@f1a8a70f1b558035f85ec525df2d54f2
---

# Garbage, Garbage Everywhere / so why arrays

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-garbage-garbage-everywhere-c3e1739c]] - broader source section: Garbage, Garbage Everywhere
- [[javascriptallonge-section-garbage-garbage-everywhere-some-history-a956a93b]] - previous source section: Garbage, Garbage Everywhere / some history
- [[javascriptallonge-section-garbage-garbage-everywhere-summary-ca623d10]] - next source section: Garbage, Garbage Everywhere / summary
- [[javascriptallonge-array]] - topic hub: opens the topic page for Array

## Statements

- Well, linked lists are fast for a few things, like taking the front element off a list, and taking the remainder of a list. But not for iterating over a list: Pointer chasing through memory is quite a bit slower than incrementing an index. In addition to the extra fetches to dereference pointers, pointer chasing suffers from cache misses. And if you want an arbitrary item from a list, you have to iterate through the list element by element, whereas with the indexed array you just fetch it. _(javascriptallonge.pdf (source-range-0e12e052-01050))_
- We have avoided discussing rebinding and mutating values, but if we want to change elements of our lists, the naïve linked list implementation suffers as well: When we take the cdr of a linked list, we are sharing the elements. If we make any change other than cons-ing a new element to the front, we are changing both the new list and the old list. _(javascriptallonge.pdf (source-range-0e12e052-01051))_
- Arrays avoid this problem by pessimistically copying all the references whenever we extract an element or sequence of elements from them (We'll see this explained later in Mutation). _(javascriptallonge.pdf (source-range-0e12e052-01052))_
- For these and other reasons, almost all languages today make it possible to use a fast array or vector type that is optimized for iteration, and even Lisp now has a variety of data structures that are optimized for specific use cases. _(javascriptallonge.pdf (source-range-0e12e052-01053))_

## Technical atoms

### Technical frame 1: Garbage, Garbage Everywhere / so why arrays

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01051))_

> We have avoided discussing rebinding and mutating values, but if we want to change elements of our lists, the naïve linked list implementation suffers as well: When we take the cdr of a linked list, we are sharing the elements. If we make any change other than cons-ing a new element to the front, we are changing both the new list and the old list.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01050))_

> And if you want an arbitrary item from a list, you have to iterate through the list element by element, whereas with the indexed array you just fetch it.

### Technical frame 2: Garbage, Garbage Everywhere / so why arrays

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01052))_

> Arrays avoid this problem by pessimistically copying all the references whenever we extract an element or sequence of elements from them (We'll see this explained later in Mutation).

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01051))_

> We have avoided discussing rebinding and mutating values, but if we want to change elements of our lists, the naïve linked list implementation suffers as well: When we take the cdr of a linked list, we are sharing the elements.
