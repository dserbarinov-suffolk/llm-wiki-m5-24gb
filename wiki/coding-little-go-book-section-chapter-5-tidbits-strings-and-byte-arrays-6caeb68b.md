---
page_id: coding-little-go-book-section-chapter-5-tidbits-strings-and-byte-arrays-6caeb68b
page_kind: source
summary: Chapter 5 - Tidbits / Strings and Byte Arrays: 12 source-backed entries and 3 atom(s) from raw/coding_little_go_book.pdf.
page_family: section-reference
sources: raw/coding_little_go_book.pdf
updated: 2026-06-30
domain: coding-little-go-book
category_path: sources/coding-little-go-book/sections
source_id: coding_little_go_book.pdf
projection_coverage: section-coding-little-go-book-section-chapter-5-tidbits-strings-and-byte-arrays-6caeb68b@c39685ae692f4cd70ea54f3f35c272a9
---

# Chapter 5 - Tidbits / Strings and Byte Arrays

From [[coding-little-go-book]].

## Related pages

- [[coding-little-go-book-section-chapter-5-tidbits-e7a41f7c]] - broader source section: Chapter 5 - Tidbits
- [[coding-little-go-book-section-chapter-5-tidbits-empty-interface-and-conversions-c4483a93]] - previous source section: Chapter 5 - Tidbits / Empty Interface and Conversions
- [[coding-little-go-book-section-chapter-5-tidbits-function-type-561f81dd]] - next source section: Chapter 5 - Tidbits / Function Type

## Statements

- Strings and byte arrays are closely related. We can easily convert one to the other: _(coding_little_go_book.pdf (source-range-23d24eb1-00378))_
- In fact, this way of converting is common across various types as well. Some functions explicitly expect an int32 or an int64 or their unsigned counterparts. You might find yourself having to do things like: _(coding_little_go_book.pdf (source-range-23d24eb1-00380))_
- Still, when it comes to bytes and strings, it's probably something you'll end up doing often. Do note that when you use []byte(X) or string(X) , you're creating a copy of the data. This is necessary because strings are immutable. _(coding_little_go_book.pdf (source-range-23d24eb1-00382))_
- Strings are made of runes which are unicode code points. If you take the length of a string, you might not get what you expect. The following prints 3: _(coding_little_go_book.pdf (source-range-23d24eb1-00383))_
- This is necessary because strings are immutable. _(coding_little_go_book.pdf (source-range-23d24eb1-00382))_

## Technical atoms

### Technical frame 1: Chapter 5 - Tidbits / Strings and Byte Arrays

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00380))_

> In fact, this way of converting is common across various types as well. Some functions explicitly expect an int32 or an int64 or their unsigned counterparts. You might find yourself having to do things like:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00379))_

```
stra := "the spice must flow"
byts := []byte(stra)
strb := string(byts)
```

### Technical frame 2: Chapter 5 - Tidbits / Strings and Byte Arrays

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00382))_

> Still, when it comes to bytes and strings, it's probably something you'll end up doing often. Do note that when you use []byte(X) or string(X) , you're creating a copy of the data. This is necessary because strings are immutable.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00381))_

```
int64(count)
```

### Technical frame 3: Chapter 5 - Tidbits / Strings and Byte Arrays

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00382))_

> Still, when it comes to bytes and strings, it's probably something you'll end up doing often. Do note that when you use []byte(X) or string(X) , you're creating a copy of the data. This is necessary because strings are immutable.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00383))_

> If you take the length of a string, you might not get what you expect.
