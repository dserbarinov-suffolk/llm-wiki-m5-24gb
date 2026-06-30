---
page_id: coding-little-go-book-concurrent
page_kind: concept
summary: Concurrent: 4 statement(s) and 4 atom(s) from raw/coding_little_go_book.pdf.
page_family: topic-concept
sources: raw/coding_little_go_book.pdf
updated: 2026-06-30
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-concurrent@c7b48abe16c1c5c85ac072b29e126d13
---

# Concurrent

What [[coding-little-go-book]] covers about concurrent:

## Statements

### Chapter 6 - Concurrency / Synchronization

- Writing concurrent code requires that you pay specific attention to where and how you read and write values. In some ways, it's like programming without a garbage collector -- it requires that you think about your data from a new angle, always watchful for possible danger. Consider: _(coding_little_go_book.pdf (source-range-23d24eb1-00409))_

- The only concurrent thing you can safely do to a variable is to read from it. You can have as many readers as you want, but writes need to be synchronized. There are various ways to do this, including using some truly atomic operations that rely on special CPU instructions. However, the most common approach is to use a mutex: _(coding_little_go_book.pdf (source-range-23d24eb1-00415))_

### Chapter 6 - Concurrency / Before You Continue

- If you're new to the world of concurrent programming, it might all seem rather overwhelming. It categorically demands considerably more attention and care. Go aims to make it easier. _(coding_little_go_book.pdf (source-range-23d24eb1-00467))_

### Conclusion

- Last but not least is the built-in support for concurrency. There's little to say about goroutines other than they're effective and simple (simple to use anyway). It's a good abstraction. Channels are more complicated. I always think it's important to understand basics before using high-level wrappers. I do think learning about concurrent programming without channels is useful. Still, channels are implemented in a way that, to me, doesn't feel quite like a simple abstraction. They are almost their own fundamental building block. I say this because they change how you write and think about concurrent programming. Given how hard concurrent programming can be, that is definitely a good thing. _(coding_little_go_book.pdf (source-range-23d24eb1-00475))_


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

### Technical frame 3: Chapter 6 - Concurrency / Synchronization

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00417))_

> A mutex serializes access to the code under lock. The reason we simply define our lock as lock sync.Mutex is because the default value of a sync.Mutex is unlocked.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00416))_

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

### Technical frame 4: Conclusion

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00474))_

> Beyond this, Go gives us a simple but effective way to organize our code. Interfaces, return-based error handling, defer for resource management and a simple way to achieve composition.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00473))_

> Still, it comes down to some basic rules (like you can only declare variable once and := does declare the variable) and fundamental understanding (like new(X) or &X{} only allocate memory, but slices, maps and channels require more initialization and thus, make ).


## Related pages

- [[coding-little-go-book-programming]] - shared statements and technical atoms: Programming shares source evidence from Chapter 6 - Concurrency / Before You Continue: If you're new to the world of concurrent programming, it might all seem rather overwhelming. It categorically demands considerably more attention and care. Go aims t ... [truncated]; Programming shares technical record from Chapter 6 - Concurrency / Synchronization: package main import ( "fmt" "time" ) var counter = 0 func main() { for i := 0; i < 20; i++ { go incr() (2 shared statement(s), 3 shared atom(s))
- [[coding-little-go-book-code]] - shared statements and technical atoms: Code shares source evidence from Chapter 6 - Concurrency / Synchronization: Writing concurrent code requires that you pay specific attention to where and how you read and write values. In some ways, it's like programming without a garbage co ... [truncated]; Code shares technical record from Chapter 6 - Concurrency / Synchronization: package main import ( "fmt" "time" ) var counter = 0 func main() { for i := 0; i < 20; i++ { go incr() (1 shared statement(s), 3 shared atom(s))
- [[coding-little-go-book-garbage]] - shared technical atoms: Garbage shares technical record from Chapter 6 - Concurrency / Synchronization: package main import ( "fmt" "time" ) var counter = 0 func main() { for i := 0; i < 20; i++ { go incr() (2 shared atom(s))
- [[coding-little-go-book-channel]] - shared technical atoms: Channel shares technical record from Conclusion: Still, it comes down to some basic rules (like you can only declare variable once and := does declare the variable) and fundamental understanding (like new(X) or &X{ ... [truncated] (1 shared atom(s))
- [[coding-little-go-book-goroutine]] - shared technical atoms: Goroutine shares technical record from Conclusion: Still, it comes down to some basic rules (like you can only declare variable once and := does declare the variable) and fundamental understanding (like new(X) or &X{ ... [truncated] (1 shared atom(s))
- [[coding-little-go-book-reason]] - shared technical atoms: Reason shares technical record from Chapter 6 - Concurrency / Synchronization: package main import ( "fmt" "time" "sync" ) var ( counter = 0 lock sync.Mutex ) func main() { for i := 0; i < 20; i++ { go incr() } time.Sleep(time.Millisecond * 10) ... [truncated] (1 shared atom(s))
- [[coding-little-go-book-you-continue]] - shared statements: Before You Continue shares source evidence from Chapter 6 - Concurrency / Before You Continue: If you're new to the world of concurrent programming, it might all seem rather overwhelming. It categorically demands considerably more attention and care. Go aims t ... [truncated] (1 shared statement(s))

## Source

- [[coding-little-go-book]]
