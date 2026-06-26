---
page_id: coding-learn-go-with-tests-excerpt-library
page_kind: concept
summary: Library: 4 statement(s) and 2 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-library@20a9fc8eff73865249cba818a50502cb
---

# Library

What [[coding-learn-go-with-tests-excerpt]] covers about library:

## Statements

- The vast majority of the standard library has excellent documentation with examples. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00041))_
- Inside here you'll see a list of all of Go's Standard Library packages, plus Third Party packages you have installed, under which you should see your example documentation for github.com/quii/learn-go-with-tests . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00208))_
- The standard library provides the strings.Builder stringsBuilder type which minimizes memory copying. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00257))_
- Investing time learning the standard library will really pay off over time. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00269))_

## Technical atoms

> Context: To view example documentation, let's take a quick look at pkgsite . Before navigating to your project's directory, make sure you have installed pkgsite by running the following command: go install golang.org/x/pkgsite/cmd/pkgsite@latest , then run pkgsite -open . , which should open a web browser for you, pointing to http://localhost:8080 . Inside here you'll see a list of all of Go's Standard Library packages, plus Third Party packages you have installed, under which you should see your example documentation for github.com/quii/learn-go-with-tests . Follow that link, and then look under Integers , then under func Add , then expand Example and you should see the example you added for sum := Add(1, 5) .
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00208))_

> If you publish your code with examples to a public URL, you can share the documentation of your code at pkg.go.dev.
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00209))_

> Context: The standard library provides the strings.Builder stringsBuilder type which minimizes memory copying. It implements a WriteString method which we can use to concatenate strings: Note : We have to call the String method to retrieve the final result.
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00257, source-range-559be4b1-00259))_

```
const repeatCount	=	5 func Repeat(character	string)	string	{ var repeated	strings.Builder for i	:=	0;	i	<	repeatCount;	i++	{ repeated.WriteString(character) } return repeated.String() }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00258))_


## Source

- [[coding-learn-go-with-tests-excerpt]]
