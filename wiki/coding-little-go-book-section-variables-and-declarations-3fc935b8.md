---
page_id: coding-little-go-book-section-variables-and-declarations-3fc935b8
page_kind: source
summary: Variables and Declarations: 31 source-backed entries and 8 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: sources/coding-little-go-book/sections
source_id: coding_little_go_book.pdf
projection_coverage: section-coding-little-go-book-section-variables-and-declarations-3fc935b8@a6346a1467c457576f155e2bbf9c3de7
---

# Variables and Declarations

From [[coding-little-go-book]].

## Statements

- Unfortunately, things are more complicated in Go. _(coding_little_go_book.pdf (source-range-810ce361-00073))_
- Still, it'll probably take some time before you truly feel comfortable with it. _(coding_little_go_book.pdf (source-range-810ce361-00073))_
- You might be thinking Woah! _(coding_little_go_book.pdf (source-range-810ce361-00074))_
- The most explicit way to deal with variable declaration and assignment in Go is also the most verbose: _(coding_little_go_book.pdf (source-range-810ce361-00075))_
- Integers are assigned 0 , booleans false , strings "" and so on. _(coding_little_go_book.pdf (source-range-810ce361-00077))_
- Go has a handy short variable declaration operator, := , which can infer the type: _(coding_little_go_book.pdf (source-range-810ce361-00079))_
- Because a variable can't be declared twice (not in the same scope anyway). _(coding_little_go_book.pdf (source-range-810ce361-00083))_
- It's important that you remember that := is used to declare the variable as well as assign a value to it. _(coding_little_go_book.pdf (source-range-810ce361-00083))_
- Because a variable can't be declared twice (not in the same scope anyway). _(coding_little_go_book.pdf (source-range-810ce361-00083))_
- This means that when we first declare a variable, we use := but on subsequent assignment, we use the assignment operator = . _(coding_little_go_book.pdf (source-range-810ce361-00085))_
- The compiler will complain with no new variables on left side of := . _(coding_little_go_book.pdf (source-range-810ce361-00085))_
- This makes a lot of sense, but it can be tricky for your muscle memory to remember when to switch between the two. _(coding_little_go_book.pdf (source-range-810ce361-00085))_
- This means that when we first declare a variable, we use := but on subsequent assignment, we use the assignment operator = . _(coding_little_go_book.pdf (source-range-810ce361-00085))_
- If you read the error message closely, you'll notice that variables is plural. _(coding_little_go_book.pdf (source-range-810ce361-00086))_
- As long as one of the variables is new, := can be used. _(coding_little_go_book.pdf (source-range-810ce361-00088))_
- However, you can't change the type of power . _(coding_little_go_book.pdf (source-range-810ce361-00090))_
- Although power is being used twice with := , the compiler won't complain the second time we use it, it'll see that the other variable, name , is a new variable and allow := . _(coding_little_go_book.pdf (source-range-810ce361-00090))_
- It was declared (implicitly) as an integer and thus, can only be assigned integers. _(coding_little_go_book.pdf (source-range-810ce361-00090))_
- It was declared (implicitly) as an integer and thus, can only be assigned integers. _(coding_little_go_book.pdf (source-range-810ce361-00090))_
- For now, the last thing to know is that, like imports, Go won't let you have unused variables. _(coding_little_go_book.pdf (source-range-810ce361-00091))_
- won't compile because name is declared but not used. _(coding_little_go_book.pdf (source-range-810ce361-00093))_
- won't compile because name is declared but not used. _(coding_little_go_book.pdf (source-range-810ce361-00093))_
- For now, remember that you'll use var NAME TYPE when declaring a variable to its zero value, NAME := VALUE when declaring and assigning a value, and NAME = VALUE when assigning to a previously declared variable. _(coding_little_go_book.pdf (source-range-810ce361-00094))_

## Technical atoms

```
package main import ( "fmt" ) func main()	{ var power	int power	=	9000 fmt.Printf("It's	over	%d\n",	power) }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00076))_

```
var power	int	=	9000
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00078))_

```
power	:=	9000
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00080))_

```
func main()	{ power	:=	getPower() } func getPower()	int	{ return 9001 }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00082))_

```
func main()	{ power	:=	9000 fmt.Printf("It's	over	%d\n",	power) //	COMPILER	ERROR: //	no	new	variables	on	left	side	of	:= power	:=	9001 fmt.Printf("It's	also	over	%d\n",	power) }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00084))_

```
func main()	{ name,	power	:=	"Goku",	9000 fmt.Printf("%s's	power	is	over	%d\n",	name,	power) }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00087))_

```
func main()	{ power	:=	1000 fmt.Printf("default	power	is	%d\n",	power) name,	power	:=	"Goku",	9000 fmt.Printf("%s's	power	is	over	%d\n",	name,	power) }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00089))_

```
func main()	{ name,	power	:=	"Goku",	1000 fmt.Printf("default	power	is	%d\n",	power) }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00092))_
