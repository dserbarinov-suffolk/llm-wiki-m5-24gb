---
page_id: coding-little-go-book-section-maps-bdc734f4
page_kind: source
summary: Maps: 15 source-backed entries and 8 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: sources/coding-little-go-book/sections
source_id: coding_little_go_book.pdf
projection_coverage: section-coding-little-go-book-section-maps-bdc734f4@97665b2c42ba80236b5d8bb60ac48e14
---

# Maps

From [[coding-little-go-book]].

## Statements

- Maps in Go are what other languages call hashtables or dictionaries. _(coding_little_go_book.pdf (source-range-773b6275-00248))_
- They work as you expect: you define a key and value, and can get, set and delete values from it. _(coding_little_go_book.pdf (source-range-773b6275-00248))_
- Maps, like slices, are created with the make function. _(coding_little_go_book.pdf (source-range-773b6275-00249))_
- To get the number of keys, we use len . _(coding_little_go_book.pdf (source-range-773b6275-00251))_
- Like make , this approach is specific to maps and arrays. _(coding_little_go_book.pdf (source-range-773b6275-00260))_
- Each iteration over a lookup will return the key value pair in a random order. _(coding_little_go_book.pdf (source-range-773b6275-00264))_
- Iteration over maps isn't ordered. _(coding_little_go_book.pdf (source-range-773b6275-00264))_

## Technical atoms

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

```
// returns 1
total := len(lookup)
// has no return, can be called on a non-existing key
delete(lookup, "goku")
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00252))_

```
lookup := make(map[string]int, 100)
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00254))_

> If you have some idea of how many keys your map will have, defining an initial size can help with performance.
_(source: coding_little_go_book.pdf (source-range-773b6275-00255))_

```
type Saiyan struct {
  Name string
  Friends map[string]*Saiyan
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00257))_

```
goku := &Saiyan{
  Name: "Goku",
  Friends: make(map[string]*Saiyan),
}
goku.Friends["krillin"] = ... //todo load or create Krillin
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00259))_

```
lookup := map[string]int{
  "goku": 9001,
  "gohan": 2044,
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00261))_

```
for key, value := range lookup {
  ...
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00263))_
