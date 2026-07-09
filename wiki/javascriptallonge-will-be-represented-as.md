---
page_id: javascriptallonge-will-be-represented-as
page_kind: concept
summary: Will be represented as:: 2 accepted assertion(s) and 3 technical atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-state-tps_477a01be997a831c@f7d387b52f70de0bf451f1a6bac1c577
---

# Will be represented as:

Source: [[javascriptallonge]]

## Statements

- We'll use the [] notation for keys, it allows us to use any expression as a key, and JavaScript will convert it to a string. (javascriptallonge.pdf p.277)
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
