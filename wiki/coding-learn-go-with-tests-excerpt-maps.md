---
page_id: coding-learn-go-with-tests-excerpt-maps
page_kind: concept
summary: Maps: 13 statement(s) and 5 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-29
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-maps@03a5f42aa121dcfa2c76b00965b63eff
---

# Maps

What [[coding-learn-go-with-tests-excerpt]] covers about maps:

## Statements

### Maps

- Maps allow you to store items in a manner similar to a dictionary. You can think of the key as the word and the value as the definition. And what better way is there to learn about Maps than to build our own dictionary? _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00548))_

- First, assuming we already have some words with their definitions in the dictionary, if we search for a word, it should return the definition of it. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00549))_

### Maps / Write the test first

- Declaring a Map is somewhat similar to an array. Except, it starts with the map keyword and requires two types. The first is the key type, which is written inside the [] . The second is the value type, which goes right after the [] . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00552))_

- The key type is special. It can only be a comparable type because without the ability to tell if 2 keys are equal, we have no way to ensure that we are getting the correct value. Comparable types are explained in depth in the language spec. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00553))_

- The value type, on the other hand, can be any type you want. It can even be another map. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00554))_

- Everything else in this test should be familiar. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00555))_

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


## Related pages

- [[coding-learn-go-with-tests-excerpt-type]] - shared statements and technical atoms: Type shares source evidence from Maps / Write the test first: The key type is special. It can only be a comparable type because without the ability to tell if 2 keys are equal, we have no way to ensure that we are getting the c ... [truncated]; Type shares technical record from Maps / Write the test first: In dictionary_test.go package main import "testing" func TestSearch(t *testing.T) { dictionary := map[string]string{"test": "this is just a test"} got := Search(dict ... [truncated] (3 shared statement(s), 1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-test]] - shared statements: Test shares source evidence from Maps / Write the test first: Everything else in this test should be familiar. (2 shared statement(s))
- [[coding-learn-go-with-tests-excerpt-section-maps-198341ba]] - source section: Maps shares source evidence from Maps: Maps allow you to store items in a manner similar to a dictionary. You can think of the key as the word and the value as the definition. And what better way is there ... [truncated]; Maps shares technical record from Maps / Write the test first: In dictionary_test.go package main import "testing" func TestSearch(t *testing.T) { dictionary := map[string]string{"test": "this is just a test"} got := Search(dict ... [truncated] (13 shared statement(s), 5 shared atom(s))

## Source

- [[coding-learn-go-with-tests-excerpt]]
