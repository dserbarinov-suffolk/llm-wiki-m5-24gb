---
page_id: coding-little-go-book-section-composition-d7ecbdda
page_kind: source
summary: Composition: 13 source-backed entries and 5 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: sources/coding-little-go-book/sections
source_id: coding_little_go_book.pdf
projection_coverage: section-coding-little-go-book-section-composition-d7ecbdda@00536b6a02d6fcfc7127b65ffa2dcea3
---

# Composition

From [[coding-little-go-book]].

## Statements

- Go supports composition, which is the act of including one structure into another. _(coding_little_go_book.pdf (source-range-810ce361-00160))_
- In Java, there's the possibility to extend structures with inheritance but, in a scenario where this is not an option, a mixin would be written like this: _(coding_little_go_book.pdf (source-range-810ce361-00160))_
- In some languages, this is called a trait or a mixin. _(coding_little_go_book.pdf (source-range-810ce361-00160))_
- In some languages, this is called a trait or a mixin. _(coding_little_go_book.pdf (source-range-810ce361-00160))_
- This can get pretty tedious. _(coding_little_go_book.pdf (source-range-810ce361-00162))_
- Every method of Person needs to be duplicated in Saiyan . _(coding_little_go_book.pdf (source-range-810ce361-00162))_
- Both of the above will print "Goku". _(coding_little_go_book.pdf (source-range-810ce361-00166))_
- When using inheritance, your class is tightly coupled to your superclass and you end up focusing on hierarchy rather than behavior. _(coding_little_go_book.pdf (source-range-810ce361-00167))_

## Technical atoms

> Languages that don't have an explicit composition mechanism can always do it the long way.
_(source: coding_little_go_book.pdf (source-range-810ce361-00160))_

```
public class Person	{ private String	name; public String	getName()	{ return this .name; } } public class Saiyan	{ //	Saiyan	is	said	to	have	a	person private Person	person; //	we	forward	the	call	to	person public String	getName()	{ return this .person.getName(); } ... }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00161))_

```
type Person struct { Name	string } func (p	*Person)	Introduce()	{ fmt.Printf("Hi,	I'm	%s\n",	p.Name) } type Saiyan struct { *Person Power	int } //	and	to	use	it: goku	:=	&Saiyan{ Person:	&Person{"Goku"}, Power:	9001, } goku.Introduce()
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00163))_

> The Saiyan structure has a field of type *Person . Because we didn't give it an explicit field name, we can implicitly access the fields and functions of the composed type. However, the Go compiler did give it a field name, consider the perfectly valid:
_(source: coding_little_go_book.pdf (source-range-810ce361-00164))_

```
goku	:=	&Saiyan{ Person:	&Person{"Goku"}, } fmt.Println(goku.Name) fmt.Println(goku.Person.Name)
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00165))_
