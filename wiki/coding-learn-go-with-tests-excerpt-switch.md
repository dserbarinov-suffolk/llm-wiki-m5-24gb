---
page_id: coding-learn-go-with-tests-excerpt-switch
page_kind: concept
summary: switch: 3 statement(s) and 1 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-switch@2c538bbf4d7f56215300f28940d4cc9b
---

# switch

What [[coding-learn-go-with-tests-excerpt]] covers about switch:

## Statements

- When you have lots of if statements checking a particular value it is common to use a switch statement instead. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00131))_
- We can use switch to refactor the code to make it easier to read and more extensible if we wish to add more language support later _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00131))_
- Write a test to now include a greeting in the language of your choice and you should see how simple it is to extend our amazing function. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00133))_

## Technical atoms

> Context: When you have lots of if statements checking a particular value it is common to use a switch statement instead. We can use switch to refactor the code to make it easier to read and more extensible if we wish to add more language support later
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00131))_

```
func Hello(name	string,	language	string)	string	{ if name	==	""	{ name	=	"World" } prefix	:=	englishHelloPrefix switch language	{ case spanish: prefix	=	spanishHelloPrefix case french: prefix	=	frenchHelloPrefix } return prefix	+	name }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00132))_


## Source

- [[coding-learn-go-with-tests-excerpt]]
