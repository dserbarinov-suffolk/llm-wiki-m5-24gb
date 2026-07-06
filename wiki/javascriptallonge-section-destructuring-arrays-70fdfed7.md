---
page_id: javascriptallonge-section-destructuring-arrays-70fdfed7
page_kind: source
summary: destructuring arrays: 10 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-destructuring-arrays-70fdfed7@8f4d1b154637fe6b9a532d32a62b77d3
---

# destructuring arrays

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-element-references-3e80b0bf]] - previous source section: element references
- [[javascriptallonge-section-gathering-5b2815df]] - next source section: gathering

## Statements

- There is another way to extract elements from arrays: Destructuring , a feature going back to Common Lisp, if not before. We saw how to construct an array literal using [ , expressions, , and ] . Here's an example of an array literal that uses a name: _(javascriptallonge.pdf (source-range-c98ab3e6-00821))_
- The line const wrapped = [something]; is interesting. On the left hand is a name to be bound, and on the right hand is an array literal, a template for constructing an array, very much like a quasi-literal string. _(javascriptallonge.pdf (source-range-c98ab3e6-00824))_
- The statement const [something] = wrapped; destructures the array represented by wrapped , binding the value of its single element to the name something . We can do the same thing with more than one element: _(javascriptallonge.pdf (source-range-c98ab3e6-00827))_
- We could do the same thing with (name) => name[1] , but destructuring is code that resembles the data it consumes, a valuable coding style. _(javascriptallonge.pdf (source-range-c98ab3e6-00829))_
- There is another way to extract elements from arrays: Destructuring , a feature going back to Common Lisp, if not before. _(javascriptallonge.pdf (source-range-c98ab3e6-00821))_

## Technical atoms

### Technical frame 1: destructuring arrays

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00824))_

> The line const wrapped = [something]; is interesting. On the left hand is a name to be bound, and on the right hand is an array literal, a template for constructing an array, very much like a quasi-literal string.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00822))_

<a id="atom-technical-atom-46a5553e38af2bb2"></a>
```
const wrap = (something) => [something];
Let’s expand it to use a block and an extra name:
const wrap = (something) => {
const wrapped = [something];
```

### Technical frame 2: destructuring arrays

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00824))_

> The line const wrapped = [something]; is interesting. On the left hand is a name to be bound, and on the right hand is an array literal, a template for constructing an array, very much like a quasi-literal string.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00823))_

<a id="atom-technical-atom-74c0e617f7101462"></a>
```
const wrap = (something) => {
const wrapped = [something]
return wrapped;
}
wrap("package")
//=> ["package"]
```
