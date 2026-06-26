---
page_id: coding-learn-go-with-tests-excerpt-section-write-the-minimal-amount-of-code-for-the-test-to-run-and-check-the-faili-088b62e3
page_kind: source
summary: Write the minimal amount of code for the test to run and check the failing test output: 12 source-backed entries and 4 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-write-the-minimal-amount-of-code-for-the-test-to-run-and-check-the-faili-088b62e3@2278c68116b609d2b381ddf05affb34c
---

# Write the minimal amount of code for the test to run and check the failing test output

From [[coding-learn-go-with-tests-excerpt]].

## Statements

- The only difference is the syntax of the method receiver func (receiverName ReceiverType) MethodName(args) . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00458))_
- The syntax for declaring methods is almost the same as functions and that's because they're so similar. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00458))_
- The only difference is the syntax of the method receiver func (receiverName ReceiverType) MethodName(args) . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00458))_
- The syntax for declaring methods is almost the same as functions and that's because they're so similar. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00458))_
- In many other programming languages this is done implicitly and you access the receiver via this . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00459))_
- When your method is called on a variable of that type, you get your reference to its data via the receiverName variable. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00459))_
- When your method is called on a variable of that type, you get your reference to its data via the receiverName variable. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00459))_
- It is a convention in Go to have the receiver variable be the first letter of the type. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00460))_

## Technical atoms

```
type Rectangle struct { Width		float64 Height	float64 } func (r	Rectangle)	Area()	float64	{ return 0 } type Circle struct { Radius	float64
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00456))_

```
} func (c	Circle)	Area()	float64	{ return 0 }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00457))_

```
r	Rectangle
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00461))_

> If you try to re-run the tests they should now compile and give you some failing output.
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00462))_
