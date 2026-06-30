---
page_id: coding-little-go-book-section-chapter-6-concurrency-channels-select-98be429f
page_kind: source
summary: Chapter 6 - Concurrency / Channels / Select: 13 source-backed entries and 1 atom(s) from raw/coding_little_go_book.pdf.
page_family: section-reference
sources: raw/coding_little_go_book.pdf
updated: 2026-06-30
domain: coding-little-go-book
category_path: sources/coding-little-go-book/sections
source_id: coding_little_go_book.pdf
projection_coverage: section-coding-little-go-book-section-chapter-6-concurrency-channels-select-98be429f@2021d7ef43c8546947ea0b81bd02b032
---

# Chapter 6 - Concurrency / Channels / Select

From [[coding-little-go-book]].

## Related pages

- [[coding-little-go-book-section-chapter-6-concurrency-channels-5666c1f3]] - broader source section: Chapter 6 - Concurrency / Channels
- [[coding-little-go-book-section-chapter-6-concurrency-channels-buffered-channels-7253b866]] - previous source section: Chapter 6 - Concurrency / Channels / Buffered Channels
- [[coding-little-go-book-section-chapter-6-concurrency-channels-timeout-234b9aa0]] - next source section: Chapter 6 - Concurrency / Channels / Timeout

## Statements

- Even with buffering, there comes a point where we need to start dropping messages. We can't use up an infinite amount of memory hoping a worker frees up. For this, we use Go's select . _(coding_little_go_book.pdf (source-range-23d24eb1-00443))_
- Syntactically, select looks a bit like a switch. With it, we can provide code for when the channel isn't available to send to. First, let's remove our channel's buffering so that we can clearly see how select works: _(coding_little_go_book.pdf (source-range-23d24eb1-00444))_
- We're pushing out 20 messages per second, but our workers can only handle 10 per second; thus, half the messages get dropped. _(coding_little_go_book.pdf (source-range-23d24eb1-00446))_
- This is only the start of what we can accomplish with select . A main purpose of select is to manage multiple channels. Given multiple channels, select will block until the first one becomes available. If no channel is available, default is executed if one is provided. A channel is randomly picked when multiple are available. _(coding_little_go_book.pdf (source-range-23d24eb1-00447))_
- It's hard to come up with a simple example that demonstrates this behavior as it's a fairly advanced feature. The next section might help illustrate this though. _(coding_little_go_book.pdf (source-range-23d24eb1-00448))_
- We're pushing out 20 messages per second, but our workers can only handle 10 per second; thus, half the messages get dropped. _(coding_little_go_book.pdf (source-range-23d24eb1-00446))_
- This is only the start of what we can accomplish with select . _(coding_little_go_book.pdf (source-range-23d24eb1-00447))_

## Technical atoms

### Technical frame 1: Chapter 6 - Concurrency / Channels / Select

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00446))_

> We're pushing out 20 messages per second, but our workers can only handle 10 per second; thus, half the messages get dropped.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00445))_

```
c := make(chan int)
Next, we change our for loop:
for {
  select {
  case c <- rand.Int():
    //optional code here
  default:
    //this can be left empty to silently drop the data
    fmt.Println("dropped")
  }
  time.Sleep(time.Millisecond * 50)
}
```
