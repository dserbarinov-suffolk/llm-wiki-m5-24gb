---
page_id: coding-learn-go-with-tests-excerpt
page_kind: source
summary: Claim-ledger projection (coding): 640 usable entries, 191 technical atoms, 92 needs-review, 153 linked page(s); write decision write-with-review-work.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-29
domain: coding-learn-go-with-tests-excerpt
category_path: sources
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: projection-coverage-372fd2dad6def8ac@671db9d1aa9a2d3d
---

# Learn Go with Tests (Excerpt)

## Learn Go with Tests (Excerpt)

- Decoupling Further refactoring Write the test first Try to run the test Write the minimal amount of code for the test to run and check the failing test output Write enough code to make it pass Refactor Make sure your test output is helpful Wrapping up Maps Write the test first Try to run the test Write the minimal amount of code for the test to run and check the output Write enough code to make it pass Refactor Using a custom type Write the test first Try and run the test Write the minimal amount of code for the test to run and check the output Write enough code to make it pass Refactor Write the test first Write the minimal amount of code for the test to run and check output Write enough code to make it pass Pointers, copies, et al Refactor Write the test first Try to run test Write the minimal amount of code for the test to run and check the _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00002))_

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

## Learn Go with Tests -- Go Fundamentals (Excerpt)

- Excerpt assembled from github.com/quii/learn-go-with-tests, covering Go language fundamentals for cross-source comparison. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00005))_

## Hello, World

- It is traditional for your first program in a new language to be Hello, World. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00008))_

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00010))_

> Put a new file in it called hello.go and put the following code inside it

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00011))_

```
package main
import "fmt"
func main() {
    fmt.Println("Hello, world")
}
```

### How it works

- Packages are ways of grouping up related Go code together. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00014))_
- When you write a program in Go, you will have a main package defined with a main func inside it. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00014))_
- When you write a program in Go, you will have a main package defined with a main func inside it. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00014))_
- The func keyword defines a function with a name and a body. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00015))_
- With import "fmt" we are importing a package which contains the Println function that we use to print. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00016))_

### How to test

- It is good to separate your "domain" code from the outside world (side-effects). _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00018))_
- The fmt.Println is a side effect (printing to stdout), and the string we send in is our domain. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00018))_
- This means this function returns a string . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00021))_
- We have created a new function with func , but this time, we've added another keyword, string, to the definition. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00021))_
- This means this function returns a string . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00021))_

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

### Go modules?

- However, if you are using Go 1.16 or later, the tests will likely not run. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00025))_
- The next step is to run the tests. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00025))_
- If the tests pass, then you are probably using an earlier version of Go. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00025))_
- If the tests pass, then you are probably using an earlier version of Go. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00025))_
- Luckily, the problem is easy to fix. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00027))_
- The name of the module, example.com/hello, usually refers to a URL where the module can be found and downloaded. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00029))_
- For now, your module file is minimal, and you can leave it that way. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00029))_
- In future chapters, you will need to run go mod init SOMENAME in each _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00029))_
- For compatibility with tools we'll start using soon, make sure your module's name has a dot somewhere in it, like the dot in .com of example.com/hello. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00029))_
- We can get back to testing and learning Go now since the tests should run, even on Go 1.16. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00029))_
- The name of the module, example.com/hello, usually refers to a URL where the module can be found and downloaded. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00029))_
- new folder before running commands like go test or go build . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00030))_

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00025))_

> The next step is to run the tests. Enter go test in your terminal. If the tests pass, then you are probably using an earlier version of Go. However, if you are using Go 1.16 or later, the tests will likely not run. Instead, you will see an error message like this in the terminal:

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00026))_

```
$ go test
go: cannot find main module; see 'go help modules'
```

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00027))_

> What's the problem? In a word, modules. Luckily, the problem is easy to fix. Enter go mod init example.com/hello in your terminal. That will create a new file with the following contents:

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00028))_

```
module example.com/hello
go 1.16
```

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00027))_

> What's the problem? In a word, modules. Luckily, the problem is easy to fix. Enter go mod init example.com/hello in your terminal. That will create a new file with the following contents:

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00029))_

> To read more about modules, you can check out the reference in the Golang documentation.

### Back to Testing

- Notice how you have not had to pick between multiple testing frameworks and then figure out how to install them. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00032))_
- Notice how you have not had to pick between multiple testing frameworks and then figure out how to install them. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00032))_
- of the code you will write. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00033))_
- Writing tests Writing a test is just like writing a function, with a few rules It needs to be in a file with a name like xxx_test.go The test function must start with the word Test The test function takes one argument only t *testing.T To use the *testing.T type, you need to import "testing" , like we did with fmt in the other file For now, it's enough to know that your t of type *testing.T is your "hook" into the testing framework so you can do things like t.Fail() when you want to fail. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00033))_
- Writing tests Writing a test is just like writing a function, with a few rules It needs to be in a file with a name like xxx_test.go The test function must start with the word Test The test function takes one argument only t *testing.T To use the *testing.T type, you need to import "testing" , like we did with fmt in the other file For now, it's enough to know that your t of type *testing.T is your "hook" into the testing framework so you can do things like t.Fail() when you want to fail. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00033))_
- When you make the test fail, it should be clear how it works. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00034))_
- You can read more about the placeholder strings in the fmt documentation. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00034))_
- The f stands for format, which allows us to build a string with values inserted into the placeholder values %q . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00034))_
- For tests, %q is very useful as it wraps your values in double quotes. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00034))_

## Go's documentation

- We just saw the documentation for the fmt package at the official package viewing website, and Go also provides ways for quickly getting at the documentation offline. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00037))_
- Another quality-of-life feature of Go is the documentation. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00037))_
- Go has a built-in tool, doc, which lets you examine any package installed on your system, or the module you're currently working on. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00038))_
- For a default installation of Go, that executable will be in $HOME/go/bin for Linux and macOS, and %USERPROFILE%\go\bin for Windows. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00040))_
- If you have not already added those paths to your $PATH var, you might want to do so to make running go-installed commands easier. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00040))_
- Go's second tool for viewing documentation is the pkgsite command, which powers Go's official package viewing website. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00040))_
- You can install pkgsite with go install golang.org/x/pkgsite/cmd/pkgsite@latest , then run it with pkgsite -open . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00040))_
- You can install pkgsite with go install golang.org/x/pkgsite/cmd/pkgsite@latest , then run it with pkgsite -open . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00040))_
- The vast majority of the standard library has excellent documentation with examples. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00041))_

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00038))_

> Go has a built-in tool, doc, which lets you examine any package installed on your system, or the module you're currently working on. To view that same documentation for the Printing verbs:

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

## Hello, YOU

- Now that we have a test, we can iterate on our software safely. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00043))_
- In the last example, we wrote the test after the code had been written so that you could get an example of how to write a test and declare a function. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00044))_
- In the last example, we wrote the test after the code had been written so that you could get an example of how to write a test and declare a function. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00044))_
- This is basic testdriven development and allows us to make sure our test is actually testing what we want. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00046))_
- When using a statically typed language like Go it is important to listen to the compiler . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00051))_
- The compiler understands how your code should snap together and work so you don't have to. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00051))_
- We have to change our function Hello to accept an argument. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00052))_
- In this case the compiler is telling you what you need to do to continue. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00052))_
- If you try and run your tests again your hello.go will fail to compile because you're not passing an argument. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00055))_
- Send in "world" to make it compile. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00055))_
- If you try and run your tests again your hello.go will fail to compile because you're not passing an argument. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00055))_
- We finally have a compiling program but it is not meeting our requirements according to the test. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00059))_
- Normally, as part of the TDD cycle, we should now refactor . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00062))_

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00045))_

> Our next requirement is to let us specify the recipient of the greeting.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00046))_

> When you retrospectively write tests, there is the risk that your test may continue to pass even if the code doesn't work as intended.

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00045))_

> Our next requirement is to let us specify the recipient of the greeting.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00048))_

```
import "testing"
func TestHello(t *testing.T) {
    got := Hello("Chris")
    want := "Hello, Chris"
if got != want {
        t.Errorf("got %q want %q", got, want)
    }
}
```

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00050))_

```
./hello_test.go:6:18: too many arguments in call to Hello
have (string)
   want ()
```

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00051, source-range-cb73a893-00055))_

> When using a statically typed language like Go it is important to listen to the compiler . The compiler understands how your code should snap together and work so you don't have to. If you try and run your tests again your hello.go will fail to compile because you're not passing an argument. Send in "world" to make it compile.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00054))_

```
func Hello(name string) string {
    return "Hello, world"
}
```

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00055))_

> If you try and run your tests again your hello.go will fail to compile because you're not passing an argument. Send in "world" to make it compile.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00056))_

```
func main() {
    fmt.Println(Hello("world"))
}
```

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00055))_

> If you try and run your tests again your hello.go will fail to compile because you're not passing an argument. Send in "world" to make it compile.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00057))_

> Now when you run your tests, you should see something like

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00055))_

> If you try and run your tests again your hello.go will fail to compile because you're not passing an argument. Send in "world" to make it compile.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00058))_

```
hello_test.go:10: got 'Hello, world' want 'Hello, Chris''
```

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00060))_

> Let's make the test pass by using the name argument and concatenate it with Hello,

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00061))_

```
func Hello(name string) string {
    return "Hello, " + name
}
```

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00060))_

> Let's make the test pass by using the name argument and concatenate it with Hello,

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00062))_

> When you run the tests, they should now pass.

## A note on source control

- At this point, if you are using source control (which you should!) I would commit the code as it is. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00064))_
- It is nice to commit at this point in case you somehow get into a mess with refactoring - you can always go back to the working version. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00065))_
- I wouldn't push to main though, because I plan to refactor next. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00065))_
- There's not a lot to refactor here, but we can introduce another language feature, constants . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00066))_

## Constants

- After refactoring, re-run your tests to make sure you haven't broken anything. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00069))_
- After refactoring, re-run your tests to make sure you haven't broken anything. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00069))_

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00068))_

```
Constants are deﬁned like so
const englishHelloPrefix = "Hello, "
We can now refactor our code
const englishHelloPrefix = "Hello, "
func Hello(name string) string {
    return englishHelloPrefix + name
}
```

### Hello, world... again

- The next requirement is when our function is called with an empty string it defaults to printing "Hello, World", rather than "Hello, ". _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00072))_
- The next requirement is when our function is called with an empty string it defaults to printing "Hello, World", rather than "Hello, ". _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00072))_
- Here, we are introducing another tool in our testing arsenal: subtests. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00075))_
- Sometimes, it is useful to group tests around a "thing" and then have subtests describing different scenarios. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00075))_
- Sometimes, it is useful to group tests around a "thing" and then have subtests describing different scenarios. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00075))_
- A benefit of this approach is you can set up shared code that can be used in the other tests. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00076))_
- If we run our tests we should see it satisfies the new requirement and we haven't accidentally broken the other functionality. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00080))_
- But there is repeated code when we check if the message is what we expect. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00081))_
- It is important that your tests are clear specifications of what the code needs to do. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00081))_
- Refactoring is not just for the production code! _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00082))_
- Now that the tests are passing, we can and should refactor our tests. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00083))_
- We need to pass in t *testing.T so that we can tell the test code to fail when we need to. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00086))_
- We've refactored our assertion into a new function. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00086))_
- This will help other developers track down problems more easily. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00088))_
- You should see that line turn grey or change to another color than the rest of your code to indicate it's now commented out. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00088))_
- Comments in Go are a great way to add additional information to your code, or in this case, a quick way to tell the compiler to ignore a line. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00088))_
- t.Helper() is needed to tell the test suite that this method is a helper. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00088))_
- By doing this, when it fails, the line number reported will be in our function call rather than inside our test helper. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00088))_
- If you still don't understand, comment it out, make a test fail and observe the test output. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00088))_
- By doing this, when it fails, the line number reported will be in our function call rather than inside our test helper. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00088))_

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00074))_

```
func TestHello(t *testing.T) {
    t.Run("saying hello to people", func(t *testing.T) {
        got := Hello("Chris")
        want := "Hello, Chris"
if got != want {
            t.Errorf("got %q want %q", got, want)
        }
    })
    t.Run("say 'Hello, World' when an empty string is supplied", 
func(t *testing.T) {
got := Hello("")
        want := "Hello, World"
if got != want {
            t.Errorf("got %q want %q", got, want)
        }
    })
}
```

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00077))_

> While we have a failing test, let's fix the code, using an if .

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00078))_

```
const englishHelloPrefix = "Hello, "
func Hello(name string) string {
    if name == "" {
```

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00077))_

> While we have a failing test, let's fix the code, using an if .

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00079))_

```
name = "World"
    }
    return englishHelloPrefix + name
}
```

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00083))_

> Now that the tests are passing, we can and should refactor our tests.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00084))_

