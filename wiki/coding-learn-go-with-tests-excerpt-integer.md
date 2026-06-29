---
page_id: coding-learn-go-with-tests-excerpt-integer
page_kind: concept
summary: Integers: 14 statement(s) and 11 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-29
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-integer@ef70cc359ef861e53234421c43e9349f
---

# Integers

What [[coding-learn-go-with-tests-excerpt]] covers about integers:

## Statements

### Integers

- Integers work as you would expect. Let's write an Add function to try things out. Create a test file called adder_test.go and write this code. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00164))_

- Note: Go source files can only have one package per directory. Make sure that your files are organised into their own packages. Here is a good explanation on this. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00165))_

### Integers / Write the test first

- You will notice that we're using %d as our format strings rather than %q . That's because we want it to print an integer rather than a string. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00170))_

- Also note that we are no longer using the main package, instead we've defined a package named integers , as the name suggests this will group functions for working with integers such as Add . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00171))_

### Integers / Write the minimal amount of code for the test to run and check the failing test output

- Now run the tests, and we should be happy that the test is correctly reporting what is wrong. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00178))_

- If you have noticed we learnt about named return value in the last section but aren't using the same here. It should generally be used when the meaning of the result isn't clear from context, in our case it's pretty much clear that Add function will add the parameters. You can refer this wiki for more details. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00180))_

### Integers / Write enough code to make it pass

- In the strictest sense of TDD we should now write the minimal amount of code to make the test pass . A pedantic programmer may do this _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00182))_

- Once we're more familiar with Go's syntax I will introduce a technique called "Property Based Testing" , which would stop annoying developers and help you find bugs. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00186))_

### Integers / Refactor

- There's not a lot in the actual code we can really improve on here. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00191))_

- This is great because it aids the usability of code you are writing. It is preferable that a user can understand the usage of your code by just looking at the type signature and documentation. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00193))_


## Technical atoms

### Technical frame 1: Integers

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00165))_

> Note: Go source files can only have one package per directory. Make sure that your files are organised into their own packages. Here is a good explanation on this.

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

### Technical frame 2: Integers / Write the test first

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

### Technical frame 3: Integers / Try and run the test

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00173))_

```
Run the test go test
Inspect the compilation error
./adder_test.go:6:9: undefined: Add
```

### Technical frame 4: Integers / Write the minimal amount of code for the test to run and check the failing test output

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00178))_

> Now run the tests, and we should be happy that the test is correctly reporting what is wrong.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00176))_

```
package integers
func Add(x, y int) int {
    return 0
}
```

### Technical frame 5: Integers / Write the minimal amount of code for the test to run and check the failing test output

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00178))_

> Now run the tests, and we should be happy that the test is correctly reporting what is wrong.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00177))_

> Remember, when you have more than one argument of the same type (in our case two integers) rather than having (x int, y int) you can shorten it to (x, y int) .

### Technical frame 6: Integers / Write the minimal amount of code for the test to run and check the failing test output

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00180))_

> If you have noticed we learnt about named return value in the last section but aren't using the same here. It should generally be used when the meaning of the result isn't clear from context, in our case it's pretty much clear that Add function will add the parameters. You can refer this wiki for more details.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00179))_

```
adder_test.go:10: expected '4' but got '0'
```

### Technical frame 7: Integers / Write enough code to make it pass

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00186))_

> Once we're more familiar with Go's syntax I will introduce a technique called "Property Based Testing" , which would stop annoying developers and help you find bugs.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00183))_

```
func Add(x, y int) int {
    return 4
}
```

### Technical frame 8: Integers / Write enough code to make it pass

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00186))_

> Once we're more familiar with Go's syntax I will introduce a technique called "Property Based Testing" , which would stop annoying developers and help you find bugs.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00188))_

```
func Add(x, y int) int {
    return x + y
}
```

### Technical frame 9: Integers / Write enough code to make it pass

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00186))_

> Once we're more familiar with Go's syntax I will introduce a technique called "Property Based Testing" , which would stop annoying developers and help you find bugs.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00189))_

> If you re-run the tests they should pass.

### Technical frame 10: Integers / Refactor

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00193))_

> This is great because it aids the usability of code you are writing. It is preferable that a user can understand the usage of your code by just looking at the type signature and documentation.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00194))_

> You can add documentation to functions with comments, and these will appear in Go Doc just like when you look at the standard library's documentation.

### Technical frame 11: Integers / Refactor

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00193))_

> This is great because it aids the usability of code you are writing. It is preferable that a user can understand the usage of your code by just looking at the type signature and documentation.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00195))_

```
// Add takes two integers and returns the sum of them.
func Add(x, y int) int {
    return x + y
}
```


## Related pages

- [[coding-learn-go-with-tests-excerpt-code]] - shared statements and technical atoms: Code shares source evidence from Integers / Refactor: There's not a lot in the actual code we can really improve on here.; Code shares technical record from Integers / Refactor: You can add documentation to functions with comments, and these will appear in Go Doc just like when you look at the standard library's documentation. (1 shared statement(s), 1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-test]] - shared statements: Test shares source evidence from Integers: Integers work as you would expect. Let's write an Add function to try things out. Create a test file called adder_test.go and write this code. (2 shared statement(s))
- [[coding-learn-go-with-tests-excerpt-section-integers-771ce4c7]] - source section: Integers shares source evidence from Integers: Integers work as you would expect. Let's write an Add function to try things out. Create a test file called adder_test.go and write this code.; Integers shares technical record from Integers: learnGoWithTests | |-> helloworld |    |- hello.go |    |- hello_test.go | |-> integers |    |- adder_test.go | |- go.mod |- README.md (14 shared statement(s), 11 shared atom(s))

## Source

- [[coding-learn-go-with-tests-excerpt]]
