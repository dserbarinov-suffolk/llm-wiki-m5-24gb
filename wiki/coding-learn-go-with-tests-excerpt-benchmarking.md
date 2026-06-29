---
page_id: coding-learn-go-with-tests-excerpt-benchmarking
page_kind: concept
summary: Benchmarking: 14 statement(s) and 7 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-29
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-benchmarking@fb237122f1c9ecd142b66a58f280e49b
---

# Benchmarking

What [[coding-learn-go-with-tests-excerpt]] covers about benchmarking:

## Statements

### Benchmarking

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

### Benchmarking / Practice exercises

- Change the test so a caller can specify how many times the character is repeated and then fix the code _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00267))_

- Have a look through the strings package. Find functions you think could be useful and experiment with them by writing tests like we have here. Investing time learning the standard library will really pay off over time. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00269))_


## Technical atoms

### Technical frame 1: Benchmarking

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00247))_

> The testing.B gives you access to the loop function. Loop() returns true as long as the benchmark should continue running.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00245))_

```
func BenchmarkRepeat(b *testing.B) {
    for b.Loop() {
        Repeat("a")
    }
}
```

### Technical frame 2: Benchmarking

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00249))_

> The number of times the code is run shouldn't matter to you, the framework will determine what is a "good" value for that to let you have some decent results.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00248))_

> When the benchmark code is executed, it measures how long it takes.

### Technical frame 3: Benchmarking

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00252))_

> What 136 ns/op means is our function takes on average 136 nanoseconds to run (on my computer). Which is pretty ok! To test this it ran it 10000000 times.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00251))_

```
goos: darwin
goarch: amd64
pkg: github.com/quii/learn-go-with-tests/for/v4
10000000           136 ns/op
PASS
```

### Technical frame 4: Benchmarking

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

### Technical frame 5: Benchmarking

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00259))_

> Note : We have to call the String method to retrieve the final result.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00258))_

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

### Technical frame 6: Benchmarking

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00260))_

> We can use BenchmarkRepeat to confirm that strings.Builder significantly improves performance. Run go test -bench=. -benchmem

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00261))_

```
goarch: amd64
pkg: github.com/quii/learn-go-with-tests/for/v4
10000000           25.70 ns/op           8 B/op 
allocs/op
PASS
```

### Technical frame 7: Benchmarking

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00260))_

> We can use BenchmarkRepeat to confirm that strings.Builder significantly improves performance. Run go test -bench=. -benchmem

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00262))_

```
p
g
signiﬁcantly improves performance. Run go test -bench=. -benchmem:
goos: darwin
goarch: amd64
pkg: github.com/quii/learn-go-with-tests/for/v4
10000000           25.70 ns/op           8 B/op           1
```


## Related pages

- [[coding-learn-go-with-tests-excerpt-test]] - shared statements and technical atoms: Test shares source evidence from Benchmarking: The testing.B gives you access to the loop function. Loop() returns true as long as the benchmark should continue running.; Test shares technical record from Benchmarking: goarch: amd64 pkg: github.com/quii/learn-go-with-tests/for/v4 10000000           25.70 ns/op           8 B/op allocs/op PASS (2 shared statement(s), 2 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-code]] - shared statements and technical atoms: Code shares source evidence from Benchmarking: The number of times the code is run shouldn't matter to you, the framework will determine what is a "good" value for that to let you have some decent results.; Code shares technical record from Benchmarking: goos: darwin goarch: amd64 pkg: github.com/quii/learn-go-with-tests/for/v4 10000000           136 ns/op PASS (1 shared statement(s), 2 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-section-benchmarking-5c1bee15]] - source section: Benchmarking shares source evidence from Benchmarking: The testing.B gives you access to the loop function. Loop() returns true as long as the benchmark should continue running.; Benchmarking shares technical record from Benchmarking: func BenchmarkRepeat(b *testing.B) { for b.Loop() { Repeat("a") } } (14 shared statement(s), 7 shared atom(s))

## Source

- [[coding-learn-go-with-tests-excerpt]]
