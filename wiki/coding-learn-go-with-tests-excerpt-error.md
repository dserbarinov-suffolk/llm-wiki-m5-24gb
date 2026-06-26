---
page_id: coding-learn-go-with-tests-excerpt-error
page_kind: concept
summary: Error: 7 statement(s) and 3 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-error@3058b39e10d22cba5d21e716446f535a
---

# Error

What [[coding-learn-go-with-tests-excerpt]] covers about error:

## Statements

- Once the above error is fixed, if you run go test the compiler will fail with the familiar ./sum_test.go:10:15: undefined: Sum error. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00290))_
- Compile time errors are our friend because they help us write software that works, runtime errors are our enemies because they affect our users. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00383))_
- When we call t.Errorf we are calling the method Errorf on the instance of our t ( testing.T ). _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00448))_
- Notice that as we've seen in the pointers and error section here in order to assert the error message we first check that the error is not nil and then use .Error() method to get the string which we can then pass to the assertion. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00580))_
- We made the errors constant; this required us to create our own DictionaryErr type which implements the error interface. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00637))_
- Having specific errors gives you more information about what went wrong. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00672))_
- dictionary_test.go:78: got error '%!q(<nil>)' want 'could not find the word you were looking for' _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00683))_

## Technical atoms

> Context: Compile time errors are our friend because they help us write software that works, runtime errors are our enemies because they affect our users.
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00383))_

```
panic:	runtime	error:	slice	bounds	out	of	range	[recovered] panic:	runtime	error:	slice	bounds	out	of	range
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00381))_

> Context: We don't have too much to refactor, but as our error usage grows we can make a few modifications.
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00635))_

```
const ( ErrNotFound			=	DictionaryErr("could	not	find	the	word	you	were looking	for") ErrWordExists	=	DictionaryErr("cannot	add	word	because	it already	exists") ) type DictionaryErr	string func (e	DictionaryErr)	Error()	string	{ return string(e) }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00636))_

> Context: Having specific errors gives you more information about what went wrong. Here is an example in a web app:
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00672))_

> You can redirect the user when ErrNotFound is encountered, but display an error message when ErrWordDoesNotExist is encountered.
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00673))_


## Source

- [[coding-learn-go-with-tests-excerpt]]
