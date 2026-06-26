---
page_id: coding-learn-go-with-tests-excerpt-section-refactor-395f18c6
page_kind: source
summary: Refactor: 4 source-backed entries and 1 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-refactor-395f18c6@b377f01cd2e5602c0791283e57c452f8
---

# Refactor

From [[coding-learn-go-with-tests-excerpt]].

## Statements

- We don't have too much to refactor, but as our error usage grows we can make a few modifications. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00635))_
- We made the errors constant; this required us to create our own DictionaryErr type which implements the error interface. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00637))_
- Simply put, it makes the errors more reusable and immutable. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00637))_

## Technical atoms

```
const ( ErrNotFound			=	DictionaryErr("could	not	find	the	word	you	were looking	for") ErrWordExists	=	DictionaryErr("cannot	add	word	because	it already	exists") ) type DictionaryErr	string func (e	DictionaryErr)	Error()	string	{ return string(e) }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00636))_
