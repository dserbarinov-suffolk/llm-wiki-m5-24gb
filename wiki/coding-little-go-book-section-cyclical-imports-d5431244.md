---
page_id: coding-little-go-book-section-cyclical-imports-d5431244
page_kind: source
summary: Cyclical Imports: 6 source-backed entries and 4 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: sources/coding-little-go-book/sections
source_id: coding_little_go_book.pdf
projection_coverage: section-coding-little-go-book-section-cyclical-imports-d5431244@b5463a002c5a5aa90c261536d5e7a9b6
---

# Cyclical Imports

From [[coding-little-go-book]].

## Statements

- This is something the compiler won't allow. _(coding_little_go_book.pdf (source-range-773b6275-00286))_
- Item no longer exists in the db package; it's been moved to the shopping package. _(coding_little_go_book.pdf (source-range-773b6275-00290))_

## Technical atoms

```
package shopping
import (
  "shopping/db"
)
type Item struct {
  Price float64
}
func PriceCheck(itemId int) (float64, bool) {
  item := db.LoadItem(itemId)
  if item == nil {
    return 0, false
  }
  return item.Price, true
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00289))_

> If you try to run the code, you'll get a couple of errors from db/db.go about Item being undefined.
_(source: coding_little_go_book.pdf (source-range-773b6275-00290))_

```
package db
import (
  "shopping"
)
func LoadItem(id int) *shopping.Item {
  return &shopping.Item{
    Price: 9.001,
  }
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00291))_

> Now when you try to run the code, you'll get a dreaded import cycle not allowed error.
_(source: coding_little_go_book.pdf (source-range-773b6275-00292))_
