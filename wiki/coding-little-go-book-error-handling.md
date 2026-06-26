---
page_id: coding-little-go-book-error-handling
page_kind: concept
summary: Error Handling: 10 statement(s) and 11 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-error-handling@70adf279082ae1d099529e0d1c29c5f8
---

# Error Handling

What [[coding-little-go-book]] covers about error handling:

## Statements

- Without it, the compiler will give an error. _(coding_little_go_book.pdf (source-range-810ce361-00120))_
- If it makes contextual sense, you should use this error, too. _(coding_little_go_book.pdf (source-range-810ce361-00348))_
- If you read the error message closely, you'll notice that variables is plural. _(coding_little_go_book.pdf (source-range-810ce361-00086))_
- Go's preferred way to deal with errors is through return values, not exceptions. _(coding_little_go_book.pdf (source-range-810ce361-00339))_
- Note that if the underlying type is not int , the above will result in an error. _(coding_little_go_book.pdf (source-range-810ce361-00373))_
- Attempts to access an out of range index in the array will result in a compiler or runtime error. _(coding_little_go_book.pdf (source-range-810ce361-00193))_
- If you try to run the code, you'll get a couple of errors from db/db.go about Item being undefined. _(coding_little_go_book.pdf (source-range-810ce361-00290))_
- Interfaces, return-based error handling, defer for resource management and a simple way to achieve composition. _(coding_little_go_book.pdf (source-range-810ce361-00474))_
- You can create your own error type; the only requirement is that it fulfills the contract of the built-in error interface, which is: _(coding_little_go_book.pdf (source-range-810ce361-00341))_
- Though the changes are often incremental, they tend to have a wide scope and they impact productivity, readability, performance, testability, dependency management, error handling, documentation, profiling, communities, standard libraries, and so on. _(coding_little_go_book.pdf (source-range-810ce361-00013))_

## Technical atoms

> Hopefully, the code that we just executed is understandable. We've created a function and printed out a string with the built-in println function. Did go run know what to execute because there was only a single choice? No. In Go, the entry point to a program has to be a function called main within a package main . We'll talk more about packages in a later chapter. For now, while we focus on understanding the basics of Go, we'll always write our code within the main package. If you want, you can alter the code and change the package name. Run the code via go run and you should get an error. Then, change the name back to main but use a different function name. You should see a different error message. Try making those same changes but use go build instead. Notice that the code compiles, there's just no entry point to run it. This is perfectly normal when you are, for example, building a library.
_(source: coding_little_go_book.pdf (source-range-810ce361-00056))_

> You should get two errors about fmt and os being imported and not used.
_(source: coding_little_go_book.pdf (source-range-810ce361-00067))_

```
func main()	{ power	:=	9000 fmt.Printf("It's	over	%d\n",	power) //	COMPILER	ERROR: //	no	new	variables	on	left	side	of	:= power	:=	9001 fmt.Printf("It's	also	over	%d\n",	power) }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00084))_

```
value,	exists	:=	power("goku") if exists	==	false	{ //	handle	this	error	case }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00099))_

```
_,	exists	:=	power("goku") if exists	==	false	{ //	handle	this	error	case }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00101))_

> Now when you try to run the code, you'll get a dreaded import cycle not allowed error.
_(source: coding_little_go_book.pdf (source-range-810ce361-00292))_


## Source

- [[coding-little-go-book]]
