---
page_id: coding-little-go-book-worker
page_kind: concept
summary: Worker: 5 statement(s) and 3 atom(s) from raw/coding_little_go_book.pdf.
page_family: topic-concept
sources: raw/coding_little_go_book.pdf
updated: 2026-06-30
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-worker@5084beeca54e53c9b016b43afb376a44
---

# Worker

What [[coding-little-go-book]] covers about worker:

## Statements

### Chapter 6 - Concurrency / Channels

- Our worker is simple. It waits until data is available then "processes" it. Dutifully, it does this in a loop, forever waiting for more data to process. To use this, the first thing we'd do is start some workers: And then we can give them some work: Here's the complete code to make it run: } func (w Worker) process(c chan int) { for { data := <-c fmt.Printf("worker %d got %d\n", w.id, data) } } c := make( chan int) for i := 0; i < 5; i++ { worker := &Worker{id: i} go worker.process(c) } for { c <- rand.Int() time.Sleep(time.Millisecond * 50) } package main import ( "fmt" "time" "math/rand" ) func main() { c := make( chan int) for i := 0; i < 5; i++ { worker := &Worker{id: i} go worker.process(c) } for { c <- rand.Int() time.Sleep(time.Millisecond * 50) } } type Worker struct { id int } func (w *Worker) process(c chan int) { for { data := <-c fmt.Printf("worker %d got %d\n", w.id, data) } } _(coding_little_go_book.pdf (source-range-23d24eb1-00429))_

- We don't know which worker is going to get what data. What we do know, what Go guarantees, is that the data we send to a channel will only be received by a single receiver. _(coding_little_go_book.pdf (source-range-23d24eb1-00430))_

### Chapter 6 - Concurrency / Channels / Buffered Channels

- In cases where you need high guarantees that the data is being processed, you probably will want to start blocking the client. In other cases, you might be willing to loosen those guarantees. There are a few popular strategies to do this. The first is to buffer the data. If no worker is available, we want to temporarily store the data in some sort of queue. Channels have this buffering capability built-in. When we created our channel with make , we can give our channel a length: _(coding_little_go_book.pdf (source-range-23d24eb1-00436))_

- You can make this change, but you'll notice that the processing is still choppy. Buffered channels don't add more capacity; they merely provide a queue for pending work and a good way to deal with a sudden spike. In our example, we're continuously pushing more data than our workers can handle. _(coding_little_go_book.pdf (source-range-23d24eb1-00438))_

### Chapter 6 - Concurrency / Channels / Select

- We're pushing out 20 messages per second, but our workers can only handle 10 per second; thus, half the messages get dropped. _(coding_little_go_book.pdf (source-range-23d24eb1-00446))_


## Technical atoms

### Technical frame 1: Chapter 6 - Concurrency / Channels

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00429))_

> Our worker is simple. It waits until data is available then "processes" it. Dutifully, it does this in a loop, forever waiting for more data to process. To use this, the first thing we'd do is start some workers: And then we can give them some work: Here's the complete code to make it run: } func (w Worker) process(c chan int) { for { data := <-c fmt.Printf("worker %d got %d\n", w.id, data) } } c := make( chan int) for i := 0; i < 5; i++ { worker := &Worker{id: i} go worker.process(c) } for { c 

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00428))_

```
id int
```

### Technical frame 2: Chapter 6 - Concurrency / Channels / Buffered Channels

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00435))_

> What's happening is that our main code, the one that accepts the user's incoming data (which we just simulated with a random number generator) is blocking as it sends to the channel because no receiver is available.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00434))_

```
for {
  data := <-c
  fmt.Printf("worker %d got %d\n", w.id, data)
  time.Sleep(time.Millisecond * 500)
}
```

### Technical frame 3: Chapter 6 - Concurrency / Channels / Buffered Channels

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00438))_

> You can make this change, but you'll notice that the processing is still choppy. Buffered channels don't add more capacity; they merely provide a queue for pending work and a good way to deal with a sudden spike. In our example, we're continuously pushing more data than our workers can handle.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00437))_

```
c := make(chan int, 100)
```


## Related pages

- [[coding-little-go-book-channel]] - shared technical atoms: Channel shares technical record from Chapter 6 - Concurrency / Channels: id int (3 shared atom(s))

## Source

- [[coding-little-go-book]]
