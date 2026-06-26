---
page_id: coding-little-go-book-select
page_kind: concept
summary: Select: 10 statement(s) and 1 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-select@f02f4486ed4addd376bd027fd12f0cae
---

# Select

What [[coding-little-go-book]] covers about select:

## Statements

- We can't use up an infinite amount of memory hoping a worker frees up. _(coding_little_go_book.pdf (source-range-773b6275-00443))_
- Even with buffering, there comes a point where we need to start dropping messages. _(coding_little_go_book.pdf (source-range-773b6275-00443))_
- With it, we can provide code for when the channel isn't available to send to. _(coding_little_go_book.pdf (source-range-773b6275-00444))_
- We're pushing out 20 messages per second, but our workers can only handle 10 per second; thus, half the messages get dropped. _(coding_little_go_book.pdf (source-range-773b6275-00446))_
- A main purpose of select is to manage multiple channels. _(coding_little_go_book.pdf (source-range-773b6275-00447))_
- If no channel is available, default is executed if one is provided. _(coding_little_go_book.pdf (source-range-773b6275-00447))_
- A channel is randomly picked when multiple are available. _(coding_little_go_book.pdf (source-range-773b6275-00447))_
- Given multiple channels, select will block until the first one becomes available. _(coding_little_go_book.pdf (source-range-773b6275-00447))_
- This is only the start of what we can accomplish with select . _(coding_little_go_book.pdf (source-range-773b6275-00447))_
- It's hard to come up with a simple example that demonstrates this behavior as it's a fairly advanced feature. _(coding_little_go_book.pdf (source-range-773b6275-00448))_

## Technical atoms

> Context: Syntactically, select looks a bit like a switch. With it, we can provide code for when the channel isn't available to send to. First, let's remove our channel's buffering so that we can clearly see how select works:
_(context: coding_little_go_book.pdf (source-range-773b6275-00444))_

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
_(source: coding_little_go_book.pdf (source-range-773b6275-00445))_


## Source

- [[coding-little-go-book]]
