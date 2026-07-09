---
page_id: javascriptallonge-copy-on-write
page_kind: concept
summary: Copy on Write: 13 accepted assertion(s) and 6 technical atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-state-tps_85d58aa32836779c@92ef0c23283f910681701113663f9838
---

# Copy on Write

Source: [[javascriptallonge]]

## Statements

- We've seen how to build lists with arrays and with linked lists. (javascriptallonge.pdf p.158)
- When you take the rest of an array with destructuring ( [first, ..rest] ), you are given a copy of the elements of the array. (javascriptallonge.pdf p.158)
- When you take the rest of a linked list with its reference, you are given the exact same nodes of the elements of the original list. (javascriptallonge.pdf p.158)
- And therefore, modifications to the parent do not affect the child, and modifications to the child do not affect the parent. (javascriptallonge.pdf p.158)
- If we know that a list doesn't share any elements with another list, we can safely modify it. (javascriptallonge.pdf p.159)
- We'll end up reinventing reference counting and garbage collection. (javascriptallonge.pdf p.159)
- But our new parent and child lists are copies that contain the desired modifications, without interfering with each other:. (javascriptallonge.pdf p.162)
- And now functions like mapWith that make copies without modifying anything, work at full speed. (javascriptallonge.pdf p.162)
- This strategy of waiting to copy until you are writing is called copy-on-write, or 'COW:'. (javascriptallonge.pdf p.162)
- Copy-on-write is the name given to the policy that whenever a task attempts to make a change to the shared information, it should first create a separate (private) copy of that information to prevent its changes from becoming visible to all the other tasks.Wikipedia 73. (javascriptallonge.pdf p.163)
- Like all strategies, it makes a tradeoff: It's much cheaper than pessimistically copying structures when you make an infrequent number of small changes, but if you tend to make a lot of changes to some that you aren't sharing, it's more expensive. (javascriptallonge.pdf p.163)
- Once we're done with it and give it to someone else, we need to be conservative and use a strategy like copy-on-read or copy-on-write. (javascriptallonge.pdf p.163)
- Looking at the code again, you see that the copy function doesn't copy on write: It follows the pattern that while constructing something, we own it and can be liberal with mutation. (javascriptallonge.pdf p.163)

## Technical atoms

<a id="atom-1"></a>
**Atom:** rule

```
The consequence of this is that if you have an array, and you take it's 'rest,' your 'child' array is a copy of the elements of the parent array.
```

<a id="atom-2"></a>
**Atom:** rule

```
Whereas if you have a linked list, and you take it's 'rest,' your 'child' list shares its nodes with the 'parent' list.
```

<a id="atom-3"></a>
**Atom:** code block

```
const parentArray = [1, 2, 3];
const [aFirst, ...childArray] = parentArray;
parentArray[2] = "three";
childArray[0] = "two";
parentArray
//=> [1,2,"three"]
childArray
//=> ["two",3]
const EMPTY = { first: {}, rest: {} };
const parentList = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY }\
}};
const childList = parentList.rest;
parentList.rest.rest.first = "three";
childList.first = "two";
parentList
//=> {"first":1,"rest":{"first":"two","rest":{"first":"three","rest":{"first":\
{},"rest":{}}}}}
childList
//=> {"first":"two","rest":{"first":"three","rest":{"first":{},"rest":{}}}}
```

<a id="atom-4"></a>
**Atom:** code block

```
const rest = ({first, rest}) => rest;
const set = (index, value, list) =>
index === 0
? { first: value, rest: list.rest }
: { first: list.first, rest: set(index - 1, value, list.rest) };
const parentList = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY }\
}};
const childList = rest(parentList);
const newParentList = set(2, "three", parentList);
const newChildList = set(0, "two", childList);
```

<a id="atom-5"></a>
**Atom:** code block

```
parentList
//=> {"first":1,"rest":{"first":2,"rest":{"first":3,"rest":{"first":{},"rest":\
{}}}}}
childList
//=> {"first":2,"rest":{"first":3,"rest":{"first":{},"rest":{}}}}
```

<a id="atom-6"></a>
**Atom:** code block

```
newParentList
//=> {"first":1,"rest":{"first":2,"rest":{"first":"three","rest":{"first":{},"\
rest":{}}}}}
newChildList
//=> {"first":"two","rest":{"first":3,"rest":{"first":{},"rest":{}}}}
```
