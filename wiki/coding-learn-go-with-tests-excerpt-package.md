---
page_id: coding-learn-go-with-tests-excerpt-package
page_kind: concept
summary: Package: 6 statement(s) and 5 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
page_family: topic-concept
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-30
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-package@bb1a71a564a40423a28a587623860026
---

# Package

What [[coding-learn-go-with-tests-excerpt]] covers about package:

## Statements

### Hello, World / How it works

- When you write a program in Go, you will have a main package defined with a main func inside it. Packages are ways of grouping up related Go code together. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00014))_

### Go's documentation

- Another quality-of-life feature of Go is the documentation. We just saw the documentation for the fmt package at the official package viewing website, and Go also provides ways for quickly getting at the documentation offline. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00037))_

### Testable Examples

- (If your editor doesn't automatically import packages for you, the compilation step will fail because you will be missing import "fmt" in adder_test.go . It is strongly recommended you research how to have these kind of errors fixed for you automatically in whatever editor you are using.) _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00202))_

- Running the package's test suite, we can see the example ExampleAdd function is executed with no further arrangement from us: _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00204))_

- To view example documentation, let's take a quick look at pkgsite . Before navigating to your project's directory, make sure you have installed pkgsite by running the following command: go install golang.org/x/pkgsite/cmd/pkgsite@latest , then run pkgsite -open . , which should open a web browser for you, pointing to http://localhost:8080 . Inside here you'll see a list of all of Go's Standard Library packages, plus Third Party packages you have installed, under which you should see your example documentation for github.com/quii/learn-go-with-tests . Follow that link, and then look under Integers , then under func Add , then expand Example and you should see the example you added for sum := Add(1, 5) . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00208))_

### Arrays and their type / Write the minimal amount of code for the test to run and check the failing test output

- From Go 1.21, slices standard package is available, which has slices.Equal function to do a simple shallow compare on slices, where you don't need to worry about the types like the above case. Note that this function expects the elements to be comparable. So, it can't be applied to slices with non-comparable elements like 2D slices. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00348))_


## Technical atoms

### Technical frame 1: Go's documentation

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00040))_

> Go's second tool for viewing documentation is the pkgsite command, which powers Go's official package viewing website. You can install pkgsite with go install golang.org/x/pkgsite/cmd/pkgsite@latest , then run it with pkgsite -open . . Go's install command will download the source files from that repository and build them into an executable binary. For a default installation of Go, that executable will be in $HOME/go/bin for Linux and macOS, and %USERPROFILE%\go\bin for Windows. If you have not 

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00039))_

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

### Technical frame 5: Arrays and their type / Write the minimal amount of code for the test to run and check the failing test output

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00347))_

> Go does not let you use equality operators with slices. You could write a function to iterate over each got and want slice and check their values, but what if we had a more convenient way to do this?

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00346))_

```
./sum_test.go:26:9: invalid operation: got != want (slice can only 
be compared to nil)
```


## Related pages

- [[coding-learn-go-with-tests-excerpt-test]] - shared statements and technical atoms: Test shares source evidence from Testable Examples: Running the package's test suite, we can see the example ExampleAdd function is executed with no further arrangement from us:; Test shares technical record from Testable Examples: func ExampleAdd() { sum := Add(1, 5) fmt.Println(sum) // Output: 6 } (1 shared statement(s), 3 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-standard]] - shared statements and technical atoms: Standard shares source evidence from Testable Examples: To view example documentation, let's take a quick look at pkgsite . Before navigating to your project's directory, make sure you have installed pkgsite by running th ... [truncated]; Standard shares technical record from Testable Examples: If you publish your code with examples to a public URL, you can share the documentation of your code at pkg.go.dev. (2 shared statement(s), 2 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-library]] - shared statements and technical atoms: Library shares source evidence from Testable Examples: To view example documentation, let's take a quick look at pkgsite . Before navigating to your project's directory, make sure you have installed pkgsite by running th ... [truncated]; Library shares technical record from Testable Examples: If you publish your code with examples to a public URL, you can share the documentation of your code at pkg.go.dev. (1 shared statement(s), 1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-function]] - shared technical atoms: Function shares technical record from Testable Examples: func ExampleAdd() { sum := Add(1, 5) fmt.Println(sum) // Output: 6 } (3 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-comment]] - shared technical atoms: Comment shares technical record from Testable Examples: $ go test -v === RUN   TestAdder --- PASS: TestAdder (0.00s) === RUN   ExampleAdd --- PASS: ExampleAdd (0.00s) (1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-note]] - shared technical atoms: Note shares technical record from Arrays and their type / Write the minimal amount of code for the test to run and check the failing test output: ./sum_test.go:26:9: invalid operation: got != want (slice can only be compared to nil) (1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-try-run-test]] - shared technical atoms: Try and run the test shares technical record from Testable Examples: $ go test -v === RUN   TestAdder --- PASS: TestAdder (0.00s) === RUN   ExampleAdd --- PASS: ExampleAdd (0.00s) (1 shared atom(s))

## Source

- [[coding-learn-go-with-tests-excerpt]]
