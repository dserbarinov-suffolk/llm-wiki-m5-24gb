---
page_id: coding-little-go-book-function-declaration
page_kind: concept
summary: Function Declarations: 18 statement(s) and 33 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-function-declaration@0bedcf066afbac863c1af8c5645fe836
---

# Function Declarations

What [[coding-little-go-book]] covers about function declarations:

## Statements

- We've also introduced another built-in function len . _(coding_little_go_book.pdf (source-range-810ce361-00062))_
- As a final note, Go does have panic and recover functions. _(coding_little_go_book.pdf (source-range-810ce361-00349))_
- You can use defer for any purpose, such as logging when a function exits. _(coding_little_go_book.pdf (source-range-810ce361-00393))_
- Not least of which is the various syntax around declaration and initialization. _(coding_little_go_book.pdf (source-range-810ce361-00472))_
- copy is one of those functions that highlights how slices change the way we code. _(coding_little_go_book.pdf (source-range-810ce361-00243))_
- Some functions explicitly expect an int32 or an int64 or their unsigned counterparts. _(coding_little_go_book.pdf (source-range-810ce361-00379))_
- Go uses a simple rule to define what types and functions are visible outside of a package. _(coding_little_go_book.pdf (source-range-810ce361-00298))_
- Unlike the array declaration, our slice isn't declared with a length within the square brackets. _(coding_little_go_book.pdf (source-range-810ce361-00201))_
- But if the function was named newItem , we wouldn't be able to access it from a different package. _(coding_little_go_book.pdf (source-range-810ce361-00302))_
- The most explicit way to deal with variable declaration and assignment in Go is also the most verbose: _(coding_little_go_book.pdf (source-range-810ce361-00074))_
- Many developers think that passing b to, or returning it from, a function is going to be more efficient. _(coding_little_go_book.pdf (source-range-810ce361-00267))_
- It does more than indent your code; it also aligns field declarations and alphabetically orders imports. _(coding_little_go_book.pdf (source-range-810ce361-00359))_
- This is a package variable (it's defined outside of a function) which is publicly accessible (upper-case first letter). _(coding_little_go_book.pdf (source-range-810ce361-00347))_
- If your structure has a function name Log with a string parameter and no return value, then it can be used as a Logger . _(coding_little_go_book.pdf (source-range-810ce361-00326))_

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
