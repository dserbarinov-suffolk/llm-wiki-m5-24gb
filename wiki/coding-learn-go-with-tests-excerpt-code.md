---
page_id: coding-learn-go-with-tests-excerpt-code
page_kind: concept
summary: Code: 10 statement(s) and 6 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-code@f88de9109abe4cfd1cc00174d557e3e2
---

# Code

What [[coding-learn-go-with-tests-excerpt]] covers about code:

## Statements

- Adding this code will cause the example to appear in your documentation, making your code even more accessible. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00203))_
- of the code you will write. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00033))_
- In the last example, we wrote the test after the code had been written so that you could get an example of how to write a test and declare a function. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00044))_
- The compiler understands how your code should snap together and work so you don't have to. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00051))_
- There's not a lot in the actual code we can really improve on here. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00191))_
- If ever your code changes so that the example is no longer valid, your build will fail. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00203))_
- Writing better documentation so users of our code can understand its usage quickly _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00214))_
- The number of times the code is run shouldn't matter to you, the framework will determine what is a "good" value for that to let you have some decent results. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00249))_
- Our code does the job, but it doesn't contain anything explicit about rectangles. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00426))_
- In our case our test helper code did not need to know the exact shape it was asserting on, only how to "ask" for its area. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00543))_

## Technical atoms

> Context: Learn Go with Tests -- Go Fundamentals (Excerpt) Hello, World How it works How to test Go modules? Back to Testing Writing tests Go's documentation Hello, YOU A note on source control Constants Hello, world... again Back to source control Discipline Keep going! More requirements French switch one...last...refactor? Wrapping up Some of Go's syntax around The TDD process and why the steps are important Integers Write the test first Try and run the test Write the minimal amount of code for the test to run and check the failing test output Write enough code to make it pass Refactor Testable Examples Wrapping up Iteration Write the test first Try and run the test Write the minimal amount of code for the test to run and check the failing test output Write enough code to make it pass Refactor Benchmarking Practice exercises Wrapping up Arrays and slices Write the test first Try to run the test Write the minimal amount of code for the test to run and check the failing test output Write enough code to make it pass Refactor Arrays and their type Write the test first Try and run the test Write the minimal amount of code for the test to run and check the failing test output Write enough code to make it pass Refactor Write the test first Try and run the test Write the minimal amount of code for the test to run and check the failing test output Write enough code to make it pass Refactor Write the test first Try and run the test Write the minimal amount of code for the test to run and check the failing test output Write enough code to make it pass Refactor Write the test first Try and run the test Write enough code to make it pass Refactor Wrapping up Structs, methods & interfaces Write the test first Try to run the test Write the minimal amount of code for the test to run and check the failing test output Write enough code to make it pass Refactor Write the test first Try to run the test Write the minimal amount of code for the test to run and check the failing test output What are methods? Write the minimal amount of code for the test to run and check the failing test output Write enough code to make it pass Refactor Wait, what? Decoupling Further refactoring Write the test first Try to run the test Write the minimal amount of code for the test to run and check the failing test output Write enough code to make it pass Refactor Make sure your test output is helpful Wrapping up Maps Write the test first Try to run the test Write the minimal amount of code for the test to run and check the output Write enough code to make it pass Refactor Using a custom type Write the test first Try and run the test Write the minimal amount of code for the test to run and check the output Write enough code to make it pass Refactor Write the test first Write the minimal amount of code for the test to run and check output Write enough code to make it pass Pointers, copies, et al Refactor Write the test first Try to run test Write the minimal amount of code for the test to run and check the
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00002))_

```
output
Write enough code to make it pass
Refactor
Write the test ﬁrst
Try and run the test
Write minimal amount of code for the test to run and check the
failing test output
Write enough code to make it pass
Write the test ﬁrst
Try and run the test
Write the minimal amount of code for the test to run and check the
failing test output
Write enough code to make it pass
Note on declaring a new error for Update
Write the test ﬁrst
Try to run the test
Write the minimal amount of code for the test to run and check the
failing test output
Write enough code to make it pass
Refactor
Try to run test
Write enough code to make it pass
Wrapping up
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00003))_

> Context: When using a statically typed language like Go it is important to listen to the compiler . The compiler understands how your code should snap together and work so you don't have to. If you try and run your tests again your hello.go will fail to compile because you're not passing an argument. Send in "world" to make it compile.
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00051, source-range-f4b7154d-00055))_

```
func Hello(name string) string {
    return "Hello, world"
}
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00054))_

> Context: There's not a lot in the actual code we can really improve on here.
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00191))_

> You can add documentation to functions with comments, and these will appear in Go Doc just like when you look at the standard library's documentation.
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00194))_

> Context: Often code examples that can be found outside the codebase, such as a readme file, become out of date and incorrect compared to the actual code because they don't get checked.
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00198))_

> If you really want to go the extra mile you can make Testable Examples.
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00197))_

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


## Source

- [[coding-learn-go-with-tests-excerpt]]
