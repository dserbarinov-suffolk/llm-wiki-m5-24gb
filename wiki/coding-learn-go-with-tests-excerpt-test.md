---
page_id: coding-learn-go-with-tests-excerpt-test
page_kind: concept
summary: Test: 41 statement(s) and 32 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
page_family: broad-topic
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-30
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-test@5609203b642084aec35bda6091c7740b
---

# Test

What [[coding-learn-go-with-tests-excerpt]] covers about test:

## Statements

### Hello, World / Go modules?

- The next step is to run the tests. Enter go test in your terminal. If the tests pass, then you are probably using an earlier version of Go. However, if you are using Go 1.16 or later, the tests will likely not run. Instead, you will see an error message like this in the terminal: _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00025))_

### Hello, World / Back to Testing

- Errorf t message and fail the test. The f stands for format, which allows us to build a string with values inserted into the placeholder values %q . When you make the test fail, it should be clear how it works. You can read more about the placeholder strings in the fmt documentation. For tests, %q is very useful as it wraps your values in double quotes. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00034))_

### Hello, YOU

- In the last example, we wrote the test after the code had been written so that you could get an example of how to write a test and declare a function. From this point on, we will be writing tests first . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00044))_

- If you try and run your tests again your hello.go will fail to compile because you're not passing an argument. Send in "world" to make it compile. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00055))_

### Constants

- After refactoring, re-run your tests to make sure you haven't broken anything. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00069))_

### Constants / Hello, world... again

- If we run our tests we should see it satisfies the new requirement and we haven't accidentally broken the other functionality. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00080))_

- Now that the tests are passing, we can and should refactor our tests. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00083))_

### Discipline

- Seeing the test fail is an important check because it also lets you see what the error message looks like. As a developer it can be very hard to work with a codebase when failing tests do not give a clear idea as to what the problem is. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00101))_

- By not writing tests, you are committing to manually checking your code by running your software, which breaks your state of flow. You won't be saving yourself any time, especially in the long run. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00103))_

### Discipline / Keep going! More requirements

- When you try and run the test again it will complain about not passing through enough arguments to Hello in your other tests and in hello.go _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00113))_

- The tests should now pass. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00119))_

### French / switch

- Write a test to now include a greeting in the language of your choice and you should see how simple it is to extend our amazing function. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00133))_

### The TDD process and why the steps are important

- Write a failing test and see it fail so we know we have written a relevant test for our requirements and seen that it produces an easy to understand description of the failure _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00157))_

### Integers

- Integers work as you would expect. Let's write an Add function to try things out. Create a test file called adder_test.go and write this code. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00164))_

### Integers / Write the minimal amount of code for the test to run and check the failing test output

- Now run the tests, and we should be happy that the test is correctly reporting what is wrong. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00178))_

### Testable Examples

- Running the package's test suite, we can see the example ExampleAdd function is executed with no further arrangement from us: _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00204))_

- Notice the special format of the comment, // Output: 6 . While the example will always be compiled, adding this comment means the example will also be executed. Go ahead and temporarily remove the comment // Output: 6 , then run go test , and you will see ExampleAdd is no longer executed. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00206))_

### Iteration / Write enough code to make it pass

- Run the test and it should pass. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00237))_

### Benchmarking / Practice exercises

- Change the test so a caller can specify how many times the character is repeated and then fix the code _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00267))_

### Arrays and their type / Refactor

- It is important to question the value of your tests. It should not be a goal to have as many tests as possible, but rather to have as much confidence as possible in your code base. Having too many tests can turn in to a real problem and it just adds more overhead in maintenance. Every test has a cost . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00327))_

### Arrays and their type / Write enough code to make it pass

- The tests should now pass. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00358))_

### Arrays and their type / Try and run the test

- Oh no! It's important to note that while the test has compiled , it has a runtime error . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00382))_

### Arrays and their type / Wrapping up

- Another handy way to experiment with Go other than writing tests is the Go playground. You can try most things out and you can easily share your code if you need to ask questions. I have made a go playground with a slice in it for you to experiment with. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00406))_

### What are methods? / Write enough code to make it pass

- If you re-run the tests the rectangle tests should be passing but circle should still be failing. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00466))_

### Decoupling / Further refactoring

