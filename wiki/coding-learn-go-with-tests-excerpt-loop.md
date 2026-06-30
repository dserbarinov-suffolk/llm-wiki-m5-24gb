---
page_id: coding-learn-go-with-tests-excerpt-loop
page_kind: concept
summary: Loop: 4 statement(s) and 1 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
page_family: topic-concept
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-30
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-loop@767152d62440665c0513bbb5955b9e09
---

# Loop

What [[coding-learn-go-with-tests-excerpt]] covers about loop:

## Statements

### Iteration / Write enough code to make it pass

- Additional variants of the for loop are described here. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00238))_

### Benchmarking

- The testing.B gives you access to the loop function. Loop() returns true as long as the benchmark should continue running. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00247))_

- When the benchmark code is executed, it measures how long it takes. After Loop() returns false, b.N contains the total number of iterations that ran. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00248))_

- Only the body of the loop is timed; it automatically excludes setup and cleanup code from benchmark timing. A typical benchmark is structured like: _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00254))_


## Technical atoms

### Technical frame 1: Benchmarking

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00256))_

> Strings in Go are immutable, meaning every concatenation, such as in our Repeat function, involves copying memory to accommodate the new string. This impacts performance, particularly during heavy string concatenation.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00255))_

```
func Benchmark(b *testing.B) {
    //... setup ...
    for b.Loop() {
        //... code to measure ...
    }
    //... cleanup ...
}
```


## Related pages

- [[coding-learn-go-with-tests-excerpt-code]] - shared technical atoms: Code shares technical record from Benchmarking: func Benchmark(b *testing.B) { //... setup ... for b.Loop() { //... code to measure ... } //... cleanup ... } (1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-write-code-pass]] - shared statements: Write enough code to make it pass shares source evidence from Iteration / Write enough code to make it pass: Additional variants of the for loop are described here. (1 shared statement(s))

## Source

- [[coding-learn-go-with-tests-excerpt]]