```
func TestHello(t *testing.T) {
    t.Run("saying hello to people", func(t *testing.T) {
        got := Hello("Chris")
        want := "Hello, Chris"
        assertCorrectMessage(t, got, want)
    })
t.Run("empty string defaults to 'world'", func(t *testing.T) {
        got := Hello("")
        want := "Hello, World"
        assertCorrectMessage(t, got, want)
    })
}
func assertCorrectMessage(t testing.TB, got, want string) {
    t.Helper()
    if got != want {
        t.Errorf("got %q want %q", got, want)
    }
}
```

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00086, source-range-cb73a893-00088))_

> We've refactored our assertion into a new function. This reduces duplication and improves the readability of our tests. We need to pass in t *testing.T so that we can tell the test code to fail when we need to. t.Helper() is needed to tell the test suite that this method is a helper. By doing this, when it fails, the line number reported will be in our function call rather than inside our test helper. This will help other developers track down problems more easily. If you still don't understand,

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00087))_

> For helper functions, it's a good idea to accept a testing.TB which is an interface that *testing.T and *testing.B both satisfy, so you can call helper functions from a test, or a benchmark (don't worry if words like "interface" mean nothing to you right now, it will be covered later).

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00086))_

> We've refactored our assertion into a new function. This reduces duplication and improves the readability of our tests. We need to pass in t *testing.T so that we can tell the test code to fail when we need to.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00089))_

> When you have more than one argument of the same type (in our case two strings) rather than having (got string, want string) you can shorten it to (got, want string) .

## Back to source control

- Now that we are happy with the code, I would amend the previous commit so that we only check in the lovely version of our code with its test. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00091))_
- Now that we are happy with the code, I would amend the previous commit so that we only check in the lovely version of our code with its test. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00091))_

## Discipline

- On the face of it this may seem tedious but sticking to the feedback loop is important. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00099))_
- Not only does it ensure that you have relevant tests , it helps ensure you design good software by refactoring with the safety of tests. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00100))_
- Not only does it ensure that you have relevant tests , it helps ensure you design good software by refactoring with the safety of tests. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00100))_
- Seeing the test fail is an important check because it also lets you see what the error message looks like. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00101))_
- Seeing the test fail is an important check because it also lets you see what the error message looks like. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00101))_
- By not writing tests, you are committing to manually checking your code by running your software, which breaks your state of flow. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00103))_
- You won't be saving yourself any time, especially in the long run. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00103))_

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00101))_

> As a developer it can be very hard to work with a codebase when failing tests do not give a clear idea as to what the problem is.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00102))_

> By ensuring your tests are fast and setting up your tools so that running tests is simple you can get in to a state of flow when writing your code.

### Keep going! More requirements

- If a language is passed in that we do not recognise, just default to English. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00105))_
- Goodness me, we have more requirements. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00105))_
- We now need to support a second parameter, specifying the language of the greeting. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00105))_
- We should be confident that we can easily use TDD to flesh out this functionality! _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00106))_
- When you try and run the test again it will complain about not passing through enough arguments to Hello in your other tests and in hello.go _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00113))_
- The tests should now pass. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00119))_
- Now it is time to refactor . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00120))_
- Try and refactor it yourself, with every change make sure you re-run the tests to make sure your refactoring isn't breaking anything. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00120))_
- You should see some problems in the code, "magic" strings, some of which are repeated. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00120))_

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00106, source-range-cb73a893-00109))_

> We should be confident that we can easily use TDD to flesh out this functionality! Remember not to cheat! Test first . When you try to run the test, the compiler should complain because you are calling Hello with two arguments rather than one.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00108))_

```
t.Run("in Spanish", func(t *testing.T) {
        got := Hello("Elodie", "Spanish")
        want := "Hola, Elodie"
        assertCorrectMessage(t, got, want)
    })
```

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00106))_

> We should be confident that we can easily use TDD to flesh out this functionality!

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00109))_

> When you try to run the test, the compiler should complain because you are calling Hello with two arguments rather than one.

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00109))_

> Remember not to cheat! Test first . When you try to run the test, the compiler should complain because you are calling Hello with two arguments rather than one.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00110))_

```
./hello_test.go:27:19: too many arguments in call to Hello
have (string, string)
   want (string)
```

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00109))_

> Remember not to cheat! Test first . When you try to run the test, the compiler should complain because you are calling Hello with two arguments rather than one.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00112))_

```
func Hello(name string, language string) string {
    if name == "" {
        name = "World"
    }
    return englishHelloPrefix + name
}
```

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00113))_

> When you try and run the test again it will complain about not passing through enough arguments to Hello in your other tests and in hello.go

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00114))_

```
./hello.go:15:19: not enough arguments in call to Hello
have (string)
   want (string, string)
```

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00113))_

> When you try and run the test again it will complain about not passing through enough arguments to Hello in your other tests and in hello.go

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00115))_

> Now all your tests should compile and pass, apart from our new scenario

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00113))_

> When you try and run the test again it will complain about not passing through enough arguments to Hello in your other tests and in hello.go

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00116))_

```
hello_test.go:29: got 'Hello, Elodie' want 'Hola, Elodie'
```

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00117))_

> We can use if here to check the language is equal to "Spanish" and if so change the message

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00118))_

```
func Hello(name string, language string) string {
    if name == "" {
        name = "World"
    }
if language == "Spanish" {
        return "Hola, " + name
    }
    return englishHelloPrefix + name
}
```

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00120))_

> Now it is time to refactor . You should see some problems in the code, "magic" strings, some of which are repeated. Try and refactor it yourself, with every change make sure you re-run the tests to make sure your refactoring isn't breaking anything.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00121))_

```
const spanish = "Spanish"
    const englishHelloPrefix = "Hello, "
    const spanishHelloPrefix = "Hola, "
func Hello(name string, language string) string {
        if name == "" {
            name = "World"
        }
if language == spanish {
            return spanishHelloPrefix + name
        }
        return englishHelloPrefix + name
    }
```

## French

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00128))_

```
func Hello(name string, language string) string {
```

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00129))_

```
if name == "" {
        name = "World"
    }
if language == spanish {
        return spanishHelloPrefix + name
    }
    if language == french {
        return frenchHelloPrefix + name
    }
    return englishHelloPrefix + name
}
```

#### switch

- We can use switch to refactor the code to make it easier to read and more extensible if we wish to add more language support later _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00131))_
- When you have lots of if statements checking a particular value it is common to use a switch statement instead. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00131))_
- Write a test to now include a greeting in the language of your choice and you should see how simple it is to extend our amazing function. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00133))_

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00131))_

> When you have lots of if statements checking a particular value it is common to use a switch statement instead. We can use switch to refactor the code to make it easier to read and more extensible if we wish to add more language support later

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00132))_

```
func Hello(name string, language string) string {
    if name == "" {
        name = "World"
    }
prefix := englishHelloPrefix
switch language {
    case spanish:
        prefix = spanishHelloPrefix
    case french:
        prefix = frenchHelloPrefix
    }
return prefix + name
}
```

## one...last...refactor?

- The simplest refactor for this would be to extract out some functionality into another function. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00135))_
- You could argue that maybe our function is getting a little big. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00135))_
- - In our function signature we have made a named return value (prefix string) . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00140))_
- - This will create a variable called prefix in your function. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00141))_
- - It will be assigned the "zero" value. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00142))_
- This depends on the type, for example int s are 0 and for string s it is "" . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00142))_
- This depends on the type, for example int s are 0 and for string s it is "" . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00142))_
- - This will display in the Go Doc for your function so it can make the intent of your code clearer. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00144))_
- - default in the switch case will be branched to if none of the other case statements match. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00145))_
- We don't want the internals of our algorithm exposed to the world, so we made this function private. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00146))_
- For readability, it's a good idea to use a line between sets of related constants. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00147))_
- - Also, we can group constants in a block instead of declaring them on their own line. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00147))_

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00136))_

```
const (
    spanish = "Spanish"
    french  = "French"
englishHelloPrefix = "Hello, "
    spanishHelloPrefix = "Hola, "
    frenchHelloPrefix  = "Bonjour, "
)
func Hello(name string, language string) string {
    if name == "" {
        name = "World"
    }
return greetingPrefix(language) + name
```

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00137))_

```
}
func greetingPrefix(language string) (prefix string) {
    switch language {
    case french:
        prefix = frenchHelloPrefix
    case spanish:
        prefix = spanishHelloPrefix
    default:
        prefix = englishHelloPrefix
    }
    return
```

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00138))_

```
}
```

### Wrapping up

## Some of Go's syntax around

## The TDD process and why the steps are important

- - Write a failing test and see it fail so we know we have written a relevant test for our requirements and seen that it produces an easy to understand description of the failure _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00157))_
- - Then refactor, backed with the safety of our tests to ensure we have well-crafted code that is easy to work with _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00159))_
- - Then refactor, backed with the safety of our tests to ensure we have well-crafted code that is easy to work with _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00159))_
- In our case, we've gone from Hello() to Hello("name") and then to Hello("name", "French") in small, easy-to-understand steps. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00160))_
- TDD is a skill that needs practice to develop, but by breaking problems down into smaller components that you can test, you will have a much easier time writing software. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00161))_

## Integers

- Integers work as you would expect. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00164))_
- Create a test file called adder_test.go and write this code. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00164))_
- Note: Go source files can only have one package per directory. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00165))_
- Here is a good explanation on this. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00165))_
- Note: Go source files can only have one package per directory. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00165))_

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00166))_

> Your project directory might look something like this:

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00167))_

```
learnGoWithTests
|
   |-> helloworld
   |    |- hello.go
   |    |- hello_test.go
   |
   |-> integers
   |    |- adder_test.go
   |
   |- go.mod
   |- README.md
```

### Write the test first

- You will notice that we're using %d as our format strings rather than %q . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00170))_
- That's because we want it to print an integer rather than a string. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00170))_
- Also note that we are no longer using the main package, instead we've defined a package named integers , as the name suggests this will group functions for working with integers such as Add . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00171))_
- Also note that we are no longer using the main package, instead we've defined a package named integers , as the name suggests this will group functions for working with integers such as Add . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00171))_

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00170))_

> You will notice that we're using %d as our format strings rather than %q . That's because we want it to print an integer rather than a string.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00169))_

```
package integers
import "testing"
func TestAdder(t *testing.T) {
    sum := Add(2, 2)
    expected := 4
if sum != expected {
        t.Errorf("expected '%d' but got '%d'", expected, sum)
    }
}
```

### Try and run the test

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00173))_

```
Run the test go test
Inspect the compilation error
./adder_test.go:6:9: undefined: Add
```

### Write the minimal amount of code for the test to run and check the failing test output

- Now run the tests, and we should be happy that the test is correctly reporting what is wrong. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00178))_
- You can refer this wiki for more details. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00180))_
- It should generally be used when the meaning of the result isn't clear from context, in our case it's pretty much clear that Add function will add the parameters. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00180))_
- If you have noticed we learnt about named return value in the last section but aren't using the same here. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00180))_

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00176))_

```
package integers
func Add(x, y int) int {
    return 0
}
```

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00177))_

> Remember, when you have more than one argument of the same type (in our case two integers) rather than having (x int, y int) you can shorten it to (x, y int) .

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00180))_

> If you have noticed we learnt about named return value in the last section but aren't using the same here. It should generally be used when the meaning of the result isn't clear from context, in our case it's pretty much clear that Add function will add the parameters. You can refer this wiki for more details.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00179))_

```
adder_test.go:10: expected '4' but got '0'
```

### Write enough code to make it pass

- In the strictest sense of TDD we should now write the minimal amount of code to make the test pass . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00182))_
- Once we're more familiar with Go's syntax I will introduce a technique called "Property Based Testing" , which would stop annoying developers and help you find bugs. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00186))_

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00183))_

```
func Add(x, y int) int {
    return 4
}
```

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00188))_

```
func Add(x, y int) int {
    return x + y
}
```

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00189))_

> If you re-run the tests they should pass.

### Refactor

- There's not a lot in the actual code we can really improve on here. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00191))_
- This is great because it aids the usability of code you are writing. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00193))_
- This is great because it aids the usability of code you are writing. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00193))_

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00191))_

> There's not a lot in the actual code we can really improve on here.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00194))_

> You can add documentation to functions with comments, and these will appear in Go Doc just like when you look at the standard library's documentation.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00195))_

```
// Add takes two integers and returns the sum of them.
func Add(x, y int) int {
    return x + y
}
```

## Testable Examples

