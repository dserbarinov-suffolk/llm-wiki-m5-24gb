---
page_id: coding-learn-go-with-tests-excerpt-code-chapter
page_kind: concept
summary: You can find all the code for this chapter here: 46 statement(s) and 13 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-code-chapter@517072520fb1ff9769793a533ac6d1d0
---

# You can find all the code for this chapter here

What [[coding-learn-go-with-tests-excerpt]] covers about you can find all the code for this chapter here:

## Statements

- of the code you will write. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00033))_
- Refactoring is not just for the production code! _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00082))_
- Once you add this to the code, the tests will pass. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00482))_
- For example, here is the finalised API for this chapter. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00209))_
- Packages are ways of grouping up related Go code together. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00014))_
- Create a test file called adder_test.go and write this code. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00164))_
- There's not a lot in the actual code we can really improve on here. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00191))_
- When the benchmark code is executed, it measures how long it takes. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00248))_
- This is great because it aids the usability of code you are writing. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00193))_
- In future chapters, you will need to run go mod init SOMENAME in each _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00029))_
- But there is repeated code when we check if the message is what we expect. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00081))_
- A handy side-effect of this is this adds a little type-safety to our code. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00392))_
- Normally you have to write code to say My type Foo implements interface Bar . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00484))_
- It is good to separate your "domain" code from the outside world (side-effects). _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00018))_

## Technical atoms

```
output Write	enough	code	to	make	it	pass Refactor Write	the	test	first Try	and	run	the	test Write	minimal	amount	of	code	for	the	test	to	run	and	check	the failing	test	output Write	enough	code	to	make	it	pass Write	the	test	first Try	and	run	the	test Write	the	minimal	amount	of	code	for	the	test	to	run	and	check	the failing	test	output Write	enough	code	to	make	it	pass Note	on	declaring	a	new	error	for	Update Write	the	test	first Try	to	run	the	test Write	the	minimal	amount	of	code	for	the	test	to	run	and	check	the failing	test	output Write	enough	code	to	make	it	pass Refactor Try	to	run	test Write	enough	code	to	make	it	pass Wrapping	up
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00003))_

> When you retrospectively write tests, there is the risk that your test may continue to pass even if the code doesn't work as intended.
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00046))_

> The compiler understands how your code should snap together and work so you don't have to.
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00051))_

```
Constants	are	defined	like	so We	can	now	refactor	our	code const englishHelloPrefix	=	"Hello,	" const englishHelloPrefix	=	"Hello,	" func Hello(name	string)	string	{ return englishHelloPrefix	+	name }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00068))_

> You can comment out the t.Helper() code by adding two forward slashes // at the beginning of the line.
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00088))_

> You should see some problems in the code, "magic" strings, some of which are repeated.
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00120))_


## Source

- [[coding-learn-go-with-tests-excerpt]]
