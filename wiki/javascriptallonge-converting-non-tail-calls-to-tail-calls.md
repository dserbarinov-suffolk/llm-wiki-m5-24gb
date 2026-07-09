---
page_id: javascriptallonge-converting-non-tail-calls-to-tail-calls
page_kind: concept
summary: topic-concept: 9 supported fragment(s) and 1 related link(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: page-projection-pgp_b8f1ad994a687215@f1fb35457ec0b82ee8afae137ceb379c
---

# converting non-tail-calls to tail-calls

Source: [[javascriptallonge]]

## Procedure

- The obvious solution is push the 1 + work into the call to length . (javascriptallonge.pdf p.120)
- Now that we've seen how it works, we can clean up the 0 + numberToBeAdded business. (javascriptallonge.pdf p.120)
- This version of length calls uses lengthDelaysWork , and JavaScript optimizes that not to take up memory proportional to the length of the string. (javascriptallonge.pdf p.120)
- We can map over large arrays without incurring all the memory and performance overhead of non-tail-calls. (javascriptallonge.pdf p.121)
- And this basic transformation from a recursive function that does not make a tail call, into a recursive function that calls itself in tail position, is a bread-and-butter pattern for programmers using a language that incorporates tail-call optimization. (javascriptallonge.pdf p.121)

## Required tables and formulas

<a id="atom-1"></a>
**Atom:** table

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


## Rules and exceptions

- Now that we've seen how it works, we can clean up the 0 + numberToBeAdded business. (javascriptallonge.pdf p.120)
- We can map over large arrays without incurring all the memory and performance overhead of non-tail-calls. (javascriptallonge.pdf p.121)

## Related pages

- [[javascriptallonge-tail-call-optimization]] - contextualizes: source-supported topic dependency