- You will find many examples in the standard library documentation. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00197))_
- Example functions are compiled whenever tests are executed. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00199))_
- It is strongly recommended you research how to have these kind of errors fixed for you automatically in whatever editor you are using.) _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00202))_
- (If your editor doesn't automatically import packages for you, the compilation step will fail because you will be missing import "fmt" in adder_test.go . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00202))_
- (If your editor doesn't automatically import packages for you, the compilation step will fail because you will be missing import "fmt" in adder_test.go . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00202))_
- Adding this code will cause the example to appear in your documentation, making your code even more accessible. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00203))_
- If ever your code changes so that the example is no longer valid, your build will fail. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00203))_
- Running the package's test suite, we can see the example ExampleAdd function is executed with no further arrangement from us: _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00204))_
- Go ahead and temporarily remove the comment // Output: 6 , then run go test , and you will see ExampleAdd is no longer executed. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00206))_
- While the example will always be compiled, adding this comment means the example will also be executed. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00206))_
- While the example will always be compiled, adding this comment means the example will also be executed. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00206))_
- Go ahead and temporarily remove the comment // Output: 6 , then run go test , and you will see ExampleAdd is no longer executed. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00206))_
- Examples without output comments are useful for demonstrating code that cannot run as unit tests, such as that which accesses the network, while guaranteeing the example at least compiles. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00207))_
- Examples without output comments are useful for demonstrating code that cannot run as unit tests, such as that which accesses the network, while guaranteeing the example at least compiles. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00207))_
- Before navigating to your project's directory, make sure you have installed pkgsite by running the following command: go install golang.org/x/pkgsite/cmd/pkgsite@latest , then run pkgsite -open . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00208))_
- Inside here you'll see a list of all of Go's Standard Library packages, plus Third Party packages you have installed, under which you should see your example documentation for github.com/quii/learn-go-with-tests . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00208))_
- Follow that link, and then look under Integers , then under func Add , then expand Example and you should see the example you added for sum := Add(1, 5) . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00208))_
- Inside here you'll see a list of all of Go's Standard Library packages, plus Third Party packages you have installed, under which you should see your example documentation for github.com/quii/learn-go-with-tests . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00208))_
- Follow that link, and then look under Integers , then under func Add , then expand Example and you should see the example you added for sum := Add(1, 5) . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00208))_
- Before navigating to your project's directory, make sure you have installed pkgsite by running the following command: go install golang.org/x/pkgsite/cmd/pkgsite@latest , then run pkgsite -open . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00208))_
- This web interface allows you to search for documentation of standard library packages and third-party packages. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00209))_
- For example, here is the finalised API for this chapter. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00209))_
- For example, here is the finalised API for this chapter. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00209))_

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00198))_

> Often code examples that can be found outside the codebase, such as a readme file, become out of date and incorrect compared to the actual code because they don't get checked.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00197))_

> If you really want to go the extra mile you can make Testable Examples.

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00200, source-range-cb73a893-00202))_

> Example functions begin with Example (much like test functions begin with Test ), and reside in a package's _test.go files. Add the following ExampleAdd function to the adder_test.go file. (If your editor doesn't automatically import packages for you, the compilation step will fail because you will be missing import "fmt" in adder_test.go . It is strongly recommended you research how to have these kind of errors fixed for you automatically in whatever editor you are using.)

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00201))_

```
func ExampleAdd() {
    sum := Add(1, 5)
    fmt.Println(sum)
    // Output: 6
}
```

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00204, source-range-cb73a893-00206))_

> Running the package's test suite, we can see the example ExampleAdd function is executed with no further arrangement from us: Notice the special format of the comment, // Output: 6 . While the example will always be compiled, adding this comment means the example will also be executed. Go ahead and temporarily remove the comment // Output: 6 , then run go test , and you will see ExampleAdd is no longer executed.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00205))_

```
$ go test -v
=== RUN   TestAdder
--- PASS: TestAdder (0.00s)
=== RUN   ExampleAdd
--- PASS: ExampleAdd (0.00s)
```

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00208))_

> To view example documentation, let's take a quick look at pkgsite . Before navigating to your project's directory, make sure you have installed pkgsite by running the following command: go install golang.org/x/pkgsite/cmd/pkgsite@latest , then run pkgsite -open . , which should open a web browser for you, pointing to http://localhost:8080 . Inside here you'll see a list of all of Go's Standard Library packages, plus Third Party packages you have installed, under which you should see your example

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00209))_

> If you publish your code with examples to a public URL, you can share the documentation of your code at pkg.go.dev.

### Wrapping up

- - Writing better documentation so users of our code can understand its usage quickly _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00214))_

## Iteration

- Which is a good thing! _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00218))_
- To do stuff repeatedly in Go, you'll need for . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00218))_
- In Go there are no while , do , until keywords, you can only use for . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00218))_
- In Go there are no while , do , until keywords, you can only use for . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00218))_

### Write the test first

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00222))_

```
package iteration
import "testing"
func TestRepeat(t *testing.T) {
    repeated := Repeat("a")
    expected := "aaaaa"
if repeated != expected {
        t.Errorf("expected %q but got %q", expected, repeated)
    }
}
```

### Try and run the test

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00224))_

```
./repeat_test.go:6:14: undefined: Repeat
```

### Write the minimal amount of code for the test to run and check the failing test output

- You don't need to know anything new right now to make the test fail properly. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00226))_
- All you need to do right now is enough to make it compile so you can check your test is written well. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00227))_
- This means you can now play with the production code as much as you like and know it's behaving as you'd hope. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00229))_
- This means you can now play with the production code as much as you like and know it's behaving as you'd hope. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00229))_

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00228))_

```
package iteration
func Repeat(character string) string {
    return ""
}
```

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00230))_

```
repeat_test.go:10: expected 'aaaaa' but got ''
```

### Write enough code to make it pass

- The for syntax is very unremarkable and follows most C-like languages. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00232))_
- Here we are declaring a string variable only. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00236))_
- However, := is simply short hand for both steps. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00236))_
- We can also use var to declare functions, as we'll see later on. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00236))_
- as we've been using := so far to declare and initializing variables. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00236))_
- Here we are declaring a string variable only. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00236))_
- Hence, the explicit version. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00236))_
- Run the test and it should pass. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00237))_
- Additional variants of the for loop are described here. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00238))_

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00233))_

```
func Repeat(character string) string {
    var repeated string
    for i := 0; i < 5; i++ {
        repeated = repeated + character
    }
    return repeated
}
```

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00235))_

```
var repeated string
```

### Refactor

- += called "the Add AND assignment operator" , adds the right operand to the left operand and assigns the result to left operand. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00242))_

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00242))_

> += called "the Add AND assignment operator" , adds the right operand to the left operand and assigns the result to left operand. It works with other types like integers.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00241))_

```
const repeatCount = 5
func Repeat(character string) string {
    var repeated string
    for i := 0; i < repeatCount; i++ {
        repeated += character
    }
    return repeated
}
```

## Benchmarking

- Loop() returns true as long as the benchmark should continue running. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00247))_
- The testing.B gives you access to the loop function. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00247))_
- After Loop() returns false, b.N contains the total number of iterations that ran. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00248))_
- After Loop() returns false, b.N contains the total number of iterations that ran. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00248))_
- The number of times the code is run shouldn't matter to you, the framework will determine what is a "good" value for that to let you have some decent results. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00249))_
- To run the benchmarks do go test -bench=. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00250))_
- What 136 ns/op means is our function takes on average 136 nanoseconds to run (on my computer). _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00252))_
- What 136 ns/op means is our function takes on average 136 nanoseconds to run (on my computer). _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00252))_
- Only the body of the loop is timed; it automatically excludes setup and cleanup code from benchmark timing. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00254))_
- Only the body of the loop is timed; it automatically excludes setup and cleanup code from benchmark timing. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00254))_
- Strings in Go are immutable, meaning every concatenation, such as in our Repeat function, involves copying memory to accommodate the new string. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00256))_
- Strings in Go are immutable, meaning every concatenation, such as in our Repeat function, involves copying memory to accommodate the new string. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00256))_
- The standard library provides the strings.Builder stringsBuilder type which minimizes memory copying. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00257))_
- Note : We have to call the String method to retrieve the final result. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00259))_
- We can use BenchmarkRepeat to confirm that strings.Builder significantly improves performance. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00260))_

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00245))_

```
func BenchmarkRepeat(b *testing.B) {
    for b.Loop() {
        Repeat("a")
    }
}
```

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00248))_

> When the benchmark code is executed, it measures how long it takes.

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00249))_

> The number of times the code is run shouldn't matter to you, the framework will determine what is a "good" value for that to let you have some decent results.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00251))_

```
goos: darwin
goarch: amd64
pkg: github.com/quii/learn-go-with-tests/for/v4
10000000           136 ns/op
PASS
```

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00254))_

> Only the body of the loop is timed; it automatically excludes setup and cleanup code from benchmark timing. A typical benchmark is structured like:

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

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00257, source-range-cb73a893-00259))_

> The standard library provides the strings.Builder stringsBuilder type which minimizes memory copying. It implements a WriteString method which we can use to concatenate strings: Note : We have to call the String method to retrieve the final result.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00258))_

```
const repeatCount = 5
func Repeat(character string) string {
    var repeated strings.Builder
    for i := 0; i < repeatCount; i++ {
        repeated.WriteString(character)
    }
    return repeated.String()
}
```

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00260))_

> We can use BenchmarkRepeat to confirm that strings.Builder significantly improves performance. Run go test -bench=. -benchmem

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00261))_

```
goarch: amd64
pkg: github.com/quii/learn-go-with-tests/for/v4
10000000           25.70 ns/op           8 B/op 
allocs/op
PASS
```

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00260))_

> We can use BenchmarkRepeat to confirm that strings.Builder significantly improves performance. Run go test -bench=. -benchmem

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00262))_

```
p
g
signiﬁcantly improves performance. Run go test -bench=. -benchmem:
goos: darwin
goarch: amd64
pkg: github.com/quii/learn-go-with-tests/for/v4
10000000           25.70 ns/op           8 B/op           1
```

### Practice exercises

- - Change the test so a caller can specify how many times the character is repeated and then fix the code _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00267))_
- - Change the test so a caller can specify how many times the character is repeated and then fix the code _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00267))_
- - Have a look through the strings package. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00269))_
- Investing time learning the standard library will really pay off over time. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00269))_

### Wrapping up

## Arrays and slices

- Arrays allow you to store multiple elements of the same type in a variable in a particular order. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00276))_
- Sum will take an array of numbers and return the total. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00277))_

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00277))_

> When you have arrays, it is very common to have to iterate over them.

### Write the test first

- Arrays have a fi xed capacity which you define when you declare the variable. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00282))_
- It is sometimes useful to also print the inputs to the function in the error message. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00285))_
- Here, we are using the %v placeholder to print the "default" format, which works well for arrays. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00285))_

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00280))_

> Create a new folder to work in. Create a new file called sum_test.go and insert the following:

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00281))_

```
package main
import "testing"
func TestSum(t *testing.T) {
numbers := [5]int{1, 2, 3, 4, 5}
got := Sum(numbers)
    want := 15
if got != want {
        t.Errorf("got %d want %d given, %v", got, want, numbers)
    }
}
```

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00282))_

> Arrays have a fi xed capacity which you define when you declare the variable. We can initialize an array in two ways:

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00283))_

```
[N]type{value1, value2, ..., valueN} e.g. numbers := [5]int{1, 2, 
3, 4, 5}
[...]type{value1, value2, ..., valueN} e.g. numbers := [...]int{1, 2,
```

### Try to run the test

- If you had initialized go mod with go mod init main you will be presented with an error _testmain.go:13:2: cannot import "main" . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00288))_
- This is because according to common practice, package main will only contain integration of other packages and not unit-testable code and hence Go will not allow you to import a package with name main . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00288))_
- This is because according to common practice, package main will only contain integration of other packages and not unit-testable code and hence Go will not allow you to import a package with name main . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00288))_
- To fix this, you can rename the main module in go.mod to any other name. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00289))_
- Once the above error is fixed, if you run go test the compiler will fail with the familiar ./sum_test.go:10:15: undefined: Sum error. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00290))_
- Now we can proceed with writing the actual method to be tested. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00290))_

### Write the minimal amount of code for the test to run and check the failing test output

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00292))_

```
package main
func Sum(numbers [5]int) int {
    return 0
}
```

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00294))_

```
sum_test.go:13: got 0 want 15 given, [1 2 3 4 5]
```

### Write enough code to make it pass

- In this case, we are using for to iterate 5 times to work through the array and add each item onto sum . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00297))_
- To get the value out of an array at a particular index, just use array[index] syntax. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00297))_

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00296))_

```
func Sum(numbers [5]int) int {
    sum := 0
    for i := 0; i < 5; i++ {
        sum += numbers[i]
    }
    return sum
}
```

### Refactor

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00300))_

```
func Sum(numbers [5]int) int {
    sum := 0
    for _, number := range numbers {
        sum += number
    }
    return sum
}
```

## Arrays and their type

