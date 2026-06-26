---
page_id: coding-little-go-book-variable
page_kind: concept
summary: Variable: 26 statement(s) and 2 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-variable@d5eadb6012a649b31d8a809aed67ac4b
---

# Variable

What [[coding-little-go-book]] covers about variable:

## Statements

- As long as one of the variables is new, := can be used. _(coding_little_go_book.pdf (source-range-810ce361-00088))_
- Some variables, when created, have an easy-to-define life. _(coding_little_go_book.pdf (source-range-810ce361-00046))_
- Just like unassigned variables have a zero value, so do fields. _(coding_little_go_book.pdf (source-range-810ce361-00123))_
- The compiler will complain with no new variables on left side of := . _(coding_little_go_book.pdf (source-range-810ce361-00085))_
- Because a variable can't be declared twice (not in the same scope anyway). _(coding_little_go_book.pdf (source-range-810ce361-00083))_
- The only concurrent thing you can safely do to a variable is to read from it. _(coding_little_go_book.pdf (source-range-810ce361-00415))_
- If you read the error message closely, you'll notice that variables is plural. _(coding_little_go_book.pdf (source-range-810ce361-00086))_
- Go has a handy short variable declaration operator, := , which can infer the type: _(coding_little_go_book.pdf (source-range-810ce361-00079))_
- What all of the above examples do is declare a variable goku and assign a value to it. _(coding_little_go_book.pdf (source-range-810ce361-00126))_
- We did spend three chapters talking about types and how to declare variables after all. _(coding_little_go_book.pdf (source-range-810ce361-00471))_
- For now, the last thing to know is that, like imports, Go won't let you have unused variables. _(coding_little_go_book.pdf (source-range-810ce361-00091))_
- The most explicit way to deal with variable declaration and assignment in Go is also the most verbose: _(coding_little_go_book.pdf (source-range-810ce361-00075))_
- It's important that you remember that := is used to declare the variable as well as assign a value to it. _(coding_little_go_book.pdf (source-range-810ce361-00083))_
- When we first looked at variables and declarations, we looked only at built-in types, like integers and strings. _(coding_little_go_book.pdf (source-range-810ce361-00117))_

## Technical atoms

> Being statically typed means that variables must be of a specific type (int, string, bool, []byte, etc.).
_(source: coding_little_go_book.pdf (source-range-810ce361-00037))_

```
func main()	{ power	:=	9000 fmt.Printf("It's	over	%d\n",	power) //	COMPILER	ERROR: //	no	new	variables	on	left	side	of	:= power	:=	9001 fmt.Printf("It's	also	over	%d\n",	power) }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00084))_


## Source

- [[coding-little-go-book]]
