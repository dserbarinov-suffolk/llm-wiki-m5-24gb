---
page_id: coding-little-go-book-type
page_kind: concept
summary: Type: 23 statement(s) and 37 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-type@3d7f68e4416fb7d253332773d49e1c23
---

# Type

What [[coding-little-go-book]] covers about type:

## Statements

- Next, we changed the type of parameter Super expects. _(coding_little_go_book.pdf (source-range-810ce361-00131))_
- Also, time.After is a channel of type chan time.Time . _(coding_little_go_book.pdf (source-range-810ce361-00456))_
- In fact, this way of converting is common across various types as well. _(coding_little_go_book.pdf (source-range-810ce361-00379))_
- This lets you use _ over and over again regardless of the returned type. _(coding_little_go_book.pdf (source-range-810ce361-00101))_
- The way Go handles visibility of types is straightforward and effective. _(coding_little_go_book.pdf (source-range-810ce361-00333))_
- If you're used to dynamically typed languages, you might find this cumbersome. _(coding_little_go_book.pdf (source-range-810ce361-00037))_
- Note that if the underlying type is not int , the above will result in an error. _(coding_little_go_book.pdf (source-range-810ce361-00372))_
- In the above code, we say that the type *Saiyan is the receiver of the Super method. _(coding_little_go_book.pdf (source-range-810ce361-00141))_
- We did spend three chapters talking about types and how to declare variables after all. _(coding_little_go_book.pdf (source-range-810ce361-00470))_
- Go is a compiled, statically typed language with a C-like syntax and garbage collection. _(coding_little_go_book.pdf (source-range-810ce361-00032))_
- Go uses a simple rule to define what types and functions are visible outside of a package. _(coding_little_go_book.pdf (source-range-810ce361-00298))_
- If you're coming from a statically typed language, you're probably feeling comfortable with Go. _(coding_little_go_book.pdf (source-range-810ce361-00108))_
- There's obviously some relation between the types Saiyan and *Saiyan , but they are two distinct types. _(coding_little_go_book.pdf (source-range-810ce361-00131))_
- On Linux / OSX, don't forget that you need to prefix the executable with dotslash, so you need to type ./main . _(coding_little_go_book.pdf (source-range-810ce361-00054))_

## Code, rules, and examples

> You can build such systems with Ruby or Python or something else (and many people do), but these types of systems can benefit from a more rigid type system and greater performance.
_(source: coding_little_go_book.pdf (source-range-810ce361-00016))_

> There are other areas where Go excels. For example, there are no dependencies when running a compiled Go program. You don't have to worry if your users have Ruby or the JVM installed, and if so, what version. For this reason, Go is becoming increasingly popular as a language for command-line interface programs and other types of utility programs you need to distribute (e.g., a log collector).
_(source: coding_little_go_book.pdf (source-range-810ce361-00017))_

> Being statically typed means that variables must be of a specific type (int, string, bool, []byte, etc.).
_(source: coding_little_go_book.pdf (source-range-810ce361-00037))_

> Go has a handy short variable declaration operator, := , which can infer the type:
_(source: coding_little_go_book.pdf (source-range-810ce361-00078))_

> However, you can't change the type of power .
_(source: coding_little_go_book.pdf (source-range-810ce361-00089))_

> There's more to learn about declaration and assignments. For now, remember that you'll use var NAME TYPE when declaring a variable to its zero value, NAME := VALUE when declaring and assigning a value, and NAME = VALUE when assigning to a previously declared variable.
_(source: coding_little_go_book.pdf (source-range-810ce361-00093))_


## Source

- [[coding-little-go-book]]