- An interesting property of arrays is that the size is encoded in its type. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00303))_
- They are different types so it's just the same as trying to pass a string into a function that wants an int . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00303))_
- You may be thinking it's quite cumbersome that arrays have a fixed length, and most of the time you probably won't be using them! _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00304))_
- Go has slices which do not encode the size of the collection and instead can have any size. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00305))_
- The next requirement will be to sum collections of varying sizes. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00306))_

### Write the test first

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00308))_

> We will now use the slice type which allows us to have collections of any size. The syntax is very similar to arrays, you just omit the size when declaring them

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00309))_

> mySlice := []int{1,2,3}

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00308))_

> We will now use the slice type which allows us to have collections of any size. The syntax is very similar to arrays, you just omit the size when declaring them

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00311))_

> myArray := [3]int{1,2,3}

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00312))_

```
func TestSum(t *testing.T) {
t.Run("collection of 5 numbers", func(t *testing.T) {
        numbers := [5]int{1, 2, 3, 4, 5}
got := Sum(numbers)
        want := 15
if got != want {
            t.Errorf("got %d want %d given, %v", got, want, numbers)
        }
    })
t.Run("collection of any size", func(t *testing.T) {
        numbers := []int{1, 2, 3}
got := Sum(numbers)
        want := 6
if got != want {
            t.Errorf("got %d want %d given, %v", got, want, numbers)
        }
    })
}
```

### Try and run the test

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00314))_

```
This does not compile
./sum_test.go:22:13: cannot use numbers (type []int) as type [5]int 
in argument to Sum
```

### Write the minimal amount of code for the test to run and check the failing test output

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00319))_

> In our case, no one else is using our function, so rather than having two functions to maintain, let's have just one.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00320))_

```
func Sum(numbers []int) int {
    sum := 0
    for _, number := range numbers {
        sum += number
    }
    return sum
}
```

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00319))_

> In our case, no one else is using our function, so rather than having two functions to maintain, let's have just one.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00321))_

> If you try to run the tests they will still not compile, you will have to change the first test to pass in a slice rather than an array.

### Write enough code to make it pass

- It turns out that fixing the compiler problems were all we need to do here and the tests pass! _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00323))_

### Refactor

- Remember that we must not neglect our test code in the refactoring stage - we can further improve our Sum tests. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00325))_
- We already refactored Sum - all we did was replace arrays with slices, so no extra changes are required. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00325))_
- It is important to question the value of your tests. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00327))_
- Having too many tests can turn in to a real problem and it just adds more overhead in maintenance. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00327))_
- It should not be a goal to have as many tests as possible, but rather to have as much confidence as possible in your code base. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00327))_
- Every test has a cost . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00327))_
- In our case, you can see that having two tests for this function is redundant. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00328))_
- If it works for a slice of one size it's very likely it'll work for a slice of any size (within reason). _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00328))_
- If you have been strict with TDD, it's quite likely you'll have close to 100% coverage anyway. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00329))_
- Whilst striving for 100% coverage should not be your end goal, the coverage tool can help identify areas of your code not covered by tests. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00329))_
- Now that we are happy we have a well-tested function you should commit your great work before taking on the next challenge. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00333))_
- Now that we are happy we have a well-tested function you should commit your great work before taking on the next challenge. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00333))_
- We need a new function called SumAll which will take a varying number of slices, returning a new slice containing the totals for each slice passed in. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00334))_

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00325))_

> We already refactored Sum - all we did was replace arrays with slices, so no extra changes are required. Remember that we must not neglect our test code in the refactoring stage - we can further improve our Sum tests.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00326))_

```
func TestSum(t *testing.T) {
t.Run("collection of 5 numbers", func(t *testing.T) {
        numbers := []int{1, 2, 3, 4, 5}
got := Sum(numbers)
        want := 15
if got != want {
            t.Errorf("got %d want %d given, %v", got, want, numbers)
        }
    })
t.Run("collection of any size", func(t *testing.T) {
        numbers := []int{1, 2, 3}
got := Sum(numbers)
        want := 6
if got != want {
            t.Errorf("got %d want %d given, %v", got, want, numbers)
        }
    })
}
```

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00330))_

```
Try running
go test -cover
You should see
```

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00331))_

```
PASS
coverage: 100.0% of statements
```

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00336))_

```
SumAll([]int{1,2}, []int{0,9}) would return []int{3, 9}
or
SumAll([]int{1,1,1}) would return []int{3}
```

### Write the test first

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00338))_

```
func TestSumAll(t *testing.T) {
got := SumAll([]int{1, 2}, []int{0, 9})
    want := []int{3, 9}
if got != want {
        t.Errorf("got %v want %v", got, want)
    }
}
```

### Try and run the test

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00340))_

```
./sum_test.go:23:9: undefined: SumAll
```

### Write the minimal amount of code for the test to run and check the failing test output

- We need to define SumAll according to what our test wants. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00342))_
- Go can let you write variadic functions that can take a variable number of arguments. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00343))_
- This is valid, but our tests still won't compile! _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00345))_
- Go does not let you use equality operators with slices. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00347))_
- So, it can't be applied to slices with non-comparable elements like 2D slices. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00348))_
- From Go 1.21, slices standard package is available, which has slices.Equal function to do a simple shallow compare on slices, where you don't need to worry about the types like the above case. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00348))_
- Note that this function expects the elements to be comparable. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00348))_
- You should have test output like the following: sum_test.go:30: got [] want [3 9] _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00351))_

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00342))_

> We need to define SumAll according to what our test wants.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00344))_

```
func SumAll(numbersToSum ...[]int) []int {
    return nil
}
```

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00348))_

> From Go 1.21, slices standard package is available, which has slices.Equal function to do a simple shallow compare on slices, where you don't need to worry about the types like the above case. Note that this function expects the elements to be comparable. So, it can't be applied to slices with non-comparable elements like 2D slices.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00346))_

```
./sum_test.go:26:9: invalid operation: got != want (slice can only 
be compared to nil)
```

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00347, source-range-cb73a893-00351))_

> Go does not let you use equality operators with slices. You could write a function to iterate over each got and want slice and check their values, but what if we had a more convenient way to do this? You should have test output like the following: sum_test.go:30: got [] want [3 9]

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00350))_

```
func TestSumAll(t *testing.T) {
got := SumAll([]int{1, 2}, []int{0, 9})
    want := []int{3, 9}
if !slices.Equal(got, want) {
        t.Errorf("got %v want %v", got, want)
    }
}
```

### Write enough code to make it pass

- You can index slices like arrays with mySlice[N] to get the value out or assign it a new value with = _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00357))_
- The tests should now pass. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00358))_

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00353))_

> What we need to do is iterate over the varargs, calculate the sum using our existing Sum function, then add it to the slice we will return

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00354))_

```
func SumAll(numbersToSum ...[]int) []int {
    lengthOfNumbers := len(numbersToSum)
    sums := make([]int, lengthOfNumbers)
for i, numbers := range numbersToSum {
        sums[i] = Sum(numbers)
    }
return sums
}
```

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00353))_

> What we need to do is iterate over the varargs, calculate the sum using our existing Sum function, then add it to the slice we will return

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00356))_

> There's a new way to create a slice. make allows you to create a slice with a starting capacity of the len of the numbersToSum we need to work through. The length of a slice is the number of elements it holds len(mySlice) , while the capacity is the number of elements it can hold in the underlying array cap(mySlice) , e.g., make([]int, 0, 5) creates a slice with length 0 and capacity 5.

### Refactor

- If you have a slice with a capacity of 2 and try to do mySlice[10] = 1 you will get a runtime error. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00360))_
- As mentioned, slices have a capacity. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00360))_
- However, you can use the append function which takes a slice and a new value, then returns a new slice with all the items in it. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00361))_
- However, you can use the append function which takes a slice and a new value, then returns a new slice with all the items in it. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00361))_
- In this implementation, we are worrying less about capacity. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00364))_
- Our next requirement is to change SumAll to SumAllTails , where it will calculate the totals of the "tails" of each slice. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00365))_
- The tail of a collection is all items in the collection except the first one (the "head"). _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00365))_
- The tail of a collection is all items in the collection except the first one (the "head"). _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00365))_

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00361, source-range-cb73a893-00364))_

> However, you can use the append function which takes a slice and a new value, then returns a new slice with all the items in it. In this implementation, we are worrying less about capacity. We start with an empty slice sums and append to it the result of Sum as we work through the varargs.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00362))_

```
func SumAll(numbersToSum ...[]int) []int {
    var sums []int
    for _, numbers := range numbersToSum {
        sums = append(sums, Sum(numbers))
    }
```

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00361, source-range-cb73a893-00364))_

> However, you can use the append function which takes a slice and a new value, then returns a new slice with all the items in it. In this implementation, we are worrying less about capacity. We start with an empty slice sums and append to it the result of Sum as we work through the varargs.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00363))_

```
return sums
}
```

### Write the test first

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00367))_

```
func TestSumAllTails(t *testing.T) {
    got := SumAllTails([]int{1, 2}, []int{0, 9})
    want := []int{2, 9}
if !reflect.DeepEqual(got, want) {
        t.Errorf("got %v want %v", got, want)
    }
}
```

### Try and run the test

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00369))_

```
./sum_test.go:26:9: undefined: SumAllTails
```

### Write the minimal amount of code for the test to run and check the failing test output

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00371))_

```
Rename the function to SumAllTails and re-run the test
sum_test.go:30: got [3 9] want [2 9]
```

### Write enough code to make it pass

- You may wish to spend some time writing other tests around slices and experiment with the slice operator to get more familiar with it. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00374))_
- The syntax is slice[low:high] . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00374))_
- In our case, we are saying "take from 1 to the end" with numbers[1:] . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00374))_

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00373))_

```
func SumAllTails(numbersToSum ...[]int) []int {
    var sums []int
    for _, numbers := range numbersToSum {
        tail := numbers[1:]
        sums = append(sums, Sum(tail))
    }
return sums
}
```

### Refactor

### Write the test first

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00379))_

```
func TestSumAllTails(t *testing.T) {
t.Run("make the sums of some slices", func(t *testing.T) {
        got := SumAllTails([]int{1, 2}, []int{0, 9})
        want := []int{2, 9}
if !reflect.DeepEqual(got, want) {
            t.Errorf("got %v want %v", got, want)
        }
    })
t.Run("safely sum empty slices", func(t *testing.T) {
        got := SumAllTails([]int{}, []int{3, 4, 5})
        want := []int{0, 9}
if !reflect.DeepEqual(got, want) {
            t.Errorf("got %v want %v", got, want)
        }
    })
}
```

### Try and run the test

- It's important to note that while the test has compiled , it has a runtime error . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00382))_
- Compile time errors are our friend because they help us write software that works, runtime errors are our enemies because they affect our users. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00383))_
- Compile time errors are our friend because they help us write software that works, runtime errors are our enemies because they affect our users. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00383))_

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00383))_

> Compile time errors are our friend because they help us write software that works, runtime errors are our enemies because they affect our users.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00381))_

```
panic: runtime error: slice bounds out of range [recovered]
panic: runtime error: slice bounds out of range
```

### Write enough code to make it pass

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00385))_

```
func SumAllTails(numbersToSum ...[]int) []int {
    var sums []int
    for _, numbers := range numbersToSum {
        if len(numbers) == 0 {
            sums = append(sums, 0)
        } else {
            tail := numbers[1:]
            sums = append(sums, Sum(tail))
        }
    }
return sums
}
```

### Refactor

- It might look strange but, it's no different to assigning a variable to a string , or an int , functions in effect are values too. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00389))_
- We could've created a new function checkSums like we normally do, but in this case, we're showing a new technique, assigning a function to a variable. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00389))_
- It also allows you to reduce the surface area of your API. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00390))_
- Hiding variables and functions that don't need to be exported is an important design consideration. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00391))_
- A handy side-effect of this is this adds a little type-safety to our code. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00392))_
- If a developer mistakenly adds a new test with checkSums(t, got, "dave") the compiler will stop them in their tracks. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00392))_

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00388))_

```
func TestSumAllTails(t *testing.T) {
checkSums := func(t testing.TB, got, want []int) {
        t.Helper()
        if !reflect.DeepEqual(got, want) {
            t.Errorf("got %v want %v", got, want)
        }
    }
t.Run("make the sums of tails of", func(t *testing.T) {
        got := SumAllTails([]int{1, 2}, []int{0, 9})
        want := []int{2, 9}
        checkSums(t, got, want)
    })
t.Run("safely sum empty slices", func(t *testing.T) {
        got := SumAllTails([]int{}, []int{3, 4, 5})
        want := []int{0, 9}
        checkSums(t, got, want)
    })
}
```

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00391))_

> By defining this function inside the test, it cannot be used by other functions in this package. Hiding variables and functions that don't need to be exported is an important design consideration.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00393))_

