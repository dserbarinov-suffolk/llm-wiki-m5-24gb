---
page_id: coding-learn-go-with-tests-excerpt-section-write-the-test-first-9c23f988
page_kind: source
summary: Write the test first: 3 source-backed entries and 1 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-write-the-test-first-9c23f988@1c5d24bc44116bc5c3251d7145016ec5
---

# Write the test first

From [[coding-learn-go-with-tests-excerpt]].

## Statements

- We also modified the previous test to check for a nil error. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00623))_
- For this test, we modified Add to return an error, which we are validating against a new error variable, ErrWordExists . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00623))_

## Technical atoms

```
func TestAdd(t	*testing.T)	{ t.Run("new	word", func (t	*testing.T)	{ dictionary	:=	Dictionary{} word	:=	"test" definition	:=	"this	is	just	a	test" err	:=	dictionary.Add(word,	definition) assertError(t,	err,	nil) assertDefinition(t,	dictionary,	word,	definition) }) t.Run("existing	word", func (t	*testing.T)	{ word	:=	"test" definition	:=	"this	is	just	a	test" dictionary	:=	Dictionary{word:	definition} err	:=	dictionary.Add(word,	"new	test") assertError(t,	err,	ErrWordExists) assertDefinition(t,	dictionary,	word,	definition) }) }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00622))_
