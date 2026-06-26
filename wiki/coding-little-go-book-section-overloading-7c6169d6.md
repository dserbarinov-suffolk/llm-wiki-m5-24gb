---
page_id: coding-little-go-book-section-overloading-7c6169d6
page_kind: source
summary: Overloading: 3 source-backed entries and 3 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: sources/coding-little-go-book/sections
source_id: coding_little_go_book.pdf
projection_coverage: section-coding-little-go-book-section-overloading-7c6169d6@d9f2fbc22c8aefcd0c313477886aaacb
---

# Overloading

From [[coding-little-go-book]].

## Technical atoms

> However, because implicit composition is really just a compiler trick, we can "overwrite" the functions of a composed type. For example, our Saiyan structure can have its own Introduce function:
_(source: coding_little_go_book.pdf (source-range-810ce361-00170))_

```
func (s	*Saiyan)	Introduce()	{ fmt.Printf("Hi,	I'm	%s.	Ya!\n",	s.Name) }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00171))_

> The composed version is always available via s.Person.Introduce() .
_(source: coding_little_go_book.pdf (source-range-810ce361-00172))_
