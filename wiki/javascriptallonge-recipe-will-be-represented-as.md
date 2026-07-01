---
page_id: javascriptallonge-recipe-will-be-represented-as
page_kind: recipe
summary: Will be represented as: reusable source-backed pattern with 2 statement(s) and 3 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-01
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: will-be-represented-as
projection_coverage: recipe-javascriptallonge-recipe-will-be-represented-as@0d6e43a2e45a82110ebe92eb9eff8750
---

# Will be represented as

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-interactive-generators-representing-naughts-and-crosses-as-a-stateless-function-will-be-represen-f1dabfc6]].
- Evidence roles: decision, constraint, example.

## Applicability And Rationale

- We'll use the [] notation for keys, it allows us to use any expression as a key, and JavaScript will convert it to a string. _(javascriptallonge.pdf (source-range-0e12e052-01908))_
- We can use a POJO to make a map from positions to moves. _(javascriptallonge.pdf (source-range-0e12e052-01908))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-01907)_

```
[
'o', 'x', ' ',
'x', ' ', ' ',
'o', ' ', ' '
]
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-01909)_

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

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-01910)_

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

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-interactive-generators-representing-naughts-and-crosses-as-a-stateless-function-will-be-represen-f1dabfc6]]
