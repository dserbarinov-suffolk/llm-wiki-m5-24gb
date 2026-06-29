---
page_id: coding-little-go-book-section-chapter-6-concurrency-55851f5e
page_kind: source
summary: Chapter 6 - Concurrency: 132 source-backed entries and 23 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-29
domain: coding-little-go-book
category_path: sources/coding-little-go-book/sections
source_id: coding_little_go_book.pdf
projection_coverage: section-coding-little-go-book-section-chapter-6-concurrency-55851f5e@179a5c634d7fb35e9fad283cb412dc73
---

# Chapter 6 - Concurrency

From [[coding-little-go-book]].

## Related pages

- [[coding-little-go-book-section-chapter-6-concurrency-goroutines-8aab6c69]] - narrower source section: Chapter 6 - Concurrency / Goroutines
- [[coding-little-go-book-section-chapter-6-concurrency-synchronization-e924d99c]] - narrower source section: Chapter 6 - Concurrency / Synchronization
- [[coding-little-go-book-section-chapter-6-concurrency-channels-5666c1f3]] - narrower source section: Chapter 6 - Concurrency / Channels
- [[coding-little-go-book-section-chapter-6-concurrency-before-you-continue-a4098176]] - narrower source section: Chapter 6 - Concurrency / Before You Continue
- [[coding-little-go-book-section-chapter-5-tidbits-e7a41f7c]] - previous source section: Chapter 5 - Tidbits
- [[coding-little-go-book-section-conclusion-2a806c10]] - next source section: Conclusion
- [[coding-little-go-book-concurrency]] - topic hub: opens the topic page for Concurrency

## Statements

- Go is often described as a concurrent-friendly language. The reason for this is that it provides a simple syntax over two powerful mechanisms: goroutines and channels. _(coding_little_go_book.pdf (source-range-23d24eb1-00397))_

## Statements by subsection

### Chapter 6 - Concurrency / Goroutines

- A goroutine is similar to a thread, but it is scheduled by Go, not the OS. Code that runs in a goroutine can run concurrently with other code. Let's look at an example: _(coding_little_go_book.pdf (source-range-23d24eb1-00399))_
- There are a few interesting things going on here, but the most important is how we start a goroutine. We simply use the go keyword followed by the function we want to execute. If we just want to run a bit of code, such as the above, we can use an anonymous function. Do note that anonymous functions aren't only used with goroutines, however. _(coding_little_go_book.pdf (source-range-23d24eb1-00402))_
- Goroutines are easy to create and have little overhead. Multiple goroutines will end up running on the same underlying OS thread. This is often called an M:N threading model because we have M application threads (goroutines) running on N OS threads. The result is that a goroutine has a fraction of overhead (a few KB) than OS threads. On modern hardware, it's possible to have millions of goroutines. _(coding_little_go_book.pdf (source-range-23d24eb1-00404))_
- Furthermore, the complexity of mapping and scheduling is hidden. We just say this code should run concurrently and let Go worry about making it happen. _(coding_little_go_book.pdf (source-range-23d24eb1-00405))_
- If we go back to our example, you'll notice that we had to Sleep for a few milliseconds. That's because the main process exits before the goroutine gets a chance to execute (the process doesn't wait until all goroutines are finished before exiting). To solve this, we need to coordinate our code. _(coding_little_go_book.pdf (source-range-23d24eb1-00406))_
- Do note that anonymous functions aren't only used with goroutines, however. _(coding_little_go_book.pdf (source-range-23d24eb1-00402))_
- If we just want to run a bit of code, such as the above, we can use an anonymous function. _(coding_little_go_book.pdf (source-range-23d24eb1-00402))_
- This is often called an M:N threading model because we have M application threads (goroutines) running on N OS threads. _(coding_little_go_book.pdf (source-range-23d24eb1-00404))_
- That's because the main process exits before the goroutine gets a chance to execute (the process doesn't wait until all goroutines are finished before exiting). _(coding_little_go_book.pdf (source-range-23d24eb1-00406))_

