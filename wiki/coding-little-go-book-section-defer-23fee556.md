---
page_id: coding-little-go-book-section-defer-23fee556
page_kind: source
summary: Defer: 7 source-backed entries and 3 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: sources/coding-little-go-book/sections
source_id: coding_little_go_book.pdf
projection_coverage: section-coding-little-go-book-section-defer-23fee556@6f657138c8b10cf54a42c70f0ac64875
---

# Defer

From [[coding-little-go-book]].

## Statements

- This lets you release resources near where it's initialized and takes care of multiple return points. _(coding_little_go_book.pdf (source-range-773b6275-00354))_
- Whatever you defer will be executed after the enclosing function (in this case main() ) returns, even if it does so violently. _(coding_little_go_book.pdf (source-range-773b6275-00354))_
- The point is to show how defer works. _(coding_little_go_book.pdf (source-range-773b6275-00354))_
- Whatever you defer will be executed after the enclosing function (in this case main() ) returns, even if it does so violently. _(coding_little_go_book.pdf (source-range-773b6275-00354))_

## Technical atoms

> Even though Go has a garbage collector, some resources require that we explicitly release them. For example, we need to Close() files after we're done with them. This sort of code is always dangerous. For one thing, as we're writing a function, it's easy to forget to Close something that we declared 10 lines up. For another, a function might have multiple return points. Go's solution is the defer keyword:
_(source: coding_little_go_book.pdf (source-range-773b6275-00352))_

```
package main
import (
  "fmt"
  "os"
)
func main() {
  file, err := os.Open("a_file_to_read")
  if err != nil {
    fmt.Println(err)
    return
  }
  defer file.Close()
  // read the file
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00353))_

> If you try to run the above code, you'll probably get an error (the file doesn't exist).
_(source: coding_little_go_book.pdf (source-range-773b6275-00354))_
