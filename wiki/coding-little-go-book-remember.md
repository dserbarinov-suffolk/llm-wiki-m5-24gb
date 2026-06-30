---
page_id: coding-little-go-book-remember
page_kind: concept
summary: Remember: 4 statement(s) and 3 atom(s) from raw/coding_little_go_book.pdf.
page_family: topic-concept
sources: raw/coding_little_go_book.pdf
updated: 2026-06-30
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-remember@3ca322e9c0cceeb7557056ad339961b6
---

# Remember

What [[coding-little-go-book]] covers about remember:

## Statements

### Chapter 1 - The Basics / Variables and Declarations

- It's important that you remember that := is used to declare the variable as well as assign a value to it. Why? Because a variable can't be declared twice (not in the same scope anyway). If you try to run the following, you'll get an error. _(coding_little_go_book.pdf (source-range-23d24eb1-00083))_

- There's more to learn about declaration and assignments. For now, remember that you'll use var NAME TYPE when declaring a variable to its zero value, NAME := VALUE when declaring and assigning a value, and NAME = VALUE when assigning to a previously declared variable. _(coding_little_go_book.pdf (source-range-23d24eb1-00094))_

### Chapter 4 - Code Organization and Interfaces / Before You Continue

- Ultimately, how you structure your code around Go's workspace is something that you'll only feel comfortable with after you've written a couple of non-trivial projects. What's most important for you to remember is the tight relationship between package names and your directory structure (not just within a project, but within the entire workspace). _(coding_little_go_book.pdf (source-range-23d24eb1-00333))_

### Chapter 6 - Concurrency / Channels / Timeout

- Back to our select , there are a couple of things to play with. First, what happens if you add the default case back? Can you guess? Try it. If you aren't sure what's going on, remember that default fires immediately if no channel is available. _(coding_little_go_book.pdf (source-range-23d24eb1-00456))_


## Technical atoms

### Technical frame 1: Chapter 1 - The Basics / Variables and Declarations

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00083))_

> It's important that you remember that := is used to declare the variable as well as assign a value to it. Why? Because a variable can't be declared twice (not in the same scope anyway). If you try to run the following, you'll get an error.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00082))_

```
func main() {
  power := getPower()
}
func getPower() int {
  return 9001
}
```

### Technical frame 2: Chapter 1 - The Basics / Variables and Declarations

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00085))_

> The compiler will complain with no new variables on left side of := . This means that when we first declare a variable, we use := but on subsequent assignment, we use the assignment operator = . This makes a lot of sense, but it can be tricky for your muscle memory to remember when to switch between the two.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00084))_

```
func main() {
  power := 9000
  fmt.Printf("It's over %d\n", power)
// COMPILER ERROR:
  // no new variables on left side of :=
  power := 9001
  fmt.Printf("It's also over %d\n", power)
}
```

### Technical frame 3: Chapter 6 - Concurrency / Channels / Timeout

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00460))_

> The first available channel is chosen.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00457))_

> If you want though, you can receive it:


## Related pages

- [[coding-little-go-book-variable]] - shared statements and technical atoms: Variable shares source evidence from Chapter 1 - The Basics / Variables and Declarations: It's important that you remember that := is used to declare the variable as well as assign a value to it. Why? Because a variable can't be declared twice (not in the ... [truncated]; Variable shares technical record from Chapter 1 - The Basics / Variables and Declarations: func main() { power := getPower() } func getPower() int { return 9001 } (2 shared statement(s), 2 shared atom(s))
- [[coding-little-go-book-channel]] - shared statements and technical atoms: Channel shares source evidence from Chapter 6 - Concurrency / Channels / Timeout: Back to our select , there are a couple of things to play with. First, what happens if you add the default case back? Can you guess? Try it. If you aren't sure what' ... [truncated]; Channel shares technical record from Chapter 6 - Concurrency / Channels / Timeout: If you want though, you can receive it: (1 shared statement(s), 1 shared atom(s))
- [[coding-little-go-book-notice]] - shared technical atoms: Notice shares technical record from Chapter 1 - The Basics / Variables and Declarations: func main() { power := 9000 fmt.Printf("It's over %d\n", power) // COMPILER ERROR: // no new variables on left side of := power := 9001 fmt.Printf("It's also over %d\n", power) } (1 shared atom(s))
- [[coding-little-go-book-you-continue]] - shared statements: Before You Continue shares source evidence from Chapter 4 - Code Organization and Interfaces / Before You Continue: Ultimately, how you structure your code around Go's workspace is something that you'll only feel comfortable with after you've written a couple of non-trivial projec ... [truncated] (1 shared statement(s))

## Source

- [[coding-little-go-book]]
