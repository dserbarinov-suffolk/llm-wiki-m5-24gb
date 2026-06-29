---
page_id: coding-learn-go-with-tests-excerpt-section-testable-examples-80b8a2ce
page_kind: source
summary: Testable Examples: 28 source-backed entries and 4 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-29
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-testable-examples-80b8a2ce@80f79e247a4dacae447427cace65d47b
---

# Testable Examples

From [[coding-learn-go-with-tests-excerpt]].

## Related pages

- [[coding-learn-go-with-tests-excerpt-section-testable-examples-wrapping-up-a2b7f25f]] - narrower source section: Testable Examples / Wrapping up
- [[coding-learn-go-with-tests-excerpt-section-integers-771ce4c7]] - previous source section: Integers
- [[coding-learn-go-with-tests-excerpt-section-iteration-9b1d79ea]] - next source section: Iteration
- [[coding-learn-go-with-tests-excerpt-testable]] - topic hub: opens the topic page for Testable

## Statements

- If you really want to go the extra mile you can make Testable Examples. You will find many examples in the standard library documentation. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00197))_
- Example functions are compiled whenever tests are executed. Because such examples are validated by the Go compiler, you can be confident your documentation's examples always reflect current code behavior. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00199))_
- (If your editor doesn't automatically import packages for you, the compilation step will fail because you will be missing import "fmt" in adder_test.go . It is strongly recommended you research how to have these kind of errors fixed for you automatically in whatever editor you are using.) _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00202))_
- Adding this code will cause the example to appear in your documentation, making your code even more accessible. If ever your code changes so that the example is no longer valid, your build will fail. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00203))_
- Running the package's test suite, we can see the example ExampleAdd function is executed with no further arrangement from us: _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00204))_
- Notice the special format of the comment, // Output: 6 . While the example will always be compiled, adding this comment means the example will also be executed. Go ahead and temporarily remove the comment // Output: 6 , then run go test , and you will see ExampleAdd is no longer executed. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00206))_
- Examples without output comments are useful for demonstrating code that cannot run as unit tests, such as that which accesses the network, while guaranteeing the example at least compiles. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00207))_
- To view example documentation, let's take a quick look at pkgsite . Before navigating to your project's directory, make sure you have installed pkgsite by running the following command: go install golang.org/x/pkgsite/cmd/pkgsite@latest , then run pkgsite -open . , which should open a web browser for you, pointing to http://localhost:8080 . Inside here you'll see a list of all of Go's Standard Library packages, plus Third Party packages you have installed, under which you should see your example documentation for github.com/quii/learn-go-with-tests . Follow that link, and then look under Integers , then under func Add , then expand Example and you should see the example you added for sum := Add(1, 5) . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00208))_
- If you publish your code with examples to a public URL, you can share the documentation of your code at pkg.go.dev. For example, here is the finalised API for this chapter. This web interface allows you to search for documentation of standard library packages and third-party packages. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00209))_
- (If your editor doesn't automatically import packages for you, the compilation step will fail because you will be missing import "fmt" in adder_test.go . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00202))_
- While the example will always be compiled, adding this comment means the example will also be executed. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00206))_
- Go ahead and temporarily remove the comment // Output: 6 , then run go test , and you will see ExampleAdd is no longer executed. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00206))_
- Examples without output comments are useful for demonstrating code that cannot run as unit tests, such as that which accesses the network, while guaranteeing the example at least compiles. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00207))_
- Inside here you'll see a list of all of Go's Standard Library packages, plus Third Party packages you have installed, under which you should see your example documentation for github.com/quii/learn-go-with-tests . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00208))_
- Follow that link, and then look under Integers , then under func Add , then expand Example and you should see the example you added for sum := Add(1, 5) . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00208))_
- Before navigating to your project's directory, make sure you have installed pkgsite by running the following command: go install golang.org/x/pkgsite/cmd/pkgsite@latest , then run pkgsite -open . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00208))_
- For example, here is the finalised API for this chapter. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00209))_

## Statements by subsection

### Testable Examples / Wrapping up

- Writing better documentation so users of our code can understand its usage quickly _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00214))_

## Technical atoms

### Technical frame 1: Testable Examples

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00199))_

> Example functions are compiled whenever tests are executed. Because such examples are validated by the Go compiler, you can be confident your documentation's examples always reflect current code behavior.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00197))_

> If you really want to go the extra mile you can make Testable Examples.

### Technical frame 2: Testable Examples

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00202))_

> (If your editor doesn't automatically import packages for you, the compilation step will fail because you will be missing import "fmt" in adder_test.go . It is strongly recommended you research how to have these kind of errors fixed for you automatically in whatever editor you are using.)

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00201))_

```
func ExampleAdd() {
    sum := Add(1, 5)
    fmt.Println(sum)
    // Output: 6
}
```

### Technical frame 3: Testable Examples

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

### Technical frame 4: Testable Examples

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00208))_

> To view example documentation, let's take a quick look at pkgsite . Before navigating to your project's directory, make sure you have installed pkgsite by running the following command: go install golang.org/x/pkgsite/cmd/pkgsite@latest , then run pkgsite -open . , which should open a web browser for you, pointing to http://localhost:8080 . Inside here you'll see a list of all of Go's Standard Library packages, plus Third Party packages you have installed, under which you should see your example

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00209))_

> If you publish your code with examples to a public URL, you can share the documentation of your code at pkg.go.dev.