- Table driven tests can be a great item in your toolbox, but be sure that you have a need for the extra noise in the tests. They are a great fit when you wish to test various implementations of an interface, or if the data being passed in to a function has lots of different requirements that need testing. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00501))_

### Decoupling / Write the test first

- Adding a new test for our new shape is very easy. Just add {Triangle{12, 6}, 36.0}, to our list. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00504))_

### Decoupling / Refactor

- Now our tests - rather, the list of test cases - make assertions of truth about shapes and their areas. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00524))_

### Decoupling / Make sure your test output is helpful

- To increase the readability of our test cases further, we can rename the want field into something more descriptive like hasArea . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00529))_

- One final tip with table driven tests is to use t.Run and to name the test cases. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00530))_

### Decoupling / Wrapping up

- Table driven tests to make your assertions clearer and your test suites easier to extend & maintain _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00541))_

- Interfaces are a great tool for hiding complexity away from other parts of the system. In our case our test helper code did not need to know the exact shape it was asserting on, only how to "ask" for its area. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00543))_

- Everything else in this test should be familiar. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00555))_
- By running go test the compiler will fail with ./dictionary_test.go:8:9: undefined: Search . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00557))_
- Your test should now fail with a much clearer error message. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00585))_
- dictionary_test.go:22: expected to get an error. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00586))_
- In this test, we are utilizing our Search function to make the validation of the dictionary a little easier. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00598))_
- There isn't much to refactor in our implementation but the test could use a little simplification. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00616))_
- For this test, we modified Add to return an error, which we are validating against a new error variable, ErrWordExists . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00623))_
- Our test creates a Dictionary with a word and then checks if the word has been removed. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00677))_
- dictionary_test.go:78: got error '%!q(<nil>)' want 'could not find the word you were looking for' _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00683))_

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

### Technical frame 2: Hello, World / Go modules?

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00027))_

> What's the problem? In a word, modules. Luckily, the problem is easy to fix. Enter go mod init example.com/hello in your terminal. That will create a new file with the following contents:

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00026))_

```
$ go test
go: cannot find main module; see 'go help modules'
```

### Technical frame 3: Hello, YOU

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00055))_

> If you try and run your tests again your hello.go will fail to compile because you're not passing an argument. Send in "world" to make it compile.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00054))_

```
func Hello(name string) string {
    return "Hello, world"
}
```

### Technical frame 4: Hello, YOU

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00059))_

> We finally have a compiling program but it is not meeting our requirements according to the test.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00056))_

```
func main() {
    fmt.Println(Hello("world"))
}
```

### Technical frame 5: Hello, YOU

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00059))_

> We finally have a compiling program but it is not meeting our requirements according to the test.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00057))_

> Now when you run your tests, you should see something like

### Technical frame 6: Hello, YOU

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00059))_

> We finally have a compiling program but it is not meeting our requirements according to the test.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00058))_

```
hello_test.go:10: got 'Hello, world' want 'Hello, Chris''
```

### Technical frame 7: Hello, YOU

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00062))_

> When you run the tests, they should now pass. Normally, as part of the TDD cycle, we should now refactor .

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00061))_

```
func Hello(name string) string {
    return "Hello, " + name
}
```

### Technical frame 8: Hello, YOU

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00059))_

> We finally have a compiling program but it is not meeting our requirements according to the test.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00062))_

> When you run the tests, they should now pass.

### Technical frame 9: Constants / Hello, world... again

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00080))_

> If we run our tests we should see it satisfies the new requirement and we haven't accidentally broken the other functionality.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00078))_

```
const englishHelloPrefix = "Hello, "
func Hello(name string) string {
    if name == "" {
```

### Technical frame 10: Constants / Hello, world... again

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00080))_

> If we run our tests we should see it satisfies the new requirement and we haven't accidentally broken the other functionality.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00079))_

```
name = "World"
    }
    return englishHelloPrefix + name
}
```

### Technical frame 11: Constants / Hello, world... again

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00086))_

> We've refactored our assertion into a new function. This reduces duplication and improves the readability of our tests. We need to pass in t *testing.T so that we can tell the test code to fail when we need to.

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

### Technical frame 12: Constants / Hello, world... again

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00088))_

> t.Helper() is needed to tell the test suite that this method is a helper. By doing this, when it fails, the line number reported will be in our function call rather than inside our test helper. This will help other developers track down problems more easily. If you still don't understand, comment it out, make a test fail and observe the test output. Comments in Go are a great way to add additional information to your code, or in this case, a quick way to tell the compiler to ignore a line. You c

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00087))_

