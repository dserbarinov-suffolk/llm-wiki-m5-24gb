---
page_id: coding-learn-go-with-tests-excerpt-section-using-a-custom-type-3f6de7c1
page_kind: source
summary: Using a custom type: 36 source-backed entries and 12 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-29
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-using-a-custom-type-3f6de7c1@2c29756261534a8682911f8b369b488f
---

# Using a custom type

From [[coding-learn-go-with-tests-excerpt]].

## Related pages

- [[coding-learn-go-with-tests-excerpt-section-using-a-custom-type-write-the-test-first-4c4dcc55]] - narrower source section: Using a custom type / Write the test first
- [[coding-learn-go-with-tests-excerpt-section-using-a-custom-type-try-and-run-the-test-ebf022ab]] - narrower source section: Using a custom type / Try and run the test
- [[coding-learn-go-with-tests-excerpt-section-using-a-custom-type-write-the-minimal-amount-of-code-for-the-test-to-run-and-check-the-output-96d1b867]] - narrower source section: Using a custom type / Write the minimal amount of code for the test to run and check the output
- [[coding-learn-go-with-tests-excerpt-section-using-a-custom-type-write-enough-code-to-make-it-pass-0fbec14c]] - narrower source section: Using a custom type / Write enough code to make it pass
- [[coding-learn-go-with-tests-excerpt-section-using-a-custom-type-refactor-862871b5]] - narrower source section: Using a custom type / Refactor
- [[coding-learn-go-with-tests-excerpt-section-using-a-custom-type-write-the-test-first-d5397d92]] - narrower source section: Using a custom type / Write the test first
- [[coding-learn-go-with-tests-excerpt-section-using-a-custom-type-write-the-minimal-amount-of-code-for-the-test-to-run-and-check-output-ef8ec6d6]] - narrower source section: Using a custom type / Write the minimal amount of code for the test to run and check output
- [[coding-learn-go-with-tests-excerpt-section-using-a-custom-type-write-enough-code-to-make-it-pass-7b766fd4]] - narrower source section: Using a custom type / Write enough code to make it pass
- [[coding-learn-go-with-tests-excerpt-section-maps-198341ba]] - previous source section: Maps
- [[coding-learn-go-with-tests-excerpt-section-pointers-copies-et-al-36483230]] - next source section: Pointers, copies, et al
- [[coding-learn-go-with-tests-excerpt-custom-type]] - topic hub: opens the topic page for Custom Type

## Statements

- We started using the Dictionary type, which we have not defined yet. Then called Search on the Dictionary instance. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00570))_
- We did not need to change assertStrings . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00571))_
- Here we created a Dictionary type which acts as a thin wrapper around map . With the custom type defined, we can create the Search method. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00574))_
- Then called Search on the Dictionary instance. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00570))_

## Statements by subsection

### Using a custom type / Write the test first

- We actually get nothing back. This is good because the program can continue to run, but there is a better approach. The function can report that the word is not in the dictionary. This way, the user isn't left wondering if the word doesn't exist or if there is just no definition (this might not seem very useful for a dictionary. However, it's a scenario that could be key in other usecases). _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00577))_
- The way to handle this scenario in Go is to return a second argument which is an Error type. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00579))_
- Notice that as we've seen in the pointers and error section here in order to assert the error message we first check that the error is not nil and then use .Error() method to get the string which we can then pass to the assertion. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00580))_
- This is good because the program can continue to run, but there is a better approach. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00577))_
- Notice that as we've seen in the pointers and error section here in order to assert the error message we first check that the error is not nil and then use .Error() method to get the string which we can then pass to the assertion. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00580))_

### Using a custom type / Write the minimal amount of code for the test to run and check the output

- Your test should now fail with a much clearer error message. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00585))_
- dictionary_test.go:22: expected to get an error. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00586))_

### Using a custom type / Write enough code to make it pass

- In order to make this pass, we are using an interesting property of the map lookup. It can return 2 values. The second value is a boolean which indicates if the key was found successfully. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00589))_
- This property allows us to differentiate between a word that doesn't exist and a word that just doesn't have a definition. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00590))_

### Using a custom type / Refactor

- By creating a new helper we were able to simplify our test, and start using our ErrNotFound variable so our test doesn't fail if we change the error text in the future. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00594))_

### Using a custom type / Write the test first

- We have a great way to search the dictionary. However, we have no way to add new words to our dictionary. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00596))_
- In this test, we are utilizing our Search function to make the validation of the dictionary a little easier. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00598))_

### Using a custom type / Write enough code to make it pass

- Adding to a map is also similar to an array. You just need to specify a key and set it equal to a value. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00603))_

## Technical atoms

### Technical frame 1: Using a custom type

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00570))_

> We started using the Dictionary type, which we have not defined yet. Then called Search on the Dictionary instance.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00568))_

```
In dictionary_test.go:
func TestSearch(t *testing.T) {
    dictionary := Dictionary{"test": "this is just a test"}
got := dictionary.Search("test")
    want := "this is just a test"
```

### Technical frame 2: Using a custom type

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00570))_

> We started using the Dictionary type, which we have not defined yet. Then called Search on the Dictionary instance.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00569))_

```
assertStrings(t, got, want)
}
```

### Technical frame 3: Using a custom type

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00574))_

> Here we created a Dictionary type which acts as a thin wrapper around map . With the custom type defined, we can create the Search method.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00573))_

```
type Dictionary map[string]string
func (d Dictionary) Search(word string) string {
    return d[word]
}
```

### Technical frame 4: Using a custom type / Write the test first

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

### Technical frame 5: Using a custom type / Try and run the test

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00582))_

```
This does not compile
./dictionary_test.go:18:10: assignment mismatch: 2 variables but 1 
values
```

### Technical frame 6: Using a custom type / Write the minimal amount of code for the test to run and check the output

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00585))_

> Your test should now fail with a much clearer error message.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00584))_

```
func (d Dictionary) Search(word string) (string, error) {
    return d[word], nil
}
```

### Technical frame 7: Using a custom type / Write enough code to make it pass

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00589))_

> In order to make this pass, we are using an interesting property of the map lookup. It can return 2 values. The second value is a boolean which indicates if the key was found successfully.

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

### Technical frame 8: Using a custom type / Refactor

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00594))_

> By creating a new helper we were able to simplify our test, and start using our ErrNotFound variable so our test doesn't fail if we change the error text in the future.

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

### Technical frame 9: Using a custom type / Refactor

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00594))_

> By creating a new helper we were able to simplify our test, and start using our ErrNotFound variable so our test doesn't fail if we change the error text in the future.

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

### Technical frame 10: Using a custom type / Write the test first

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00598))_

> In this test, we are utilizing our Search function to make the validation of the dictionary a little easier.

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

### Technical frame 11: Using a custom type / Write the minimal amount of code for the test to run and check output

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00600))_

```
In dictionary.go
func (d Dictionary) Add(word, definition string) {
}
Your test should now fail
dictionary_test.go:31: should find added word: could not find the 
word you were looking for
```

### Technical frame 12: Using a custom type / Write enough code to make it pass

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00603))_

> Adding to a map is also similar to an array. You just need to specify a key and set it equal to a value.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00602))_

```
func (d Dictionary) Add(word, definition string) {
    d[word] = definition
}
```
