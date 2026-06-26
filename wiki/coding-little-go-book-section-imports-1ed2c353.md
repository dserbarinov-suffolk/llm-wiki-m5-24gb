---
page_id: coding-little-go-book-section-imports-1ed2c353
page_kind: source
summary: Imports: 22 source-backed entries and 7 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: sources/coding-little-go-book/sections
source_id: coding_little_go_book.pdf
projection_coverage: section-coding-little-go-book-section-imports-1ed2c353@a232175217091b6d3e77140849e344ff
---

# Imports

From [[coding-little-go-book]].

## Statements

- Go has a number of built-in functions, such as println , which can be used without reference. _(coding_little_go_book.pdf (source-range-810ce361-00058))_
- We can't get very far though, without making use of Go's standard library and eventually using third-party libraries. _(coding_little_go_book.pdf (source-range-810ce361-00058))_
- Go has a number of built-in functions, such as println , which can be used without reference. _(coding_little_go_book.pdf (source-range-810ce361-00058))_
- We've also introduced another built-in function len . _(coding_little_go_book.pdf (source-range-810ce361-00063))_
- You've probably noticed we prefix the function name with the package, e.g., fmt.Println . _(coding_little_go_book.pdf (source-range-810ce361-00064))_
- For now, knowing how to import and use a package is a good start. _(coding_little_go_book.pdf (source-range-810ce361-00064))_
- This is different from many other languages. _(coding_little_go_book.pdf (source-range-810ce361-00064))_
- It will not compile if you import a package but don't use it. _(coding_little_go_book.pdf (source-range-810ce361-00065))_
- Go is strict about importing packages. _(coding_little_go_book.pdf (source-range-810ce361-00065))_
- Over time, you'll get used to it (it'll still be annoying though). _(coding_little_go_book.pdf (source-range-810ce361-00067))_
- Go is strict about this because unused imports can slow compilation; admittedly a problem most of us don't have to this degree. _(coding_little_go_book.pdf (source-range-810ce361-00067))_
- Go is strict about this because unused imports can slow compilation; admittedly a problem most of us don't have to this degree. _(coding_little_go_book.pdf (source-range-810ce361-00067))_
- You can click on that section header and see the source code. _(coding_little_go_book.pdf (source-range-810ce361-00068))_
- Another thing to note is that Go's standard library is well documented. _(coding_little_go_book.pdf (source-range-810ce361-00068))_
- If you're ever stuck without internet access, you can get the documentation running locally via: _(coding_little_go_book.pdf (source-range-810ce361-00069))_

## Technical atoms

> [Figure] (p.7)
_(source: coding_little_go_book.pdf (source-range-810ce361-00059))_

```
func main()	{ if len(os.Args)	!=	2	{ os.Exit(1) } fmt.Println("It's	over",	os.Args[1]) }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00060))_

```
go	run	main.go	9000
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00062))_

> If you're wondering why we expect 2 arguments, it's because the first argument -- at index 0 -- is always the path of the currently running executable.
_(source: coding_little_go_book.pdf (source-range-810ce361-00063))_

```
package main import ( "fmt" "os" ) func main()	{ }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00066))_

> You should get two errors about fmt and os being imported and not used.
_(source: coding_little_go_book.pdf (source-range-810ce361-00067))_

```
godoc	-http=:6060
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00070))_
