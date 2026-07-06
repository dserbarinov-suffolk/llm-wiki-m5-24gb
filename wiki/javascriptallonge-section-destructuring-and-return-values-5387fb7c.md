---
page_id: javascriptallonge-section-destructuring-and-return-values-5387fb7c
page_kind: source
summary: destructuring and return values: 1 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-destructuring-and-return-values-5387fb7c@ac2adfd97e198c66bff78a64c278b642
---

# destructuring and return values

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-destructuring-is-not-pattern-matching-385525f3]] - previous source section: destructuring is not pattern matching
- [[javascriptallonge-section-destructuring-parameters-e2eab6f1]] - next source section: destructuring parameters

## Technical atoms

### Technical frame 1: destructuring and return values

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00852))_

<a id="atom-technical-atom-7e25061238cfb4ee"></a>
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