> For helper functions, it's a good idea to accept a testing.TB which is an interface that *testing.T and *testing.B both satisfy, so you can call helper functions from a test, or a benchmark (don't worry if words like "interface" mean nothing to you right now, it will be covered later).

### Technical frame 13: Constants / Hello, world... again

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00088))_

> t.Helper() is needed to tell the test suite that this method is a helper. By doing this, when it fails, the line number reported will be in our function call rather than inside our test helper. This will help other developers track down problems more easily. If you still don't understand, comment it out, make a test fail and observe the test output. Comments in Go are a great way to add additional information to your code, or in this case, a quick way to tell the compiler to ignore a line. You c

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00089))_

> When you have more than one argument of the same type (in our case two strings) rather than having (got string, want string) you can shorten it to (got, want string) .

### Technical frame 14: Discipline / Keep going! More requirements

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00113))_

> When you try and run the test again it will complain about not passing through enough arguments to Hello in your other tests and in hello.go

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00108))_

```
t.Run("in Spanish", func(t *testing.T) {
        got := Hello("Elodie", "Spanish")
        want := "Hola, Elodie"
        assertCorrectMessage(t, got, want)
    })
```

### Technical frame 15: Discipline / Keep going! More requirements

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00113))_

> When you try and run the test again it will complain about not passing through enough arguments to Hello in your other tests and in hello.go

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00110))_

```
./hello_test.go:27:19: too many arguments in call to Hello
have (string, string)
   want (string)
```

### Technical frame 16: Discipline / Keep going! More requirements

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00113))_

> When you try and run the test again it will complain about not passing through enough arguments to Hello in your other tests and in hello.go

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00112))_

```
func Hello(name string, language string) string {
    if name == "" {
        name = "World"
    }
    return englishHelloPrefix + name
}
```

### Technical frame 17: Discipline / Keep going! More requirements

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00119))_

> The tests should now pass.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00114))_

```
./hello.go:15:19: not enough arguments in call to Hello
have (string)
   want (string, string)
```

### Technical frame 18: Discipline / Keep going! More requirements

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00119))_

> The tests should now pass.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00115))_

> Now all your tests should compile and pass, apart from our new scenario

### Technical frame 19: Discipline / Keep going! More requirements

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00119))_

> The tests should now pass.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00116))_

```
hello_test.go:29: got 'Hello, Elodie' want 'Hola, Elodie'
```

### Technical frame 20: Discipline / Keep going! More requirements

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

### Technical frame 21: Testable Examples

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

### Technical frame 22: Testable Examples

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

### Technical frame 23: Testable Examples

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00208))_

> To view example documentation, let's take a quick look at pkgsite . Before navigating to your project's directory, make sure you have installed pkgsite by running the following command: go install golang.org/x/pkgsite/cmd/pkgsite@latest , then run pkgsite -open . , which should open a web browser for you, pointing to http://localhost:8080 . Inside here you'll see a list of all of Go's Standard Library packages, plus Third Party packages you have installed, under which you should see your example

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00209))_

> If you publish your code with examples to a public URL, you can share the documentation of your code at pkg.go.dev.

### Technical frame 24: Arrays and their type / Refactor

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00327))_

> It is important to question the value of your tests. It should not be a goal to have as many tests as possible, but rather to have as much confidence as possible in your code base. Having too many tests can turn in to a real problem and it just adds more overhead in maintenance. Every test has a cost .

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

### Technical frame 25: Arrays and their type / Wrapping up

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00407))_

> Here is an example of slicing an array and how changing the slice affects the original array; but a "copy" of the slice will not affect the original array. Another example of why it's a good idea to make a copy of a slice after slicing a very large slice.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00406))_

> You can try most things out and you can easily share your code if you need to ask questions.

### Technical frame 26: Decoupling / Further refactoring

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00498))_

> The only new syntax here is creating an "anonymous struct", areaTests . We are declaring a slice of structs by using []struct with two fields, the shape and the want . Then we fill the slice with cases.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00496))_

> Table driven tests are useful when you want to build a list of test cases that can be tested in the same manner.

### Technical frame 27: Decoupling / Further refactoring

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00498))_

