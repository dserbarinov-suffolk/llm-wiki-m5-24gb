---
page_id: javascriptallonge-plain-old-javascript-objects
page_kind: concept
summary: Plain Old JavaScript Objects: 8 accepted assertion(s) and 3 technical atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-state-tps_89b044418b05e3cb@4744809b129cd7360bc3971938f0a5ca
---

# Plain Old JavaScript Objects

Source: [[javascriptallonge]]

## Statements

- Lists are not the only way to represent collections of things, but they are the 'oldest' data structure in the history of high level languages, because they map very closely to the way the hardware is organized in a computer. (javascriptallonge.pdf p.132)
- So back when lists were the only things available, programmers would introduce constants to make things easier on themselves:. (javascriptallonge.pdf p.132)
- Remembering that the name is the first item is error-prone, and being expected to look at user[0][1] and know that we are talking about a surname is unreasonable. (javascriptallonge.pdf p.132)
- Over time, this need to build heterogeneous data structures with access to members by name evolved into the Dictionary 69 data type, a mapping from a unique set of objects to another set of objects. (javascriptallonge.pdf p.132)
- Now they could write user[NAME][LAST] or user[OCCUPATION][TITLE] instead of user[0][1] or user[1][0] . (javascriptallonge.pdf p.132)
- Dictionaries store key-value pairs, so instead of binding NAME to 0 and then storing a name in an array at index 0 , we can bind a name directly to name in a dictionary, and we let JavaScript sort out whether the implementation is a list of key-value pairs, a hashed collection, a tree of some sort, or anything else. (javascriptallonge.pdf p.132)
- JavaScript has dictionaries, and it calls them 'objects.' The word 'object' is loaded in programming circles, due to the widespread use of the term 'object-oriented programming' that was coined by Alan Kay but has since come to mean many, many things to many different people. (javascriptallonge.pdf p.132)
- In JavaScript, an object is a map from string keys to values. (javascriptallonge.pdf p.132)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

```
const remember = ["the milk", "the coffee beans", "the biscotti"];
And they can be used to store heterogeneous things in various levels of structure:
```

<a id="atom-2"></a>
**Atom:** code block

```
const user = [["Reginald", "Braithwaite"],[ "author", ["JavaScript Allongé", "Ja\
vaScript Spessore", "CoffeeScript Ristretto"]]];
```

<a id="atom-3"></a>
**Atom:** code block

```
const NAME = 0,
FIRST = 0,
LAST = 1,
OCCUPATION = 1,
TITLE = 0,
RESPONSIBILITIES = 1;
const user = [["Reginald", "Braithwaite"],[ "author", ["JavaScript Allongé", "Ja\
vaScript Spessore", "CoffeeScript Ristretto"]]];
```
