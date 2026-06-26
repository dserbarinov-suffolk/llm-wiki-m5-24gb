---
page_id: coding-learn-go-with-tests-excerpt-value
page_kind: concept
summary: Value: 5 statement(s) and 1 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-value@c8860f60fa64ae1d0af53260365ffe06
---

# Value

What [[coding-learn-go-with-tests-excerpt]] covers about value:

## Statements

- Getting a value out of a Map is the same as getting a value out of Array map[key] . _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00562))_
- To get the value out of an array at a particular index, just use array[index] syntax. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00297))_
- The value type, on the other hand, can be any type you want. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00554))_
- The second value is a boolean which indicates if the key was found successfully. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00589))_
- Except, we didn't consider what happens when the value we are trying to add already exists! _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00619))_

## Technical atoms

> Context: The key type is special. It can only be a comparable type because without the ability to tell if 2 keys are equal, we have no way to ensure that we are getting the correct value. Comparable types are explained in depth in the language spec.
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00553))_

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
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00551))_


## Source

- [[coding-learn-go-with-tests-excerpt]]
