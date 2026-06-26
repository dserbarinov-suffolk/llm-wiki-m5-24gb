---
page_id: coding-learn-go-with-tests-excerpt-pointer-copy
page_kind: concept
summary: Pointers, copies, et al: 5 statement(s) and 4 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-pointer-copy@9dcbeca0ebc5155dfc5e22c57c302059
---

# Pointers, copies, et al

What [[coding-learn-go-with-tests-excerpt]] covers about pointers, copies, et al:

## Statements

- So when you pass a map to a function/method, you are indeed copying it, but just the pointer part, not the underlying data structure that contains the data. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00608))_
- An interesting property of maps is that you can modify them without passing as an address to it (e.g &myMap ) _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00605))_
- You can read more about maps here. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00609))_
- A gotcha with maps is that they can be a nil value. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00609))_
- Instead, you can initialize an empty map or use the make keyword to create a map for you: _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00612))_

## Technical atoms

> Context: This may make them feel like a "reference type", but as Dave Cheney describes they are not.
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00606))_

```
A map value is a pointer to a runtime.hmap structure.
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00607))_

> Context: Therefore, you should never initialize a nil map variable:
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00610))_

```
var m map[string]string
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00611))_

> Context: Instead, you can initialize an empty map or use the make keyword to create a map for you:
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00612))_

```
var dictionary = map[string]string{}
// OR
var dictionary = make(map[string]string)
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00613))_

> Context: Instead, you can initialize an empty map or use the make keyword to create a map for you:
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00612))_

> Which ensures that you will never get a runtime panic.
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00614))_


## Source

- [[coding-learn-go-with-tests-excerpt]]
