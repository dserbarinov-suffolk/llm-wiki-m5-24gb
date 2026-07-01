---
page_id: javascriptallonge-recipe-copy-on-read
page_kind: recipe
summary: copy-on-read: reusable source-backed pattern with 7 statement(s) and 1 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-01
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: copy-on-read
projection_coverage: recipe-javascriptallonge-recipe-copy-on-read@5808207839e067c1c5634eca69103e68
---

# copy-on-read

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-copy-on-write-a-few-utilities-copy-on-read-3e3c1bfb]].
- Evidence roles: decision, constraint, explanation, example.

## Applicability And Rationale

- Whenever we take the rest of a list, make a copy. _(javascriptallonge.pdf (source-range-0e12e052-01234))_
- One strategy for avoiding problems is to be pessimistic . _(javascriptallonge.pdf (source-range-0e12e052-01234))_
- Thereafter, we can write to the parent or the copy of the child freely. _(javascriptallonge.pdf (source-range-0e12e052-01236))_
- This strategy is called 'copy-on-read', because when we attempt the parent to 'read' the value of a child of the list, we make a copy and read the copy of the child. _(javascriptallonge.pdf (source-range-0e12e052-01236))_
- As we expected, making a copy lets us modify the copy without interfering with the original. _(javascriptallonge.pdf (source-range-0e12e052-01237))_
- Sometimes we don't need to make a copy because we won't be modifying the list. _(javascriptallonge.pdf (source-range-0e12e052-01237))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-01235)_

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

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-copy-on-write-a-few-utilities-copy-on-read-3e3c1bfb]]
