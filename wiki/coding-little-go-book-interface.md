---
page_id: coding-little-go-book-interface
page_kind: concept
summary: Interfaces: 7 statement(s) and 15 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-interface@d9e159b2b8d8bc497ca779173e8c2d15
---

# Interfaces

What [[coding-little-go-book]] covers about interfaces:

## Statements

- The standard library is full of interfaces. _(coding_little_go_book.pdf (source-range-810ce361-00328))_
- It also tends to promote small and focused interfaces. _(coding_little_go_book.pdf (source-range-810ce361-00328))_
- Finally, interfaces are commonly used to avoid cyclical imports. _(coding_little_go_book.pdf (source-range-810ce361-00330))_
- You'll see and probably use the empty interface more than you might first expect. _(coding_little_go_book.pdf (source-range-810ce361-00375))_
- Finally, if you're new to interfaces, it might take some time before you get a feel for them. _(coding_little_go_book.pdf (source-range-810ce361-00334))_
- Interfaces, return-based error handling, defer for resource management and a simple way to achieve composition. _(coding_little_go_book.pdf (source-range-810ce361-00473))_
- Since every type implements all 0 of the empty interface's methods, and since interfaces are implicitly implemented, every type fulfills the contract of the empty interface. _(coding_little_go_book.pdf (source-range-810ce361-00367))_

## Code, rules, and examples

> There are other areas where Go excels. For example, there are no dependencies when running a compiled Go program. You don't have to worry if your users have Ruby or the JVM installed, and if so, what version. For this reason, Go is becoming increasingly popular as a language for command-line interface programs and other types of utility programs you need to distribute (e.g., a log collector).
_(source: coding_little_go_book.pdf (source-range-810ce361-00017))_

> that I won't be able to make those same assumptions. How much time do you spend talking about interfaces knowing that for some, the concept will be new, while others won't need much more than Go has interfaces ? Ultimately, I take comfort in knowing that you'll let me know if some parts are too shallow or others too detailed. Consider that the price of this book.
_(source: coding_little_go_book.pdf (source-range-810ce361-00021))_

> Fields can be of any type -including other structures and types that we haven't explored yet such as arrays, maps, interfaces and functions.
_(source: coding_little_go_book.pdf (source-range-810ce361-00156))_

> In a few sections, we'll look at interfaces which can help us untangle these types of dependencies.
_(source: coding_little_go_book.pdf (source-range-810ce361-00296))_

> Interfaces are types that define a contract but not an implementation. Here's an example:
_(source: coding_little_go_book.pdf (source-range-810ce361-00318))_

```
type Logger interface { Log(message	string) }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00319))_


## Source

- [[coding-little-go-book]]
