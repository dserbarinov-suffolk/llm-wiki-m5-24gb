---
page_id: javascriptallonge-defaults-and-destructuring
page_kind: concept
summary: topic-concept: 6 supported fragment(s) and 1 related link(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: page-projection-pgp_20d67b664b4699ee@38270d748a79fdbde6188289aa17b87b
---

# defaults and destructuring

Source: [[javascriptallonge]]

## Statements

- Now we learn that we can create a default parameter argument. (javascriptallonge.pdf p.124)
- How very useful: defaults can be supplied for destructuring assignments, just like defaults for parameters. (javascriptallonge.pdf p.125)

## Rules

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


## Related pages

- [[javascriptallonge-default-arguments]] - contextualizes: source-supported topic dependency
