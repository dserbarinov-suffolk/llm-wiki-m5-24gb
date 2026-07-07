---
page_id: javascriptallonge-section-composing-and-decomposing-data-99b4771a
page_kind: source
summary: Composing and Decomposing Data: 1 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-composing-and-decomposing-data-99b4771a@da38756c24ce28ab83e95dc92a932b63
---

# Composing and Decomposing Data

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-picking-the-bean-choice-and-truthiness-d2a76f30]] - previous source section: Picking the Bean: Choice and Truthiness
- [[javascriptallonge-section-garbage-garbage-everywhere-8c9764a5]] - next source section: Garbage, Garbage Everywhere

### Source structure

- [[javascriptallonge-section-composing-and-decomposing-data-arrays-and-destructuring-arguments-2a38bfc8]] - narrower source section: Composing and Decomposing Data / Arrays and Destructuring Arguments
- [[javascriptallonge-section-composing-and-decomposing-data-default-arguments-363804ac]] - narrower source section: Composing and Decomposing Data / default arguments
- [[javascriptallonge-section-composing-and-decomposing-data-defaults-and-destructuring-960d8813]] - narrower source section: Composing and Decomposing Data / defaults and destructuring
- [[javascriptallonge-section-composing-and-decomposing-data-factorials-4b205fe1]] - narrower source section: Composing and Decomposing Data / factorials
- [[javascriptallonge-section-composing-and-decomposing-data-self-similarity-ea23a471]] - narrower source section: Composing and Decomposing Data / Self-Similarity
- [[javascriptallonge-section-composing-and-decomposing-data-tail-calls-and-default-arguments-b4311a56]] - narrower source section: Composing and Decomposing Data / Tail Calls (and Default Arguments)

## Statements

- Recursion is the root of computation since it trades description for time.-Alan Perlis, Epigrams in Programming 55 _(javascriptallonge.pdf (source-range-c98ab3e6-00795))_

## Technical atoms

### Technical frame 1: Composing and Decomposing Data / Arrays and Destructuring Arguments / gathering

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00833))_

> Sometimes we need to extract arrays from arrays. Here is the most common pattern: Extracting the head and gathering everything but the head from an array:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00837))_

<a id="atom-technical-atom-5337ddc45c7cfcfe"></a>
```text
57 https://en.wikipedia.org/wiki/CAR_and_CDR
58 Kyle Simpson is the author of You Don't Know JS, available here
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 57 | https://en.wikipedia.org/wiki/CAR_and_CDR |
| 58 | Kyle Simpson is the author of You Don't Know JS, available here |

</details>

### Technical frame 2: Composing and Decomposing Data / Tail Calls (and Default Arguments) / converting non-tail-calls to tail-calls

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00967))_

> Brilliant! We can map over large arrays without incurring all the memory and performance overhead of non-tail-calls. And this basic transformation from a recursive function that does not make a tail call, into a recursive function that calls itself in tail position, is a bread-and-butter pattern for programmers using a language that incorporates tail-call optimization.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00966))_

<a id="atom-technical-atom-3439b2237aced771"></a>
| 0, | 1, | 2, | 3, | 4, | 5, | 6, | 7, | 8, | 9, |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 10, | 11, | 12, | 13, | 14, | 15, | 16, | 17, | 18, | 19, |
| 20, | 21, | 22, | 23, | 24, | 25, | 26, | 27, | 28, | 29, |
| 30, | 31, | 32, | 33, | 34, | 35, | 36, | 37, | 38, | 39, |
| 40, | 41, | 42, | 43, | 44, | 45, | 46, | 47, | 48, | 49, |
| 50, | 51, | 52, | 53, | 54, | 55, | 56, | 57, | 58, | 59, |
| 60, | 61, | 62, | 63, | 64, | 65, | 66, | 67, | 68, | 69, |
| 70, | 71, | 72, | 73, | 74, | 75, | 76, | 77, | 78, | 79, |
| 80, | 81, | 82, | 83, | 84, | 85, | 86, | 87, | 88, | 89, |
| 90, | 91, | 92, | 93, | 94, | 95, | 96, | 97, | 98, | 99, |

<details>
<summary>Raw table text</summary>

```text
converting non-tail-calls to tail-calls
| 0, | 1, | 2, | 3, | 4, | 5, | 6, | 7, | 8, | 9, |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 10, | 11, | 12, | 13, | 14, | 15, | 16, | 17, | 18, | 19, |
| 20, | 21, | 22, | 23, | 24, | 25, | 26, | 27, | 28, | 29, |
| 30, | 31, | 32, | 33, | 34, | 35, | 36, | 37, | 38, | 39, |
| 40, | 41, | 42, | 43, | 44, | 45, | 46, | 47, | 48, | 49, |
| 50, | 51, | 52, | 53, | 54, | 55, | 56, | 57, | 58, | 59, |
| 60, | 61, | 62, | 63, | 64, | 65, | 66, | 67, | 68, | 69, |
| 70, | 71, | 72, | 73, | 74, | 75, | 76, | 77, | 78, | 79, |
| 80, | 81, | 82, | 83, | 84, | 85, | 86, | 87, | 88, | 89, |
| 90, | 91, | 92, | 93, | 94, | 95, | 96, | 97, | 98, | 99, |
```

</details>
