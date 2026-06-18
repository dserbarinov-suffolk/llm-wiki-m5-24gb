---
category: source
summary: Self-Similarity from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.109-125
updated: 2026-06-18
domain: javascriptallonge
category_path: source-sections
source_id: javascriptallonge.pdf
---

## Self-Similarity

In *JavaScript Allongé*, the concept of **self-similarity** is explored through recursion and the manipulation of arrays using destructuring and spreads. This idea is rooted in the recursive definition of a list, which can be either:

1. Empty (`[]`), or
2. An element concatenated with a list (`[e, ...list]`).

This parallels the use of array literals and destructuring assignments to compose and decompose data structures. For example:

- Building a list: `[
