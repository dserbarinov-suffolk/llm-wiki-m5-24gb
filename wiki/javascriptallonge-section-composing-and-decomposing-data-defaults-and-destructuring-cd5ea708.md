---
page_id: javascriptallonge-section-composing-and-decomposing-data-defaults-and-destructuring-cd5ea708
page_kind: source
summary: Composing and Decomposing Data / defaults and destructuring: 3 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-06-30
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-composing-and-decomposing-data-defaults-and-destructuring-cd5ea708@7eb831832d56b9e51fd457c152c0e455
---

# Composing and Decomposing Data / defaults and destructuring

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-composing-and-decomposing-data-58c1e32b]] - broader source section: Composing and Decomposing Data
- [[javascriptallonge-section-composing-and-decomposing-data-default-arguments-870cb490]] - previous source section: Composing and Decomposing Data / default arguments

## Statements

- Wesawearlier that destructuring parameters works the same way as destructuring assignment. Now we learn that we can create a default parameter argument. Can we create a default destructuring assignment? _(javascriptallonge.pdf (source-range-0e12e052-01006))_
- How very useful: defaults can be supplied for destructuring assignments, just like defaults for parameters. _(javascriptallonge.pdf (source-range-0e12e052-01008))_

## Technical atoms

### Technical frame 1: Composing and Decomposing Data / defaults and destructuring

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01008))_

> How very useful: defaults can be supplied for destructuring assignments, just like defaults for parameters.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01007))_

```
const [first, second = "two"] = ["one"];
`${first} . ${second}`
//=> "one . two"
const [first, second = "two"] = ["primus", "secundus"];
`${first} . ${second}`
//=> "primus . secundus"
```
