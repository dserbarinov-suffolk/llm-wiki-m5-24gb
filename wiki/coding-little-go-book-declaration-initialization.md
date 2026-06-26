---
page_id: coding-little-go-book-declaration-initialization
page_kind: concept
summary: Declarations and Initializations: 4 statement(s) and 6 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-declaration-initialization@b70ec9774a6d24afe99c58620e7590e5
---

# Declarations and Initializations

What [[coding-little-go-book]] covers about declarations and initializations:

## Statements

- Not least of which is the various syntax around declaration and initialization. _(coding_little_go_book.pdf (source-range-810ce361-00472))_
- Unlike the array declaration, our slice isn't declared with a length within the square brackets. _(coding_little_go_book.pdf (source-range-810ce361-00201))_
- The most explicit way to deal with variable declaration and assignment in Go is also the most verbose: _(coding_little_go_book.pdf (source-range-810ce361-00074))_
- It does more than indent your code; it also aligns field declarations and alphabetically orders imports. _(coding_little_go_book.pdf (source-range-810ce361-00359))_

## Code, rules, and examples

> Go has a handy short variable declaration operator, := , which can infer the type:
_(source: coding_little_go_book.pdf (source-range-810ce361-00078))_

> There's more to learn about declaration and assignments. For now, remember that you'll use var NAME TYPE when declaring a variable to its zero value, NAME := VALUE when declaring and assigning a value, and NAME = VALUE when assigning to a previously declared variable.
_(source: coding_little_go_book.pdf (source-range-810ce361-00093))_

> Before we do that, we have to dive back into declarations.
_(source: coding_little_go_book.pdf (source-range-810ce361-00114))_

> When we first looked at variables and declarations, we looked only at built-in types, like integers and strings.
_(source: coding_little_go_book.pdf (source-range-810ce361-00116))_

> Furthermore, you can skip the field name and rely on the order of the field declarations (though for the sake of clarity, you should only do this for structures with few fields):
_(source: coding_little_go_book.pdf (source-range-810ce361-00123))_

> Still, it comes down to some basic rules (like you can only declare variable once and := does declare the variable) and fundamental understanding (like new(X) or &X{} only allocate memory, but slices, maps and channels require more initialization and thus, make ).
_(source: coding_little_go_book.pdf (source-range-810ce361-00472))_


## Source

- [[coding-little-go-book]]
