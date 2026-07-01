---
page_id: javascriptallonge-recipe-after-another-drink
page_kind: recipe
summary: after another drink: reusable source-backed pattern with 5 statement(s) and 2 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-01
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: after-another-drink
projection_coverage: recipe-javascriptallonge-recipe-after-another-drink@9f3439bc397d1288f5523b4743d390e1
---

# after another drink

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-interlude-the-carpenter-interviews-for-a-job-after-another-drink-a995f2e4]].
- Evidence roles: decision, explanation, example.

## Applicability And Rationale

- A few drinks later, The Carpenter was telling his Thing story and an engineer named Kidu introduced themself. _(javascriptallonge.pdf (source-range-0e12e052-01859))_
- I had a look at the code you left on the whiteboard. _(javascriptallonge.pdf (source-range-0e12e052-01861))_
- Whereas the problem as stated involves a single stream of directions. _(javascriptallonge.pdf (source-range-0e12e052-01862))_
- There's no benefit to constant space if finite space is sufficient. _(javascriptallonge.pdf (source-range-0e12e052-01865))_
- The Carpenter stared at Kidu's solution. _(javascriptallonge.pdf (source-range-0e12e052-01867))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-01864)_

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

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-01866)_

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

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-interlude-the-carpenter-interviews-for-a-job-after-another-drink-a995f2e4]]
