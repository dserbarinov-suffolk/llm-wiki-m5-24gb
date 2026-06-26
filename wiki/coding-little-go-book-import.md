---
page_id: coding-little-go-book-import
page_kind: concept
summary: Imports: 12 statement(s) and 3 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-import@9c797ce8b12cdd8ae225b38573fb01a8
---

# Imports

What [[coding-little-go-book]] covers about imports:

## Statements

- Go has a number of built-in functions, such as println , which can be used without reference. _(coding_little_go_book.pdf (source-range-773b6275-00058))_
- We can't get very far though, without making use of Go's standard library and eventually using third-party libraries. _(coding_little_go_book.pdf (source-range-773b6275-00058))_
- We've also introduced another built-in function len . _(coding_little_go_book.pdf (source-range-773b6275-00063))_
- For now, knowing how to import and use a package is a good start. _(coding_little_go_book.pdf (source-range-773b6275-00064))_
- You've probably noticed we prefix the function name with the package, e.g., fmt.Println . _(coding_little_go_book.pdf (source-range-773b6275-00064))_
- This is different from many other languages. _(coding_little_go_book.pdf (source-range-773b6275-00064))_
- It will not compile if you import a package but don't use it. _(coding_little_go_book.pdf (source-range-773b6275-00065))_
- Go is strict about importing packages. _(coding_little_go_book.pdf (source-range-773b6275-00065))_
- Go is strict about this because unused imports can slow compilation; admittedly a problem most of us don't have to this degree. _(coding_little_go_book.pdf (source-range-773b6275-00067))_
- Over time, you'll get used to it (it'll still be annoying though). _(coding_little_go_book.pdf (source-range-773b6275-00067))_
- You can click on that section header and see the source code. _(coding_little_go_book.pdf (source-range-773b6275-00068))_
- Another thing to note is that Go's standard library is well documented. _(coding_little_go_book.pdf (source-range-773b6275-00068))_

## Technical atoms

> Context: Go has a number of built-in functions, such as println , which can be used without reference. We can't get very far though, without making use of Go's standard library and eventually using third-party libraries. In Go, the import keyword is used to declare the packages that are used by the code in the file. Let's change our program:
_(context: coding_little_go_book.pdf (source-range-773b6275-00058))_

```
func main() {
  if len(os.Args) != 2 {
    os.Exit(1)
  }
  fmt.Println("It's over", os.Args[1])
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00060))_

> Context: Go is strict about importing packages. It will not compile if you import a package but don't use it. Try to run the following: You should get two errors about fmt and os being imported and not used. Can this get annoying? Absolutely. Over time, you'll get used to it (it'll still be annoying though). Go is strict about this because unused imports can slow compilation; admittedly a problem most of us don't have to this degree.
_(context: coding_little_go_book.pdf (source-range-773b6275-00065, source-range-773b6275-00067))_

```
package main
import (
  "fmt"
  "os"
)
func main() {
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00066))_

> Context: Go is strict about importing packages. It will not compile if you import a package but don't use it. Try to run the following:
_(context: coding_little_go_book.pdf (source-range-773b6275-00065))_

> You should get two errors about fmt and os being imported and not used.
_(source: coding_little_go_book.pdf (source-range-773b6275-00067))_


## Source

- [[coding-little-go-book]]
