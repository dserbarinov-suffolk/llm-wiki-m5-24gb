---
page_id: coding-learn-go-with-tests-excerpt-section-write-the-test-first-6f5fa1cb
page_kind: source
summary: Write the test first: 13 source-backed entries and 2 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-write-the-test-first-6f5fa1cb@61a96626559451cd99258639f6f095d0
---

# Write the test first

From [[coding-learn-go-with-tests-excerpt]].

## Statements

- The second is the value type, which goes right after the [] . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00552))_
- The first is the key type, which is written inside the [] . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00552))_
- The first is the key type, which is written inside the [] . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00552))_
- The second is the value type, which goes right after the [] . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00552))_
- It can only be a comparable type because without the ability to tell if 2 keys are equal, we have no way to ensure that we are getting the correct value. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00553))_
- Comparable types are explained in depth in the language spec. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00553))_
- The key type is special. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00553))_
- It can only be a comparable type because without the ability to tell if 2 keys are equal, we have no way to ensure that we are getting the correct value. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00553))_
- The value type, on the other hand, can be any type you want. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00554))_
- It can even be another map. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00554))_
- Everything else in this test should be familiar. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00555))_

## Technical atoms

```
In dictionary_test.go package main import "testing" func TestSearch(t	*testing.T)	{ dictionary	:= map [string]string{"test":	"this	is	just	a	test"} got	:=	Search(dictionary,	"test") want	:=	"this	is	just	a	test" if got	!=	want	{ t.Errorf("got	%q	want	%q	given,	%q",	got,	want,	"test") } }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00551))_

> Except, it starts with the map keyword and requires two types.
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00552))_
