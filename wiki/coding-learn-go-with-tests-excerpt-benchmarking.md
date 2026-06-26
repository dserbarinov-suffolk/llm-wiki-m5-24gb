---
page_id: coding-learn-go-with-tests-excerpt-benchmarking
page_kind: concept
summary: Benchmarking: 11 statement(s) and 7 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-benchmarking@c7e630fc702dfe9c64b139ec5abce63d
---

# Benchmarking

What [[coding-learn-go-with-tests-excerpt]] covers about benchmarking:

## Statements

- What 136 ns/op means is our function takes on average 136 nanoseconds to run (on my computer). _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00252))_
- The testing.B gives you access to the loop function. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00247))_
- Loop() returns true as long as the benchmark should continue running. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00247))_
- After Loop() returns false, b.N contains the total number of iterations that ran. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00248))_
- The number of times the code is run shouldn't matter to you, the framework will determine what is a "good" value for that to let you have some decent results. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00249))_
- To run the benchmarks do go test -bench=. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00250))_
- Only the body of the loop is timed; it automatically excludes setup and cleanup code from benchmark timing. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00254))_
- Strings in Go are immutable, meaning every concatenation, such as in our Repeat function, involves copying memory to accommodate the new string. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00256))_
- The standard library provides the strings.Builder stringsBuilder type which minimizes memory copying. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00257))_
- Note : We have to call the String method to retrieve the final result. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00259))_
- We can use BenchmarkRepeat to confirm that strings.Builder significantly improves performance. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00260))_

## Technical atoms

```
func BenchmarkRepeat(b *testing.B) {
    for b.Loop() {
        Repeat("a")
    }
}
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00245))_

> When the benchmark code is executed, it measures how long it takes.
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00248))_

> Context: The number of times the code is run shouldn't matter to you, the framework will determine what is a "good" value for that to let you have some decent results.
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00249))_

```
goos: darwin
goarch: amd64
pkg: github.com/quii/learn-go-with-tests/for/v4
10000000           136 ns/op
PASS
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00251))_

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

> Context: The standard library provides the strings.Builder stringsBuilder type which minimizes memory copying. It implements a WriteString method which we can use to concatenate strings: Note : We have to call the String method to retrieve the final result.
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00257, source-range-f4b7154d-00259))_

```
const repeatCount = 5
func Repeat(character string) string {
    var repeated strings.Builder
    for i := 0; i < repeatCount; i++ {
        repeated.WriteString(character)
    }
    return repeated.String()
}
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00258))_

> Context: We can use BenchmarkRepeat to confirm that strings.Builder significantly improves performance. Run go test -bench=. -benchmem
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00260))_

```
goarch: amd64
pkg: github.com/quii/learn-go-with-tests/for/v4
10000000           25.70 ns/op           8 B/op 
allocs/op
PASS
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00261))_


## Source

- [[coding-learn-go-with-tests-excerpt]]
