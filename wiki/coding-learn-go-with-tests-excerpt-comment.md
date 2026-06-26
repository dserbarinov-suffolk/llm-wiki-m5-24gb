---
page_id: coding-learn-go-with-tests-excerpt-comment
page_kind: concept
summary: Comment: 4 statement(s) and 2 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-comment@e3c6e47030a6ff4009f3f1f23d6788bf
---

# Comment

What [[coding-learn-go-with-tests-excerpt]] covers about comment:

## Statements

- If you still don't understand, comment it out, make a test fail and observe the test output. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00088))_
- Comments in Go are a great way to add additional information to your code, or in this case, a quick way to tell the compiler to ignore a line. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00088))_
- Go ahead and temporarily remove the comment // Output: 6 , then run go test , and you will see ExampleAdd is no longer executed. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00206))_
- Examples without output comments are useful for demonstrating code that cannot run as unit tests, such as that which accesses the network, while guaranteeing the example at least compiles. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00207))_

## Technical atoms

> Context: We've refactored our assertion into a new function. This reduces duplication and improves the readability of our tests. We need to pass in t *testing.T so that we can tell the test code to fail when we need to. t.Helper() is needed to tell the test suite that this method is a helper. By doing this, when it fails, the line number reported will be in our function call rather than inside our test helper. This will help other developers track down problems more easily. If you still don't understand, comment it out, make a test fail and observe the test output. Comments in Go are a great way to add additional information to your code, or in this case, a quick way to tell the compiler to ignore a line. You can comment out the t.Helper() code by adding two forward slashes // at the beginning of the line. You should see that line turn grey or change to another color than the rest of your code to indicate it's now commented out.
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00086, source-range-559be4b1-00088))_

> For helper functions, it's a good idea to accept a testing.TB which is an interface that *testing.T and *testing.B both satisfy, so you can call helper functions from a test, or a benchmark (don't worry if words like "interface" mean nothing to you right now, it will be covered later).
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00087))_

> Context: Running the package's test suite, we can see the example ExampleAdd function is executed with no further arrangement from us: Notice the special format of the comment, // Output: 6 . While the example will always be compiled, adding this comment means the example will also be executed. Go ahead and temporarily remove the comment // Output: 6 , then run go test , and you will see ExampleAdd is no longer executed.
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00204, source-range-559be4b1-00206))_

```
$	go	test	-v ===	RUN			TestAdder ---	PASS:	TestAdder ( 0.00s ) ===	RUN			ExampleAdd ---	PASS:	ExampleAdd ( 0.00s )
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00205))_


## Source

- [[coding-learn-go-with-tests-excerpt]]
