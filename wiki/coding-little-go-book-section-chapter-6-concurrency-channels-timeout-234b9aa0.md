---
page_id: coding-little-go-book-section-chapter-6-concurrency-channels-timeout-234b9aa0
page_kind: source
summary: Chapter 6 - Concurrency / Channels / Timeout: 26 source-backed entries and 0 atom(s) from raw/coding_little_go_book.pdf.
page_family: section-reference
sources: raw/coding_little_go_book.pdf
updated: 2026-06-30
domain: coding-little-go-book
category_path: sources/coding-little-go-book/sections
source_id: coding_little_go_book.pdf
projection_coverage: section-coding-little-go-book-section-chapter-6-concurrency-channels-timeout-234b9aa0@8bfbfd9db79d2b9a4e867ea54fa1d87b
---

# Chapter 6 - Concurrency / Channels / Timeout

From [[coding-little-go-book]].

## Related pages

- [[coding-little-go-book-section-chapter-6-concurrency-channels-5666c1f3]] - broader source section: Chapter 6 - Concurrency / Channels
- [[coding-little-go-book-section-chapter-6-concurrency-channels-select-98be429f]] - previous source section: Chapter 6 - Concurrency / Channels / Select

## Statements

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
