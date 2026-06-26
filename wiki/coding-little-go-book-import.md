---
page_id: coding-little-go-book-import
page_kind: concept
summary: Imports: 12 statement(s) and 26 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-import@c65a8940341aa143daaed8f202ca4837
---

# Imports

What [[coding-little-go-book]] covers about imports:

## Statements

- Go is strict about importing packages. _(coding_little_go_book.pdf (source-range-810ce361-00064))_
- It will not compile if you import a package but don't use it. _(coding_little_go_book.pdf (source-range-810ce361-00064))_
- Finally, interfaces are commonly used to avoid cyclical imports. _(coding_little_go_book.pdf (source-range-810ce361-00330))_
- We just talked about how to import packages that live in our workspace. _(coding_little_go_book.pdf (source-range-810ce361-00309))_
- There are a few interesting things going on here, but the most important is how we start a goroutine. _(coding_little_go_book.pdf (source-range-810ce361-00401))_
- It does more than indent your code; it also aligns field declarations and alphabetically orders imports. _(coding_little_go_book.pdf (source-range-810ce361-00359))_
- It's important that you remember that := is used to declare the variable as well as assign a value to it. _(coding_little_go_book.pdf (source-range-810ce361-00082))_
- It's tempting to think that importing shopping/db is somehow special because we're inside the shopping package/folder already. _(coding_little_go_book.pdf (source-range-810ce361-00279))_
- Go is strict about this because unused imports can slow compilation; admittedly a problem most of us don't have to this degree. _(coding_little_go_book.pdf (source-range-810ce361-00066))_
- The important rule about these shared packages is that they shouldn't import anything from the shopping package or any sub-packages. _(coding_little_go_book.pdf (source-range-810ce361-00296))_
- pricecheck.go will still import shopping/db , but db.go will now import shopping/models instead of shopping , thus breaking the cycle. _(coding_little_go_book.pdf (source-range-810ce361-00294))_
- What's most important for you to remember is the tight relationship between package names and your directory structure (not just within a project, but within the entire workspace). _(coding_little_go_book.pdf (source-range-810ce361-00332))_

## Code, rules, and examples

> You've probably noticed we prefix the function name with the package, e.g., fmt.Println . This is different from many other languages. We'll learn more about packages in later chapters. For now, knowing how to import and use a package is a good start.
_(source: coding_little_go_book.pdf (source-range-810ce361-00063))_

```
package main import ( "fmt" "os" ) func main()	{ }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00065))_

> You should get two errors about fmt and os being imported and not used.
_(source: coding_little_go_book.pdf (source-range-810ce361-00066))_

```
package main import ( "fmt" ) func main()	{ var power	int power	=	9000 fmt.Printf("It's	over	%d\n",	power) }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00075))_

> For now, the last thing to know is that, like imports, Go won't let you have unused variables. For example,
_(source: coding_little_go_book.pdf (source-range-810ce361-00090))_

```
import ( "fmt" "math/rand" "sort" ) func main()	{ scores	:=	make([]int,	100) for i	:=	0;	i	<	100;	i++	{ scores[i]	=	int(rand.Int31n(1000)) } sort.Ints(scores) worst	:=	make([]int,	5) copy(worst,	scores[:5]) fmt.Println(worst) }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00244))_


## Source

- [[coding-little-go-book]]
