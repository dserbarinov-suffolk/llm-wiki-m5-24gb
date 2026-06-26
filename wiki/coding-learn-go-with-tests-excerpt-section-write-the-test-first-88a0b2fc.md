---
page_id: coding-learn-go-with-tests-excerpt-section-write-the-test-first-88a0b2fc
page_kind: source
summary: Write the test first: 4 source-backed entries and 1 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-write-the-test-first-88a0b2fc@c008cb6d5d58f8a5bc0ff92d16793918
---

# Write the test first

From [[coding-learn-go-with-tests-excerpt]].

## Statements

- We have a great way to search the dictionary. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00596))_
- However, we have no way to add new words to our dictionary. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00596))_
- In this test, we are utilizing our Search function to make the validation of the dictionary a little easier. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00598))_

## Technical atoms

```
func TestAdd(t	*testing.T)	{ dictionary	:=	Dictionary{} dictionary.Add("test",	"this	is	just	a	test") want	:=	"this	is	just	a	test" got,	err	:=	dictionary.Search("test") if err	!=	nil	{ t.Fatal("should	find	added	word:",	err) } assertStrings(t,	got,	want) }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00597))_
