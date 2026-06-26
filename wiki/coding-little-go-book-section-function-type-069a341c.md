---
page_id: coding-little-go-book-section-function-type-069a341c
page_kind: source
summary: Function Type: 5 source-backed entries and 3 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: sources/coding-little-go-book/sections
source_id: coding_little_go_book.pdf
projection_coverage: section-coding-little-go-book-section-function-type-069a341c@48e112072547110ef66fce4ef09e60b6
---

# Function Type

From [[coding-little-go-book]].

## Statements

- which can then be used anywhere -- as a field type, as a parameter, as a return value. _(coding_little_go_book.pdf (source-range-773b6275-00389))_
- which can then be used anywhere -- as a field type, as a parameter, as a return value. _(coding_little_go_book.pdf (source-range-773b6275-00389))_

## Technical atoms

```
type Add func(a int, b int) int
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00388))_

```
package main
import (
  "fmt"
)
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00390))_

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
_(source: coding_little_go_book.pdf (source-range-773b6275-00391))_
