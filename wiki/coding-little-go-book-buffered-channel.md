---
page_id: coding-little-go-book-buffered-channel
page_kind: concept
summary: Buffered Channels: 10 statement(s) and 3 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-29
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-buffered-channel@18e216b5d19de75e26bf0aaf0e013d11
---

# Buffered Channels

What [[coding-little-go-book]] covers about buffered channels:

## Statements

### Chapter 6 - Concurrency / Channels / Buffered Channels

- What's happening is that our main code, the one that accepts the user's incoming data (which we just simulated with a random number generator) is blocking as it sends to the channel because no receiver is available. _(coding_little_go_book.pdf (source-range-23d24eb1-00435))_

- In cases where you need high guarantees that the data is being processed, you probably will want to start blocking the client. In other cases, you might be willing to loosen those guarantees. There are a few popular strategies to do this. The first is to buffer the data. If no worker is available, we want to temporarily store the data in some sort of queue. Channels have this buffering capability built-in. When we created our channel with make , we can give our channel a length: _(coding_little_go_book.pdf (source-range-23d24eb1-00436))_

- You can make this change, but you'll notice that the processing is still choppy. Buffered channels don't add more capacity; they merely provide a queue for pending work and a good way to deal with a sudden spike. In our example, we're continuously pushing more data than our workers can handle. _(coding_little_go_book.pdf (source-range-23d24eb1-00438))_

- You can see that it grows and grows until it fills up, at which point sending to our channel start to block again. _(coding_little_go_book.pdf (source-range-23d24eb1-00441))_


## Technical atoms

### Technical frame 1: Chapter 6 - Concurrency / Channels / Buffered Channels

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

### Technical frame 2: Chapter 6 - Concurrency / Channels / Buffered Channels

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00438))_

> You can make this change, but you'll notice that the processing is still choppy. Buffered channels don't add more capacity; they merely provide a queue for pending work and a good way to deal with a sudden spike. In our example, we're continuously pushing more data than our workers can handle.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00437))_

```
c := make(chan int, 100)
```

### Technical frame 3: Chapter 6 - Concurrency / Channels / Buffered Channels

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00441))_

> You can see that it grows and grows until it fills up, at which point sending to our channel start to block again.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00440))_

```
for {
  c <- rand.Int()
  fmt.Println(len(c))
  time.Sleep(time.Millisecond * 50)
}
```


## Related pages

- [[coding-little-go-book-channel]] - broader topic: Channels shares source evidence from Chapter 6 - Concurrency / Channels / Buffered Channels: What's happening is that our main code, the one that accepts the user's incoming data (which we just simulated with a random number generator) is blocking as it send ... [truncated]; Channels shares technical record from Chapter 6 - Concurrency / Channels / Buffered Channels: for { data := <-c fmt.Printf("worker %d got %d\n", w.id, data) time.Sleep(time.Millisecond * 500) } (10 shared statement(s), 3 shared atom(s))
- [[coding-little-go-book-concurrency]] - shared statements and technical atoms: Concurrency shares source evidence from Chapter 6 - Concurrency / Channels / Buffered Channels: What's happening is that our main code, the one that accepts the user's incoming data (which we just simulated with a random number generator) is blocking as it send ... [truncated]; Concurrency shares technical record from Chapter 6 - Concurrency / Channels / Buffered Channels: for { data := <-c fmt.Printf("worker %d got %d\n", w.id, data) time.Sleep(time.Millisecond * 500) } (10 shared statement(s), 3 shared atom(s))
- [[coding-little-go-book-section-chapter-6-concurrency-channels-buffered-channels-7253b866]] - source section: Chapter 6 - Concurrency / Channels / Buffered Channels shares source evidence from Chapter 6 - Concurrency / Channels / Buffered Channels: What's happening is that our main code, the one that accepts the user's incoming data (which we just simulated with a random number generator) is blocking as it send ... [truncated]; Chapter 6 - Concurrency / Channels / Buffered Channels shares technical record from Chapter 6 - Concurrency / Channels / Buffered Channels: for { data := <-c fmt.Printf("worker %d got %d\n", w.id, data) time.Sleep(time.Millisecond * 500) } (10 shared statement(s), 3 shared atom(s))

## Source

- [[coding-little-go-book]]
