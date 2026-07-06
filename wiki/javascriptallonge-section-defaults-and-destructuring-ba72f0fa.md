---
page_id: javascriptallonge-section-defaults-and-destructuring-ba72f0fa
page_kind: source
summary: defaults and destructuring: 3 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-defaults-and-destructuring-ba72f0fa@5e69b1b7f465dfd21e7f9684d79737d4
---

# defaults and destructuring

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-default-arguments-53255884]] - previous source section: default arguments
- [[javascriptallonge-section-garbage-garbage-everywhere-8c9764a5]] - next source section: Garbage, Garbage Everywhere

## Statements

- Wesawearlier that destructuring parameters works the same way as destructuring assignment. Now we learn that we can create a default parameter argument. Can we create a default destructuring assignment? _(javascriptallonge.pdf (source-range-c98ab3e6-00992))_
- How very useful: defaults can be supplied for destructuring assignments, just like defaults for parameters. _(javascriptallonge.pdf (source-range-c98ab3e6-00994))_

## Technical atoms

### Technical frame 1: defaults and destructuring

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
