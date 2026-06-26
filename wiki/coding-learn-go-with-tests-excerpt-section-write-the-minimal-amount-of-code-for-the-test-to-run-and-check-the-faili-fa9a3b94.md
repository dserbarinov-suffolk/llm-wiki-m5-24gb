---
page_id: coding-learn-go-with-tests-excerpt-section-write-the-minimal-amount-of-code-for-the-test-to-run-and-check-the-faili-fa9a3b94
page_kind: source
summary: Write the minimal amount of code for the test to run and check the failing test output: 3 source-backed entries and 2 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-write-the-minimal-amount-of-code-for-the-test-to-run-and-check-the-faili-fa9a3b94@61287abfb74fd78cbb71e305b88825bd
---

# Write the minimal amount of code for the test to run and check the failing test output

From [[coding-learn-go-with-tests-excerpt]].

## Statements

- We added our own error type and are returning a nil error. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00663))_

## Technical atoms

```
const ( ErrNotFound									=	DictionaryErr("could	not	find	the	word	you were	looking	for") ErrWordExists							=	DictionaryErr("cannot	add	word	because	it already	exists") ErrWordDoesNotExist	=	DictionaryErr("cannot	perform	operation	on word	because	it	does	not	exist") ) func (d	Dictionary)	Update(word,	definition	string)	error	{ d[word]	=	definition return nil }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00662))_

```
dictionary_test.go:66:	got	error	'%!q(<nil>)'	want	'cannot	update word	because	it	does	not	exist'
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00665))_
