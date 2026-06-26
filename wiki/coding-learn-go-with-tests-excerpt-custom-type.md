---
page_id: coding-learn-go-with-tests-excerpt-custom-type
page_kind: concept
summary: Using a custom type: 5 statement(s) and 2 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-custom-type@49a9b81d6cbfc62ff1832ebbcc40b623
---

# Using a custom type

What [[coding-learn-go-with-tests-excerpt]] covers about using a custom type:

## Statements

- Then called Search on the Dictionary instance. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00570))_
- We started using the Dictionary type, which we have not defined yet. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00570))_
- We did not need to change assertStrings . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00571))_
- With the custom type defined, we can create the Search method. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00574))_
- Here we created a Dictionary type which acts as a thin wrapper around map . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00574))_

## Technical atoms

> Context: We can improve our dictionary's usage by creating a new type around map and making Search a method.
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00567))_

```
In dictionary_test.go : func TestSearch(t	*testing.T)	{ dictionary	:=	Dictionary{"test":	"this	is	just	a	test"} got	:=	dictionary.Search("test") want	:=	"this	is	just	a	test"
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00568))_

> Context: We can improve our dictionary's usage by creating a new type around map and making Search a method.
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00567))_

```
assertStrings(t,	got,	want) }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00569))_


## Source

- [[coding-learn-go-with-tests-excerpt]]
