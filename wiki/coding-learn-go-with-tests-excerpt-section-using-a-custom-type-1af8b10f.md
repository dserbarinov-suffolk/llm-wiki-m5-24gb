---
page_id: coding-learn-go-with-tests-excerpt-section-using-a-custom-type-1af8b10f
page_kind: source
summary: Using a custom type: 9 source-backed entries and 3 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-using-a-custom-type-1af8b10f@c65dbd3290de4a6900a86dd590fc51f5
---

# Using a custom type

From [[coding-learn-go-with-tests-excerpt]].

## Statements

- Then called Search on the Dictionary instance. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00570))_
- We started using the Dictionary type, which we have not defined yet. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00570))_
- Then called Search on the Dictionary instance. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00570))_
- We did not need to change assertStrings . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00571))_
- With the custom type defined, we can create the Search method. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00574))_
- Here we created a Dictionary type which acts as a thin wrapper around map . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00574))_

## Technical atoms

```
In dictionary_test.go : func TestSearch(t	*testing.T)	{ dictionary	:=	Dictionary{"test":	"this	is	just	a	test"} got	:=	dictionary.Search("test") want	:=	"this	is	just	a	test"
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00568))_

```
assertStrings(t,	got,	want) }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00569))_

```
type Dictionary map [string]string func (d	Dictionary)	Search(word	string)	string	{ return d[word] }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00573))_
