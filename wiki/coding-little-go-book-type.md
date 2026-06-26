---
page_id: coding-little-go-book-type
page_kind: concept
summary: Type: 34 statement(s) and 21 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-type@232c86d3c196a31a7bb9107dd6cdaeab
---

# Type

What [[coding-little-go-book]] covers about type:

## Statements

- However, you can't change the type of power . _(coding_little_go_book.pdf (source-range-810ce361-00090))_
- Next, we changed the type of parameter Super expects. _(coding_little_go_book.pdf (source-range-810ce361-00132))_
- Also, time.After is a channel of type chan time.Time . _(coding_little_go_book.pdf (source-range-810ce361-00457))_
- Interfaces are types that define a contract but not an implementation. _(coding_little_go_book.pdf (source-range-810ce361-00319))_
- In fact, this way of converting is common across various types as well. _(coding_little_go_book.pdf (source-range-810ce361-00380))_
- This lets you use _ over and over again regardless of the returned type. _(coding_little_go_book.pdf (source-range-810ce361-00102))_
- The way Go handles visibility of types is straightforward and effective. _(coding_little_go_book.pdf (source-range-810ce361-00334))_
- If you're used to dynamically typed languages, you might find this cumbersome. _(coding_little_go_book.pdf (source-range-810ce361-00037))_
- Note that if the underlying type is not int , the above will result in an error. _(coding_little_go_book.pdf (source-range-810ce361-00373))_
- Go has a handy short variable declaration operator, := , which can infer the type: _(coding_little_go_book.pdf (source-range-810ce361-00079))_
- In the above code, we say that the type *Saiyan is the receiver of the Super method. _(coding_little_go_book.pdf (source-range-810ce361-00142))_
- which can then be used anywhere -- as a field type, as a parameter, as a return value. _(coding_little_go_book.pdf (source-range-810ce361-00389))_
- We did spend three chapters talking about types and how to declare variables after all. _(coding_little_go_book.pdf (source-range-810ce361-00471))_
- Go is a compiled, statically typed language with a C-like syntax and garbage collection. _(coding_little_go_book.pdf (source-range-810ce361-00032))_

## Technical atoms

> Being statically typed means that variables must be of a specific type (int, string, bool, []byte, etc.).
_(source: coding_little_go_book.pdf (source-range-810ce361-00037))_

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

```
type Person struct { Name	string } func (p	*Person)	Introduce()	{ fmt.Printf("Hi,	I'm	%s\n",	p.Name) } type Saiyan struct { *Person Power	int } //	and	to	use	it: goku	:=	&Saiyan{ Person:	&Person{"Goku"}, Power:	9001, } goku.Introduce()
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00163))_


## Source

- [[coding-little-go-book]]
