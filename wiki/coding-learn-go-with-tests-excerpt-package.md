---
page_id: coding-learn-go-with-tests-excerpt-package
page_kind: concept
summary: Package: 17 statement(s) and 13 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-package@de66bde571c0785b1f66ac3dd94888de
---

# Package

What [[coding-learn-go-with-tests-excerpt]] covers about package:

## Statements

- Have a look through the strings package. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00269))_
- Packages are ways of grouping up related Go code together. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00014))_
- Note: Go source files can only have one package per directory. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00165))_
- You can have functions with the same name declared in different packages . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00445))_
- So we could create our Area(Circle) in a new package, but that feels overkill here. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00445))_
- When you write a program in Go, you will have a main package defined with a main func inside it. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00014))_
- With import "fmt" we are importing a package which contains the Println function that we use to print. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00016))_
- This web interface allows you to search for documentation of standard library packages and third-party packages. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00209))_
- Go's second tool for viewing documentation is the pkgsite command, which powers Go's official package viewing website. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00040))_
- Running the package's test suite, we can see the example ExampleAdd function is executed with no further arrangement from us: _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00204))_
- Go has a built-in tool, doc, which lets you examine any package installed on your system, or the module you're currently working on. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00038))_
- (If your editor doesn't automatically import packages for you, the compilation step will fail because you will be missing import "fmt" in adder_test.go . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00202))_
- We just saw the documentation for the fmt package at the official package viewing website, and Go also provides ways for quickly getting at the documentation offline. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00037))_
- Also note that we are no longer using the main package, instead we've defined a package named integers , as the name suggests this will group functions for working with integers such as Add . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00171))_

## Technical atoms

```
package main import "fmt" func main()	{ fmt.Println("Hello,	world") }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00011))_

```
package main import "fmt" func Hello()	string	{ return "Hello,	world" } func main()	{ fmt.Println(Hello()) }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00020))_

```
package main import "testing" func TestHello(t	*testing.T)	{ got	:=	Hello() want	:=	"Hello,	world" if got	!=	want	{ t.Errorf("got	%q	want	%q",	got,	want) } }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00023))_

```
$	go	doc	fmt package	fmt	//	import	"fmt" Package	fmt	implements	formatted	I/O	with	functions	analogous	to	C's printf	and scanf.	The	format	'verbs'	are	derived	from	C's	but	are	simpler. #	Printing The	verbs: General: %v		the	value	in	a	default	format when	printing	structs,	the	plus	flag	(%+v)	adds	field	names %#v	a	Go-syntax	representation	of	the	value %T		a	Go-syntax	representation	of	the	type	of	the	value %%		a	literal	percent	sign;	consumes	no	value ...
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00039))_

```
package integers import "testing" func TestAdder(t	*testing.T)	{ sum	:=	Add(2,	2) expected	:=	4 if sum	!=	expected	{ t.Errorf("expected	'%d'	but	got	'%d'",	expected,	sum) } }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00169))_

```
package integers func Add(x,	y	int)	int	{ return 0 }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00176))_


## Source

- [[coding-learn-go-with-tests-excerpt]]
