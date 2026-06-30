---
page_id: coding-little-go-book-reason
page_kind: concept
summary: Reason: 6 statement(s) and 3 atom(s) from raw/coding_little_go_book.pdf.
page_family: topic-concept
sources: raw/coding_little_go_book.pdf
updated: 2026-06-30
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-reason@d76a8acded488e90c708645a6302882f
---

# Reason

What [[coding-little-go-book]] covers about reason:

## Statements

### Introduction

- That leaves us with an important question: why Go? For me, there are two compelling reasons. The first is that it's a relatively simple language with a relatively simple standard library. In a lot of ways, the incremental nature of Go is to simplify some of the complexity we've seen being added to languages over the last couple of decades. The other reason is that for many developers, it will complement your existing arsenal. _(coding_little_go_book.pdf (source-range-23d24eb1-00014))_

- There are other areas where Go excels. For example, there are no dependencies when running a compiled Go program. You don't have to worry if your users have Ruby or the JVM installed, and if so, what version. For this reason, Go is becoming increasingly popular as a language for command-line interface programs and other types of utility programs you need to distribute (e.g., a log collector). _(coding_little_go_book.pdf (source-range-23d24eb1-00017))_

### Chapter 3 - Maps, Arrays and Slices / Slices

- But that changes the intent of our original code. Appending to a slice of length 0 will set the first element. For whatever reason, our crashing code wanted to set the element at index 7. To do this, we can re-slice our slice: _(coding_little_go_book.pdf (source-range-23d24eb1-00211))_

### Chapter 5 - Tidbits / go fmt

- I know, you have your own style and you want to stick to it. That's what I did for a long time, but I'm glad I eventually gave in. A big reason for this is the go fmt command. It's easy to use and authoritative (so no one argues over meaningless preferences). _(coding_little_go_book.pdf (source-range-23d24eb1-00357))_

### Chapter 6 - Concurrency

- Go is often described as a concurrent-friendly language. The reason for this is that it provides a simple syntax over two powerful mechanisms: goroutines and channels. _(coding_little_go_book.pdf (source-range-23d24eb1-00397))_

### Chapter 6 - Concurrency / Synchronization

- A mutex serializes access to the code under lock. The reason we simply define our lock as lock sync.Mutex is because the default value of a sync.Mutex is unlocked. _(coding_little_go_book.pdf (source-range-23d24eb1-00417))_


## Technical atoms

### Technical frame 1: Chapter 3 - Maps, Arrays and Slices / Slices

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00213))_

> How large can we resize a slice? Up to its capacity which, in this case, is 10. You might be thinking this doesn't actually solve the fixed-length issue of arrays. It turns out that append is pretty special. If the underlying array is full, it will create a new larger array and copy the values over (this is exactly how dynamic arrays work in PHP , Python, Ruby, JavaScript, ...). This is why, in the example above that used append , we had to re-assign the value returned by append to our scores va

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00212))_

```
func main() {
  scores := make([]int, 0, 10)
  scores = scores[0:8]
  scores[7] = 9033
  fmt.Println(scores)
}
```

### Technical frame 2: Chapter 5 - Tidbits / go fmt

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00360))_

> Give it a try. It does more than indent your code; it also aligns field declarations and alphabetically orders imports.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00358))_

> When you're inside a project, you can apply the formatting rule to it and all sub-projects via:

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


## Related pages

- [[coding-little-go-book-code]] - shared statements and technical atoms: Code shares source evidence from Chapter 3 - Maps, Arrays and Slices / Slices: But that changes the intent of our original code. Appending to a slice of length 0 will set the first element. For whatever reason, our crashing code wanted to set t ... [truncated]; Code shares technical record from Chapter 3 - Maps, Arrays and Slices / Slices: func main() { scores := make([]int, 0, 10) scores = scores[0:8] scores[7] = 9033 fmt.Println(scores) } (1 shared statement(s), 2 shared atom(s))
- [[coding-little-go-book-array]] - shared technical atoms: Array shares technical record from Chapter 3 - Maps, Arrays and Slices / Slices: func main() { scores := make([]int, 0, 10) scores = scores[0:8] scores[7] = 9033 fmt.Println(scores) } (1 shared atom(s))
- [[coding-little-go-book-concurrent]] - shared technical atoms: Concurrent shares technical record from Chapter 6 - Concurrency / Synchronization: package main import ( "fmt" "time" "sync" ) var ( counter = 0 lock sync.Mutex ) func main() { for i := 0; i < 20; i++ { go incr() } time.Sleep(time.Millisecond * 10) ... [truncated] (1 shared atom(s))
- [[coding-little-go-book-copy]] - shared technical atoms: Copy shares technical record from Chapter 3 - Maps, Arrays and Slices / Slices: func main() { scores := make([]int, 0, 10) scores = scores[0:8] scores[7] = 9033 fmt.Println(scores) } (1 shared atom(s))
- [[coding-little-go-book-ruby]] - shared technical atoms: Ruby shares technical record from Chapter 3 - Maps, Arrays and Slices / Slices: func main() { scores := make([]int, 0, 10) scores = scores[0:8] scores[7] = 9033 fmt.Println(scores) } (1 shared atom(s))
- [[coding-little-go-book-slice]] - shared technical atoms: Slice shares technical record from Chapter 3 - Maps, Arrays and Slices / Slices: func main() { scores := make([]int, 0, 10) scores = scores[0:8] scores[7] = 9033 fmt.Println(scores) } (1 shared atom(s))
- [[coding-little-go-book-value]] - shared technical atoms: Value shares technical record from Chapter 3 - Maps, Arrays and Slices / Slices: func main() { scores := make([]int, 0, 10) scores = scores[0:8] scores[7] = 9033 fmt.Println(scores) } (1 shared atom(s))

## Source

- [[coding-little-go-book]]
