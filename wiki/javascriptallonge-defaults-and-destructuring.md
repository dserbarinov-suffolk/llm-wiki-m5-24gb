---
page_id: javascriptallonge-defaults-and-destructuring
page_kind: concept
summary: defaults and destructuring: 2 accepted assertion(s) and 1 technical atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-state-tps_08b19691583a480a@ae04c4efb98815b4e4c69ebd1ba0d392
---

# defaults and destructuring

Source: [[javascriptallonge]]

## Statements

- Now we learn that we can create a default parameter argument. (javascriptallonge.pdf p.124)
- How very useful: defaults can be supplied for destructuring assignments, just like defaults for parameters. (javascriptallonge.pdf p.125)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

```
const [first, second = "two"] = ["one"];
`${first} . ${second}`
//=> "one . two"
const [first, second = "two"] = ["primus", "secundus"];
`${first} . ${second}`
//=> "primus . secundus"
```
