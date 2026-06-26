---
page_id: coding-learn-go-with-tests-excerpt-section-benchmarking-4c600dce
page_kind: source
summary: Benchmarking: 22 source-backed entries and 7 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-benchmarking-4c600dce@f215b642d3a8a96e8caa0fdc88e0ff51
---

# Benchmarking

From [[coding-learn-go-with-tests-excerpt]].

## Statements

- The testing.B gives you access to the loop function. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00247))_
- After Loop() returns false, b.N contains the total number of iterations that ran. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00248))_
- When the benchmark code is executed, it measures how long it takes. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00248))_
- After Loop() returns false, b.N contains the total number of iterations that ran. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00248))_
- The number of times the code is run shouldn't matter to you, the framework will determine what is a "good" value for that to let you have some decent results. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00249))_
- To run the benchmarks do go test -bench=. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00250))_
- What 136 ns/op means is our function takes on average 136 nanoseconds to run (on my computer). _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00252))_
- What 136 ns/op means is our function takes on average 136 nanoseconds to run (on my computer). _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00252))_
- Only the body of the loop is timed; it automatically excludes setup and cleanup code from benchmark timing. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00254))_
- Only the body of the loop is timed; it automatically excludes setup and cleanup code from benchmark timing. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00254))_
- Strings in Go are immutable, meaning every concatenation, such as in our Repeat function, involves copying memory to accommodate the new string. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00256))_
- Strings in Go are immutable, meaning every concatenation, such as in our Repeat function, involves copying memory to accommodate the new string. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00256))_
- The standard library provides the strings.Builder stringsBuilder type which minimizes memory copying. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00257))_
- Note : We have to call the String method to retrieve the final result. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00259))_
- We can use BenchmarkRepeat to confirm that strings.Builder significantly improves performance. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00260))_

## Technical atoms

```
func BenchmarkRepeat(b	*testing.B)	{ for b.Loop()	{ Repeat("a") } }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00245))_

> Loop() returns true as long as the benchmark should continue running.
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00247))_

```
goos:	darwin goarch:	amd64 pkg:	github.com/quii/learn-go-with-tests/for/v4 10000000											136	ns/op PASS
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00251))_

```
func Benchmark(b	*testing.B)	{ //...	setup	... for b.Loop()	{ //...	code	to	measure	... } //...	cleanup	... }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00255))_

```
const repeatCount	=	5 func Repeat(character	string)	string	{ var repeated	strings.Builder for i	:=	0;	i	<	repeatCount;	i++	{ repeated.WriteString(character) } return repeated.String() }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00258))_

```
goarch:	amd64 pkg:	github.com/quii/learn-go-with-tests/for/v4 allocs/op PASS
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00261))_

```
: goos:	darwin 10000000											25.70	ns/op											8	B/op											1
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00262))_
