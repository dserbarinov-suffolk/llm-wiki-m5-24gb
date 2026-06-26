---
page_id: coding-little-go-book-string
page_kind: concept
summary: String: 9 statement(s) and 22 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-string@7fdc1ab26607a0437a00f457b07a1610
---

# String

What [[coding-little-go-book]] covers about string:

## Statements

- Strings and byte arrays are closely related. _(coding_little_go_book.pdf (source-range-810ce361-00378))_
- This is necessary because strings are immutable. _(coding_little_go_book.pdf (source-range-810ce361-00382))_
- Strings are made of runes which are unicode code points. _(coding_little_go_book.pdf (source-range-810ce361-00383))_
- Integers are assigned 0 , booleans false , strings "" and so on. _(coding_little_go_book.pdf (source-range-810ce361-00077))_
- If you take the length of a string, you might not get what you expect. _(coding_little_go_book.pdf (source-range-810ce361-00383))_
- Still, when it comes to bytes and strings, it's probably something you'll end up doing often. _(coding_little_go_book.pdf (source-range-810ce361-00382))_
- When we first looked at variables and declarations, we looked only at built-in types, like integers and strings. _(coding_little_go_book.pdf (source-range-810ce361-00117))_
- In the example that we've seen so far, Saiyan has two fields Name and Power of types string and int , respectively. _(coding_little_go_book.pdf (source-range-810ce361-00157))_
- If your structure has a function name Log with a string parameter and no return value, then it can be used as a Logger . _(coding_little_go_book.pdf (source-range-810ce361-00327))_

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
