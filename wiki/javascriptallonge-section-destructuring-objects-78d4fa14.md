---
page_id: javascriptallonge-section-destructuring-objects-78d4fa14
page_kind: source
summary: destructuring objects: 7 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-destructuring-objects-78d4fa14@b1424d74aadc10a868d3c7a857a6cc3f
---

# destructuring objects

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-literal-object-syntax-71689c8a]] - previous source section: literal object syntax
- [[javascriptallonge-section-revisiting-linked-lists-9741196a]] - next source section: revisiting linked lists

## Statements

- Terrible grammar and capitalization, but let's move on. It is very common to write things like title: title when destructuring objects. When the label is a valid variable name, it's often the most obvious variable name as well. So JavaScript supports a further syntactic optimization: _(javascriptallonge.pdf (source-range-c98ab3e6-01079))_

## Technical atoms

### Technical frame 1: destructuring objects

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01079))_

> Terrible grammar and capitalization, but let's move on. It is very common to write things like title: title when destructuring objects. When the label is a valid variable name, it's often the most obvious variable name as well. So JavaScript supports a further syntactic optimization:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01075))_

<a id="atom-technical-atom-7e6f1f63a68d677c"></a>
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

### Technical frame 2: destructuring objects

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01079))_

> Terrible grammar and capitalization, but let's move on. It is very common to write things like title: title when destructuring objects. When the label is a valid variable name, it's often the most obvious variable name as well. So JavaScript supports a further syntactic optimization:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01080))_

<a id="atom-technical-atom-154953666ca27427"></a>
```
const description = ({name: { first }, occupation: { title } }) =>
`${first} is a ${title}`;
description(user)
//=> "Reginald is a Author"
And that same syntax works for literals:
const abbrev = ({name: { first, last }, occupation: { title } }) => {
```

### Technical frame 3: destructuring objects

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
