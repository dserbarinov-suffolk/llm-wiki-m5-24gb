---
page_id: coding-little-go-book-system
page_kind: concept
summary: System: 4 statement(s) and 1 atom(s) from raw/coding_little_go_book.pdf.
page_family: topic-concept
sources: raw/coding_little_go_book.pdf
updated: 2026-06-30
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-system@a35d9ea02a54676c87a1f8ecd3e79781
---

# System

What [[coding-little-go-book]] covers about system:

## Statements

### Introduction

- I've always had a love-hate relationship when it comes to learning new languages. On the one hand, languages are so fundamental to what we do, that even small changes can have measurable impact. That aha moment when something clicks can have a lasting effect on how you program and can redefine your expectations of other languages. On the downside, language design is fairly incremental. Learning new keywords, type system, coding style as well as new libraries, communities and paradigms is a lot of work that seems hard to justify. Compared to everything else we have to learn, new languages often feel like a poor investment of our time. _(coding_little_go_book.pdf (source-range-23d24eb1-00012))_

### Getting Started / Windows

- Download the latest zip file. If you're on an x64 system, you'll want go#.#.#.windows-amd64.zip , where #.#.# is the latest version of Go. Unzip it at a location of your choosing. c:\Go is a good choice. Set up two environment variables: 1. GOPATH points to your workspace. That might be something like c:\users\goku\work\go . 2. Add c:\Go\bin to your PATH environment variable. Environment variables can be set through the Environment Variables button on the Advanced tab of the System control panel. Some versions of Windows provide this control panel through the Advanced System Settings option inside the System control panel. Open a command prompt and type go version . You'll hopefully get an output that looks like go version go1.3.3 windows/amd64 . _(coding_little_go_book.pdf (source-range-23d24eb1-00030))_

### Chapter 1 - The Basics / Static Typing

- Being statically typed means that variables must be of a specific type (int, string, bool, []byte, etc.). This is either achieved by specifying the type when the variable is declared or, in many cases, letting the compiler infer the type (we'll look at examples shortly). There's a lot more that can be said about static typing, but I believe it's something better understood by looking at code. If you're used to dynamically typed languages, you might find this cumbersome. You're not wrong, but there are advantages, especially when you pair static typing with compilation. The two are often conflated. It's true that when you have one, you normally have the other but it isn't a hard rule. With a rigid type system, a compiler is able to detect problems beyond mere syntactical mistakes as well as make further optimizations. _(coding_little_go_book.pdf (source-range-23d24eb1-00037))_

### Chapter 1 - The Basics / Before You Continue

- If you're coming from a dynamic language, the complexity around types and declarations might seem like a step backwards. I don't disagree with you. For some systems, dynamic languages are categorically more productive. _(coding_little_go_book.pdf (source-range-23d24eb1-00108))_


## Technical atoms

### Technical frame 1: Introduction

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00018))_

> Put plainly, learning Go is an efficient use of your time. You won't have to spend long hours learning or even mastering Go, and you'll end up with something practical from your effort.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00017))_

> You don't have to worry if your users have Ruby or the JVM installed, and if so, what version.


## Related pages

- [[coding-little-go-book-type]] - shared statements and technical atoms: Type shares source evidence from Introduction: I've always had a love-hate relationship when it comes to learning new languages. On the one hand, languages are so fundamental to what we do, that even small change ... [truncated]; Type shares technical record from Introduction: You don't have to worry if your users have Ruby or the JVM installed, and if so, what version. (2 shared statement(s), 1 shared atom(s))
- [[coding-little-go-book-compiler]] - shared statements: Compiler shares source evidence from Chapter 1 - The Basics / Static Typing: Being statically typed means that variables must be of a specific type (int, string, bool, []byte, etc.). This is either achieved by specifying the type when the var ... [truncated] (1 shared statement(s))
- [[coding-little-go-book-language]] - shared statements: Language shares source evidence from Chapter 1 - The Basics / Before You Continue: If you're coming from a dynamic language, the complexity around types and declarations might seem like a step backwards. I don't disagree with you. For some systems, ... [truncated] (1 shared statement(s))

## Source

- [[coding-little-go-book]]
