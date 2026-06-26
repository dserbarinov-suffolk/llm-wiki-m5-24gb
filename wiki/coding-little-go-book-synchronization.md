---
page_id: coding-little-go-book-synchronization
page_kind: concept
summary: Synchronization: 22 statement(s) and 4 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-synchronization@4d5d0a3f781c30794f7267fd85ce6b75
---

# Synchronization

What [[coding-little-go-book]] covers about synchronization:

## Statements

- Creating goroutines is trivial, and they are so cheap that we can start many; however, concurrent code needs to be coordinated. _(coding_little_go_book.pdf (source-range-773b6275-00408))_
- To help with this problem, Go provides channels . _(coding_little_go_book.pdf (source-range-773b6275-00408))_
- In some ways, it's like programming without a garbage collector -- it requires that you think about your data from a new angle, always watchful for possible danger. _(coding_little_go_book.pdf (source-range-773b6275-00409))_
- Writing concurrent code requires that you pay specific attention to where and how you read and write values. _(coding_little_go_book.pdf (source-range-773b6275-00409))_
- However, the reality is that the behavior is undefined. _(coding_little_go_book.pdf (source-range-773b6275-00413))_
- If you think the output is 1, 2, ... _(coding_little_go_book.pdf (source-range-773b6275-00413))_
- Because we potentially have multiple (two in this case) goroutines writing to the same variable, counter , at the same time. _(coding_little_go_book.pdf (source-range-773b6275-00413))_
- If you run this example, you'll see that very often the numbers are printed in a weird order, and/or numbers are duplicated/missing. _(coding_little_go_book.pdf (source-range-773b6275-00414))_
- There are worse possibilities too, such as system crashes or accessing an arbitrary piece of data and incrementing it! _(coding_little_go_book.pdf (source-range-773b6275-00414))_
- The only concurrent thing you can safely do to a variable is to read from it. _(coding_little_go_book.pdf (source-range-773b6275-00415))_
- You can have as many readers as you want, but writes need to be synchronized. _(coding_little_go_book.pdf (source-range-773b6275-00415))_
- There are various ways to do this, including using some truly atomic operations that rely on special CPU instructions. _(coding_little_go_book.pdf (source-range-773b6275-00415))_
- The reason we simply define our lock as lock sync.Mutex is because the default value of a sync.Mutex is unlocked. _(coding_little_go_book.pdf (source-range-773b6275-00417))_
- While it might be tempting to use coarse locks (locks that cover a large amount of code), that undermines the very reason we're doing concurrent programming in the first place. _(coding_little_go_book.pdf (source-range-773b6275-00418))_

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

> Context: Is that really a danger? Yes, absolutely. counter++ might seem like a simple line of code, but it actually gets broken down into multiple assembly statements -- the exact nature is dependent on the platform that you're running. If you run this example, you'll see that very often the numbers are printed in a weird order, and/or numbers are duplicated/missing. There are worse possibilities too, such as system crashes or accessing an arbitrary piece of data and incrementing it!
_(context: coding_little_go_book.pdf (source-range-773b6275-00414))_

> It's true that if you run the above code, you'll sometimes get that output.
_(source: coding_little_go_book.pdf (source-range-773b6275-00413))_

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


## Source

- [[coding-little-go-book]]
