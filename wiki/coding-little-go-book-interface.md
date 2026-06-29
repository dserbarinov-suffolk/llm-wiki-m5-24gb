---
page_id: coding-little-go-book-interface
page_kind: concept
summary: Interfaces: 13 statement(s) and 6 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-29
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-interface@cee3acc90ba3740083f476cba48b9aea
---

# Interfaces

What [[coding-little-go-book]] covers about interfaces:

## Statements

### Chapter 4 - Code Organization and Interfaces / Interfaces

- Interfaces are types that define a contract but not an implementation. Here's an example: _(coding_little_go_book.pdf (source-range-23d24eb1-00319))_

- You might be wondering what purpose this could possibly serve. Interfaces help decouple your code from specific implementations. For example, we might have various types of loggers: _(coding_little_go_book.pdf (source-range-23d24eb1-00321))_

- Yet by programming against the interface, rather than these concrete implementations, we can easily change (and test) which we use without any impact to our code. _(coding_little_go_book.pdf (source-range-23d24eb1-00323))_

- In a language like C# or Java, we have to be explicit when a class implements an interface: In Go, this happens implicitly. If your structure has a function name Log with a string parameter and no return value, then it can be used as a Logger . This cuts down on the verboseness of using interfaces: } public class ConsoleLogger : Logger { public void Logger(message string) { Console.WriteLine(message) } } type ConsoleLogger struct {} (l ConsoleLogger) Log(message string) { _(coding_little_go_book.pdf (source-range-23d24eb1-00327))_

- It also tends to promote small and focused interfaces. The standard library is full of interfaces. The io package has a handful of popular ones such as io.Reader , io.Writer , and io.Closer . If you write a function that expects a parameter that you'll only be calling Close() on, you absolutely should accept an io.Closer rather than whatever concrete type you're using. _(coding_little_go_book.pdf (source-range-23d24eb1-00329))_

- Interfaces can also participate in composition. And, interfaces themselves can be composed of other interfaces. For example, io.ReadCloser is an interface composed of the io.Reader interface as well as the io.Closer interface. _(coding_little_go_book.pdf (source-range-23d24eb1-00330))_

- Finally, interfaces are commonly used to avoid cyclical imports. Since they don't have implementations, they'll have limited dependencies. _(coding_little_go_book.pdf (source-range-23d24eb1-00331))_


## Technical atoms

### Technical frame 1: Chapter 4 - Code Organization and Interfaces / Interfaces

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00321))_

> You might be wondering what purpose this could possibly serve. Interfaces help decouple your code from specific implementations. For example, we might have various types of loggers:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00320))_

```
type Logger interface {
  Log(message string)
}
```

### Technical frame 2: Chapter 4 - Code Organization and Interfaces / Interfaces

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00323))_

> Yet by programming against the interface, rather than these concrete implementations, we can easily change (and test) which we use without any impact to our code.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00322))_

```
type SqlLogger struct { ... }
type ConsoleLogger struct { ... }
type FileLogger struct { ... }
```

### Technical frame 3: Chapter 4 - Code Organization and Interfaces / Interfaces

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00327))_

> In a language like C# or Java, we have to be explicit when a class implements an interface: In Go, this happens implicitly. If your structure has a function name Log with a string parameter and no return value, then it can be used as a Logger . This cuts down on the verboseness of using interfaces: } public class ConsoleLogger : Logger { public void Logger(message string) { Console.WriteLine(message) } } type ConsoleLogger struct {} (l ConsoleLogger) Log(message string) {

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00325))_

```
type Server struct {
  logger Logger
}
```

### Technical frame 4: Chapter 4 - Code Organization and Interfaces / Interfaces

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00327))_

> In a language like C# or Java, we have to be explicit when a class implements an interface: In Go, this happens implicitly. If your structure has a function name Log with a string parameter and no return value, then it can be used as a Logger . This cuts down on the verboseness of using interfaces: } public class ConsoleLogger : Logger { public void Logger(message string) { Console.WriteLine(message) } } type ConsoleLogger struct {} (l ConsoleLogger) Log(message string) {

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00326))_

```
or a function parameter (or return value):
func process(logger Logger) {
  logger.Log("hello!")
```

### Technical frame 5: Chapter 4 - Code Organization and Interfaces / Interfaces

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00329))_

> It also tends to promote small and focused interfaces. The standard library is full of interfaces. The io package has a handful of popular ones such as io.Reader , io.Writer , and io.Closer . If you write a function that expects a parameter that you'll only be calling Close() on, you absolutely should accept an io.Closer rather than whatever concrete type you're using.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00327))_

> In a language like C# or Java, we have to be explicit when a class implements an interface: In Go, this happens implicitly.

### Technical frame 6: Chapter 4 - Code Organization and Interfaces / Interfaces

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00329))_

> It also tends to promote small and focused interfaces. The standard library is full of interfaces. The io package has a handful of popular ones such as io.Reader , io.Writer , and io.Closer . If you write a function that expects a parameter that you'll only be calling Close() on, you absolutely should accept an io.Closer rather than whatever concrete type you're using.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00328))_

```
func (l ConsoleLogger) 
  fmt.Println(message)
}
```


## Related pages

- [[coding-little-go-book-code-organization-and-interface]] - narrower topic: Code Organization and Interfaces shares source evidence from Chapter 4 - Code Organization and Interfaces / Interfaces: Interfaces are types that define a contract but not an implementation. Here's an example:; Code Organization and Interfaces shares technical record from Chapter 4 - Code Organization and Interfaces / Interfaces: type Logger interface { Log(message string) } (13 shared statement(s), 6 shared atom(s))
- [[coding-little-go-book-code-organization]] - shared statements and technical atoms: Code Organization shares source evidence from Chapter 4 - Code Organization and Interfaces / Interfaces: Yet by programming against the interface, rather than these concrete implementations, we can easily change (and test) which we use without any impact to our code.; Code Organization shares technical record from Chapter 4 - Code Organization and Interfaces / Interfaces: type SqlLogger struct { ... } type ConsoleLogger struct { ... } type FileLogger struct { ... } (1 shared statement(s), 1 shared atom(s))
- [[coding-little-go-book-section-chapter-4-code-organization-and-interfaces-interfaces-ee136513]] - source section: Chapter 4 - Code Organization and Interfaces / Interfaces shares source evidence from Chapter 4 - Code Organization and Interfaces / Interfaces: Interfaces are types that define a contract but not an implementation. Here's an example:; Chapter 4 - Code Organization and Interfaces / Interfaces shares technical record from Chapter 4 - Code Organization and Interfaces / Interfaces: type Logger interface { Log(message string) } (13 shared statement(s), 6 shared atom(s))

## Source

- [[coding-little-go-book]]
