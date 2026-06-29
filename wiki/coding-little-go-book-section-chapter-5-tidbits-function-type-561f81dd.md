---
page_id: coding-little-go-book-section-chapter-5-tidbits-function-type-561f81dd
page_kind: source
summary: Chapter 5 - Tidbits / Function Type: 5 source-backed entries and 3 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-29
domain: coding-little-go-book
category_path: sources/coding-little-go-book/sections
source_id: coding_little_go_book.pdf
projection_coverage: section-coding-little-go-book-section-chapter-5-tidbits-function-type-561f81dd@9422ea48a3d7b914292c503274a8e639
---

# Chapter 5 - Tidbits / Function Type

From [[coding-little-go-book]].

## Related pages

- [[coding-little-go-book-section-chapter-5-tidbits-e7a41f7c]] - broader source section: Chapter 5 - Tidbits
- [[coding-little-go-book-section-chapter-5-tidbits-strings-and-byte-arrays-6caeb68b]] - previous source section: Chapter 5 - Tidbits / Strings and Byte Arrays
- [[coding-little-go-book-section-chapter-5-tidbits-before-you-continue-25d54302]] - next source section: Chapter 5 - Tidbits / Before You Continue

## Statements

- which can then be used anywhere -- as a field type, as a parameter, as a return value. _(coding_little_go_book.pdf (source-range-23d24eb1-00389))_
- which can then be used anywhere -- as a field type, as a parameter, as a return value. _(coding_little_go_book.pdf (source-range-23d24eb1-00389))_

## Technical atoms

### Technical frame 1: Chapter 5 - Tidbits / Function Type

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00389))_

> which can then be used anywhere -- as a field type, as a parameter, as a return value.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00388))_

```
type Add func(a int, b int) int
```

### Technical frame 2: Chapter 5 - Tidbits / Function Type

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00389))_

> which can then be used anywhere -- as a field type, as a parameter, as a return value.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00390))_

```
package main
import (
  "fmt"
)
```

### Technical frame 3: Chapter 5 - Tidbits / Function Type

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00389))_

> which can then be used anywhere -- as a field type, as a parameter, as a return value.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00391))_

```
type Add func(a int, b int) int
func main() {
  fmt.Println(process(func(a int, b int) int{
      return a + b
  }))
}
func process(adder Add) int {
  return adder(1, 2)
}
```
