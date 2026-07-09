---
page_id: javascriptallonge-destructuring-objects
page_kind: concept
summary: destructuring objects: 2 accepted assertion(s) and 5 technical atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-state-tps_17b2512bda8273dd@10611f9906d0bad25136fa055bed8fa6
---

# destructuring objects

Source: [[javascriptallonge]]

## Statements

- When the label is a valid variable name, it's often the most obvious variable name as well. (javascriptallonge.pdf p.137)
- It is very common to write things like title: title when destructuring objects. (javascriptallonge.pdf p.137)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

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

<a id="atom-2"></a>
**Atom:** code block

```
} = us\
```

<a id="atom-3"></a>
**Atom:** code block

```
const description = ({name: { first: given }, occupation: { title: title } }) =>
`${given} is a ${title}`;
description(user)
//=> "Reginald is a Author"
```

<a id="atom-4"></a>
**Atom:** code block

```
const description = ({name: { first }, occupation: { title } }) =>
`${first} is a ${title}`;
description(user)
//=> "Reginald is a Author"
And that same syntax works for literals:
const abbrev = ({name: { first, last }, occupation: { title } }) => {
```

<a id="atom-5"></a>
**Atom:** code block

```
const abbrev = ({name: { first, last }, occupation: { title } }) =>
return { first, last, title};
}
abbrev(user)
//=> {"first":"Reginald","last":"Braithwaite","title":"Author"}
```
