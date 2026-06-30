---
page_id: coding-learn-go-with-tests-excerpt-error
page_kind: concept
summary: Error: 6 statement(s) and 3 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
page_family: topic-concept
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-30
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-error@bb3b9be9740a0e74d41b09d35ffa9363
---

# Error

What [[coding-learn-go-with-tests-excerpt]] covers about error:

## Statements

### Arrays and slices / Try to run the test

- Once the above error is fixed, if you run go test the compiler will fail with the familiar ./sum_test.go:10:15: undefined: Sum error. Now we can proceed with writing the actual method to be tested. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00290))_

### Arrays and their type / Try and run the test

- Compile time errors are our friend because they help us write software that works, runtime errors are our enemies because they affect our users. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00383))_

### Using a custom type / Write the test first

- Notice that as we've seen in the pointers and error section here in order to assert the error message we first check that the error is not nil and then use .Error() method to get the string which we can then pass to the assertion. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00580))_

### Pointers, copies, et al / Refactor

- We made the errors constant; this required us to create our own DictionaryErr type which implements the error interface. You can read more about the details in this excellent article by Dave Cheney. Simply put, it makes the errors more reusable and immutable. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00637))_

### Note on declaring a new error for Update

- Having specific errors gives you more information about what went wrong. Here is an example in a web app: _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00672))_

### Note on declaring a new error for Update / Write the minimal amount of code for the test to run and check the failing test output

- dictionary_test.go:78: got error '%!q(<nil>)' want 'could not find the word you were looking for' _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00683))_


## Technical atoms

### Technical frame 1: Arrays and their type / Try and run the test

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00382))_

> Oh no! It's important to note that while the test has compiled , it has a runtime error .

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00381))_

```
panic: runtime error: slice bounds out of range [recovered]
panic: runtime error: slice bounds out of range
```

### Technical frame 2: Pointers, copies, et al / Refactor

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00637))_

> We made the errors constant; this required us to create our own DictionaryErr type which implements the error interface. You can read more about the details in this excellent article by Dave Cheney. Simply put, it makes the errors more reusable and immutable.

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

### Technical frame 3: Note on declaring a new error for Update

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00672))_

> Having specific errors gives you more information about what went wrong. Here is an example in a web app:

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00673))_

> You can redirect the user when ErrNotFound is encountered, but display an error message when ErrWordDoesNotExist is encountered.


## Related pages

- [[coding-learn-go-with-tests-excerpt-try-run-test]] - shared statements and technical atoms: Try and run the test shares source evidence from Arrays and slices / Try to run the test: Once the above error is fixed, if you run go test the compiler will fail with the familiar ./sum_test.go:10:15: undefined: Sum error. Now we can proceed with writing ... [truncated]; Try and run the test shares technical record from Arrays and their type / Try and run the test: panic: runtime error: slice bounds out of range [recovered] panic: runtime error: slice bounds out of range (2 shared statement(s), 1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-test]] - shared statements: Test shares source evidence from Note on declaring a new error for Update / Write the minimal amount of code for the test to run and check the failing test output: dictionary_test.go:78: got error '%!q(<nil>)' want 'could not find the word you were looking for' (1 shared statement(s))
- [[coding-learn-go-with-tests-excerpt-write-test]] - shared statements: Write the test first shares source evidence from Using a custom type / Write the test first: Notice that as we've seen in the pointers and error section here in order to assert the error message we first check that the error is not nil and then use .Error() ... [truncated] (1 shared statement(s))

## Source

- [[coding-learn-go-with-tests-excerpt]]
