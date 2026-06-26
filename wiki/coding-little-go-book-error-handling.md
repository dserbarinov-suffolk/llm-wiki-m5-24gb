---
page_id: coding-little-go-book-error-handling
page_kind: concept
summary: Error Handling: 7 statement(s) and 18 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-error-handling@42243939ec2545d3b7e3f1136e219d45
---

# Error Handling

What [[coding-little-go-book]] covers about error handling:

## Statements

- Without it, the compiler will give an error. _(coding_little_go_book.pdf (source-range-810ce361-00119))_
- If it makes contextual sense, you should use this error, too. _(coding_little_go_book.pdf (source-range-810ce361-00347))_
- Note that if the underlying type is not int , the above will result in an error. _(coding_little_go_book.pdf (source-range-810ce361-00372))_
- Attempts to access an out of range index in the array will result in a compiler or runtime error. _(coding_little_go_book.pdf (source-range-810ce361-00192))_
- If you try to run the code, you'll get a couple of errors from db/db.go about Item being undefined. _(coding_little_go_book.pdf (source-range-810ce361-00289))_
- Interfaces, return-based error handling, defer for resource management and a simple way to achieve composition. _(coding_little_go_book.pdf (source-range-810ce361-00473))_
- Though the changes are often incremental, they tend to have a wide scope and they impact productivity, readability, performance, testability, dependency management, error handling, documentation, profiling, communities, standard libraries, and so on. _(coding_little_go_book.pdf (source-range-810ce361-00013))_

## Code, rules, and examples

> Hopefully, the code that we just executed is understandable. We've created a function and printed out a string with the built-in println function. Did go run know what to execute because there was only a single choice? No. In Go, the entry point to a program has to be a function called main within a package main . We'll talk more about packages in a later chapter. For now, while we focus on understanding the basics of Go, we'll always write our code within the main package. If you want, you can alter the code and change the package name. Run the code via go run and you should get an error. Then, change the name back to main but use a different function name. You should see a different error message. Try making those same changes but use go build instead. Notice that the code compiles, there's just no entry point to run it. This is perfectly normal when you are, for example, building a library.
_(source: coding_little_go_book.pdf (source-range-810ce361-00056))_

> You should get two errors about fmt and os being imported and not used.
_(source: coding_little_go_book.pdf (source-range-810ce361-00066))_

```
func main()	{ power	:=	9000 fmt.Printf("It's	over	%d\n",	power) //	COMPILER	ERROR: //	no	new	variables	on	left	side	of	:= power	:=	9001 fmt.Printf("It's	also	over	%d\n",	power) }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00083))_

> If you read the error message closely, you'll notice that variables is plural. That's because Go lets you assign multiple variables (using either = or := ):
_(source: coding_little_go_book.pdf (source-range-810ce361-00085))_

```
value,	exists	:=	power("goku") if exists	==	false	{ //	handle	this	error	case }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00098))_

```
_,	exists	:=	power("goku") if exists	==	false	{ //	handle	this	error	case }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00100))_


## Source

- [[coding-little-go-book]]
