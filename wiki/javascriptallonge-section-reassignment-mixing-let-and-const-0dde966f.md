---
page_id: javascriptallonge-section-reassignment-mixing-let-and-const-0dde966f
page_kind: source
summary: Reassignment / mixing let and const: 6 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-reassignment-mixing-let-and-const-0dde966f@ee00b1e6eca41f983f9c4533b02842c4
---

# Reassignment / mixing let and const

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-reassignment-why-const-and-let-were-invented-cf53c7fd]] - next source section: Reassignment / why const and let were invented

### Source structure

- [[javascriptallonge-section-reassignment-c80c0ca4]] - broader source section: Reassignment
- [[javascriptallonge-section-reassignment-mixing-let-and-const-var-65ff1805]] - narrower source section: Reassignment / mixing let and const / var

## Statements

- Some programmers dislike deliberately shadowing variables. The suggestion is that shadowing a variable is confusing code. If you buy that argument, the way that shadowing works in JavaScript exists to protect us from accidentally shadowing a variable when we move code around. _(javascriptallonge.pdf (source-range-c98ab3e6-01156))_
- Shadowing a let with a const does not change our ability to rebind the variable in its original scope. And: _(javascriptallonge.pdf (source-range-c98ab3e6-01159))_
- Shadowing a const with a let does not permit it to be rebound in its original scope. _(javascriptallonge.pdf (source-range-c98ab3e6-01161))_

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
