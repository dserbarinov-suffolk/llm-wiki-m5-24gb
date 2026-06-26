---
page_id: coding-little-go-book-string-byte-array
page_kind: concept
summary: Strings and Byte Arrays: 36 statement(s) and 25 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-string-byte-array@9bc13f04588eec476a47c4bb0c6aff86
---

# Strings and Byte Arrays

What [[coding-little-go-book]] covers about strings and byte arrays:

## Statements

- Arrays are efficient but rigid. _(coding_little_go_book.pdf (source-range-810ce361-00198))_
- Strings and byte arrays are closely related. _(coding_little_go_book.pdf (source-range-810ce361-00378))_
- We can use len to get the length of the array. _(coding_little_go_book.pdf (source-range-810ce361-00196))_
- In Go, you rarely, if ever, use arrays directly. _(coding_little_go_book.pdf (source-range-810ce361-00200))_
- This is necessary because strings are immutable. _(coding_little_go_book.pdf (source-range-810ce361-00382))_
- In Go, like many other languages, arrays are fixed. _(coding_little_go_book.pdf (source-range-810ce361-00191))_
- Slices as wrappers to arrays is a powerful concept. _(coding_little_go_book.pdf (source-range-810ce361-00230))_
- Many languages have the concept of slicing an array. _(coding_little_go_book.pdf (source-range-810ce361-00230))_
- Both JavaScript and Ruby arrays have a slice method. _(coding_little_go_book.pdf (source-range-810ce361-00230))_
- Strings are made of runes which are unicode code points. _(coding_little_go_book.pdf (source-range-810ce361-00383))_
- Like make , this approach is specific to maps and arrays. _(coding_little_go_book.pdf (source-range-810ce361-00260))_
- Integers are assigned 0 , booleans false , strings "" and so on. _(coding_little_go_book.pdf (source-range-810ce361-00077))_
- These are arrays that resize themselves as data is added to them. _(coding_little_go_book.pdf (source-range-810ce361-00191))_
- If you take the length of a string, you might not get what you expect. _(coding_little_go_book.pdf (source-range-810ce361-00383))_

## Technical atoms

> Being statically typed means that variables must be of a specific type (int, string, bool, []byte, etc.).
_(source: coding_little_go_book.pdf (source-range-810ce361-00037))_

> Hopefully, the code that we just executed is understandable. We've created a function and printed out a string with the built-in println function. Did go run know what to execute because there was only a single choice? No. In Go, the entry point to a program has to be a function called main within a package main . We'll talk more about packages in a later chapter. For now, while we focus on understanding the basics of Go, we'll always write our code within the main package. If you want, you can alter the code and change the package name. Run the code via go run and you should get an error. Then, change the name back to main but use a different function name. You should see a different error message. Try making those same changes but use go build instead. Notice that the code compiles, there's just no entry point to run it. This is perfectly normal when you are, for example, building a library.
_(source: coding_little_go_book.pdf (source-range-810ce361-00056))_

```
func log(message	string)	{ } func add(a	int,	b	int)	int	{ } func power(name	string)	(int,	bool)	{ }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00097))_

```
type Saiyan struct { Name	string Power	int }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00114))_

```
type Saiyan struct { Name	string Power	int } func (s	*Saiyan)	Super()	{ s.Power	+=	10000 }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00141))_

```
func NewSaiyan(name	string,	power	int)	*Saiyan	{ return &Saiyan{ Name:	name, Power:	power, } }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00146))_


## Source

- [[coding-little-go-book]]
