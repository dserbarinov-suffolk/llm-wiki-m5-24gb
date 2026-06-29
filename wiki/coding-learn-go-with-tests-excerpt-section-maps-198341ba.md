---
page_id: coding-learn-go-with-tests-excerpt-section-maps-198341ba
page_kind: source
summary: Maps: 21 source-backed entries and 5 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-29
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-maps-198341ba@e5e19fefd105a908f8effc5c734327fb
---

# Maps

From [[coding-learn-go-with-tests-excerpt]].

## Related pages

- [[coding-learn-go-with-tests-excerpt-section-maps-write-the-test-first-3b38a417]] - narrower source section: Maps / Write the test first
- [[coding-learn-go-with-tests-excerpt-section-maps-try-to-run-the-test-74951c57]] - narrower source section: Maps / Try to run the test
- [[coding-learn-go-with-tests-excerpt-section-maps-write-the-minimal-amount-of-code-for-the-test-to-run-and-check-the-output-dbf2203c]] - narrower source section: Maps / Write the minimal amount of code for the test to run and check the output
- [[coding-learn-go-with-tests-excerpt-section-maps-write-enough-code-to-make-it-pass-e76e129f]] - narrower source section: Maps / Write enough code to make it pass
- [[coding-learn-go-with-tests-excerpt-section-maps-refactor-a6824beb]] - narrower source section: Maps / Refactor
- [[coding-learn-go-with-tests-excerpt-section-decoupling-1c6183b3]] - previous source section: Decoupling
- [[coding-learn-go-with-tests-excerpt-section-using-a-custom-type-3f6de7c1]] - next source section: Using a custom type
- [[coding-learn-go-with-tests-excerpt-maps]] - topic hub: opens the topic page for Maps

## Statements

- Maps allow you to store items in a manner similar to a dictionary. You can think of the key as the word and the value as the definition. And what better way is there to learn about Maps than to build our own dictionary? _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00548))_
- First, assuming we already have some words with their definitions in the dictionary, if we search for a word, it should return the definition of it. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00549))_

## Statements by subsection

### Maps / Write the test first

- Declaring a Map is somewhat similar to an array. Except, it starts with the map keyword and requires two types. The first is the key type, which is written inside the [] . The second is the value type, which goes right after the [] . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00552))_
- The key type is special. It can only be a comparable type because without the ability to tell if 2 keys are equal, we have no way to ensure that we are getting the correct value. Comparable types are explained in depth in the language spec. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00553))_
- The value type, on the other hand, can be any type you want. It can even be another map. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00554))_
- Everything else in this test should be familiar. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00555))_
- The second is the value type, which goes right after the [] . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00552))_
- The first is the key type, which is written inside the [] . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00552))_
- Except, it starts with the map keyword and requires two types. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00552))_

### Maps / Try to run the test

- By running go test the compiler will fail with ./dictionary_test.go:8:9: undefined: Search . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00557))_

### Maps / Write enough code to make it pass

- Getting a value out of a Map is the same as getting a value out of Array map[key] . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00562))_

### Maps / Refactor

- I decided to create an assertStrings helper to make the implementation more general. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00565))_

## Technical atoms

### Technical frame 1: Maps / Write the test first

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00552))_

> Declaring a Map is somewhat similar to an array. Except, it starts with the map keyword and requires two types. The first is the key type, which is written inside the [] . The second is the value type, which goes right after the [] .

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

### Technical frame 2: Maps / Write the test first

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00554))_

> The value type, on the other hand, can be any type you want. It can even be another map.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00553))_

> It can only be a comparable type because without the ability to tell if 2 keys are equal, we have no way to ensure that we are getting the correct value.

### Technical frame 3: Maps / Write the minimal amount of code for the test to run and check the output

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

### Technical frame 4: Maps / Write enough code to make it pass

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00562))_

> Getting a value out of a Map is the same as getting a value out of Array map[key] .

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00561))_

```
func Search(dictionary map[string]string, word string) string {
    return dictionary[word]
}
```

### Technical frame 5: Maps / Refactor

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00565))_

> I decided to create an assertStrings helper to make the implementation more general.

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
