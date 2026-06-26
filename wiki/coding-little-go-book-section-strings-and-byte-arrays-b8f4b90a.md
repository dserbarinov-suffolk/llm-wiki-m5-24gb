---
page_id: coding-little-go-book-section-strings-and-byte-arrays-b8f4b90a
page_kind: source
summary: Strings and Byte Arrays: 12 source-backed entries and 5 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: sources/coding-little-go-book/sections
source_id: coding_little_go_book.pdf
projection_coverage: section-coding-little-go-book-section-strings-and-byte-arrays-b8f4b90a@2912206e1d04f34021421de850cb781c
---

# Strings and Byte Arrays

From [[coding-little-go-book]].

## Statements

- Strings and byte arrays are closely related. _(coding_little_go_book.pdf (source-range-773b6275-00378))_
- In fact, this way of converting is common across various types as well. _(coding_little_go_book.pdf (source-range-773b6275-00380))_
- Some functions explicitly expect an int32 or an int64 or their unsigned counterparts. _(coding_little_go_book.pdf (source-range-773b6275-00380))_
- Still, when it comes to bytes and strings, it's probably something you'll end up doing often. _(coding_little_go_book.pdf (source-range-773b6275-00382))_
- This is necessary because strings are immutable. _(coding_little_go_book.pdf (source-range-773b6275-00382))_
- This is necessary because strings are immutable. _(coding_little_go_book.pdf (source-range-773b6275-00382))_
- Strings are made of runes which are unicode code points. _(coding_little_go_book.pdf (source-range-773b6275-00383))_

## Technical atoms

```
stra := "the spice must flow"
byts := []byte(stra)
strb := string(byts)
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00379))_

```
int64(count)
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00381))_

> If you take the length of a string, you might not get what you expect.
_(source: coding_little_go_book.pdf (source-range-773b6275-00383))_

```
fmt.Println(len("椒"))
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00384))_

> If you iterate over a string using range , you'll get runes, not bytes.
_(source: coding_little_go_book.pdf (source-range-773b6275-00385))_
