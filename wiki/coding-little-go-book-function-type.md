---
page_id: coding-little-go-book-function-type
page_kind: concept
summary: Function Type: 35 statement(s) and 56 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-function-type@3a5c18fba815155649d15e326eb38c93
---

# Function Type

What [[coding-little-go-book]] covers about function type:

## Statements

- We've also introduced another built-in function len . _(coding_little_go_book.pdf (source-range-810ce361-00062))_
- Next, we changed the type of parameter Super expects. _(coding_little_go_book.pdf (source-range-810ce361-00131))_
- Also, time.After is a channel of type chan time.Time . _(coding_little_go_book.pdf (source-range-810ce361-00456))_
- As a final note, Go does have panic and recover functions. _(coding_little_go_book.pdf (source-range-810ce361-00349))_
- In fact, this way of converting is common across various types as well. _(coding_little_go_book.pdf (source-range-810ce361-00379))_
- This lets you use _ over and over again regardless of the returned type. _(coding_little_go_book.pdf (source-range-810ce361-00101))_
- The way Go handles visibility of types is straightforward and effective. _(coding_little_go_book.pdf (source-range-810ce361-00333))_
- You can use defer for any purpose, such as logging when a function exits. _(coding_little_go_book.pdf (source-range-810ce361-00393))_
- If you're used to dynamically typed languages, you might find this cumbersome. _(coding_little_go_book.pdf (source-range-810ce361-00037))_
- Note that if the underlying type is not int , the above will result in an error. _(coding_little_go_book.pdf (source-range-810ce361-00372))_
- copy is one of those functions that highlights how slices change the way we code. _(coding_little_go_book.pdf (source-range-810ce361-00243))_
- In the above code, we say that the type *Saiyan is the receiver of the Super method. _(coding_little_go_book.pdf (source-range-810ce361-00141))_
- Some functions explicitly expect an int32 or an int64 or their unsigned counterparts. _(coding_little_go_book.pdf (source-range-810ce361-00379))_
- We did spend three chapters talking about types and how to declare variables after all. _(coding_little_go_book.pdf (source-range-810ce361-00470))_

## Code, rules, and examples

> You can build such systems with Ruby or Python or something else (and many people do), but these types of systems can benefit from a more rigid type system and greater performance.
_(source: coding_little_go_book.pdf (source-range-810ce361-00016))_

> There are other areas where Go excels. For example, there are no dependencies when running a compiled Go program. You don't have to worry if your users have Ruby or the JVM installed, and if so, what version. For this reason, Go is becoming increasingly popular as a language for command-line interface programs and other types of utility programs you need to distribute (e.g., a log collector).
_(source: coding_little_go_book.pdf (source-range-810ce361-00017))_

> Being statically typed means that variables must be of a specific type (int, string, bool, []byte, etc.).
_(source: coding_little_go_book.pdf (source-range-810ce361-00037))_

> For example, the lifetime of a variable returned by a function or referenced by other variables and objects can be tricky to determine.
_(source: coding_little_go_book.pdf (source-range-810ce361-00046))_

> Some variables, when created, have an easy-to-define life. A variable local to a function, for example, disappears when the function exits. In other cases, it isn't so obvious -- at least to a compiler. For example, the lifetime of a variable returned by a function or referenced by other variables and objects can be tricky to determine. Without garbage collection, it's up to developers to free the memory associated with such variables at a point where the developer knows the variable isn't needed. How? In C, you'd literally free(str); the variable.
_(source: coding_little_go_book.pdf (source-range-810ce361-00046))_

> Hopefully, the code that we just executed is understandable. We've created a function and printed out a string with the built-in println function. Did go run know what to execute because there was only a single choice? No. In Go, the entry point to a program has to be a function called main within a package main . We'll talk more about packages in a later chapter. For now, while we focus on understanding the basics of Go, we'll always write our code within the main package. If you want, you can alter the code and change the package name. Run the code via go run and you should get an error. Then, change the name back to main but use a different function name. You should see a different error message. Try making those same changes but use go build instead. Notice that the code compiles, there's just no entry point to run it. This is perfectly normal when you are, for example, building a library.
_(source: coding_little_go_book.pdf (source-range-810ce361-00056))_


## Source

- [[coding-little-go-book]]
