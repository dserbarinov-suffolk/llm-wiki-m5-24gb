---
page_id: coding-little-go-book-code-organization
page_kind: concept
summary: Code Organization: 5 statement(s) and 5 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-29
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-code-organization@18f3861aa4c85dcaf0a19b0b131d9b7e
---

# Code Organization

What [[coding-little-go-book]] covers about code organization:

## Statements

### Chapter 4 - Code Organization and Interfaces / Packages

- Notice that the name of the package is the same as the name of the folder. Also, obviously, we aren't actually accessing the database. We're just using this as an example to show how to organize code. _(coding_little_go_book.pdf (source-range-23d24eb1-00277))_

### Chapter 4 - Code Organization and Interfaces / Packages / Visibility

- This also applies to structure fields. If a structure field name starts with a lowercase letter, only code within the same package will be able to access them. _(coding_little_go_book.pdf (source-range-23d24eb1-00300))_

### Chapter 4 - Code Organization and Interfaces / Packages / Dependency Management

- go get has a couple of other tricks up its sleeve. If we go get within a project, it'll scan all the files, looking for imports to third-party libraries and will download them. In a way, our own source code becomes a Gemfile or package.json . _(coding_little_go_book.pdf (source-range-23d24eb1-00314))_

### Chapter 4 - Code Organization and Interfaces / Interfaces

- Yet by programming against the interface, rather than these concrete implementations, we can easily change (and test) which we use without any impact to our code. _(coding_little_go_book.pdf (source-range-23d24eb1-00323))_

### Chapter 4 - Code Organization and Interfaces / Before You Continue

- Ultimately, how you structure your code around Go's workspace is something that you'll only feel comfortable with after you've written a couple of non-trivial projects. What's most important for you to remember is the tight relationship between package names and your directory structure (not just within a project, but within the entire workspace). _(coding_little_go_book.pdf (source-range-23d24eb1-00333))_


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

### Technical frame 2: Chapter 4 - Code Organization and Interfaces / Packages / Cyclical Imports

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

### Technical frame 3: Chapter 4 - Code Organization and Interfaces / Packages / Cyclical Imports

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00295))_

> pricecheck.go will still import shopping/db , but db.go will now import shopping/models instead of shopping , thus breaking the cycle. Since we moved the shared Item structure to shopping/models/item.go , we need to change shopping/db/db.go to reference the Item structure from models package:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00292))_

> Now when you try to run the code, you'll get a dreaded import cycle not allowed error.

### Technical frame 4: Chapter 4 - Code Organization and Interfaces / Packages / Cyclical Imports

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

### Technical frame 5: Chapter 4 - Code Organization and Interfaces / Interfaces

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00323))_

> Yet by programming against the interface, rather than these concrete implementations, we can easily change (and test) which we use without any impact to our code.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00322))_

```
type SqlLogger struct { ... }
type ConsoleLogger struct { ... }
type FileLogger struct { ... }
```


## Related pages

- [[coding-little-go-book-code]] - broader topic: Code shares source evidence from Chapter 4 - Code Organization and Interfaces / Packages / Visibility: This also applies to structure fields. If a structure field name starts with a lowercase letter, only code within the same package will be able to access them. (3 shared statement(s))
- [[coding-little-go-book-code-organization-and-interface]] - narrower topic: Code Organization and Interfaces shares source evidence from Chapter 4 - Code Organization and Interfaces / Packages: Notice that the name of the package is the same as the name of the folder. Also, obviously, we aren't actually accessing the database. We're just using this as an ex ... [truncated]; Code Organization and Interfaces shares technical record from Chapter 4 - Code Organization and Interfaces / Packages: type Item struct { Price float64 } func LoadItem(id int) *Item { return &Item{ Price: 9.001, } } (5 shared statement(s), 5 shared atom(s))
- [[coding-little-go-book-package]] - shared statements and technical atoms: Packages shares source evidence from Chapter 4 - Code Organization and Interfaces / Packages: Notice that the name of the package is the same as the name of the folder. Also, obviously, we aren't actually accessing the database. We're just using this as an ex ... [truncated]; Packages shares technical record from Chapter 4 - Code Organization and Interfaces / Packages: type Item struct { Price float64 } func LoadItem(id int) *Item { return &Item{ Price: 9.001, } } (3 shared statement(s), 4 shared atom(s))
- [[coding-little-go-book-interface]] - shared statements and technical atoms: Interfaces shares source evidence from Chapter 4 - Code Organization and Interfaces / Interfaces: Yet by programming against the interface, rather than these concrete implementations, we can easily change (and test) which we use without any impact to our code.; Interfaces shares technical record from Chapter 4 - Code Organization and Interfaces / Interfaces: type SqlLogger struct { ... } type ConsoleLogger struct { ... } type FileLogger struct { ... } (1 shared statement(s), 1 shared atom(s))
- [[coding-little-go-book-cyclical-import]] - shared technical atoms: Cyclical Imports shares technical record from Chapter 4 - Code Organization and Interfaces / Packages / Cyclical Imports: package db import ( "shopping" ) func LoadItem(id int) *shopping.Item { return &shopping.Item{ Price: 9.001, } } (3 shared atom(s))

## Source

- [[coding-little-go-book]]
