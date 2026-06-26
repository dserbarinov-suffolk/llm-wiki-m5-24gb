---
page_id: coding-little-go-book-interface
page_kind: concept
summary: Interfaces: 17 statement(s) and 4 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-interface@e881cde44a7114f0abb0d6bb1478a716
---

# Interfaces

What [[coding-little-go-book]] covers about interfaces:

## Statements

- The standard library is full of interfaces. _(coding_little_go_book.pdf (source-range-810ce361-00329))_
- Interfaces can also participate in composition. _(coding_little_go_book.pdf (source-range-810ce361-00330))_
- It also tends to promote small and focused interfaces. _(coding_little_go_book.pdf (source-range-810ce361-00329))_
- And, interfaces themselves can be composed of other interfaces. _(coding_little_go_book.pdf (source-range-810ce361-00330))_
- Finally, interfaces are commonly used to avoid cyclical imports. _(coding_little_go_book.pdf (source-range-810ce361-00331))_
- Interfaces are types that define a contract but not an implementation. _(coding_little_go_book.pdf (source-range-810ce361-00319))_
- You'll see and probably use the empty interface more than you might first expect. _(coding_little_go_book.pdf (source-range-810ce361-00376))_
- Finally, if you're new to interfaces, it might take some time before you get a feel for them. _(coding_little_go_book.pdf (source-range-810ce361-00335))_
- In a few sections, we'll look at interfaces which can help us untangle these types of dependencies. _(coding_little_go_book.pdf (source-range-810ce361-00297))_
- Interfaces, return-based error handling, defer for resource management and a simple way to achieve composition. _(coding_little_go_book.pdf (source-range-810ce361-00474))_
- For example, io.ReadCloser is an interface composed of the io.Reader interface as well as the io.Closer interface. _(coding_little_go_book.pdf (source-range-810ce361-00330))_
- In a language like C# or Java, we have to be explicit when a class implements an interface: In Go, this happens implicitly. _(coding_little_go_book.pdf (source-range-810ce361-00327))_
- You can create your own error type; the only requirement is that it fulfills the contract of the built-in error interface, which is: _(coding_little_go_book.pdf (source-range-810ce361-00341))_
- Fields can be of any type -including other structures and types that we haven't explored yet such as arrays, maps, interfaces and functions. _(coding_little_go_book.pdf (source-range-810ce361-00157))_

## Technical atoms

> that I won't be able to make those same assumptions. How much time do you spend talking about interfaces knowing that for some, the concept will be new, while others won't need much more than Go has interfaces ? Ultimately, I take comfort in knowing that you'll let me know if some parts are too shallow or others too detailed. Consider that the price of this book.
_(source: coding_little_go_book.pdf (source-range-810ce361-00021))_

```
type Logger interface { Log(message	string) }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00320))_

```
type error interface { Error()	string }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00342))_

```
func add(a interface {},	b interface {}) interface {}	{ ... }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00370))_


## Source

- [[coding-little-go-book]]