### Chapter 6 - Concurrency / Synchronization

- Creating goroutines is trivial, and they are so cheap that we can start many; however, concurrent code needs to be coordinated. To help with this problem, Go provides channels . Before we look at channels , I think it's important to understand a little bit about the basics of concurrent programming. _(coding_little_go_book.pdf (source-range-23d24eb1-00408))_
- Writing concurrent code requires that you pay specific attention to where and how you read and write values. In some ways, it's like programming without a garbage collector -- it requires that you think about your data from a new angle, always watchful for possible danger. Consider: _(coding_little_go_book.pdf (source-range-23d24eb1-00409))_
- If you think the output is 1, 2, ... 20 you're both right and wrong. It's true that if you run the above code, you'll sometimes get that output. However, the reality is that the behavior is undefined. Why? Because we potentially have multiple (two in this case) goroutines writing to the same variable, counter , at the same time. Or, just as bad, one goroutine would be reading counter while another writes to it. _(coding_little_go_book.pdf (source-range-23d24eb1-00413))_
- Is that really a danger? Yes, absolutely. counter++ might seem like a simple line of code, but it actually gets broken down into multiple assembly statements -- the exact nature is dependent on the platform that you're running. If you run this example, you'll see that very often the numbers are printed in a weird order, and/or numbers are duplicated/missing. There are worse possibilities too, such as system crashes or accessing an arbitrary piece of data and incrementing it! _(coding_little_go_book.pdf (source-range-23d24eb1-00414))_
- The only concurrent thing you can safely do to a variable is to read from it. You can have as many readers as you want, but writes need to be synchronized. There are various ways to do this, including using some truly atomic operations that rely on special CPU instructions. However, the most common approach is to use a mutex: _(coding_little_go_book.pdf (source-range-23d24eb1-00415))_
- A mutex serializes access to the code under lock. The reason we simply define our lock as lock sync.Mutex is because the default value of a sync.Mutex is unlocked. _(coding_little_go_book.pdf (source-range-23d24eb1-00417))_
- Seems simple enough? The example above is deceptive. There's a whole class of serious bugs that can arise when doing concurrent programming. First of all, it isn't always so obvious what code needs to be protected. While it might be tempting to use coarse locks (locks that cover a large amount of code), that undermines the very reason we're doing concurrent programming in the first place. We generally want fine locks; else, we end up with a ten-lane highway that suddenly turns into a one-lane road. _(coding_little_go_book.pdf (source-range-23d24eb1-00418))_
- The other problem has to do with deadlocks. With a single lock, this isn't a problem, but if you're using two or more locks around the same code, it's dangerously easy to have situations where goroutineA holds lockA but needs access to lockB, while goroutineB holds lockB but needs access to lockA. _(coding_little_go_book.pdf (source-range-23d24eb1-00419))_
- It actually is possible to deadlock with a single lock, if we forget to release it. This isn't as dangerous as a multi-lock deadlock (because those are really tough to spot), but just so you can see what happens, try running: _(coding_little_go_book.pdf (source-range-23d24eb1-00420))_
- There's more to concurrent programming than what we've seen so far. For one thing, there's another common mutex called a read-write mutex. This exposes two locking functions: one to lock for reading and one to lock for writing. This distinction allows multiple simultaneous readers while ensuring that writing is exclusive. In Go, sync.RWMutex is such a lock. In addition to the Lock and Unlock methods of a sync.Mutex , it also exposes RLock and RUnlock methods; where R stands for Read . While read-write mutexes are commonly used, they place an additional burden on developers: we must now pay attention to not only when we're accessing data, but also how. _(coding_little_go_book.pdf (source-range-23d24eb1-00423))_
- These are all things that are doable without channels . Certainly for simpler cases, I believe you should use primitives such as sync.Mutex and sync.RWMutex , but as we'll see in the next section, channels aim at making concurrent programming cleaner and less error-prone. _(coding_little_go_book.pdf (source-range-23d24eb1-00425))_
- Because we potentially have multiple (two in this case) goroutines writing to the same variable, counter , at the same time. _(coding_little_go_book.pdf (source-range-23d24eb1-00413))_
- There are worse possibilities too, such as system crashes or accessing an arbitrary piece of data and incrementing it! _(coding_little_go_book.pdf (source-range-23d24eb1-00414))_
- The only concurrent thing you can safely do to a variable is to read from it. _(coding_little_go_book.pdf (source-range-23d24eb1-00415))_
- The reason we simply define our lock as lock sync.Mutex is because the default value of a sync.Mutex is unlocked. _(coding_little_go_book.pdf (source-range-23d24eb1-00417))_
- This isn't as dangerous as a multi-lock deadlock (because those are really tough to spot), but just so you can see what happens, try running: _(coding_little_go_book.pdf (source-range-23d24eb1-00420))_
- While read-write mutexes are commonly used, they place an additional burden on developers: we must now pay attention to not only when we're accessing data, but also how. _(coding_little_go_book.pdf (source-range-23d24eb1-00423))_
- For example, sleeping for 10 milliseconds isn't a particularly elegant solution. _(coding_little_go_book.pdf (source-range-23d24eb1-00424))_

