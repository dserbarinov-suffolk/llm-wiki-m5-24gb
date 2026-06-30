---
page_id: coding-learn-go-with-tests-excerpt-function
page_kind: concept
summary: Function: 7 statement(s) and 7 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
page_family: topic-concept
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-30
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-function@24fc5f8c14446c2374535652b046d8b2
---

# Function

What [[coding-learn-go-with-tests-excerpt]] covers about function:

## Statements

### one...last...refactor?

- In our function signature we have made a named return value (prefix string) . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00140))_

### Testable Examples

- Example functions are compiled whenever tests are executed. Because such examples are validated by the Go compiler, you can be confident your documentation's examples always reflect current code behavior. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00199))_

### Arrays and their type / Write the minimal amount of code for the test to run and check the failing test output

- From Go 1.21, slices standard package is available, which has slices.Equal function to do a simple shallow compare on slices, where you don't need to worry about the types like the above case. Note that this function expects the elements to be comparable. So, it can't be applied to slices with non-comparable elements like 2D slices. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00348))_

### Arrays and their type / Refactor

- By defining this function inside the test, it cannot be used by other functions in this package. Hiding variables and functions that don't need to be exported is an important design consideration. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00391))_

### Using a custom type / Write the test first

- We actually get nothing back. This is good because the program can continue to run, but there is a better approach. The function can report that the word is not in the dictionary. This way, the user isn't left wondering if the word doesn't exist or if there is just no definition (this might not seem very useful for a dictionary. However, it's a scenario that could be key in other usecases). _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00577))_

### Pointers, copies, et al

- So when you pass a map to a function/method, you are indeed copying it, but just the pointer part, not the underlying data structure that contains the data. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00608))_

### Pointers, copies, et al / Write enough code to make it pass

- This function looks almost identical to Add except we switched when we update the dictionary and when we return an error. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00669))_


## Technical atoms

### Technical frame 1: Testable Examples

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

### Technical frame 2: Testable Examples

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

### Technical frame 3: Arrays and their type / Write the minimal amount of code for the test to run and check the failing test output

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00347))_

> Go does not let you use equality operators with slices. You could write a function to iterate over each got and want slice and check their values, but what if we had a more convenient way to do this?

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00346))_

```
./sum_test.go:26:9: invalid operation: got != want (slice can only 
be compared to nil)
```

### Technical frame 4: Arrays and their type / Write the minimal amount of code for the test to run and check the failing test output

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00351))_

> You should have test output like the following: sum_test.go:30: got [] want [3 9]

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

### Technical frame 5: Arrays and their type / Refactor

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00392))_

> A handy side-effect of this is this adds a little type-safety to our code. If a developer mistakenly adds a new test with checkSums(t, got, "dave") the compiler will stop them in their tracks.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00393))_

```
$ go test
./sum_test.go:52:21: cannot use "dave" (type string) as type []int 
in argument to checkSums
```

### Technical frame 6: Using a custom type / Write the test first

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00579))_

> The way to handle this scenario in Go is to return a second argument which is an Error type.

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

### Technical frame 7: Pointers, copies, et al / Write minimal amount of code for the test to run and check the failing test output

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00648))_

> With that in place, we are able to see that we need to change the definition of the word.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00647))_

```
func (d Dictionary) Update(word, definition string) {}
```


## Related pages

- [[coding-learn-go-with-tests-excerpt-note]] - shared statements and technical atoms: Note shares source evidence from Arrays and their type / Write the minimal amount of code for the test to run and check the failing test output: From Go 1.21, slices standard package is available, which has slices.Equal function to do a simple shallow compare on slices, where you don't need to worry about the ... [truncated]; Note shares technical record from Arrays and their type / Write the minimal amount of code for the test to run and check the failing test output: ./sum_test.go:26:9: invalid operation: got != want (slice can only be compared to nil) (1 shared statement(s), 1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-write-test]] - shared statements and technical atoms: Write the test first shares source evidence from Using a custom type / Write the test first: We actually get nothing back. This is good because the program can continue to run, but there is a better approach. The function can report that the word is not in t ... [truncated]; Write the test first shares technical record from Using a custom type / Write the test first: func TestSearch(t *testing.T) { dictionary := Dictionary{"test": "this is just a test"} t.Run("known word", func(t *testing.T) { got, _ := dictionary.Search("test") ... [truncated] (1 shared statement(s), 1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-package]] - shared technical atoms: Package shares technical record from Testable Examples: func ExampleAdd() { sum := Add(1, 5) fmt.Println(sum) // Output: 6 } (3 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-test]] - shared technical atoms: Test shares technical record from Testable Examples: func ExampleAdd() { sum := Add(1, 5) fmt.Println(sum) // Output: 6 } (2 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-comment]] - shared technical atoms: Comment shares technical record from Testable Examples: $ go test -v === RUN   TestAdder --- PASS: TestAdder (0.00s) === RUN   ExampleAdd --- PASS: ExampleAdd (0.00s) (1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-standard]] - shared technical atoms: Standard shares technical record from Arrays and their type / Write the minimal amount of code for the test to run and check the failing test output: ./sum_test.go:26:9: invalid operation: got != want (slice can only be compared to nil) (1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-try-run-test]] - shared technical atoms: Try and run the test shares technical record from Testable Examples: $ go test -v === RUN   TestAdder --- PASS: TestAdder (0.00s) === RUN   ExampleAdd --- PASS: ExampleAdd (0.00s) (1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-write-code-pass]] - shared statements: Write enough code to make it pass shares source evidence from Pointers, copies, et al / Write enough code to make it pass: This function looks almost identical to Add except we switched when we update the dictionary and when we return an error. (1 shared statement(s))

## Source

- [[coding-learn-go-with-tests-excerpt]]
