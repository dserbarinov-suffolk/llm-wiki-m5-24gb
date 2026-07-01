---
page_id: javascriptallonge-destructuring
page_kind: concept
summary: Destructuring: 1 statement(s) and 2 atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-01
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-destructuring@af29e376210ddfb269eeab40270f1f83
---

# Destructuring

What [[javascriptallonge]] covers about destructuring:

## Statements

### Composing and Decomposing Data / defaults and destructuring

- How very useful: defaults can be supplied for destructuring assignments, just like defaults for parameters. _(javascriptallonge.pdf (source-range-0e12e052-01008))_


## Technical atoms

### Technical frame 1: Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring and return values

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00866))_

```
const description = (nameAndOccupation) => {
if (nameAndOccupation.length < 2) {
return ["", "occupation missing"]
}
else {
const [[first, last], occupation] = nameAndOccupation;
return [`${first} is a ${occupation}`, "ok"];
}
}
const [reg, status] = description([["Reginald", "Braithwaite"], "programmer"]);
reg
//=> "Reginald is a programmer"
status
//=> "ok"
```

### Technical frame 2: Composing and Decomposing Data / defaults and destructuring

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


## Related pages

- [[javascriptallonge-default]] - shared statements and technical atoms: Default shares source evidence from Composing and Decomposing Data / defaults and destructuring: How very useful: defaults can be supplied for destructuring assignments, just like defaults for parameters.; Default shares technical record from Composing and Decomposing Data / defaults and destructuring: const [first, second = "two"] = ["one"]; `${first} . ${second}` //=> "one . two" const [first, second = "two"] = ["primus", "secundus"]; `${first} . ${second}` //=> ... [truncated] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-return-value]] - shared technical atoms: Return Value shares technical record from Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring and return values: const description = (nameAndOccupation) => { if (nameAndOccupation.length < 2) { return ["", "occupation missing"] } else { const [[first, last], occupation] = nameA ... [truncated] (1 shared atom(s))

## Source

- [[javascriptallonge]]
