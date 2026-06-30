---
page_id: coding-little-go-book-compiler
page_kind: concept
summary: Compiler: 4 statement(s) and 2 atom(s) from raw/coding_little_go_book.pdf.
page_family: topic-concept
sources: raw/coding_little_go_book.pdf
updated: 2026-06-30
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-compiler@730cea1c5335c2c448744f94da482d8f
---

# Compiler

What [[coding-little-go-book]] covers about compiler:

## Statements

### Chapter 1 - The Basics / Static Typing

- Being statically typed means that variables must be of a specific type (int, string, bool, []byte, etc.). This is either achieved by specifying the type when the variable is declared or, in many cases, letting the compiler infer the type (we'll look at examples shortly). There's a lot more that can be said about static typing, but I believe it's something better understood by looking at code. If you're used to dynamically typed languages, you might find this cumbersome. You're not wrong, but there are advantages, especially when you pair static typing with compilation. The two are often conflated. It's true that when you have one, you normally have the other but it isn't a hard rule. With a rigid type system, a compiler is able to detect problems beyond mere syntactical mistakes as well as make further optimizations. _(coding_little_go_book.pdf (source-range-23d24eb1-00037))_

### Chapter 1 - The Basics / Variables and Declarations

- The compiler will complain with no new variables on left side of := . This means that when we first declare a variable, we use := but on subsequent assignment, we use the assignment operator = . This makes a lot of sense, but it can be tricky for your muscle memory to remember when to switch between the two. _(coding_little_go_book.pdf (source-range-23d24eb1-00085))_

### Chapter 2 - Structures / Declarations and Initializations

- Note: The trailing , in the above structure is required. Without it, the compiler will give an error. You'll appreciate the required consistency, especially if you've used a language or format that enforces the opposite. _(coding_little_go_book.pdf (source-range-23d24eb1-00120))_

### Chapter 3 - Maps, Arrays and Slices / Slices

- Here, the output is going to be [0, 0, 0, 0, 0, 9332] . Maybe you thought it would be [9332, 0, 0, 0, 0] ? To a human, that might seem logical. To a compiler, you're telling it to append a value to a slice that already holds 5 values. _(coding_little_go_book.pdf (source-range-23d24eb1-00220))_


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

### Technical frame 2: Chapter 3 - Maps, Arrays and Slices / Slices

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00220))_

> Here, the output is going to be [0, 0, 0, 0, 0, 9332] . Maybe you thought it would be [9332, 0, 0, 0, 0] ? To a human, that might seem logical. To a compiler, you're telling it to append a value to a slice that already holds 5 values.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00219))_

```
func main() {
  scores := make([]int, 5)
  scores = append(scores, 9332)
  fmt.Println(scores)
}
```


## Related pages

- [[coding-little-go-book-value]] - shared statements and technical atoms: Value shares source evidence from Chapter 3 - Maps, Arrays and Slices / Slices: Here, the output is going to be [0, 0, 0, 0, 0, 9332] . Maybe you thought it would be [9332, 0, 0, 0, 0] ? To a human, that might seem logical. To a compiler, you're ... [truncated]; Value shares technical record from Chapter 2 - Structures / Declarations and Initializations: goku := Saiyan{ Name: "Goku", Power: 9000, } (1 shared statement(s), 2 shared atom(s))
- [[coding-little-go-book-slice]] - shared statements and technical atoms: Slice shares source evidence from Chapter 3 - Maps, Arrays and Slices / Slices: Here, the output is going to be [0, 0, 0, 0, 0, 9332] . Maybe you thought it would be [9332, 0, 0, 0, 0] ? To a human, that might seem logical. To a compiler, you're ... [truncated]; Slice shares technical record from Chapter 3 - Maps, Arrays and Slices / Slices: func main() { scores := make([]int, 5) scores = append(scores, 9332) fmt.Println(scores) } (1 shared statement(s), 1 shared atom(s))
- [[coding-little-go-book-note]] - shared technical atoms: Note shares technical record from Chapter 2 - Structures / Declarations and Initializations: goku := Saiyan{ Name: "Goku", Power: 9000, } (1 shared atom(s))
- [[coding-little-go-book-structure]] - shared technical atoms: Structure shares technical record from Chapter 2 - Structures / Declarations and Initializations: goku := Saiyan{ Name: "Goku", Power: 9000, } (1 shared atom(s))
- [[coding-little-go-book-system]] - shared statements: System shares source evidence from Chapter 1 - The Basics / Static Typing: Being statically typed means that variables must be of a specific type (int, string, bool, []byte, etc.). This is either achieved by specifying the type when the var ... [truncated] (1 shared statement(s))
- [[coding-little-go-book-type]] - shared statements: Type shares source evidence from Chapter 1 - The Basics / Static Typing: Being statically typed means that variables must be of a specific type (int, string, bool, []byte, etc.). This is either achieved by specifying the type when the var ... [truncated] (1 shared statement(s))
- [[coding-little-go-book-variable]] - shared statements: Variable shares source evidence from Chapter 1 - The Basics / Variables and Declarations: The compiler will complain with no new variables on left side of := . This means that when we first declare a variable, we use := but on subsequent assignment, we us ... [truncated] (1 shared statement(s))

## Source

- [[coding-little-go-book]]
