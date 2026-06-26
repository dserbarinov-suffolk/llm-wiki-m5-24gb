---
page_id: coding-learn-go-with-tests-excerpt-error
page_kind: concept
summary: Error: 31 statement(s) and 50 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-error@eda53f6ec2d691f9d2f2fda99d0aaff3
---

# Error

What [[coding-learn-go-with-tests-excerpt]] covers about error:

## Statements

- dictionary_test.go:22: expected to get an error. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00586))_
- We also modified Update to return an error value. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00657))_
- We could reuse ErrNotFound and not add a new error. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00671))_
- Map will not throw an error if the value already exists. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00620))_
- We can change our error message into %#v got %g want %g . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00528))_
- We added our own error type and are returning a nil error. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00663))_
- Here we are using a switch statement to match on the error. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00633))_
- We also modified the previous test to check for a nil error. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00623))_
- We are still modifying the value, and returning a nil error. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00629))_
- Simply put, it makes the errors more reusable and immutable. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00637))_
- We added yet another error type for when the word does not exist. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00657))_
- Having specific errors gives you more information about what went wrong. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00672))_
- However, it is often better to have a precise error for when an update fails. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00671))_
- It's important to note that while the test has compiled , it has a runtime error . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00382))_

## Technical atoms

```
output Write	enough	code	to	make	it	pass Refactor Write	the	test	first Try	and	run	the	test Write	minimal	amount	of	code	for	the	test	to	run	and	check	the failing	test	output Write	enough	code	to	make	it	pass Write	the	test	first Try	and	run	the	test Write	the	minimal	amount	of	code	for	the	test	to	run	and	check	the failing	test	output Write	enough	code	to	make	it	pass Note	on	declaring	a	new	error	for	Update Write	the	test	first Try	to	run	the	test Write	the	minimal	amount	of	code	for	the	test	to	run	and	check	the failing	test	output Write	enough	code	to	make	it	pass Refactor Try	to	run	test Write	enough	code	to	make	it	pass Wrapping	up
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00003))_

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
package integers import "testing" func TestAdder(t	*testing.T)	{ sum	:=	Add(2,	2) expected	:=	4 if sum	!=	expected	{ t.Errorf("expected	'%d'	but	got	'%d'",	expected,	sum) } }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00169))_


## Source

- [[coding-learn-go-with-tests-excerpt]]
