---
page_id: javascriptallonge-section-composing-and-decomposing-data-defaults-and-destructuring-960d8813
page_kind: source
summary: Composing and Decomposing Data / defaults and destructuring: 3 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-composing-and-decomposing-data-defaults-and-destructuring-960d8813@c0391cec83fcf894cff4b433326d5176
---

# Composing and Decomposing Data / defaults and destructuring

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-composing-and-decomposing-data-default-arguments-363804ac]] - previous source section: Composing and Decomposing Data / default arguments

### Source structure

- [[javascriptallonge-section-composing-and-decomposing-data-99b4771a]] - broader source section: Composing and Decomposing Data

### Recipes

- [[javascriptallonge-recipe-defaults-and-destructuring]] - recipe pattern: defaults and destructuring

## Statements

- Wesawearlier that destructuring parameters works the same way as destructuring assignment. Now we learn that we can create a default parameter argument. Can we create a default destructuring assignment? _(javascriptallonge.pdf (source-range-c98ab3e6-00992))_
- How very useful: defaults can be supplied for destructuring assignments, just like defaults for parameters. _(javascriptallonge.pdf (source-range-c98ab3e6-00994))_

## Technical atoms

### Technical frame 1: Composing and Decomposing Data / defaults and destructuring

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00994))_

> How very useful: defaults can be supplied for destructuring assignments, just like defaults for parameters.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00993))_

<a id="atom-technical-atom-a4a5e6bc581b11af"></a>
```
const [first, second = "two"] = ["one"];
`${first} . ${second}`
//=> "one . two"
const [first, second = "two"] = ["primus", "secundus"];
`${first} . ${second}`
//=> "primus . secundus"
```
