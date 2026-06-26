---
page_id: coding-little-go-book-string-byte-array
page_kind: concept
summary: Strings and Byte Arrays: 30 statement(s) and 35 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-string-byte-array@6a507494f2a1e0779f9ec3ec78d500c9
---

# Strings and Byte Arrays

What [[coding-little-go-book]] covers about strings and byte arrays:

## Statements

- Arrays are efficient but rigid. _(coding_little_go_book.pdf (source-range-810ce361-00197))_
- Strings and byte arrays are closely related. _(coding_little_go_book.pdf (source-range-810ce361-00377))_
- In Go, you rarely, if ever, use arrays directly. _(coding_little_go_book.pdf (source-range-810ce361-00199))_
- This is necessary because strings are immutable. _(coding_little_go_book.pdf (source-range-810ce361-00381))_
- In Go, like many other languages, arrays are fixed. _(coding_little_go_book.pdf (source-range-810ce361-00190))_
- Slices as wrappers to arrays is a powerful concept. _(coding_little_go_book.pdf (source-range-810ce361-00229))_
- Many languages have the concept of slicing an array. _(coding_little_go_book.pdf (source-range-810ce361-00229))_
- Both JavaScript and Ruby arrays have a slice method. _(coding_little_go_book.pdf (source-range-810ce361-00229))_
- Strings are made of runes which are unicode code points. _(coding_little_go_book.pdf (source-range-810ce361-00382))_
- Like make , this approach is specific to maps and arrays. _(coding_little_go_book.pdf (source-range-810ce361-00259))_
- Integers are assigned 0 , booleans false , strings "" and so on. _(coding_little_go_book.pdf (source-range-810ce361-00076))_
- These are arrays that resize themselves as data is added to them. _(coding_little_go_book.pdf (source-range-810ce361-00190))_
- If you take the length of a string, you might not get what you expect. _(coding_little_go_book.pdf (source-range-810ce361-00382))_
- We'll now have this same conversation with respect to array and map values. _(coding_little_go_book.pdf (source-range-810ce361-00265))_

## Code, rules, and examples

> Being statically typed means that variables must be of a specific type (int, string, bool, []byte, etc.).
_(source: coding_little_go_book.pdf (source-range-810ce361-00037))_

> Saying that a language has a C-like syntax means that if you're used to any other C-like languages such as C, C++, Java, JavaScript and C#, then you're going to find Go familiar -- superficially, at least. For example, it means && is used as a boolean AND, == is used to compare equality, { and } start and end a scope, and array indexes start at 0.
_(source: coding_little_go_book.pdf (source-range-810ce361-00039))_

> Hopefully, the code that we just executed is understandable. We've created a function and printed out a string with the built-in println function. Did go run know what to execute because there was only a single choice? No. In Go, the entry point to a program has to be a function called main within a package main . We'll talk more about packages in a later chapter. For now, while we focus on understanding the basics of Go, we'll always write our code within the main package. If you want, you can alter the code and change the package name. Run the code via go run and you should get an error. Then, change the name back to main but use a different function name. You should see a different error message. Try making those same changes but use go build instead. Notice that the code compiles, there's just no entry point to run it. This is perfectly normal when you are, for example, building a library.
_(source: coding_little_go_book.pdf (source-range-810ce361-00056))_

```
func log(message	string)	{ } func add(a	int,	b	int)	int	{ } func power(name	string)	(int,	bool)	{ }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00096))_

```
type Saiyan struct { Name	string Power	int }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00113))_

> When we first looked at variables and declarations, we looked only at built-in types, like integers and strings.
_(source: coding_little_go_book.pdf (source-range-810ce361-00116))_


## Source

- [[coding-little-go-book]]
