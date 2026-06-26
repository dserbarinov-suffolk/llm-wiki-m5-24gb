---
page_id: coding-learn-go-with-tests-excerpt-section-testable-examples-92bba1d7
page_kind: source
summary: Testable Examples: 27 source-backed entries and 4 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-testable-examples-92bba1d7@9f5001f4eaa5933bf5c9f5f3ec65d6ce
---

# Testable Examples

From [[coding-learn-go-with-tests-excerpt]].

## Statements

- You will find many examples in the standard library documentation. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00197))_
- Example functions are compiled whenever tests are executed. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00199))_
- (If your editor doesn't automatically import packages for you, the compilation step will fail because you will be missing import "fmt" in adder_test.go . _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00202))_
- It is strongly recommended you research how to have these kind of errors fixed for you automatically in whatever editor you are using.) _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00202))_
- (If your editor doesn't automatically import packages for you, the compilation step will fail because you will be missing import "fmt" in adder_test.go . _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00202))_
- If ever your code changes so that the example is no longer valid, your build will fail. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00203))_
- Adding this code will cause the example to appear in your documentation, making your code even more accessible. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00203))_
- Running the package's test suite, we can see the example ExampleAdd function is executed with no further arrangement from us: _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00204))_
- While the example will always be compiled, adding this comment means the example will also be executed. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00206))_
- Go ahead and temporarily remove the comment // Output: 6 , then run go test , and you will see ExampleAdd is no longer executed. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00206))_
- While the example will always be compiled, adding this comment means the example will also be executed. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00206))_
- Go ahead and temporarily remove the comment // Output: 6 , then run go test , and you will see ExampleAdd is no longer executed. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00206))_
- Examples without output comments are useful for demonstrating code that cannot run as unit tests, such as that which accesses the network, while guaranteeing the example at least compiles. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00207))_
- Examples without output comments are useful for demonstrating code that cannot run as unit tests, such as that which accesses the network, while guaranteeing the example at least compiles. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00207))_
- Follow that link, and then look under Integers , then under func Add , then expand Example and you should see the example you added for sum := Add(1, 5) . _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00208))_
- Before navigating to your project's directory, make sure you have installed pkgsite by running the following command: go install golang.org/x/pkgsite/cmd/pkgsite@latest , then run pkgsite -open . _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00208))_
- Inside here you'll see a list of all of Go's Standard Library packages, plus Third Party packages you have installed, under which you should see your example documentation for github.com/quii/learn-go-with-tests . _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00208))_
- Inside here you'll see a list of all of Go's Standard Library packages, plus Third Party packages you have installed, under which you should see your example documentation for github.com/quii/learn-go-with-tests . _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00208))_
- Follow that link, and then look under Integers , then under func Add , then expand Example and you should see the example you added for sum := Add(1, 5) . _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00208))_
- Before navigating to your project's directory, make sure you have installed pkgsite by running the following command: go install golang.org/x/pkgsite/cmd/pkgsite@latest , then run pkgsite -open . _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00208))_
- For example, here is the finalised API for this chapter. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00209))_
- This web interface allows you to search for documentation of standard library packages and third-party packages. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00209))_
- For example, here is the finalised API for this chapter. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00209))_

## Technical atoms

> If you really want to go the extra mile you can make Testable Examples.
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00197))_

```
func ExampleAdd() {
    sum := Add(1, 5)
    fmt.Println(sum)
    // Output: 6
}
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00201))_

```
$ go test -v
=== RUN   TestAdder
--- PASS: TestAdder (0.00s)
=== RUN   ExampleAdd
--- PASS: ExampleAdd (0.00s)
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00205))_

> If you publish your code with examples to a public URL, you can share the documentation of your code at pkg.go.dev.
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00209))_
