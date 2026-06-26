---
page_id: coding-little-go-book-variable-declaration
page_kind: concept
summary: Variables and Declarations: 30 statement(s) and 3 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-variable-declaration@4d76e59d3c8f7c17a088e7742d680cab
---

# Variables and Declarations

What [[coding-little-go-book]] covers about variables and declarations:

## Statements

- As long as one of the variables is new, := can be used. _(coding_little_go_book.pdf (source-range-810ce361-00088))_
- Some variables, when created, have an easy-to-define life. _(coding_little_go_book.pdf (source-range-810ce361-00046))_
- Before we do that, we have to dive back into declarations. _(coding_little_go_book.pdf (source-range-810ce361-00115))_
- Just like unassigned variables have a zero value, so do fields. _(coding_little_go_book.pdf (source-range-810ce361-00123))_
- The compiler will complain with no new variables on left side of := . _(coding_little_go_book.pdf (source-range-810ce361-00085))_
- Because a variable can't be declared twice (not in the same scope anyway). _(coding_little_go_book.pdf (source-range-810ce361-00083))_
- The only concurrent thing you can safely do to a variable is to read from it. _(coding_little_go_book.pdf (source-range-810ce361-00415))_
- If you read the error message closely, you'll notice that variables is plural. _(coding_little_go_book.pdf (source-range-810ce361-00086))_
- Not least of which is the various syntax around declaration and initialization. _(coding_little_go_book.pdf (source-range-810ce361-00473))_
- Go has a handy short variable declaration operator, := , which can infer the type: _(coding_little_go_book.pdf (source-range-810ce361-00079))_
- What all of the above examples do is declare a variable goku and assign a value to it. _(coding_little_go_book.pdf (source-range-810ce361-00126))_
- We did spend three chapters talking about types and how to declare variables after all. _(coding_little_go_book.pdf (source-range-810ce361-00471))_
- For now, the last thing to know is that, like imports, Go won't let you have unused variables. _(coding_little_go_book.pdf (source-range-810ce361-00091))_
- Unlike the array declaration, our slice isn't declared with a length within the square brackets. _(coding_little_go_book.pdf (source-range-810ce361-00202))_

## Technical atoms

> Being statically typed means that variables must be of a specific type (int, string, bool, []byte, etc.).
_(source: coding_little_go_book.pdf (source-range-810ce361-00037))_

```
func main()	{ power	:=	9000 fmt.Printf("It's	over	%d\n",	power) //	COMPILER	ERROR: //	no	new	variables	on	left	side	of	:= power	:=	9001 fmt.Printf("It's	also	over	%d\n",	power) }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00084))_

> Furthermore, you can skip the field name and rely on the order of the field declarations (though for the sake of clarity, you should only do this for structures with few fields):
_(source: coding_little_go_book.pdf (source-range-810ce361-00124))_


## Source

- [[coding-little-go-book]]
