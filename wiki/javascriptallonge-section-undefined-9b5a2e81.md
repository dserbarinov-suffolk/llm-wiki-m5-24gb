---
page_id: javascriptallonge-section-undefined-9b5a2e81
page_kind: source
summary: undefined: 14 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-undefined-9b5a2e81@347985c6d70a96857d39f66c2aeb10df
---

# undefined

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-the-simplest-possible-block-5da702d2]] - previous source section: the simplest possible block
- [[javascriptallonge-section-void-c67a822d]] - next source section: void

## Statements

- In JavaScript, the absence of a value is written undefined , and it means there is no value. It will crop up again. undefined is its own type of value, and it acts like a value type: _(javascriptallonge.pdf (source-range-c98ab3e6-00211))_
- Like numbers, booleans and strings, JavaScript can print out the value undefined . _(javascriptallonge.pdf (source-range-c98ab3e6-00214))_
- No matter how you evaluate undefined , you get an identical value back. undefined is a value that means 'I don't have a value.' But it's still a value :-) _(javascriptallonge.pdf (source-range-c98ab3e6-00216))_
- 18 Sometimes, you will find JavaScript that has statements that are separated by newlines without semi-colons. This works because JavaScript has a feature that can infer where the semi-colons should be most of the time. We will not take advantage of this feature, but it's helpful to know it exists. _(javascriptallonge.pdf (source-range-c98ab3e6-00217))_
- You might think that undefined in JavaScript is equivalent to NULL in SQL. No. In SQL, two things that are NULL are not equal to nor share the same identity, because two unknowns can't be equal. In JavaScript, every undefined is identical to every other undefined . _(javascriptallonge.pdf (source-range-c98ab3e6-00218))_
- In JavaScript, the absence of a value is written undefined , and it means there is no value. _(javascriptallonge.pdf (source-range-c98ab3e6-00211))_
- This works because JavaScript has a feature that can infer where the semi-colons should be most of the time. _(javascriptallonge.pdf (source-range-c98ab3e6-00217))_
- In SQL, two things that are NULL are not equal to nor share the same identity, because two unknowns can't be equal. _(javascriptallonge.pdf (source-range-c98ab3e6-00218))_

## Technical atoms

### Technical frame 1: undefined

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00214))_

> Like numbers, booleans and strings, JavaScript can print out the value undefined .

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00212))_

<a id="atom-technical-atom-62b489c3348a33a0"></a>
```
undefined
```

### Technical frame 2: undefined

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00214))_

> Like numbers, booleans and strings, JavaScript can print out the value undefined .

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00213))_

<a id="atom-technical-atom-d7f4dab15ef86a18"></a>
```
//=> undefined
```

### Technical frame 3: undefined

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00216))_

> No matter how you evaluate undefined , you get an identical value back. undefined is a value that means 'I don't have a value.' But it's still a value :-)

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00215))_

<a id="atom-technical-atom-68dc26441ffd855a"></a>
```
undefined === undefined
//=> true
(() => {})() === (() => {})()
//=> true
(() => {})() === undefined
//=> true
```
