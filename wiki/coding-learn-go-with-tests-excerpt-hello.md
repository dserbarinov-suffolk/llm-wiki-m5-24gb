---
page_id: coding-learn-go-with-tests-excerpt-hello
page_kind: concept
summary: Hello, World: 24 statement(s) and 6 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-29
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-hello@e69fffe06a8c9024649270c6246cb007
---

# Hello, World

What [[coding-learn-go-with-tests-excerpt]] covers about hello, world:

## Statements

### Hello, World

- It is traditional for your first program in a new language to be Hello, World. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00008))_

### Hello, World / How it works

- When you write a program in Go, you will have a main package defined with a main func inside it. Packages are ways of grouping up related Go code together. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00014))_

- The func keyword defines a function with a name and a body. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00015))_

- With import "fmt" we are importing a package which contains the Println function that we use to print. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00016))_

### Hello, World / How to test

- How do you test this? It is good to separate your "domain" code from the outside world (side-effects). The fmt.Println is a side effect (printing to stdout), and the string we send in is our domain. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00018))_

- We have created a new function with func , but this time, we've added another keyword, string, to the definition. This means this function returns a string . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00021))_

### Hello, World / Go modules?

- The next step is to run the tests. Enter go test in your terminal. If the tests pass, then you are probably using an earlier version of Go. However, if you are using Go 1.16 or later, the tests will likely not run. Instead, you will see an error message like this in the terminal: _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00025))_

- What's the problem? In a word, modules. Luckily, the problem is easy to fix. Enter go mod init example.com/hello in your terminal. That will create a new file with the following contents: _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00027))_

- This file tells the go tools essential information about your code. If you planned to distribute your application, you would include where the code was available for download as well as information about dependencies. The name of the module, example.com/hello, usually refers to a URL where the module can be found and downloaded. For compatibility with tools we'll start using soon, make sure your module's name has a dot somewhere in it, like the dot in .com of example.com/hello. For now, your module file is minimal, and you can leave it that way. To read more about modules, you can check out the reference in the Golang documentation. We can get back to testing and learning Go now since the tests should run, even on Go 1.16. In future chapters, you will need to run go mod init SOMENAME in each _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00029))_

### Hello, World / Back to Testing

- Run go test in your terminal. It should've passed! Just to check, try deliberately breaking the test by changing the want string. Notice how you have not had to pick between multiple testing frameworks and then figure out how to install them. Everything you need is built into the language, and the syntax is the same as the rest _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00032))_

- of the code you will write. Writing tests Writing a test is just like writing a function, with a few rules It needs to be in a file with a name like xxx_test.go The test function must start with the word Test The test function takes one argument only t *testing.T To use the *testing.T type, you need to import "testing" , like we did with fmt in the other file For now, it's enough to know that your t of type *testing.T is your "hook" into the testing framework so you can do things like t.Fail() when you want to fail. We've covered some new topics: if If statements in Go are very much like other programming languages. Declaring variables We're declaring some variables with the syntax varName := value , which lets us reuse some values in our test for readability. t.Errorf We are calling the method on our , which will print out a _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00033))_

- Errorf t message and fail the test. The f stands for format, which allows us to build a string with values inserted into the placeholder values %q . When you make the test fail, it should be clear how it works. You can read more about the placeholder strings in the fmt documentation. For tests, %q is very useful as it wraps your values in double quotes. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00034))_


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

### Technical frame 2: Hello, World / How to test

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00021))_

> We have created a new function with func , but this time, we've added another keyword, string, to the definition. This means this function returns a string .

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00020))_

```
package main
import "fmt"
func Hello() string {
    return "Hello, world"
}
func main() {
    fmt.Println(Hello())
}
```

### Technical frame 3: Hello, World / How to test

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00021))_

> We have created a new function with func , but this time, we've added another keyword, string, to the definition. This means this function returns a string .

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00023))_

