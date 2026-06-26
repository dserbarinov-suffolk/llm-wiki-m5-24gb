---
page_id: coding-little-go-book-function
page_kind: concept
summary: Function: 22 statement(s) and 10 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-function@56a5f9f8c98f25023ff37b25150220de
---

# Function

What [[coding-little-go-book]] covers about function:

## Statements

- We've also introduced another built-in function len . _(coding_little_go_book.pdf (source-range-810ce361-00063))_
- Maps, like slices, are created with the make function. _(coding_little_go_book.pdf (source-range-810ce361-00249))_
- As a final note, Go does have panic and recover functions. _(coding_little_go_book.pdf (source-range-810ce361-00350))_
- You can use defer for any purpose, such as logging when a function exits. _(coding_little_go_book.pdf (source-range-810ce361-00394))_
- To block for a maximum amount of time, we can use the time.After function. _(coding_little_go_book.pdf (source-range-810ce361-00451))_
- This is a good time to point out that functions can return multiple values. _(coding_little_go_book.pdf (source-range-810ce361-00096))_
- copy is one of those functions that highlights how slices change the way we code. _(coding_little_go_book.pdf (source-range-810ce361-00244))_
- Some functions explicitly expect an int32 or an int64 or their unsigned counterparts. _(coding_little_go_book.pdf (source-range-810ce361-00380))_
- You've probably noticed we prefix the function name with the package, e.g., fmt.Println . _(coding_little_go_book.pdf (source-range-810ce361-00064))_
- Go uses a simple rule to define what types and functions are visible outside of a package. _(coding_little_go_book.pdf (source-range-810ce361-00299))_
- If we just want to run a bit of code, such as the above, we can use an anonymous function. _(coding_little_go_book.pdf (source-range-810ce361-00402))_
- Go has a number of built-in functions, such as println , which can be used without reference. _(coding_little_go_book.pdf (source-range-810ce361-00058))_
- But if the function was named newItem , we wouldn't be able to access it from a different package. _(coding_little_go_book.pdf (source-range-810ce361-00303))_
- Finally, now that we know about slices, we can look at another commonly used built-in function: copy . _(coding_little_go_book.pdf (source-range-810ce361-00244))_

## Technical atoms

> Hopefully, the code that we just executed is understandable. We've created a function and printed out a string with the built-in println function. Did go run know what to execute because there was only a single choice? No. In Go, the entry point to a program has to be a function called main within a package main . We'll talk more about packages in a later chapter. For now, while we focus on understanding the basics of Go, we'll always write our code within the main package. If you want, you can alter the code and change the package name. Run the code via go run and you should get an error. Then, change the name back to main but use a different function name. You should see a different error message. Try making those same changes but use go build instead. Notice that the code compiles, there's just no entry point to run it. This is perfectly normal when you are, for example, building a library.
_(source: coding_little_go_book.pdf (source-range-810ce361-00056))_

> Despite the lack of constructors, Go does have a built-in new function which is used to allocate the memory required by a type.
_(source: coding_little_go_book.pdf (source-range-810ce361-00151))_

> The Saiyan structure has a field of type *Person . Because we didn't give it an explicit field name, we can implicitly access the fields and functions of the composed type. However, the Go compiler did give it a field name, consider the perfectly valid:
_(source: coding_little_go_book.pdf (source-range-810ce361-00164))_

> However, because implicit composition is really just a compiler trick, we can "overwrite" the functions of a composed type. For example, our Saiyan structure can have its own Introduce function:
_(source: coding_little_go_book.pdf (source-range-810ce361-00170))_

> This changes how you code. For example, a number of functions take a position parameter. In JavaScript, if we want to find the first space in a string (yes, slices work on strings too!) after the first five characters, we'd write:
_(source: coding_little_go_book.pdf (source-range-810ce361-00235))_

```
or	a	function	parameter	(or	return	value): func process(logger	Logger)	{ logger.Log("hello!")
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00326))_


## Source

- [[coding-little-go-book]]
