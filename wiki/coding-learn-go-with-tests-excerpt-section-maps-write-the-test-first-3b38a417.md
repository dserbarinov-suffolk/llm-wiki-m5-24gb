---
page_id: coding-learn-go-with-tests-excerpt-section-maps-write-the-test-first-3b38a417
page_kind: source
summary: Maps / Write the test first: 13 source-backed entries and 2 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-29
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-maps-write-the-test-first-3b38a417@ae2c039de551c5578697638ea7100b3a
---

# Maps / Write the test first

From [[coding-learn-go-with-tests-excerpt]].

## Related pages

- [[coding-learn-go-with-tests-excerpt-section-maps-198341ba]] - broader source section: Maps
- [[coding-learn-go-with-tests-excerpt-section-maps-try-to-run-the-test-74951c57]] - next source section: Maps / Try to run the test

## Statements

- Declaring a Map is somewhat similar to an array. Except, it starts with the map keyword and requires two types. The first is the key type, which is written inside the [] . The second is the value type, which goes right after the [] . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00552))_
- The key type is special. It can only be a comparable type because without the ability to tell if 2 keys are equal, we have no way to ensure that we are getting the correct value. Comparable types are explained in depth in the language spec. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00553))_
- The value type, on the other hand, can be any type you want. It can even be another map. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00554))_
- Everything else in this test should be familiar. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00555))_
- The second is the value type, which goes right after the [] . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00552))_
- The first is the key type, which is written inside the [] . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00552))_
- Except, it starts with the map keyword and requires two types. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00552))_

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
