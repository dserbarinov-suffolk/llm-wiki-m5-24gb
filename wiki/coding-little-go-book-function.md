---
page_id: coding-little-go-book-function
page_kind: concept
summary: Function: 5 statement(s) and 4 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-function@09416bda469764b53a584340685ea787
---

# Function

What [[coding-little-go-book]] covers about function:

## Statements

- Many developers think that passing b to, or returning it from, a function is going to be more efficient. _(coding_little_go_book.pdf (source-range-773b6275-00268))_
- But if the function was named newItem , we wouldn't be able to access it from a different package. _(coding_little_go_book.pdf (source-range-773b6275-00303))_
- If you write a function that expects a parameter that you'll only be calling Close() on, you absolutely should accept an io.Closer rather than whatever concrete type you're using. _(coding_little_go_book.pdf (source-range-773b6275-00329))_
- However, the first time you see a function that expects something like io.Reader , you'll find yourself thanking the author for not demanding more than he or she needed. _(coding_little_go_book.pdf (source-range-773b6275-00335))_
- Some functions explicitly expect an int32 or an int64 or their unsigned counterparts. _(coding_little_go_book.pdf (source-range-773b6275-00380))_

## Technical atoms

> Context: For example, if our items.go file had a function that looked like:
_(context: coding_little_go_book.pdf (source-range-773b6275-00301))_

```
func NewItem() *Item {
  // ...
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00302))_

> Context: For example, if our items.go file had a function that looked like:
_(context: coding_little_go_book.pdf (source-range-773b6275-00301))_

> For example, if you rename the Item's Price field to price , you should get an error.
_(source: coding_little_go_book.pdf (source-range-773b6275-00304))_

> Context: In a language like C# or Java, we have to be explicit when a class implements an interface: In Go, this happens implicitly. If your structure has a function name Log with a string parameter and no return value, then it can be used as a Logger . This cuts down on the verboseness of using interfaces: } public class ConsoleLogger : Logger { public void Logger(message string) { Console.WriteLine(message) } } type ConsoleLogger struct {} (l ConsoleLogger) Log(message string) {
_(context: coding_little_go_book.pdf (source-range-773b6275-00327))_

```
func (l ConsoleLogger) 
  fmt.Println(message)
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00328))_

> Context: In fact, this way of converting is common across various types as well. Some functions explicitly expect an int32 or an int64 or their unsigned counterparts. You might find yourself having to do things like: Still, when it comes to bytes and strings, it's probably something you'll end up doing often. Do note that when you use []byte(X) or string(X) , you're creating a copy of the data. This is necessary because strings are immutable.
_(context: coding_little_go_book.pdf (source-range-773b6275-00380, source-range-773b6275-00382))_

```
int64(count)
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00381))_


## Source

- [[coding-little-go-book]]