### Chapter 6 - Concurrency / Channels

- Our worker is simple. It waits until data is available then "processes" it. Dutifully, it does this in a loop, forever waiting for more data to process. To use this, the first thing we'd do is start some workers: And then we can give them some work: Here's the complete code to make it run: } func (w Worker) process(c chan int) { for { data := <-c fmt.Printf("worker %d got %d\n", w.id, data) } } c := make( chan int) for i := 0; i < 5; i++ { worker := &Worker{id: i} go worker.process(c) } for { c <- rand.Int() time.Sleep(time.Millisecond * 50) } package main import ( "fmt" "time" "math/rand" ) func main() { c := make( chan int) for i := 0; i < 5; i++ { worker := &Worker{id: i} go worker.process(c) } for { c <- rand.Int() time.Sleep(time.Millisecond * 50) } } type Worker struct { id int } func (w *Worker) process(c chan int) { for { data := <-c fmt.Printf("worker %d got %d\n", w.id, data) } } _(coding_little_go_book.pdf (source-range-23d24eb1-00429))_
- We don't know which worker is going to get what data. What we do know, what Go guarantees, is that the data we send to a channel will only be received by a single receiver. _(coding_little_go_book.pdf (source-range-23d24eb1-00430))_
- Notice that the only shared state is the channel, which we can safely receive from and send to concurrently. Channels provide all of the synchronization code we need and also ensure that, at any given time, only one goroutine has access to a specific piece of data. _(coding_little_go_book.pdf (source-range-23d24eb1-00431))_
- It waits until data is available then "processes" it. _(coding_little_go_book.pdf (source-range-23d24eb1-00429))_
- Notice that the only shared state is the channel, which we can safely receive from and send to concurrently. _(coding_little_go_book.pdf (source-range-23d24eb1-00431))_
- Channels provide all of the synchronization code we need and also ensure that, at any given time, only one goroutine has access to a specific piece of data. _(coding_little_go_book.pdf (source-range-23d24eb1-00431))_

### Chapter 6 - Concurrency / Channels / Buffered Channels