```
$ go test
./sum_test.go:52:21: cannot use "dave" (type string) as type []int 
in argument to checkSums
```

### Wrapping up

- - How they have a fi xed capacity but you can create new slices from old ones using append _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00399))_
- We've used slices and arrays with integers but they work with any other type too, including arrays/slices themselves. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00404))_
- I have made a go playground with a slice in it for you to experiment with. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00406))_
- Another handy way to experiment with Go other than writing tests is the Go playground. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00406))_
- Another example of why it's a good idea to make a copy of a slice after slicing a very large slice. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00407))_
- Here is an example of slicing an array and how changing the slice affects the original array; but a "copy" of the slice will not affect the original array. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00407))_
- Another example of why it's a good idea to make a copy of a slice after slicing a very large slice. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00407))_

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00404))_

> So you can declare a variable of [][]string if you need to.

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00405))_

> Check out the Go blog post on slices for an in-depth look into slices. Try writing more tests to solidify what you learn from reading it.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00406))_

> You can try most things out and you can easily share your code if you need to ask questions.

## Structs, methods & interfaces

- Suppose that we need some geometry code to calculate the perimeter of a rectangle given a height and width. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00410))_
- We can write a Perimeter(width float64, height float64) function, where float64 is for floating-point numbers like 123.45 . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00410))_

### Write the test first

- The f is for our float64 and the .2 means print 2 decimal places. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00414))_
- The f is for our float64 and the .2 means print 2 decimal places. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00414))_

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00413))_

```
func TestPerimeter(t *testing.T) {
    got := Perimeter(10.0, 10.0)
    want := 40.0
if got != want {
        t.Errorf("got %.2f want %.2f", got, want)
    }
}
```

### Try to run the test

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00416))_

```
./shapes_test.go:6:9: undefined: Perimeter
```

### Write the minimal amount of code for the test to run and check the failing test output

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00418))_

```
func Perimeter(width float64, height float64) float64 {
    return 0
}
Results in shapes_test.go:10: got 0.00 want 40.00.
```

### Write enough code to make it pass

- Try to do it yourself, following the TDD cycle. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00422))_

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00420))_

```
func Perimeter(width float64, height float64) float64 {
    return 2 * (width + height)
}
```

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00422))_

> Try to do it yourself, following the TDD cycle.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00424))_

```
func TestPerimeter(t *testing.T) {
    got := Perimeter(10.0, 10.0)
    want := 40.0
if got != want {
        t.Errorf("got %.2f want %.2f", got, want)
    }
}
func TestArea(t *testing.T) {
    got := Area(12.0, 6.0)
    want := 72.0
if got != want {
        t.Errorf("got %.2f want %.2f", got, want)
    }
}
And code like this
func Perimeter(width float64, height float64) float64 {
    return 2 * (width + height)
}
func Area(width float64, height float64) float64 {
    return width * height
}
```

### Refactor

- An unwary developer might try to supply the width and height of a triangle to these functions without realising they will return the wrong answer. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00426))_
- Our code does the job, but it doesn't contain anything explicit about rectangles. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00426))_
- We could just give the functions more specific names like RectangleArea . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00427))_
- A neater solution is to define our own type called Rectangle which encapsulates this concept for us. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00427))_
- We can create a simple type using a struct . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00428))_
- A struct is just a named collection of fields where you can store data. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00428))_
- Our next requirement is to write an Area function for circles. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00435))_

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00429))_

> Declare a struct in your shapes.go file like this

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00430))_

```
type Rectangle struct {
    Width  float64
    Height float64
}
```

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00431))_

> Now let's refactor the tests to use Rectangle instead of plain float64 s.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00432))_

```
func TestPerimeter(t *testing.T) {
    rectangle := Rectangle{10.0, 10.0}
    got := Perimeter(rectangle)
    want := 40.0
if got != want {
        t.Errorf("got %.2f want %.2f", got, want)
    }
}
func TestArea(t *testing.T) {
    rectangle := Rectangle{12.0, 6.0}
    got := Area(rectangle)
    want := 72.0
if got != want {
        t.Errorf("got %.2f want %.2f", got, want)
    }
}
Remember to run your tests before attempting to ﬁx. The tests should
show a helpful error like
./shapes_test.go:7:18: not enough arguments in call to Perimeter
have (Rectangle)
   want (float64, float64)
You can access the ﬁelds of a struct with the syntax of myStruct.field.
Change the two functions to ﬁx the test.
func Perimeter(rectangle Rectangle) float64 {
    return 2 * (rectangle.Width + rectangle.Height)
```

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00431))_

> Now let's refactor the tests to use Rectangle instead of plain float64 s.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00433))_

```
func Perimeter(rectangle Rectangle) float64 {
    return 2 * (rectangle.Width + rectangle.He
}
func Area(rectangle Rectangle) float64 {
    return rectangle.Width * rectangle.Height
}
```

### Write the test first

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00437))_

```
func TestArea(t *testing.T) {
t.Run("rectangles", func(t *testing.T) {
        rectangle := Rectangle{12, 6}
        got := Area(rectangle)
        want := 72.0
if got != want {
            t.Errorf("got %g want %g", got, want)
        }
    })
t.Run("circles", func(t *testing.T) {
        circle := Circle{10}
        got := Area(circle)
        want := 314.1592653589793
```

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00438))_

```
if got != want {
            t.Errorf("got %g want %g", got, want)
        }
    })
}
```

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00439))_

> As you can see, the f has been replaced by g , with good reason. Use of g will print a more precise decimal number in the error message (fmt options). For example, using a radius of 1.5 in a circle area calculation, f would show 7.068583 whereas g would show 7.0685834705770345 .

### Try to run the test

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00441))_

```
./shapes_test.go:28:13: undefined: Circle
```

### Write the minimal amount of code for the test to run and check the failing test output

- - You can have functions with the same name declared in different packages . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00445))_
- So we could create our Area(Circle) in a new package, but that feels overkill here. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00445))_
- - We can define methods on our newly defined types instead. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00446))_

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00443))_

```
We need to deﬁne our Circle type.
type Circle struct {
    Radius float64
}
Now try to run the tests again
./shapes_test.go:29:14: cannot use circle (type Circle) as type 
Rectangle in argument to Area
Some programming languages allow you to do something like this:
func Area(circle Circle) float64       {}
func Area(rectangle Rectangle) float64 {}
But you cannot in Go
./shapes.go:20:32: Area redeclared in this block
```

## What are methods?

- So far we have only been writing functions but we have been using some methods. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00448))_
- When we call t.Errorf we are calling the method Errorf on the instance of our t ( testing.T ). _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00448))_
- So far we have only been writing functions but we have been using some methods. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00448))_
- Where you can just call functions wherever you like, such as Area(rectangle) you can only call methods on "things". _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00450))_
- Where you can just call functions wherever you like, such as Area(rectangle) you can only call methods on "things". _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00450))_
- It is so important to take the time to slowly read the error messages you get, it will help you in the long run. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00453))_
- I would like to reiterate how great the compiler is here. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00453))_

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00450))_

> Methods are very similar to functions but they are called by invoking them on an instance of a particular type. Where you can just call functions wherever you like, such as Area(rectangle) you can only call methods on "things".

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00452))_

```
func TestArea(t *testing.T) {
t.Run("rectangles", func(t *testing.T) {
        rectangle := Rectangle{12, 6}
        got := rectangle.Area()
        want := 72.0
if got != want {
            t.Errorf("got %g want %g", got, want)
        }
    })
t.Run("circles", func(t *testing.T) {
        circle := Circle{10}
        got := circle.Area()
        want := 314.1592653589793
if got != want {
            t.Errorf("got %g want %g", got, want)
        }
    })
}
If we try to run the tests, we get
./shapes_test.go:19:19: rectangle.Area undefined (type Rectangle has 
no field or method Area)
./shapes_test.go:29:16: circle.Area undefined (type Circle has no 
field or method Area)
type Circle has no ﬁeld or method Area
```

### Write the minimal amount of code for the test to run and check the failing test output

- The only difference is the syntax of the method receiver func (receiverName ReceiverType) MethodName(args) . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00458))_
- The syntax for declaring methods is almost the same as functions and that's because they're so similar. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00458))_
- The syntax for declaring methods is almost the same as functions and that's because they're so similar. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00458))_
- The only difference is the syntax of the method receiver func (receiverName ReceiverType) MethodName(args) . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00458))_
- In many other programming languages this is done implicitly and you access the receiver via this . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00459))_
- It is a convention in Go to have the receiver variable be the first letter of the type. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00460))_

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00458))_

> The syntax for declaring methods is almost the same as functions and that's because they're so similar. The only difference is the syntax of the method receiver func (receiverName ReceiverType) MethodName(args) .

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00456))_

```
type Rectangle struct {
    Width  float64
    Height float64
}
func (r Rectangle) Area() float64 {
    return 0
}
type Circle struct {
    Radius float64
```

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00458))_

> The syntax for declaring methods is almost the same as functions and that's because they're so similar. The only difference is the syntax of the method receiver func (receiverName ReceiverType) MethodName(args) .

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00457))_

```
}
func (c Circle) Area() float64 {
    return 0
}
```

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00459))_

> When your method is called on a variable of that type, you get your reference to its data via the receiverName variable.

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00462))_

> If you try to re-run the tests they should now compile and give you some failing output.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00461))_

```
r Rectangle
```

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00462))_

> If you try to re-run the tests they should now compile and give you some failing output.

### Write enough code to make it pass

- If you re-run the tests the rectangle tests should be passing but circle should still be failing. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00466))_

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00465))_

```
func (r Rectangle) Area() float64 {
    return r.Width * r.Height
}
```

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00468))_

```
func (c Circle) Area() float64 {
    return math.Pi * c.Radius * c.Radius
}
```

### Refactor

- There is some duplication in our tests. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00470))_
- All we want to do is take a collection of shapes , call the Area() method on them and then check the result. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00471))_
- All we want to do is take a collection of shapes , call the Area() method on them and then check the result. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00471))_
- We want to be able to write some kind of checkArea function that we can pass both Rectangle s and Circle s to, but fail to compile if we try to pass in something that isn't a shape. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00472))_
- With Go, we can codify this intent with interfaces . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00473))_
- Interfaces are a very powerful concept in statically typed languages like Go because they allow you to make functions that can be used with different types and create highly-decoupled code whilst still maintaining type-safety. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00474))_
- Interfaces are a very powerful concept in statically typed languages like Go because they allow you to make functions that can be used with different types and create highly-decoupled code whilst still maintaining type-safety. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00474))_
- We are creating a helper function like we have in other exercises but this time we are asking for a Shape to be passed in. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00478))_
- If we try to call this with something that isn't a shape, then it will not compile. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00478))_
- If we try to call this with something that isn't a shape, then it will not compile. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00478))_
- We're creating a new type just like we did with Rectangle and Circle but this time it is an interface rather than a struct . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00481))_
- Once you add this to the code, the tests will pass. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00482))_

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00473))_

> With Go, we can codify this intent with interfaces .

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00476))_

```
func TestArea(t *testing.T) {
```

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00477))_

```
checkArea := func(t testing.TB, shape Shape, want float64) {
        t.Helper()
        got := shape.Area()
        if got != want {
            t.Errorf("got %g want %g", got, want)
        }
    }
t.Run("rectangles", func(t *testing.T) {
        rectangle := Rectangle{12, 6}
        checkArea(t, rectangle, 72.0)
    })
t.Run("circles", func(t *testing.T) {
        circle := Circle{10}
        checkArea(t, circle, 314.1592653589793)
    })
}
```

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00479))_

> How does something become a shape? We just tell Go what a Shape is using an interface declaration

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00480))_

```
type Shape interface {
    Area() float64
}
```

## Wait, what?

- This is quite different to interfaces in most other programming languages. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00484))_
- Normally you have to write code to say My type Foo implements interface Bar . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00484))_
- - Rectangle has a method called Area that returns a float64 so it satisfies the Shape interface _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00486))_
- - Circle has a method called Area that returns a float64 so it satisfies the Shape interface _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00487))_
- In Go interface resolution is implicit . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00490))_
- If the type you pass in matches what the interface is asking for, it will compile. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00490))_

## Decoupling

- By declaring an interface, the helper is decoupled from the concrete types and only has the method it needs to do its job. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00492))_
- Notice how our helper does not need to concern itself with whether the shape is a Rectangle or a Circle or a Triangle . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00492))_
- By declaring an interface, the helper is decoupled from the concrete types and only has the method it needs to do its job. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00492))_
- This kind of approach of using interfaces to declare only what you need is very important in software design and will be covered in more detail in later sections. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00493))_
- This kind of approach of using interfaces to declare only what you need is very important in software design and will be covered in more detail in later sections. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00493))_

### Further refactoring

