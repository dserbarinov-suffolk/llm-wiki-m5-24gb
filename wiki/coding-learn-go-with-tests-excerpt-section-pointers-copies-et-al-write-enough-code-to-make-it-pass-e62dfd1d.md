---
page_id: coding-learn-go-with-tests-excerpt-section-pointers-copies-et-al-write-enough-code-to-make-it-pass-e62dfd1d
page_kind: source
summary: Pointers, copies, et al / Write enough code to make it pass: 4 source-backed entries and 2 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-29
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-pointers-copies-et-al-write-enough-code-to-make-it-pass-e62dfd1d@f1b723b9ca07e8bfc9ef153208d0f498
---

# Pointers, copies, et al / Write enough code to make it pass

From [[coding-learn-go-with-tests-excerpt]].

## Related pages

- [[coding-learn-go-with-tests-excerpt-section-pointers-copies-et-al-36483230]] - broader source section: Pointers, copies, et al
- [[coding-learn-go-with-tests-excerpt-section-pointers-copies-et-al-write-the-minimal-amount-of-code-for-the-test-to-run-and-check-the-failing-80732c5f]] - previous source section: Pointers, copies, et al / Write the minimal amount of code for the test to run and check the failing test output

## Statements

- This function looks almost identical to Add except we switched when we update the dictionary and when we return an error. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00669))_
- This function looks almost identical to Add except we switched when we update the dictionary and when we return an error. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00669))_

## Technical atoms

### Technical frame 1: Pointers, copies, et al / Write enough code to make it pass

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00669))_

> This function looks almost identical to Add except we switched when we update the dictionary and when we return an error.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00667))_

```
func (d Dictionary) Update(word, definition string) error {
    _, err := d.Search(word)
switch err {
    case ErrNotFound:
        return ErrWordDoesNotExist
    case nil:
        d[word] = definition
    default:
        return err
    }
return nil
```

### Technical frame 2: Pointers, copies, et al / Write enough code to make it pass

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00669))_

> This function looks almost identical to Add except we switched when we update the dictionary and when we return an error.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00668))_

```
}
```
