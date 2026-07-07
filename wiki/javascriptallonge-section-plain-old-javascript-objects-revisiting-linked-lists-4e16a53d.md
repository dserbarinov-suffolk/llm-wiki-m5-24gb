---
page_id: javascriptallonge-section-plain-old-javascript-objects-revisiting-linked-lists-4e16a53d
page_kind: source
summary: Plain Old JavaScript Objects / revisiting linked lists: 20 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-plain-old-javascript-objects-revisiting-linked-lists-4e16a53d@df19fdcf6e2d0cc51cdd07d265800454
---

# Plain Old JavaScript Objects / revisiting linked lists

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-plain-old-javascript-objects-destructuring-objects-6546a490]] - previous source section: Plain Old JavaScript Objects / destructuring objects

### Source structure

- [[javascriptallonge-section-plain-old-javascript-objects-ae9a88a3]] - broader source section: Plain Old JavaScript Objects

### Recipes

- [[javascriptallonge-recipe-revisiting-linked-lists]] - recipe pattern: revisiting linked lists

## Statements

- In essence, this simple implementation used functions to create an abstraction with named elements. But now that we've looked at objects, we can use an object instead of a two-element array. While we're at it, let's use contemporary names. So our linked list nodes will be formed from { first, rest } _(javascriptallonge.pdf (source-range-c98ab3e6-01085))_
- What about mapping? Well, let's start with the simplest possible thing, making a copy of a list. As we saw above, and discussed in Garbage, Garbage Everywhere, it is fast to iterate forward through a linked list. What isn't fast is naïvely copying a list: _(javascriptallonge.pdf (source-range-c98ab3e6-01088))_
- The problem here is that linked lists are constructed back-to-front, but we iterate over them frontto-back. So to copy a list, we have to save all the bits on the call stack and then construct the list from back-to-front as all the recursive calls return. _(javascriptallonge.pdf (source-range-c98ab3e6-01090))_
- We could follow the strategy of delaying the work. Let's write that naively: _(javascriptallonge.pdf (source-range-c98ab3e6-01091))_
- Well, well, well. We have unwittingly reversed the list. This makes sense, if lists are constructed from back to front, and we make a linked list out of items as we iterate through it, we're going to get a backwards copy of the list. This isn't a bad thing by any stretch of the imagination. Let's call it what it is: _(javascriptallonge.pdf (source-range-c98ab3e6-01093))_
- Our mapWith function takes twice as long as a straight iteration, because it iterates over the entire list twice, once to map, and once to reverse the list. Likewise, it takes twice as much memory, because it constructs a reverse of the desired result before throwing it away. _(javascriptallonge.pdf (source-range-c98ab3e6-01095))_
- Mind you, this is still much, much faster than making partial copies of arrays. For a list of length n , wecreated n superfluous nodes and copied n superfluous values. Whereas our naïve array algorithm created 2 n superfluous arrays and copied n 2 superfluous values. _(javascriptallonge.pdf (source-range-c98ab3e6-01096))_
- So to copy a list, we have to save all the bits on the call stack and then construct the list from back-to-front as all the recursive calls return. _(javascriptallonge.pdf (source-range-c98ab3e6-01090))_
- Our mapWith function takes twice as long as a straight iteration, because it iterates over the entire list twice, once to map, and once to reverse the list. _(javascriptallonge.pdf (source-range-c98ab3e6-01095))_
- Likewise, it takes twice as much memory, because it constructs a reverse of the desired result before throwing it away. _(javascriptallonge.pdf (source-range-c98ab3e6-01095))_
- Whereas our naïve array algorithm created 2 n superfluous arrays and copied n 2 superfluous values. _(javascriptallonge.pdf (source-range-c98ab3e6-01096))_

## Technical atoms

### Technical frame 1: Plain Old JavaScript Objects / revisiting linked lists

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01085))_

> In essence, this simple implementation used functions to create an abstraction with named elements. But now that we've looked at objects, we can use an object instead of a two-element array. While we're at it, let's use contemporary names. So our linked list nodes will be formed from { first, rest }

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01084))_

<a id="atom-technical-atom-02a0b846c102558d"></a>
```
const cons = (a, d) => [a, d],
car
= ([a, d]) => a,
cdr
= ([a, d]) => d;
```

### Technical frame 2: Plain Old JavaScript Objects / revisiting linked lists

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01088))_

> What about mapping? Well, let's start with the simplest possible thing, making a copy of a list. As we saw above, and discussed in Garbage, Garbage Everywhere, it is fast to iterate forward through a linked list. What isn't fast is naïvely copying a list:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01086))_

<a id="atom-technical-atom-d9b8b52b15508a2f"></a>
```
In that case, a linked list of the numbers 1, 2, and 3 will look like this: { first: 1, rest: { first:
2, rest: { first: 3, rest: EMPTY } } }.
We can then perform the equivalent of [first, ...rest] with direct property accessors:
```

### Technical frame 3: Plain Old JavaScript Objects / revisiting linked lists

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01090))_

> The problem here is that linked lists are constructed back-to-front, but we iterate over them frontto-back. So to copy a list, we have to save all the bits on the call stack and then construct the list from back-to-front as all the recursive calls return.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01089))_

<a id="atom-technical-atom-618479c2eabba072"></a>
```
const slowcopy = (node) =>
node === EMPTY
? EMPTY
: { first: node.first, rest: slowcopy(node.rest)};
slowcopy(OneTwoThree)
//=> {"first":1,"rest":{"first":2,"rest":{"first":3,"rest":{}}}}
```
