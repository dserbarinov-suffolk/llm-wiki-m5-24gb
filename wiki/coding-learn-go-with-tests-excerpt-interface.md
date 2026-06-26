---
page_id: coding-learn-go-with-tests-excerpt-interface
page_kind: concept
summary: Interface: 17 statement(s) and 2 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-interface@353e65fe5720dcbc29b02bd40d85df20
---

# Interface

What [[coding-learn-go-with-tests-excerpt]] covers about interface:

## Statements

- In Go interface resolution is implicit . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00490))_
- With Go, we can codify this intent with interfaces . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00473))_
- This is quite different to interfaces in most other programming languages. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00484))_
- Normally you have to write code to say My type Foo implements interface Bar . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00484))_
- If the type you pass in matches what the interface is asking for, it will compile. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00490))_
- Interfaces are a great tool for hiding complexity away from other parts of the system. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00543))_
- Circle has a method called Area that returns a float64 so it satisfies the Shape interface _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00487))_
- Rectangle has a method called Area that returns a float64 so it satisfies the Shape interface _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00486))_
- Adding methods so you can add functionality to your data types and so you can implement interfaces _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00540))_
- This web interface allows you to search for documentation of standard library packages and third-party packages. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00209))_
- As you become more familiar with Go you will start to see the real strength of interfaces and the standard library. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00544))_
- By declaring an interface, the helper is decoupled from the concrete types and only has the method it needs to do its job. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00492))_
- We're creating a new type just like we did with Rectangle and Circle but this time it is an interface rather than a struct . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00481))_
- This kind of approach of using interfaces to declare only what you need is very important in software design and will be covered in more detail in later sections. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00493))_

## Technical atoms

```
type Shape interface { Area()	float64 }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00480))_

> We made the errors constant; this required us to create our own DictionaryErr type which implements the error interface.
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00637))_


## Source

- [[coding-learn-go-with-tests-excerpt]]
