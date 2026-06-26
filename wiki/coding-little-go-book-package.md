---
page_id: coding-little-go-book-package
page_kind: concept
summary: Package: 5 statement(s) and 4 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-package@7aeb19b698c23946eac1caec65e2cc62
---

# Package

What [[coding-little-go-book]] covers about package:

## Statements

- Item no longer exists in the db package; it's been moved to the shopping package. _(coding_little_go_book.pdf (source-range-773b6275-00290))_
- Notice that the name of the package is the same as the name of the folder. _(coding_little_go_book.pdf (source-range-773b6275-00277))_
- If you're building a package, you don't need anything more than what we've seen. _(coding_little_go_book.pdf (source-range-773b6275-00281))_
- If a structure field name starts with a lowercase letter, only code within the same package will be able to access them. _(coding_little_go_book.pdf (source-range-773b6275-00300))_
- The io package has a handful of popular ones such as io.Reader , io.Writer , and io.Closer . _(coding_little_go_book.pdf (source-range-773b6275-00329))_

## Technical atoms

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

> Context: If you try to run the code, you'll get a couple of errors from db/db.go about Item being undefined. This makes sense. Item no longer exists in the db package; it's been moved to the shopping package. We need to change shopping/db/db.go to:
_(context: coding_little_go_book.pdf (source-range-773b6275-00290))_

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

> Context: If you try to run the code, you'll get a couple of errors from db/db.go about Item being undefined. This makes sense. Item no longer exists in the db package; it's been moved to the shopping package. We need to change shopping/db/db.go to:
_(context: coding_little_go_book.pdf (source-range-773b6275-00290))_

> Now when you try to run the code, you'll get a dreaded import cycle not allowed error.
_(source: coding_little_go_book.pdf (source-range-773b6275-00292))_


## Source

- [[coding-little-go-book]]
