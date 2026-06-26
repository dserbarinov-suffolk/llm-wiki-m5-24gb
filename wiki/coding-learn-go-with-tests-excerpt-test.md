---
page_id: coding-learn-go-with-tests-excerpt-test
page_kind: concept
summary: Test: 40 statement(s) and 34 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-test@9017d44de6d328da8c809831d330dde1
---

# Test

What [[coding-learn-go-with-tests-excerpt]] covers about test:

## Statements

- In the last example, we wrote the test after the code had been written so that you could get an example of how to write a test and declare a function. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00044))_
- Now that the tests are passing, we can and should refactor our tests. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00083))_
- When you try and run the test again it will complain about not passing through enough arguments to Hello in your other tests and in hello.go _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00113))_
- Write a failing test and see it fail so we know we have written a relevant test for our requirements and seen that it produces an easy to understand description of the failure _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00157))_
- Now run the tests, and we should be happy that the test is correctly reporting what is wrong. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00178))_
- Table driven tests can be a great item in your toolbox, but be sure that you have a need for the extra noise in the tests. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00501))_
- One final tip with table driven tests is to use t.Run and to name the test cases. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00530))_
- Table driven tests to make your assertions clearer and your test suites easier to extend & maintain _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00541))_
- If the tests pass, then you are probably using an earlier version of Go. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00025))_
- For tests, %q is very useful as it wraps your values in double quotes. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00034))_
- If you try and run your tests again your hello.go will fail to compile because you're not passing an argument. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00055))_
- After refactoring, re-run your tests to make sure you haven't broken anything. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00069))_
- If we run our tests we should see it satisfies the new requirement and we haven't accidentally broken the other functionality. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00080))_
- Seeing the test fail is an important check because it also lets you see what the error message looks like. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00101))_

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

> Context: The next step is to run the tests. Enter go test in your terminal. If the tests pass, then you are probably using an earlier version of Go. However, if you are using Go 1.16 or later, the tests will likely not run. Instead, you will see an error message like this in the terminal:
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00025))_

```
$ go test
go: cannot find main module; see 'go help modules'
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00026))_

> Context: When using a statically typed language like Go it is important to listen to the compiler . The compiler understands how your code should snap together and work so you don't have to. If you try and run your tests again your hello.go will fail to compile because you're not passing an argument. Send in "world" to make it compile.
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00051, source-range-f4b7154d-00055))_

```
func Hello(name string) string {
    return "Hello, world"
}
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00054))_

> Context: If you try and run your tests again your hello.go will fail to compile because you're not passing an argument. Send in "world" to make it compile.
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00055))_

```
func main() {
    fmt.Println(Hello("world"))
}
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00056))_

> Context: If you try and run your tests again your hello.go will fail to compile because you're not passing an argument. Send in "world" to make it compile.
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00055))_

> Now when you run your tests, you should see something like
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00057))_

> Context: If you try and run your tests again your hello.go will fail to compile because you're not passing an argument. Send in "world" to make it compile.
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00055))_

```
hello_test.go:10: got 'Hello, world' want 'Hello, Chris''
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00058))_


## Source

- [[coding-learn-go-with-tests-excerpt]]
