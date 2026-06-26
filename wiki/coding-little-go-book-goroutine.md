---
page_id: coding-little-go-book-goroutine
page_kind: concept
summary: Goroutines: 13 statement(s) and 6 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-goroutine@6bd5e42ad754aae0b8838f2945747c7a
---

# Goroutines

What [[coding-little-go-book]] covers about goroutines:

## Statements

- Goroutines are easy to create and have little overhead. _(coding_little_go_book.pdf (source-range-810ce361-00403))_
- On modern hardware, it's possible to have millions of goroutines. _(coding_little_go_book.pdf (source-range-810ce361-00403))_
- Goroutines effectively abstract what's needed to run concurrent code. _(coding_little_go_book.pdf (source-range-810ce361-00467))_
- Multiple goroutines will end up running on the same underlying OS thread. _(coding_little_go_book.pdf (source-range-810ce361-00403))_
- The result is that a goroutine has a fraction of overhead (a few KB) than OS threads. _(coding_little_go_book.pdf (source-range-810ce361-00403))_
- There are a few interesting things going on here, but the most important is how we start a goroutine. _(coding_little_go_book.pdf (source-range-810ce361-00401))_
- There's little to say about goroutines other than they're effective and simple (simple to use anyway). _(coding_little_go_book.pdf (source-range-810ce361-00474))_
- The reason for this is that it provides a simple syntax over two powerful mechanisms: goroutines and channels. _(coding_little_go_book.pdf (source-range-810ce361-00396))_
- This is often called an M:N threading model because we have M application threads (goroutines) running on N OS threads. _(coding_little_go_book.pdf (source-range-810ce361-00403))_
- Because we potentially have multiple (two in this case) goroutines writing to the same variable, counter , at the same time. _(coding_little_go_book.pdf (source-range-810ce361-00412))_
- Channels provide all of the synchronization code we need and also ensure that, at any given time, only one goroutine has access to a specific piece of data. _(coding_little_go_book.pdf (source-range-810ce361-00430))_
- That's because the main process exits before the goroutine gets a chance to execute (the process doesn't wait until all goroutines are finished before exiting). _(coding_little_go_book.pdf (source-range-810ce361-00405))_
- With a single lock, this isn't a problem, but if you're using two or more locks around the same code, it's dangerously easy to have situations where goroutineA holds lockA but needs access to lockB, while goroutineB holds lockB but needs access to lockA. _(coding_little_go_book.pdf (source-range-810ce361-00418))_

## Code, rules, and examples

> Code that runs in a goroutine can run concurrently with other code.
_(source: coding_little_go_book.pdf (source-range-810ce361-00398))_

> A goroutine is similar to a thread, but it is scheduled by Go, not the OS. Code that runs in a goroutine can run concurrently with other code. Let's look at an example:
_(source: coding_little_go_book.pdf (source-range-810ce361-00398))_

> Creating goroutines is trivial, and they are so cheap that we can start many; however, concurrent code needs to be coordinated.
_(source: coding_little_go_book.pdf (source-range-810ce361-00407))_

> Furthermore, part of concurrent programming isn't so much about serializing access across the narrowest possible piece of code; it's also about coordinating multiple goroutines. For example, sleeping for 10 milliseconds isn't a particularly elegant solution. What if a goroutine takes more than 10 milliseconds? What if it takes less and we're just wasting cycles? Also, what if instead of just waiting for goroutines to finish, we want to tell one hey, I have new data for you to process! ?
_(source: coding_little_go_book.pdf (source-range-810ce361-00423))_

> In other words, a goroutine that has data can pass it to another goroutine via a channel.
_(source: coding_little_go_book.pdf (source-range-810ce361-00426))_

> The challenge with concurrent programming stems from sharing data. If your goroutines share no data, you needn't worry about synchronizing them. That isn't an option for all systems, however. In fact, many systems are built with the exact opposite goal in mind: to share data across multiple requests. An in-memory cache or a database, are good examples of this. This is becoming an increasingly common reality. Channels help make concurrent programming saner by taking shared data out of the picture. A channel is a communication pipe between goroutines which is used to pass data. In other words, a goroutine that has data can pass it to another goroutine via a channel. The result is that, at any point in time, only one goroutine has access to the data. A channel, like everything else, has a type. This is the type of data that we'll be passing through our channel. For example, to create a channel which can be used to pass an integer around, we'd do: The type of this channel is chan int . Therefore, to pass this channel to a function, our signature looks like: Channels support two operations: receiving and sending. We send to a channel by doing: CHANNEL <- DATA and receive from one by doing VAR := <-CHANNEL The arrow points in the direction that data flows. When sending, the data flows into the channel. When receiving, the data flows out of the channel. The final thing to know before we look at our first example is that receiving and sending to and from a channel is blocking. That is, when we receive from a channel, execution of the goroutine won't continue until data is available. Similarly, when we send to a channel, execution won't continue until the data is received. Consider a system with incoming data that we want to handle in separate goroutines. This is a common requirement. If we did our data-intensive processing on the goroutine which accepts the incoming data, we'd risk timing out clients. First, we'll write our worker. This could be a simple function, but I'll make it part of a structure since we haven't seen goroutines used like this before: c := make( chan int) func worker(c chan int) { ... } type Worker struct {
_(source: coding_little_go_book.pdf (source-range-810ce361-00426))_


## Source

- [[coding-little-go-book]]
