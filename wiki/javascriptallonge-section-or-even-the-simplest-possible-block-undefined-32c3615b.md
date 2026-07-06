---
page_id: javascriptallonge-section-or-even-the-simplest-possible-block-undefined-32c3615b
page_kind: source
summary: Or even: / the simplest possible block / undefined: 14 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-or-even-the-simplest-possible-block-undefined-32c3615b@5be140e5dfd670ebd0281c68ef7a38c1
---

# Or even: / the simplest possible block / undefined

From [[javascriptallonge]].

## Related pages

### Source structure

- [[javascriptallonge-section-or-even-the-simplest-possible-block-cef121f0]] - broader source section: Or even: / the simplest possible block

## Statements

- In JavaScript, the absence of a value is written undefined , and it means there is no value. It will crop up again. undefined is its own type of value, and it acts like a value type: _(javascriptallonge.pdf (source-range-c98ab3e6-00219))_
- Like numbers, booleans and strings, JavaScript can print out the value undefined . _(javascriptallonge.pdf (source-range-c98ab3e6-00222))_
- No matter how you evaluate undefined , you get an identical value back. undefined is a value that means 'I don't have a value.' But it's still a value :-) _(javascriptallonge.pdf (source-range-c98ab3e6-00224))_
- 18 Sometimes, you will find JavaScript that has statements that are separated by newlines without semi-colons. This works because JavaScript has a feature that can infer where the semi-colons should be most of the time. We will not take advantage of this feature, but it's helpful to know it exists. _(javascriptallonge.pdf (source-range-c98ab3e6-00225))_
- You might think that undefined in JavaScript is equivalent to NULL in SQL. No. In SQL, two things that are NULL are not equal to nor share the same identity, because two unknowns can't be equal. In JavaScript, every undefined is identical to every other undefined . _(javascriptallonge.pdf (source-range-c98ab3e6-00226))_
- In JavaScript, the absence of a value is written undefined , and it means there is no value. _(javascriptallonge.pdf (source-range-c98ab3e6-00219))_
- This works because JavaScript has a feature that can infer where the semi-colons should be most of the time. _(javascriptallonge.pdf (source-range-c98ab3e6-00225))_
- In SQL, two things that are NULL are not equal to nor share the same identity, because two unknowns can't be equal. _(javascriptallonge.pdf (source-range-c98ab3e6-00226))_

## Technical atoms

### Technical frame 1: Or even: / the simplest possible block / undefined

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00222))_

> Like numbers, booleans and strings, JavaScript can print out the value undefined .

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00220))_

<a id="atom-technical-atom-d59974f2bc22234d"></a>
```
undefined
```

### Technical frame 2: Or even: / the simplest possible block / undefined

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00222))_

> Like numbers, booleans and strings, JavaScript can print out the value undefined .

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00221))_

<a id="atom-technical-atom-d3afeb023ecd949a"></a>
```
//=> undefined
```

### Technical frame 3: Or even: / the simplest possible block / undefined

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00224))_

> No matter how you evaluate undefined , you get an identical value back. undefined is a value that means 'I don't have a value.' But it's still a value :-)

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00223))_

<a id="atom-technical-atom-5a32c82afb1975e9"></a>
```
undefined === undefined
//=> true
(() => {})() === (() => {})()
//=> true
(() => {})() === undefined
//=> true
```
