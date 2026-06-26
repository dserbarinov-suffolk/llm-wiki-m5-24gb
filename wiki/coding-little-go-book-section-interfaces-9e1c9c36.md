---
page_id: coding-little-go-book-section-interfaces-9e1c9c36
page_kind: source
summary: Interfaces: 24 source-backed entries and 6 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: sources/coding-little-go-book/sections
source_id: coding_little_go_book.pdf
projection_coverage: section-coding-little-go-book-section-interfaces-9e1c9c36@357e08103a0ba6e6b0ce40b0a70537d2
---

# Interfaces

From [[coding-little-go-book]].

## Statements

- Interfaces are types that define a contract but not an implementation. _(coding_little_go_book.pdf (source-range-773b6275-00319))_
- You might be wondering what purpose this could possibly serve. _(coding_little_go_book.pdf (source-range-773b6275-00321))_
- Yet by programming against the interface, rather than these concrete implementations, we can easily change (and test) which we use without any impact to our code. _(coding_little_go_book.pdf (source-range-773b6275-00323))_
- If your structure has a function name Log with a string parameter and no return value, then it can be used as a Logger . _(coding_little_go_book.pdf (source-range-773b6275-00327))_
- If your structure has a function name Log with a string parameter and no return value, then it can be used as a Logger . _(coding_little_go_book.pdf (source-range-773b6275-00327))_
- The standard library is full of interfaces. _(coding_little_go_book.pdf (source-range-773b6275-00329))_
- It also tends to promote small and focused interfaces. _(coding_little_go_book.pdf (source-range-773b6275-00329))_
- The io package has a handful of popular ones such as io.Reader , io.Writer , and io.Closer . _(coding_little_go_book.pdf (source-range-773b6275-00329))_
- If you write a function that expects a parameter that you'll only be calling Close() on, you absolutely should accept an io.Closer rather than whatever concrete type you're using. _(coding_little_go_book.pdf (source-range-773b6275-00329))_
- The io package has a handful of popular ones such as io.Reader , io.Writer , and io.Closer . _(coding_little_go_book.pdf (source-range-773b6275-00329))_
- If you write a function that expects a parameter that you'll only be calling Close() on, you absolutely should accept an io.Closer rather than whatever concrete type you're using. _(coding_little_go_book.pdf (source-range-773b6275-00329))_
- Interfaces can also participate in composition. _(coding_little_go_book.pdf (source-range-773b6275-00330))_
- For example, io.ReadCloser is an interface composed of the io.Reader interface as well as the io.Closer interface. _(coding_little_go_book.pdf (source-range-773b6275-00330))_
- And, interfaces themselves can be composed of other interfaces. _(coding_little_go_book.pdf (source-range-773b6275-00330))_
- For example, io.ReadCloser is an interface composed of the io.Reader interface as well as the io.Closer interface. _(coding_little_go_book.pdf (source-range-773b6275-00330))_
- Finally, interfaces are commonly used to avoid cyclical imports. _(coding_little_go_book.pdf (source-range-773b6275-00331))_
- Since they don't have implementations, they'll have limited dependencies. _(coding_little_go_book.pdf (source-range-773b6275-00331))_
- Since they don't have implementations, they'll have limited dependencies. _(coding_little_go_book.pdf (source-range-773b6275-00331))_

## Technical atoms

```
type Logger interface {
  Log(message string)
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00320))_

```
type SqlLogger struct { ... }
type ConsoleLogger struct { ... }
type FileLogger struct { ... }
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00322))_

```
type Server struct {
  logger Logger
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00325))_

```
or a function parameter (or return value):
func process(logger Logger) {
  logger.Log("hello!")
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00326))_

> In a language like C# or Java, we have to be explicit when a class implements an interface: In Go, this happens implicitly.
_(source: coding_little_go_book.pdf (source-range-773b6275-00327))_

```
func (l ConsoleLogger) 
  fmt.Println(message)
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00328))_
