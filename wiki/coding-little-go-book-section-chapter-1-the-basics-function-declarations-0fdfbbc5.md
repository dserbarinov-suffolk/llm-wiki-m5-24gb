---
page_id: coding-little-go-book-section-chapter-1-the-basics-function-declarations-0fdfbbc5
page_kind: source
summary: Chapter 1 - The Basics / Function Declarations: 10 source-backed entries and 4 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-29
domain: coding-little-go-book
category_path: sources/coding-little-go-book/sections
source_id: coding_little_go_book.pdf
projection_coverage: section-coding-little-go-book-section-chapter-1-the-basics-function-declarations-0fdfbbc5@001c13f8ea047264cdc2105b6d04eba0
---

# Chapter 1 - The Basics / Function Declarations

From [[coding-little-go-book]].

## Related pages

- [[coding-little-go-book-section-chapter-1-the-basics-45e21143]] - broader source section: Chapter 1 - The Basics
- [[coding-little-go-book-section-chapter-1-the-basics-variables-and-declarations-dd932e02]] - previous source section: Chapter 1 - The Basics / Variables and Declarations
- [[coding-little-go-book-section-chapter-1-the-basics-before-you-continue-b0ff71fd]] - next source section: Chapter 1 - The Basics / Before You Continue

## Statements

- This is a good time to point out that functions can return multiple values. Let's look at three functions: one with no return value, one with one return value, and one with two return values. _(coding_little_go_book.pdf (source-range-23d24eb1-00096))_
- This is more than a convention. _ , the blank identifier, is special in that the return value isn't actually assigned. This lets you use _ over and over again regardless of the returned type. _(coding_little_go_book.pdf (source-range-23d24eb1-00102))_
- Being able to return multiple values is something you'll use often. You'll also frequently use _ to discard a value. Named return values and the slightly less verbose parameter declaration aren't that common. Still, you'll run into all of these sooner than later so it's important to know about them. _(coding_little_go_book.pdf (source-range-23d24eb1-00105))_
- Sometimes, you only care about one of the return values. _(coding_little_go_book.pdf (source-range-23d24eb1-00100))_

## Technical atoms

### Technical frame 1: Chapter 1 - The Basics / Function Declarations

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00102))_

> This is more than a convention. _ , the blank identifier, is special in that the return value isn't actually assigned. This lets you use _ over and over again regardless of the returned type.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00097))_

```
func log(message string) {
}
func add(a int, b int) int {
}
func power(name string) (int, bool) {
}
```

### Technical frame 2: Chapter 1 - The Basics / Function Declarations

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00102))_

> This is more than a convention. _ , the blank identifier, is special in that the return value isn't actually assigned. This lets you use _ over and over again regardless of the returned type.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00099))_

```
value, exists := power("goku")
if exists == false {
  // handle this error case
}
```

### Technical frame 3: Chapter 1 - The Basics / Function Declarations

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00102))_

> This is more than a convention. _ , the blank identifier, is special in that the return value isn't actually assigned. This lets you use _ over and over again regardless of the returned type.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00101))_

```
_, exists := power("goku")
if exists == false {
  // handle this error case
}
```

### Technical frame 4: Chapter 1 - The Basics / Function Declarations

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00105))_

> Being able to return multiple values is something you'll use often. You'll also frequently use _ to discard a value. Named return values and the slightly less verbose parameter declaration aren't that common. Still, you'll run into all of these sooner than later so it's important to know about them.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00104))_

```
func add(a, b int) int {
}
```
