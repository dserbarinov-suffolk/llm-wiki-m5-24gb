---
page_id: coding-learn-go-with-tests-excerpt-code
page_kind: concept
summary: Code: 10 statement(s) and 6 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
page_family: topic-concept
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-30
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-code@12912bb62cc3bbfe9689c43ae5f54caa
---

# Code

What [[coding-learn-go-with-tests-excerpt]] covers about code:

## Statements

### Hello, World / Back to Testing

- of the code you will write. Writing tests Writing a test is just like writing a function, with a few rules It needs to be in a file with a name like xxx_test.go The test function must start with the word Test The test function takes one argument only t *testing.T To use the *testing.T type, you need to import "testing" , like we did with fmt in the other file For now, it's enough to know that your t of type *testing.T is your "hook" into the testing framework so you can do things like t.Fail() when you want to fail. We've covered some new topics: if If statements in Go are very much like other programming languages. Declaring variables We're declaring some variables with the syntax varName := value , which lets us reuse some values in our test for readability. t.Errorf We are calling the method on our , which will print out a _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00033))_

### Hello, YOU

- In the last example, we wrote the test after the code had been written so that you could get an example of how to write a test and declare a function. From this point on, we will be writing tests first . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00044))_

- When using a statically typed language like Go it is important to listen to the compiler . The compiler understands how your code should snap together and work so you don't have to. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00051))_

### Integers / Refactor

- There's not a lot in the actual code we can really improve on here. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00191))_

### Testable Examples

- Adding this code will cause the example to appear in your documentation, making your code even more accessible. If ever your code changes so that the example is no longer valid, your build will fail. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00203))_

### Testable Examples / Wrapping up

- Writing better documentation so users of our code can understand its usage quickly _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00214))_

### Benchmarking

- The number of times the code is run shouldn't matter to you, the framework will determine what is a "good" value for that to let you have some decent results. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00249))_

### Structs, methods & interfaces / Refactor

- Our code does the job, but it doesn't contain anything explicit about rectangles. An unwary developer might try to supply the width and height of a triangle to these functions without realising they will return the wrong answer. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00426))_

### Decoupling / Wrapping up

- Interfaces are a great tool for hiding complexity away from other parts of the system. In our case our test helper code did not need to know the exact shape it was asserting on, only how to "ask" for its area. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00543))_


## Technical atoms

### Technical frame 1: Learn Go with Tests (Excerpt)

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00002))_

> Learn Go with Tests -- Go Fundamentals (Excerpt) Hello, World How it works How to test Go modules? Back to Testing Writing tests Go's documentation Hello, YOU A note on source control Constants Hello, world... again Back to source control Discipline Keep going! More requirements French switch one...last...refactor? Wrapping up Some of Go's syntax around The TDD process and why the steps are important Integers Write the test first Try and run the test Write the minimal amount of code for the test

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00003))_

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

### Technical frame 2: Hello, YOU

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00055))_

> If you try and run your tests again your hello.go will fail to compile because you're not passing an argument. Send in "world" to make it compile.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00054))_

```
func Hello(name string) string {
    return "Hello, world"
}
```

### Technical frame 3: Integers / Refactor

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00193))_

> This is great because it aids the usability of code you are writing. It is preferable that a user can understand the usage of your code by just looking at the type signature and documentation.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00194))_

> You can add documentation to functions with comments, and these will appear in Go Doc just like when you look at the standard library's documentation.

### Technical frame 4: Testable Examples

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00199))_

> Example functions are compiled whenever tests are executed. Because such examples are validated by the Go compiler, you can be confident your documentation's examples always reflect current code behavior.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00197))_

> If you really want to go the extra mile you can make Testable Examples.

### Technical frame 5: Benchmarking

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

### Technical frame 6: Benchmarking

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

- [[coding-learn-go-with-tests-excerpt-write-code-pass]] - narrower topic: Write enough code to make it pass shares source evidence from Hello, World / Back to Testing: of the code you will write. Writing tests Writing a test is just like writing a function, with a few rules It needs to be in a file with a name like xxx_test.go The ... [truncated]; Write enough code to make it pass shares technical record from Learn Go with Tests (Excerpt): output Write enough code to make it pass Refactor Write the test ﬁrst Try and run the test Write minimal amount of code for the test to run and check the failing tes ... [truncated] (2 shared statement(s), 1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-test]] - shared statements and technical atoms: Test shares source evidence from Hello, YOU: In the last example, we wrote the test after the code had been written so that you could get an example of how to write a test and declare a function. From this poin ... [truncated]; Test shares technical record from Learn Go with Tests (Excerpt): output Write enough code to make it pass Refactor Write the test ﬁrst Try and run the test Write minimal amount of code for the test to run and check the failing tes ... [truncated] (2 shared statement(s), 2 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-compiler]] - shared statements and technical atoms: Compiler shares source evidence from Hello, YOU: When using a statically typed language like Go it is important to listen to the compiler . The compiler understands how your code should snap together and work so yo ... [truncated]; Compiler shares technical record from Hello, YOU: func Hello(name string) string { return "Hello, world" } (1 shared statement(s), 1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-write-test]] - shared statements and technical atoms: Write the test first shares source evidence from Hello, YOU: In the last example, we wrote the test after the code had been written so that you could get an example of how to write a test and declare a function. From this poin ... [truncated]; Write the test first shares technical record from Learn Go with Tests (Excerpt): output Write enough code to make it pass Refactor Write the test ﬁrst Try and run the test Write minimal amount of code for the test to run and check the failing tes ... [truncated] (1 shared statement(s), 1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-loop]] - shared technical atoms: Loop shares technical record from Benchmarking: func Benchmark(b *testing.B) { //... setup ... for b.Loop() { //... code to measure ... } //... cleanup ... } (1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-try-run-test]] - shared technical atoms: Try and run the test shares technical record from Learn Go with Tests (Excerpt): output Write enough code to make it pass Refactor Write the test ﬁrst Try and run the test Write minimal amount of code for the test to run and check the failing tes ... [truncated] (1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-write]] - shared technical atoms: Write shares technical record from Learn Go with Tests (Excerpt): output Write enough code to make it pass Refactor Write the test ﬁrst Try and run the test Write minimal amount of code for the test to run and check the failing tes ... [truncated] (1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-helper]] - shared statements: Helper shares source evidence from Decoupling / Wrapping up: Interfaces are a great tool for hiding complexity away from other parts of the system. In our case our test helper code did not need to know the exact shape it was a ... [truncated] (1 shared statement(s))
- [[coding-learn-go-with-tests-excerpt-writing]] - shared statements: Writing shares source evidence from Testable Examples / Wrapping up: Writing better documentation so users of our code can understand its usage quickly (1 shared statement(s))

## Source

- [[coding-learn-go-with-tests-excerpt]]
