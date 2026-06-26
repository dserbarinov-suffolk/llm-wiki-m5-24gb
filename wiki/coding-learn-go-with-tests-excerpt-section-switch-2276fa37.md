---
page_id: coding-learn-go-with-tests-excerpt-section-switch-2276fa37
page_kind: source
summary: switch: 4 source-backed entries and 2 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-switch-2276fa37@839fa881dee93f26fbb0cb0a78f8fcab
---

# switch

From [[coding-learn-go-with-tests-excerpt]].

## Statements

- When you have lots of if statements checking a particular value it is common to use a switch statement instead. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00131))_
- We can use switch to refactor the code to make it easier to read and more extensible if we wish to add more language support later _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00131))_

## Technical atoms

```
func Hello(name	string,	language	string)	string	{ if name	==	""	{ name	=	"World" } prefix	:=	englishHelloPrefix switch language	{ case spanish: prefix	=	spanishHelloPrefix case french: prefix	=	frenchHelloPrefix } return prefix	+	name }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00132))_

> Write a test to now include a greeting in the language of your choice and you should see how simple it is to extend our amazing function.
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00133))_
