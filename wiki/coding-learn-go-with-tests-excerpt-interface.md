---
page_id: coding-learn-go-with-tests-excerpt-interface
page_kind: concept
summary: Interface: 8 statement(s) and 2 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
page_family: topic-concept
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-30
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-interface@5243d12061e93d2bac83994eaa38dff1
---

# Interface

What [[coding-learn-go-with-tests-excerpt]] covers about interface:

## Statements

### Testable Examples

- If you publish your code with examples to a public URL, you can share the documentation of your code at pkg.go.dev. For example, here is the finalised API for this chapter. This web interface allows you to search for documentation of standard library packages and third-party packages. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00209))_

### What are methods? / Refactor

- Interfaces are a very powerful concept in statically typed languages like Go because they allow you to make functions that can be used with different types and create highly-decoupled code whilst still maintaining type-safety. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00474))_

### Wait, what?

- In Go interface resolution is implicit . If the type you pass in matches what the interface is asking for, it will compile. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00490))_

### Decoupling

- Notice how our helper does not need to concern itself with whether the shape is a Rectangle or a Circle or a Triangle . By declaring an interface, the helper is decoupled from the concrete types and only has the method it needs to do its job. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00492))_

- This kind of approach of using interfaces to declare only what you need is very important in software design and will be covered in more detail in later sections. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00493))_

### Decoupling / Wrapping up

- Interfaces are a great tool for hiding complexity away from other parts of the system. In our case our test helper code did not need to know the exact shape it was asserting on, only how to "ask" for its area. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00543))_

- As you become more familiar with Go you will start to see the real strength of interfaces and the standard library. You'll learn about interfaces defined in the standard library that are used everywhere and by implementing them against your own types, you can very quickly re-use a lot of great functionality. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00544))_


## Technical atoms

### Technical frame 1: What are methods? / Refactor

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00478))_

> We are creating a helper function like we have in other exercises but this time we are asking for a Shape to be passed in. If we try to call this with something that isn't a shape, then it will not compile.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00476))_

```
func TestArea(t *testing.T) {
```

### Technical frame 2: What are methods? / Refactor

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00481))_

> We're creating a new type just like we did with Rectangle and Circle but this time it is an interface rather than a struct .

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00480))_

```
type Shape interface {
    Area() float64
}
```


## Related pages

- [[coding-learn-go-with-tests-excerpt-helper]] - shared statements: Helper shares source evidence from Decoupling: Notice how our helper does not need to concern itself with whether the shape is a Rectangle or a Circle or a Triangle . By declaring an interface, the helper is deco ... [truncated] (1 shared statement(s))
- [[coding-learn-go-with-tests-excerpt-type]] - shared statements: Type shares source evidence from Wait, what?: In Go interface resolution is implicit . If the type you pass in matches what the interface is asking for, it will compile. (1 shared statement(s))

## Source

- [[coding-learn-go-with-tests-excerpt]]
