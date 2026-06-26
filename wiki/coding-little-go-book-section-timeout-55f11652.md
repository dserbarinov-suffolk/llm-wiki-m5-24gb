---
page_id: coding-little-go-book-section-timeout-55f11652
page_kind: source
summary: Timeout: 24 source-backed entries and 5 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: sources/coding-little-go-book/sections
source_id: coding_little_go_book.pdf
projection_coverage: section-coding-little-go-book-section-timeout-55f11652@263eb84219c8d087131034e18f4b6ab2
---

# Timeout

From [[coding-little-go-book]].

## Statements

- Another popular option is to timeout. _(coding_little_go_book.pdf (source-range-810ce361-00450))_
- We've looked at buffering messages as well as simply dropping them. _(coding_little_go_book.pdf (source-range-810ce361-00450))_
- This is also something easy to achieve in Go. _(coding_little_go_book.pdf (source-range-810ce361-00450))_
- To block for a maximum amount of time, we can use the time.After function. _(coding_little_go_book.pdf (source-range-810ce361-00451))_
- To block for a maximum amount of time, we can use the time.After function. _(coding_little_go_book.pdf (source-range-810ce361-00451))_
- The channel is written to after the specified time expires. _(coding_little_go_book.pdf (source-range-810ce361-00453))_
- time.After returns a channel, so we can select from it. _(coding_little_go_book.pdf (source-range-810ce361-00453))_
- time.After returns a channel, so we can select from it. _(coding_little_go_book.pdf (source-range-810ce361-00453))_
- The channel is written to after the specified time expires. _(coding_little_go_book.pdf (source-range-810ce361-00453))_
- Back to our select , there are a couple of things to play with. _(coding_little_go_book.pdf (source-range-810ce361-00456))_
- If you aren't sure what's going on, remember that default fires immediately if no channel is available. _(coding_little_go_book.pdf (source-range-810ce361-00456))_
- Also, time.After is a channel of type chan time.Time . _(coding_little_go_book.pdf (source-range-810ce361-00457))_
- In the above example, we simply discard the value that was sent to the channel. _(coding_little_go_book.pdf (source-range-810ce361-00457))_
- Also, time.After is a channel of type chan time.Time . _(coding_little_go_book.pdf (source-range-810ce361-00457))_
- Notice that we're sending to c but receiving from time.After . _(coding_little_go_book.pdf (source-range-810ce361-00459))_
- - The first available channel is chosen. _(coding_little_go_book.pdf (source-range-810ce361-00460))_
- - If multiple channels are available, one is randomly picked. _(coding_little_go_book.pdf (source-range-810ce361-00461))_
- - If no channel is available, the default case is executed. _(coding_little_go_book.pdf (source-range-810ce361-00462))_
- Finally, it's common to see a select inside a for . _(coding_little_go_book.pdf (source-range-810ce361-00464))_

## Technical atoms

```
for { select { case c	<-	rand.Int(): case <-time.After(time.Millisecond	*	100): fmt.Println("timed	out") } time.Sleep(time.Millisecond	*	50) }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00452))_

```
func after(d	time.Duration) chan bool	{ c	:=	make( chan bool)
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00454))_

```
go func ()	{ time.Sleep(d) c	<-	true }() return c }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00455))_

```
case t	:=	<-time.After(time.Millisecond	*	100): fmt.Println("timed	out	at",	t)
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00458))_

```
for { select { case data	:=	<-c: fmt.Printf("worker	%d	got	%d\n",	w.id,	data) case <-time.After(time.Millisecond	*	10): fmt.Println("Break	time") time.Sleep(time.Second) } }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00465))_