```
package main
import "testing"
func TestHello(t *testing.T) {
    got := Hello()
    want := "Hello, world"
if got != want {
        t.Errorf("got %q want %q", got, want)
    }
}
```

### Technical frame 4: Hello, World / Go modules?

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00027))_

> What's the problem? In a word, modules. Luckily, the problem is easy to fix. Enter go mod init example.com/hello in your terminal. That will create a new file with the following contents:

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00026))_

```
$ go test
go: cannot find main module; see 'go help modules'
```

### Technical frame 5: Hello, World / Go modules?

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00029))_

> This file tells the go tools essential information about your code. If you planned to distribute your application, you would include where the code was available for download as well as information about dependencies. The name of the module, example.com/hello, usually refers to a URL where the module can be found and downloaded. For compatibility with tools we'll start using soon, make sure your module's name has a dot somewhere in it, like the dot in .com of example.com/hello. For now, your mod

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00028))_

```
module example.com/hello
go 1.16
```

### Technical frame 6: Hello, World / Go modules?

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00027))_

> What's the problem? In a word, modules. Luckily, the problem is easy to fix. Enter go mod init example.com/hello in your terminal. That will create a new file with the following contents:

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00029))_

> To read more about modules, you can check out the reference in the Golang documentation.


## Related pages

- [[coding-learn-go-with-tests-excerpt-module]] - shared statements and technical atoms: Go modules? shares source evidence from Hello, World / Go modules?: The next step is to run the tests. Enter go test in your terminal. If the tests pass, then you are probably using an earlier version of Go. However, if you are using ... [truncated]; Go modules? shares technical record from Hello, World / Go modules?: $ go test go: cannot find main module; see 'go help modules' (9 shared statement(s), 3 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-how-test]] - shared statements and technical atoms: How to test shares source evidence from Hello, World / How to test: How do you test this? It is good to separate your "domain" code from the outside world (side-effects). The fmt.Println is a side effect (printing to stdout), and the ... [truncated]; How to test shares technical record from Hello, World / How to test: package main import "fmt" func Hello() string { return "Hello, world" } func main() { fmt.Println(Hello()) } (4 shared statement(s), 2 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-test]] - shared statements and technical atoms: Test shares source evidence from Hello, World / Go modules?: The next step is to run the tests. Enter go test in your terminal. If the tests pass, then you are probably using an earlier version of Go. However, if you are using ... [truncated]; Test shares technical record from Hello, World / Go modules?: $ go test go: cannot find main module; see 'go help modules' (2 shared statement(s), 1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-code]] - shared statements: Code shares source evidence from Hello, World / Back to Testing: of the code you will write. Writing tests Writing a test is just like writing a function, with a few rules It needs to be in a file with a name like xxx_test.go The ... [truncated] (1 shared statement(s))
- [[coding-learn-go-with-tests-excerpt-package]] - shared statements: Package shares source evidence from Hello, World / How it works: When you write a program in Go, you will have a main package defined with a main func inside it. Packages are ways of grouping up related Go code together. (1 shared statement(s))
- [[coding-learn-go-with-tests-excerpt-section-hello-world-72ad81c1]] - source section: Hello, World shares source evidence from Hello, World: It is traditional for your first program in a new language to be Hello, World.; Hello, World shares technical record from Hello, World: package main import "fmt" func main() { fmt.Println("Hello, world") } (24 shared statement(s), 6 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-section-constants-hello-world-again-f51dc2d1]] - source section: Constants / Hello, world... again shares source evidence from Constants / Hello, world... again: The next requirement is when our function is called with an empty string it defaults to printing "Hello, World", rather than "Hello, ".; Constants / Hello, world... again shares technical record from Constants / Hello, world... again: func TestHello(t *testing.T) { t.Run("saying hello to people", func(t *testing.T) { got := Hello("Chris") want := "Hello, Chris" if got != want { t.Errorf("got %q wa ... [truncated] (17 shared statement(s), 6 shared atom(s))

## Source

- [[coding-learn-go-with-tests-excerpt]]
