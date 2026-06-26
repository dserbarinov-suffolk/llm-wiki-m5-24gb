---
page_id: coding-learn-go-with-tests-excerpt-testing
page_kind: concept
summary: Back to Testing: 9 statement(s) and 40 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-testing@6413769d61b6d46d1c60710385c34e42
---

# Back to Testing

What [[coding-learn-go-with-tests-excerpt]] covers about back to testing:

## Statements

- The testing.B gives you access to the loop function. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00247))_
- Here, we are introducing another tool in our testing arsenal: subtests. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00075))_
- We need to pass in t *testing.T so that we can tell the test code to fail when we need to. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00086))_
- We can get back to testing and learning Go now since the tests should run, even on Go 1.16. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00029))_
- When we call t.Errorf we are calling the method Errorf on the instance of our t ( testing.T ). _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00448))_
- This is basic testdriven development and allows us to make sure our test is actually testing what we want. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00046))_
- Notice how you have not had to pick between multiple testing frameworks and then figure out how to install them. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00032))_
- Once we're more familiar with Go's syntax I will introduce a technique called "Property Based Testing" , which would stop annoying developers and help you find bugs. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00186))_
- They are a great fit when you wish to test various implementations of an interface, or if the data being passed in to a function has lots of different requirements that need testing. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00501))_

## Technical atoms

```
package main import "testing" func TestHello(t	*testing.T)	{ got	:=	Hello() want	:=	"Hello,	world" if got	!=	want	{ t.Errorf("got	%q	want	%q",	got,	want) } }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00023))_

```
import "testing" func TestHello(t	*testing.T)	{ got	:=	Hello("Chris") want	:=	"Hello,	Chris" if got	!=	want	{ t.Errorf("got	%q	want	%q",	got,	want) } }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00048))_

```
func TestHello(t	*testing.T)	{ t.Run("saying	hello	to	people", func (t	*testing.T)	{ got	:=	Hello("Chris") want	:=	"Hello,	Chris" if got	!=	want	{ t.Errorf("got	%q	want	%q",	got,	want) } }) t.Run("say	'Hello,	World'	when	an	empty	string	is	supplied", func (t	*testing.T)	{ got	:=	Hello("") want	:=	"Hello,	World" if got	!=	want	{ t.Errorf("got	%q	want	%q",	got,	want) } }) }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00074))_

```
func TestHello(t	*testing.T)	{ t.Run("saying	hello	to	people", func (t	*testing.T)	{ got	:=	Hello("Chris") want	:=	"Hello,	Chris" assertCorrectMessage(t,	got,	want) }) t.Run("empty	string	defaults	to	'world'", func (t	*testing.T)	{ got	:=	Hello("") want	:=	"Hello,	World" assertCorrectMessage(t,	got,	want) }) } func assertCorrectMessage(t	testing.TB,	got,	want	string)	{ t.Helper() if got	!=	want	{ t.Errorf("got	%q	want	%q",	got,	want) } }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00084))_

```
t.Run("in	Spanish", func (t	*testing.T)	{ got	:=	Hello("Elodie",	"Spanish") want	:=	"Hola,	Elodie" assertCorrectMessage(t,	got,	want) })
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00108))_

```
package integers import "testing" func TestAdder(t	*testing.T)	{ sum	:=	Add(2,	2) expected	:=	4 if sum	!=	expected	{ t.Errorf("expected	'%d'	but	got	'%d'",	expected,	sum) } }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00169))_


## Source

- [[coding-learn-go-with-tests-excerpt]]
