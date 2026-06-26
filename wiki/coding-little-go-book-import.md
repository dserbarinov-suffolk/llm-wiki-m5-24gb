---
page_id: coding-little-go-book-import
page_kind: concept
summary: Imports: 14 statement(s) and 22 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-import@8a5be836a85034949c1bfd645a1ce1b3
---

# Imports

What [[coding-little-go-book]] covers about imports:

## Statements

- Go is strict about importing packages. _(coding_little_go_book.pdf (source-range-810ce361-00065))_
- It will not compile if you import a package but don't use it. _(coding_little_go_book.pdf (source-range-810ce361-00065))_
- Finally, interfaces are commonly used to avoid cyclical imports. _(coding_little_go_book.pdf (source-range-810ce361-00331))_
- For now, knowing how to import and use a package is a good start. _(coding_little_go_book.pdf (source-range-810ce361-00064))_
- We just talked about how to import packages that live in our workspace. _(coding_little_go_book.pdf (source-range-810ce361-00310))_
- For now, the last thing to know is that, like imports, Go won't let you have unused variables. _(coding_little_go_book.pdf (source-range-810ce361-00091))_
- There are a few interesting things going on here, but the most important is how we start a goroutine. _(coding_little_go_book.pdf (source-range-810ce361-00402))_
- It does more than indent your code; it also aligns field declarations and alphabetically orders imports. _(coding_little_go_book.pdf (source-range-810ce361-00360))_
- It's important that you remember that := is used to declare the variable as well as assign a value to it. _(coding_little_go_book.pdf (source-range-810ce361-00083))_
- It's tempting to think that importing shopping/db is somehow special because we're inside the shopping package/folder already. _(coding_little_go_book.pdf (source-range-810ce361-00280))_
- Go is strict about this because unused imports can slow compilation; admittedly a problem most of us don't have to this degree. _(coding_little_go_book.pdf (source-range-810ce361-00067))_
- The important rule about these shared packages is that they shouldn't import anything from the shopping package or any sub-packages. _(coding_little_go_book.pdf (source-range-810ce361-00297))_
- pricecheck.go will still import shopping/db , but db.go will now import shopping/models instead of shopping , thus breaking the cycle. _(coding_little_go_book.pdf (source-range-810ce361-00295))_
- What's most important for you to remember is the tight relationship between package names and your directory structure (not just within a project, but within the entire workspace). _(coding_little_go_book.pdf (source-range-810ce361-00333))_

## Technical atoms

```
package main import ( "fmt" "os" ) func main()	{ }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00066))_

> You should get two errors about fmt and os being imported and not used.
_(source: coding_little_go_book.pdf (source-range-810ce361-00067))_

```
package main import ( "fmt" ) func main()	{ var power	int power	=	9000 fmt.Printf("It's	over	%d\n",	power) }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00076))_

```
import ( "fmt" "math/rand" "sort" ) func main()	{ scores	:=	make([]int,	100) for i	:=	0;	i	<	100;	i++	{ scores[i]	=	int(rand.Int31n(1000)) } sort.Ints(scores) worst	:=	make([]int,	5) copy(worst,	scores[:5]) fmt.Println(worst) }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00245))_

> To keep more complicated libraries and systems organized, we need to learn about packages. In Go, package names follow the directory structure of your Go workspace. If we were building a shopping system, we'd probably start with a package name "shopping" and put our source files in $GOPATH/src/shopping/ . We don't want to put everything inside this folder though. For example, maybe we want to isolate some database logic inside its own folder. To achieve this, we create a subfolder at $GOPATH/src/shopping/db . The package name of the files within this subfolder is simply db , but to access it from another package, including the shopping package, we need to import shopping/db . In other words, when you name a package, via the package keyword, you provide a single value, not a complete hierarchy (e.g., "shopping" or "db"). When you import a package, you specify the complete path. Let's try it. Inside your Go workspace's src folder (which we set up in Getting Started of the Introduction), create a new folder called shopping and a subfolder within it called db . Inside of shopping/db , create a file called db.go and add the following code:
_(source: coding_little_go_book.pdf (source-range-810ce361-00274))_

```
package shopping import ( "shopping/db" ) func PriceCheck(itemId	int)	(float64,	bool)	{ item	:=	db.LoadItem(itemId) if item	==	nil	{ return 0,	false } return item.Price,	true }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00279))_


## Source

- [[coding-little-go-book]]
