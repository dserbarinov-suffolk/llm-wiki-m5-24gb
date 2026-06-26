---
page_id: coding-learn-go-with-tests-excerpt-benchmarking
page_kind: concept
summary: Benchmarking: 11 statement(s) and 0 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-benchmarking@1837a6a8ca3479e15596c30853f54104
---

# Benchmarking

What [[coding-learn-go-with-tests-excerpt]] covers about benchmarking:

## Statements

- Loop() returns true as long as the benchmark should continue running. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00247))_
- The testing.B gives you access to the loop function. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00247))_
- After Loop() returns false, b.N contains the total number of iterations that ran. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00248))_
- The number of times the code is run shouldn't matter to you, the framework will determine what is a "good" value for that to let you have some decent results. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00249))_
- To run the benchmarks do go test -bench=. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00250))_
- What 136 ns/op means is our function takes on average 136 nanoseconds to run (on my computer). _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00252))_
- Only the body of the loop is timed; it automatically excludes setup and cleanup code from benchmark timing. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00254))_
- Strings in Go are immutable, meaning every concatenation, such as in our Repeat function, involves copying memory to accommodate the new string. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00256))_
- The standard library provides the strings.Builder stringsBuilder type which minimizes memory copying. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00257))_
- Note : We have to call the String method to retrieve the final result. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00259))_
- We can use BenchmarkRepeat to confirm that strings.Builder significantly improves performance. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00260))_

## Source

- [[coding-learn-go-with-tests-excerpt]]
