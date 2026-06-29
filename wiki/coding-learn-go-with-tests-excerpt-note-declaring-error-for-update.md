---
page_id: coding-learn-go-with-tests-excerpt-note-declaring-error-for-update
page_kind: concept
summary: Note on declaring a new error for Update: 11 statement(s) and 9 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-29
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-note-declaring-error-for-update@366161d22d3cd57b75fefbc8df0034a0
---

# Note on declaring a new error for Update

What [[coding-learn-go-with-tests-excerpt]] covers about note on declaring a new error for update:

## Statements

### Note on declaring a new error for Update

- We could reuse ErrNotFound and not add a new error. However, it is often better to have a precise error for when an update fails. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00671))_

- Having specific errors gives you more information about what went wrong. Here is an example in a web app: _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00672))_

### Note on declaring a new error for Update / Write the test first

- Our test creates a Dictionary with a word and then checks if the word has been removed. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00677))_

### Note on declaring a new error for Update / Write the minimal amount of code for the test to run and check the failing test output

- After we add this, the test tells us we are not deleting the word. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00682))_

- dictionary_test.go:78: got error '%!q(<nil>)' want 'could not find the word you were looking for' _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00683))_

### Note on declaring a new error for Update / Write enough code to make it pass

- Go has a built-in function delete that works on maps. It takes two arguments and returns nothing. The first argument is the map and the second is the key to be removed. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00687))_

### Note on declaring a new error for Update / Refactor

- There isn't much to refactor, but we can implement the same logic from Update to handle cases where word doesn't exist. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00689))_

### Note on declaring a new error for Update / Try to run test

- The compiler will fail because we are not returning a value for Delete . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00692))_

### Note on declaring a new error for Update / Write enough code to make it pass

- We are again using a switch statement to match on the error when we attempt to delete a word that doesn't exist. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00696))_


## Technical atoms

### Technical frame 1: Note on declaring a new error for Update

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00672))_

> Having specific errors gives you more information about what went wrong. Here is an example in a web app:

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00673))_

> You can redirect the user when ErrNotFound is encountered, but display an error message when ErrWordDoesNotExist is encountered.

### Technical frame 2: Note on declaring a new error for Update / Write the test first

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00677))_

> Our test creates a Dictionary with a word and then checks if the word has been removed.

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

### Technical frame 3: Note on declaring a new error for Update / Try to run the test

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00679))_

```
By running go test we get:
./dictionary_test.go:74:6: dictionary.Delete undefined (type 
Dictionary has no field or method Delete)
```

### Technical frame 4: Note on declaring a new error for Update / Write the minimal amount of code for the test to run and check the failing test output

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00682))_

> After we add this, the test tells us we are not deleting the word.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00681))_

```
func (d Dictionary) Delete(word string) {
}
```

### Technical frame 5: Note on declaring a new error for Update / Write enough code to make it pass

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00687))_

> Go has a built-in function delete that works on maps. It takes two arguments and returns nothing. The first argument is the map and the second is the key to be removed.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00685))_

```
func (d Dictionary) Delete(word string) {
    delete(d, word)
```

### Technical frame 6: Note on declaring a new error for Update / Write enough code to make it pass

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00687))_

> Go has a built-in function delete that works on maps. It takes two arguments and returns nothing. The first argument is the map and the second is the key to be removed.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00686))_

```
}
```

### Technical frame 7: Note on declaring a new error for Update / Refactor

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

### Technical frame 8: Note on declaring a new error for Update / Try to run test

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00692))_

> The compiler will fail because we are not returning a value for Delete .

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00693))_

```
./dictionary_test.go:77:10: dictionary.Delete(word) (no value) used 
as value
./dictionary_test.go:90:10: dictionary.Delete(word) (no value) used 
as value
```

### Technical frame 9: Note on declaring a new error for Update / Write enough code to make it pass

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00696))_

> We are again using a switch statement to match on the error when we attempt to delete a word that doesn't exist.

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


## Related pages

- [[coding-learn-go-with-tests-excerpt-test]] - shared statements: Test shares source evidence from Note on declaring a new error for Update / Write the test first: Our test creates a Dictionary with a word and then checks if the word has been removed. (1 shared statement(s))
- [[coding-learn-go-with-tests-excerpt-section-note-on-declaring-a-new-error-for-update-a49f3aa6]] - source section: Note on declaring a new error for Update shares source evidence from Note on declaring a new error for Update: We could reuse ErrNotFound and not add a new error. However, it is often better to have a precise error for when an update fails.; Note on declaring a new error for Update shares technical record from Note on declaring a new error for Update: You can redirect the user when ErrNotFound is encountered, but display an error message when ErrWordDoesNotExist is encountered. (11 shared statement(s), 9 shared atom(s))

## Source

- [[coding-learn-go-with-tests-excerpt]]
