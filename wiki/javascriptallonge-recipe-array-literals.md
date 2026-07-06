---
page_id: javascriptallonge-recipe-array-literals
page_kind: recipe
summary: array literals: reusable source-backed pattern with 5 statement(s) and 6 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: array-literals
projection_coverage: recipe-javascriptallonge-recipe-array-literals@c9bb06f9596f21c11148d38e145e5770
---

# array literals

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-composing-and-decomposing-data-arrays-and-destructuring-arguments-array-literals-e663df80]].
- Evidence roles: decision, definition, procedure, explanation, constraint, example.

## Applicability And Rationale

- JavaScript has a literal syntax for creating an array: The [ and ] characters. _(javascriptallonge.pdf (source-range-c98ab3e6-00814))_
- Although that seems like something nobody would ever construct, many students have worked with almost the exact same thing when they explored various means of constructing arithmetic from Set Theory. _(javascriptallonge.pdf (source-range-c98ab3e6-00822))_
- This is an array with one element that is an array with one element that is an array with one element that is an array with one element that is an empty array. _(javascriptallonge.pdf (source-range-c98ab3e6-00822))_
- Array literals are expressions, and arrays are reference types . _(javascriptallonge.pdf (source-range-c98ab3e6-00825))_
- We can see that each time an array literal is evaluated, we get a new, distinct array, even if it contains the exact same elements: _(javascriptallonge.pdf (source-range-c98ab3e6-00825))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00815)_

```
[]
//=> []
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00817)_

```
[1]
//=> [1]
[2, 3, 4]
//=> [2,3,4]
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00819)_

```
[ 2,
3,
2 + 2
]
//=> [2,3,4]
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00821)_

```
[[[[[]]]]]
```

### Atom 5: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00824)_

```
const wrap = (something) => [something];
wrap("lunch")
//=> ["lunch"]
```

### Atom 6: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00826)_

```
[] === []
//=> false
[2 + 2] === [2 + 2]
//=> false
const array_of_one = () => [1];
array_of_one() === array_of_one()
//=> false
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-composing-and-decomposing-data-arrays-and-destructuring-arguments-array-literals-e663df80]]
