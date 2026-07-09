---
page_id: javascriptallonge-so-why-arrays
page_kind: concept
summary: so why arrays: 5 accepted assertion(s) and 2 technical atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-state-tps_89cbb033bc1469df@673c3f53d96e8cc5461e8e711fa323d4
---

# so why arrays

Source: [[javascriptallonge]]

## Statements

- But not for iterating over a list: Pointer chasing through memory is quite a bit slower than incrementing an index. (javascriptallonge.pdf p.131)
- Well, linked lists are fast for a few things, like taking the front element off a list, and taking the remainder of a list. (javascriptallonge.pdf p.131)
- If we make any change other than cons-ing a new element to the front, we are changing both the new list and the old list. (javascriptallonge.pdf p.131)
- Arrays avoid this problem by pessimistically copying all the references whenever we extract an element or sequence of elements from them (We'll see this explained later in Mutation). (javascriptallonge.pdf p.131)
- For these and other reasons, almost all languages today make it possible to use a fast array or vector type that is optimized for iteration, and even Lisp now has a variety of data structures that are optimized for specific use cases. (javascriptallonge.pdf p.131)

## Technical atoms

<a id="atom-1"></a>
**Atom:** rule

```
And if you want an arbitrary item from a list, you have to iterate through the list element by element, whereas with the indexed array you just fetch it.
```

<a id="atom-2"></a>
**Atom:** rule

```
We have avoided discussing rebinding and mutating values, but if we want to change elements of our lists, the naïve linked list implementation suffers as well: When we take the cdr of a linked list, we are sharing the elements.
```
