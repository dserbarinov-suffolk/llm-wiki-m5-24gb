---
page_id: javascriptallonge-recipe-back-on-the-block
page_kind: recipe
summary: back on the block: reusable source-backed pattern with 5 statement(s) and 3 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: back-on-the-block
projection_coverage: recipe-javascriptallonge-recipe-back-on-the-block@153a06acb2a35eb8e2408ff81ce60f71
---

# back on the block

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-or-even-back-on-the-block-b65a6ef3]].
- Evidence roles: decision, constraint, structured-state, example.

## Applicability And Rationale

- We haven't discussed these statements . _(javascriptallonge.pdf (source-range-0e12e052-00240))_
- Although they aren't very practical, these are valid JavaScript functions, and they return undefined when applied: _(javascriptallonge.pdf (source-range-0e12e052-00241))_
- There are many kinds of JavaScript statements, but the first kind is one we've already met. _(javascriptallonge.pdf (source-range-0e12e052-00241))_
- As we saw with commas above, we can rearrange these functions onto multiple lines when we feel its more readable that way: _(javascriptallonge.pdf (source-range-0e12e052-00243))_
- But no matter how we arrange them, a block with one or more expressions still evaluates to undefined : _(javascriptallonge.pdf (source-range-0e12e052-00245))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-00237)_

```
(() => {})()
//=> undefined
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-00242)_

```
() => { 2 + 2 }
() => { 1 + 1; 2 + 2 }
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-00244)_

```
() => {
1 + 1;
2 + 2
}
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-or-even-back-on-the-block-b65a6ef3]]
