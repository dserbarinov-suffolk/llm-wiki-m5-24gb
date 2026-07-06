---
page_id: javascriptallonge-recipe-defaults-and-destructuring
page_kind: recipe
summary: defaults and destructuring: reusable source-backed pattern with 2 statement(s) and 1 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: defaults-and-destructuring
projection_coverage: recipe-javascriptallonge-recipe-defaults-and-destructuring@5f2284eccceb2d2bc3ed3600f6382e9c
---

# defaults and destructuring

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-composing-and-decomposing-data-defaults-and-destructuring-3d9ba8f9]].
- Evidence roles: decision, constraint, example.

## Applicability And Rationale

- Now we learn that we can create a default parameter argument. _(javascriptallonge.pdf (source-range-c98ab3e6-01006))_
- How very useful: defaults can be supplied for destructuring assignments, just like defaults for parameters. _(javascriptallonge.pdf (source-range-c98ab3e6-01008))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01007)_

```
const [first, second = "two"] = ["one"];
`${first} . ${second}`
//=> "one . two"
const [first, second = "two"] = ["primus", "secundus"];
`${first} . ${second}`
//=> "primus . secundus"
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-composing-and-decomposing-data-defaults-and-destructuring-3d9ba8f9]]