- Now that you have some understanding of structs we can introduce "table driven tests". _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00495))_
- The only new syntax here is creating an "anonymous struct", areaTests . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00498))_
- The only new syntax here is creating an "anonymous struct", areaTests . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00498))_
- Then we fill the slice with cases. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00498))_
- We then iterate over them just like we do any other slice, using the struct fields to run our tests. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00499))_
- We then iterate over them just like we do any other slice, using the struct fields to run our tests. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00499))_
- You can see how it would be very easy for a developer to introduce a new shape, implement Area and then add it to the test cases. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00500))_
- In addition, if a bug is found with Area it is very easy to add a new test case to exercise it before fixing it. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00500))_
- In addition, if a bug is found with Area it is very easy to add a new test case to exercise it before fixing it. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00500))_
- You can see how it would be very easy for a developer to introduce a new shape, implement Area and then add it to the test cases. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00500))_
- Table driven tests can be a great item in your toolbox, but be sure that you have a need for the extra noise in the tests. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00501))_
- They are a great fit when you wish to test various implementations of an interface, or if the data being passed in to a function has lots of different requirements that need testing. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00501))_

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00495))_

> Now that you have some understanding of structs we can introduce "table driven tests".

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00496))_

> Table driven tests are useful when you want to build a list of test cases that can be tested in the same manner.

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00496))_

> Table driven tests are useful when you want to build a list of test cases that can be tested in the same manner.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00497))_

```
func TestArea(t *testing.T) {
areaTests := []struct {
        shape Shape
        want  float64
    }{
        {Rectangle{12, 6}, 72.0},
        {Circle{10}, 314.1592653589793},
    }
for _, tt := range areaTests {
        got := tt.shape.Area()
        if got != tt.want {
            t.Errorf("got %g want %g", got, tt.want)
        }
    }
}
```

### Write the test first

- Adding a new test for our new shape is very easy. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00504))_

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00504))_

> Adding a new test for our new shape is very easy. Just add {Triangle{12, 6}, 36.0}, to our list.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00505))_

```
func TestArea(t *testing.T) {
areaTests := []struct {
        shape Shape
        want  float64
```

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00504))_

> Adding a new test for our new shape is very easy. Just add {Triangle{12, 6}, 36.0}, to our list.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00506))_

```
}{
        {Rectangle{12, 6}, 72.0},
        {Circle{10}, 314.1592653589793},
        {Triangle{12, 6}, 36.0},
    }
for _, tt := range areaTests {
        got := tt.shape.Area()
        if got != tt.want {
            t.Errorf("got %g want %g", got, tt.want)
        }
    }
}
```

### Try to run the test

### Write the minimal amount of code for the test to run and check the failing test output

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00510))_

```
./shapes_test.go:25:4: undefined: Triangle
We have not deﬁned Triangle yet
type Triangle struct {
    Base   float64
    Height float64
}
Try again
./shapes_test.go:25:8: cannot use Triangle literal (type Triangle) 
as type Shape in field value:
Triangle does not implement Shape (missing Area method)
It's telling us we cannot use a Triangle as a shape because it does not
have an Area() method, so add an empty implementation to get the
test working
func (t Triangle) Area() float64 {
    return 0
}
Finally the code compiles and we get our error
shapes_test.go:31: got 0.00 want 36.00
```

### Write enough code to make it pass

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00512))_

```
func (t Triangle) Area() float64 {
    return (t.Base * t.Height) * 0.5
}
And our tests pass!
```

### Refactor

- Again, the implementation is fine but our tests could do with some improvement. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00514))_
- It's not immediately clear what all the numbers represent and you should be aiming for your tests to be easily understood. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00517))_
- Now our tests - rather, the list of test cases - make assertions of truth about shapes and their areas. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00524))_

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00516))_

```
{Rectangle{12, 6}, 72.0},
{Circle{10}, 314.1592653589793},
{Triangle{12, 6}, 36.0},
```

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00518))_

> So far you've only been shown syntax for creating instances of structs MyStruct{val1, val2} but you can optionally name the fields.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00520))_

```
{shape: Rectangle{Width: 12, Height: 6}, want: 72.0},
       {shape: Circle{Radius: 10}, want: 314.1592653589793},
       {shape: Triangle{Base: 12, Height: 6}, want: 36.0},
```

### Make sure your test output is helpful

- It printed shapes_test.go:31: got 0.00 want 36.00 . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00526))_
- We knew this was in relation to Triangle because we were just working with it. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00527))_
- This is not a great experience for the developer, they will have to manually look through the cases to find out which case actually failed. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00527))_
- We knew this was in relation to Triangle because we were just working with it. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00527))_
- The %#v format string will print out our struct with the values in its field, so the developer can see at a glance the properties that are being tested. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00528))_
- We can change our error message into %#v got %g want %g . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00528))_
- To increase the readability of our test cases further, we can rename the want field into something more descriptive like hasArea . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00529))_
- One final tip with table driven tests is to use t.Run and to name the test cases. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00530))_
- By wrapping each case in a t.Run you will have clearer test output on failures as it will print the name of the case _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00531))_
- And you can run specific tests within your table with go test -run TestArea/Rectangle . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00533))_
- And you can run specific tests within your table with go test -run TestArea/Rectangle . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00533))_

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00530))_

> One final tip with table driven tests is to use t.Run and to name the test cases.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00532))_

```
--- FAIL: TestArea (0.00s)
--- FAIL: TestArea/Rectangle (0.00s)
       shapes_test.go:33: main.Rectangle{Width:12, Height:6} got 
72.00 want 72.10
```

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00533))_

> And you can run specific tests within your table with go test -run TestArea/Rectangle .

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00535))_

```
func TestArea(t *testing.T) {
areaTests := []struct {
        name    string
        shape   Shape
        hasArea float64
    }{
        {name: "Rectangle", shape: Rectangle{Width: 12, Height: 6}, 
hasArea: 72.0},
{name: "Circle", shape: Circle{Radius: 10}, hasArea: 
314.1592653589793},
{name: "Triangle", shape: Triangle{Base: 12, Height: 6}, 
hasArea: 36.0},
}
for _, tt := range areaTests {
        // using tt.name from the case to use it as the `t.Run` test 
name
t.Run(tt.name, func(t *testing.T) {
            got := tt.shape.Area()
            if got != tt.hasArea {
                t.Errorf("%#v got %g want %g", tt.shape, got, 
tt.hasArea)
}
        })
}
}
```

### Wrapping up

- This was more TDD practice, iterating over our solutions to basic mathematic problems and learning new language features motivated by our tests. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00537))_
- - Declaring structs to create your own data types which lets you bundle related data together and make the intent of your code clearer _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00538))_
- - Adding methods so you can add functionality to your data types and so you can implement interfaces _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00540))_
- - Table driven tests to make your assertions clearer and your test suites easier to extend & maintain _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00541))_
- This was an important chapter because we are now starting to define our own types. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00542))_
- In statically typed languages like Go, being able to design your own types is essential for building software that is easy to understand, to piece together and to test. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00542))_
- This was an important chapter because we are now starting to define our own types. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00542))_
- In our case our test helper code did not need to know the exact shape it was asserting on, only how to "ask" for its area. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00543))_
- Interfaces are a great tool for hiding complexity away from other parts of the system. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00543))_
- In our case our test helper code did not need to know the exact shape it was asserting on, only how to "ask" for its area. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00543))_
- As you become more familiar with Go you will start to see the real strength of interfaces and the standard library. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00544))_
- You'll learn about interfaces defined in the standard library that are used everywhere and by implementing them against your own types, you can very quickly re-use a lot of great functionality. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00544))_

## Maps

- You can think of the key as the word and the value as the definition. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00548))_
- First, assuming we already have some words with their definitions in the dictionary, if we search for a word, it should return the definition of it. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00549))_

### Write the test first

- Except, it starts with the map keyword and requires two types. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00552))_
- The second is the value type, which goes right after the [] . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00552))_
- The first is the key type, which is written inside the [] . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00552))_
- The second is the value type, which goes right after the [] . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00552))_
- The first is the key type, which is written inside the [] . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00552))_
- Except, it starts with the map keyword and requires two types. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00552))_
- Comparable types are explained in depth in the language spec. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00553))_
- The key type is special. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00553))_
- The value type, on the other hand, can be any type you want. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00554))_
- It can even be another map. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00554))_
- Everything else in this test should be familiar. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00555))_

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00553))_

> The key type is special. It can only be a comparable type because without the ability to tell if 2 keys are equal, we have no way to ensure that we are getting the correct value. Comparable types are explained in depth in the language spec.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00551))_

```
In dictionary_test.go
package main
import "testing"
func TestSearch(t *testing.T) {
    dictionary := map[string]string{"test": "this is just a test"}
got := Search(dictionary, "test")
    want := "this is just a test"
if got != want {
        t.Errorf("got %q want %q given, %q", got, want, "test")
    }
}
```

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00553))_

> It can only be a comparable type because without the ability to tell if 2 keys are equal, we have no way to ensure that we are getting the correct value.

### Try to run the test

- By running go test the compiler will fail with ./dictionary_test.go:8:9: undefined: Search . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00557))_

### Write the minimal amount of code for the test to run and check the output

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00559))_

```
In dictionary.go
package main
func Search(dictionary map[string]string, word string) string {
    return ""
}
Your test should now fail with a clear error message
dictionary_test.go:12: got '' want 'this is just a test' given, 
'test'.
```

### Write enough code to make it pass

- Getting a value out of a Map is the same as getting a value out of Array map[key] . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00562))_

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00561))_

```
func Search(dictionary map[string]string, word string) string {
    return dictionary[word]
}
```

### Refactor

- I decided to create an assertStrings helper to make the implementation more general. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00565))_

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00564))_

```
func TestSearch(t *testing.T) {
    dictionary := map[string]string{"test": "this is just a test"}
got := Search(dictionary, "test")
    want := "this is just a test"
assertStrings(t, got, want)
}
func assertStrings(t testing.TB, got, want string) {
    t.Helper()
if got != want {
        t.Errorf("got %q want %q", got, want)
    }
}
```

## Using a custom type

- Then called Search on the Dictionary instance. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00570))_
- We started using the Dictionary type, which we have not defined yet. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00570))_
- Then called Search on the Dictionary instance. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00570))_
- We did not need to change assertStrings . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00571))_
- Here we created a Dictionary type which acts as a thin wrapper around map . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00574))_
- With the custom type defined, we can create the Search method. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00574))_

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00567))_

> We can improve our dictionary's usage by creating a new type around map and making Search a method.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00568))_

```
In dictionary_test.go:
func TestSearch(t *testing.T) {
    dictionary := Dictionary{"test": "this is just a test"}
got := dictionary.Search("test")
    want := "this is just a test"
```

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00567))_

> We can improve our dictionary's usage by creating a new type around map and making Search a method.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00569))_

```
assertStrings(t, got, want)
}
```

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00572))_

> In dictionary.go :

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00573))_

```
type Dictionary map[string]string
func (d Dictionary) Search(word string) string {
    return d[word]
}
```

### Write the test first

- This is good because the program can continue to run, but there is a better approach. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00577))_
- However, it's a scenario that could be key in other usecases). _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00577))_
- The function can report that the word is not in the dictionary. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00577))_
- This way, the user isn't left wondering if the word doesn't exist or if there is just no definition (this might not seem very useful for a dictionary. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00577))_
- This is good because the program can continue to run, but there is a better approach. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00577))_
- The way to handle this scenario in Go is to return a second argument which is an Error type. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00579))_
- Notice that as we've seen in the pointers and error section here in order to assert the error message we first check that the error is not nil and then use .Error() method to get the string which we can then pass to the assertion. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00580))_
- Notice that as we've seen in the pointers and error section here in order to assert the error message we first check that the error is not nil and then use .Error() method to get the string which we can then pass to the assertion. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00580))_

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00577))_

> We actually get nothing back. This is good because the program can continue to run, but there is a better approach. The function can report that the word is not in the dictionary. This way, the user isn't left wondering if the word doesn't exist or if there is just no definition (this might not seem very useful for a dictionary. However, it's a scenario that could be key in other usecases).

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00578))_

```
func TestSearch(t *testing.T) {
    dictionary := Dictionary{"test": "this is just a test"}
t.Run("known word", func(t *testing.T) {
        got, _ := dictionary.Search("test")
        want := "this is just a test"
assertStrings(t, got, want)
    })
t.Run("unknown word", func(t *testing.T) {
        _, err := dictionary.Search("unknown")
        want := "could not find the word you were looking for"
if err == nil {
            t.Fatal("expected to get an error.")
        }
assertStrings(t, err.Error(), want)
    })
}
```

### Try and run the test

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00582))_

```
This does not compile
./dictionary_test.go:18:10: assignment mismatch: 2 variables but 1 
values
```

### Write the minimal amount of code for the test to run and check the output

