---
page_id: javascriptallonge-mixing
page_kind: concept
summary: Mixing: 0 statement(s) and 1 atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-mixing@a7757754774892a92c0663c509bfc160
---

# Mixing

What [[javascriptallonge]] covers about mixing:

## Statements


## Technical atoms

### Technical frame 1: Reassignment / mixing let and const

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01178))_

> Shadowing a let with a const does not change our ability to rebind the variable in its original scope. And:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01177))_

<a id="atom-technical-atom-6a4dfd38d219fc66"></a>
```
(() => {
let age = 49;
if (true) {
const age = 50;
}
age = 51;
return age;
})()
//=> 51
```


## Related pages

### Shared technical atoms

- [[javascriptallonge-const]] - shared technical atoms: Const shares technical record from Reassignment / mixing let and const: (() => { let age = 49; if (true) { const age = 50; } age = 51; return age; })() //=> 51 (1 shared atom(s))

## Source

- [[javascriptallonge]]
