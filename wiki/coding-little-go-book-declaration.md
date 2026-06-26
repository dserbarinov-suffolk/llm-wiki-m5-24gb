---
page_id: coding-little-go-book-declaration
page_kind: concept
summary: Declaration: 4 statement(s) and 3 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-declaration@b1c4ba45910374775298d2eb2fd3b11c
---

# Declaration

What [[coding-little-go-book]] covers about declaration:

## Statements

- The most explicit way to deal with variable declaration and assignment in Go is also the most verbose: _(coding_little_go_book.pdf (source-range-773b6275-00075))_
- Go has a handy short variable declaration operator, := , which can infer the type: _(coding_little_go_book.pdf (source-range-773b6275-00079))_
- When we first looked at variables and declarations, we looked only at built-in types, like integers and strings. _(coding_little_go_book.pdf (source-range-773b6275-00117))_
- Furthermore, you can skip the field name and rely on the order of the field declarations (though for the sake of clarity, you should only do this for structures with few fields): _(coding_little_go_book.pdf (source-range-773b6275-00124))_

## Technical atoms

> Context: The most explicit way to deal with variable declaration and assignment in Go is also the most verbose:
_(context: coding_little_go_book.pdf (source-range-773b6275-00075))_

```
package main
import (
  "fmt"
)
func main() {
  var power int
  power = 9000
  fmt.Printf("It's over %d\n", power)
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00076))_

> Context: Still, that's a lot of typing. Go has a handy short variable declaration operator, := , which can infer the type:
_(context: coding_little_go_book.pdf (source-range-773b6275-00079))_

```
power := 9000
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00080))_

> Context: Furthermore, you can skip the field name and rely on the order of the field declarations (though for the sake of clarity, you should only do this for structures with few fields): What all of the above examples do is declare a variable goku and assign a value to it.
_(context: coding_little_go_book.pdf (source-range-773b6275-00124, source-range-773b6275-00126))_

```
goku := Saiyan{"Goku", 9000}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00125))_


## Source

- [[coding-little-go-book]]
