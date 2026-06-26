---
page_id: coding-learn-go-with-tests-excerpt-section-write-enough-code-to-make-it-pass-05e7757f
page_kind: source
summary: Write enough code to make it pass: 3 source-backed entries and 3 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-write-enough-code-to-make-it-pass-05e7757f@c601f8b25c119a3fa732beca33e39949
---

# Write enough code to make it pass

From [[coding-learn-go-with-tests-excerpt]].

## Technical atoms

```
func (d	Dictionary)	Update(word,	definition	string)	error	{ _,	err	:=	d.Search(word) switch err	{ case ErrNotFound: return ErrWordDoesNotExist case nil: d[word]	=	definition default : return err } return nil
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00667))_

```
}
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00668))_

> This function looks almost identical to Add except we switched when we update the dictionary and when we return an error.
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00669))_
