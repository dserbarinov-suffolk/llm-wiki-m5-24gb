---
page_id: coding-little-go-book-section-chapter-5-tidbits-defer-9e77b4c5
page_kind: source
summary: Chapter 5 - Tidbits / Defer: 7 source-backed entries and 3 atom(s) from raw/coding_little_go_book.pdf.
page_family: section-reference
sources: raw/coding_little_go_book.pdf
updated: 2026-06-30
domain: coding-little-go-book
category_path: sources/coding-little-go-book/sections
source_id: coding_little_go_book.pdf
projection_coverage: section-coding-little-go-book-section-chapter-5-tidbits-defer-9e77b4c5@4da991a45c5168b305e49f732576d450
---

# Chapter 5 - Tidbits / Defer

From [[coding-little-go-book]].

## Related pages

- [[coding-little-go-book-section-chapter-5-tidbits-e7a41f7c]] - broader source section: Chapter 5 - Tidbits
- [[coding-little-go-book-section-chapter-5-tidbits-error-handling-c2084411]] - previous source section: Chapter 5 - Tidbits / Error Handling
- [[coding-little-go-book-section-chapter-5-tidbits-go-fmt-e0b0680f]] - next source section: Chapter 5 - Tidbits / go fmt

## Statements

- If you try to run the above code, you'll probably get an error (the file doesn't exist). The point is to show how defer works. Whatever you defer will be executed after the enclosing function (in this case main() ) returns, even if it does so violently. This lets you release resources near where it's initialized and takes care of multiple return points. _(coding_little_go_book.pdf (source-range-23d24eb1-00354))_
- Whatever you defer will be executed after the enclosing function (in this case main() ) returns, even if it does so violently. _(coding_little_go_book.pdf (source-range-23d24eb1-00354))_

## Technical atoms

### Technical frame 1: Chapter 5 - Tidbits / Defer

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00354))_

> If you try to run the above code, you'll probably get an error (the file doesn't exist). The point is to show how defer works. Whatever you defer will be executed after the enclosing function (in this case main() ) returns, even if it does so violently. This lets you release resources near where it's initialized and takes care of multiple return points.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00352))_

> Even though Go has a garbage collector, some resources require that we explicitly release them. For example, we need to Close() files after we're done with them. This sort of code is always dangerous. For one thing, as we're writing a function, it's easy to forget to Close something that we declared 10 lines up. For another, a function might have multiple return points. Go's solution is the defer keyword:

### Technical frame 2: Chapter 5 - Tidbits / Defer

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00354))_

> If you try to run the above code, you'll probably get an error (the file doesn't exist). The point is to show how defer works. Whatever you defer will be executed after the enclosing function (in this case main() ) returns, even if it does so violently. This lets you release resources near where it's initialized and takes care of multiple return points.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00353))_

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

### Technical frame 3: Chapter 5 - Tidbits / Defer

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00354))_

> If you try to run the above code, you'll probably get an error (the file doesn't exist).
