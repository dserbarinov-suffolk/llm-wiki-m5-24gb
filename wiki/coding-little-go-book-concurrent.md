---
page_id: coding-little-go-book-concurrent
page_kind: concept
summary: Concurrent: 4 statement(s) and 4 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-concurrent@f623dbcefdb8ce531663978fe4ad6838
---

# Concurrent

What [[coding-little-go-book]] covers about concurrent:

## Statements

- Writing concurrent code requires that you pay specific attention to where and how you read and write values. _(coding_little_go_book.pdf (source-range-773b6275-00409))_
- The only concurrent thing you can safely do to a variable is to read from it. _(coding_little_go_book.pdf (source-range-773b6275-00415))_
- If you're new to the world of concurrent programming, it might all seem rather overwhelming. _(coding_little_go_book.pdf (source-range-773b6275-00467))_
- Given how hard concurrent programming can be, that is definitely a good thing. _(coding_little_go_book.pdf (source-range-773b6275-00475))_

## Technical atoms

> Context: Writing concurrent code requires that you pay specific attention to where and how you read and write values. In some ways, it's like programming without a garbage collector -- it requires that you think about your data from a new angle, always watchful for possible danger. Consider: What do you think the output will be?
_(context: coding_little_go_book.pdf (source-range-773b6275-00409, source-range-773b6275-00412))_

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
_(source: coding_little_go_book.pdf (source-range-773b6275-00410))_

> Context: Writing concurrent code requires that you pay specific attention to where and how you read and write values. In some ways, it's like programming without a garbage collector -- it requires that you think about your data from a new angle, always watchful for possible danger. Consider: What do you think the output will be?
_(context: coding_little_go_book.pdf (source-range-773b6275-00409, source-range-773b6275-00412))_

```
}
  time.Sleep(time.Millisecond * 10)
}
func incr() {
  counter++
  fmt.Println(counter)
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00411))_

> Context: The only concurrent thing you can safely do to a variable is to read from it. You can have as many readers as you want, but writes need to be synchronized. There are various ways to do this, including using some truly atomic operations that rely on special CPU instructions. However, the most common approach is to use a mutex: A mutex serializes access to the code under lock. The reason we simply define our lock as lock sync.Mutex is because the default value of a sync.Mutex is unlocked.
_(context: coding_little_go_book.pdf (source-range-773b6275-00415, source-range-773b6275-00417))_

```
package main
import (
  "fmt"
  "time"
  "sync"
)
var (
  counter = 0
  lock sync.Mutex
)
func main() {
  for i := 0; i < 20; i++ {
    go incr()
  }
  time.Sleep(time.Millisecond * 10)
}
func incr() {
  lock.Lock()
  defer lock.Unlock()
  counter++
  fmt.Println(counter)
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00416))_

> Context: I recently heard Go described as a boring language. Boring because it's easy to learn, easy to write and, most importantly, easy to read. Perhaps, I did this reality a disservice. We did spend three chapters talking about types and how to declare variables after all. Last but not least is the built-in support for concurrency. There's little to say about goroutines other than they're effective and simple (simple to use anyway). It's a good abstraction. Channels are more complicated. I always think it's important to understand basics before using high-level wrappers. I do think learning about concurrent programming without channels is useful. Still, channels are implemented in a way that, to me, doesn't feel quite like a simple abstraction. They are almost their own fundamental building block. I say this because they change how you write and think about concurrent programming. Given how hard concurrent programming can be, that is definitely a good thing.
_(context: coding_little_go_book.pdf (source-range-773b6275-00471, source-range-773b6275-00475))_

> Still, it comes down to some basic rules (like you can only declare variable once and := does declare the variable) and fundamental understanding (like new(X) or &X{} only allocate memory, but slices, maps and channels require more initialization and thus, make ).
_(source: coding_little_go_book.pdf (source-range-773b6275-00473))_


## Source

- [[coding-little-go-book]]
