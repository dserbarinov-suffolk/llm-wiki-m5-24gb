---
page_id: coding-learn-go-with-tests-excerpt-section-refactor-de84fbe5
page_kind: source
summary: Refactor: 5 source-backed entries and 2 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-refactor-de84fbe5@396c83bf80416b40815bc5029db578e2
---

# Refactor

From [[coding-learn-go-with-tests-excerpt]].

## Statements

- Again, the implementation is fine but our tests could do with some improvement. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00514))_
- It's not immediately clear what all the numbers represent and you should be aiming for your tests to be easily understood. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00517))_
- Now our tests - rather, the list of test cases - make assertions of truth about shapes and their areas. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00524))_

## Technical atoms

```
{Rectangle{12,	6},	72.0}, {Circle{10},	314.1592653589793}, {Triangle{12,	6},	36.0},
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00516))_

```
{shape:	Rectangle{Width:	12,	Height:	6},	want:	72.0}, {shape:	Circle{Radius:	10},	want:	314.1592653589793}, {shape:	Triangle{Base:	12,	Height:	6},	want:	36.0},
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00520))_