> The only new syntax here is creating an "anonymous struct", areaTests . We are declaring a slice of structs by using []struct with two fields, the shape and the want . Then we fill the slice with cases.

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

### Technical frame 28: Decoupling / Write the test first

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00504))_

> Adding a new test for our new shape is very easy. Just add {Triangle{12, 6}, 36.0}, to our list.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00505))_

```
func TestArea(t *testing.T) {
areaTests := []struct {
        shape Shape
        want  float64
```

### Technical frame 29: Decoupling / Write the test first

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

### Technical frame 30: Decoupling / Make sure your test output is helpful

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00533))_

> And you can run specific tests within your table with go test -run TestArea/Rectangle .

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00532))_

```
--- FAIL: TestArea (0.00s)
--- FAIL: TestArea/Rectangle (0.00s)
       shapes_test.go:33: main.Rectangle{Width:12, Height:6} got 
72.00 want 72.10
```

### Technical frame 31: Decoupling / Make sure your test output is helpful

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

### Technical frame 32: Pointers, copies, et al / Refactor

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00618))_

> We made variables for word and definition, and moved the definition assertion into its own helper function.

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


## Related pages

- [[coding-learn-go-with-tests-excerpt-try-run-test]] - narrower topic: Try and run the test shares source evidence from Hello, YOU: If you try and run your tests again your hello.go will fail to compile because you're not passing an argument. Send in "world" to make it compile.; Try and run the test shares technical record from Learn Go with Tests (Excerpt): output Write enough code to make it pass Refactor Write the test ﬁrst Try and run the test Write minimal amount of code for the test to run and check the failing tes ... [truncated] (10 shared statement(s), 4 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-write-test]] - narrower topic: Write the test first shares source evidence from Hello, YOU: In the last example, we wrote the test after the code had been written so that you could get an example of how to write a test and declare a function. From this poin ... [truncated]; Write the test first shares technical record from Learn Go with Tests (Excerpt): output Write enough code to make it pass Refactor Write the test ﬁrst Try and run the test Write minimal amount of code for the test to run and check the failing tes ... [truncated] (9 shared statement(s), 3 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-write-code-pass]] - shared statements and technical atoms: Write enough code to make it pass shares source evidence from Hello, YOU: In the last example, we wrote the test after the code had been written so that you could get an example of how to write a test and declare a function. From this poin ... [truncated]; Write enough code to make it pass shares technical record from Learn Go with Tests (Excerpt): output Write enough code to make it pass Refactor Write the test ﬁrst Try and run the test Write minimal amount of code for the test to run and check the failing tes ... [truncated] (5 shared statement(s), 1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-code]] - shared statements and technical atoms: Code shares source evidence from Hello, YOU: In the last example, we wrote the test after the code had been written so that you could get an example of how to write a test and declare a function. From this poin ... [truncated]; Code shares technical record from Learn Go with Tests (Excerpt): output Write enough code to make it pass Refactor Write the test ﬁrst Try and run the test Write minimal amount of code for the test to run and check the failing tes ... [truncated] (2 shared statement(s), 2 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-write]] - shared statements and technical atoms: Write shares source evidence from French / switch: Write a test to now include a greeting in the language of your choice and you should see how simple it is to extend our amazing function.; Write shares technical record from Learn Go with Tests (Excerpt): output Write enough code to make it pass Refactor Write the test ﬁrst Try and run the test Write minimal amount of code for the test to run and check the failing tes ... [truncated] (2 shared statement(s), 1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-array]] - shared technical atoms: Array shares technical record from Arrays and their type / Refactor: func TestSum(t *testing.T) { t.Run("collection of 5 numbers", func(t *testing.T) { numbers := []int{1, 2, 3, 4, 5} got := Sum(numbers) want := 15 if got != want { t. ... [truncated] (1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-error]] - shared statements: Error shares source evidence from Note on declaring a new error for Update / Write the minimal amount of code for the test to run and check the failing test output: dictionary_test.go:78: got error '%!q(<nil>)' want 'could not find the word you were looking for' (1 shared statement(s))
- [[coding-learn-go-with-tests-excerpt-note]] - shared statements: Note shares source evidence from Arrays and their type / Try and run the test: Oh no! It's important to note that while the test has compiled , it has a runtime error . (1 shared statement(s))

## Source

- [[coding-learn-go-with-tests-excerpt]]
