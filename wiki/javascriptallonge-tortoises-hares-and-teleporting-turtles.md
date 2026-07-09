---
page_id: javascriptallonge-tortoises-hares-and-teleporting-turtles
page_kind: concept
summary: topic-concept: 11 supported fragment(s) and 1 related link(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: page-projection-pgp_438e8869869f9f26@241e5708f7f463d17ef283cf919ef9f9
---

# Tortoises, Hares, and Teleporting Turtles

Source: [[javascriptallonge]]

## Statements

- It was , 'Write an algorithm to detect a loop in a linked list, in constant space.'. (javascriptallonge.pdf p.164)
- This is the 'trick answer' to a question about finding a missing integer from a list, so I was trying the old, 'Transform this into a problem you've already solved 74 ' meta-algorithm. (javascriptallonge.pdf p.164)
- Eventually, I came up with something and tried it (In Java!) on my home PC. (javascriptallonge.pdf p.164)
- No matter how large it is , you will eventually have the fast reference equal to the slow reference, and thus you'll detect the loop. (javascriptallonge.pdf p.165)
- You have two node references, and one traverses the list at twice the speed of the other. (javascriptallonge.pdf p.165)
- It seems to be faster under certain circumstances, depending on the size of the loop and the relative costs of certain operations. (javascriptallonge.pdf p.166)
- What's interesting about these two algorithms is that they both tangle two separate concerns: How to traverse a data structure, and what to do with the elements that you encounter. (javascriptallonge.pdf p.166)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

```
const EMPTY = null;
const isEmpty = (node) => node === EMPTY;
const pair = (first, rest = EMPTY) => ({first, rest});
const list = (...elements) => {
const [first, ...rest] = elements;
return elements.length === 0
? EMPTY
: pair(first, list(...rest))
}
const forceAppend = (list1, list2) => {
if (isEmpty(list1)) {
return "FAIL!"
}
if (isEmpty(list1.rest)) {
list1.rest = list2;
}
else {
forceAppend(list1.rest, list2);
```

<a id="atom-2"></a>
**Atom:** code block

```
}
}
const tortoiseAndHare = (aPair) => {
let tortoisePair = aPair,
harePair = aPair.rest;
while (true) {
if (isEmpty(tortoisePair) || isEmpty(harePair)) {
return false;
}
if (tortoisePair.first === harePair.first) {
return true;
}
harePair = harePair.rest;
if (isEmpty(harePair)) {
return false;
}
if (tortoisePair.first === harePair.first) {
return true;
}
tortoisePair = tortoisePair.rest;
harePair = harePair.rest;
}
};
const aList = list(1, 2, 3, 4, 5);
tortoiseAndHare(aList)
//=> false
forceAppend(aList, aList.rest.rest);
tortoiseAndHare(aList);
//=> true
```

<a id="atom-3"></a>
**Atom:** code block

```
const teleportingTurtle = (list) => {
let speed = 1,
rabbit = list,
turtle = rabbit;
while (true) {
for (let i = 0; i <= speed; i += 1) {
rabbit = rabbit.rest;
if (rabbit == null) {
return false;
}
if (rabbit === turtle) {
return true;
}
}
turtle = rabbit;
speed *= 2;
}
return false;
};
const aList = list(1, 2, 3, 4, 5);
teleportingTurtle(aList)
//=> false
forceAppend(aList, aList.rest.rest);
teleportingTurtle(aList);
//=> true
```


## Related pages

- [[javascriptallonge-functional-iterators]] - contextualizes: source-supported topic dependency
