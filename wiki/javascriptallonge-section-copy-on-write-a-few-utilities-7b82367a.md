---
page_id: javascriptallonge-section-copy-on-write-a-few-utilities-7b82367a
page_kind: source
summary: Copy on Write / a few utilities: 3 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-copy-on-write-a-few-utilities-7b82367a@570df870d145cee08edd84c32193a7d3
---

# Copy on Write / a few utilities

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-copy-on-write-tortoises-hares-and-teleporting-turtles-3a4746f2]] - next source section: Copy on Write / Tortoises, Hares, and Teleporting Turtles

### Source structure

- [[javascriptallonge-section-copy-on-write-d081f846]] - broader source section: Copy on Write
- [[javascriptallonge-section-copy-on-write-a-few-utilities-copy-on-read-2d301e7a]] - narrower source section: Copy on Write / a few utilities / copy-on-read
- [[javascriptallonge-section-copy-on-write-a-few-utilities-copy-on-write-db9192e0]] - narrower source section: Copy on Write / a few utilities / copy-on-write

## Statements

- Our new at and set functions behave similarly to array[index] and array[index] = value . The main difference is that array[index] = value evaluates to value , while set(index, value, list) evaluates to the modified list . _(javascriptallonge.pdf (source-range-c98ab3e6-01212))_

## Technical atoms

### Technical frame 1: Copy on Write / a few utilities

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01212))_

> Our new at and set functions behave similarly to array[index] and array[index] = value . The main difference is that array[index] = value evaluates to value , while set(index, value, list) evaluates to the modified list .

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01210))_

<a id="atom-technical-atom-9cde04494d451288"></a>
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
const first = ({first, rest}) => first;
const rest = ({first, rest}) => rest;
const reverse = (node, delayed = EMPTY) =>
node === EMPTY
? delayed
: reverse(rest(node), { first: first(node), rest: delayed });
const mapWith = (fn, node, delayed = EMPTY) =>
node === EMPTY
? reverse(delayed)
: mapWith(fn, rest(node), { first: fn(first(node)), rest: delayed });
const at = (index, list) =>
index === 0
? first(list)
: at(index - 1, rest(list));
const set = (index, value, list, originalList = list) =>
index === 0
? (list.first = value, originalList)
: set(index - 1, value, rest(list), originalList)
const parentList = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY }\
}};
```

### Technical frame 2: Copy on Write / a few utilities

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01212))_

> Our new at and set functions behave similarly to array[index] and array[index] = value . The main difference is that array[index] = value evaluates to value , while set(index, value, list) evaluates to the modified list .

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01211))_

<a id="atom-technical-atom-9fe6e0881f198a76"></a>
```
const childList = rest(parentList);
set(2, "three", parentList);
set(0, "two", childList);
parentList
//=> {"first":1,"rest":{"first":"two","rest":{"first":"three","rest":{"first":\
{},"rest":{}}}}}
childList
//=> {"first":"two","rest":{"first":"three","rest":{"first":{},"rest":{}}}}
```
