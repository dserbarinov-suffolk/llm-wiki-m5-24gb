---
page_id: coding-little-go-book-expect
page_kind: concept
summary: Expect: 4 statement(s) and 3 atom(s) from raw/coding_little_go_book.pdf.
page_family: topic-concept
sources: raw/coding_little_go_book.pdf
updated: 2026-06-30
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-expect@14956356f349e78faecd2057ffa96a1d
---

# Expect

What [[coding-little-go-book]] covers about expect:

## Statements

### Chapter 3 - Maps, Arrays and Slices / Maps

- Maps in Go are what other languages call hashtables or dictionaries. They work as you expect: you define a key and value, and can get, set and delete values from it. _(coding_little_go_book.pdf (source-range-23d24eb1-00248))_

### Chapter 4 - Code Organization and Interfaces / Interfaces

- It also tends to promote small and focused interfaces. The standard library is full of interfaces. The io package has a handful of popular ones such as io.Reader , io.Writer , and io.Closer . If you write a function that expects a parameter that you'll only be calling Close() on, you absolutely should accept an io.Closer rather than whatever concrete type you're using. _(coding_little_go_book.pdf (source-range-23d24eb1-00329))_

### Chapter 4 - Code Organization and Interfaces / Before You Continue

- Finally, if you're new to interfaces, it might take some time before you get a feel for them. However, the first time you see a function that expects something like io.Reader , you'll find yourself thanking the author for not demanding more than he or she needed. _(coding_little_go_book.pdf (source-range-23d24eb1-00335))_

### Chapter 5 - Tidbits / Strings and Byte Arrays

- In fact, this way of converting is common across various types as well. Some functions explicitly expect an int32 or an int64 or their unsigned counterparts. You might find yourself having to do things like: _(coding_little_go_book.pdf (source-range-23d24eb1-00380))_


## Technical atoms

### Technical frame 1: Chapter 5 - Tidbits / Strings and Byte Arrays

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00382))_

> Still, when it comes to bytes and strings, it's probably something you'll end up doing often. Do note that when you use []byte(X) or string(X) , you're creating a copy of the data. This is necessary because strings are immutable.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00381))_

```
int64(count)
```

### Technical frame 2: Chapter 5 - Tidbits / Strings and Byte Arrays

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00383))_

> Strings are made of runes which are unicode code points. If you take the length of a string, you might not get what you expect. The following prints 3:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00384))_

```
fmt.Println(len("椒"))
```

### Technical frame 3: Chapter 5 - Tidbits / Strings and Byte Arrays

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00383))_

> Strings are made of runes which are unicode code points. If you take the length of a string, you might not get what you expect. The following prints 3:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00385))_

> If you iterate over a string using range , you'll get runes, not bytes.


## Related pages

- [[coding-little-go-book-function]] - shared statements and technical atoms: Function shares source evidence from Chapter 4 - Code Organization and Interfaces / Interfaces: It also tends to promote small and focused interfaces. The standard library is full of interfaces. The io package has a handful of popular ones such as io.Reader , i ... [truncated]; Function shares technical record from Chapter 5 - Tidbits / Strings and Byte Arrays: int64(count) (3 shared statement(s), 1 shared atom(s))
- [[coding-little-go-book-string]] - shared technical atoms: String shares technical record from Chapter 5 - Tidbits / Strings and Byte Arrays: int64(count) (3 shared atom(s))
- [[coding-little-go-book-you-continue]] - shared statements: Before You Continue shares source evidence from Chapter 4 - Code Organization and Interfaces / Before You Continue: Finally, if you're new to interfaces, it might take some time before you get a feel for them. However, the first time you see a function that expects something like ... [truncated] (1 shared statement(s))

## Source

- [[coding-little-go-book]]
