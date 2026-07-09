---
page_id: javascriptallonge-destructuring
page_kind: concept
summary: Destructuring: 1 statement(s) and 2 atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-destructuring@8bde1b18fc2653b06f76f8cfbcbb4725
---

# Destructuring

What [[javascriptallonge]] covers about destructuring:

## Statements

### Composing and Decomposing Data / defaults and destructuring

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

### Technical atom 2

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

### Source structure

- [[javascriptallonge-section-composing-and-decomposing-data-arrays-and-destructuring-arguments-2a38bfc8]] - source section: Composing and Decomposing Data / Arrays and Destructuring Arguments
- [[javascriptallonge-section-composing-and-decomposing-data-arrays-and-destructuring-arguments-array-literals-f2f1b6ec]] - source section: Composing and Decomposing Data / Arrays and Destructuring Arguments / array literals
- [[javascriptallonge-section-composing-and-decomposing-data-arrays-and-destructuring-arguments-destructuring-and-return-value-0323454e]] - source section: Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring and return values
- [[javascriptallonge-section-composing-and-decomposing-data-arrays-and-destructuring-arguments-destructuring-arrays-327f6ba9]] - source section: Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring arrays
- [[javascriptallonge-section-composing-and-decomposing-data-arrays-and-destructuring-arguments-destructuring-is-not-pattern-m-27d4b226]] - source section: Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring is not pattern matching
- [[javascriptallonge-section-composing-and-decomposing-data-arrays-and-destructuring-arguments-destructuring-parameters-1a788a19]] - source section: Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring parameters
- [[javascriptallonge-section-composing-and-decomposing-data-arrays-and-destructuring-arguments-element-references-75756e27]] - source section: Composing and Decomposing Data / Arrays and Destructuring Arguments / element references
- [[javascriptallonge-section-composing-and-decomposing-data-arrays-and-destructuring-arguments-gathering-1b2d594b]] - source section: Composing and Decomposing Data / Arrays and Destructuring Arguments / gathering

### Shared technical atoms

- [[javascriptallonge-default]] - shared statements and technical atoms: Default shares source evidence from Composing and Decomposing Data / defaults and destructuring: How very useful: defaults can be supplied for destructuring assignments, just like defaults for parameters.; Default shares technical record from Composing and Decomposing Data / defaults and destructuring: const [first, second = "two"] = ["one"]; `${first} . ${second}` //=> "one . two" const [first, second = "two"] = ["primus", "secundus"]; `${first} . ${second}` //=> ... [truncated] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-return-value]] - shared technical atoms: Return Value shares technical record from Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring and return values: const description = (nameAndOccupation) => { if (nameAndOccupation.length < 2) { return ["", "occupation missing"] } else { const [[first, last], occupation] = nameA ... [truncated] (1 shared atom(s))

## Source

- [[javascriptallonge]]
