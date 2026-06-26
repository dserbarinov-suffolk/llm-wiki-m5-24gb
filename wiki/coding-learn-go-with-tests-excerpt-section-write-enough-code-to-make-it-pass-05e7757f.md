---
page_id: coding-learn-go-with-tests-excerpt-section-write-enough-code-to-make-it-pass-05e7757f
page_kind: source
summary: Write enough code to make it pass: 4 source-backed entries and 2 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-write-enough-code-to-make-it-pass-05e7757f@1fffea84e880825a6233ce3a27163290
---

# Write enough code to make it pass

From [[coding-learn-go-with-tests-excerpt]].

## Statements

- This function looks almost identical to Add except we switched when we update the dictionary and when we return an error. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00669))_
- This function looks almost identical to Add except we switched when we update the dictionary and when we return an error. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00669))_

## Technical atoms

```
func (d	Dictionary)	Update(word,	definition	string)	error	{ _,	err	:=	d.Search(word) switch err	{ case ErrNotFound: return ErrWordDoesNotExist case nil: d[word]	=	definition default : return err } return nil
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00667))_

```
}
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00668))_
