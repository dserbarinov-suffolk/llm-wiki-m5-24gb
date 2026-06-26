---
page_id: coding-learn-go-with-tests-excerpt-section-write-the-test-first-bfabd389
page_kind: source
summary: Write the test first: 3 source-backed entries and 2 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-write-the-test-first-bfabd389@0f3ddaaf64ec82a11b40a3bbfc082cac
---

# Write the test first

From [[coding-learn-go-with-tests-excerpt]].

## Statements

- Update is very closely related to Add and will be our next implementation. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00642))_

## Technical atoms

```
func TestUpdate(t	*testing.T)	{ word	:=	"test" definition	:=	"this	is	just	a	test" dictionary	:=	Dictionary{word:	definition} newDefinition	:=	"new	definition"
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00640))_

```
dictionary.Update(word,	newDefinition) assertDefinition(t,	dictionary,	word,	newDefinition) }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00641))_
