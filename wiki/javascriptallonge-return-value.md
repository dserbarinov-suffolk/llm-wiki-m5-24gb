---
page_id: javascriptallonge-return-value
page_kind: concept
summary: Return Value: 0 statement(s) and 1 atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-return-value@4eac32e38f9a2544f83ae4eaffb2c317
---

# Return Value

What [[javascriptallonge]] covers about return value:

## Statements


## Technical atoms

### Technical atom 1

<a id="atom-technical-atom-7e25061238cfb4ee"></a>

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00851))_

> Some languages support multiple return values: A function can return several things at once, like a value and an error code. This can easily be emulated in JavaScript with destructuring:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00852))_

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

### Shared technical atoms

- [[javascriptallonge-destructuring]] - shared technical atoms: Destructuring shares technical record from Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring and return values: const description = (nameAndOccupation) => { if (nameAndOccupation.length < 2) { return ["", "occupation missing"] } else { const [[first, last], occupation] = nameA ... [truncated] (1 shared atom(s))

## Source

- [[javascriptallonge]]
