---
page_id: coding-learn-go-with-tests-excerpt-section-iteration-refactor-5810cb18
page_kind: source
summary: Iteration / Refactor: 2 source-backed entries and 1 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-29
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-iteration-refactor-5810cb18@f6bc27ff70536b3c9e0a0b3041d20317
---

# Iteration / Refactor

From [[coding-learn-go-with-tests-excerpt]].

## Related pages

- [[coding-learn-go-with-tests-excerpt-section-iteration-9b1d79ea]] - broader source section: Iteration
- [[coding-learn-go-with-tests-excerpt-section-iteration-write-enough-code-to-make-it-pass-82c13f0e]] - previous source section: Iteration / Write enough code to make it pass
- [[coding-learn-go-with-tests-excerpt-refactor]] - topic hub: opens the topic page for Refactor

## Statements

- += called "the Add AND assignment operator" , adds the right operand to the left operand and assigns the result to left operand. It works with other types like integers. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00242))_

## Technical atoms

### Technical frame 1: Iteration / Refactor

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00242))_

> += called "the Add AND assignment operator" , adds the right operand to the left operand and assigns the result to left operand. It works with other types like integers.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00241))_

```
const repeatCount = 5
func Repeat(character string) string {
    var repeated string
    for i := 0; i < repeatCount; i++ {
        repeated += character
    }
    return repeated
}
```
