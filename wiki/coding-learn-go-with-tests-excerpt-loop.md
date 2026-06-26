---
page_id: coding-learn-go-with-tests-excerpt-loop
page_kind: concept
summary: Loop: 4 statement(s) and 1 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-loop@3b470dbcc97dd5a3f83a2a20197a9c8f
---

# Loop

What [[coding-learn-go-with-tests-excerpt]] covers about loop:

## Statements

- Additional variants of the for loop are described here. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00238))_
- Loop() returns true as long as the benchmark should continue running. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00247))_
- After Loop() returns false, b.N contains the total number of iterations that ran. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00248))_
- Only the body of the loop is timed; it automatically excludes setup and cleanup code from benchmark timing. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00254))_

## Technical atoms

> Context: Only the body of the loop is timed; it automatically excludes setup and cleanup code from benchmark timing. A typical benchmark is structured like:
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00254))_

```
func Benchmark(b *testing.B) {
    //... setup ...
    for b.Loop() {
        //... code to measure ...
    }
    //... cleanup ...
}
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00255))_


## Source

- [[coding-learn-go-with-tests-excerpt]]
