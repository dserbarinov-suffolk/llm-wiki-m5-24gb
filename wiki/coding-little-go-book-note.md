---
page_id: coding-little-go-book-note
page_kind: concept
summary: Note: 6 statement(s) and 2 atom(s) from raw/coding_little_go_book.pdf.
page_family: topic-concept
sources: raw/coding_little_go_book.pdf
updated: 2026-06-30
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-note@2de14c5bd780b796fbe3ce7e5ea21716
---

# Note

What [[coding-little-go-book]] covers about note:

## Statements

### Chapter 1 - The Basics / Imports

- Another thing to note is that Go's standard library is well documented. You can head over to https://golang.org/pkg/fmt/#Println to learn more about the Println function that we used. You can click on that section header and see the source code. Also, scroll to the top to learn more about Go's formatting capabilities. _(coding_little_go_book.pdf (source-range-23d24eb1-00068))_

### Chapter 2 - Structures / Declarations and Initializations

- Note: The trailing , in the above structure is required. Without it, the compiler will give an error. You'll appreciate the required consistency, especially if you've used a language or format that enforces the opposite. _(coding_little_go_book.pdf (source-range-23d24eb1-00120))_

- Note that we're still passing a copy of goku's value to Super it just so happens that goku's value has become an address. That copy is the same address as the original, which is what that indirection buys us. Think of it as copying the directions to a restaurant. What you have is a copy, but it still points to the same restaurant as the original. _(coding_little_go_book.pdf (source-range-23d24eb1-00133))_

### Chapter 3 - Maps, Arrays and Slices / Slices

- This creates a slice with a length of 0 but with a capacity of 10. (If you're paying attention, you'll note that make and len are overloaded. Go is a language that, to the frustration of some, makes use of features which aren't exposed for developers to use.) _(coding_little_go_book.pdf (source-range-23d24eb1-00206))_

### Chapter 5 - Tidbits / Error Handling

- As a final note, Go does have panic and recover functions. panic is like throwing an exception while recover is like catch ; they are rarely used. _(coding_little_go_book.pdf (source-range-23d24eb1-00350))_

### Chapter 5 - Tidbits / Empty Interface and Conversions

- Note that if the underlying type is not int , the above will result in an error. _(coding_little_go_book.pdf (source-range-23d24eb1-00373))_


## Technical atoms

### Technical frame 1: Chapter 2 - Structures / Declarations and Initializations

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00120))_

> Note: The trailing , in the above structure is required. Without it, the compiler will give an error. You'll appreciate the required consistency, especially if you've used a language or format that enforces the opposite.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00119))_

```
goku := Saiyan{
  Name: "Goku",
  Power: 9000,
}
```

### Technical frame 2: Chapter 5 - Tidbits / Empty Interface and Conversions

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00373))_

> Note that if the underlying type is not int , the above will result in an error.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00372))_

```
return a.(int) + b.(int)
```


## Related pages

- [[coding-little-go-book-structure]] - shared statements and technical atoms: Structure shares source evidence from Chapter 2 - Structures / Declarations and Initializations: Note: The trailing , in the above structure is required. Without it, the compiler will give an error. You'll appreciate the required consistency, especially if you'v ... [truncated]; Structure shares technical record from Chapter 2 - Structures / Declarations and Initializations: goku := Saiyan{ Name: "Goku", Power: 9000, } (1 shared statement(s), 1 shared atom(s))
- [[coding-little-go-book-type]] - shared statements and technical atoms: Type shares source evidence from Chapter 5 - Tidbits / Empty Interface and Conversions: Note that if the underlying type is not int , the above will result in an error.; Type shares technical record from Chapter 5 - Tidbits / Empty Interface and Conversions: return a.(int) + b.(int) (1 shared statement(s), 1 shared atom(s))
- [[coding-little-go-book-value]] - shared statements and technical atoms: Value shares source evidence from Chapter 2 - Structures / Declarations and Initializations: Note that we're still passing a copy of goku's value to Super it just so happens that goku's value has become an address. That copy is the same address as the origin ... [truncated]; Value shares technical record from Chapter 2 - Structures / Declarations and Initializations: goku := Saiyan{ Name: "Goku", Power: 9000, } (1 shared statement(s), 1 shared atom(s))
- [[coding-little-go-book-compiler]] - shared technical atoms: Compiler shares technical record from Chapter 2 - Structures / Declarations and Initializations: goku := Saiyan{ Name: "Goku", Power: 9000, } (1 shared atom(s))
- [[coding-little-go-book-copy]] - shared statements: Copy shares source evidence from Chapter 2 - Structures / Declarations and Initializations: Note that we're still passing a copy of goku's value to Super it just so happens that goku's value has become an address. That copy is the same address as the origin ... [truncated] (1 shared statement(s))

## Source

- [[coding-little-go-book]]
