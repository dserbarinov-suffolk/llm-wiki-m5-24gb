---
page_id: coding-learn-go-with-tests-excerpt-section-pointers-copies-et-al-write-the-test-first-764407b8
page_kind: source
summary: Pointers, copies, et al / Write the test first: 3 source-backed entries and 2 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-29
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-pointers-copies-et-al-write-the-test-first-764407b8@d9734097998bbb918d34607e5781cd5c
---

# Pointers, copies, et al / Write the test first

From [[coding-learn-go-with-tests-excerpt]].

## Related pages

- [[coding-learn-go-with-tests-excerpt-section-pointers-copies-et-al-36483230]] - broader source section: Pointers, copies, et al
- [[coding-learn-go-with-tests-excerpt-section-pointers-copies-et-al-refactor-c066e9e2]] - previous source section: Pointers, copies, et al / Refactor
- [[coding-learn-go-with-tests-excerpt-section-pointers-copies-et-al-try-and-run-the-test-22b48658]] - next source section: Pointers, copies, et al / Try and run the test

## Statements

- Update is very closely related to Add and will be our next implementation. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00642))_

## Technical atoms

### Technical frame 1: Pointers, copies, et al / Write the test first

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00642))_

> Update is very closely related to Add and will be our next implementation.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00640))_

```
func TestUpdate(t *testing.T) {
    word := "test"
    definition := "this is just a test"
    dictionary := Dictionary{word: definition}
    newDefinition := "new definition"
```

### Technical frame 2: Pointers, copies, et al / Write the test first

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00642))_

> Update is very closely related to Add and will be our next implementation.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00641))_

```
dictionary.Update(word, newDefinition)
assertDefinition(t, dictionary, word, newDefinition)
}
```
