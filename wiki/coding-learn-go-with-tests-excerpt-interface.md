---
page_id: coding-learn-go-with-tests-excerpt-interface
page_kind: concept
summary: Interface: 8 statement(s) and 2 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-interface@600a3443f708fc9d4148f6dfb5774e98
---

# Interface

What [[coding-learn-go-with-tests-excerpt]] covers about interface:

## Statements

- This web interface allows you to search for documentation of standard library packages and third-party packages. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00209))_
- Interfaces are a very powerful concept in statically typed languages like Go because they allow you to make functions that can be used with different types and create highly-decoupled code whilst still maintaining type-safety. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00474))_
- If the type you pass in matches what the interface is asking for, it will compile. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00490))_
- In Go interface resolution is implicit . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00490))_
- By declaring an interface, the helper is decoupled from the concrete types and only has the method it needs to do its job. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00492))_
- This kind of approach of using interfaces to declare only what you need is very important in software design and will be covered in more detail in later sections. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00493))_
- Interfaces are a great tool for hiding complexity away from other parts of the system. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00543))_
- You'll learn about interfaces defined in the standard library that are used everywhere and by implementing them against your own types, you can very quickly re-use a lot of great functionality. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00544))_

## Technical atoms

> Context: With Go, we can codify this intent with interfaces .
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00473))_

```
func TestArea(t	*testing.T)	{
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00476))_

> Context: How does something become a shape? We just tell Go what a Shape is using an interface declaration
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00479))_

```
type Shape interface { Area()	float64 }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00480))_


## Source

- [[coding-learn-go-with-tests-excerpt]]