- What's happening is that our main code, the one that accepts the user's incoming data (which we just simulated with a random number generator) is blocking as it sends to the channel because no receiver is available. _(coding_little_go_book.pdf (source-range-23d24eb1-00435))_
- In cases where you need high guarantees that the data is being processed, you probably will want to start blocking the client. In other cases, you might be willing to loosen those guarantees. There are a few popular strategies to do this. The first is to buffer the data. If no worker is available, we want to temporarily store the data in some sort of queue. Channels have this buffering capability built-in. When we created our channel with make , we can give our channel a length: _(coding_little_go_book.pdf (source-range-23d24eb1-00436))_
- You can make this change, but you'll notice that the processing is still choppy. Buffered channels don't add more capacity; they merely provide a queue for pending work and a good way to deal with a sudden spike. In our example, we're continuously pushing more data than our workers can handle. _(coding_little_go_book.pdf (source-range-23d24eb1-00438))_
- You can see that it grows and grows until it fills up, at which point sending to our channel start to block again. _(coding_little_go_book.pdf (source-range-23d24eb1-00441))_
- What's happening is that our main code, the one that accepts the user's incoming data (which we just simulated with a random number generator) is blocking as it sends to the channel because no receiver is available. _(coding_little_go_book.pdf (source-range-23d24eb1-00435))_

### Chapter 6 - Concurrency / Channels / Select

- Even with buffering, there comes a point where we need to start dropping messages. We can't use up an infinite amount of memory hoping a worker frees up. For this, we use Go's select . _(coding_little_go_book.pdf (source-range-23d24eb1-00443))_
- Syntactically, select looks a bit like a switch. With it, we can provide code for when the channel isn't available to send to. First, let's remove our channel's buffering so that we can clearly see how select works: _(coding_little_go_book.pdf (source-range-23d24eb1-00444))_
- We're pushing out 20 messages per second, but our workers can only handle 10 per second; thus, half the messages get dropped. _(coding_little_go_book.pdf (source-range-23d24eb1-00446))_
- This is only the start of what we can accomplish with select . A main purpose of select is to manage multiple channels. Given multiple channels, select will block until the first one becomes available. If no channel is available, default is executed if one is provided. A channel is randomly picked when multiple are available. _(coding_little_go_book.pdf (source-range-23d24eb1-00447))_
- It's hard to come up with a simple example that demonstrates this behavior as it's a fairly advanced feature. The next section might help illustrate this though. _(coding_little_go_book.pdf (source-range-23d24eb1-00448))_
- We're pushing out 20 messages per second, but our workers can only handle 10 per second; thus, half the messages get dropped. _(coding_little_go_book.pdf (source-range-23d24eb1-00446))_
- This is only the start of what we can accomplish with select . _(coding_little_go_book.pdf (source-range-23d24eb1-00447))_

### Chapter 6 - Concurrency / Channels / Timeout

- We've looked at buffering messages as well as simply dropping them. Another popular option is to timeout. We're willing to block for some time, but not forever. This is also something easy to achieve in Go. Admittedly, the syntax might be hard to follow but it's such a neat and useful feature that I couldn't leave it out. _(coding_little_go_book.pdf (source-range-23d24eb1-00450))_
- To block for a maximum amount of time, we can use the time.After function. Let's look at it then try to peek beyond the magic. To use this, our sender becomes: _(coding_little_go_book.pdf (source-range-23d24eb1-00451))_
- time.After returns a channel, so we can select from it. The channel is written to after the specified time expires. That's it. There's nothing more magical than that. If you're curious, here's what an implementation of after could look like: _(coding_little_go_book.pdf (source-range-23d24eb1-00453))_
- Back to our select , there are a couple of things to play with. First, what happens if you add the default case back? Can you guess? Try it. If you aren't sure what's going on, remember that default fires immediately if no channel is available. _(coding_little_go_book.pdf (source-range-23d24eb1-00456))_
- Also, time.After is a channel of type chan time.Time . In the above example, we simply discard the value that was sent to the channel. If you want though, you can receive it: _(coding_little_go_book.pdf (source-range-23d24eb1-00457))_
- The first available channel is chosen. _(coding_little_go_book.pdf (source-range-23d24eb1-00460))_
- If multiple channels are available, one is randomly picked. _(coding_little_go_book.pdf (source-range-23d24eb1-00461))_
- If no channel is available, the default case is executed. _(coding_little_go_book.pdf (source-range-23d24eb1-00462))_
- To block for a maximum amount of time, we can use the time.After function. _(coding_little_go_book.pdf (source-range-23d24eb1-00451))_
- time.After returns a channel, so we can select from it. _(coding_little_go_book.pdf (source-range-23d24eb1-00453))_
- The channel is written to after the specified time expires. _(coding_little_go_book.pdf (source-range-23d24eb1-00453))_
- Also, time.After is a channel of type chan time.Time . _(coding_little_go_book.pdf (source-range-23d24eb1-00457))_
- Notice that we're sending to c but receiving from time.After . _(coding_little_go_book.pdf (source-range-23d24eb1-00459))_
- Finally, it's common to see a select inside a for . _(coding_little_go_book.pdf (source-range-23d24eb1-00464))_

