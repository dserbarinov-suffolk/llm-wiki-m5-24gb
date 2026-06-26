---
page_id: coding-learn-go-with-tests-excerpt-section-write-enough-code-to-make-it-pass-5b35a970
page_kind: source
summary: Write enough code to make it pass: 11 source-backed entries and 2 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-write-enough-code-to-make-it-pass-5b35a970@ec6383e618a3eb7bbe3ab8ab93ceaa02
---

# Write enough code to make it pass

From [[coding-learn-go-with-tests-excerpt]].

## Statements

- The for syntax is very unremarkable and follows most C-like languages. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00232))_
- as we've been using := so far to declare and initializing variables. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00236))_
- However, := is simply short hand for both steps. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00236))_
- We can also use var to declare functions, as we'll see later on. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00236))_
- Here we are declaring a string variable only. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00236))_
- Here we are declaring a string variable only. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00236))_
- Hence, the explicit version. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00236))_
- Run the test and it should pass. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00237))_
- Additional variants of the for loop are described here. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00238))_

## Technical atoms

```
func Repeat(character string) string {
    var repeated string
    for i := 0; i < 5; i++ {
        repeated = repeated + character
    }
    return repeated
}
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00233))_

```
var repeated string
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00235))_
