---
page_id: coding-learn-go-with-tests-excerpt-hello
page_kind: concept
summary: Hello, World: 6 statement(s) and 27 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-hello@999bd05c1fa9a270142a610da98f559e
---

# Hello, World

What [[coding-learn-go-with-tests-excerpt]] covers about hello, world:

## Statements

- We have to change our function Hello to accept an argument. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00052))_
- It is traditional for your first program in a new language to be Hello, World. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00008))_
- If you try and run your tests again your hello.go will fail to compile because you're not passing an argument. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00055))_
- The next requirement is when our function is called with an empty string it defaults to printing "Hello, World", rather than "Hello, ". _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00072))_
- When you try and run the test again it will complain about not passing through enough arguments to Hello in your other tests and in hello.go _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00113))_
- For compatibility with tools we'll start using soon, make sure your module's name has a dot somewhere in it, like the dot in .com of example.com/hello. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00029))_

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
module	example.com/hello go	1.16
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00028))_

> The name of the module, example.com/hello, usually refers to a URL where the module can be found and downloaded.
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00029))_

```
import "testing" func TestHello(t	*testing.T)	{ got	:=	Hello("Chris") want	:=	"Hello,	Chris" if got	!=	want	{ t.Errorf("got	%q	want	%q",	got,	want) } }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00048))_


## Source

- [[coding-learn-go-with-tests-excerpt]]
