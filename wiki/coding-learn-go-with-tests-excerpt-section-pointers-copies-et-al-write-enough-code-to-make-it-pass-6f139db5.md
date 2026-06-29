---
page_id: coding-learn-go-with-tests-excerpt-section-pointers-copies-et-al-write-enough-code-to-make-it-pass-6f139db5
page_kind: source
summary: Pointers, copies, et al / Write enough code to make it pass: 3 source-backed entries and 1 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-29
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-pointers-copies-et-al-write-enough-code-to-make-it-pass-6f139db5@054c2f3222bd7e6d05ea28e1391a2d6d
---

# Pointers, copies, et al / Write enough code to make it pass

From [[coding-learn-go-with-tests-excerpt]].

## Related pages

- [[coding-learn-go-with-tests-excerpt-section-pointers-copies-et-al-36483230]] - broader source section: Pointers, copies, et al
- [[coding-learn-go-with-tests-excerpt-section-pointers-copies-et-al-write-the-minimal-amount-of-code-for-the-test-to-run-and-check-the-output-7f59b214]] - previous source section: Pointers, copies, et al / Write the minimal amount of code for the test to run and check the output
- [[coding-learn-go-with-tests-excerpt-section-pointers-copies-et-al-refactor-c066e9e2]] - next source section: Pointers, copies, et al / Refactor

## Statements

- Here we are using a switch statement to match on the error. Having a switch like this provides an extra safety net, in case Search returns an error other than ErrNotFound . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00633))_

## Technical atoms

### Technical frame 1: Pointers, copies, et al / Write enough code to make it pass

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00633))_

> Here we are using a switch statement to match on the error. Having a switch like this provides an extra safety net, in case Search returns an error other than ErrNotFound .

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00632))_

```
func (d Dictionary) Add(word, definition string) error {
    _, err := d.Search(word)
switch err {
    case ErrNotFound:
        d[word] = definition
    case nil:
        return ErrWordExists
    default:
        return err
    }
return nil
}
```