### Chapter 6 - Concurrency / Before You Continue

- If you're new to the world of concurrent programming, it might all seem rather overwhelming. It categorically demands considerably more attention and care. Go aims to make it easier. _(coding_little_go_book.pdf (source-range-23d24eb1-00467))_
- Goroutines effectively abstract what's needed to run concurrent code. Channels help eliminate some serious bugs that can happen when data is shared by eliminating the sharing of data. This doesn't just eliminate bugs, but it changes how one approaches concurrent programming. You start to think about concurrency with respect to message passing, rather than dangerous areas of code. _(coding_little_go_book.pdf (source-range-23d24eb1-00468))_
- Having said that, I still make extensive use of the various synchronization primitives found in the sync and sync/atomic packages. I think it's important to be comfortable with both. I encourage you to first focus on channels, but when you see a simple example that needs a short-lived lock, consider using a mutex or readwrite mutex. _(coding_little_go_book.pdf (source-range-23d24eb1-00469))_

## Technical atoms

### Technical frame 1: Chapter 6 - Concurrency / Goroutines

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00402))_

> There are a few interesting things going on here, but the most important is how we start a goroutine. We simply use the go keyword followed by the function we want to execute. If we just want to run a bit of code, such as the above, we can use an anonymous function. Do note that anonymous functions aren't only used with goroutines, however.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00400))_

```
package main
import (
  "fmt"
  "time"
)
func main() {
  fmt.Println("start")
  go process()
  time.Sleep(time.Millisecond * 10) // this is bad, don't do this!
  fmt.Println("done")
}
```

### Technical frame 2: Chapter 6 - Concurrency / Goroutines

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00402))_

> There are a few interesting things going on here, but the most important is how we start a goroutine. We simply use the go keyword followed by the function we want to execute. If we just want to run a bit of code, such as the above, we can use an anonymous function. Do note that anonymous functions aren't only used with goroutines, however.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00401))_

```
func process() {
  fmt.Println("processing")
}
```

### Technical frame 3: Chapter 6 - Concurrency / Goroutines

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00404))_

> Goroutines are easy to create and have little overhead. Multiple goroutines will end up running on the same underlying OS thread. This is often called an M:N threading model because we have M application threads (goroutines) running on N OS threads. The result is that a goroutine has a fraction of overhead (a few KB) than OS threads. On modern hardware, it's possible to have millions of goroutines.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00403))_

```
go func() {
  fmt.Println("processing")
}()
```

### Technical frame 4: Chapter 6 - Concurrency / Synchronization

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00413))_

> If you think the output is 1, 2, ... 20 you're both right and wrong. It's true that if you run the above code, you'll sometimes get that output. However, the reality is that the behavior is undefined. Why? Because we potentially have multiple (two in this case) goroutines writing to the same variable, counter , at the same time. Or, just as bad, one goroutine would be reading counter while another writes to it.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00410))_

```
package main
import (
  "fmt"
  "time"
)
var counter = 0
func main() {
  for i := 0; i < 20; i++ {
    go incr()
```

### Technical frame 5: Chapter 6 - Concurrency / Synchronization

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00413))_

