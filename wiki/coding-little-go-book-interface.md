---
page_id: coding-little-go-book-interface
page_kind: concept
summary: Interfaces: 13 statement(s) and 6 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-interface@273d280a930f26e1a14512b1d86d7b18
---

# Interfaces

What [[coding-little-go-book]] covers about interfaces:

## Statements

- And, interfaces themselves can be composed of other interfaces. _(coding_little_go_book.pdf (source-range-773b6275-00330))_
- Interfaces are types that define a contract but not an implementation. _(coding_little_go_book.pdf (source-range-773b6275-00319))_
- Yet by programming against the interface, rather than these concrete implementations, we can easily change (and test) which we use without any impact to our code. _(coding_little_go_book.pdf (source-range-773b6275-00323))_
- Interfaces can also participate in composition. _(coding_little_go_book.pdf (source-range-773b6275-00330))_
- Finally, interfaces are commonly used to avoid cyclical imports. _(coding_little_go_book.pdf (source-range-773b6275-00331))_
- The standard library is full of interfaces. _(coding_little_go_book.pdf (source-range-773b6275-00329))_
- It also tends to promote small and focused interfaces. _(coding_little_go_book.pdf (source-range-773b6275-00329))_
- For example, io.ReadCloser is an interface composed of the io.Reader interface as well as the io.Closer interface. _(coding_little_go_book.pdf (source-range-773b6275-00330))_
- You might be wondering what purpose this could possibly serve. _(coding_little_go_book.pdf (source-range-773b6275-00321))_
- If your structure has a function name Log with a string parameter and no return value, then it can be used as a Logger . _(coding_little_go_book.pdf (source-range-773b6275-00327))_
- The io package has a handful of popular ones such as io.Reader , io.Writer , and io.Closer . _(coding_little_go_book.pdf (source-range-773b6275-00329))_
- If you write a function that expects a parameter that you'll only be calling Close() on, you absolutely should accept an io.Closer rather than whatever concrete type you're using. _(coding_little_go_book.pdf (source-range-773b6275-00329))_
- Since they don't have implementations, they'll have limited dependencies. _(coding_little_go_book.pdf (source-range-773b6275-00331))_

## Technical atoms

> Context: Interfaces are types that define a contract but not an implementation. Here's an example:
_(context: coding_little_go_book.pdf (source-range-773b6275-00319))_

```
type Logger interface {
  Log(message string)
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00320))_

> Context: You might be wondering what purpose this could possibly serve. Interfaces help decouple your code from specific implementations. For example, we might have various types of loggers:
_(context: coding_little_go_book.pdf (source-range-773b6275-00321))_

```
type SqlLogger struct { ... }
type ConsoleLogger struct { ... }
type FileLogger struct { ... }
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00322))_

> Context: How would you use one? Just like any other type, it could be a structure's field:
_(context: coding_little_go_book.pdf (source-range-773b6275-00324))_

```
type Server struct {
  logger Logger
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00325))_

> Context: How would you use one? Just like any other type, it could be a structure's field:
_(context: coding_little_go_book.pdf (source-range-773b6275-00324))_

```
or a function parameter (or return value):
func process(logger Logger) {
  logger.Log("hello!")
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00326))_

> Context: How would you use one? Just like any other type, it could be a structure's field:
_(context: coding_little_go_book.pdf (source-range-773b6275-00324))_

> In a language like C# or Java, we have to be explicit when a class implements an interface: In Go, this happens implicitly.
_(source: coding_little_go_book.pdf (source-range-773b6275-00327))_

> Context: In a language like C# or Java, we have to be explicit when a class implements an interface: In Go, this happens implicitly. If your structure has a function name Log with a string parameter and no return value, then it can be used as a Logger . This cuts down on the verboseness of using interfaces: } public class ConsoleLogger : Logger { public void Logger(message string) { Console.WriteLine(message) } } type ConsoleLogger struct {} (l ConsoleLogger) Log(message string) {
_(context: coding_little_go_book.pdf (source-range-773b6275-00327))_

```
func (l ConsoleLogger) 
  fmt.Println(message)
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00328))_


## Source

- [[coding-little-go-book]]
