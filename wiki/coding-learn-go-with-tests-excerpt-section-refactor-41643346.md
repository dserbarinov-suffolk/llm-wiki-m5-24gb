---
page_id: coding-learn-go-with-tests-excerpt-section-refactor-41643346
page_kind: source
summary: Refactor: 2 source-backed entries and 1 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-refactor-41643346@eaff80da161b8db27f83e609c05ca606
---

# Refactor

From [[coding-learn-go-with-tests-excerpt]].

## Statements

- There isn't much to refactor, but we can implement the same logic from Update to handle cases where word doesn't exist. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00689))_

## Technical atoms

```
func TestDelete(t	*testing.T)	{ t.Run("existing	word", func (t	*testing.T)	{ word	:=	"test" dictionary	:=	Dictionary{word:	"test	definition"} err	:=	dictionary.Delete(word) assertError(t,	err,	nil) _,	err	=	dictionary.Search(word) assertError(t,	err,	ErrNotFound) }) t.Run("non-existing	word", func (t	*testing.T)	{ word	:=	"test" dictionary	:=	Dictionary{} err	:=	dictionary.Delete(word) assertError(t,	err,	ErrWordDoesNotExist) }) }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00690))_
