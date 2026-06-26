---
page_id: coding-little-go-book-section-select-cb67e916
page_kind: source
summary: Select: 13 source-backed entries and 1 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: sources/coding-little-go-book/sections
source_id: coding_little_go_book.pdf
projection_coverage: section-coding-little-go-book-section-select-cb67e916@1e8b36fe6a690c032e79c4a5a76b4661
---

# Select

From [[coding-little-go-book]].

## Statements

- We can't use up an infinite amount of memory hoping a worker frees up. _(coding_little_go_book.pdf (source-range-810ce361-00443))_
- Even with buffering, there comes a point where we need to start dropping messages. _(coding_little_go_book.pdf (source-range-810ce361-00443))_
- With it, we can provide code for when the channel isn't available to send to. _(coding_little_go_book.pdf (source-range-810ce361-00444))_
- We're pushing out 20 messages per second, but our workers can only handle 10 per second; thus, half the messages get dropped. _(coding_little_go_book.pdf (source-range-810ce361-00446))_
- We're pushing out 20 messages per second, but our workers can only handle 10 per second; thus, half the messages get dropped. _(coding_little_go_book.pdf (source-range-810ce361-00446))_
- A channel is randomly picked when multiple are available. _(coding_little_go_book.pdf (source-range-810ce361-00447))_
- This is only the start of what we can accomplish with select . _(coding_little_go_book.pdf (source-range-810ce361-00447))_
- A main purpose of select is to manage multiple channels. _(coding_little_go_book.pdf (source-range-810ce361-00447))_
- Given multiple channels, select will block until the first one becomes available. _(coding_little_go_book.pdf (source-range-810ce361-00447))_
- If no channel is available, default is executed if one is provided. _(coding_little_go_book.pdf (source-range-810ce361-00447))_
- This is only the start of what we can accomplish with select . _(coding_little_go_book.pdf (source-range-810ce361-00447))_
- It's hard to come up with a simple example that demonstrates this behavior as it's a fairly advanced feature. _(coding_little_go_book.pdf (source-range-810ce361-00448))_

## Technical atoms

```
Next,	we	change	our for loop: c	:=	make( chan int) for { select { case c	<-	rand.Int(): //optional	code	here default : //this	can	be	left	empty	to	silently	drop	the	data fmt.Println("dropped") } time.Sleep(time.Millisecond	*	50) }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00445))_
