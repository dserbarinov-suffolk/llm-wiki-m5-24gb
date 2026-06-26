---
page_id: coding-learn-go-with-tests-excerpt-section-write-enough-code-to-make-it-pass-f6be49d5
page_kind: source
summary: Write enough code to make it pass: 2 source-backed entries and 1 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-write-enough-code-to-make-it-pass-f6be49d5@b8a944b40c8da79db54c4ce1232076b9
---

# Write enough code to make it pass

From [[coding-learn-go-with-tests-excerpt]].

## Statements

- We are again using a switch statement to match on the error when we attempt to delete a word that doesn't exist. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00696))_

## Technical atoms

```
func (d Dictionary) Delete(word string) error {
    _, err := d.Search(word)
switch err {
    case ErrNotFound:
        return ErrWordDoesNotExist
    case nil:
        delete(d, word)
    default:
        return err
    }
return nil
}
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00695))_
