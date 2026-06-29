---
page_id: coding-little-go-book-timeout
page_kind: concept
summary: Timeout: 13 statement(s) and 7 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-29
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-timeout@97bb4c6b6f9c22141cae2c57e3613f5c
---

# Timeout

What [[coding-little-go-book]] covers about timeout:

## Statements

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

### Technical frame 1: Chapter 6 - Concurrency / Channels / Timeout

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

### Technical frame 2: Chapter 6 - Concurrency / Channels / Timeout

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00456))_

> Back to our select , there are a couple of things to play with. First, what happens if you add the default case back? Can you guess? Try it. If you aren't sure what's going on, remember that default fires immediately if no channel is available.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00454))_

```
func after(d time.Duration) chan bool {
  c := make(chan bool)
```

### Technical frame 3: Chapter 6 - Concurrency / Channels / Timeout

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

### Technical frame 4: Chapter 6 - Concurrency / Channels / Timeout

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00457))_

> Also, time.After is a channel of type chan time.Time . In the above example, we simply discard the value that was sent to the channel. If you want though, you can receive it:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00456))_

> First, what happens if you add the default case back?

### Technical frame 5: Chapter 6 - Concurrency / Channels / Timeout

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00460))_

> The first available channel is chosen.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00457))_

> If you want though, you can receive it:

### Technical frame 6: Chapter 6 - Concurrency / Channels / Timeout

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00460))_

> The first available channel is chosen.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00458))_

```
case t := <-time.After(time.Millisecond * 100):
  fmt.Println("timed out at", t)
```

### Technical frame 7: Chapter 6 - Concurrency / Channels / Timeout

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

- [[coding-little-go-book-channel]] - shared statements and technical atoms: Channels shares source evidence from Chapter 6 - Concurrency / Channels / Timeout: We've looked at buffering messages as well as simply dropping them. Another popular option is to timeout. We're willing to block for some time, but not forever. This ... [truncated]; Channels shares technical record from Chapter 6 - Concurrency / Channels / Timeout: for { select { case c <- rand.Int(): case <-time.After(time.Millisecond * 100): fmt.Println("timed out") } time.Sleep(time.Millisecond * 50) } (13 shared statement(s), 7 shared atom(s))
- [[coding-little-go-book-concurrency]] - shared statements and technical atoms: Concurrency shares source evidence from Chapter 6 - Concurrency / Channels / Timeout: We've looked at buffering messages as well as simply dropping them. Another popular option is to timeout. We're willing to block for some time, but not forever. This ... [truncated]; Concurrency shares technical record from Chapter 6 - Concurrency / Channels / Timeout: for { select { case c <- rand.Int(): case <-time.After(time.Millisecond * 100): fmt.Println("timed out") } time.Sleep(time.Millisecond * 50) } (13 shared statement(s), 7 shared atom(s))
- [[coding-little-go-book-value]] - shared statements and technical atoms: Value shares source evidence from Chapter 6 - Concurrency / Channels / Timeout: Also, time.After is a channel of type chan time.Time . In the above example, we simply discard the value that was sent to the channel. If you want though, you can receive it:; Value shares technical record from Chapter 6 - Concurrency / Channels / Timeout: go func() { time.Sleep(d) c <- true }() return c } (1 shared statement(s), 3 shared atom(s))
- [[coding-little-go-book-section-chapter-6-concurrency-channels-timeout-234b9aa0]] - source section: Chapter 6 - Concurrency / Channels / Timeout shares source evidence from Chapter 6 - Concurrency / Channels / Timeout: We've looked at buffering messages as well as simply dropping them. Another popular option is to timeout. We're willing to block for some time, but not forever. This ... [truncated]; Chapter 6 - Concurrency / Channels / Timeout shares technical record from Chapter 6 - Concurrency / Channels / Timeout: for { select { case c <- rand.Int(): case <-time.After(time.Millisecond * 100): fmt.Println("timed out") } time.Sleep(time.Millisecond * 50) } (13 shared statement(s), 7 shared atom(s))

## Source

- [[coding-little-go-book]]
