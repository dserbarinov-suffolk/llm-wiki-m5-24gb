---
page_id: coding-little-go-book-channel
page_kind: concept
summary: Channel: 13 statement(s) and 11 atom(s) from raw/coding_little_go_book.pdf.
page_family: topic-concept
sources: raw/coding_little_go_book.pdf
updated: 2026-06-30
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-channel@1a1784ee4f90cf59097e229d66ca1b01
---

# Channel

What [[coding-little-go-book]] covers about channel:

## Statements

### Chapter 6 - Concurrency / Channels

- Notice that the only shared state is the channel, which we can safely receive from and send to concurrently. Channels provide all of the synchronization code we need and also ensure that, at any given time, only one goroutine has access to a specific piece of data. _(coding_little_go_book.pdf (source-range-23d24eb1-00431))_

### Chapter 6 - Concurrency / Channels / Buffered Channels

- In cases where you need high guarantees that the data is being processed, you probably will want to start blocking the client. In other cases, you might be willing to loosen those guarantees. There are a few popular strategies to do this. The first is to buffer the data. If no worker is available, we want to temporarily store the data in some sort of queue. Channels have this buffering capability built-in. When we created our channel with make , we can give our channel a length: _(coding_little_go_book.pdf (source-range-23d24eb1-00436))_

### Chapter 6 - Concurrency / Channels / Select

- This is only the start of what we can accomplish with select . A main purpose of select is to manage multiple channels. Given multiple channels, select will block until the first one becomes available. If no channel is available, default is executed if one is provided. A channel is randomly picked when multiple are available. _(coding_little_go_book.pdf (source-range-23d24eb1-00447))_

### Chapter 6 - Concurrency / Channels / Timeout

- time.After returns a channel, so we can select from it. The channel is written to after the specified time expires. That's it. There's nothing more magical than that. If you're curious, here's what an implementation of after could look like: _(coding_little_go_book.pdf (source-range-23d24eb1-00453))_

- Back to our select , there are a couple of things to play with. First, what happens if you add the default case back? Can you guess? Try it. If you aren't sure what's going on, remember that default fires immediately if no channel is available. _(coding_little_go_book.pdf (source-range-23d24eb1-00456))_

- The first available channel is chosen. _(coding_little_go_book.pdf (source-range-23d24eb1-00460))_

- If multiple channels are available, one is randomly picked. _(coding_little_go_book.pdf (source-range-23d24eb1-00461))_

- If no channel is available, the default case is executed. _(coding_little_go_book.pdf (source-range-23d24eb1-00462))_

### Chapter 6 - Concurrency / Before You Continue

- Having said that, I still make extensive use of the various synchronization primitives found in the sync and sync/atomic packages. I think it's important to be comfortable with both. I encourage you to first focus on channels, but when you see a simple example that needs a short-lived lock, consider using a mutex or readwrite mutex. _(coding_little_go_book.pdf (source-range-23d24eb1-00469))_

### Conclusion

- Last but not least is the built-in support for concurrency. There's little to say about goroutines other than they're effective and simple (simple to use anyway). It's a good abstraction. Channels are more complicated. I always think it's important to understand basics before using high-level wrappers. I do think learning about concurrent programming without channels is useful. Still, channels are implemented in a way that, to me, doesn't feel quite like a simple abstraction. They are almost their own fundamental building block. I say this because they change how you write and think about concurrent programming. Given how hard concurrent programming can be, that is definitely a good thing. _(coding_little_go_book.pdf (source-range-23d24eb1-00475))_


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

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00456))_

> Back to our select , there are a couple of things to play with. First, what happens if you add the default case back? Can you guess? Try it. If you aren't sure what's going on, remember that default fires immediately if no channel is available.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00454))_

```
func after(d time.Duration) chan bool {
  c := make(chan bool)
```

### Technical frame 7: Chapter 6 - Concurrency / Channels / Timeout

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

### Technical frame 8: Chapter 6 - Concurrency / Channels / Timeout

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00457))_

> Also, time.After is a channel of type chan time.Time . In the above example, we simply discard the value that was sent to the channel. If you want though, you can receive it:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00456))_

> First, what happens if you add the default case back?

### Technical frame 9: Chapter 6 - Concurrency / Channels / Timeout

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00460))_

> The first available channel is chosen.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00457))_

> If you want though, you can receive it:

### Technical frame 10: Chapter 6 - Concurrency / Channels / Timeout

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00460))_

> The first available channel is chosen.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00458))_

```
case t := <-time.After(time.Millisecond * 100):
  fmt.Println("timed out at", t)
```

### Technical frame 11: Conclusion

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00474))_

> Beyond this, Go gives us a simple but effective way to organize our code. Interfaces, return-based error handling, defer for resource management and a simple way to achieve composition.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00473))_

> Still, it comes down to some basic rules (like you can only declare variable once and := does declare the variable) and fundamental understanding (like new(X) or &X{} only allocate memory, but slices, maps and channels require more initialization and thus, make ).


## Related pages

- [[coding-little-go-book-remember]] - shared statements and technical atoms: Remember shares source evidence from Chapter 6 - Concurrency / Channels / Timeout: Back to our select , there are a couple of things to play with. First, what happens if you add the default case back? Can you guess? Try it. If you aren't sure what' ... [truncated]; Remember shares technical record from Chapter 6 - Concurrency / Channels / Timeout: If you want though, you can receive it: (1 shared statement(s), 1 shared atom(s))
- [[coding-little-go-book-value]] - shared technical atoms: Value shares technical record from Chapter 6 - Concurrency / Channels / Timeout: go func() { time.Sleep(d) c <- true }() return c } (3 shared atom(s))
- [[coding-little-go-book-worker]] - shared technical atoms: Worker shares technical record from Chapter 6 - Concurrency / Channels: id int (3 shared atom(s))
- [[coding-little-go-book-concurrent]] - shared technical atoms: Concurrent shares technical record from Conclusion: Still, it comes down to some basic rules (like you can only declare variable once and := does declare the variable) and fundamental understanding (like new(X) or &X{ ... [truncated] (1 shared atom(s))
- [[coding-little-go-book-goroutine]] - shared technical atoms: Goroutine shares technical record from Conclusion: Still, it comes down to some basic rules (like you can only declare variable once and := does declare the variable) and fundamental understanding (like new(X) or &X{ ... [truncated] (1 shared atom(s))
- [[coding-little-go-book-programming]] - shared technical atoms: Programming shares technical record from Conclusion: Still, it comes down to some basic rules (like you can only declare variable once and := does declare the variable) and fundamental understanding (like new(X) or &X{ ... [truncated] (1 shared atom(s))
- [[coding-little-go-book-you-continue]] - shared statements: Before You Continue shares source evidence from Chapter 6 - Concurrency / Before You Continue: Having said that, I still make extensive use of the various synchronization primitives found in the sync and sync/atomic packages. I think it's important to be comfo ... [truncated] (1 shared statement(s))
- [[coding-little-go-book-section-chapter-6-concurrency-channels-5666c1f3]] - source section: Chapter 6 - Concurrency / Channels shares source evidence from Chapter 6 - Concurrency / Channels: Our worker is simple. It waits until data is available then "processes" it. Dutifully, it does this in a loop, forever waiting for more data to process. To use this, ... [truncated]; Chapter 6 - Concurrency / Channels shares technical record from Chapter 6 - Concurrency / Channels: id int (39 shared statement(s), 12 shared atom(s))

## Source

- [[coding-little-go-book]]
