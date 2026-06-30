---
page_id: coding-little-go-book-empty-interface
page_kind: concept
summary: Empty Interface: 2 statement(s) and 1 atom(s) from raw/coding_little_go_book.pdf.
page_family: topic-concept
sources: raw/coding_little_go_book.pdf
updated: 2026-06-30
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-empty-interface@bfe679441ebd559f8af9a338595795fd
---

# Empty Interface

What [[coding-little-go-book]] covers about empty interface:

## Statements

### Chapter 5 - Tidbits / Empty Interface and Conversions

- In most object-oriented languages, a built-in base class, often named object , is the superclass for all other classes. Go, having no inheritance, doesn't have such a superclass. What it does have is an empty interface with no methods: interface{} . Since every type implements all 0 of the empty interface's methods, and since interfaces are implicitly implemented, every type fulfills the contract of the empty interface. _(coding_little_go_book.pdf (source-range-23d24eb1-00368))_

- You'll see and probably use the empty interface more than you might first expect. Admittedly, it won't result in clean code. Converting values back and forth is ugly and dangerous but sometimes, in a static language, it's the only choice. _(coding_little_go_book.pdf (source-range-23d24eb1-00376))_


## Technical atoms

### Technical frame 1: Chapter 5 - Tidbits / Empty Interface and Conversions

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00376))_

> You'll see and probably use the empty interface more than you might first expect. Admittedly, it won't result in clean code. Converting values back and forth is ugly and dangerous but sometimes, in a static language, it's the only choice.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00375))_

```
switch a.(type) {
  case int:
    fmt.Printf("a is now an int and equals %d\n", a)
  case bool, string:
    // ...
  default:
    // ...
}
```


## Related pages

- [[coding-little-go-book-type]] - shared statements and technical atoms: Type shares source evidence from Chapter 5 - Tidbits / Empty Interface and Conversions: In most object-oriented languages, a built-in base class, often named object , is the superclass for all other classes. Go, having no inheritance, doesn't have such ... [truncated]; Type shares technical record from Chapter 5 - Tidbits / Empty Interface and Conversions: switch a.(type) { case int: fmt.Printf("a is now an int and equals %d\n", a) case bool, string: // ... default: // ... } (1 shared statement(s), 1 shared atom(s))
- [[coding-little-go-book-value]] - shared technical atoms: Value shares technical record from Chapter 5 - Tidbits / Empty Interface and Conversions: switch a.(type) { case int: fmt.Printf("a is now an int and equals %d\n", a) case bool, string: // ... default: // ... } (1 shared atom(s))

## Source

- [[coding-little-go-book]]
