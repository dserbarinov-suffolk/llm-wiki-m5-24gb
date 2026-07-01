---
page_id: javascriptallonge-return-value
page_kind: concept
summary: Return Value: 0 statement(s) and 1 atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-01
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-return-value@f4e3a8255c2208604175d88314d0d51f
---

# Return Value

What [[javascriptallonge]] covers about return value:

## Statements


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


## Related pages

- [[javascriptallonge-destructuring]] - shared technical atoms: Destructuring shares technical record from Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring and return values: const description = (nameAndOccupation) => { if (nameAndOccupation.length < 2) { return ["", "occupation missing"] } else { const [[first, last], occupation] = nameA ... [truncated] (1 shared atom(s))

## Source

- [[javascriptallonge]]
