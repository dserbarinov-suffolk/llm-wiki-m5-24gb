---
page_id: coding-little-go-book-you-continue
page_kind: concept
summary: Before You Continue: 15 statement(s) and 3 atom(s) from raw/coding_little_go_book.pdf.
page_family: topic-concept
sources: raw/coding_little_go_book.pdf
updated: 2026-06-30
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-you-continue@e120fd1338c3f33290a18387c7476620
---

# Before You Continue

What [[coding-little-go-book]] covers about before you continue:

## Statements

### Chapter 4 - Code Organization and Interfaces / Before You Continue

- Ultimately, how you structure your code around Go's workspace is something that you'll only feel comfortable with after you've written a couple of non-trivial projects. What's most important for you to remember is the tight relationship between package names and your directory structure (not just within a project, but within the entire workspace). _(coding_little_go_book.pdf (source-range-23d24eb1-00333))_

- The way Go handles visibility of types is straightforward and effective. It's also consistent. There are a few things we haven't looked at, such as constants and global variables but rest assured, their visibility is determined by the same naming rule. _(coding_little_go_book.pdf (source-range-23d24eb1-00334))_

- Finally, if you're new to interfaces, it might take some time before you get a feel for them. However, the first time you see a function that expects something like io.Reader , you'll find yourself thanking the author for not demanding more than he or she needed. _(coding_little_go_book.pdf (source-range-23d24eb1-00335))_

### Chapter 5 - Tidbits / Before You Continue

- We looked at various aspects of programming with Go. Most notably, we saw how error handling behaves and how to release resources such as connections and open files. Many people dislike Go's approach to error handling. It can feel like a step backwards. Sometimes, I agree. Yet, I also find that it results in code that's easier to follow. defer is an unusual but practical approach to resource management. In fact, it isn't tied to resource management only. You can use defer for any purpose, such as logging when a function exits. _(coding_little_go_book.pdf (source-range-23d24eb1-00394))_

- Certainly, we haven't looked at all of the tidbits Go has to offer. But you should be feeling comfortable enough to tackle whatever you come across. _(coding_little_go_book.pdf (source-range-23d24eb1-00395))_

### Chapter 6 - Concurrency / Before You Continue

- If you're new to the world of concurrent programming, it might all seem rather overwhelming. It categorically demands considerably more attention and care. Go aims to make it easier. _(coding_little_go_book.pdf (source-range-23d24eb1-00467))_

- Goroutines effectively abstract what's needed to run concurrent code. Channels help eliminate some serious bugs that can happen when data is shared by eliminating the sharing of data. This doesn't just eliminate bugs, but it changes how one approaches concurrent programming. You start to think about concurrency with respect to message passing, rather than dangerous areas of code. _(coding_little_go_book.pdf (source-range-23d24eb1-00468))_

- Having said that, I still make extensive use of the various synchronization primitives found in the sync and sync/atomic packages. I think it's important to be comfortable with both. I encourage you to first focus on channels, but when you see a simple example that needs a short-lived lock, consider using a mutex or readwrite mutex. _(coding_little_go_book.pdf (source-range-23d24eb1-00469))_


## Technical atoms

### Technical frame 1: Chapter 4 - Code Organization and Interfaces / Before You Continue

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00334))_

> The way Go handles visibility of types is straightforward and effective. It's also consistent. There are a few things we haven't looked at, such as constants and global variables but rest assured, their visibility is determined by the same naming rule.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00335))_

> Finally, if you're new to interfaces, it might take some time before you get a feel for them.

### Technical frame 2: Chapter 5 - Tidbits / Before You Continue

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00395))_

> Certainly, we haven't looked at all of the tidbits Go has to offer. But you should be feeling comfortable enough to tackle whatever you come across.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00394))_

> You can use defer for any purpose, such as logging when a function exits.

### Technical frame 3: Chapter 6 - Concurrency / Before You Continue

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00469))_

> Having said that, I still make extensive use of the various synchronization primitives found in the sync and sync/atomic packages. I think it's important to be comfortable with both. I encourage you to first focus on channels, but when you see a simple example that needs a short-lived lock, consider using a mutex or readwrite mutex.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00468))_

> Channels help eliminate some serious bugs that can happen when data is shared by eliminating the sharing of data.


## Related pages

- [[coding-little-go-book-type]] - shared statements and technical atoms: Type shares source evidence from Chapter 4 - Code Organization and Interfaces / Before You Continue: The way Go handles visibility of types is straightforward and effective. It's also consistent. There are a few things we haven't looked at, such as constants and glo ... [truncated]; Type shares technical record from Chapter 4 - Code Organization and Interfaces / Before You Continue: Finally, if you're new to interfaces, it might take some time before you get a feel for them. (1 shared statement(s), 1 shared atom(s))
- [[coding-little-go-book-code]] - shared statements: Code shares source evidence from Chapter 4 - Code Organization and Interfaces / Before You Continue: Ultimately, how you structure your code around Go's workspace is something that you'll only feel comfortable with after you've written a couple of non-trivial projec ... [truncated] (1 shared statement(s))
- [[coding-little-go-book-function]] - shared statements: Function shares source evidence from Chapter 4 - Code Organization and Interfaces / Before You Continue: Finally, if you're new to interfaces, it might take some time before you get a feel for them. However, the first time you see a function that expects something like ... [truncated] (1 shared statement(s))
- [[coding-little-go-book-section-chapter-4-code-organization-and-interfaces-before-you-continue-75e8df25]] - source section: Chapter 4 - Code Organization and Interfaces / Before You Continue shares source evidence from Chapter 4 - Code Organization and Interfaces / Before You Continue: Ultimately, how you structure your code around Go's workspace is something that you'll only feel comfortable with after you've written a couple of non-trivial projec ... [truncated]; Chapter 4 - Code Organization and Interfaces / Before You Continue shares technical record from Chapter 4 - Code Organization and Interfaces / Before You Continue: Finally, if you're new to interfaces, it might take some time before you get a feel for them. (5 shared statement(s), 1 shared atom(s))
- [[coding-little-go-book-section-chapter-5-tidbits-before-you-continue-25d54302]] - source section: Chapter 5 - Tidbits / Before You Continue shares source evidence from Chapter 5 - Tidbits / Before You Continue: We looked at various aspects of programming with Go. Most notably, we saw how error handling behaves and how to release resources such as connections and open files. ... [truncated]; Chapter 5 - Tidbits / Before You Continue shares technical record from Chapter 5 - Tidbits / Before You Continue: You can use defer for any purpose, such as logging when a function exits. (5 shared statement(s), 1 shared atom(s))
- [[coding-little-go-book-section-chapter-6-concurrency-before-you-continue-a4098176]] - source section: Chapter 6 - Concurrency / Before You Continue shares source evidence from Chapter 6 - Concurrency / Before You Continue: If you're new to the world of concurrent programming, it might all seem rather overwhelming. It categorically demands considerably more attention and care. Go aims t ... [truncated]; Chapter 6 - Concurrency / Before You Continue shares technical record from Chapter 6 - Concurrency / Before You Continue: Channels help eliminate some serious bugs that can happen when data is shared by eliminating the sharing of data. (5 shared statement(s), 1 shared atom(s))

## Source

- [[coding-little-go-book]]
