---
page_id: javascriptallonge-copy-on-read
page_kind: concept
summary: copy-on-read: 7 accepted assertion(s) and 1 technical atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-state-tps_c07144304dbbacde@976445a1ea6c2152fd93c9f9cc88df56
---

# copy-on-read

Source: [[javascriptallonge]]

## Statements

- Whenever we take the rest of a list, make a copy. (javascriptallonge.pdf p.161)
- One strategy for avoiding problems is to be pessimistic . (javascriptallonge.pdf p.161)
- Thereafter, we can write to the parent or the copy of the child freely. (javascriptallonge.pdf p.161)
- This strategy is called 'copy-on-read', because when we attempt the parent to 'read' the value of a child of the list, we make a copy and read the copy of the child. (javascriptallonge.pdf p.161)
- Sometimes we don't need to make a copy because we won't be modifying the list. (javascriptallonge.pdf p.161)
- As we expected , making a copy lets us modify the copy without interfering with the original. (javascriptallonge.pdf p.161)
- Our mapWith function would be very expensive if we make a copy every time we call rest(node) . (javascriptallonge.pdf p.161)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

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
