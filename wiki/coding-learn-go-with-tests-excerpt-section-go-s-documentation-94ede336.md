---
page_id: coding-learn-go-with-tests-excerpt-section-go-s-documentation-94ede336
page_kind: source
summary: Go's documentation: 10 source-backed entries and 1 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-go-s-documentation-94ede336@edc2c6174486260fa7a418e842fba46c
---

# Go's documentation

From [[coding-learn-go-with-tests-excerpt]].

## Statements

- Another quality-of-life feature of Go is the documentation. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00037))_
- We just saw the documentation for the fmt package at the official package viewing website, and Go also provides ways for quickly getting at the documentation offline. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00037))_
- Go has a built-in tool, doc, which lets you examine any package installed on your system, or the module you're currently working on. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00038))_
- Go's second tool for viewing documentation is the pkgsite command, which powers Go's official package viewing website. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00040))_
- For a default installation of Go, that executable will be in $HOME/go/bin for Linux and macOS, and %USERPROFILE%\go\bin for Windows. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00040))_
- If you have not already added those paths to your $PATH var, you might want to do so to make running go-installed commands easier. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00040))_
- You can install pkgsite with go install golang.org/x/pkgsite/cmd/pkgsite@latest , then run it with pkgsite -open . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00040))_
- You can install pkgsite with go install golang.org/x/pkgsite/cmd/pkgsite@latest , then run it with pkgsite -open . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00040))_
- The vast majority of the standard library has excellent documentation with examples. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00041))_

## Technical atoms

```
$	go	doc	fmt package	fmt	//	import	"fmt" Package	fmt	implements	formatted	I/O	with	functions	analogous	to	C's printf	and scanf.	The	format	'verbs'	are	derived	from	C's	but	are	simpler. #	Printing The	verbs: General: %v		the	value	in	a	default	format when	printing	structs,	the	plus	flag	(%+v)	adds	field	names %#v	a	Go-syntax	representation	of	the	value %T		a	Go-syntax	representation	of	the	type	of	the	value %%		a	literal	percent	sign;	consumes	no	value ...
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00039))_
