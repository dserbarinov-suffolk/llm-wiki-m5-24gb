---
page_id: coding-learn-go-with-tests-excerpt-syntax
page_kind: concept
summary: Syntax: 5 statement(s) and 2 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
page_family: topic-concept
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-30
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-syntax@7b808029f86dcaa30a98a332fca34c9f
---

# Syntax

What [[coding-learn-go-with-tests-excerpt]] covers about syntax:

## Statements

### Integers / Write enough code to make it pass

- Once we're more familiar with Go's syntax I will introduce a technique called "Property Based Testing" , which would stop annoying developers and help you find bugs. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00186))_

### Iteration / Write enough code to make it pass

- The for syntax is very unremarkable and follows most C-like languages. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00232))_

### Arrays and their type / Write enough code to make it pass

- Slices can be sliced! The syntax is slice[low:high] . If you omit the value on one of the sides of the : it captures everything to that side of it. In our case, we are saying "take from 1 to the end" with numbers[1:] . You may wish to spend some time writing other tests around slices and experiment with the slice operator to get more familiar with it. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00374))_

### What are methods? / Write the minimal amount of code for the test to run and check the failing test output

- The syntax for declaring methods is almost the same as functions and that's because they're so similar. The only difference is the syntax of the method receiver func (receiverName ReceiverType) MethodName(args) . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00458))_

### Decoupling / Further refactoring

- The only new syntax here is creating an "anonymous struct", areaTests . We are declaring a slice of structs by using []struct with two fields, the shape and the want . Then we fill the slice with cases. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00498))_


## Technical atoms

### Technical frame 1: What are methods? / Write the minimal amount of code for the test to run and check the failing test output

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00458))_

> The syntax for declaring methods is almost the same as functions and that's because they're so similar. The only difference is the syntax of the method receiver func (receiverName ReceiverType) MethodName(args) .

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00456))_

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

### Technical frame 2: What are methods? / Write the minimal amount of code for the test to run and check the failing test output

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00458))_

> The syntax for declaring methods is almost the same as functions and that's because they're so similar. The only difference is the syntax of the method receiver func (receiverName ReceiverType) MethodName(args) .

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00457))_

```
}
func (c Circle) Area() float64 {
    return 0
}
```


## Related pages

- [[coding-learn-go-with-tests-excerpt-write-code-pass]] - shared statements: Write enough code to make it pass shares source evidence from Integers / Write enough code to make it pass: Once we're more familiar with Go's syntax I will introduce a technique called "Property Based Testing" , which would stop annoying developers and help you find bugs. (3 shared statement(s))

## Source

- [[coding-learn-go-with-tests-excerpt]]
