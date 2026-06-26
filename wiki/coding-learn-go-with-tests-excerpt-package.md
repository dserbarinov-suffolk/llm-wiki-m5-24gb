---
page_id: coding-learn-go-with-tests-excerpt-package
page_kind: concept
summary: Package: 6 statement(s) and 5 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-package@7e16eb2140f9b201097256f3d204c087
---

# Package

What [[coding-learn-go-with-tests-excerpt]] covers about package:

## Statements

- Packages are ways of grouping up related Go code together. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00014))_
- We just saw the documentation for the fmt package at the official package viewing website, and Go also provides ways for quickly getting at the documentation offline. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00037))_
- (If your editor doesn't automatically import packages for you, the compilation step will fail because you will be missing import "fmt" in adder_test.go . _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00202))_
- Running the package's test suite, we can see the example ExampleAdd function is executed with no further arrangement from us: _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00204))_
- Inside here you'll see a list of all of Go's Standard Library packages, plus Third Party packages you have installed, under which you should see your example documentation for github.com/quii/learn-go-with-tests . _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00208))_
- From Go 1.21, slices standard package is available, which has slices.Equal function to do a simple shallow compare on slices, where you don't need to worry about the types like the above case. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00348))_

## Technical atoms

> Context: Go has a built-in tool, doc, which lets you examine any package installed on your system, or the module you're currently working on. To view that same documentation for the Printing verbs:
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00038))_

```
$ go doc fmt
package fmt // import "fmt"
Package fmt implements formatted I/O with functions analogous to C's 
printf and
scanf. The format 'verbs' are derived from C's but are simpler.
# Printing
The verbs:
General:
%v  the value in a default format
       when printing structs, the plus flag (%+v) adds field names
   %#v a Go-syntax representation of the value
   %T  a Go-syntax representation of the type of the value
   %%  a literal percent sign; consumes no value
...
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00039))_

> Context: Example functions begin with Example (much like test functions begin with Test ), and reside in a package's _test.go files. Add the following ExampleAdd function to the adder_test.go file. (If your editor doesn't automatically import packages for you, the compilation step will fail because you will be missing import "fmt" in adder_test.go . It is strongly recommended you research how to have these kind of errors fixed for you automatically in whatever editor you are using.)
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00200, source-range-f4b7154d-00202))_

```
func ExampleAdd() {
    sum := Add(1, 5)
    fmt.Println(sum)
    // Output: 6
}
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00201))_

> Context: Running the package's test suite, we can see the example ExampleAdd function is executed with no further arrangement from us: Notice the special format of the comment, // Output: 6 . While the example will always be compiled, adding this comment means the example will also be executed. Go ahead and temporarily remove the comment // Output: 6 , then run go test , and you will see ExampleAdd is no longer executed.
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00204, source-range-f4b7154d-00206))_

```
$ go test -v
=== RUN   TestAdder
--- PASS: TestAdder (0.00s)
=== RUN   ExampleAdd
--- PASS: ExampleAdd (0.00s)
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00205))_

> Context: To view example documentation, let's take a quick look at pkgsite . Before navigating to your project's directory, make sure you have installed pkgsite by running the following command: go install golang.org/x/pkgsite/cmd/pkgsite@latest , then run pkgsite -open . , which should open a web browser for you, pointing to http://localhost:8080 . Inside here you'll see a list of all of Go's Standard Library packages, plus Third Party packages you have installed, under which you should see your example documentation for github.com/quii/learn-go-with-tests . Follow that link, and then look under Integers , then under func Add , then expand Example and you should see the example you added for sum := Add(1, 5) .
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00208))_

> If you publish your code with examples to a public URL, you can share the documentation of your code at pkg.go.dev.
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00209))_

> Context: From Go 1.21, slices standard package is available, which has slices.Equal function to do a simple shallow compare on slices, where you don't need to worry about the types like the above case. Note that this function expects the elements to be comparable. So, it can't be applied to slices with non-comparable elements like 2D slices.
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00348))_

```
./sum_test.go:26:9: invalid operation: got != want (slice can only 
be compared to nil)
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00346))_


## Source

- [[coding-learn-go-with-tests-excerpt]]
