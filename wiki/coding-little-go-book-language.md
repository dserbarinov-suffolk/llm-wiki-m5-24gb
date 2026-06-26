---
page_id: coding-little-go-book-language
page_kind: concept
summary: Language: 29 statement(s) and 10 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-language@84031efcd3ddc750c2656ca43a63e521
---

# Language

What [[coding-little-go-book]] covers about language:

## Statements

- In Go, like many other languages, arrays are fixed. _(coding_little_go_book.pdf (source-range-810ce361-00190))_
- I recently heard Go described as a boring language. _(coding_little_go_book.pdf (source-range-810ce361-00470))_
- Many languages have the concept of slicing an array. _(coding_little_go_book.pdf (source-range-810ce361-00229))_
- In some languages, this is called a trait or a mixin. _(coding_little_go_book.pdf (source-range-810ce361-00159))_
- On the downside, language design is fairly incremental. _(coding_little_go_book.pdf (source-range-810ce361-00012))_
- Go is often described as a concurrent-friendly language. _(coding_little_go_book.pdf (source-range-810ce361-00396))_
- The other is my discomfort at writing a book about a language. _(coding_little_go_book.pdf (source-range-810ce361-00020))_
- Maps in Go are what other languages call hashtables or dictionaries. _(coding_little_go_book.pdf (source-range-810ce361-00247))_
- For some systems, dynamic languages are categorically more productive. _(coding_little_go_book.pdf (source-range-810ce361-00107))_
- Go isn't an object-oriented (OO) language like C++, Java, Ruby and C#. _(coding_little_go_book.pdf (source-range-810ce361-00110))_
- This is how many languages behave, including Ruby, Python, Java and C#. _(coding_little_go_book.pdf (source-range-810ce361-00135))_
- If you're used to dynamically typed languages, you might find this cumbersome. _(coding_little_go_book.pdf (source-range-810ce361-00037))_
- Go is a compiled, statically typed language with a C-like syntax and garbage collection. _(coding_little_go_book.pdf (source-range-810ce361-00032))_
- If you've mostly been making use of dynamic languages, you might feel a little different. _(coding_little_go_book.pdf (source-range-810ce361-00472))_

## Code, rules, and examples

> I've always had a love-hate relationship when it comes to learning new languages.
_(source: coding_little_go_book.pdf (source-range-810ce361-00012))_

> Go was built as a system language (e.g., operating systems, device drivers) and thus aimed at C and C++ developers. According to the Go team, and which is certainly true of me, application developers, not system developers, have become the primary Go users. Why? I can't speak authoritatively for system developers, but for those of us building websites, services, desktop applications and the like, it partially comes down to the emerging need for a class of systems that sit somewhere in between low-level system applications and higherlevel applications.
_(source: coding_little_go_book.pdf (source-range-810ce361-00015))_

> There are other areas where Go excels. For example, there are no dependencies when running a compiled Go program. You don't have to worry if your users have Ruby or the JVM installed, and if so, what version. For this reason, Go is becoming increasingly popular as a language for command-line interface programs and other types of utility programs you need to distribute (e.g., a log collector).
_(source: coding_little_go_book.pdf (source-range-810ce361-00017))_

> Compiled languages can be unpleasant to work with because compilation can be slow.
_(source: coding_little_go_book.pdf (source-range-810ce361-00034))_

> Saying that a language has a C-like syntax means that if you're used to any other C-like languages such as C, C++, Java, JavaScript and C#, then you're going to find Go familiar -- superficially, at least. For example, it means && is used as a boolean AND, == is used to compare equality, { and } start and end a scope, and array indexes start at 0.
_(source: coding_little_go_book.pdf (source-range-810ce361-00039))_

> Languages with garbage collectors (e.g., Ruby, Python, Java, JavaScript, C#, Go) are able to keep track of these and free them when they're no longer used. Garbage collection adds overhead, but it also eliminates a number of devastating bugs.
_(source: coding_little_go_book.pdf (source-range-810ce361-00047))_


## Source

- [[coding-little-go-book]]
