---
page_id: coding-little-go-book-goroutine
page_kind: concept
summary: Goroutines: 13 statement(s) and 3 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-29
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-goroutine@ad2590e3479b624fef2ebcef870a4f79
---

# Goroutines

What [[coding-little-go-book]] covers about goroutines:

## Statements

### Chapter 6 - Concurrency / Goroutines

- A goroutine is similar to a thread, but it is scheduled by Go, not the OS. Code that runs in a goroutine can run concurrently with other code. Let's look at an example: _(coding_little_go_book.pdf (source-range-23d24eb1-00399))_

- There are a few interesting things going on here, but the most important is how we start a goroutine. We simply use the go keyword followed by the function we want to execute. If we just want to run a bit of code, such as the above, we can use an anonymous function. Do note that anonymous functions aren't only used with goroutines, however. _(coding_little_go_book.pdf (source-range-23d24eb1-00402))_

- Goroutines are easy to create and have little overhead. Multiple goroutines will end up running on the same underlying OS thread. This is often called an M:N threading model because we have M application threads (goroutines) running on N OS threads. The result is that a goroutine has a fraction of overhead (a few KB) than OS threads. On modern hardware, it's possible to have millions of goroutines. _(coding_little_go_book.pdf (source-range-23d24eb1-00404))_

- Furthermore, the complexity of mapping and scheduling is hidden. We just say this code should run concurrently and let Go worry about making it happen. _(coding_little_go_book.pdf (source-range-23d24eb1-00405))_

- If we go back to our example, you'll notice that we had to Sleep for a few milliseconds. That's because the main process exits before the goroutine gets a chance to execute (the process doesn't wait until all goroutines are finished before exiting). To solve this, we need to coordinate our code. _(coding_little_go_book.pdf (source-range-23d24eb1-00406))_


## Technical atoms

### Technical frame 1: Chapter 6 - Concurrency / Goroutines

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00402))_

> There are a few interesting things going on here, but the most important is how we start a goroutine. We simply use the go keyword followed by the function we want to execute. If we just want to run a bit of code, such as the above, we can use an anonymous function. Do note that anonymous functions aren't only used with goroutines, however.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00400))_

```
package main
import (
  "fmt"
  "time"
)
func main() {
  fmt.Println("start")
  go process()
  time.Sleep(time.Millisecond * 10) // this is bad, don't do this!
  fmt.Println("done")
}
```

### Technical frame 2: Chapter 6 - Concurrency / Goroutines

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00402))_

> There are a few interesting things going on here, but the most important is how we start a goroutine. We simply use the go keyword followed by the function we want to execute. If we just want to run a bit of code, such as the above, we can use an anonymous function. Do note that anonymous functions aren't only used with goroutines, however.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00401))_

```
func process() {
  fmt.Println("processing")
}
```

### Technical frame 3: Chapter 6 - Concurrency / Goroutines

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00404))_

> Goroutines are easy to create and have little overhead. Multiple goroutines will end up running on the same underlying OS thread. This is often called an M:N threading model because we have M application threads (goroutines) running on N OS threads. The result is that a goroutine has a fraction of overhead (a few KB) than OS threads. On modern hardware, it's possible to have millions of goroutines.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00403))_

```
go func() {
  fmt.Println("processing")
}()
```


## Related pages

- [[coding-little-go-book-concurrency]] - shared statements and technical atoms: Concurrency shares source evidence from Chapter 6 - Concurrency / Goroutines: A goroutine is similar to a thread, but it is scheduled by Go, not the OS. Code that runs in a goroutine can run concurrently with other code. Let's look at an example:; Concurrency shares technical record from Chapter 6 - Concurrency / Goroutines: package main import ( "fmt" "time" ) func main() { fmt.Println("start") go process() time.Sleep(time.Millisecond * 10) // this is bad, don't do this! fmt.Println("done") } (13 shared statement(s), 3 shared atom(s))
- [[coding-little-go-book-code]] - shared statements and technical atoms: Code shares source evidence from Chapter 6 - Concurrency / Goroutines: A goroutine is similar to a thread, but it is scheduled by Go, not the OS. Code that runs in a goroutine can run concurrently with other code. Let's look at an example:; Code shares technical record from Chapter 6 - Concurrency / Goroutines: package main import ( "fmt" "time" ) func main() { fmt.Println("start") go process() time.Sleep(time.Millisecond * 10) // this is bad, don't do this! fmt.Println("done") } (3 shared statement(s), 3 shared atom(s))
- [[coding-little-go-book-section-chapter-6-concurrency-goroutines-8aab6c69]] - source section: Chapter 6 - Concurrency / Goroutines shares source evidence from Chapter 6 - Concurrency / Goroutines: A goroutine is similar to a thread, but it is scheduled by Go, not the OS. Code that runs in a goroutine can run concurrently with other code. Let's look at an example:; Chapter 6 - Concurrency / Goroutines shares technical record from Chapter 6 - Concurrency / Goroutines: package main import ( "fmt" "time" ) func main() { fmt.Println("start") go process() time.Sleep(time.Millisecond * 10) // this is bad, don't do this! fmt.Println("done") } (13 shared statement(s), 3 shared atom(s))

## Source

- [[coding-little-go-book]]
