---
page_id: coding-little-go-book-conclusion
page_kind: concept
summary: Conclusion: 17 statement(s) and 1 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-conclusion@d94e424fd71c9a0570cdd20fd0680816
---

# Conclusion

What [[coding-little-go-book]] covers about conclusion:

## Statements

- Perhaps, I did this reality a disservice. _(coding_little_go_book.pdf (source-range-773b6275-00471))_
- I recently heard Go described as a boring language. _(coding_little_go_book.pdf (source-range-773b6275-00471))_
- We did spend three chapters talking about types and how to declare variables after all. _(coding_little_go_book.pdf (source-range-773b6275-00471))_
- That Go makes pointers visible and that slices are thin wrappers around arrays probably isn't overwhelming to seasoned Java or C# developers. _(coding_little_go_book.pdf (source-range-773b6275-00472))_
- If you have a background in a statically typed language, much of what we saw was probably, at best, a refresher. _(coding_little_go_book.pdf (source-range-773b6275-00472))_
- Not least of which is the various syntax around declaration and initialization. _(coding_little_go_book.pdf (source-range-773b6275-00473))_
- It is a fair bit to learn. _(coding_little_go_book.pdf (source-range-773b6275-00473))_
- If you've mostly been making use of dynamic languages, you might feel a little different. _(coding_little_go_book.pdf (source-range-773b6275-00473))_
- Despite being a fan of Go, I find that for all the progress towards simplicity, there's something less than simple about it. _(coding_little_go_book.pdf (source-range-773b6275-00473))_
- Beyond this, Go gives us a simple but effective way to organize our code. _(coding_little_go_book.pdf (source-range-773b6275-00474))_
- Interfaces, return-based error handling, defer for resource management and a simple way to achieve composition. _(coding_little_go_book.pdf (source-range-773b6275-00474))_
- Given how hard concurrent programming can be, that is definitely a good thing. _(coding_little_go_book.pdf (source-range-773b6275-00475))_
- They are almost their own fundamental building block. _(coding_little_go_book.pdf (source-range-773b6275-00475))_
- There's little to say about goroutines other than they're effective and simple (simple to use anyway). _(coding_little_go_book.pdf (source-range-773b6275-00475))_

## Technical atoms

> Context: I recently heard Go described as a boring language. Boring because it's easy to learn, easy to write and, most importantly, easy to read. Perhaps, I did this reality a disservice. We did spend three chapters talking about types and how to declare variables after all. Last but not least is the built-in support for concurrency. There's little to say about goroutines other than they're effective and simple (simple to use anyway). It's a good abstraction. Channels are more complicated. I always think it's important to understand basics before using high-level wrappers. I do think learning about concurrent programming without channels is useful. Still, channels are implemented in a way that, to me, doesn't feel quite like a simple abstraction. They are almost their own fundamental building block. I say this because they change how you write and think about concurrent programming. Given how hard concurrent programming can be, that is definitely a good thing.
_(context: coding_little_go_book.pdf (source-range-773b6275-00471, source-range-773b6275-00475))_

> Still, it comes down to some basic rules (like you can only declare variable once and := does declare the variable) and fundamental understanding (like new(X) or &X{} only allocate memory, but slices, maps and channels require more initialization and thus, make ).
_(source: coding_little_go_book.pdf (source-range-773b6275-00473))_


## Source

- [[coding-little-go-book]]
