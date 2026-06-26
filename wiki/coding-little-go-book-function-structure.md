---
page_id: coding-little-go-book-function-structure
page_kind: concept
summary: Functions on Structures: 24 statement(s) and 39 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-function-structure@dc21d35fa690ba56c2f6e23a922991ce
---

# Functions on Structures

What [[coding-little-go-book]] covers about functions on structures:

## Statements

- Structures don't have constructors. _(coding_little_go_book.pdf (source-range-810ce361-00144))_
- We've also introduced another built-in function len . _(coding_little_go_book.pdf (source-range-810ce361-00062))_
- As a final note, Go does have panic and recover functions. _(coding_little_go_book.pdf (source-range-810ce361-00349))_
- You can use defer for any purpose, such as logging when a function exits. _(coding_little_go_book.pdf (source-range-810ce361-00393))_
- If we have a structure with many fields, creating copies can be expensive. _(coding_little_go_book.pdf (source-range-810ce361-00136))_
- copy is one of those functions that highlights how slices change the way we code. _(coding_little_go_book.pdf (source-range-810ce361-00243))_
- Go supports composition, which is the act of including one structure into another. _(coding_little_go_book.pdf (source-range-810ce361-00159))_
- A slice is a lightweight structure that wraps and represents a portion of an array. _(coding_little_go_book.pdf (source-range-810ce361-00199))_
- Some functions explicitly expect an int32 or an int64 or their unsigned counterparts. _(coding_little_go_book.pdf (source-range-810ce361-00379))_
- Go uses a simple rule to define what types and functions are visible outside of a package. _(coding_little_go_book.pdf (source-range-810ce361-00298))_
- Now that we're talking about structures, we need to expand that conversation to include pointers. _(coding_little_go_book.pdf (source-range-810ce361-00116))_
- But if the function was named newItem , we wouldn't be able to access it from a different package. _(coding_little_go_book.pdf (source-range-810ce361-00302))_
- Many developers think that passing b to, or returning it from, a function is going to be more efficient. _(coding_little_go_book.pdf (source-range-810ce361-00267))_
- The following chapters will build on what we know about structures as well as the inner workings that we've explored. _(coding_little_go_book.pdf (source-range-810ce361-00186))_

## Code, rules, and examples

> For example, the lifetime of a variable returned by a function or referenced by other variables and objects can be tricky to determine.
_(source: coding_little_go_book.pdf (source-range-810ce361-00046))_

> Some variables, when created, have an easy-to-define life. A variable local to a function, for example, disappears when the function exits. In other cases, it isn't so obvious -- at least to a compiler. For example, the lifetime of a variable returned by a function or referenced by other variables and objects can be tricky to determine. Without garbage collection, it's up to developers to free the memory associated with such variables at a point where the developer knows the variable isn't needed. How? In C, you'd literally free(str); the variable.
_(source: coding_little_go_book.pdf (source-range-810ce361-00046))_

> Hopefully, the code that we just executed is understandable. We've created a function and printed out a string with the built-in println function. Did go run know what to execute because there was only a single choice? No. In Go, the entry point to a program has to be a function called main within a package main . We'll talk more about packages in a later chapter. For now, while we focus on understanding the basics of Go, we'll always write our code within the main package. If you want, you can alter the code and change the package name. Run the code via go run and you should get an error. Then, change the name back to main but use a different function name. You should see a different error message. Try making those same changes but use go build instead. Notice that the code compiles, there's just no entry point to run it. This is perfectly normal when you are, for example, building a library.
_(source: coding_little_go_book.pdf (source-range-810ce361-00056))_

> Go has a number of built-in functions, such as println , which can be used without reference.
_(source: coding_little_go_book.pdf (source-range-810ce361-00058))_

> You've probably noticed we prefix the function name with the package, e.g., fmt.Println . This is different from many other languages. We'll learn more about packages in later chapters. For now, knowing how to import and use a package is a good start.
_(source: coding_little_go_book.pdf (source-range-810ce361-00063))_

> You can head over to https://golang.org/pkg/fmt/#Println to learn more about the Println function that we used.
_(source: coding_little_go_book.pdf (source-range-810ce361-00067))_


## Source

- [[coding-little-go-book]]
