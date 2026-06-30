---
page_id: coding-little-go-book-garbage
page_kind: concept
summary: Garbage: 4 statement(s) and 2 atom(s) from raw/coding_little_go_book.pdf.
page_family: topic-concept
sources: raw/coding_little_go_book.pdf
updated: 2026-06-30
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-garbage@89f508021492bed83b65da192a9bbf77
---

# Garbage

What [[coding-little-go-book]] covers about garbage:

## Statements

### Chapter 1 - The Basics / Garbage Collected

- Some variables, when created, have an easy-to-define life. A variable local to a function, for example, disappears when the function exits. In other cases, it isn't so obvious -- at least to a compiler. For example, the lifetime of a variable returned by a function or referenced by other variables and objects can be tricky to determine. Without garbage collection, it's up to developers to free the memory associated with such variables at a point where the developer knows the variable isn't needed. How? In C, you'd literally free(str); the variable. _(coding_little_go_book.pdf (source-range-23d24eb1-00046))_

- Languages with garbage collectors (e.g., Ruby, Python, Java, JavaScript, C#, Go) are able to keep track of these and free them when they're no longer used. Garbage collection adds overhead, but it also eliminates a number of devastating bugs. _(coding_little_go_book.pdf (source-range-23d24eb1-00047))_

### Chapter 6 - Concurrency / Synchronization

- Writing concurrent code requires that you pay specific attention to where and how you read and write values. In some ways, it's like programming without a garbage collector -- it requires that you think about your data from a new angle, always watchful for possible danger. Consider: _(coding_little_go_book.pdf (source-range-23d24eb1-00409))_


## Technical atoms

### Technical frame 1: Chapter 6 - Concurrency / Synchronization

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00413))_

> If you think the output is 1, 2, ... 20 you're both right and wrong. It's true that if you run the above code, you'll sometimes get that output. However, the reality is that the behavior is undefined. Why? Because we potentially have multiple (two in this case) goroutines writing to the same variable, counter , at the same time. Or, just as bad, one goroutine would be reading counter while another writes to it.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00410))_

```
package main
import (
  "fmt"
  "time"
)
var counter = 0
func main() {
  for i := 0; i < 20; i++ {
    go incr()
```

### Technical frame 2: Chapter 6 - Concurrency / Synchronization

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00413))_

> If you think the output is 1, 2, ... 20 you're both right and wrong. It's true that if you run the above code, you'll sometimes get that output. However, the reality is that the behavior is undefined. Why? Because we potentially have multiple (two in this case) goroutines writing to the same variable, counter , at the same time. Or, just as bad, one goroutine would be reading counter while another writes to it.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00411))_

```
}
  time.Sleep(time.Millisecond * 10)
}
func incr() {
  counter++
  fmt.Println(counter)
}
```


## Related pages

- [[coding-little-go-book-programming]] - shared statements and technical atoms: Programming shares source evidence from Chapter 6 - Concurrency / Synchronization: Writing concurrent code requires that you pay specific attention to where and how you read and write values. In some ways, it's like programming without a garbage co ... [truncated]; Programming shares technical record from Chapter 6 - Concurrency / Synchronization: package main import ( "fmt" "time" ) var counter = 0 func main() { for i := 0; i < 20; i++ { go incr() (1 shared statement(s), 2 shared atom(s))
- [[coding-little-go-book-code]] - shared technical atoms: Code shares technical record from Chapter 6 - Concurrency / Synchronization: package main import ( "fmt" "time" ) var counter = 0 func main() { for i := 0; i < 20; i++ { go incr() (2 shared atom(s))
- [[coding-little-go-book-concurrent]] - shared technical atoms: Concurrent shares technical record from Chapter 6 - Concurrency / Synchronization: package main import ( "fmt" "time" ) var counter = 0 func main() { for i := 0; i < 20; i++ { go incr() (2 shared atom(s))
- [[coding-little-go-book-language]] - shared statements: Language shares source evidence from Chapter 1 - The Basics / Garbage Collected: Languages with garbage collectors (e.g., Ruby, Python, Java, JavaScript, C#, Go) are able to keep track of these and free them when they're no longer used. Garbage c ... [truncated] (1 shared statement(s))
- [[coding-little-go-book-ruby]] - shared statements: Ruby shares source evidence from Chapter 1 - The Basics / Garbage Collected: Languages with garbage collectors (e.g., Ruby, Python, Java, JavaScript, C#, Go) are able to keep track of these and free them when they're no longer used. Garbage c ... [truncated] (1 shared statement(s))

## Source

- [[coding-little-go-book]]
