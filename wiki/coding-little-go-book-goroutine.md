---
page_id: coding-little-go-book-goroutine
page_kind: concept
summary: Goroutines: 13 statement(s) and 3 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-goroutine@0ff1b5fbc852fa259963a7c20cec2bd5
---

# Goroutines

What [[coding-little-go-book]] covers about goroutines:

## Statements

- Code that runs in a goroutine can run concurrently with other code. _(coding_little_go_book.pdf (source-range-773b6275-00399))_
- If we just want to run a bit of code, such as the above, we can use an anonymous function. _(coding_little_go_book.pdf (source-range-773b6275-00402))_
- There are a few interesting things going on here, but the most important is how we start a goroutine. _(coding_little_go_book.pdf (source-range-773b6275-00402))_
- Goroutines are easy to create and have little overhead. _(coding_little_go_book.pdf (source-range-773b6275-00404))_
- Multiple goroutines will end up running on the same underlying OS thread. _(coding_little_go_book.pdf (source-range-773b6275-00404))_
- The result is that a goroutine has a fraction of overhead (a few KB) than OS threads. _(coding_little_go_book.pdf (source-range-773b6275-00404))_
- This is often called an M:N threading model because we have M application threads (goroutines) running on N OS threads. _(coding_little_go_book.pdf (source-range-773b6275-00404))_
- On modern hardware, it's possible to have millions of goroutines. _(coding_little_go_book.pdf (source-range-773b6275-00404))_
- Furthermore, the complexity of mapping and scheduling is hidden. _(coding_little_go_book.pdf (source-range-773b6275-00405))_
- We just say this code should run concurrently and let Go worry about making it happen. _(coding_little_go_book.pdf (source-range-773b6275-00405))_
- If we go back to our example, you'll notice that we had to Sleep for a few milliseconds. _(coding_little_go_book.pdf (source-range-773b6275-00406))_
- To solve this, we need to coordinate our code. _(coding_little_go_book.pdf (source-range-773b6275-00406))_
- That's because the main process exits before the goroutine gets a chance to execute (the process doesn't wait until all goroutines are finished before exiting). _(coding_little_go_book.pdf (source-range-773b6275-00406))_

## Technical atoms

> Context: A goroutine is similar to a thread, but it is scheduled by Go, not the OS. Code that runs in a goroutine can run concurrently with other code. Let's look at an example: There are a few interesting things going on here, but the most important is how we start a goroutine. We simply use the go keyword followed by the function we want to execute. If we just want to run a bit of code, such as the above, we can use an anonymous function. Do note that anonymous functions aren't only used with goroutines, however.
_(context: coding_little_go_book.pdf (source-range-773b6275-00399, source-range-773b6275-00402))_

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
_(source: coding_little_go_book.pdf (source-range-773b6275-00400))_

> Context: A goroutine is similar to a thread, but it is scheduled by Go, not the OS. Code that runs in a goroutine can run concurrently with other code. Let's look at an example: There are a few interesting things going on here, but the most important is how we start a goroutine. We simply use the go keyword followed by the function we want to execute. If we just want to run a bit of code, such as the above, we can use an anonymous function. Do note that anonymous functions aren't only used with goroutines, however.
_(context: coding_little_go_book.pdf (source-range-773b6275-00399, source-range-773b6275-00402))_

```
func process() {
  fmt.Println("processing")
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00401))_

> Context: There are a few interesting things going on here, but the most important is how we start a goroutine. We simply use the go keyword followed by the function we want to execute. If we just want to run a bit of code, such as the above, we can use an anonymous function. Do note that anonymous functions aren't only used with goroutines, however. Goroutines are easy to create and have little overhead. Multiple goroutines will end up running on the same underlying OS thread. This is often called an M:N threading model because we have M application threads (goroutines) running on N OS threads. The result is that a goroutine has a fraction of overhead (a few KB) than OS threads. On modern hardware, it's possible to have millions of goroutines.
_(context: coding_little_go_book.pdf (source-range-773b6275-00402, source-range-773b6275-00404))_

```
go func() {
  fmt.Println("processing")
}()
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00403))_


## Source

- [[coding-little-go-book]]
