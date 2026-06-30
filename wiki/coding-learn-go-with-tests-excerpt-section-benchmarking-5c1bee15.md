---
page_id: coding-learn-go-with-tests-excerpt-section-benchmarking-5c1bee15
page_kind: source
summary: Benchmarking: 26 source-backed entries and 0 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
page_family: section-reference
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-30
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-benchmarking-5c1bee15@5b61f746e200ead07d475dc11b5f049a
---

# Benchmarking

From [[coding-learn-go-with-tests-excerpt]].

## Related pages

- [[coding-learn-go-with-tests-excerpt-section-benchmarking-practice-exercises-694810f9]] - narrower source section: Benchmarking / Practice exercises
- [[coding-learn-go-with-tests-excerpt-section-iteration-9b1d79ea]] - previous source section: Iteration
- [[coding-learn-go-with-tests-excerpt-section-arrays-and-slices-648d683c]] - next source section: Arrays and slices

## Statements

- The testing.B gives you access to the loop function. Loop() returns true as long as the benchmark should continue running. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00247))_
- When the benchmark code is executed, it measures how long it takes. After Loop() returns false, b.N contains the total number of iterations that ran. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00248))_
- The number of times the code is run shouldn't matter to you, the framework will determine what is a "good" value for that to let you have some decent results. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00249))_
- To run the benchmarks do go test -bench=. (or if you're in Windows Powershell go test -bench="." ) _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00250))_
- What 136 ns/op means is our function takes on average 136 nanoseconds to run (on my computer). Which is pretty ok! To test this it ran it 10000000 times. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00252))_
- Only the body of the loop is timed; it automatically excludes setup and cleanup code from benchmark timing. A typical benchmark is structured like: _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00254))_
- Strings in Go are immutable, meaning every concatenation, such as in our Repeat function, involves copying memory to accommodate the new string. This impacts performance, particularly during heavy string concatenation. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00256))_
- The standard library provides the strings.Builder stringsBuilder type which minimizes memory copying. It implements a WriteString method which we can use to concatenate strings: _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00257))_
- Note : We have to call the String method to retrieve the final result. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00259))_
- We can use BenchmarkRepeat to confirm that strings.Builder significantly improves performance. Run go test -bench=. -benchmem _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00260))_
- After Loop() returns false, b.N contains the total number of iterations that ran. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00248))_
- What 136 ns/op means is our function takes on average 136 nanoseconds to run (on my computer). _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00252))_
- Only the body of the loop is timed; it automatically excludes setup and cleanup code from benchmark timing. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00254))_
- Strings in Go are immutable, meaning every concatenation, such as in our Repeat function, involves copying memory to accommodate the new string. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00256))_

## Statements by subsection

### Benchmarking / Practice exercises

- Change the test so a caller can specify how many times the character is repeated and then fix the code _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00267))_
- Have a look through the strings package. Find functions you think could be useful and experiment with them by writing tests like we have here. Investing time learning the standard library will really pay off over time. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00269))_
- - Change the test so a caller can specify how many times the character is repeated and then fix the code _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00267))_
