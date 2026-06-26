---
page_id: coding-little-go-book-variable-declaration
page_kind: concept
summary: Variables and Declarations: 17 statement(s) and 19 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-variable-declaration@aefc1e3d2adf6898ea1944b60f56f1ca
---

# Variables and Declarations

What [[coding-little-go-book]] covers about variables and declarations:

## Statements

- Just like unassigned variables have a zero value, so do fields. _(coding_little_go_book.pdf (source-range-810ce361-00122))_
- The compiler will complain with no new variables on left side of := . _(coding_little_go_book.pdf (source-range-810ce361-00084))_
- Not least of which is the various syntax around declaration and initialization. _(coding_little_go_book.pdf (source-range-810ce361-00472))_
- What all of the above examples do is declare a variable goku and assign a value to it. _(coding_little_go_book.pdf (source-range-810ce361-00125))_
- We did spend three chapters talking about types and how to declare variables after all. _(coding_little_go_book.pdf (source-range-810ce361-00470))_
- Unlike the array declaration, our slice isn't declared with a length within the square brackets. _(coding_little_go_book.pdf (source-range-810ce361-00201))_
- The most explicit way to deal with variable declaration and assignment in Go is also the most verbose: _(coding_little_go_book.pdf (source-range-810ce361-00074))_
- It does more than indent your code; it also aligns field declarations and alphabetically orders imports. _(coding_little_go_book.pdf (source-range-810ce361-00359))_
- It's important that you remember that := is used to declare the variable as well as assign a value to it. _(coding_little_go_book.pdf (source-range-810ce361-00082))_
- This is a package variable (it's defined outside of a function) which is publicly accessible (upper-case first letter). _(coding_little_go_book.pdf (source-range-810ce361-00347))_
- This means that when we first declare a variable, we use := but on subsequent assignment, we use the assignment operator = . _(coding_little_go_book.pdf (source-range-810ce361-00084))_
- Because we potentially have multiple (two in this case) goroutines writing to the same variable, counter , at the same time. _(coding_little_go_book.pdf (source-range-810ce361-00412))_
- Many times though, we don't want a variable that is directly associated with our value but rather a variable that has a pointer to our value. _(coding_little_go_book.pdf (source-range-810ce361-00126))_
- There are a few things we haven't looked at, such as constants and global variables but rest assured, their visibility is determined by the same naming rule. _(coding_little_go_book.pdf (source-range-810ce361-00333))_

## Code, rules, and examples

> Environment variables can be set through the Environment Variables button on the Advanced tab of the System control panel.
_(source: coding_little_go_book.pdf (source-range-810ce361-00030))_

> Being statically typed means that variables must be of a specific type (int, string, bool, []byte, etc.).
_(source: coding_little_go_book.pdf (source-range-810ce361-00037))_

> For example, the lifetime of a variable returned by a function or referenced by other variables and objects can be tricky to determine.
_(source: coding_little_go_book.pdf (source-range-810ce361-00046))_

> Some variables, when created, have an easy-to-define life. A variable local to a function, for example, disappears when the function exits. In other cases, it isn't so obvious -- at least to a compiler. For example, the lifetime of a variable returned by a function or referenced by other variables and objects can be tricky to determine. Without garbage collection, it's up to developers to free the memory associated with such variables at a point where the developer knows the variable isn't needed. How? In C, you'd literally free(str); the variable.
_(source: coding_little_go_book.pdf (source-range-810ce361-00046))_

> It'd be nice to begin and end our look at variables by saying you declare and assign to a variable by doing x = 4. Unfortunately, things are more complicated in Go. We'll begin our conversation by looking at simple examples. Then, in the next chapter, we'll expand this when we look at creating and using structures. Still, it'll probably take some time before you truly feel comfortable with it.
_(source: coding_little_go_book.pdf (source-range-810ce361-00072))_

> Go has a handy short variable declaration operator, := , which can infer the type:
_(source: coding_little_go_book.pdf (source-range-810ce361-00078))_


## Source

- [[coding-little-go-book]]
