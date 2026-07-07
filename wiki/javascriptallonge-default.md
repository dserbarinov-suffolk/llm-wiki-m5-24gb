---
page_id: javascriptallonge-default
page_kind: concept
summary: Default: 2 statement(s) and 1 atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-default@2cf3d216c538978c7c163118440b24fb
---

# Default

What [[javascriptallonge]] covers about default:

## Statements

### Composing and Decomposing Data / defaults and destructuring

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


## Related pages

### Shared technical atoms

- [[javascriptallonge-destructuring]] - shared statements and technical atoms: Destructuring shares source evidence from Composing and Decomposing Data / defaults and destructuring: How very useful: defaults can be supplied for destructuring assignments, just like defaults for parameters.; Destructuring shares technical record from Composing and Decomposing Data / defaults and destructuring: const [first, second = "two"] = ["one"]; `${first} . ${second}` //=> "one . two" const [first, second = "two"] = ["primus", "secundus"]; `${first} . ${second}` //=> ... [truncated] (1 shared statement(s), 1 shared atom(s))

## Source

- [[javascriptallonge]]
