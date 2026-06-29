---
page_id: coding-learn-go-with-tests-excerpt-section-structs-methods-interfaces-write-the-minimal-amount-of-code-for-the-test-to-run-and-check-the-fa-44e30158
page_kind: source
summary: Structs, methods & interfaces / Write the minimal amount of code for the test to run and check the failing test output: 4 source-backed entries and 1 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-29
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-structs-methods-interfaces-write-the-minimal-amount-of-code-for-the-test-to-run-and-check-the-fa-44e30158@19f0c7c8330b8afd0b0841cbe739f381
---

# Structs, methods & interfaces / Write the minimal amount of code for the test to run and check the failing test output

From [[coding-learn-go-with-tests-excerpt]].

## Related pages

- [[coding-learn-go-with-tests-excerpt-section-structs-methods-interfaces-82e8585b]] - broader source section: Structs, methods & interfaces
- [[coding-learn-go-with-tests-excerpt-section-structs-methods-interfaces-try-to-run-the-test-fadb70be]] - previous source section: Structs, methods & interfaces / Try to run the test

## Statements

- You can have functions with the same name declared in different packages . So we could create our Area(Circle) in a new package, but that feels overkill here. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00445))_
- We can define methods on our newly defined types instead. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00446))_

## Technical atoms

### Technical frame 1: Structs, methods & interfaces / Write the minimal amount of code for the test to run and check the failing test output

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00445))_

> You can have functions with the same name declared in different packages . So we could create our Area(Circle) in a new package, but that feels overkill here.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00443))_

```
We need to deﬁne our Circle type.
type Circle struct {
    Radius float64
}
Now try to run the tests again
./shapes_test.go:29:14: cannot use circle (type Circle) as type 
Rectangle in argument to Area
Some programming languages allow you to do something like this:
func Area(circle Circle) float64       {}
func Area(rectangle Rectangle) float64 {}
But you cannot in Go
./shapes.go:20:32: Area redeclared in this block
```
