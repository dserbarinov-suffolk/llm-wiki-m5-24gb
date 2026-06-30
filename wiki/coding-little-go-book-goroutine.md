---
page_id: coding-little-go-book-goroutine
page_kind: concept
summary: Goroutine: 7 statement(s) and 4 atom(s) from raw/coding_little_go_book.pdf.
page_family: topic-concept
sources: raw/coding_little_go_book.pdf
updated: 2026-06-30
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-goroutine@7fef59a6eac4ca90dbe50d330d2bfb79
---

# Goroutine

What [[coding-little-go-book]] covers about goroutine:

## Statements

### Chapter 6 - Concurrency / Goroutines

- A goroutine is similar to a thread, but it is scheduled by Go, not the OS. Code that runs in a goroutine can run concurrently with other code. Let's look at an example: _(coding_little_go_book.pdf (source-range-23d24eb1-00399))_

- Goroutines are easy to create and have little overhead. Multiple goroutines will end up running on the same underlying OS thread. This is often called an M:N threading model because we have M application threads (goroutines) running on N OS threads. The result is that a goroutine has a fraction of overhead (a few KB) than OS threads. On modern hardware, it's possible to have millions of goroutines. _(coding_little_go_book.pdf (source-range-23d24eb1-00404))_

- If we go back to our example, you'll notice that we had to Sleep for a few milliseconds. That's because the main process exits before the goroutine gets a chance to execute (the process doesn't wait until all goroutines are finished before exiting). To solve this, we need to coordinate our code. _(coding_little_go_book.pdf (source-range-23d24eb1-00406))_

### Chapter 6 - Concurrency / Synchronization

- Creating goroutines is trivial, and they are so cheap that we can start many; however, concurrent code needs to be coordinated. To help with this problem, Go provides channels . Before we look at channels , I think it's important to understand a little bit about the basics of concurrent programming. _(coding_little_go_book.pdf (source-range-23d24eb1-00408))_

### Chapter 6 - Concurrency / Before You Continue

- Goroutines effectively abstract what's needed to run concurrent code. Channels help eliminate some serious bugs that can happen when data is shared by eliminating the sharing of data. This doesn't just eliminate bugs, but it changes how one approaches concurrent programming. You start to think about concurrency with respect to message passing, rather than dangerous areas of code. _(coding_little_go_book.pdf (source-range-23d24eb1-00468))_

### Conclusion

- Last but not least is the built-in support for concurrency. There's little to say about goroutines other than they're effective and simple (simple to use anyway). It's a good abstraction. Channels are more complicated. I always think it's important to understand basics before using high-level wrappers. I do think learning about concurrent programming without channels is useful. Still, channels are implemented in a way that, to me, doesn't feel quite like a simple abstraction. They are almost their own fundamental building block. I say this because they change how you write and think about concurrent programming. Given how hard concurrent programming can be, that is definitely a good thing. _(coding_little_go_book.pdf (source-range-23d24eb1-00475))_


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

### Technical frame 4: Conclusion

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00474))_

> Beyond this, Go gives us a simple but effective way to organize our code. Interfaces, return-based error handling, defer for resource management and a simple way to achieve composition.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00473))_

> Still, it comes down to some basic rules (like you can only declare variable once and := does declare the variable) and fundamental understanding (like new(X) or &X{} only allocate memory, but slices, maps and channels require more initialization and thus, make ).


## Related pages

- [[coding-little-go-book-code]] - shared statements and technical atoms: Code shares source evidence from Chapter 6 - Concurrency / Goroutines: A goroutine is similar to a thread, but it is scheduled by Go, not the OS. Code that runs in a goroutine can run concurrently with other code. Let's look at an example:; Code shares technical record from Chapter 6 - Concurrency / Goroutines: package main import ( "fmt" "time" ) func main() { fmt.Println("start") go process() time.Sleep(time.Millisecond * 10) // this is bad, don't do this! fmt.Println("done") } (1 shared statement(s), 3 shared atom(s))
- [[coding-little-go-book-channel]] - shared technical atoms: Channel shares technical record from Conclusion: Still, it comes down to some basic rules (like you can only declare variable once and := does declare the variable) and fundamental understanding (like new(X) or &X{ ... [truncated] (1 shared atom(s))
- [[coding-little-go-book-concurrent]] - shared technical atoms: Concurrent shares technical record from Conclusion: Still, it comes down to some basic rules (like you can only declare variable once and := does declare the variable) and fundamental understanding (like new(X) or &X{ ... [truncated] (1 shared atom(s))
- [[coding-little-go-book-programming]] - shared technical atoms: Programming shares technical record from Conclusion: Still, it comes down to some basic rules (like you can only declare variable once and := does declare the variable) and fundamental understanding (like new(X) or &X{ ... [truncated] (1 shared atom(s))
- [[coding-little-go-book-you-continue]] - shared statements: Before You Continue shares source evidence from Chapter 6 - Concurrency / Before You Continue: Goroutines effectively abstract what's needed to run concurrent code. Channels help eliminate some serious bugs that can happen when data is shared by eliminating th ... [truncated] (1 shared statement(s))
- [[coding-little-go-book-section-chapter-6-concurrency-goroutines-8aab6c69]] - source section: Chapter 6 - Concurrency / Goroutines shares source evidence from Chapter 6 - Concurrency / Goroutines: A goroutine is similar to a thread, but it is scheduled by Go, not the OS. Code that runs in a goroutine can run concurrently with other code. Let's look at an example:; Chapter 6 - Concurrency / Goroutines shares technical record from Chapter 6 - Concurrency / Goroutines: package main import ( "fmt" "time" ) func main() { fmt.Println("start") go process() time.Sleep(time.Millisecond * 10) // this is bad, don't do this! fmt.Println("done") } (13 shared statement(s), 3 shared atom(s))

## Source

- [[coding-little-go-book]]
