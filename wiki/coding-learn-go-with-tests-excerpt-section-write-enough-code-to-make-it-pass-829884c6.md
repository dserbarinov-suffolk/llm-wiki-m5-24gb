---
page_id: coding-learn-go-with-tests-excerpt-section-write-enough-code-to-make-it-pass-829884c6
page_kind: source
summary: Write enough code to make it pass: 3 source-backed entries and 1 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-write-enough-code-to-make-it-pass-829884c6@13c1eaf81c094664ee4534d07ce9a1e5
---

# Write enough code to make it pass

From [[coding-learn-go-with-tests-excerpt]].

## Statements

- Having a switch like this provides an extra safety net, in case Search returns an error other than ErrNotFound . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00633))_
- Here we are using a switch statement to match on the error. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00633))_

## Technical atoms

```
func (d	Dictionary)	Add(word,	definition	string)	error	{ _,	err	:=	d.Search(word) switch err	{ case ErrNotFound: d[word]	=	definition case nil: return ErrWordExists default : return err } return nil }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00632))_
