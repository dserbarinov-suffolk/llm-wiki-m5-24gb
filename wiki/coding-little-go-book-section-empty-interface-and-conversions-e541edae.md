---
page_id: coding-little-go-book-section-empty-interface-and-conversions-e541edae
page_kind: source
summary: Empty Interface and Conversions: 10 source-backed entries and 3 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: sources/coding-little-go-book/sections
source_id: coding_little_go_book.pdf
projection_coverage: section-coding-little-go-book-section-empty-interface-and-conversions-e541edae@95f8a25439197f29b4d0b4027150da4b
---

# Empty Interface and Conversions

From [[coding-little-go-book]].

## Statements

- Go, having no inheritance, doesn't have such a superclass. _(coding_little_go_book.pdf (source-range-810ce361-00368))_
- Since every type implements all 0 of the empty interface's methods, and since interfaces are implicitly implemented, every type fulfills the contract of the empty interface. _(coding_little_go_book.pdf (source-range-810ce361-00368))_
- In most object-oriented languages, a built-in base class, often named object , is the superclass for all other classes. _(coding_little_go_book.pdf (source-range-810ce361-00368))_
- Note that if the underlying type is not int , the above will result in an error. _(coding_little_go_book.pdf (source-range-810ce361-00373))_
- Converting values back and forth is ugly and dangerous but sometimes, in a static language, it's the only choice. _(coding_little_go_book.pdf (source-range-810ce361-00376))_
- You'll see and probably use the empty interface more than you might first expect. _(coding_little_go_book.pdf (source-range-810ce361-00376))_
- Converting values back and forth is ugly and dangerous but sometimes, in a static language, it's the only choice. _(coding_little_go_book.pdf (source-range-810ce361-00376))_

## Technical atoms

```
func add(a interface {},	b interface {}) interface {}	{ ... }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00370))_

```
return a.(int)	+	b.(int)
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00372))_

```
switch a.( type )	{ case int: fmt.Printf("a	is	now	an	int	and	equals	%d\n",	a) case bool,	string: //	... default : //	... }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00375))_
