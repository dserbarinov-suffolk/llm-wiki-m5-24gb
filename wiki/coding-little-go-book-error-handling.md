---
page_id: coding-little-go-book-error-handling
page_kind: concept
summary: Error Handling: 6 statement(s) and 7 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-error-handling@8790793b072cb409231ec5433af41f58
---

# Error Handling

What [[coding-little-go-book]] covers about error handling:

## Statements

- Go's preferred way to deal with errors is through return values, not exceptions. _(coding_little_go_book.pdf (source-range-773b6275-00339))_
- You can create your own error type; the only requirement is that it fulfills the contract of the built-in error interface, which is: _(coding_little_go_book.pdf (source-range-773b6275-00341))_
- This is a package variable (it's defined outside of a function) which is publicly accessible (upper-case first letter). _(coding_little_go_book.pdf (source-range-773b6275-00348))_
- If it makes contextual sense, you should use this error, too. _(coding_little_go_book.pdf (source-range-773b6275-00348))_
- As a final note, Go does have panic and recover functions. _(coding_little_go_book.pdf (source-range-773b6275-00350))_
- panic is like throwing an exception while recover is like catch ; they are rarely used. _(coding_little_go_book.pdf (source-range-773b6275-00350))_

## Technical atoms

> Context: Go's preferred way to deal with errors is through return values, not exceptions. Consider the strconv.Atoi function which takes a string and tries to convert it to an integer:
_(context: coding_little_go_book.pdf (source-range-773b6275-00339))_

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

> Context: You can create your own error type; the only requirement is that it fulfills the contract of the built-in error interface, which is:
_(context: coding_little_go_book.pdf (source-range-773b6275-00341))_

```
type error interface {
  Error() string
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00342))_

> Context: More commonly, we can create our own errors by importing the errors package and using it in the New function:
_(context: coding_little_go_book.pdf (source-range-773b6275-00343))_

```
import (
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00344))_

> Context: More commonly, we can create our own errors by importing the errors package and using it in the New function:
_(context: coding_little_go_book.pdf (source-range-773b6275-00343))_

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

> Context: There's a common pattern in Go's standard library of using error variables. For example, the io package has an EOF variable which is defined as:
_(context: coding_little_go_book.pdf (source-range-773b6275-00346))_

```
var EOF = errors.New("EOF")
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00347))_

> Context: There's a common pattern in Go's standard library of using error variables. For example, the io package has an EOF variable which is defined as:
_(context: coding_little_go_book.pdf (source-range-773b6275-00346))_

> Various functions can return this error, say when we're reading from a file or STDIN.
_(source: coding_little_go_book.pdf (source-range-773b6275-00348))_


## Source

- [[coding-little-go-book]]
