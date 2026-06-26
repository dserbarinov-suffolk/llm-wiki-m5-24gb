---
page_id: coding-learn-go-with-tests-excerpt-section-how-to-test-2bf146e5
page_kind: source
summary: How to test: 7 source-backed entries and 2 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-how-to-test-2bf146e5@08d6fe5287210abb2926255580308046
---

# How to test

From [[coding-learn-go-with-tests-excerpt]].

## Statements

- It is good to separate your "domain" code from the outside world (side-effects). _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00018))_
- The fmt.Println is a side effect (printing to stdout), and the string we send in is our domain. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00018))_
- We have created a new function with func , but this time, we've added another keyword, string, to the definition. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00021))_
- This means this function returns a string . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00021))_
- This means this function returns a string . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00021))_

## Technical atoms

```
package main import "fmt" func Hello()	string	{ return "Hello,	world" } func main()	{ fmt.Println(Hello()) }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00020))_

```
package main import "testing" func TestHello(t	*testing.T)	{ got	:=	Hello() want	:=	"Hello,	world" if got	!=	want	{ t.Errorf("got	%q	want	%q",	got,	want) } }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00023))_
