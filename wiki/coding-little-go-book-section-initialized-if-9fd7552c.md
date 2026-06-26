---
page_id: coding-little-go-book-section-initialized-if-9fd7552c
page_kind: source
summary: Initialized If: 6 source-backed entries and 2 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: sources/coding-little-go-book/sections
source_id: coding_little_go_book.pdf
projection_coverage: section-coding-little-go-book-section-initialized-if-9fd7552c@1d71ec9c830c501269856a38bc80c9c5
---

# Initialized If

From [[coding-little-go-book]].

## Statements

- Go supports a slightly modified if-statement, one where a value can be initiated prior to the condition being evaluated: _(coding_little_go_book.pdf (source-range-810ce361-00362))_
- Go supports a slightly modified if-statement, one where a value can be initiated prior to the condition being evaluated: _(coding_little_go_book.pdf (source-range-810ce361-00362))_
- Interestingly, while the values aren't available outside the ifstatement, they are available inside any else if or else . _(coding_little_go_book.pdf (source-range-810ce361-00366))_
- Interestingly, while the values aren't available outside the ifstatement, they are available inside any else if or else . _(coding_little_go_book.pdf (source-range-810ce361-00366))_

## Technical atoms

```
if x	:=	10;	count	>	x	{ ... }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00363))_

```
if err	:=	process();	err	!=	nil	{ return err }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00365))_
