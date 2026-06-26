---
page_id: coding-little-go-book-section-buffered-channels-8143a8b5
page_kind: source
summary: Buffered Channels: 14 source-backed entries and 3 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: sources/coding-little-go-book/sections
source_id: coding_little_go_book.pdf
projection_coverage: section-coding-little-go-book-section-buffered-channels-8143a8b5@9da2d2428075bde32f0de6332002860a
---

# Buffered Channels

From [[coding-little-go-book]].

## Statements

- What's happening is that our main code, the one that accepts the user's incoming data (which we just simulated with a random number generator) is blocking as it sends to the channel because no receiver is available. _(coding_little_go_book.pdf (source-range-810ce361-00435))_
- What's happening is that our main code, the one that accepts the user's incoming data (which we just simulated with a random number generator) is blocking as it sends to the channel because no receiver is available. _(coding_little_go_book.pdf (source-range-810ce361-00435))_
- In other cases, you might be willing to loosen those guarantees. _(coding_little_go_book.pdf (source-range-810ce361-00436))_
- If no worker is available, we want to temporarily store the data in some sort of queue. _(coding_little_go_book.pdf (source-range-810ce361-00436))_
- In cases where you need high guarantees that the data is being processed, you probably will want to start blocking the client. _(coding_little_go_book.pdf (source-range-810ce361-00436))_
- Channels have this buffering capability built-in. _(coding_little_go_book.pdf (source-range-810ce361-00436))_
- The first is to buffer the data. _(coding_little_go_book.pdf (source-range-810ce361-00436))_
- There are a few popular strategies to do this. _(coding_little_go_book.pdf (source-range-810ce361-00436))_
- In our example, we're continuously pushing more data than our workers can handle. _(coding_little_go_book.pdf (source-range-810ce361-00438))_
- You can make this change, but you'll notice that the processing is still choppy. _(coding_little_go_book.pdf (source-range-810ce361-00438))_
- You can see that it grows and grows until it fills up, at which point sending to our channel start to block again. _(coding_little_go_book.pdf (source-range-810ce361-00441))_

## Technical atoms

```
for { data	:=	<-c fmt.Printf("worker	%d	got	%d\n",	w.id,	data) time.Sleep(time.Millisecond	*	500) }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00434))_

```
c	:=	make( chan int,	100)
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00437))_

```
for { c	<-	rand.Int() fmt.Println(len(c)) time.Sleep(time.Millisecond	*	50) }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00440))_
