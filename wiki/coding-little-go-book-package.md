---
page_id: coding-little-go-book-package
page_kind: concept
summary: package db: 7 statement(s) and 3 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-package@e07b26c6f42036c209daa429bfdfc9ac
---

# package db

What [[coding-little-go-book]] covers about package db:

## Statements

- Notice that the name of the package is the same as the name of the folder. _(coding_little_go_book.pdf (source-range-773b6275-00277))_
- If you're building a package, you don't need anything more than what we've seen. _(coding_little_go_book.pdf (source-range-773b6275-00281))_
- It's tempting to think that importing shopping/db is somehow special because we're inside the shopping package/folder already. _(coding_little_go_book.pdf (source-range-773b6275-00280))_
- We're just using this as an example to show how to organize code. _(coding_little_go_book.pdf (source-range-773b6275-00277))_
- Now, create a file called pricecheck.go inside of the main shopping folder. _(coding_little_go_book.pdf (source-range-773b6275-00278))_
- To build an executable, you still need a main . _(coding_little_go_book.pdf (source-range-773b6275-00281))_
- The way I prefer to do this is to create a subfolder called main inside of shopping with a file called main.go and the following content: _(coding_little_go_book.pdf (source-range-773b6275-00281))_

## Technical atoms

```
type Item struct {
  Price float64
}
func LoadItem(id int) *Item {
  return &Item{
    Price: 9.001,
  }
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00276))_

> Context: Now, create a file called pricecheck.go inside of the main shopping folder. Its content is: It's tempting to think that importing shopping/db is somehow special because we're inside the shopping package/folder already. In reality, you're importing $GOPATH/src/shopping/db , which means you could just as easily import test/db so long as you had a package named db inside of your workspace's src/test folder.
_(context: coding_little_go_book.pdf (source-range-773b6275-00278, source-range-773b6275-00280))_

```
package shopping
import (
  "shopping/db"
)
func PriceCheck(itemId int) (float64, bool) {
  item := db.LoadItem(itemId)
  if item == nil {
    return 0, false
  }
  return item.Price, true
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00279))_

> Context: If you're building a package, you don't need anything more than what we've seen. To build an executable, you still need a main . The way I prefer to do this is to create a subfolder called main inside of shopping with a file called main.go and the following content:
_(context: coding_little_go_book.pdf (source-range-773b6275-00281))_

```
package main
import (
  "shopping"
  "fmt"
)
func main() {
  fmt.Println(shopping.PriceCheck(4343))
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00282))_


## Source

- [[coding-little-go-book]]
