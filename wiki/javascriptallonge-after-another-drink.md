---
page_id: javascriptallonge-after-another-drink
page_kind: concept
summary: after another drink: 5 accepted assertion(s) and 2 technical atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-state-tps_a1cdeadf39520512@61674958e211dff58557ae210fa390ee
---

# after another drink

Source: [[javascriptallonge]]

## Statements

- A few drinks later, The Carpenter was telling his Thing story and an engineer named Kidu introduced themself. (javascriptallonge.pdf p.270)
- I had a look at the code you left on the whiteboard. (javascriptallonge.pdf p.271)
- Whereas the problem as stated involves a single stream of directions. (javascriptallonge.pdf p.271)
- There's no benefit to constant space if finite space is sufficient. (javascriptallonge.pdf p.271)
- The Carpenter stared at Kidu's solution. (javascriptallonge.pdf p.272)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

```
// implements Teleporting Tortoise
// cycle detection algorithm.
const hasCycle = (iterable) => {
let iterator = iterable[Symbol.iterator](),
teleportDistance = 1;
while (true) {
let {value, done} = iterator.next(),
tortoise = value;
if (done) return false;
for (let i = 0; i < teleportDistance; ++i) {
let {value, done} = iterator.next(),
hare = value;
if (done) return false;
if (tortoise === hare) return true;
}
teleportDistance *= 2;
}
return false;
};
```

<a id="atom-2"></a>
**Atom:** code block

```
const hasCycle = (orderedCollection) => {
const visited = new Set();
for (let element of orderedCollection) {
if (visited.has(element)) {
return true;
}
visited.add(element);
}
return false;
};
```
