---
page_id: coding-little-go-book-section-chapter-5-tidbits-empty-interface-and-conversions-c4483a93
page_kind: source
summary: Chapter 5 - Tidbits / Empty Interface and Conversions: 10 source-backed entries and 3 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-29
domain: coding-little-go-book
category_path: sources/coding-little-go-book/sections
source_id: coding_little_go_book.pdf
projection_coverage: section-coding-little-go-book-section-chapter-5-tidbits-empty-interface-and-conversions-c4483a93@c708d39630d652b0707a0b825f0fca0e
---

# Chapter 5 - Tidbits / Empty Interface and Conversions

From [[coding-little-go-book]].

## Related pages

- [[coding-little-go-book-section-chapter-5-tidbits-e7a41f7c]] - broader source section: Chapter 5 - Tidbits
- [[coding-little-go-book-section-chapter-5-tidbits-initialized-if-10bfb3a1]] - previous source section: Chapter 5 - Tidbits / Initialized If
- [[coding-little-go-book-section-chapter-5-tidbits-strings-and-byte-arrays-6caeb68b]] - next source section: Chapter 5 - Tidbits / Strings and Byte Arrays

## Statements

- In most object-oriented languages, a built-in base class, often named object , is the superclass for all other classes. Go, having no inheritance, doesn't have such a superclass. What it does have is an empty interface with no methods: interface{} . Since every type implements all 0 of the empty interface's methods, and since interfaces are implicitly implemented, every type fulfills the contract of the empty interface. _(coding_little_go_book.pdf (source-range-23d24eb1-00368))_
- Note that if the underlying type is not int , the above will result in an error. _(coding_little_go_book.pdf (source-range-23d24eb1-00373))_
- You'll see and probably use the empty interface more than you might first expect. Admittedly, it won't result in clean code. Converting values back and forth is ugly and dangerous but sometimes, in a static language, it's the only choice. _(coding_little_go_book.pdf (source-range-23d24eb1-00376))_
- Converting values back and forth is ugly and dangerous but sometimes, in a static language, it's the only choice. _(coding_little_go_book.pdf (source-range-23d24eb1-00376))_

## Technical atoms

### Technical frame 1: Chapter 5 - Tidbits / Empty Interface and Conversions

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00373))_

> Note that if the underlying type is not int , the above will result in an error.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00370))_

```
func add(a interface{}, b interface{}) interface{} {
  ...
}
```

### Technical frame 2: Chapter 5 - Tidbits / Empty Interface and Conversions

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00373))_

> Note that if the underlying type is not int , the above will result in an error.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00372))_

```
return a.(int) + b.(int)
```

### Technical frame 3: Chapter 5 - Tidbits / Empty Interface and Conversions

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
