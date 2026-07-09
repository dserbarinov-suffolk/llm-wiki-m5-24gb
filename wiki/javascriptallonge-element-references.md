---
page_id: javascriptallonge-element-references
page_kind: concept
summary: element references: 3 accepted assertion(s) and 2 technical atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-state-tps_0add072eaef8fa80@52fa50b62968dff978e3fde3fc5b2962
---

# element references

Source: [[javascriptallonge]]

## Statements

- Array elements can be extracted using [ and ] as postfix operators. (javascriptallonge.pdf p.102)
- As we can see, JavaScript Arrays are zero-based 56 . (javascriptallonge.pdf p.102)
- We know that every array is its own unique entity, with its own unique reference. (javascriptallonge.pdf p.102)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

```
const oneTwoThree = ["one", "two", "three"];
oneTwoThree[0]
//=> 'one'
oneTwoThree[1]
//=> 'two'
oneTwoThree[2]
//=> 'three'
```

<a id="atom-2"></a>
**Atom:** code block

```
const x = [],
a = [x];
a[0] === x
//=> true, arrays store references to the things you put in them.
```
