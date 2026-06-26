---
page_id: coding-little-go-book-section-error-handling-3bbe033f
page_kind: source
summary: Error Handling: 14 source-backed entries and 7 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: sources/coding-little-go-book/sections
source_id: coding_little_go_book.pdf
projection_coverage: section-coding-little-go-book-section-error-handling-3bbe033f@89dabbbb9413bddcfe28e390dc0093d8
---

# Error Handling

From [[coding-little-go-book]].

## Statements

- Go's preferred way to deal with errors is through return values, not exceptions. _(coding_little_go_book.pdf (source-range-773b6275-00339))_
- You can create your own error type; the only requirement is that it fulfills the contract of the built-in error interface, which is: _(coding_little_go_book.pdf (source-range-773b6275-00341))_
- You can create your own error type; the only requirement is that it fulfills the contract of the built-in error interface, which is: _(coding_little_go_book.pdf (source-range-773b6275-00341))_
- This is a package variable (it's defined outside of a function) which is publicly accessible (upper-case first letter). _(coding_little_go_book.pdf (source-range-773b6275-00348))_
- If it makes contextual sense, you should use this error, too. _(coding_little_go_book.pdf (source-range-773b6275-00348))_
- As a final note, Go does have panic and recover functions. _(coding_little_go_book.pdf (source-range-773b6275-00350))_
- panic is like throwing an exception while recover is like catch ; they are rarely used. _(coding_little_go_book.pdf (source-range-773b6275-00350))_

## Technical atoms

```
package main
import (
  "fmt"
  "os"
  "strconv"
)
func main() {
  if len(os.Args) != 2 {
    os.Exit(1)
  }
n, err := strconv.Atoi(os.Args[1])
  if err != nil {
    fmt.Println("not a valid number")
  } else {
    fmt.Println(n)
  }
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00340))_

```
type error interface {
  Error() string
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00342))_

```
import (
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00344))_

```
"errors"
)
func process(count int) error {
  if count < 1 {
    return errors.New("Invalid count")
  }
  ...
  return nil
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00345))_

```
var EOF = errors.New("EOF")
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00347))_

> Various functions can return this error, say when we're reading from a file or STDIN.
_(source: coding_little_go_book.pdf (source-range-773b6275-00348))_

```
package main
import (
  "fmt"
  "io"
)
func main() {
  var input int
  _, err := fmt.Scan(&input)
  if err == io.EOF {
    fmt.Println("no more input!")
  }
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00349))_
