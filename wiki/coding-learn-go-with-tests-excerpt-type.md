---
page_id: coding-learn-go-with-tests-excerpt-type
page_kind: concept
summary: Type: 8 statement(s) and 3 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-type@4bbba4401315e8600356589d3768a398
---

# Type

What [[coding-learn-go-with-tests-excerpt]] covers about type:

## Statements

- The value type, on the other hand, can be any type you want. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00554))_
- This depends on the type, for example int s are 0 and for string s it is "" . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00142))_
- We're creating a new type just like we did with Rectangle and Circle but this time it is an interface rather than a struct . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00481))_
- If the type you pass in matches what the interface is asking for, it will compile. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00490))_
- Declaring structs to create your own data types which lets you bundle related data together and make the intent of your code clearer _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00538))_
- Comparable types are explained in depth in the language spec. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00553))_
- The key type is special. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00553))_
- With the custom type defined, we can create the Search method. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00574))_

## Technical atoms

> Context: The key type is special. It can only be a comparable type because without the ability to tell if 2 keys are equal, we have no way to ensure that we are getting the correct value. Comparable types are explained in depth in the language spec.
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00553))_

```
In dictionary_test.go package main import "testing" func TestSearch(t	*testing.T)	{ dictionary	:= map [string]string{"test":	"this	is	just	a	test"} got	:=	Search(dictionary,	"test") want	:=	"this	is	just	a	test" if got	!=	want	{ t.Errorf("got	%q	want	%q	given,	%q",	got,	want,	"test") } }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00551))_

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
