---
page_id: coding-little-go-book-empty-interface-and-conversion
page_kind: concept
summary: Empty Interface and Conversions: 6 statement(s) and 3 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-empty-interface-and-conversion@ab6a3c28b2d5628e5f24fcac79503be2
---

# Empty Interface and Conversions

What [[coding-little-go-book]] covers about empty interface and conversions:

## Statements

- Since every type implements all 0 of the empty interface's methods, and since interfaces are implicitly implemented, every type fulfills the contract of the empty interface. _(coding_little_go_book.pdf (source-range-773b6275-00368))_
- Converting values back and forth is ugly and dangerous but sometimes, in a static language, it's the only choice. _(coding_little_go_book.pdf (source-range-773b6275-00376))_
- You'll see and probably use the empty interface more than you might first expect. _(coding_little_go_book.pdf (source-range-773b6275-00376))_
- In most object-oriented languages, a built-in base class, often named object , is the superclass for all other classes. _(coding_little_go_book.pdf (source-range-773b6275-00368))_
- Go, having no inheritance, doesn't have such a superclass. _(coding_little_go_book.pdf (source-range-773b6275-00368))_
- Note that if the underlying type is not int , the above will result in an error. _(coding_little_go_book.pdf (source-range-773b6275-00373))_

## Technical atoms

> Context: If we wanted to, we could write an add function with the following signature:
_(context: coding_little_go_book.pdf (source-range-773b6275-00369))_

```
func add(a interface{}, b interface{}) interface{} {
  ...
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00370))_

> Context: To convert an interface variable to an explicit type, you use .(TYPE) : Note that if the underlying type is not int , the above will result in an error.
_(context: coding_little_go_book.pdf (source-range-773b6275-00371, source-range-773b6275-00373))_

```
return a.(int) + b.(int)
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00372))_

> Context: You also have access to a powerful type switch: You'll see and probably use the empty interface more than you might first expect. Admittedly, it won't result in clean code. Converting values back and forth is ugly and dangerous but sometimes, in a static language, it's the only choice.
_(context: coding_little_go_book.pdf (source-range-773b6275-00374, source-range-773b6275-00376))_

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
_(source: coding_little_go_book.pdf (source-range-773b6275-00375))_


## Source

- [[coding-little-go-book]]
