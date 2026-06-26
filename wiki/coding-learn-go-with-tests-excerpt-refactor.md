---
page_id: coding-learn-go-with-tests-excerpt-refactor
page_kind: concept
summary: one...last...refactor?: 17 statement(s) and 4 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-refactor@272a2d4a132258752cbbaeacd5826f75
---

# one...last...refactor?

What [[coding-learn-go-with-tests-excerpt]] covers about one...last...refactor?:

## Statements

- Now it is time to refactor . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00120))_
- Refactoring is not just for the production code! _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00082))_
- We've refactored our assertion into a new function. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00086))_
- Normally, as part of the TDD cycle, we should now refactor . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00062))_
- Now that the tests are passing, we can and should refactor our tests. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00083))_
- There is no refactoring we need to do on this since it was a simple change. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00653))_
- After refactoring, re-run your tests to make sure you haven't broken anything. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00069))_
- There's not a lot to refactor here, but we can introduce another language feature, constants . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00066))_
- The simplest refactor for this would be to extract out some functionality into another function. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00135))_
- We don't have too much to refactor, but as our error usage grows we can make a few modifications. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00635))_
- There isn't much to refactor in our implementation but the test could use a little simplification. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00616))_
- Remember that we must not neglect our test code in the refactoring stage - we can further improve our Sum tests. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00325))_
- Then refactor, backed with the safety of our tests to ensure we have well-crafted code that is easy to work with _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00159))_
- There isn't much to refactor, but we can implement the same logic from Update to handle cases where word doesn't exist. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00689))_

## Technical atoms

```
output Write	enough	code	to	make	it	pass Refactor Write	the	test	first Try	and	run	the	test Write	minimal	amount	of	code	for	the	test	to	run	and	check	the failing	test	output Write	enough	code	to	make	it	pass Write	the	test	first Try	and	run	the	test Write	the	minimal	amount	of	code	for	the	test	to	run	and	check	the failing	test	output Write	enough	code	to	make	it	pass Note	on	declaring	a	new	error	for	Update Write	the	test	first Try	to	run	the	test Write	the	minimal	amount	of	code	for	the	test	to	run	and	check	the failing	test	output Write	enough	code	to	make	it	pass Refactor Try	to	run	test Write	enough	code	to	make	it	pass Wrapping	up
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00003))_

> It is nice to commit at this point in case you somehow get into a mess with refactoring - you can always go back to the working version.
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00065))_

```
Constants	are	defined	like	so We	can	now	refactor	our	code const englishHelloPrefix	=	"Hello,	" const englishHelloPrefix	=	"Hello,	" func Hello(name	string)	string	{ return englishHelloPrefix	+	name }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00068))_

> We already refactored Sum - all we did was replace arrays with slices, so no extra changes are required.
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00325))_


## Source

- [[coding-learn-go-with-tests-excerpt]]
