---
page_id: javascriptallonge-section-copy-on-write-a-few-utilities-copy-on-read-3e3c1bfb
page_kind: source
summary: Copy on Write / a few utilities / copy-on-read: 10 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-06-30
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-copy-on-write-a-few-utilities-copy-on-read-3e3c1bfb@b1f40c4c90e00cdcfb142ca9a3abf037
---

# Copy on Write / a few utilities / copy-on-read

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-copy-on-write-a-few-utilities-31a03dc1]] - broader source section: Copy on Write / a few utilities
- [[javascriptallonge-section-copy-on-write-a-few-utilities-copy-on-write-09152c57]] - next source section: Copy on Write / a few utilities / copy-on-write

## Statements

- So back to the problem of structure sharing. One strategy for avoiding problems is to be pessimistic . Whenever we take the rest of a list, make a copy. _(javascriptallonge.pdf (source-range-0e12e052-01234))_
- This strategy is called 'copy-on-read', because when we attempt the parent to 'read' the value of a child of the list, we make a copy and read the copy of the child. Thereafter, we can write to the parent or the copy of the child freely. _(javascriptallonge.pdf (source-range-0e12e052-01236))_
- As we expected, making a copy lets us modify the copy without interfering with the original. This is, however, expensive. Sometimes we don't need to make a copy because we won't be modifying the list. Our mapWith function would be very expensive if we make a copy every time we call rest(node) . _(javascriptallonge.pdf (source-range-0e12e052-01237))_
- This strategy is called 'copy-on-read', because when we attempt the parent to 'read' the value of a child of the list, we make a copy and read the copy of the child. _(javascriptallonge.pdf (source-range-0e12e052-01236))_
- Sometimes we don't need to make a copy because we won't be modifying the list. _(javascriptallonge.pdf (source-range-0e12e052-01237))_

## Technical atoms

### Technical frame 1: Copy on Write / a few utilities / copy-on-read

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01236))_

> This strategy is called 'copy-on-read', because when we attempt the parent to 'read' the value of a child of the list, we make a copy and read the copy of the child. Thereafter, we can write to the parent or the copy of the child freely.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01235))_

```
const rest = ({first, rest}) => copy(rest);
const parentList = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY }\
}};
const childList = rest(parentList);
const newParentList = set(2, "three", parentList);
set(0, "two", childList);
parentList
//=> {"first":1,"rest":{"first":2,"rest":{"first":"three","rest":{"first":{},"\
rest":{}}}}}
childList
//=> {"first":"two","rest":{"first":3,"rest":{"first":{},"rest":{}}}}
```