> If you think the output is 1, 2, ... 20 you're both right and wrong. It's true that if you run the above code, you'll sometimes get that output. However, the reality is that the behavior is undefined. Why? Because we potentially have multiple (two in this case) goroutines writing to the same variable, counter , at the same time. Or, just as bad, one goroutine would be reading counter while another writes to it.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00411))_

```
}
  time.Sleep(time.Millisecond * 10)
}
func incr() {
  counter++
  fmt.Println(counter)
}
```

### Technical frame 6: Chapter 6 - Concurrency / Synchronization

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00414))_

> Is that really a danger? Yes, absolutely. counter++ might seem like a simple line of code, but it actually gets broken down into multiple assembly statements -- the exact nature is dependent on the platform that you're running. If you run this example, you'll see that very often the numbers are printed in a weird order, and/or numbers are duplicated/missing. There are worse possibilities too, such as system crashes or accessing an arbitrary piece of data and incrementing it!

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00413))_

> It's true that if you run the above code, you'll sometimes get that output.

### Technical frame 7: Chapter 6 - Concurrency / Synchronization

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00417))_

> A mutex serializes access to the code under lock. The reason we simply define our lock as lock sync.Mutex is because the default value of a sync.Mutex is unlocked.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00416))_

```
package main
import (
  "fmt"
  "time"
  "sync"
)
var (
  counter = 0
  lock sync.Mutex
)
func main() {
  for i := 0; i < 20; i++ {
    go incr()
  }
  time.Sleep(time.Millisecond * 10)
}
func incr() {
  lock.Lock()
  defer lock.Unlock()
  counter++
  fmt.Println(counter)
}
```

### Technical frame 8: Chapter 6 - Concurrency / Synchronization

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00423))_

> There's more to concurrent programming than what we've seen so far. For one thing, there's another common mutex called a read-write mutex. This exposes two locking functions: one to lock for reading and one to lock for writing. This distinction allows multiple simultaneous readers while ensuring that writing is exclusive. In Go, sync.RWMutex is such a lock. In addition to the Lock and Unlock methods of a sync.Mutex , it also exposes RLock and RUnlock methods; where R stands for Read . While read

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00422))_

```
import (
  "time"
  "sync"
)
var (
  lock sync.Mutex
)
func main() {
  go func() { lock.Lock() }()
  time.Sleep(time.Millisecond * 10)
  lock.Lock()
}
```

### Technical frame 9: Chapter 6 - Concurrency / Synchronization

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00425))_

> These are all things that are doable without channels . Certainly for simpler cases, I believe you should use primitives such as sync.Mutex and sync.RWMutex , but as we'll see in the next section, channels aim at making concurrent programming cleaner and less error-prone.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00424))_

> What if a goroutine takes more than 10 milliseconds?

### Technical frame 10: Chapter 6 - Concurrency / Channels

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00429))_

> Our worker is simple. It waits until data is available then "processes" it. Dutifully, it does this in a loop, forever waiting for more data to process. To use this, the first thing we'd do is start some workers: And then we can give them some work: Here's the complete code to make it run: } func (w Worker) process(c chan int) { for { data := <-c fmt.Printf("worker %d got %d\n", w.id, data) } } c := make( chan int) for i := 0; i < 5; i++ { worker := &Worker{id: i} go worker.process(c) } for { c 

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00427))_

