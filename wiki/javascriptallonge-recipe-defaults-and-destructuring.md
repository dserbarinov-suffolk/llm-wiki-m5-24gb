---
page_id: javascriptallonge-recipe-defaults-and-destructuring
page_kind: recipe
summary: defaults and destructuring: reusable source-backed pattern with 2 statement(s) and 1 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: defaults-and-destructuring
projection_coverage: recipe-javascriptallonge-recipe-defaults-and-destructuring@3c980a7b887ad11a9d7387016cfdef99
---

# defaults and destructuring

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-composing-and-decomposing-data-defaults-and-destructuring-cd5ea708]].
- Evidence roles: decision, constraint, example.

## Applicability And Rationale

- Now we learn that we can create a default parameter argument. _(javascriptallonge.pdf (source-range-0e12e052-01006))_
- How very useful: defaults can be supplied for destructuring assignments, just like defaults for parameters. _(javascriptallonge.pdf (source-range-0e12e052-01008))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-01007)_

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
- Source section: [[javascriptallonge-section-composing-and-decomposing-data-defaults-and-destructuring-cd5ea708]]
