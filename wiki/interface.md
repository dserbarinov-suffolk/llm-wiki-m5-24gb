---
page_id: interface
page_kind: concept
summary: Canonical concept 'Interface': 2 source(s), 21 statement(s), 5 atom(s), 0 relation(s).
sources: raw/coding_learn_go_with_tests_excerpt.pdf, raw/coding_little_go_book.pdf
updated: 2026-06-26
category_path: concepts
projection_coverage: canonical-concept-interface@f1d3517111b135d501fe636b8395c867
---

# Interface

Compiled concept page from 2 source(s), 21 statement(s), and 5 technical atom(s).

## Source Evidence

### [[coding-learn-go-with-tests-excerpt]]

Source topic: [[coding-learn-go-with-tests-excerpt-interface]]

#### Statements

- This web interface allows you to search for documentation of standard library packages and third-party packages. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00209))_
- Interfaces are a very powerful concept in statically typed languages like Go because they allow you to make functions that can be used with different types and create highly-decoupled code whilst still maintaining type-safety. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00474))_
- In Go interface resolution is implicit . _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00490))_
- If the type you pass in matches what the interface is asking for, it will compile. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00490))_
- By declaring an interface, the helper is decoupled from the concrete types and only has the method it needs to do its job. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00492))_
- This kind of approach of using interfaces to declare only what you need is very important in software design and will be covered in more detail in later sections. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00493))_
- Interfaces are a great tool for hiding complexity away from other parts of the system. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00543))_
- You'll learn about interfaces defined in the standard library that are used everywhere and by implementing them against your own types, you can very quickly re-use a lot of great functionality. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00544))_

#### Technical atoms

> Context: With Go, we can codify this intent with interfaces .
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00473))_

```
func TestArea(t *testing.T) {
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00476))_

> Context: How does something become a shape? We just tell Go what a Shape is using an interface declaration
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00479))_

```
type Shape interface {
    Area() float64
}
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00480))_


### [[coding-little-go-book]]

Source topic: [[coding-little-go-book-interface]]

#### Statements

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

#### Technical atoms

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

> Context: In a language like C# or Java, we have to be explicit when a class implements an interface: In Go, this happens implicitly. If your structure has a function name Log with a string parameter and no return value, then it can be used as a Logger . This cuts down on the verboseness of using interfaces: } public class ConsoleLogger : Logger { public void Logger(message string) { Console.WriteLine(message) } } type ConsoleLogger struct {} (l ConsoleLogger) Log(message string) {
_(context: coding_little_go_book.pdf (source-range-773b6275-00327))_

```
func (l ConsoleLogger) 
  fmt.Println(message)
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00328))_


## Cross-Source Comparison

- No typed cross-source relationships detected yet.
