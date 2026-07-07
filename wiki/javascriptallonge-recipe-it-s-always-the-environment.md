---
page_id: javascriptallonge-recipe-it-s-always-the-environment
page_kind: recipe
summary: it's always the environment: reusable source-backed pattern with 11 statement(s) and 4 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: it-s-always-the-environment
projection_coverage: recipe-javascriptallonge-recipe-it-s-always-the-environment@e10ddb4a88376a0d0852b7cad20c73ad
---

# it's always the environment

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-it-s-always-the-environment-ff95f958]].
- Evidence roles: decision, explanation, constraint, structured-state, example.

## Applicability And Rationale

- As we've said before, all functions are associated with an environment. _(javascriptallonge.pdf (source-range-c98ab3e6-00340))_
- To understand how closures are evaluated, we need to revisit environments. _(javascriptallonge.pdf (source-range-c98ab3e6-00340))_
- We also hand-waved something when describing our environment. _(javascriptallonge.pdf (source-range-c98ab3e6-00340))_
- Some people get so excited by this that they write entire books about them, some are great a , some-how shall I put this-are interesting b if you use Ruby. _(javascriptallonge.pdf (source-range-c98ab3e6-00343))_
- (x) => x is called the I Combinator, or the Identity Function . _(javascriptallonge.pdf (source-range-c98ab3e6-00343))_
- (x) => (y) => x is called the K Combinator, or Kestrel . _(javascriptallonge.pdf (source-range-c98ab3e6-00343))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00345)_

```
bh
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00347)_

```
(x) =>
(y) =>
(z) => x + y + z
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00349)_

```
(x, y, z) => x + y + z
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00352)_

```
ah
bh
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-it-s-always-the-environment-ff95f958]]
