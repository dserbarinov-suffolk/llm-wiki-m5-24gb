---
page_id: coding-little-go-book-string-and-byte-array
page_kind: concept
summary: Strings and Byte Arrays: 6 statement(s) and 5 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-29
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-string-and-byte-array@90707b3797a7d17327a80fed8db881fe
---

# Strings and Byte Arrays

What [[coding-little-go-book]] covers about strings and byte arrays:

## Statements

### Chapter 5 - Tidbits / Strings and Byte Arrays

- Strings and byte arrays are closely related. We can easily convert one to the other: _(coding_little_go_book.pdf (source-range-23d24eb1-00378))_

- In fact, this way of converting is common across various types as well. Some functions explicitly expect an int32 or an int64 or their unsigned counterparts. You might find yourself having to do things like: _(coding_little_go_book.pdf (source-range-23d24eb1-00380))_

- Still, when it comes to bytes and strings, it's probably something you'll end up doing often. Do note that when you use []byte(X) or string(X) , you're creating a copy of the data. This is necessary because strings are immutable. _(coding_little_go_book.pdf (source-range-23d24eb1-00382))_

- Strings are made of runes which are unicode code points. If you take the length of a string, you might not get what you expect. The following prints 3: _(coding_little_go_book.pdf (source-range-23d24eb1-00383))_


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

### Technical frame 4: Chapter 5 - Tidbits / Strings and Byte Arrays

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00383))_

> Strings are made of runes which are unicode code points. If you take the length of a string, you might not get what you expect. The following prints 3:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00384))_

```
fmt.Println(len("椒"))
```

### Technical frame 5: Chapter 5 - Tidbits / Strings and Byte Arrays

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00383))_

> Strings are made of runes which are unicode code points. If you take the length of a string, you might not get what you expect. The following prints 3:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00385))_

> If you iterate over a string using range , you'll get runes, not bytes.


## Related pages

- [[coding-little-go-book-tidbit]] - shared statements and technical atoms: Tidbits shares source evidence from Chapter 5 - Tidbits / Strings and Byte Arrays: Strings and byte arrays are closely related. We can easily convert one to the other:; Tidbits shares technical record from Chapter 5 - Tidbits / Strings and Byte Arrays: stra := "the spice must flow" byts := []byte(stra) strb := string(byts) (6 shared statement(s), 5 shared atom(s))
- [[coding-little-go-book-section-chapter-5-tidbits-strings-and-byte-arrays-6caeb68b]] - source section: Chapter 5 - Tidbits / Strings and Byte Arrays shares source evidence from Chapter 5 - Tidbits / Strings and Byte Arrays: Strings and byte arrays are closely related. We can easily convert one to the other:; Chapter 5 - Tidbits / Strings and Byte Arrays shares technical record from Chapter 5 - Tidbits / Strings and Byte Arrays: stra := "the spice must flow" byts := []byte(stra) strb := string(byts) (6 shared statement(s), 5 shared atom(s))

## Source

- [[coding-little-go-book]]
