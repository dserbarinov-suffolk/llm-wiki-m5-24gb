---
page_id: coding-little-go-book-channel
page_kind: concept
summary: Channels: 39 statement(s) and 12 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-29
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-channel@c7f00ca92b1d4dce3afe0d30a11372df
---

# Channels

What [[coding-little-go-book]] covers about channels:

## Statements

### Chapter 6 - Concurrency / Channels

- Our worker is simple. It waits until data is available then "processes" it. Dutifully, it does this in a loop, forever waiting for more data to process. To use this, the first thing we'd do is start some workers: And then we can give them some work: Here's the complete code to make it run: } func (w Worker) process(c chan int) { for { data := <-c fmt.Printf("worker %d got %d\n", w.id, data) } } c := make( chan int) for i := 0; i < 5; i++ { worker := &Worker{id: i} go worker.process(c) } for { c <- rand.Int() time.Sleep(time.Millisecond * 50) } package main import ( "fmt" "time" "math/rand" ) func main() { c := make( chan int) for i := 0; i < 5; i++ { worker := &Worker{id: i} go worker.process(c) } for { c <- rand.Int() time.Sleep(time.Millisecond * 50) } } type Worker struct { id int } func (w *Worker) process(c chan int) { for { data := <-c fmt.Printf("worker %d got %d\n", w.id, data) } } _(coding_little_go_book.pdf (source-range-23d24eb1-00429))_

- We don't know which worker is going to get what data. What we do know, what Go guarantees, is that the data we send to a channel will only be received by a single receiver. _(coding_little_go_book.pdf (source-range-23d24eb1-00430))_

- Notice that the only shared state is the channel, which we can safely receive from and send to concurrently. Channels provide all of the synchronization code we need and also ensure that, at any given time, only one goroutine has access to a specific piece of data. _(coding_little_go_book.pdf (source-range-23d24eb1-00431))_

### Chapter 6 - Concurrency / Channels / Buffered Channels

- What's happening is that our main code, the one that accepts the user's incoming data (which we just simulated with a random number generator) is blocking as it sends to the channel because no receiver is available. _(coding_little_go_book.pdf (source-range-23d24eb1-00435))_

- In cases where you need high guarantees that the data is being processed, you probably will want to start blocking the client. In other cases, you might be willing to loosen those guarantees. There are a few popular strategies to do this. The first is to buffer the data. If no worker is available, we want to temporarily store the data in some sort of queue. Channels have this buffering capability built-in. When we created our channel with make , we can give our channel a length: _(coding_little_go_book.pdf (source-range-23d24eb1-00436))_

- You can make this change, but you'll notice that the processing is still choppy. Buffered channels don't add more capacity; they merely provide a queue for pending work and a good way to deal with a sudden spike. In our example, we're continuously pushing more data than our workers can handle. _(coding_little_go_book.pdf (source-range-23d24eb1-00438))_

- You can see that it grows and grows until it fills up, at which point sending to our channel start to block again. _(coding_little_go_book.pdf (source-range-23d24eb1-00441))_

### Chapter 6 - Concurrency / Channels / Select

- Even with buffering, there comes a point where we need to start dropping messages. We can't use up an infinite amount of memory hoping a worker frees up. For this, we use Go's select . _(coding_little_go_book.pdf (source-range-23d24eb1-00443))_

- Syntactically, select looks a bit like a switch. With it, we can provide code for when the channel isn't available to send to. First, let's remove our channel's buffering so that we can clearly see how select works: _(coding_little_go_book.pdf (source-range-23d24eb1-00444))_

- We're pushing out 20 messages per second, but our workers can only handle 10 per second; thus, half the messages get dropped. _(coding_little_go_book.pdf (source-range-23d24eb1-00446))_

- This is only the start of what we can accomplish with select . A main purpose of select is to manage multiple channels. Given multiple channels, select will block until the first one becomes available. If no channel is available, default is executed if one is provided. A channel is randomly picked when multiple are available. _(coding_little_go_book.pdf (source-range-23d24eb1-00447))_

- It's hard to come up with a simple example that demonstrates this behavior as it's a fairly advanced feature. The next section might help illustrate this though. _(coding_little_go_book.pdf (source-range-23d24eb1-00448))_

### Chapter 6 - Concurrency / Channels / Timeout

- We've looked at buffering messages as well as simply dropping them. Another popular option is to timeout. We're willing to block for some time, but not forever. This is also something easy to achieve in Go. Admittedly, the syntax might be hard to follow but it's such a neat and useful feature that I couldn't leave it out. _(coding_little_go_book.pdf (source-range-23d24eb1-00450))_

- To block for a maximum amount of time, we can use the time.After function. Let's look at it then try to peek beyond the magic. To use this, our sender becomes: _(coding_little_go_book.pdf (source-range-23d24eb1-00451))_

- time.After returns a channel, so we can select from it. The channel is written to after the specified time expires. That's it. There's nothing more magical than that. If you're curious, here's what an implementation of after could look like: _(coding_little_go_book.pdf (source-range-23d24eb1-00453))_

- Back to our select , there are a couple of things to play with. First, what happens if you add the default case back? Can you guess? Try it. If you aren't sure what's going on, remember that default fires immediately if no channel is available. _(coding_little_go_book.pdf (source-range-23d24eb1-00456))_

- Also, time.After is a channel of type chan time.Time . In the above example, we simply discard the value that was sent to the channel. If you want though, you can receive it: _(coding_little_go_book.pdf (source-range-23d24eb1-00457))_

