---
page_id: coding-little-go-book-section-chapter-6-concurrency-synchronization-e924d99c
page_kind: source
summary: Chapter 6 - Concurrency / Synchronization: 40 source-backed entries and 0 atom(s) from raw/coding_little_go_book.pdf.
page_family: section-reference
sources: raw/coding_little_go_book.pdf
updated: 2026-06-30
domain: coding-little-go-book
category_path: sources/coding-little-go-book/sections
source_id: coding_little_go_book.pdf
projection_coverage: section-coding-little-go-book-section-chapter-6-concurrency-synchronization-e924d99c@f0c3e3ccf9963cda03f4d849bbc8ec01
---

# Chapter 6 - Concurrency / Synchronization

From [[coding-little-go-book]].

## Related pages

- [[coding-little-go-book-section-chapter-6-concurrency-55851f5e]] - broader source section: Chapter 6 - Concurrency
- [[coding-little-go-book-section-chapter-6-concurrency-goroutines-8aab6c69]] - previous source section: Chapter 6 - Concurrency / Goroutines
- [[coding-little-go-book-section-chapter-6-concurrency-channels-5666c1f3]] - next source section: Chapter 6 - Concurrency / Channels

## Statements

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
