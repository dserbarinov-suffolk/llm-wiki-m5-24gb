---
page_id: coding-little-go-book-buffered-channel
page_kind: concept
summary: Buffered Channels: 10 statement(s) and 3 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-buffered-channel@5b41fc2cd06e41f68a676425a499e6f5
---

# Buffered Channels

What [[coding-little-go-book]] covers about buffered channels:

## Statements

- Channels have this buffering capability built-in. _(coding_little_go_book.pdf (source-range-773b6275-00436))_
- What's happening is that our main code, the one that accepts the user's incoming data (which we just simulated with a random number generator) is blocking as it sends to the channel because no receiver is available. _(coding_little_go_book.pdf (source-range-773b6275-00435))_
- You can see that it grows and grows until it fills up, at which point sending to our channel start to block again. _(coding_little_go_book.pdf (source-range-773b6275-00441))_
- In cases where you need high guarantees that the data is being processed, you probably will want to start blocking the client. _(coding_little_go_book.pdf (source-range-773b6275-00436))_
- There are a few popular strategies to do this. _(coding_little_go_book.pdf (source-range-773b6275-00436))_
- If no worker is available, we want to temporarily store the data in some sort of queue. _(coding_little_go_book.pdf (source-range-773b6275-00436))_
- The first is to buffer the data. _(coding_little_go_book.pdf (source-range-773b6275-00436))_
- In other cases, you might be willing to loosen those guarantees. _(coding_little_go_book.pdf (source-range-773b6275-00436))_
- In our example, we're continuously pushing more data than our workers can handle. _(coding_little_go_book.pdf (source-range-773b6275-00438))_
- You can make this change, but you'll notice that the processing is still choppy. _(coding_little_go_book.pdf (source-range-773b6275-00438))_

## Technical atoms

> Context: Given the above code, what happens if we have more data coming in than we can handle? You can simulate this by changing the worker to sleep after it has received data: What's happening is that our main code, the one that accepts the user's incoming data (which we just simulated with a random number generator) is blocking as it sends to the channel because no receiver is available.
_(context: coding_little_go_book.pdf (source-range-773b6275-00433, source-range-773b6275-00435))_

```
for {
  data := <-c
  fmt.Printf("worker %d got %d\n", w.id, data)
  time.Sleep(time.Millisecond * 500)
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00434))_

> Context: In cases where you need high guarantees that the data is being processed, you probably will want to start blocking the client. In other cases, you might be willing to loosen those guarantees. There are a few popular strategies to do this. The first is to buffer the data. If no worker is available, we want to temporarily store the data in some sort of queue. Channels have this buffering capability built-in. When we created our channel with make , we can give our channel a length:
_(context: coding_little_go_book.pdf (source-range-773b6275-00436))_

```
c := make(chan int, 100)
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00437))_

> Context: Nevertheless, we can get a sense what the buffered channel is, in fact, buffering by looking at the channel's len :
_(context: coding_little_go_book.pdf (source-range-773b6275-00439))_

```
for {
  c <- rand.Int()
  fmt.Println(len(c))
  time.Sleep(time.Millisecond * 50)
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00440))_


## Source

- [[coding-little-go-book]]
