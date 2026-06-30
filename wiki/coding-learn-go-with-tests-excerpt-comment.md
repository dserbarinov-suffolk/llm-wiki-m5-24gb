---
page_id: coding-learn-go-with-tests-excerpt-comment
page_kind: concept
summary: Comment: 4 statement(s) and 2 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
page_family: topic-concept
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-30
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-comment@01f35e45970efdba205eec341830d434
---

# Comment

What [[coding-learn-go-with-tests-excerpt]] covers about comment:

## Statements

### Constants / Hello, world... again

- t.Helper() is needed to tell the test suite that this method is a helper. By doing this, when it fails, the line number reported will be in our function call rather than inside our test helper. This will help other developers track down problems more easily. If you still don't understand, comment it out, make a test fail and observe the test output. Comments in Go are a great way to add additional information to your code, or in this case, a quick way to tell the compiler to ignore a line. You can comment out the t.Helper() code by adding two forward slashes // at the beginning of the line. You should see that line turn grey or change to another color than the rest of your code to indicate it's now commented out. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00088))_

### Testable Examples

- Notice the special format of the comment, // Output: 6 . While the example will always be compiled, adding this comment means the example will also be executed. Go ahead and temporarily remove the comment // Output: 6 , then run go test , and you will see ExampleAdd is no longer executed. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00206))_

- Examples without output comments are useful for demonstrating code that cannot run as unit tests, such as that which accesses the network, while guaranteeing the example at least compiles. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00207))_


## Technical atoms

### Technical frame 1: Constants / Hello, world... again

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00088))_

> t.Helper() is needed to tell the test suite that this method is a helper. By doing this, when it fails, the line number reported will be in our function call rather than inside our test helper. This will help other developers track down problems more easily. If you still don't understand, comment it out, make a test fail and observe the test output. Comments in Go are a great way to add additional information to your code, or in this case, a quick way to tell the compiler to ignore a line. You c

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00087))_

> For helper functions, it's a good idea to accept a testing.TB which is an interface that *testing.T and *testing.B both satisfy, so you can call helper functions from a test, or a benchmark (don't worry if words like "interface" mean nothing to you right now, it will be covered later).

### Technical frame 2: Testable Examples

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00206))_

> Notice the special format of the comment, // Output: 6 . While the example will always be compiled, adding this comment means the example will also be executed. Go ahead and temporarily remove the comment // Output: 6 , then run go test , and you will see ExampleAdd is no longer executed.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00205))_

```
$ go test -v
=== RUN   TestAdder
--- PASS: TestAdder (0.00s)
=== RUN   ExampleAdd
--- PASS: ExampleAdd (0.00s)
```


## Related pages

- [[coding-learn-go-with-tests-excerpt-test]] - shared statements and technical atoms: Test shares source evidence from Testable Examples: Notice the special format of the comment, // Output: 6 . While the example will always be compiled, adding this comment means the example will also be executed. Go a ... [truncated]; Test shares technical record from Constants / Hello, world... again: For helper functions, it's a good idea to accept a testing.TB which is an interface that *testing.T and *testing.B both satisfy, so you can call helper functions fro ... [truncated] (1 shared statement(s), 2 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-try-run-test]] - shared statements and technical atoms: Try and run the test shares source evidence from Testable Examples: Notice the special format of the comment, // Output: 6 . While the example will always be compiled, adding this comment means the example will also be executed. Go a ... [truncated]; Try and run the test shares technical record from Testable Examples: $ go test -v === RUN   TestAdder --- PASS: TestAdder (0.00s) === RUN   ExampleAdd --- PASS: ExampleAdd (0.00s) (2 shared statement(s), 1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-function]] - shared technical atoms: Function shares technical record from Testable Examples: $ go test -v === RUN   TestAdder --- PASS: TestAdder (0.00s) === RUN   ExampleAdd --- PASS: ExampleAdd (0.00s) (1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-helper]] - shared technical atoms: Helper shares technical record from Constants / Hello, world... again: For helper functions, it's a good idea to accept a testing.TB which is an interface that *testing.T and *testing.B both satisfy, so you can call helper functions fro ... [truncated] (1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-package]] - shared technical atoms: Package shares technical record from Testable Examples: $ go test -v === RUN   TestAdder --- PASS: TestAdder (0.00s) === RUN   ExampleAdd --- PASS: ExampleAdd (0.00s) (1 shared atom(s))

## Source

- [[coding-learn-go-with-tests-excerpt]]
