---
page_id: coding-little-go-book-function-type
page_kind: concept
summary: Function Type: 53 statement(s) and 26 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-function-type@1185fc09ca685bdb8392c460c810e5a7
---

# Function Type

What [[coding-little-go-book]] covers about function type:

## Statements

- However, you can't change the type of power . _(coding_little_go_book.pdf (source-range-810ce361-00090))_
- We've also introduced another built-in function len . _(coding_little_go_book.pdf (source-range-810ce361-00063))_
- Next, we changed the type of parameter Super expects. _(coding_little_go_book.pdf (source-range-810ce361-00132))_
- Maps, like slices, are created with the make function. _(coding_little_go_book.pdf (source-range-810ce361-00249))_
- Also, time.After is a channel of type chan time.Time . _(coding_little_go_book.pdf (source-range-810ce361-00457))_
- As a final note, Go does have panic and recover functions. _(coding_little_go_book.pdf (source-range-810ce361-00350))_
- Interfaces are types that define a contract but not an implementation. _(coding_little_go_book.pdf (source-range-810ce361-00319))_
- In fact, this way of converting is common across various types as well. _(coding_little_go_book.pdf (source-range-810ce361-00380))_
- This lets you use _ over and over again regardless of the returned type. _(coding_little_go_book.pdf (source-range-810ce361-00102))_
- The way Go handles visibility of types is straightforward and effective. _(coding_little_go_book.pdf (source-range-810ce361-00334))_
- You can use defer for any purpose, such as logging when a function exits. _(coding_little_go_book.pdf (source-range-810ce361-00394))_
- To block for a maximum amount of time, we can use the time.After function. _(coding_little_go_book.pdf (source-range-810ce361-00451))_
- This is a good time to point out that functions can return multiple values. _(coding_little_go_book.pdf (source-range-810ce361-00096))_
- If you're used to dynamically typed languages, you might find this cumbersome. _(coding_little_go_book.pdf (source-range-810ce361-00037))_

## Technical atoms

> Being statically typed means that variables must be of a specific type (int, string, bool, []byte, etc.).
_(source: coding_little_go_book.pdf (source-range-810ce361-00037))_

> Hopefully, the code that we just executed is understandable. We've created a function and printed out a string with the built-in println function. Did go run know what to execute because there was only a single choice? No. In Go, the entry point to a program has to be a function called main within a package main . We'll talk more about packages in a later chapter. For now, while we focus on understanding the basics of Go, we'll always write our code within the main package. If you want, you can alter the code and change the package name. Run the code via go run and you should get an error. Then, change the name back to main but use a different function name. You should see a different error message. Try making those same changes but use go build instead. Notice that the code compiles, there's just no entry point to run it. This is perfectly normal when you are, for example, building a library.
_(source: coding_little_go_book.pdf (source-range-810ce361-00056))_

```
type Saiyan struct { Name	string Power	int }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00114))_

```
type Saiyan struct { Name	string Power	int } func (s	*Saiyan)	Super()	{ s.Power	+=	10000 }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00141))_

> Despite the lack of constructors, Go does have a built-in new function which is used to allocate the memory required by a type.
_(source: coding_little_go_book.pdf (source-range-810ce361-00151))_

```
For	example,	we	could	expand	our	definition	of Saiyan : which	we'd	initialize	via: type Saiyan struct { Name	string Power	int Father	*Saiyan } gohan	:=	&Saiyan{ Name:	"Gohan", Power:	1000, Father:	&Saiyan	{ Name:	"Goku", Power:	9001, Father:	nil, }, }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00158))_


## Source

- [[coding-little-go-book]]
