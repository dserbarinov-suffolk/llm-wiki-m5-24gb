---
page_id: coding-little-go-book-change
page_kind: concept
summary: Change: 9 statement(s) and 10 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-change@bccbfad4ffa368062d1a076ce47106dd
---

# Change

What [[coding-little-go-book]] covers about change:

## Statements

- Next, we changed the type of parameter Super expects. _(coding_little_go_book.pdf (source-range-810ce361-00131))_
- copy is one of those functions that highlights how slices change the way we code. _(coding_little_go_book.pdf (source-range-810ce361-00243))_
- Next, open a shell/command prompt and change the directory to where you saved the file. _(coding_little_go_book.pdf (source-range-810ce361-00052))_
- On the one hand, languages are so fundamental to what we do, that even small changes can have measurable impact. _(coding_little_go_book.pdf (source-range-810ce361-00012))_
- On the one hand, it's a pretty slight syntactical change; on the other, it does feel a little less compartmentalized. _(coding_little_go_book.pdf (source-range-810ce361-00146))_
- Because Super made changes to a copy of our original goku value and thus, changes made in Super weren't reflected in the caller. _(coding_little_go_book.pdf (source-range-810ce361-00129))_
- As we already saw, passing values is a great way to make data immutable (changes that a function makes to it won't be reflected in the calling code). _(coding_little_go_book.pdf (source-range-810ce361-00180))_
- Since we moved the shared Item structure to shopping/models/item.go , we need to change shopping/db/db.go to reference the Item structure from models package: _(coding_little_go_book.pdf (source-range-810ce361-00294))_
- Though the changes are often incremental, they tend to have a wide scope and they impact productivity, readability, performance, testability, dependency management, error handling, documentation, profiling, communities, standard libraries, and so on. _(coding_little_go_book.pdf (source-range-810ce361-00013))_

## Code, rules, and examples

> Hopefully, the code that we just executed is understandable. We've created a function and printed out a string with the built-in println function. Did go run know what to execute because there was only a single choice? No. In Go, the entry point to a program has to be a function called main within a package main . We'll talk more about packages in a later chapter. For now, while we focus on understanding the basics of Go, we'll always write our code within the main package. If you want, you can alter the code and change the package name. Run the code via go run and you should get an error. Then, change the name back to main but use a different function name. You should see a different error message. Try making those same changes but use go build instead. Notice that the code compiles, there's just no entry point to run it. This is perfectly normal when you are, for example, building a library.
_(source: coding_little_go_book.pdf (source-range-810ce361-00056))_

> However, you can't change the type of power .
_(source: coding_little_go_book.pdf (source-range-810ce361-00089))_

> We can prove that it's a copy by trying to change where it points to (not something you'd likely want to actually do):
_(source: coding_little_go_book.pdf (source-range-810ce361-00133))_

> Even if you don't intend to change the data, consider the cost of creating a copy of large structures. Conversely, you might have small structures, say:
_(source: coding_little_go_book.pdf (source-range-810ce361-00181))_

```
c	:=	cap(scores) fmt.Println(c) for i	:=	0;	i	<	25;	i++	{ scores	=	append(scores,	i) //	if	our	capacity	has	changed, //	Go	had	to	grow	our	array	to	accommodate	the	new	data if cap(scores)	!=	c	{ c	=	cap(scores) fmt.Println(c) } } }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00215))_

> This changes how you code. For example, a number of functions take a position parameter. In JavaScript, if we want to find the first space in a string (yes, slices work on strings too!) after the first five characters, we'd write:
_(source: coding_little_go_book.pdf (source-range-810ce361-00234))_


## Source

- [[coding-little-go-book]]
