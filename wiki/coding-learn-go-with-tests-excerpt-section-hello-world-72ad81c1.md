---
page_id: coding-learn-go-with-tests-excerpt-section-hello-world-72ad81c1
page_kind: source
summary: Hello, World: 38 source-backed entries and 3 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
page_family: section-reference
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-30
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-hello-world-72ad81c1@4e172590e4bb0d9c2d22ac456198ef3f
---

# Hello, World

From [[coding-learn-go-with-tests-excerpt]].

## Related pages

- [[coding-learn-go-with-tests-excerpt-section-hello-world-how-it-works-e2369fdb]] - narrower source section: Hello, World / How it works
- [[coding-learn-go-with-tests-excerpt-section-hello-world-how-to-test-b6606620]] - narrower source section: Hello, World / How to test
- [[coding-learn-go-with-tests-excerpt-section-hello-world-go-modules-3cb7c993]] - narrower source section: Hello, World / Go modules?
- [[coding-learn-go-with-tests-excerpt-section-hello-world-back-to-testing-7ab34920]] - narrower source section: Hello, World / Back to Testing
- [[coding-learn-go-with-tests-excerpt-section-learn-go-with-tests-go-fundamentals-excerpt-0faa888c]] - previous source section: Learn Go with Tests -- Go Fundamentals (Excerpt)
- [[coding-learn-go-with-tests-excerpt-section-go-s-documentation-38415959]] - next source section: Go's documentation

## Statements

- It is traditional for your first program in a new language to be Hello, World. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00008))_

## Statements by subsection

### Hello, World / How it works

- When you write a program in Go, you will have a main package defined with a main func inside it. Packages are ways of grouping up related Go code together. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00014))_
- The func keyword defines a function with a name and a body. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00015))_
- With import "fmt" we are importing a package which contains the Println function that we use to print. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00016))_
- When you write a program in Go, you will have a main package defined with a main func inside it. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00014))_

### Hello, World / How to test

- How do you test this? It is good to separate your "domain" code from the outside world (side-effects). The fmt.Println is a side effect (printing to stdout), and the string we send in is our domain. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00018))_
- We have created a new function with func , but this time, we've added another keyword, string, to the definition. This means this function returns a string . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00021))_
- This means this function returns a string . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00021))_

### Hello, World / Go modules?

- The next step is to run the tests. Enter go test in your terminal. If the tests pass, then you are probably using an earlier version of Go. However, if you are using Go 1.16 or later, the tests will likely not run. Instead, you will see an error message like this in the terminal: _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00025))_
- What's the problem? In a word, modules. Luckily, the problem is easy to fix. Enter go mod init example.com/hello in your terminal. That will create a new file with the following contents: _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00027))_
- This file tells the go tools essential information about your code. If you planned to distribute your application, you would include where the code was available for download as well as information about dependencies. The name of the module, example.com/hello, usually refers to a URL where the module can be found and downloaded. For compatibility with tools we'll start using soon, make sure your module's name has a dot somewhere in it, like the dot in .com of example.com/hello. For now, your module file is minimal, and you can leave it that way. To read more about modules, you can check out the reference in the Golang documentation. We can get back to testing and learning Go now since the tests should run, even on Go 1.16. In future chapters, you will need to run go mod init SOMENAME in each _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00029))_
- If the tests pass, then you are probably using an earlier version of Go. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00025))_
- The name of the module, example.com/hello, usually refers to a URL where the module can be found and downloaded. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00029))_
- new folder before running commands like go test or go build . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00030))_

### Hello, World / Back to Testing

- Run go test in your terminal. It should've passed! Just to check, try deliberately breaking the test by changing the want string. Notice how you have not had to pick between multiple testing frameworks and then figure out how to install them. Everything you need is built into the language, and the syntax is the same as the rest _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00032))_
- of the code you will write. Writing tests Writing a test is just like writing a function, with a few rules It needs to be in a file with a name like xxx_test.go The test function must start with the word Test The test function takes one argument only t *testing.T To use the *testing.T type, you need to import "testing" , like we did with fmt in the other file For now, it's enough to know that your t of type *testing.T is your "hook" into the testing framework so you can do things like t.Fail() when you want to fail. We've covered some new topics: if If statements in Go are very much like other programming languages. Declaring variables We're declaring some variables with the syntax varName := value , which lets us reuse some values in our test for readability. t.Errorf We are calling the method on our , which will print out a _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00033))_
- Errorf t message and fail the test. The f stands for format, which allows us to build a string with values inserted into the placeholder values %q . When you make the test fail, it should be clear how it works. You can read more about the placeholder strings in the fmt documentation. For tests, %q is very useful as it wraps your values in double quotes. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00034))_
- Notice how you have not had to pick between multiple testing frameworks and then figure out how to install them. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00032))_
- Writing tests Writing a test is just like writing a function, with a few rules It needs to be in a file with a name like xxx_test.go The test function must start with the word Test The test function takes one argument only t *testing.T To use the *testing.T type, you need to import "testing" , like we did with fmt in the other file For now, it's enough to know that your t of type *testing.T is your "hook" into the testing framework so you can do things like t.Fail() when you want to fail. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00033))_

## Technical atoms

### Technical frame 1: Hello, World

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00008))_

> It is traditional for your first program in a new language to be Hello, World.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00011))_

```
package main
import "fmt"
func main() {
    fmt.Println("Hello, world")
}
```

### Technical frame 2: Hello, World / Go modules?

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00029))_

> This file tells the go tools essential information about your code. If you planned to distribute your application, you would include where the code was available for download as well as information about dependencies. The name of the module, example.com/hello, usually refers to a URL where the module can be found and downloaded. For compatibility with tools we'll start using soon, make sure your module's name has a dot somewhere in it, like the dot in .com of example.com/hello. For now, your mod

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00028))_

```
module example.com/hello
go 1.16
```

### Technical frame 3: Hello, World / Go modules?

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00027))_

> What's the problem? In a word, modules. Luckily, the problem is easy to fix. Enter go mod init example.com/hello in your terminal. That will create a new file with the following contents:

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00029))_

> To read more about modules, you can check out the reference in the Golang documentation.
