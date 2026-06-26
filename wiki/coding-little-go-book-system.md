---
page_id: coding-little-go-book-system
page_kind: concept
summary: System: 9 statement(s) and 6 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-system@39f29932d86dfceb5a9bc1ac8a1c9607
---

# System

What [[coding-little-go-book]] covers about system:

## Statements

- For some systems, dynamic languages are categorically more productive. _(coding_little_go_book.pdf (source-range-810ce361-00107))_
- If you're on an x64 system, you'll want go#.#.#.windows-amd64.zip , where #.#.# is the latest version of Go. _(coding_little_go_book.pdf (source-range-810ce361-00030))_
- There are worse possibilities too, such as system crashes or accessing an arbitrary piece of data and incrementing it! _(coding_little_go_book.pdf (source-range-810ce361-00413))_
- Some versions of Windows provide this control panel through the Advanced System Settings option inside the System control panel. _(coding_little_go_book.pdf (source-range-810ce361-00030))_
- With a rigid type system, a compiler is able to detect problems beyond mere syntactical mistakes as well as make further optimizations. _(coding_little_go_book.pdf (source-range-810ce361-00037))_
- Learning new keywords, type system, coding style as well as new libraries, communities and paradigms is a lot of work that seems hard to justify. _(coding_little_go_book.pdf (source-range-810ce361-00012))_
- Similarly, you can use Go to build websites (and many people do), but I still prefer, by a wide margin, the expressiveness of Node or Ruby for such systems. _(coding_little_go_book.pdf (source-range-810ce361-00016))_
- From a practical point of view, this chapter introduced structures, how to make an instance of a structure a receiver of a function, and added pointers to our existing knowledge of Go's type system. _(coding_little_go_book.pdf (source-range-810ce361-00186))_
- I don't know what label to give it, but over the course of my career, as systems continue to grow in complexity and as concurrency frequently measures in the tens of thousands, there's clearly been a growing need for custom infrastructure-type systems. _(coding_little_go_book.pdf (source-range-810ce361-00016))_

## Code, rules, and examples

> I can't speak authoritatively for system developers, but for those of us building websites, services, desktop applications and the like, it partially comes down to the emerging need for a class of systems that sit somewhere in between low-level system applications and higherlevel applications.
_(source: coding_little_go_book.pdf (source-range-810ce361-00015))_

> Go was built as a system language (e.g., operating systems, device drivers) and thus aimed at C and C++ developers. According to the Go team, and which is certainly true of me, application developers, not system developers, have become the primary Go users. Why? I can't speak authoritatively for system developers, but for those of us building websites, services, desktop applications and the like, it partially comes down to the emerging need for a class of systems that sit somewhere in between low-level system applications and higherlevel applications.
_(source: coding_little_go_book.pdf (source-range-810ce361-00015))_

> You can build such systems with Ruby or Python or something else (and many people do), but these types of systems can benefit from a more rigid type system and greater performance.
_(source: coding_little_go_book.pdf (source-range-810ce361-00016))_

> Environment variables can be set through the Environment Variables button on the Advanced tab of the System control panel.
_(source: coding_little_go_book.pdf (source-range-810ce361-00030))_

> To keep more complicated libraries and systems organized, we need to learn about packages. In Go, package names follow the directory structure of your Go workspace. If we were building a shopping system, we'd probably start with a package name "shopping" and put our source files in $GOPATH/src/shopping/ . We don't want to put everything inside this folder though. For example, maybe we want to isolate some database logic inside its own folder. To achieve this, we create a subfolder at $GOPATH/src/shopping/db . The package name of the files within this subfolder is simply db , but to access it from another package, including the shopping package, we need to import shopping/db . In other words, when you name a package, via the package keyword, you provide a single value, not a complete hierarchy (e.g., "shopping" or "db"). When you import a package, you specify the complete path. Let's try it. Inside your Go workspace's src folder (which we set up in Getting Started of the Introduction), create a new folder called shopping and a subfolder within it called db . Inside of shopping/db , create a file called db.go and add the following code:
_(source: coding_little_go_book.pdf (source-range-810ce361-00273))_

> The challenge with concurrent programming stems from sharing data. If your goroutines share no data, you needn't worry about synchronizing them. That isn't an option for all systems, however. In fact, many systems are built with the exact opposite goal in mind: to share data across multiple requests. An in-memory cache or a database, are good examples of this. This is becoming an increasingly common reality. Channels help make concurrent programming saner by taking shared data out of the picture. A channel is a communication pipe between goroutines which is used to pass data. In other words, a goroutine that has data can pass it to another goroutine via a channel. The result is that, at any point in time, only one goroutine has access to the data. A channel, like everything else, has a type. This is the type of data that we'll be passing through our channel. For example, to create a channel which can be used to pass an integer around, we'd do: The type of this channel is chan int . Therefore, to pass this channel to a function, our signature looks like: Channels support two operations: receiving and sending. We send to a channel by doing: CHANNEL <- DATA and receive from one by doing VAR := <-CHANNEL The arrow points in the direction that data flows. When sending, the data flows into the channel. When receiving, the data flows out of the channel. The final thing to know before we look at our first example is that receiving and sending to and from a channel is blocking. That is, when we receive from a channel, execution of the goroutine won't continue until data is available. Similarly, when we send to a channel, execution won't continue until the data is received. Consider a system with incoming data that we want to handle in separate goroutines. This is a common requirement. If we did our data-intensive processing on the goroutine which accepts the incoming data, we'd risk timing out clients. First, we'll write our worker. This could be a simple function, but I'll make it part of a structure since we haven't seen goroutines used like this before: c := make( chan int) func worker(c chan int) { ... } type Worker struct {
_(source: coding_little_go_book.pdf (source-range-810ce361-00426))_


## Source

- [[coding-little-go-book]]
