---
page_id: coding-learn-go-with-tests-excerpt-value
page_kind: concept
summary: Value: 5 statement(s) and 1 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
page_family: topic-concept
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-30
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-value@e0e069f35f53358c9e6f4d3ff339f878
---

# Value

What [[coding-learn-go-with-tests-excerpt]] covers about value:

## Statements

### Arrays and slices / Write enough code to make it pass

- To get the value out of an array at a particular index, just use array[index] syntax. In this case, we are using for to iterate 5 times to work through the array and add each item onto sum . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00297))_

### Maps / Write the test first

- The value type, on the other hand, can be any type you want. It can even be another map. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00554))_

### Maps / Write enough code to make it pass

- Getting a value out of a Map is the same as getting a value out of Array map[key] . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00562))_

### Using a custom type / Write enough code to make it pass

- In order to make this pass, we are using an interesting property of the map lookup. It can return 2 values. The second value is a boolean which indicates if the key was found successfully. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00589))_

### Pointers, copies, et al / Refactor

- Our Add is looking good. Except, we didn't consider what happens when the value we are trying to add already exists! _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00619))_


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


## Related pages

- [[coding-learn-go-with-tests-excerpt-type]] - shared statements and technical atoms: Type shares source evidence from Maps / Write the test first: The value type, on the other hand, can be any type you want. It can even be another map.; Type shares technical record from Maps / Write the test first: In dictionary_test.go package main import "testing" func TestSearch(t *testing.T) { dictionary := map[string]string{"test": "this is just a test"} got := Search(dict ... [truncated] (1 shared statement(s), 1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-write-test]] - shared statements and technical atoms: Write the test first shares source evidence from Maps / Write the test first: The value type, on the other hand, can be any type you want. It can even be another map.; Write the test first shares technical record from Maps / Write the test first: In dictionary_test.go package main import "testing" func TestSearch(t *testing.T) { dictionary := map[string]string{"test": "this is just a test"} got := Search(dict ... [truncated] (1 shared statement(s), 1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-write-code-pass]] - shared statements: Write enough code to make it pass shares source evidence from Arrays and slices / Write enough code to make it pass: To get the value out of an array at a particular index, just use array[index] syntax. In this case, we are using for to iterate 5 times to work through the array and ... [truncated] (3 shared statement(s))
- [[coding-learn-go-with-tests-excerpt-array]] - shared statements: Array shares source evidence from Arrays and slices / Write enough code to make it pass: To get the value out of an array at a particular index, just use array[index] syntax. In this case, we are using for to iterate 5 times to work through the array and ... [truncated] (1 shared statement(s))

## Source

- [[coding-learn-go-with-tests-excerpt]]
