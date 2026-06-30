---
page_id: coding-little-go-book-section-chapter-4-code-organization-and-interfaces-packages-57d2c239
page_kind: source
summary: Chapter 4 - Code Organization and Interfaces / Packages: 52 source-backed entries and 8 atom(s) from raw/coding_little_go_book.pdf.
page_family: section-reference
sources: raw/coding_little_go_book.pdf
updated: 2026-06-30
domain: coding-little-go-book
category_path: sources/coding-little-go-book/sections
source_id: coding_little_go_book.pdf
projection_coverage: section-coding-little-go-book-section-chapter-4-code-organization-and-interfaces-packages-57d2c239@7586b0a37c3224ce2144e2046d3bcce0
---

# Chapter 4 - Code Organization and Interfaces / Packages

From [[coding-little-go-book]].

## Related pages

- [[coding-little-go-book-section-chapter-4-code-organization-and-interfaces-16681a63]] - broader source section: Chapter 4 - Code Organization and Interfaces
- [[coding-little-go-book-section-chapter-4-code-organization-and-interfaces-packages-cyclical-imports-bbcc282e]] - narrower source section: Chapter 4 - Code Organization and Interfaces / Packages / Cyclical Imports
- [[coding-little-go-book-section-chapter-4-code-organization-and-interfaces-packages-visibility-9acaaf15]] - narrower source section: Chapter 4 - Code Organization and Interfaces / Packages / Visibility
- [[coding-little-go-book-section-chapter-4-code-organization-and-interfaces-packages-package-management-ac6e6900]] - narrower source section: Chapter 4 - Code Organization and Interfaces / Packages / Package Management
- [[coding-little-go-book-section-chapter-4-code-organization-and-interfaces-packages-dependency-management-6bec99ea]] - narrower source section: Chapter 4 - Code Organization and Interfaces / Packages / Dependency Management
- [[coding-little-go-book-section-chapter-4-code-organization-and-interfaces-interfaces-ee136513]] - next source section: Chapter 4 - Code Organization and Interfaces / Interfaces

## Statements

- Notice that the name of the package is the same as the name of the folder. Also, obviously, we aren't actually accessing the database. We're just using this as an example to show how to organize code. _(coding_little_go_book.pdf (source-range-23d24eb1-00277))_
- Now, create a file called pricecheck.go inside of the main shopping folder. Its content is: _(coding_little_go_book.pdf (source-range-23d24eb1-00278))_
- It's tempting to think that importing shopping/db is somehow special because we're inside the shopping package/folder already. In reality, you're importing $GOPATH/src/shopping/db , which means you could just as easily import test/db so long as you had a package named db inside of your workspace's src/test folder. _(coding_little_go_book.pdf (source-range-23d24eb1-00280))_
- If you're building a package, you don't need anything more than what we've seen. To build an executable, you still need a main . The way I prefer to do this is to create a subfolder called main inside of shopping with a file called main.go and the following content: _(coding_little_go_book.pdf (source-range-23d24eb1-00281))_
- Now, create a file called pricecheck.go inside of the main shopping folder. _(coding_little_go_book.pdf (source-range-23d24eb1-00278))_
- It's tempting to think that importing shopping/db is somehow special because we're inside the shopping package/folder already. _(coding_little_go_book.pdf (source-range-23d24eb1-00280))_
- The way I prefer to do this is to create a subfolder called main inside of shopping with a file called main.go and the following content: _(coding_little_go_book.pdf (source-range-23d24eb1-00281))_

## Statements by subsection

### Chapter 4 - Code Organization and Interfaces / Packages / Cyclical Imports

- As you start writing more complex systems, you're bound to run into cyclical imports. This happens when package A imports package B but package B imports package A (either directly or indirectly through another package). This is something the compiler won't allow. _(coding_little_go_book.pdf (source-range-23d24eb1-00286))_
- If you try to run the code, you'll get a couple of errors from db/db.go about Item being undefined. This makes sense. Item no longer exists in the db package; it's been moved to the shopping package. We need to change shopping/db/db.go to: _(coding_little_go_book.pdf (source-range-23d24eb1-00290))_
- pricecheck.go will still import shopping/db , but db.go will now import shopping/models instead of shopping , thus breaking the cycle. Since we moved the shared Item structure to shopping/models/item.go , we need to change shopping/db/db.go to reference the Item structure from models package: _(coding_little_go_book.pdf (source-range-23d24eb1-00295))_
- You'll often need to share more than just models , so you might have other similar folders named utilities and such. The important rule about these shared packages is that they shouldn't import anything from the shopping package or any sub-packages. In a few sections, we'll look at interfaces which can help us untangle these types of dependencies. _(coding_little_go_book.pdf (source-range-23d24eb1-00297))_
- pricecheck.go will still import shopping/db , but db.go will now import shopping/models instead of shopping , thus breaking the cycle. _(coding_little_go_book.pdf (source-range-23d24eb1-00295))_

### Chapter 4 - Code Organization and Interfaces / Packages / Visibility

- Go uses a simple rule to define what types and functions are visible outside of a package. If the name of the type or function starts with an uppercase letter, it's visible. If it starts with a lowercase letter, it isn't. _(coding_little_go_book.pdf (source-range-23d24eb1-00299))_
- This also applies to structure fields. If a structure field name starts with a lowercase letter, only code within the same package will be able to access them. _(coding_little_go_book.pdf (source-range-23d24eb1-00300))_
- it could be called via models.NewItem() . But if the function was named newItem , we wouldn't be able to access it from a different package. _(coding_little_go_book.pdf (source-range-23d24eb1-00303))_
- If a structure field name starts with a lowercase letter, only code within the same package will be able to access them. _(coding_little_go_book.pdf (source-range-23d24eb1-00300))_

### Chapter 4 - Code Organization and Interfaces / Packages / Package Management

- The go command we've been using to run and build has a get subcommand which is used to fetch third-party libraries. go get supports various protocols but for this example, we'll be getting a library from Github, meaning, you'll need git installed on your computer. _(coding_little_go_book.pdf (source-range-23d24eb1-00306))_
- Assuming you already have git installed, from a shell/command prompt, enter: _(coding_little_go_book.pdf (source-range-23d24eb1-00307))_
- go get fetches the remote files and stores them in your workspace. Go ahead and check your $GOPATH/src . In addition to the shopping project that we created, you'll now see a github.com folder. Within, you'll see a mattn folder which contains a go-sqlite3 folder. _(coding_little_go_book.pdf (source-range-23d24eb1-00309))_
- We just talked about how to import packages that live in our workspace. To use our newly gotten go-sqlite3 package, we'd import it like so: _(coding_little_go_book.pdf (source-range-23d24eb1-00310))_
- Within, you'll see a mattn folder which contains a go-sqlite3 folder. _(coding_little_go_book.pdf (source-range-23d24eb1-00309))_

### Chapter 4 - Code Organization and Interfaces / Packages / Dependency Management

- go get has a couple of other tricks up its sleeve. If we go get within a project, it'll scan all the files, looking for imports to third-party libraries and will download them. In a way, our own source code becomes a Gemfile or package.json . _(coding_little_go_book.pdf (source-range-23d24eb1-00314))_
- Eventually, you might find go get inadequate. For one thing, there's no way to specify a revision, it always points to the master/head/trunk/default. This is an even larger problem if you have two projects needing different versions of the same library. _(coding_little_go_book.pdf (source-range-23d24eb1-00316))_
- To solve this, you can use a third-party dependency management tool. They are still young, but two promising ones are goop and godep. A more complete list is available at the go-wiki. _(coding_little_go_book.pdf (source-range-23d24eb1-00317))_

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