- Your test should now fail with a much clearer error message. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00585))_
- dictionary_test.go:22: expected to get an error. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00586))_

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00584))_

```
func (d Dictionary) Search(word string) (string, error) {
    return d[word], nil
}
```

### Write enough code to make it pass

- The second value is a boolean which indicates if the key was found successfully. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00589))_
- In order to make this pass, we are using an interesting property of the map lookup. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00589))_
- This property allows us to differentiate between a word that doesn't exist and a word that just doesn't have a definition. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00590))_

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00588))_

```
func (d Dictionary) Search(word string) (string, error) {
    definition, ok := d[word]
    if !ok {
        return "", errors.New("could not find the word you were 
looking for")
}
return definition, nil
}
```

### Refactor

- By creating a new helper we were able to simplify our test, and start using our ErrNotFound variable so our test doesn't fail if we change the error text in the future. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00594))_

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00592))_

```
var ErrNotFound = errors.New("could not find the word you were 
looking for")
func (d Dictionary) Search(word string) (string, error) {
    definition, ok := d[word]
    if !ok {
        return "", ErrNotFound
    }
return definition, nil
}
We can get rid of the magic error in our Search function by extracting
it into a variable. This will also allow us to have a better test.
t.Run("unknown word", func(t *testing.T) {
    _, got := dictionary.Search("unknown")
    if got == nil {
        t.Fatal("expected to get an error.")
    }
    assertError(t, got, ErrNotFound)
```

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00593))_

```
})
func assertError(t testing.TB, got, want error) {
    t.Helper()
if got != want {
        t.Errorf("got error %q want %q", got, want)
    }
}
```

### Write the test first

- However, we have no way to add new words to our dictionary. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00596))_
- We have a great way to search the dictionary. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00596))_
- In this test, we are utilizing our Search function to make the validation of the dictionary a little easier. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00598))_

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00597))_

```
func TestAdd(t *testing.T) {
    dictionary := Dictionary{}
    dictionary.Add("test", "this is just a test")
want := "this is just a test"
    got, err := dictionary.Search("test")
    if err != nil {
        t.Fatal("should find added word:", err)
    }
assertStrings(t, got, want)
}
```

### Write the minimal amount of code for the test to run and check output

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00600))_

```
In dictionary.go
func (d Dictionary) Add(word, definition string) {
}
Your test should now fail
dictionary_test.go:31: should find added word: could not find the 
word you were looking for
```

### Write enough code to make it pass

- You just need to specify a key and set it equal to a value. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00603))_

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00602))_

```
func (d Dictionary) Add(word, definition string) {
    d[word] = definition
}
```

## Pointers, copies, et al

- An interesting property of maps is that you can modify them without passing as an address to it (e.g &myMap ) _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00605))_
- So when you pass a map to a function/method, you are indeed copying it, but just the pointer part, not the underlying data structure that contains the data. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00608))_
- A gotcha with maps is that they can be a nil value. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00609))_
- You can read more about maps here. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00609))_
- Instead, you can initialize an empty map or use the make keyword to create a map for you: _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00612))_

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00606))_

> This may make them feel like a "reference type", but as Dave Cheney describes they are not.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00607))_

```
A map value is a pointer to a runtime.hmap structure.
```

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00610))_

> Therefore, you should never initialize a nil map variable:

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00611))_

```
var m map[string]string
```

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00612))_

> Instead, you can initialize an empty map or use the make keyword to create a map for you:

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00613))_

```
var dictionary = map[string]string{}
// OR
var dictionary = make(map[string]string)
```

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00612))_

> Instead, you can initialize an empty map or use the make keyword to create a map for you:

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00614))_

> Which ensures that you will never get a runtime panic.

### Refactor

- There isn't much to refactor in our implementation but the test could use a little simplification. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00616))_
- We made variables for word and definition, and moved the definition assertion into its own helper function. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00618))_
- Our Add is looking good. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00619))_
- Except, we didn't consider what happens when the value we are trying to add already exists! _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00619))_
- Except, we didn't consider what happens when the value we are trying to add already exists! _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00619))_
- Instead, they will go ahead and overwrite the value with the newly provided value. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00620))_
- This can be convenient in practice, but makes our function name less than accurate. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00620))_
- Map will not throw an error if the value already exists. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00620))_
- It should only add new words to our dictionary. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00620))_
- It should only add new words to our dictionary. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00620))_

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00616))_

> There isn't much to refactor in our implementation but the test could use a little simplification.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00617))_

```
func TestAdd(t *testing.T) {
    dictionary := Dictionary{}
    word := "test"
    definition := "this is just a test"
dictionary.Add(word, definition)
assertDefinition(t, dictionary, word, definition)
}
func assertDefinition(t testing.TB, dictionary Dictionary, word, 
definition string) {
t.Helper()
got, err := dictionary.Search(word)
    if err != nil {
        t.Fatal("should find added word:", err)
    }
    assertStrings(t, got, definition)
}
```

### Write the test first

- We also modified the previous test to check for a nil error. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00623))_
- For this test, we modified Add to return an error, which we are validating against a new error variable, ErrWordExists . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00623))_

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00622))_

```
func TestAdd(t *testing.T) {
    t.Run("new word", func(t *testing.T) {
        dictionary := Dictionary{}
        word := "test"
        definition := "this is just a test"
err := dictionary.Add(word, definition)
assertError(t, err, nil)
        assertDefinition(t, dictionary, word, definition)
    })
t.Run("existing word", func(t *testing.T) {
        word := "test"
        definition := "this is just a test"
        dictionary := Dictionary{word: definition}
        err := dictionary.Add(word, "new test")
assertError(t, err, ErrWordExists)
        assertDefinition(t, dictionary, word, definition)
    })
}
```

### Try to run test

- The compiler will fail because we are not returning a value for Add . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00625))_
- The compiler will fail because we are not returning a value for Add . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00625))_

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00626))_

```
./dictionary_test.go:30:13: dictionary.Add(word, definition) used as 
value
./dictionary_test.go:41:13: dictionary.Add(word, "new test") used as 
value
```

### Write the minimal amount of code for the test to run and check the output

- We are still modifying the value, and returning a nil error. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00629))_

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00628))_

```
In dictionary.go
var (
    ErrNotFound   = errors.New("could not find the word you were 
looking for")
ErrWordExists = errors.New("cannot add word because it already 
exists")
)
func (d Dictionary) Add(word, definition string) error {
    d[word] = definition
    return nil
}
```

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00630))_

```
dictionary_test.go:43: got error '%!q(<nil>)' want 'cannot add word 
because it already exists'
dictionary_test.go:44: got 'new test' want 'this is just a test'
```

### Write enough code to make it pass

- Having a switch like this provides an extra safety net, in case Search returns an error other than ErrNotFound . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00633))_
- Here we are using a switch statement to match on the error. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00633))_

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00632))_

```
func (d Dictionary) Add(word, definition string) error {
    _, err := d.Search(word)
switch err {
    case ErrNotFound:
        d[word] = definition
    case nil:
        return ErrWordExists
    default:
        return err
    }
return nil
}
```

### Refactor

- We don't have too much to refactor, but as our error usage grows we can make a few modifications. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00635))_
- We made the errors constant; this required us to create our own DictionaryErr type which implements the error interface. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00637))_
- Simply put, it makes the errors more reusable and immutable. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00637))_

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00635))_

> We don't have too much to refactor, but as our error usage grows we can make a few modifications.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00636))_

```
const (
    ErrNotFound   = DictionaryErr("could not find the word you were 
looking for")
ErrWordExists = DictionaryErr("cannot add word because it 
already exists")
)
type DictionaryErr string
func (e DictionaryErr) Error() string {
    return string(e)
}
```

### Write the test first

- Update is very closely related to Add and will be our next implementation. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00642))_

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00640))_

```
func TestUpdate(t *testing.T) {
    word := "test"
    definition := "this is just a test"
    dictionary := Dictionary{word: definition}
    newDefinition := "new definition"
```

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00641))_

```
dictionary.Update(word, newDefinition)
assertDefinition(t, dictionary, word, newDefinition)
}
```

### Try and run the test

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00644))_

```
./dictionary_test.go:53:2: dictionary.Update undefined (type 
Dictionary has no field or method Update)
```

### Write minimal amount of code for the test to run and check the failing test output

- We need to define our function. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00646))_
- With that in place, we are able to see that we need to change the definition of the word. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00648))_

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00646))_

> We already know how to deal with an error like this. We need to define our function.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00647))_

```
func (d Dictionary) Update(word, definition string) {}
```

### Write enough code to make it pass

- We already saw how to do this when we fixed the issue with Add . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00651))_
- However, we now have the same issue as with Add . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00653))_
- There is no refactoring we need to do on this since it was a simple change. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00653))_

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00652))_

```
func (d Dictionary) Update(word, definition string) {
    d[word] = definition
}
```

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00653))_

> If we pass in a new word, Update will add it to the dictionary.

### Write the test first

- We added yet another error type for when the word does not exist. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00657))_
- We also modified Update to return an error value. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00657))_

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00655))_

```
t.Run("existing word", func(t *testing.T) {
    word := "test"
    definition := "this is just a test"
    dictionary := Dictionary{word: definition}
    newDefinition := "new definition"
err := dictionary.Update(word, newDefinition)
assertError(t, err, nil)
    assertDefinition(t, dictionary, word, newDefinition)
})
t.Run("new word", func(t *testing.T) {
    word := "test"
    definition := "this is just a test"
    dictionary := Dictionary{}
```

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00656))_

```
err := dictionary.Update(word, definition)
assertError(t, err, ErrWordDoesNotExist)
})
```

### Try and run the test

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00659))_

```
./dictionary_test.go:53:16: dictionary.Update(word, newDefinition) 
used as value
./dictionary_test.go:64:16: dictionary.Update(word, definition) used 
as value
./dictionary_test.go:66:23: undefined: ErrWordDoesNotExist
```

### Write the minimal amount of code for the test to run and check the failing test output

- We added our own error type and are returning a nil error. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00663))_

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00662))_

```
const (
    ErrNotFound         = DictionaryErr("could not find the word you 
were looking for")
ErrWordExists       = DictionaryErr("cannot add word because it 
already exists")
ErrWordDoesNotExist = DictionaryErr("cannot perform operation on 
word because it does not exist")
)
func (d Dictionary) Update(word, definition string) error {
    d[word] = definition
    return nil
}
```

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00664))_

> With these changes, we now get a very clear error:

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00665))_

```
dictionary_test.go:66: got error '%!q(<nil>)' want 'cannot update 
word because it does not exist'
```

### Write enough code to make it pass

- This function looks almost identical to Add except we switched when we update the dictionary and when we return an error. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00669))_
- This function looks almost identical to Add except we switched when we update the dictionary and when we return an error. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00669))_

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00667))_

```
func (d Dictionary) Update(word, definition string) error {
    _, err := d.Search(word)
switch err {
    case ErrNotFound:
        return ErrWordDoesNotExist
    case nil:
        d[word] = definition
    default:
        return err
    }
return nil
```

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00668))_

```
}
```

## Note on declaring a new error for Update

- However, it is often better to have a precise error for when an update fails. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00671))_
- We could reuse ErrNotFound and not add a new error. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00671))_
- Having specific errors gives you more information about what went wrong. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00672))_

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00672))_

> Having specific errors gives you more information about what went wrong. Here is an example in a web app:

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00673))_

> You can redirect the user when ErrNotFound is encountered, but display an error message when ErrWordDoesNotExist is encountered.

### Write the test first

- Our test creates a Dictionary with a word and then checks if the word has been removed. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00677))_
- Our test creates a Dictionary with a word and then checks if the word has been removed. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00677))_

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00676))_

```
func TestDelete(t *testing.T) {
    word := "test"
    dictionary := Dictionary{word: "test definition"}
dictionary.Delete(word)
_, err := dictionary.Search(word)
    assertError(t, err, ErrNotFound)
}
```

### Try to run the test

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00679))_

```
By running go test we get:
./dictionary_test.go:74:6: dictionary.Delete undefined (type 
Dictionary has no field or method Delete)
```

### Write the minimal amount of code for the test to run and check the failing test output

- After we add this, the test tells us we are not deleting the word. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00682))_
- After we add this, the test tells us we are not deleting the word. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00682))_
- dictionary_test.go:78: got error '%!q(<nil>)' want 'could not find the word you were looking for' _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00683))_

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00681))_

```
func (d Dictionary) Delete(word string) {
}
```

### Write enough code to make it pass

- The first argument is the map and the second is the key to be removed. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00687))_
- Go has a built-in function delete that works on maps. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00687))_

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00685))_

```
func (d Dictionary) Delete(word string) {
    delete(d, word)
```

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00686))_

```
}
```

### Refactor

- There isn't much to refactor, but we can implement the same logic from Update to handle cases where word doesn't exist. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00689))_

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00689))_

