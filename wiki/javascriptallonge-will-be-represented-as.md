---
page_id: javascriptallonge-will-be-represented-as
page_kind: concept
summary: topic-concept: 6 supported fragment(s) and 0 related link(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: page-projection-pgp_f717e332bdf3d1de@ef3060b832d9b255d22d5724408ab53c
---

# Will be represented as:

Source: [[javascriptallonge]]

## Statements

- We'll use the [] notation for keys, it allows us to use any expression as a key, and JavaScript will convert it to a string. (javascriptallonge.pdf p.277)
- We can use a POJO to make a map from positions to moves. (javascriptallonge.pdf p.277)

## Rules

- We can use a POJO to make a map from positions to moves. (javascriptallonge.pdf p.277)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

```
[
'o', 'x', ' ',
'x', ' ', ' ',
'o', ' ', ' '
]
```

<a id="atom-2"></a>
**Atom:** code block

```
const moveLookupTable = {
[[
' ', ' ', ' ',
' ', ' ', ' ',
' ', ' ', ' '
]]: 0,
[[
'o', 'x', ' ',
' ', ' ', ' ',
' ', ' ', ' '
]]: 6,
[[
'o', 'x', 'x',
' ', ' ', ' ',
'o', ' ', ' '
]]: 3,
[[
'o', 'x', ' ',
'x', ' ', ' ',
'o', ' ', ' '
]]: 8,
[[
'o', 'x', ' ',
' ', 'x', ' ',
'o', ' ', ' '
```

<a id="atom-3"></a>
**Atom:** code block

```
]]: 3,
[[
'o', 'x', ' ',
' ', ' ', 'x',
'o', ' ', ' '
]]: 3,
[[
'o', 'x', ' ',
' ', ' ', ' ',
'o', 'x', ' '
]]: 3,
[[
'o', 'x', ' ',
' ', ' ', ' ',
'o', ' ', 'x'
]]: 3
// ...
};
```
