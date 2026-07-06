---
page_id: javascriptallonge-section-composing-and-decomposing-data-defaults-and-destructuring-3d9ba8f9
page_kind: source
summary: Composing and Decomposing Data / defaults and destructuring: 3 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-composing-and-decomposing-data-defaults-and-destructuring-3d9ba8f9@8311910a650a77c3aad86ca242f201d2
---

# Composing and Decomposing Data / defaults and destructuring

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-composing-and-decomposing-data-default-arguments-d8781602]] - previous source section: Composing and Decomposing Data / default arguments

### Source structure

- [[javascriptallonge-section-composing-and-decomposing-data-d80dc70f]] - broader source section: Composing and Decomposing Data

## Statements

- Wesawearlier that destructuring parameters works the same way as destructuring assignment. Now we learn that we can create a default parameter argument. Can we create a default destructuring assignment? _(javascriptallonge.pdf (source-range-c98ab3e6-01006))_
- How very useful: defaults can be supplied for destructuring assignments, just like defaults for parameters. _(javascriptallonge.pdf (source-range-c98ab3e6-01008))_

## Technical atoms

### Technical frame 1: Composing and Decomposing Data / defaults and destructuring

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01008))_

> How very useful: defaults can be supplied for destructuring assignments, just like defaults for parameters.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01007))_

<a id="atom-technical-atom-08a4d8c2f911d51a"></a>
```
const [first, second = "two"] = ["one"];
`${first} . ${second}`
//=> "one . two"
const [first, second = "two"] = ["primus", "secundus"];
`${first} . ${second}`
//=> "primus . secundus"
```