> There isn't much to refactor, but we can implement the same logic from Update to handle cases where word doesn't exist.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00690))_

```
func TestDelete(t *testing.T) {
    t.Run("existing word", func(t *testing.T) {
        word := "test"
        dictionary := Dictionary{word: "test definition"}
err := dictionary.Delete(word)
assertError(t, err, nil)
_, err = dictionary.Search(word)
assertError(t, err, ErrNotFound)
    })
t.Run("non-existing word", func(t *testing.T) {
        word := "test"
        dictionary := Dictionary{}
err := dictionary.Delete(word)
assertError(t, err, ErrWordDoesNotExist)
    })
}
```

### Try to run test

- The compiler will fail because we are not returning a value for Delete . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00692))_
- The compiler will fail because we are not returning a value for Delete . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00692))_

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00693))_

```
./dictionary_test.go:77:10: dictionary.Delete(word) (no value) used 
as value
./dictionary_test.go:90:10: dictionary.Delete(word) (no value) used 
as value
```

### Write enough code to make it pass

- We are again using a switch statement to match on the error when we attempt to delete a word that doesn't exist. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00696))_

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00695))_

```
func (d Dictionary) Delete(word string) error {
    _, err := d.Search(word)
switch err {
    case ErrNotFound:
        return ErrWordDoesNotExist
    case nil:
        delete(d, word)
    default:
        return err
    }
return nil
}
```

### Wrapping up

## Source review

### Needs review

- Back to Testing Writing tests Go's documentation Hello, YOU A note on source control Constants Hello, world... — _fragmentary: no subject/predicate region recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00002))_
- again Back to source control Discipline Keep going! — _fragmentary: no subject/predicate region recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00002))_
- By Chris James (quii). — _fragmentary: no subject/predicate region recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00005))_
- Licensed under MIT. — _fragmentary: no subject/predicate region recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00005))_
- To run it, type go run hello.go . — _fragmentary: no subject/predicate region recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00012))_
- Now create a new file called hello_test.go where we are going to write a test for our Hello function — _unextracted: segment carries subject matter but no structured claim was recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00022))_
- Enter go test in your terminal. — _fragmentary: no subject/predicate region recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00025))_
- Enter go mod init example.com/hello in your terminal. — _fragmentary: no subject/predicate region recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00027))_
- This file tells the go tools essential information about your code. — _fragmentary: no subject/predicate region recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00029))_
- new folder before running commands like go test or go build . — _fragmentary: no subject/predicate region recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00030))_
- Run go test in your terminal. — _fragmentary: no subject/predicate region recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00032))_
- Declaring variables We're declaring some variables with the syntax varName := value , which lets us reuse some values in our test for readability. — _fragmentary: no subject/predicate region recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00033))_
- Errorf t message and fail the test. — _fragmentary: no subject/predicate region recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00034))_
- We will later explore the difference between methods and functions. — _unextracted: segment carries subject matter but no structured claim was recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00035))_
- Our next requirement is to let us specify the recipient of the greeting. — _unextracted: segment carries subject matter but no structured claim was recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00045))_
- I wouldn't push to main though, because I plan to refactor next. — _fragmentary: no subject/predicate region recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00065))_
- It's worth thinking about creating constants to capture the meaning of values and sometimes to aid performance. — _fragmentary: no subject/predicate region recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00070))_
- While we have a failing test, let's fix the code, using an if . — _unextracted: segment carries subject matter but no structured claim was recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00077))_
- This reduces duplication and improves the readability of our tests. — _fragmentary: no subject/predicate region recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00086))_
- Write a test for a user passing in Spanish. — _fragmentary: no subject/predicate region recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00107))_
- Add it to the existing suite. — _fragmentary: no subject/predicate region recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00107))_
- Remember not to cheat! — _fragmentary: no subject/predicate region recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00109))_
- - Write a test asserting that if you pass in "French" you get "Bonjour, — _fragmentary: no subject/predicate region recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00123))_
- In Go, public functions start with a capital letter, and private ones start with a lowercase letter. — _fragmentary: no subject/predicate region recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00146))_
- - The function name starts with a lowercase letter. — _fragmentary: no subject/predicate region recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00146))_
- Who knew you could get so much out of Hello, world ? — _unextracted: segment carries subject matter but no structured claim was recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00149))_
- - if , const and switch — _unextracted: segment carries subject matter but no structured claim was recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00154))_
- In our case, we've gone from Hello() to Hello("name") and then to Hello("name", "French") in small, easy-to-understand steps. — _fragmentary: no subject/predicate region recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00160))_
- Make sure that your files are organised into their own packages. — _fragmentary: no subject/predicate region recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00165))_
- That's because we want it to print an integer rather than a string. — _fragmentary: no subject/predicate region recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00170))_
- Write enough code to satisfy the compiler and that's all - remember we want to check that our tests fail for the correct reason. — _fragmentary: no subject/predicate region recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00175))_
- Ah hah! Foiled again, TDD is a sham right? — _unextracted: segment carries subject matter but no structured claim was recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00184))_
- We could write another test, with some different numbers to force that test to fail but that feels like a game of cat and mouse. — _unextracted: segment carries subject matter but no structured claim was recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00185))_
- Often code examples that can be found outside the codebase, such as a readme file, become out of date and incorrect compared to the actual code because they don't get checked. — _unextracted: segment carries subject matter but no structured claim was recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00198))_
- Add the following ExampleAdd function to the adder_test.go file. — _fragmentary: no subject/predicate region recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00200))_
- Notice the special format of the comment, // Output: 6 . — _fragmentary: no subject/predicate region recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00206))_
- Let's write a test for a function that repeats a character 5 times. — _unextracted: segment carries subject matter but no structured claim was recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00219))_
- There's nothing new so far, so try and write it yourself for practice. — _fragmentary: no subject/predicate region recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00220))_
- Unlike other languages like C, Java, or JavaScript there are no parentheses surrounding the three components of the for statement and the braces { } are always required. You might wonder what is happening in the row — _unextracted: segment carries subject matter but no structured claim was recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00234))_
- Hence, the explicit version. — _fragmentary: no subject/predicate region recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00236))_
- Now it's time to refactor and introduce another construct += assignment operator. — _fragmentary: no subject/predicate region recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00240))_
- It works with other types like integers. — _fragmentary: no subject/predicate region recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00242))_
- Writing benchmarks in Go is another first-class feature of the language and it is very similar to writing tests. — _unextracted: segment carries subject matter but no structured claim was recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00244))_
- You'll see the code is very similar to a test. — _unextracted: segment carries subject matter but no structured claim was recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00246))_
- To test this it ran it 10000000 times. — _fragmentary: no subject/predicate region recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00252))_
- This impacts performance, particularly during heavy string concatenation. — _fragmentary: no subject/predicate region recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00256))_
- Run go test -bench=. — _fragmentary: no subject/predicate region recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00260))_
- Create a new folder to work in. — _fragmentary: no subject/predicate region recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00280))_
- On each iteration, range returns two values - the index and the value. — _fragmentary: no subject/predicate region recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00301))_
- range lets you iterate over an array. — _fragmentary: no subject/predicate region recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00301))_
- If you try to pass an [4]int into a function that expects [5]int , it won't compile. — _fragmentary: no subject/predicate region recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00303))_
- We will now use the slice type which allows us to have collections of any size. The syntax is very similar to arrays, you just omit the size when declaring them — _unextracted: segment carries subject matter but no structured claim was recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00308))_
- - Break the existing API by changing the argument to Sum to be a slice rather than an array. When we do this, we will potentially ruin someone's day because our other test will no longer compile! — _unextracted: segment carries subject matter but no structured claim was recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00317))_
- In our case, no one else is using our function, so rather than having two functions to maintain, let's have just one. — _unextracted: segment carries subject matter but no structured claim was recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00319))_
- If it works for a slice of one size it's very likely it'll work for a slice of any size (within reason). — _fragmentary: no subject/predicate region recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00328))_
- Go's built-in testing toolkit features a coverage tool. — _fragmentary: no subject/predicate region recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00329))_
- Now delete one of the tests and check the coverage again. — _fragmentary: no subject/predicate region recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00332))_
- Let's go ahead and put this into practice! — _unextracted: segment carries subject matter but no structured claim was recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00349))_
- What we need to do is iterate over the varargs, calculate the sum using our existing Sum function, then add it to the slice we will return — _unextracted: segment carries subject matter but no structured claim was recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00353))_
- Lots of new things to learn! — _fragmentary: no subject/predicate region recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00355))_
- We start with an empty slice sums and append to it the result of Sum as we work through the varargs. — _fragmentary: no subject/predicate region recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00364))_
- If you omit the value on one of the sides of the : it captures everything to that side of it. — _fragmentary: no subject/predicate region recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00374))_
- Not a lot to refactor this time. — _fragmentary: no subject/predicate region recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00376))_
- What do you think would happen if you passed in an empty slice into our function? What is the "tail" of an empty slice? What happens when you tell Go to capture all elements from myEmptySlice[1:] ? — _unextracted: segment carries subject matter but no structured claim was recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00377))_
- Our tests have some repeated code around the assertions again, so let's extract those into a function. — _unextracted: segment carries subject matter but no structured claim was recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00387))_
- - How to slice, slices! — _fragmentary: no subject/predicate region recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00400))_
- Try writing more tests to solidify what you learn from reading it. — _fragmentary: no subject/predicate region recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00405))_
- Check out the Go blog post on slices for an in-depth look into slices. — _fragmentary: no subject/predicate region recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00405))_
- So far, so easy. Now let's create a function called Area(width, height float64) which returns the area of a rectangle. — _unextracted: segment carries subject matter but no structured claim was recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00421))_
- Now let's refactor the tests to use Rectangle instead of plain float64 s. — _unextracted: segment carries subject matter but no structured claim was recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00431))_
- I hope you'll agree that passing a Rectangle to a function conveys our intent more clearly, but there are more benefits of using structs that we will cover later. — _unextracted: segment carries subject matter but no structured claim was recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00434))_
- A method declaration binds an identifier, the method name, to a method, and associates the method with the receiver's base type. — _fragmentary: no subject/predicate region recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00449))_
- An example will help so let's change our tests first to call methods instead and then fix the code. — _unextracted: segment carries subject matter but no structured claim was recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00451))_
- To make circle's Area function pass we will borrow the Pi constant from the math package (remember to import it). — _unextracted: segment carries subject matter but no structured claim was recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00467))_
- How does something become a shape? We just tell Go what a Shape is using an interface declaration — _unextracted: segment carries subject matter but no structured claim was recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00479))_
- Then we fill the slice with cases. — _fragmentary: no subject/predicate region recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00498))_
- Remember, keep trying to run the test and let the compiler guide you toward a solution. — _fragmentary: no subject/predicate region recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00508))_
- So far you've only been shown syntax for creating instances of structs MyStruct{val1, val2} but you can optionally name the fields. — _unextracted: segment carries subject matter but no structured claim was recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00518))_
- The test speaks to us more clearly, as if it were an assertion of truth, not a sequence of operations — _unextracted: segment carries subject matter but no structured claim was recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00522))_
- In arrays & slices, you saw how to store values in order. — _fragmentary: no subject/predicate region recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00547))_
- The basic search was very easy to implement, but what will happen if we supply a word that's not in our dictionary? — _unextracted: segment carries subject matter but no structured claim was recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00576))_
- We actually get nothing back. — _fragmentary: no subject/predicate region recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00577))_
- This may make them feel like a "reference type", but as Dave Cheney describes they are not. — _unextracted: segment carries subject matter but no structured claim was recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00606))_
- Both approaches create an empty hash map and point dictionary at it. — _fragmentary: no subject/predicate region recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00614))_
- Add should not modify existing values. — _fragmentary: no subject/predicate region recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00620))_
- Now we get two more errors. — _fragmentary: no subject/predicate region recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00629))_
- Next, let's create a function to Update the definition of a word. — _unextracted: segment carries subject matter but no structured claim was recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00638))_
- We already know how to deal with an error like this. — _fragmentary: no subject/predicate region recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00646))_
- We get 3 errors this time, but we know how to deal with these. — _fragmentary: no subject/predicate region recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00660))_
- Next, let's create a function to Delete a word in the dictionary. — _unextracted: segment carries subject matter but no structured claim was recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00674))_
- It takes two arguments and returns nothing. — _fragmentary: no subject/predicate region recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00687))_
- We made a full CRUD (Create, Read, Update and Delete) API for our dictionary. — _fragmentary: no subject/predicate region recovered_ _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00698))_

### Disposition counts

- non-claim: 95
