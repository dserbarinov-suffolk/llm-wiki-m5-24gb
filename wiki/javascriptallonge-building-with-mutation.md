---
page_id: javascriptallonge-building-with-mutation
page_kind: concept
summary: building with mutation: 5 accepted assertion(s) and 4 technical atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-state-tps_9e39a792c9d5948e@cb53e3be7d04c9949c9cea666ad89486
---

# building with mutation

Source: [[javascriptallonge]]

## Statements

- As noted , one pattern is to be more liberal about mutation when building a data structure. (javascriptallonge.pdf p.145)
- If we want to make a copy of a linked list without iterating over it twice and making a copy we discard later, we can use mutation:. (javascriptallonge.pdf p.145)
- This algorithm makes copies of nodes as it goes, and mutates the last node in the list so that it can splice the next one on. (javascriptallonge.pdf p.146)
- Adding a node to an existing list is risky, as we saw when considering the fact that OneToFive and ThreeToFive share the same nodes. (javascriptallonge.pdf p.146)
- But when we're in the midst of creating a brand new list, we aren't sharing any nodes with any other lists, and we can afford to be more liberal about using mutation to save space and/or time. (javascriptallonge.pdf p.146)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

```
const reverse = (node, delayed = EMPTY) =>
node === EMPTY
? delayed
: reverse(node.rest, { first: node.first, rest: delayed });
const copy = (node) => reverse(reverse(node));
```

<a id="atom-2"></a>
**Atom:** code block

```
const copy = (node, head = null, tail = null) => {
if (node === EMPTY) {
return head;
}
else if (tail === null) {
const { first, rest } = node;
const newNode = { first, rest };
return copy(rest, newNode, newNode);
}
else {
const { first, rest } = node;
const newNode = { first, rest };
tail.rest = newNode;
return copy(node.rest, head, newNode);
}
}
```

<a id="atom-3"></a>
**Atom:** code block

```
const mapWith = (fn, node, head = null, tail = null) => {
if (node === EMPTY) {
return head;
}
else if (tail === null) {
const { first, rest } = node;
const newNode = { first: fn(first), rest };
return mapWith(fn, rest, newNode, newNode);
}
else {
const { first, rest } = node;
const newNode = { first: fn(first), rest };
tail.rest = newNode;
return mapWith(fn, node.rest, head, newNode);
}
}
mapWith((x) => 1.0 / x, OneToFive)
```

<a id="atom-4"></a>
**Atom:** code block

```
//=> {"first":1,"rest":{"first":0.5,"rest":{"first":0.3333333333333333,"rest":\
{"first":0.25,"rest":{"first":0.2,"rest":{}}}}}}
```
