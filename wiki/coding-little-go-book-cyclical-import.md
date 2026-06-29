---
page_id: coding-little-go-book-cyclical-import
page_kind: concept
summary: Cyclical Imports: 7 statement(s) and 6 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-29
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-cyclical-import@c1cafbcaca0afb76540c457dc625f7fa
---

# Cyclical Imports

What [[coding-little-go-book]] covers about cyclical imports:

## Statements

### Chapter 4 - Code Organization and Interfaces / Packages / Cyclical Imports

- As you start writing more complex systems, you're bound to run into cyclical imports. This happens when package A imports package B but package B imports package A (either directly or indirectly through another package). This is something the compiler won't allow. _(coding_little_go_book.pdf (source-range-23d24eb1-00286))_

- If you try to run the code, you'll get a couple of errors from db/db.go about Item being undefined. This makes sense. Item no longer exists in the db package; it's been moved to the shopping package. We need to change shopping/db/db.go to: _(coding_little_go_book.pdf (source-range-23d24eb1-00290))_

- pricecheck.go will still import shopping/db , but db.go will now import shopping/models instead of shopping , thus breaking the cycle. Since we moved the shared Item structure to shopping/models/item.go , we need to change shopping/db/db.go to reference the Item structure from models package: _(coding_little_go_book.pdf (source-range-23d24eb1-00295))_

- You'll often need to share more than just models , so you might have other similar folders named utilities and such. The important rule about these shared packages is that they shouldn't import anything from the shopping package or any sub-packages. In a few sections, we'll look at interfaces which can help us untangle these types of dependencies. _(coding_little_go_book.pdf (source-range-23d24eb1-00297))_


## Technical atoms

### Technical frame 1: Chapter 4 - Code Organization and Interfaces / Packages / Cyclical Imports

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00290))_

> If you try to run the code, you'll get a couple of errors from db/db.go about Item being undefined. This makes sense. Item no longer exists in the db package; it's been moved to the shopping package. We need to change shopping/db/db.go to:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00289))_

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

### Technical frame 2: Chapter 4 - Code Organization and Interfaces / Packages / Cyclical Imports

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00295))_

> pricecheck.go will still import shopping/db , but db.go will now import shopping/models instead of shopping , thus breaking the cycle. Since we moved the shared Item structure to shopping/models/item.go , we need to change shopping/db/db.go to reference the Item structure from models package:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00290))_

> If you try to run the code, you'll get a couple of errors from db/db.go about Item being undefined.

### Technical frame 3: Chapter 4 - Code Organization and Interfaces / Packages / Cyclical Imports

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

### Technical frame 4: Chapter 4 - Code Organization and Interfaces / Packages / Cyclical Imports

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00295))_

> pricecheck.go will still import shopping/db , but db.go will now import shopping/models instead of shopping , thus breaking the cycle. Since we moved the shared Item structure to shopping/models/item.go , we need to change shopping/db/db.go to reference the Item structure from models package:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00292))_

> Now when you try to run the code, you'll get a dreaded import cycle not allowed error.

### Technical frame 5: Chapter 4 - Code Organization and Interfaces / Packages / Cyclical Imports

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

### Technical frame 6: Chapter 4 - Code Organization and Interfaces / Packages / Cyclical Imports

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


## Related pages

- [[coding-little-go-book-code-organization-and-interface]] - shared statements and technical atoms: Code Organization and Interfaces shares source evidence from Chapter 4 - Code Organization and Interfaces / Packages / Cyclical Imports: As you start writing more complex systems, you're bound to run into cyclical imports. This happens when package A imports package B but package B imports package A ( ... [truncated]; Code Organization and Interfaces shares technical record from Chapter 4 - Code Organization and Interfaces / Packages / Cyclical Imports: package shopping import ( "shopping/db" ) type Item struct { Price float64 } func PriceCheck(itemId int) (float64, bool) { item := db.LoadItem(itemId) if item == nil ... [truncated] (7 shared statement(s), 6 shared atom(s))
- [[coding-little-go-book-package]] - shared statements and technical atoms: Packages shares source evidence from Chapter 4 - Code Organization and Interfaces / Packages / Cyclical Imports: As you start writing more complex systems, you're bound to run into cyclical imports. This happens when package A imports package B but package B imports package A ( ... [truncated]; Packages shares technical record from Chapter 4 - Code Organization and Interfaces / Packages / Cyclical Imports: package shopping import ( "shopping/db" ) type Item struct { Price float64 } func PriceCheck(itemId int) (float64, bool) { item := db.LoadItem(itemId) if item == nil ... [truncated] (7 shared statement(s), 6 shared atom(s))
- [[coding-little-go-book-code-organization]] - shared technical atoms: Code Organization shares technical record from Chapter 4 - Code Organization and Interfaces / Packages / Cyclical Imports: package db import ( "shopping" ) func LoadItem(id int) *shopping.Item { return &shopping.Item{ Price: 9.001, } } (3 shared atom(s))
- [[coding-little-go-book-section-chapter-4-code-organization-and-interfaces-packages-cyclical-imports-bbcc282e]] - source section: Chapter 4 - Code Organization and Interfaces / Packages / Cyclical Imports shares source evidence from Chapter 4 - Code Organization and Interfaces / Packages / Cyclical Imports: As you start writing more complex systems, you're bound to run into cyclical imports. This happens when package A imports package B but package B imports package A ( ... [truncated]; Chapter 4 - Code Organization and Interfaces / Packages / Cyclical Imports shares technical record from Chapter 4 - Code Organization and Interfaces / Packages / Cyclical Imports: package shopping import ( "shopping/db" ) type Item struct { Price float64 } func PriceCheck(itemId int) (float64, bool) { item := db.LoadItem(itemId) if item == nil ... [truncated] (7 shared statement(s), 6 shared atom(s))

## Source

- [[coding-little-go-book]]
