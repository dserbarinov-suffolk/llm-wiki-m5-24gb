---
page_id: javascriptallonge-section-plain-old-javascript-objects-destructuring-objects-6546a490
page_kind: source
summary: Plain Old JavaScript Objects / destructuring objects: 5 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-plain-old-javascript-objects-destructuring-objects-6546a490@1cb8e537d8ecc9014c73551f00a565a5
---

# Plain Old JavaScript Objects / destructuring objects

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-plain-old-javascript-objects-literal-object-syntax-41ad73a1]] - previous source section: Plain Old JavaScript Objects / literal object syntax
- [[javascriptallonge-section-plain-old-javascript-objects-revisiting-linked-lists-4e16a53d]] - next source section: Plain Old JavaScript Objects / revisiting linked lists

### Source structure

- [[javascriptallonge-section-plain-old-javascript-objects-ae9a88a3]] - broader source section: Plain Old JavaScript Objects

## Statements

- Terrible grammar and capitalization, but let's move on. It is very common to write things like title: title when destructuring objects. When the label is a valid variable name, it's often the most obvious variable name as well. So JavaScript supports a further syntactic optimization: _(javascriptallonge.pdf (source-range-c98ab3e6-01079))_

## Technical atoms

### Technical frame 1: Plain Old JavaScript Objects / destructuring objects

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01079))_

> Terrible grammar and capitalization, but let's move on. It is very common to write things like title: title when destructuring objects. When the label is a valid variable name, it's often the most obvious variable name as well. So JavaScript supports a further syntactic optimization:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01081))_

<a id="atom-technical-atom-33b47d4af6a385f1"></a>
```
const abbrev = ({name: { first, last }, occupation: { title } }) =>
return { first, last, title};
}
abbrev(user)
//=> {"first":"Reginald","last":"Braithwaite","title":"Author"}
```
