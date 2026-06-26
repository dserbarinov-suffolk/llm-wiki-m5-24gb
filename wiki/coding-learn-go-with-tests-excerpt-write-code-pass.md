---
page_id: coding-learn-go-with-tests-excerpt-write-code-pass
page_kind: concept
summary: Write enough code to make it pass: 68 statement(s) and 27 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-write-code-pass@1aec8f6849cc4976789f713e0589236d
---

# Write enough code to make it pass

What [[coding-learn-go-with-tests-excerpt]] covers about write enough code to make it pass:

## Statements

- of the code you will write. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00033))_
- Refactoring is not just for the production code! _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00082))_
- Once you add this to the code, the tests will pass. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00482))_
- Packages are ways of grouping up related Go code together. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00014))_
- Create a test file called adder_test.go and write this code. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00164))_
- Our next requirement is to write an Area function for circles. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00435))_
- If we pass in a new word, Update will add it to the dictionary. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00653))_
- There's not a lot in the actual code we can really improve on here. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00191))_
- When the benchmark code is executed, it measures how long it takes. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00248))_
- This is great because it aids the usability of code you are writing. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00193))_
- Now that the tests are passing, we can and should refactor our tests. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00083))_
- If the tests pass, then you are probably using an earlier version of Go. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00025))_
- But there is repeated code when we check if the message is what we expect. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00081))_
- A handy side-effect of this is this adds a little type-safety to our code. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00392))_

## Technical atoms

```
output Write	enough	code	to	make	it	pass Refactor Write	the	test	first Try	and	run	the	test Write	minimal	amount	of	code	for	the	test	to	run	and	check	the failing	test	output Write	enough	code	to	make	it	pass Write	the	test	first Try	and	run	the	test Write	the	minimal	amount	of	code	for	the	test	to	run	and	check	the failing	test	output Write	enough	code	to	make	it	pass Note	on	declaring	a	new	error	for	Update Write	the	test	first Try	to	run	the	test Write	the	minimal	amount	of	code	for	the	test	to	run	and	check	the failing	test	output Write	enough	code	to	make	it	pass Refactor Try	to	run	test Write	enough	code	to	make	it	pass Wrapping	up
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00003))_

> It should've passed!
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00032))_

> When you retrospectively write tests, there is the risk that your test may continue to pass even if the code doesn't work as intended.
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00046))_

> The compiler understands how your code should snap together and work so you don't have to.
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00051))_

> When you run the tests, they should now pass.
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00062))_

```
Constants	are	defined	like	so We	can	now	refactor	our	code const englishHelloPrefix	=	"Hello,	" const englishHelloPrefix	=	"Hello,	" func Hello(name	string)	string	{ return englishHelloPrefix	+	name }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00068))_


## Source

- [[coding-learn-go-with-tests-excerpt]]
