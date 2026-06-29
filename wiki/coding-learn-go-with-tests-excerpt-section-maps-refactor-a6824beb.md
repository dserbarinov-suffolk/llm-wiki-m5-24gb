---
page_id: coding-learn-go-with-tests-excerpt-section-maps-refactor-a6824beb
page_kind: source
summary: Maps / Refactor: 2 source-backed entries and 1 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-29
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-maps-refactor-a6824beb@eb19b12f18c8bfe99b06979f1abae2d9
---

# Maps / Refactor

From [[coding-learn-go-with-tests-excerpt]].

## Related pages

- [[coding-learn-go-with-tests-excerpt-section-maps-198341ba]] - broader source section: Maps
- [[coding-learn-go-with-tests-excerpt-section-maps-write-enough-code-to-make-it-pass-e76e129f]] - previous source section: Maps / Write enough code to make it pass
- [[coding-learn-go-with-tests-excerpt-refactor]] - topic hub: opens the topic page for Refactor

## Statements

- I decided to create an assertStrings helper to make the implementation more general. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00565))_

## Technical atoms

### Technical frame 1: Maps / Refactor

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
