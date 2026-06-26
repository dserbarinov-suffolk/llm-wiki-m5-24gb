---
page_id: coding-learn-go-with-tests-excerpt-syntax
page_kind: concept
summary: Syntax: 5 statement(s) and 2 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-syntax@004a42dc8e3c51b4900ea14698501905
---

# Syntax

What [[coding-learn-go-with-tests-excerpt]] covers about syntax:

## Statements

- Once we're more familiar with Go's syntax I will introduce a technique called "Property Based Testing" , which would stop annoying developers and help you find bugs. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00186))_
- The for syntax is very unremarkable and follows most C-like languages. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00232))_
- The syntax is slice[low:high] . _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00374))_
- The syntax for declaring methods is almost the same as functions and that's because they're so similar. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00458))_
- The only new syntax here is creating an "anonymous struct", areaTests . _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00498))_

## Technical atoms

> Context: The syntax for declaring methods is almost the same as functions and that's because they're so similar. The only difference is the syntax of the method receiver func (receiverName ReceiverType) MethodName(args) .
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00458))_

```
type Rectangle struct {
    Width  float64
    Height float64
}
func (r Rectangle) Area() float64 {
    return 0
}
type Circle struct {
    Radius float64
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00456))_

> Context: The syntax for declaring methods is almost the same as functions and that's because they're so similar. The only difference is the syntax of the method receiver func (receiverName ReceiverType) MethodName(args) .
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00458))_

```
}
func (c Circle) Area() float64 {
    return 0
}
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00457))_


## Source

- [[coding-learn-go-with-tests-excerpt]]
