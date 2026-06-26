---
page_id: coding-little-go-book-maps
page_kind: concept
summary: Maps: 7 statement(s) and 4 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-maps@6f51cf313f269ce960a072b0a8674790
---

# Maps

What [[coding-little-go-book]] covers about maps:

## Statements

- Maps in Go are what other languages call hashtables or dictionaries. _(coding_little_go_book.pdf (source-range-773b6275-00248))_
- Maps, like slices, are created with the make function. _(coding_little_go_book.pdf (source-range-773b6275-00249))_
- Iteration over maps isn't ordered. _(coding_little_go_book.pdf (source-range-773b6275-00264))_
- Like make , this approach is specific to maps and arrays. _(coding_little_go_book.pdf (source-range-773b6275-00260))_
- They work as you expect: you define a key and value, and can get, set and delete values from it. _(coding_little_go_book.pdf (source-range-773b6275-00248))_
- To get the number of keys, we use len . _(coding_little_go_book.pdf (source-range-773b6275-00251))_
- Each iteration over a lookup will return the key value pair in a random order. _(coding_little_go_book.pdf (source-range-773b6275-00264))_

## Technical atoms

> Context: Maps, like slices, are created with the make function. Let's look at an example:
_(context: coding_little_go_book.pdf (source-range-773b6275-00249))_

```
func main() {
  lookup := make(map[string]int)
  lookup["goku"] = 9001
  power, exists := lookup["vegeta"]
// prints 0, false
  // 0 is the default value for an integer
  fmt.Println(power, exists)
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00250))_

> Context: Maps grow dynamically. However, we can supply a second argument to make to set an initial size:
_(context: coding_little_go_book.pdf (source-range-773b6275-00253))_

```
lookup := make(map[string]int, 100)
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00254))_

> Context: Maps grow dynamically. However, we can supply a second argument to make to set an initial size:
_(context: coding_little_go_book.pdf (source-range-773b6275-00253))_

> If you have some idea of how many keys your map will have, defining an initial size can help with performance.
_(source: coding_little_go_book.pdf (source-range-773b6275-00255))_

> Context: There's yet another way to declare and initialize values in Go. Like make , this approach is specific to maps and arrays. We can declare as a composite literal:
_(context: coding_little_go_book.pdf (source-range-773b6275-00260))_

```
lookup := map[string]int{
  "goku": 9001,
  "gohan": 2044,
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00261))_


## Source

- [[coding-little-go-book]]
