---
page_id: coding-learn-go-with-tests-excerpt-section-write-the-minimal-amount-of-code-for-the-test-to-run-and-check-the-faili-498e1008
page_kind: source
summary: Write the minimal amount of code for the test to run and check the failing test output: 4 source-backed entries and 1 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-write-the-minimal-amount-of-code-for-the-test-to-run-and-check-the-faili-498e1008@837fb3787532b7147875a63ae17048e3
---

# Write the minimal amount of code for the test to run and check the failing test output

From [[coding-learn-go-with-tests-excerpt]].

## Statements

- - You can have functions with the same name declared in different packages . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00445))_
- So we could create our Area(Circle) in a new package, but that feels overkill here. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00445))_
- - We can define methods on our newly defined types instead. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00446))_

## Technical atoms

```
We	need	to	define	our Circle type. Now	try	to	run	the	tests	again ./shapes_test.go:29:14:	cannot	use	circle	(type	Circle)	as	type Rectangle	in	argument	to	Area Some	programming	languages	allow	you	to	do	something	like	this: But	you	cannot	in	Go ./shapes.go:20:32:	Area	redeclared	in	this	block type Circle struct { Radius	float64 } func Area(circle	Circle)	float64							{} func Area(rectangle	Rectangle)	float64	{}
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00443))_
