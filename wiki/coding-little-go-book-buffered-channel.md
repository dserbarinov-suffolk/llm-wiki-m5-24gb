---
page_id: coding-little-go-book-buffered-channel
page_kind: concept
summary: Buffered Channels: 25 statement(s) and 1 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-buffered-channel@2c08c71daa956a1b6dd558ffb3321fce
---

# Buffered Channels

What [[coding-little-go-book]] covers about buffered channels:

## Statements

- Channels are more complicated. _(coding_little_go_book.pdf (source-range-810ce361-00475))_
- The first available channel is chosen. _(coding_little_go_book.pdf (source-range-810ce361-00460))_
- To help with this problem, Go provides channels . _(coding_little_go_book.pdf (source-range-810ce361-00408))_
- Channels have this buffering capability built-in. _(coding_little_go_book.pdf (source-range-810ce361-00436))_
- Also, time.After is a channel of type chan time.Time . _(coding_little_go_book.pdf (source-range-810ce361-00457))_
- These are all things that are doable without channels . _(coding_little_go_book.pdf (source-range-810ce361-00425))_
- time.After returns a channel, so we can select from it. _(coding_little_go_book.pdf (source-range-810ce361-00453))_
- A main purpose of select is to manage multiple channels. _(coding_little_go_book.pdf (source-range-810ce361-00447))_
- A channel is randomly picked when multiple are available. _(coding_little_go_book.pdf (source-range-810ce361-00447))_
- The channel is written to after the specified time expires. _(coding_little_go_book.pdf (source-range-810ce361-00453))_
- If no channel is available, the default case is executed. _(coding_little_go_book.pdf (source-range-810ce361-00462))_
- If multiple channels are available, one is randomly picked. _(coding_little_go_book.pdf (source-range-810ce361-00461))_
- If no channel is available, default is executed if one is provided. _(coding_little_go_book.pdf (source-range-810ce361-00447))_
- I do think learning about concurrent programming without channels is useful. _(coding_little_go_book.pdf (source-range-810ce361-00475))_

## Technical atoms

> The challenge with concurrent programming stems from sharing data. If your goroutines share no data, you needn't worry about synchronizing them. That isn't an option for all systems, however. In fact, many systems are built with the exact opposite goal in mind: to share data across multiple requests. An in-memory cache or a database, are good examples of this. This is becoming an increasingly common reality. Channels help make concurrent programming saner by taking shared data out of the picture. A channel is a communication pipe between goroutines which is used to pass data. In other words, a goroutine that has data can pass it to another goroutine via a channel. The result is that, at any point in time, only one goroutine has access to the data. A channel, like everything else, has a type. This is the type of data that we'll be passing through our channel. For example, to create a channel which can be used to pass an integer around, we'd do: The type of this channel is chan int . Therefore, to pass this channel to a function, our signature looks like: Channels support two operations: receiving and sending. We send to a channel by doing: CHANNEL <- DATA and receive from one by doing VAR := <-CHANNEL The arrow points in the direction that data flows. When sending, the data flows into the channel. When receiving, the data flows out of the channel. The final thing to know before we look at our first example is that receiving and sending to and from a channel is blocking. That is, when we receive from a channel, execution of the goroutine won't continue until data is available. Similarly, when we send to a channel, execution won't continue until the data is received. Consider a system with incoming data that we want to handle in separate goroutines. This is a common requirement. If we did our data-intensive processing on the goroutine which accepts the incoming data, we'd risk timing out clients. First, we'll write our worker. This could be a simple function, but I'll make it part of a structure since we haven't seen goroutines used like this before: c := make( chan int) func worker(c chan int) { ... } type Worker struct {
_(source: coding_little_go_book.pdf (source-range-810ce361-00427))_


## Source

- [[coding-little-go-book]]
