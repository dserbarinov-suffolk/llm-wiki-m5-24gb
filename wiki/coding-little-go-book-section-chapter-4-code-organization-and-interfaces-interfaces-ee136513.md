---
page_id: coding-little-go-book-section-chapter-4-code-organization-and-interfaces-interfaces-ee136513
page_kind: source
summary: Chapter 4 - Code Organization and Interfaces / Interfaces: 24 source-backed entries and 3 atom(s) from raw/coding_little_go_book.pdf.
page_family: section-reference
sources: raw/coding_little_go_book.pdf
updated: 2026-06-30
domain: coding-little-go-book
category_path: sources/coding-little-go-book/sections
source_id: coding_little_go_book.pdf
projection_coverage: section-coding-little-go-book-section-chapter-4-code-organization-and-interfaces-interfaces-ee136513@06fc215d269b93b6044fd6fa33a9499e
---

# Chapter 4 - Code Organization and Interfaces / Interfaces

From [[coding-little-go-book]].

## Related pages

- [[coding-little-go-book-section-chapter-4-code-organization-and-interfaces-16681a63]] - broader source section: Chapter 4 - Code Organization and Interfaces
- [[coding-little-go-book-section-chapter-4-code-organization-and-interfaces-packages-57d2c239]] - previous source section: Chapter 4 - Code Organization and Interfaces / Packages
- [[coding-little-go-book-section-chapter-4-code-organization-and-interfaces-before-you-continue-75e8df25]] - next source section: Chapter 4 - Code Organization and Interfaces / Before You Continue
- [[coding-little-go-book-interface]] - topic hub: opens the topic page for Interface

## Statements

- Interfaces are types that define a contract but not an implementation. Here's an example: _(coding_little_go_book.pdf (source-range-23d24eb1-00319))_
- You might be wondering what purpose this could possibly serve. Interfaces help decouple your code from specific implementations. For example, we might have various types of loggers: _(coding_little_go_book.pdf (source-range-23d24eb1-00321))_
- Yet by programming against the interface, rather than these concrete implementations, we can easily change (and test) which we use without any impact to our code. _(coding_little_go_book.pdf (source-range-23d24eb1-00323))_
- In a language like C# or Java, we have to be explicit when a class implements an interface: In Go, this happens implicitly. If your structure has a function name Log with a string parameter and no return value, then it can be used as a Logger . This cuts down on the verboseness of using interfaces: } public class ConsoleLogger : Logger { public void Logger(message string) { Console.WriteLine(message) } } type ConsoleLogger struct {} (l ConsoleLogger) Log(message string) { _(coding_little_go_book.pdf (source-range-23d24eb1-00327))_
- It also tends to promote small and focused interfaces. The standard library is full of interfaces. The io package has a handful of popular ones such as io.Reader , io.Writer , and io.Closer . If you write a function that expects a parameter that you'll only be calling Close() on, you absolutely should accept an io.Closer rather than whatever concrete type you're using. _(coding_little_go_book.pdf (source-range-23d24eb1-00329))_
- Interfaces can also participate in composition. And, interfaces themselves can be composed of other interfaces. For example, io.ReadCloser is an interface composed of the io.Reader interface as well as the io.Closer interface. _(coding_little_go_book.pdf (source-range-23d24eb1-00330))_
- Finally, interfaces are commonly used to avoid cyclical imports. Since they don't have implementations, they'll have limited dependencies. _(coding_little_go_book.pdf (source-range-23d24eb1-00331))_
- If your structure has a function name Log with a string parameter and no return value, then it can be used as a Logger . _(coding_little_go_book.pdf (source-range-23d24eb1-00327))_
- If you write a function that expects a parameter that you'll only be calling Close() on, you absolutely should accept an io.Closer rather than whatever concrete type you're using. _(coding_little_go_book.pdf (source-range-23d24eb1-00329))_
- The io package has a handful of popular ones such as io.Reader , io.Writer , and io.Closer . _(coding_little_go_book.pdf (source-range-23d24eb1-00329))_
- For example, io.ReadCloser is an interface composed of the io.Reader interface as well as the io.Closer interface. _(coding_little_go_book.pdf (source-range-23d24eb1-00330))_
- Since they don't have implementations, they'll have limited dependencies. _(coding_little_go_book.pdf (source-range-23d24eb1-00331))_

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

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00329))_

> It also tends to promote small and focused interfaces. The standard library is full of interfaces. The io package has a handful of popular ones such as io.Reader , io.Writer , and io.Closer . If you write a function that expects a parameter that you'll only be calling Close() on, you absolutely should accept an io.Closer rather than whatever concrete type you're using.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00328))_

```
func (l ConsoleLogger) 
  fmt.Println(message)
}
```
