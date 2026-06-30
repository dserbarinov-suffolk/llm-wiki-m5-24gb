---
page_id: javascriptallonge-section-plain-old-javascript-objects-destructuring-objects-233d242e
page_kind: source
summary: Plain Old JavaScript Objects / destructuring objects: 7 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-06-30
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-plain-old-javascript-objects-destructuring-objects-233d242e@b79b3c1d58efb30220270b3e1e9f7cfe
---

# Plain Old JavaScript Objects / destructuring objects

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-plain-old-javascript-objects-79315aff]] - broader source section: Plain Old JavaScript Objects
- [[javascriptallonge-section-plain-old-javascript-objects-literal-object-syntax-25e0b081]] - previous source section: Plain Old JavaScript Objects / literal object syntax
- [[javascriptallonge-section-plain-old-javascript-objects-revisiting-linked-lists-23e98a21]] - next source section: Plain Old JavaScript Objects / revisiting linked lists

## Statements

- Terrible grammar and capitalization, but let's move on. It is very common to write things like title: title when destructuring objects. When the label is a valid variable name, it's often the most obvious variable name as well. So JavaScript supports a further syntactic optimization: _(javascriptallonge.pdf (source-range-0e12e052-01095))_

## Technical atoms

### Technical frame 1: Plain Old JavaScript Objects / destructuring objects

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01095))_

> Terrible grammar and capitalization, but let's move on. It is very common to write things like title: title when destructuring objects. When the label is a valid variable name, it's often the most obvious variable name as well. So JavaScript supports a further syntactic optimization:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01091))_

```
const user = {
name: { first: "Reginald",
last: "Braithwaite"
},
occupation: { title: "Author",
responsibilities: [ "JavaScript Allongé",
"JavaScript Spessore",
"CoffeeScript Ristretto"
]
}
};
user.name.last
//=> "Braithwaite"
user.occupation.title
//=> "Author"
And we can also write:
const {name: { first: given, last: surname}, occupation: { title: title }
er;
surname
//=> "Braithwaite"
title
//=> "Author"
```

### Technical frame 2: Plain Old JavaScript Objects / destructuring objects

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01095))_

> Terrible grammar and capitalization, but let's move on. It is very common to write things like title: title when destructuring objects. When the label is a valid variable name, it's often the most obvious variable name as well. So JavaScript supports a further syntactic optimization:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01096))_

```
const description = ({name: { first }, occupation: { title } }) =>
`${first} is a ${title}`;
description(user)
//=> "Reginald is a Author"
And that same syntax works for literals:
const abbrev = ({name: { first, last }, occupation: { title } }) => {
```

### Technical frame 3: Plain Old JavaScript Objects / destructuring objects

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01095))_

> Terrible grammar and capitalization, but let's move on. It is very common to write things like title: title when destructuring objects. When the label is a valid variable name, it's often the most obvious variable name as well. So JavaScript supports a further syntactic optimization:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01097))_

```
const abbrev = ({name: { first, last }, occupation: { title } }) =>
return { first, last, title};
}
abbrev(user)
//=> {"first":"Reginald","last":"Braithwaite","title":"Author"}
```
