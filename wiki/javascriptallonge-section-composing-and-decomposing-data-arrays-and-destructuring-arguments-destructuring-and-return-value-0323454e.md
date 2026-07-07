---
page_id: javascriptallonge-section-composing-and-decomposing-data-arrays-and-destructuring-arguments-destructuring-and-return-value-0323454e
page_kind: source
summary: Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring and return values: 1 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-composing-and-decomposing-data-arrays-and-destructuring-arguments-destructuring-and-return-value-0323454e@d1be300a8a1f99cfb6243684c7dbd27d
---

# Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring and return values

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-composing-and-decomposing-data-arrays-and-destructuring-arguments-destructuring-is-not-pattern-m-27d4b226]] - previous source section: Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring is not pattern matching
- [[javascriptallonge-section-composing-and-decomposing-data-arrays-and-destructuring-arguments-destructuring-parameters-1a788a19]] - next source section: Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring parameters

### Source structure

- [[javascriptallonge-section-composing-and-decomposing-data-arrays-and-destructuring-arguments-2a38bfc8]] - broader source section: Composing and Decomposing Data / Arrays and Destructuring Arguments

## Technical atoms

### Technical frame 1: Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring and return values

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
