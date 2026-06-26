---
page_id: coding-learn-go-with-tests-excerpt-note
page_kind: concept
summary: Note: 5 statement(s) and 2 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-note@ee24900be557787c8320bb76d0cb675c
---

# Note

What [[coding-learn-go-with-tests-excerpt]] covers about note:

## Statements

- Note: Go source files can only have one package per directory. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00165))_
- Also note that we are no longer using the main package, instead we've defined a package named integers , as the name suggests this will group functions for working with integers such as Add . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00171))_
- Note : We have to call the String method to retrieve the final result. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00259))_
- Note that this function expects the elements to be comparable. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00348))_
- It's important to note that while the test has compiled , it has a runtime error . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00382))_

## Technical atoms

> Context: The standard library provides the strings.Builder stringsBuilder type which minimizes memory copying. It implements a WriteString method which we can use to concatenate strings: Note : We have to call the String method to retrieve the final result.
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00257, source-range-559be4b1-00259))_

```
const repeatCount	=	5 func Repeat(character	string)	string	{ var repeated	strings.Builder for i	:=	0;	i	<	repeatCount;	i++	{ repeated.WriteString(character) } return repeated.String() }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00258))_

> Context: From Go 1.21, slices standard package is available, which has slices.Equal function to do a simple shallow compare on slices, where you don't need to worry about the types like the above case. Note that this function expects the elements to be comparable. So, it can't be applied to slices with non-comparable elements like 2D slices.
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00348))_

```
./sum_test.go:26:9:	invalid	operation:	got	!=	want	(slice	can	only be	compared	to	nil)
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00346))_


## Source

- [[coding-learn-go-with-tests-excerpt]]
