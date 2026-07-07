---
page_id: javascriptallonge-mixing
page_kind: concept
summary: Mixing: 0 statement(s) and 1 atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-mixing@a22c6448915d9d22ebda496a1fa3e6c1
---

# Mixing

What [[javascriptallonge]] covers about mixing:

## Statements


## Technical atoms

### Technical frame 1: Reassignment / mixing let and const

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01159))_

> Shadowing a let with a const does not change our ability to rebind the variable in its original scope. And:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01158))_

<a id="atom-technical-atom-73fcad6cbcb4f1b0"></a>
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

### Source structure

- [[javascriptallonge-section-reassignment-mixing-let-and-const-0dde966f]] - source section: Reassignment / mixing let and const
- [[javascriptallonge-section-reassignment-mixing-let-and-const-var-65ff1805]] - source section: Reassignment / mixing let and const / var

### Shared technical atoms

- [[javascriptallonge-const]] - shared technical atoms: Const shares technical record from Reassignment / mixing let and const: (() => { let age = 49; if (true) { const age = 50; } age = 51; return age; })() //=> 51 (1 shared atom(s))

## Source

- [[javascriptallonge]]
