---
page_id: javascriptallonge-section-plain-old-javascript-objects-ae9a88a3
page_kind: source
summary: Plain Old JavaScript Objects: 14 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-plain-old-javascript-objects-ae9a88a3@eb01dfc83d6cb62d8e8517948143bbae
---

# Plain Old JavaScript Objects

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-garbage-garbage-everywhere-8c9764a5]] - previous source section: Garbage, Garbage Everywhere
- [[javascriptallonge-section-mutation-ae8039d8]] - next source section: Mutation

### Source structure

- [[javascriptallonge-section-plain-old-javascript-objects-destructuring-objects-6546a490]] - narrower source section: Plain Old JavaScript Objects / destructuring objects
- [[javascriptallonge-section-plain-old-javascript-objects-literal-object-syntax-41ad73a1]] - narrower source section: Plain Old JavaScript Objects / literal object syntax
- [[javascriptallonge-section-plain-old-javascript-objects-revisiting-linked-lists-4e16a53d]] - narrower source section: Plain Old JavaScript Objects / revisiting linked lists

## Statements

- Lists are not the only way to represent collections of things, but they are the 'oldest' data structure in the history of high level languages, because they map very closely to the way the hardware is organized in a computer. Lists are obviously very handy for homogeneous collections of things, like a shopping list: _(javascriptallonge.pdf (source-range-c98ab3e6-01041))_
- Remembering that the name is the first item is error-prone, and being expected to look at user[0][1] and know that we are talking about a surname is unreasonable. So back when lists were the only things available, programmers would introduce constants to make things easier on themselves: _(javascriptallonge.pdf (source-range-c98ab3e6-01044))_
- Now they could write user[NAME][LAST] or user[OCCUPATION][TITLE] instead of user[0][1] or user[1][0] . Over time, this need to build heterogeneous data structures with access to members by name evolved into the Dictionary 69 data type, a mapping from a unique set of objects to another set of objects. _(javascriptallonge.pdf (source-range-c98ab3e6-01046))_
- Dictionaries store key-value pairs, so instead of binding NAME to 0 and then storing a name in an array at index 0 , we can bind a name directly to name in a dictionary, and we let JavaScript sort out whether the implementation is a list of key-value pairs, a hashed collection, a tree of some sort, or anything else. _(javascriptallonge.pdf (source-range-c98ab3e6-01047))_
- JavaScript has dictionaries, and it calls them 'objects.' The word 'object' is loaded in programming circles, due to the widespread use of the term 'object-oriented programming' that was coined by Alan Kay but has since come to mean many, many things to many different people. _(javascriptallonge.pdf (source-range-c98ab3e6-01048))_
- In JavaScript, an object is a map from string keys to values. _(javascriptallonge.pdf (source-range-c98ab3e6-01049))_
- Lists are not the only way to represent collections of things, but they are the 'oldest' data structure in the history of high level languages, because they map very closely to the way the hardware is organized in a computer. _(javascriptallonge.pdf (source-range-c98ab3e6-01041))_
- So back when lists were the only things available, programmers would introduce constants to make things easier on themselves: _(javascriptallonge.pdf (source-range-c98ab3e6-01044))_
- Dictionaries store key-value pairs, so instead of binding NAME to 0 and then storing a name in an array at index 0 , we can bind a name directly to name in a dictionary, and we let JavaScript sort out whether the implementation is a list of key-value pairs, a hashed collection, a tree of some sort, or anything else. _(javascriptallonge.pdf (source-range-c98ab3e6-01047))_
