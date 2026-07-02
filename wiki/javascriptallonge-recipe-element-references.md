---
page_id: javascriptallonge-recipe-element-references
page_kind: recipe
summary: element references: reusable source-backed pattern with 3 statement(s) and 2 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: element-references
projection_coverage: recipe-javascriptallonge-recipe-element-references@433f44c460158ccf0f2d52ec4406f262
---

# element references

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-composing-and-decomposing-data-arrays-and-destructuring-arguments-element-references-24b6e6cb]].
- Evidence roles: decision, constraint, procedure, example.

## Applicability And Rationale

- Array elements can be extracted using [ and ] as postfix operators. _(javascriptallonge.pdf (source-range-0e12e052-00828))_
- As we can see, JavaScript Arrays are zero-based 56 . _(javascriptallonge.pdf (source-range-0e12e052-00830))_
- We know that every array is its own unique entity, with its own unique reference. _(javascriptallonge.pdf (source-range-0e12e052-00831))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-00829)_

```
const oneTwoThree = ["one", "two", "three"];
oneTwoThree[0]
//=> 'one'
oneTwoThree[1]
//=> 'two'
oneTwoThree[2]
//=> 'three'
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-00833)_

```
const x = [],
a = [x];
a[0] === x
//=> true, arrays store references to the things you put in them.
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-composing-and-decomposing-data-arrays-and-destructuring-arguments-element-references-24b6e6cb]]
