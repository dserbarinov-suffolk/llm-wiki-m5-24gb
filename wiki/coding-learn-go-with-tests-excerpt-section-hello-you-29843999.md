---
page_id: coding-learn-go-with-tests-excerpt-section-hello-you-29843999
page_kind: source
summary: Hello, YOU: 22 source-backed entries and 10 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-hello-you-29843999@1b323ad55849ba75852451cc98cda305
---

# Hello, YOU

From [[coding-learn-go-with-tests-excerpt]].

## Statements

- Now that we have a test, we can iterate on our software safely. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00043))_
- In the last example, we wrote the test after the code had been written so that you could get an example of how to write a test and declare a function. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00044))_
- In the last example, we wrote the test after the code had been written so that you could get an example of how to write a test and declare a function. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00044))_
- This is basic testdriven development and allows us to make sure our test is actually testing what we want. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00046))_
- When using a statically typed language like Go it is important to listen to the compiler . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00051))_
- In this case the compiler is telling you what you need to do to continue. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00052))_
- We have to change our function Hello to accept an argument. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00052))_
- If you try and run your tests again your hello.go will fail to compile because you're not passing an argument. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00055))_
- Send in "world" to make it compile. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00055))_
- If you try and run your tests again your hello.go will fail to compile because you're not passing an argument. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00055))_
- We finally have a compiling program but it is not meeting our requirements according to the test. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00059))_
- Normally, as part of the TDD cycle, we should now refactor . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00062))_

## Technical atoms

> When you retrospectively write tests, there is the risk that your test may continue to pass even if the code doesn't work as intended.
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00046))_

```
import "testing" func TestHello(t	*testing.T)	{ got	:=	Hello("Chris") want	:=	"Hello,	Chris" if got	!=	want	{ t.Errorf("got	%q	want	%q",	got,	want) } }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00048))_

```
./hello_test.go:6:18:	too	many	arguments	in	call	to	Hello have	(string) want	()
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00050))_

> The compiler understands how your code should snap together and work so you don't have to.
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00051))_

```
func Hello(name	string)	string	{ return "Hello,	world" }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00054))_

```
func main()	{ fmt.Println(Hello("world")) }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00056))_

> Now when you run your tests, you should see something like
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00057))_

```
hello_test.go:10:	got	'Hello,	world'	want	'Hello,	Chris''
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00058))_

```
func Hello(name	string)	string	{ return "Hello,	"	+	name }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00061))_

> When you run the tests, they should now pass.
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00062))_
