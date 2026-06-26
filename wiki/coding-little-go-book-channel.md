---
page_id: coding-little-go-book-channel
page_kind: concept
summary: Channels: 6 statement(s) and 1 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-channel@e4d75ec2d5241bdf4b629aedd146317a
---

# Channels

What [[coding-little-go-book]] covers about channels:

## Statements

- Channels provide all of the synchronization code we need and also ensure that, at any given time, only one goroutine has access to a specific piece of data. _(coding_little_go_book.pdf (source-range-773b6275-00431))_
- Notice that the only shared state is the channel, which we can safely receive from and send to concurrently. _(coding_little_go_book.pdf (source-range-773b6275-00431))_
- It waits until data is available then "processes" it. _(coding_little_go_book.pdf (source-range-773b6275-00429))_
- Dutifully, it does this in a loop, forever waiting for more data to process. _(coding_little_go_book.pdf (source-range-773b6275-00429))_
- Our worker is simple. _(coding_little_go_book.pdf (source-range-773b6275-00429))_
- We don't know which worker is going to get what data. _(coding_little_go_book.pdf (source-range-773b6275-00430))_

## Technical atoms

> Context: The challenge with concurrent programming stems from sharing data. If your goroutines share no data, you needn't worry about synchronizing them. That isn't an option for all systems, however. In fact, many systems are built with the exact opposite goal in mind: to share data across multiple requests. An in-memory cache or a database, are good examples of this. This is becoming an increasingly common reality. Channels help make concurrent programming saner by taking shared data out of the picture. A channel is a communication pipe between goroutines which is used to pass data. In other words, a goroutine that has data can pass it to another goroutine via a channel. The result is that, at any point in time, only one goroutine has access to the data. A channel, like everything else, has a type. This is the type of data that we'll be passing through our channel. For example, to create a channel which can be used to pass an integer around, we'd do: The type of this channel is chan int . Therefore, to pass this channel to a function, our signature looks like: Channels support two operations: receiving and sending. We send to a channel by doing: CHANNEL <- DATA and receive from one by doing VAR := <-CHANNEL The arrow points in the direction that data flows. When sending, the data flows into the channel. When receiving, the data flows out of the channel. The final thing to know before we look at our first example is that receiving and sending to and from a channel is blocking. That is, when we receive from a channel, execution of the goroutine won't continue until data is available. Similarly, when we send to a channel, execution won't continue until the data is received. Consider a system with incoming data that we want to handle in separate goroutines. This is a common requirement. If we did our data-intensive processing on the goroutine which accepts the incoming data, we'd risk timing out clients. First, we'll write our worker. This could be a simple function, but I'll make it part of a structure since we haven't seen goroutines used like this before: c := make( chan int) func worker(c chan int) { ... } type Worker struct {
_(context: coding_little_go_book.pdf (source-range-773b6275-00427))_

```
id int
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00428))_


## Source

- [[coding-little-go-book]]
