---
page_id: coding-learn-go-with-tests-excerpt-section-pointers-copies-et-al-70ac4baf
page_kind: source
summary: Pointers, copies, et al: 9 source-backed entries and 4 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-pointers-copies-et-al-70ac4baf@228a82a80ede00a4377211950c30415c
---

# Pointers, copies, et al

From [[coding-learn-go-with-tests-excerpt]].

## Statements

- An interesting property of maps is that you can modify them without passing as an address to it (e.g &myMap ) _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00605))_
- So when you pass a map to a function/method, you are indeed copying it, but just the pointer part, not the underlying data structure that contains the data. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00608))_
- A gotcha with maps is that they can be a nil value. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00609))_
- You can read more about maps here. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00609))_
- Instead, you can initialize an empty map or use the make keyword to create a map for you: _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00612))_

## Technical atoms

```
A	map	value	is	a	pointer	to	a	runtime.hmap	structure.
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00607))_

```
var m map [string]string
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00611))_

```
var dictionary	= map [string]string{} //	OR var dictionary	=	make( map [string]string)
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00613))_

> Which ensures that you will never get a runtime panic.
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00614))_
