---
page_id: javascriptallonge-section-plain-old-javascript-objects-literal-object-syntax-41ad73a1
page_kind: source
summary: Plain Old JavaScript Objects / literal object syntax: 19 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-plain-old-javascript-objects-literal-object-syntax-41ad73a1@110ae55a2472d3163d00e2bd0af8ecfd
---

# Plain Old JavaScript Objects / literal object syntax

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-plain-old-javascript-objects-destructuring-objects-6546a490]] - next source section: Plain Old JavaScript Objects / destructuring objects

### Source structure

- [[javascriptallonge-section-plain-old-javascript-objects-ae9a88a3]] - broader source section: Plain Old JavaScript Objects

### Recipes

- [[javascriptallonge-recipe-literal-object-syntax]] - recipe pattern: literal object syntax

## Statements

- JavaScript has a literal syntax for creating objects. This object maps values to the keys year , month , and day : _(javascriptallonge.pdf (source-range-c98ab3e6-01052))_
- Two objects created with separate evaluations have differing identities, just like arrays: _(javascriptallonge.pdf (source-range-c98ab3e6-01054))_
- Values contained within an object work just like values contained within an array, we access them by reference to the original: _(javascriptallonge.pdf (source-range-c98ab3e6-01056))_
- Names needn't be alphanumeric strings. For anything else, enclose the label in quotes: _(javascriptallonge.pdf (source-range-c98ab3e6-01058))_
- If the name is an alphanumeric string conforming to the same rules as names of variables, there's a simplified syntax for accessing the values: _(javascriptallonge.pdf (source-range-c98ab3e6-01060))_
- Expressions can be used for keys as well. The syntax is to enclose the key's expression in [ and ] : _(javascriptallonge.pdf (source-range-c98ab3e6-01062))_
- It is very common to associate named function expressions with keys in objects, and there is a 'compact method syntax' for binding named function expressions to keywords: _(javascriptallonge.pdf (source-range-c98ab3e6-01070))_
- (There are some other technical differences between binding a named function expression and using compact method syntax, but they are not relevant here. We will generally prefer compact method syntax whenever we can.) _(javascriptallonge.pdf (source-range-c98ab3e6-01072))_
- Values contained within an object work just like values contained within an array, we access them by reference to the original: _(javascriptallonge.pdf (source-range-c98ab3e6-01056))_

## Technical atoms

### Technical frame 1: Plain Old JavaScript Objects / literal object syntax

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01054))_

> Two objects created with separate evaluations have differing identities, just like arrays:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01053))_

<a id="atom-technical-atom-86ff9c88f6398559"></a>
```
{ year: 2012, month: 6, day: 14 }
```

### Technical frame 2: Plain Old JavaScript Objects / literal object syntax

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01072))_

> (There are some other technical differences between binding a named function expression and using compact method syntax, but they are not relevant here. We will generally prefer compact method syntax whenever we can.)

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01071))_

<a id="atom-technical-atom-5fc0450b87f8fabc"></a>
```
const SecretDecoderRing = {
encode (plaintext) {
return plaintext
.split('')
.map( char => char.charCodeAt() )
.map( code => code + 1 )
.map( code => String.fromCharCode(code) )
.join('');
},
decode (cyphertext) {
return cyphertext
.split('')
.map( char => char.charCodeAt() )
.map( code => code - 1 )
.map( code => String.fromCharCode(code) )
.join('');
}
}
```