> The challenge with concurrent programming stems from sharing data. If your goroutines share no data, you needn't worry about synchronizing them. That isn't an option for all systems, however. In fact, many systems are built with the exact opposite goal in mind: to share data across multiple requests. An in-memory cache or a database, are good examples of this. This is becoming an increasingly common reality. Channels help make concurrent programming saner by taking shared data out of the picture. A channel is a communication pipe between goroutines which is used to pass data. In other words, a goroutine that has data can pass it to another goroutine via a channel. The result is that, at any point in time, only one goroutine has access to the data. A channel, like everything else, has a type. This is the type of data that we'll be passing through our channel. For example, to create a channel which can be used to pass an integer around, we'd do: The type of this channel is chan int . Therefore, to pass this channel to a function, our signature looks like: Channels support two operations: receiving and sending. We send to a channel by doing: CHANNEL <- DATA and receive from one by doing VAR := <-CHANNEL The arrow points in the direction that data flows. When sending, the data flows into the channel. When receiving, the data flows out of the channel. The final thing to know before we look at our first example is that receiving and sending to and from a channel is blocking. That is, when we receive from a channel, execution of the goroutine won't continue until data is available. Similarly, when we send to a channel, execution won't continue until the data is received. Consider a system with incoming data that we want to handle in separate goroutines. This is a common requirement. If we did our data-intensive processing on the goroutine which accepts the incoming data, we'd risk timing out clients. First, we'll write our worker. This could be a simple function, but I'll make it part of a structure since we haven't seen goroutines used like this before: c := make( chan int) func worker(c chan int) { ... } type Worker struct {

### Technical frame 11: Chapter 6 - Concurrency / Channels

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00429))_

> Our worker is simple. It waits until data is available then "processes" it. Dutifully, it does this in a loop, forever waiting for more data to process. To use this, the first thing we'd do is start some workers: And then we can give them some work: Here's the complete code to make it run: } func (w Worker) process(c chan int) { for { data := <-c fmt.Printf("worker %d got %d\n", w.id, data) } } c := make( chan int) for i := 0; i < 5; i++ { worker := &Worker{id: i} go worker.process(c) } for { c 

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00428))_

```
id int
```

### Technical frame 12: Chapter 6 - Concurrency / Channels / Buffered Channels

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

### Technical frame 13: Chapter 6 - Concurrency / Channels / Buffered Channels

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00438))_

> You can make this change, but you'll notice that the processing is still choppy. Buffered channels don't add more capacity; they merely provide a queue for pending work and a good way to deal with a sudden spike. In our example, we're continuously pushing more data than our workers can handle.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00437))_

```
c := make(chan int, 100)
```

### Technical frame 14: Chapter 6 - Concurrency / Channels / Buffered Channels

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

### Technical frame 15: Chapter 6 - Concurrency / Channels / Select

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

### Technical frame 16: Chapter 6 - Concurrency / Channels / Timeout

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

### Technical frame 17: Chapter 6 - Concurrency / Channels / Timeout

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00456))_

> Back to our select , there are a couple of things to play with. First, what happens if you add the default case back? Can you guess? Try it. If you aren't sure what's going on, remember that default fires immediately if no channel is available.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00454))_

```
func after(d time.Duration) chan bool {
  c := make(chan bool)
```

### Technical frame 18: Chapter 6 - Concurrency / Channels / Timeout

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

### Technical frame 19: Chapter 6 - Concurrency / Channels / Timeout

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00457))_

> Also, time.After is a channel of type chan time.Time . In the above example, we simply discard the value that was sent to the channel. If you want though, you can receive it:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00456))_

> First, what happens if you add the default case back?

### Technical frame 20: Chapter 6 - Concurrency / Channels / Timeout

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00460))_

> The first available channel is chosen.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00457))_

> If you want though, you can receive it:

### Technical frame 21: Chapter 6 - Concurrency / Channels / Timeout

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00460))_

> The first available channel is chosen.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00458))_

```
case t := <-time.After(time.Millisecond * 100):
  fmt.Println("timed out at", t)
```

### Technical frame 22: Chapter 6 - Concurrency / Channels / Timeout

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

### Technical frame 23: Chapter 6 - Concurrency / Before You Continue

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00469))_

> Having said that, I still make extensive use of the various synchronization primitives found in the sync and sync/atomic packages. I think it's important to be comfortable with both. I encourage you to first focus on channels, but when you see a simple example that needs a short-lived lock, consider using a mutex or readwrite mutex.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00468))_

> Channels help eliminate some serious bugs that can happen when data is shared by eliminating the sharing of data.
