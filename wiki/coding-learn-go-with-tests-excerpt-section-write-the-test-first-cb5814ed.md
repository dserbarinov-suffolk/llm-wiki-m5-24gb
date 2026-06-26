---
page_id: coding-learn-go-with-tests-excerpt-section-write-the-test-first-cb5814ed
page_kind: source
summary: Write the test first: 4 source-backed entries and 2 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-write-the-test-first-cb5814ed@488249d6335cbf0fd8717a6416a87876
---

# Write the test first

From [[coding-learn-go-with-tests-excerpt]].

## Statements

- We added yet another error type for when the word does not exist. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00657))_
- We also modified Update to return an error value. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00657))_

## Technical atoms

```
t.Run("existing	word", func (t	*testing.T)	{ word	:=	"test" definition	:=	"this	is	just	a	test" dictionary	:=	Dictionary{word:	definition} newDefinition	:=	"new	definition" err	:=	dictionary.Update(word,	newDefinition) assertError(t,	err,	nil) assertDefinition(t,	dictionary,	word,	newDefinition) }) t.Run("new	word", func (t	*testing.T)	{ word	:=	"test" definition	:=	"this	is	just	a	test" dictionary	:=	Dictionary{}
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00655))_

```
err	:=	dictionary.Update(word,	definition) assertError(t,	err,	ErrWordDoesNotExist) })
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00656))_
