---
page_id: coding-little-go-book-string-and-byte-array
page_kind: concept
summary: Strings and Byte Arrays: 6 statement(s) and 5 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-string-and-byte-array@cda7dafe1ee47d4e480061d34a9b6302
---

# Strings and Byte Arrays

What [[coding-little-go-book]] covers about strings and byte arrays:

## Statements

- Strings and byte arrays are closely related. _(coding_little_go_book.pdf (source-range-773b6275-00378))_
- Still, when it comes to bytes and strings, it's probably something you'll end up doing often. _(coding_little_go_book.pdf (source-range-773b6275-00382))_
- Strings are made of runes which are unicode code points. _(coding_little_go_book.pdf (source-range-773b6275-00383))_
- This is necessary because strings are immutable. _(coding_little_go_book.pdf (source-range-773b6275-00382))_
- In fact, this way of converting is common across various types as well. _(coding_little_go_book.pdf (source-range-773b6275-00380))_
- Some functions explicitly expect an int32 or an int64 or their unsigned counterparts. _(coding_little_go_book.pdf (source-range-773b6275-00380))_

## Technical atoms

> Context: Strings and byte arrays are closely related. We can easily convert one to the other:
_(context: coding_little_go_book.pdf (source-range-773b6275-00378))_

```
stra := "the spice must flow"
byts := []byte(stra)
strb := string(byts)
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00379))_

> Context: In fact, this way of converting is common across various types as well. Some functions explicitly expect an int32 or an int64 or their unsigned counterparts. You might find yourself having to do things like: Still, when it comes to bytes and strings, it's probably something you'll end up doing often. Do note that when you use []byte(X) or string(X) , you're creating a copy of the data. This is necessary because strings are immutable.
_(context: coding_little_go_book.pdf (source-range-773b6275-00380, source-range-773b6275-00382))_

```
int64(count)
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00381))_

> Context: Still, when it comes to bytes and strings, it's probably something you'll end up doing often. Do note that when you use []byte(X) or string(X) , you're creating a copy of the data. This is necessary because strings are immutable.
_(context: coding_little_go_book.pdf (source-range-773b6275-00382))_

> If you take the length of a string, you might not get what you expect.
_(source: coding_little_go_book.pdf (source-range-773b6275-00383))_

> Context: Strings are made of runes which are unicode code points. If you take the length of a string, you might not get what you expect. The following prints 3:
_(context: coding_little_go_book.pdf (source-range-773b6275-00383))_

```
fmt.Println(len("椒"))
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00384))_

> Context: Strings are made of runes which are unicode code points. If you take the length of a string, you might not get what you expect. The following prints 3:
_(context: coding_little_go_book.pdf (source-range-773b6275-00383))_

> If you iterate over a string using range , you'll get runes, not bytes.
_(source: coding_little_go_book.pdf (source-range-773b6275-00385))_


## Source

- [[coding-little-go-book]]
