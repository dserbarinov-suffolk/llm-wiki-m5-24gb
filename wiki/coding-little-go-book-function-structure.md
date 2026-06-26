---
page_id: coding-little-go-book-function-structure
page_kind: concept
summary: Functions on Structures: 36 statement(s) and 14 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-function-structure@a2d7a20eb6fbd326dfa48db1cda5d9c0
---

# Functions on Structures

What [[coding-little-go-book]] covers about functions on structures:

## Statements

- Structures don't have constructors. _(coding_little_go_book.pdf (source-range-810ce361-00145))_
- We've also introduced another built-in function len . _(coding_little_go_book.pdf (source-range-810ce361-00063))_
- Maps, like slices, are created with the make function. _(coding_little_go_book.pdf (source-range-810ce361-00249))_
- As a final note, Go does have panic and recover functions. _(coding_little_go_book.pdf (source-range-810ce361-00350))_
- What Go does have are structures, which can be associated with methods. _(coding_little_go_book.pdf (source-range-810ce361-00112))_
- You can use defer for any purpose, such as logging when a function exits. _(coding_little_go_book.pdf (source-range-810ce361-00394))_
- If we have a structure with many fields, creating copies can be expensive. _(coding_little_go_book.pdf (source-range-810ce361-00137))_
- To block for a maximum amount of time, we can use the time.After function. _(coding_little_go_book.pdf (source-range-810ce361-00451))_
- This is a good time to point out that functions can return multiple values. _(coding_little_go_book.pdf (source-range-810ce361-00096))_
- copy is one of those functions that highlights how slices change the way we code. _(coding_little_go_book.pdf (source-range-810ce361-00244))_
- Go supports composition, which is the act of including one structure into another. _(coding_little_go_book.pdf (source-range-810ce361-00160))_
- A slice is a lightweight structure that wraps and represents a portion of an array. _(coding_little_go_book.pdf (source-range-810ce361-00200))_
- Some functions explicitly expect an int32 or an int64 or their unsigned counterparts. _(coding_little_go_book.pdf (source-range-810ce361-00380))_
- You've probably noticed we prefix the function name with the package, e.g., fmt.Println . _(coding_little_go_book.pdf (source-range-810ce361-00064))_

## Technical atoms

> Hopefully, the code that we just executed is understandable. We've created a function and printed out a string with the built-in println function. Did go run know what to execute because there was only a single choice? No. In Go, the entry point to a program has to be a function called main within a package main . We'll talk more about packages in a later chapter. For now, while we focus on understanding the basics of Go, we'll always write our code within the main package. If you want, you can alter the code and change the package name. Run the code via go run and you should get an error. Then, change the name back to main but use a different function name. You should see a different error message. Try making those same changes but use go build instead. Notice that the code compiles, there's just no entry point to run it. This is perfectly normal when you are, for example, building a library.
_(source: coding_little_go_book.pdf (source-range-810ce361-00056))_

> Note: The trailing , in the above structure is required.
_(source: coding_little_go_book.pdf (source-range-810ce361-00120))_

> Furthermore, you can skip the field name and rely on the order of the field declarations (though for the sake of clarity, you should only do this for structures with few fields):
_(source: coding_little_go_book.pdf (source-range-810ce361-00124))_

> It should also be obvious that copying a pointer is going to be cheaper than copying a complex structure.
_(source: coding_little_go_book.pdf (source-range-810ce361-00137))_

> Despite the lack of constructors, Go does have a built-in new function which is used to allocate the memory required by a type.
_(source: coding_little_go_book.pdf (source-range-810ce361-00151))_

> The Saiyan structure has a field of type *Person . Because we didn't give it an explicit field name, we can implicitly access the fields and functions of the composed type. However, the Go compiler did give it a field name, consider the perfectly valid:
_(source: coding_little_go_book.pdf (source-range-810ce361-00164))_


## Source

- [[coding-little-go-book]]
