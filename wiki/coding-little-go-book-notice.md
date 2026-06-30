---
page_id: coding-little-go-book-notice
page_kind: concept
summary: Notice: 4 statement(s) and 2 atom(s) from raw/coding_little_go_book.pdf.
page_family: topic-concept
sources: raw/coding_little_go_book.pdf
updated: 2026-06-30
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-notice@3a97dacf0f9205ecf4631994de312c33
---

# Notice

What [[coding-little-go-book]] covers about notice:

## Statements

### Chapter 1 - The Basics / Variables and Declarations

- If you read the error message closely, you'll notice that variables is plural. That's because Go lets you assign multiple variables (using either = or := ): _(coding_little_go_book.pdf (source-range-23d24eb1-00086))_

### Chapter 4 - Code Organization and Interfaces / Packages

- Notice that the name of the package is the same as the name of the folder. Also, obviously, we aren't actually accessing the database. We're just using this as an example to show how to organize code. _(coding_little_go_book.pdf (source-range-23d24eb1-00277))_

### Chapter 6 - Concurrency / Goroutines

- If we go back to our example, you'll notice that we had to Sleep for a few milliseconds. That's because the main process exits before the goroutine gets a chance to execute (the process doesn't wait until all goroutines are finished before exiting). To solve this, we need to coordinate our code. _(coding_little_go_book.pdf (source-range-23d24eb1-00406))_

### Chapter 6 - Concurrency / Channels

- Notice that the only shared state is the channel, which we can safely receive from and send to concurrently. Channels provide all of the synchronization code we need and also ensure that, at any given time, only one goroutine has access to a specific piece of data. _(coding_little_go_book.pdf (source-range-23d24eb1-00431))_


## Technical atoms

### Technical frame 1: Chapter 1 - The Basics / Variables and Declarations

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

### Technical frame 2: Chapter 1 - The Basics / Variables and Declarations

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00088))_

> As long as one of the variables is new, := can be used. Consider:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00087))_

```
func main() {
  name, power := "Goku", 9000
  fmt.Printf("%s's power is over %d\n", name, power)
}
```


## Related pages

- [[coding-little-go-book-variable]] - shared statements and technical atoms: Variable shares source evidence from Chapter 1 - The Basics / Variables and Declarations: If you read the error message closely, you'll notice that variables is plural. That's because Go lets you assign multiple variables (using either = or := ):; Variable shares technical record from Chapter 1 - The Basics / Variables and Declarations: func main() { power := 9000 fmt.Printf("It's over %d\n", power) // COMPILER ERROR: // no new variables on left side of := power := 9001 fmt.Printf("It's also over %d\n", power) } (1 shared statement(s), 2 shared atom(s))
- [[coding-little-go-book-remember]] - shared technical atoms: Remember shares technical record from Chapter 1 - The Basics / Variables and Declarations: func main() { power := 9000 fmt.Printf("It's over %d\n", power) // COMPILER ERROR: // no new variables on left side of := power := 9001 fmt.Printf("It's also over %d\n", power) } (1 shared atom(s))
- [[coding-little-go-book-package]] - shared statements: Package shares source evidence from Chapter 4 - Code Organization and Interfaces / Packages: Notice that the name of the package is the same as the name of the folder. Also, obviously, we aren't actually accessing the database. We're just using this as an ex ... [truncated] (1 shared statement(s))

## Source

- [[coding-little-go-book]]
