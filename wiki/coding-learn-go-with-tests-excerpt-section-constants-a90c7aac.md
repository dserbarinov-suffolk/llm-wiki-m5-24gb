---
page_id: coding-learn-go-with-tests-excerpt-section-constants-a90c7aac
page_kind: source
summary: Constants: 3 source-backed entries and 1 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-constants-a90c7aac@c1fd8ef67fce523515cfcdc9be18eabf
---

# Constants

From [[coding-learn-go-with-tests-excerpt]].

## Statements

- After refactoring, re-run your tests to make sure you haven't broken anything. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00069))_
- After refactoring, re-run your tests to make sure you haven't broken anything. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00069))_

## Technical atoms

```
Constants are deﬁned like so
const englishHelloPrefix = "Hello, "
We can now refactor our code
const englishHelloPrefix = "Hello, "
func Hello(name string) string {
    return englishHelloPrefix + name
}
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00068))_
