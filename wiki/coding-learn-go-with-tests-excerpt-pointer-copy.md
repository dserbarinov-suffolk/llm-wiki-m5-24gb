---
page_id: coding-learn-go-with-tests-excerpt-pointer-copy
page_kind: concept
summary: Pointers, copies, et al: 5 statement(s) and 0 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-pointer-copy@83135db248a646c214826513d5b72557
---

# Pointers, copies, et al

What [[coding-learn-go-with-tests-excerpt]] covers about pointers, copies, et al:

## Statements

- So when you pass a map to a function/method, you are indeed copying it, but just the pointer part, not the underlying data structure that contains the data. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00608))_
- An interesting property of maps is that you can modify them without passing as an address to it (e.g &myMap ) _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00605))_
- You can read more about maps here. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00609))_
- A gotcha with maps is that they can be a nil value. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00609))_
- Instead, you can initialize an empty map or use the make keyword to create a map for you: _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00612))_

## Source

- [[coding-learn-go-with-tests-excerpt]]