- The first available channel is chosen. _(coding_little_go_book.pdf (source-range-23d24eb1-00460))_

- If multiple channels are available, one is randomly picked. _(coding_little_go_book.pdf (source-range-23d24eb1-00461))_

- If no channel is available, the default case is executed. _(coding_little_go_book.pdf (source-range-23d24eb1-00462))_


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

### Technical frame 4: Chapter 6 - Concurrency / Channels / Buffered Channels

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

### Technical frame 5: Chapter 6 - Concurrency / Channels / Select

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

### Technical frame 6: Chapter 6 - Concurrency / Channels / Timeout

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00453))_

> time.After returns a channel, so we can select from it. The channel is written to after the specified time expires. That's it. There's nothing more magical than that. If you're curious, here's what an implementation of after could look like:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00452))_

```
for {
  select {
  case c <- rand.Int():
  case <-time.After(time.Millisecond * 100):
    fmt.Println("timed out")
  }
  time.Sleep(time.Millisecond * 50)
}
```

### Technical frame 7: Chapter 6 - Concurrency / Channels / Timeout

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00456))_

> Back to our select , there are a couple of things to play with. First, what happens if you add the default case back? Can you guess? Try it. If you aren't sure what's going on, remember that default fires immediately if no channel is available.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00454))_

```
func after(d time.Duration) chan bool {
  c := make(chan bool)
```

### Technical frame 8: Chapter 6 - Concurrency / Channels / Timeout

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00456))_

> Back to our select , there are a couple of things to play with. First, what happens if you add the default case back? Can you guess? Try it. If you aren't sure what's going on, remember that default fires immediately if no channel is available.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00455))_

```
go func() {
    time.Sleep(d)
    c <- true
  }()
  return c
}
```

### Technical frame 9: Chapter 6 - Concurrency / Channels / Timeout

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00457))_

> Also, time.After is a channel of type chan time.Time . In the above example, we simply discard the value that was sent to the channel. If you want though, you can receive it:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00456))_

> First, what happens if you add the default case back?

### Technical frame 10: Chapter 6 - Concurrency / Channels / Timeout

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00460))_

> The first available channel is chosen.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00457))_

> If you want though, you can receive it:

### Technical frame 11: Chapter 6 - Concurrency / Channels / Timeout

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00460))_

> The first available channel is chosen.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00458))_

```
case t := <-time.After(time.Millisecond * 100):
  fmt.Println("timed out at", t)
```

### Technical frame 12: Chapter 6 - Concurrency / Channels / Timeout

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00462))_

> If no channel is available, the default case is executed.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00465))_

```
for {
  select {
  case data := <-c:
    fmt.Printf("worker %d got %d\n", w.id, data)
  case <-time.After(time.Millisecond * 10):
    fmt.Println("Break time")
    time.Sleep(time.Second)
  }
}
```


## Related pages

- [[coding-little-go-book-buffered-channel]] - narrower topic: Buffered Channels shares source evidence from Chapter 6 - Concurrency / Channels / Buffered Channels: What's happening is that our main code, the one that accepts the user's incoming data (which we just simulated with a random number generator) is blocking as it send ... [truncated]; Buffered Channels shares technical record from Chapter 6 - Concurrency / Channels / Buffered Channels: for { data := <-c fmt.Printf("worker %d got %d\n", w.id, data) time.Sleep(time.Millisecond * 500) } (10 shared statement(s), 3 shared atom(s))
- [[coding-little-go-book-concurrency]] - shared statements and technical atoms: Concurrency shares source evidence from Chapter 6 - Concurrency / Channels: Our worker is simple. It waits until data is available then "processes" it. Dutifully, it does this in a loop, forever waiting for more data to process. To use this, ... [truncated]; Concurrency shares technical record from Chapter 6 - Concurrency / Channels: id int (39 shared statement(s), 12 shared atom(s))
- [[coding-little-go-book-timeout]] - shared statements and technical atoms: Timeout shares source evidence from Chapter 6 - Concurrency / Channels / Timeout: We've looked at buffering messages as well as simply dropping them. Another popular option is to timeout. We're willing to block for some time, but not forever. This ... [truncated]; Timeout shares technical record from Chapter 6 - Concurrency / Channels / Timeout: for { select { case c <- rand.Int(): case <-time.After(time.Millisecond * 100): fmt.Println("timed out") } time.Sleep(time.Millisecond * 50) } (13 shared statement(s), 7 shared atom(s))
- [[coding-little-go-book-value]] - shared statements and technical atoms: Value shares source evidence from Chapter 6 - Concurrency / Channels / Timeout: Also, time.After is a channel of type chan time.Time . In the above example, we simply discard the value that was sent to the channel. If you want though, you can receive it:; Value shares technical record from Chapter 6 - Concurrency / Channels / Timeout: go func() { time.Sleep(d) c <- true }() return c } (1 shared statement(s), 3 shared atom(s))
- [[coding-little-go-book-section-chapter-6-concurrency-channels-5666c1f3]] - source section: Chapter 6 - Concurrency / Channels shares source evidence from Chapter 6 - Concurrency / Channels: Our worker is simple. It waits until data is available then "processes" it. Dutifully, it does this in a loop, forever waiting for more data to process. To use this, ... [truncated]; Chapter 6 - Concurrency / Channels shares technical record from Chapter 6 - Concurrency / Channels: id int (39 shared statement(s), 12 shared atom(s))

## Source

- [[coding-little-go-book]]
