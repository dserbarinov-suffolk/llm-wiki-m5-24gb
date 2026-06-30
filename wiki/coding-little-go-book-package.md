---
page_id: coding-little-go-book-package
page_kind: concept
summary: Package: 5 statement(s) and 8 atom(s) from raw/coding_little_go_book.pdf.
page_family: topic-concept
sources: raw/coding_little_go_book.pdf
updated: 2026-06-30
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-package@3eb57f8138452e90b6bfe06c14b752d5
---

# Package

What [[coding-little-go-book]] covers about package:

## Statements

### Chapter 4 - Code Organization and Interfaces / Packages

- Notice that the name of the package is the same as the name of the folder. Also, obviously, we aren't actually accessing the database. We're just using this as an example to show how to organize code. _(coding_little_go_book.pdf (source-range-23d24eb1-00277))_

- If you're building a package, you don't need anything more than what we've seen. To build an executable, you still need a main . The way I prefer to do this is to create a subfolder called main inside of shopping with a file called main.go and the following content: _(coding_little_go_book.pdf (source-range-23d24eb1-00281))_

### Chapter 4 - Code Organization and Interfaces / Packages / Cyclical Imports

- If you try to run the code, you'll get a couple of errors from db/db.go about Item being undefined. This makes sense. Item no longer exists in the db package; it's been moved to the shopping package. We need to change shopping/db/db.go to: _(coding_little_go_book.pdf (source-range-23d24eb1-00290))_

### Chapter 4 - Code Organization and Interfaces / Packages / Visibility

- This also applies to structure fields. If a structure field name starts with a lowercase letter, only code within the same package will be able to access them. _(coding_little_go_book.pdf (source-range-23d24eb1-00300))_

### Chapter 4 - Code Organization and Interfaces / Interfaces

- It also tends to promote small and focused interfaces. The standard library is full of interfaces. The io package has a handful of popular ones such as io.Reader , io.Writer , and io.Closer . If you write a function that expects a parameter that you'll only be calling Close() on, you absolutely should accept an io.Closer rather than whatever concrete type you're using. _(coding_little_go_book.pdf (source-range-23d24eb1-00329))_


## Technical atoms

### Technical frame 1: Chapter 4 - Code Organization and Interfaces / Packages

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00277))_

> Notice that the name of the package is the same as the name of the folder. Also, obviously, we aren't actually accessing the database. We're just using this as an example to show how to organize code.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00276))_

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

### Technical frame 2: Chapter 4 - Code Organization and Interfaces / Packages

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00280))_

> It's tempting to think that importing shopping/db is somehow special because we're inside the shopping package/folder already. In reality, you're importing $GOPATH/src/shopping/db , which means you could just as easily import test/db so long as you had a package named db inside of your workspace's src/test folder.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00279))_

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

### Technical frame 3: Chapter 4 - Code Organization and Interfaces / Packages

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00281))_

> If you're building a package, you don't need anything more than what we've seen. To build an executable, you still need a main . The way I prefer to do this is to create a subfolder called main inside of shopping with a file called main.go and the following content:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00282))_

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

### Technical frame 4: Chapter 4 - Code Organization and Interfaces / Packages / Cyclical Imports

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00295))_

> pricecheck.go will still import shopping/db , but db.go will now import shopping/models instead of shopping , thus breaking the cycle. Since we moved the shared Item structure to shopping/models/item.go , we need to change shopping/db/db.go to reference the Item structure from models package:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00291))_

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

### Technical frame 5: Chapter 4 - Code Organization and Interfaces / Packages / Cyclical Imports

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00295))_

> pricecheck.go will still import shopping/db , but db.go will now import shopping/models instead of shopping , thus breaking the cycle. Since we moved the shared Item structure to shopping/models/item.go , we need to change shopping/db/db.go to reference the Item structure from models package:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00292))_

> Now when you try to run the code, you'll get a dreaded import cycle not allowed error.

### Technical frame 6: Chapter 4 - Code Organization and Interfaces / Packages / Cyclical Imports

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00295))_

> pricecheck.go will still import shopping/db , but db.go will now import shopping/models instead of shopping , thus breaking the cycle. Since we moved the shared Item structure to shopping/models/item.go , we need to change shopping/db/db.go to reference the Item structure from models package:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00294))_

```
- shopping
   pricecheck.go
   - db
     db.go
   - models
     item.go
   - main
     main.go
```

### Technical frame 7: Chapter 4 - Code Organization and Interfaces / Packages / Cyclical Imports

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00297))_

> You'll often need to share more than just models , so you might have other similar folders named utilities and such. The important rule about these shared packages is that they shouldn't import anything from the shopping package or any sub-packages. In a few sections, we'll look at interfaces which can help us untangle these types of dependencies.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00296))_

```
package db
import (
  "shopping/models"
)
func LoadItem(id int) *models.Item {
  return &models.Item{
    Price: 9.001,
  }
}
```

### Technical frame 8: Chapter 4 - Code Organization and Interfaces / Packages / Package Management

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00310))_

> We just talked about how to import packages that live in our workspace. To use our newly gotten go-sqlite3 package, we'd import it like so:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00311))_

```
import (
  "github.com/mattn/go-sqlite3"
)
```


## Related pages

- [[coding-little-go-book-code]] - shared statements: Code shares source evidence from Chapter 4 - Code Organization and Interfaces / Packages / Visibility: This also applies to structure fields. If a structure field name starts with a lowercase letter, only code within the same package will be able to access them. (1 shared statement(s))
- [[coding-little-go-book-notice]] - shared statements: Notice shares source evidence from Chapter 4 - Code Organization and Interfaces / Packages: Notice that the name of the package is the same as the name of the folder. Also, obviously, we aren't actually accessing the database. We're just using this as an ex ... [truncated] (1 shared statement(s))
- [[coding-little-go-book-structure]] - shared statements: Structure shares source evidence from Chapter 4 - Code Organization and Interfaces / Packages / Visibility: This also applies to structure fields. If a structure field name starts with a lowercase letter, only code within the same package will be able to access them. (1 shared statement(s))
- [[coding-little-go-book-section-chapter-4-code-organization-and-interfaces-packages-57d2c239]] - source section: Chapter 4 - Code Organization and Interfaces / Packages shares source evidence from Chapter 4 - Code Organization and Interfaces / Packages: Notice that the name of the package is the same as the name of the folder. Also, obviously, we aren't actually accessing the database. We're just using this as an ex ... [truncated]; Chapter 4 - Code Organization and Interfaces / Packages shares technical record from Chapter 4 - Code Organization and Interfaces / Packages: type Item struct { Price float64 } func LoadItem(id int) *Item { return &Item{ Price: 9.001, } } (31 shared statement(s), 14 shared atom(s))

## Source

- [[coding-little-go-book]]
