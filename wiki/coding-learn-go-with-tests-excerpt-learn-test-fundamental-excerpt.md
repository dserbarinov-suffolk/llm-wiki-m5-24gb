---
page_id: coding-learn-go-with-tests-excerpt-learn-test-fundamental-excerpt
page_kind: concept
summary: Learn Go with Tests -- Go Fundamentals (Excerpt): 103 statement(s) and 77 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-learn-test-fundamental-excerpt@73dae3755b1279bae8e22312a26204dd
---

# Learn Go with Tests -- Go Fundamentals (Excerpt)

What [[coding-learn-go-with-tests-excerpt]] covers about learn go with tests -- go fundamentals (excerpt):

## Statements

- Every test has a cost . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00327))_
- The next step is to run the tests. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00025))_
- There is some duplication in our tests. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00470))_
- To run the benchmarks do go test -bench=. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00250))_
- Everything else in this test should be familiar. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00555))_
- This is valid, but our tests still won't compile! _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00345))_
- Adding a new test for our new shape is very easy. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00504))_
- Once you add this to the code, the tests will pass. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00482))_
- The testing.B gives you access to the loop function. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00247))_
- It is important to question the value of your tests. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00327))_
- We need to define SumAll according to what our test wants. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00342))_
- Example functions are compiled whenever tests are executed. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00199))_
- Create a test file called adder_test.go and write this code. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00164))_
- We also modified the previous test to check for a nil error. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00623))_

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
$	go	test go:	cannot	find	main	module;	see	'go	help	modules'
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00026))_

> When you retrospectively write tests, there is the risk that your test may continue to pass even if the code doesn't work as intended.
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00046))_

```
import "testing" func TestHello(t	*testing.T)	{ got	:=	Hello("Chris") want	:=	"Hello,	Chris" if got	!=	want	{ t.Errorf("got	%q	want	%q",	got,	want) } }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00048))_

> Now when you run your tests, you should see something like
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00057))_


## Source

- [[coding-learn-go-with-tests-excerpt]]
