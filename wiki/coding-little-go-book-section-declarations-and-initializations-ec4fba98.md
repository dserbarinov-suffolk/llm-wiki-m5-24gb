---
page_id: coding-little-go-book-section-declarations-and-initializations-ec4fba98
page_kind: source
summary: Declarations and Initializations: 39 source-backed entries and 10 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: sources/coding-little-go-book/sections
source_id: coding_little_go_book.pdf
projection_coverage: section-coding-little-go-book-section-declarations-and-initializations-ec4fba98@428ba93d00bcc4d1b53fe88dbe05a4d2
---

# Declarations and Initializations

From [[coding-little-go-book]].

## Statements

- When we first looked at variables and declarations, we looked only at built-in types, like integers and strings. _(coding_little_go_book.pdf (source-range-810ce361-00117))_
- Now that we're talking about structures, we need to expand that conversation to include pointers. _(coding_little_go_book.pdf (source-range-810ce361-00117))_
- When we first looked at variables and declarations, we looked only at built-in types, like integers and strings. _(coding_little_go_book.pdf (source-range-810ce361-00117))_
- You'll appreciate the required consistency, especially if you've used a language or format that enforces the opposite. _(coding_little_go_book.pdf (source-range-810ce361-00120))_
- Without it, the compiler will give an error. _(coding_little_go_book.pdf (source-range-810ce361-00120))_
- We don't have to set all or even any of the fields. _(coding_little_go_book.pdf (source-range-810ce361-00121))_
- Just like unassigned variables have a zero value, so do fields. _(coding_little_go_book.pdf (source-range-810ce361-00123))_
- What all of the above examples do is declare a variable goku and assign a value to it. _(coding_little_go_book.pdf (source-range-810ce361-00126))_
- Many times though, we don't want a variable that is directly associated with our value but rather a variable that has a pointer to our value. _(coding_little_go_book.pdf (source-range-810ce361-00127))_
- Loosely, it's the difference between being at a house and having directions to the house. _(coding_little_go_book.pdf (source-range-810ce361-00127))_
- A pointer is a memory address; it's the location of where to find the actual value. _(coding_little_go_book.pdf (source-range-810ce361-00127))_
- To make this work as you probably expect, we need to pass a pointer to our value: _(coding_little_go_book.pdf (source-range-810ce361-00130))_
- Because Super made changes to a copy of our original goku value and thus, changes made in Super weren't reflected in the caller. _(coding_little_go_book.pdf (source-range-810ce361-00130))_
- Because Super made changes to a copy of our original goku value and thus, changes made in Super weren't reflected in the caller. _(coding_little_go_book.pdf (source-range-810ce361-00130))_
- There's obviously some relation between the types Saiyan and *Saiyan , but they are two distinct types. _(coding_little_go_book.pdf (source-range-810ce361-00132))_
- Next, we changed the type of parameter Super expects. _(coding_little_go_book.pdf (source-range-810ce361-00132))_
- It used to expect a value of type Saiyan but now expects an address of type *Saiyan , where *X means pointer to value of type X . _(coding_little_go_book.pdf (source-range-810ce361-00132))_
- The first is the use of the & operator to get the address of our value (it's called the address of operator). _(coding_little_go_book.pdf (source-range-810ce361-00132))_
- It used to expect a value of type Saiyan but now expects an address of type *Saiyan , where *X means pointer to value of type X . _(coding_little_go_book.pdf (source-range-810ce361-00132))_
- What you have is a copy, but it still points to the same restaurant as the original. _(coding_little_go_book.pdf (source-range-810ce361-00133))_
- Note that we're still passing a copy of goku's value to Super it just so happens that goku's value has become an address. _(coding_little_go_book.pdf (source-range-810ce361-00133))_
- That copy is the same address as the original, which is what that indirection buys us. _(coding_little_go_book.pdf (source-range-810ce361-00133))_
- This is how many languages behave, including Ruby, Python, Java and C#. _(coding_little_go_book.pdf (source-range-810ce361-00136))_
- Go, and to some degree C#, simply make the fact visible. _(coding_little_go_book.pdf (source-range-810ce361-00136))_
- On a 64-bit machine, a pointer is 64 bits large. _(coding_little_go_book.pdf (source-range-810ce361-00137))_
- The real value of pointers though is that they let you share values. _(coding_little_go_book.pdf (source-range-810ce361-00137))_
- If we have a structure with many fields, creating copies can be expensive. _(coding_little_go_book.pdf (source-range-810ce361-00137))_
- At the end of this chapter, after we've seen a bit more of what we can do with structures, we'll re-examine the pointer-versus-value question. _(coding_little_go_book.pdf (source-range-810ce361-00138))_
- At the end of this chapter, after we've seen a bit more of what we can do with structures, we'll re-examine the pointer-versus-value question. _(coding_little_go_book.pdf (source-range-810ce361-00138))_

## Technical atoms

```
goku	:=	Saiyan{ Name:	"Goku", Power:	9000, }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00119))_

> Note: The trailing , in the above structure is required.
_(source: coding_little_go_book.pdf (source-range-810ce361-00120))_

```
goku	:=	Saiyan{} //	or goku	:=	Saiyan{Name:	"Goku"} goku.Power	=	9000
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00122))_

> Furthermore, you can skip the field name and rely on the order of the field declarations (though for the sake of clarity, you should only do this for structures with few fields):
_(source: coding_little_go_book.pdf (source-range-810ce361-00124))_

```
goku	:=	Saiyan{"Goku",	9000}
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00125))_

```
func main()	{ goku	:=	Saiyan{"Goku",	9000} Super(goku) fmt.Println(goku.Power) } func Super(s	Saiyan)	{ s.Power	+=	10000 }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00129))_

```
func main()	{ goku	:=	&Saiyan{"Goku",	9000} Super(goku) fmt.Println(goku.Power) } func Super(s	*Saiyan)	{ s.Power	+=	10000 }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00131))_

```
func main()	{ goku	:=	&Saiyan{"Goku",	9000} Super(goku) fmt.Println(goku.Power) } func Super(s	*Saiyan)	{ s	=	&Saiyan{"Gohan",	1000} }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00135))_

> It should also be obvious that copying a pointer is going to be cheaper than copying a complex structure.
_(source: coding_little_go_book.pdf (source-range-810ce361-00137))_

> All this isn't to say that you'll always want a pointer.
_(source: coding_little_go_book.pdf (source-range-810ce361-00138))_
