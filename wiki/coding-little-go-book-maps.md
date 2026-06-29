---
page_id: coding-little-go-book-maps
page_kind: concept
summary: Maps: 7 statement(s) and 8 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-29
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-maps@256c17886a13e0ecfa868a1283dada1c
---

# Maps

What [[coding-little-go-book]] covers about maps:

## Statements

### Chapter 3 - Maps, Arrays and Slices / Maps

- Maps in Go are what other languages call hashtables or dictionaries. They work as you expect: you define a key and value, and can get, set and delete values from it. _(coding_little_go_book.pdf (source-range-23d24eb1-00248))_

- Maps, like slices, are created with the make function. Let's look at an example: _(coding_little_go_book.pdf (source-range-23d24eb1-00249))_

- To get the number of keys, we use len . To remove a value based on its key, we use delete : _(coding_little_go_book.pdf (source-range-23d24eb1-00251))_

- There's yet another way to declare and initialize values in Go. Like make , this approach is specific to maps and arrays. We can declare as a composite literal: _(coding_little_go_book.pdf (source-range-23d24eb1-00260))_

- Iteration over maps isn't ordered. Each iteration over a lookup will return the key value pair in a random order. _(coding_little_go_book.pdf (source-range-23d24eb1-00264))_


## Technical atoms

### Technical frame 1: Chapter 3 - Maps, Arrays and Slices / Maps

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00251))_

> To get the number of keys, we use len . To remove a value based on its key, we use delete :

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00250))_

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

### Technical frame 2: Chapter 3 - Maps, Arrays and Slices / Maps

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00260))_

> There's yet another way to declare and initialize values in Go. Like make , this approach is specific to maps and arrays. We can declare as a composite literal:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00252))_

```
// returns 1
total := len(lookup)
// has no return, can be called on a non-existing key
delete(lookup, "goku")
```

### Technical frame 3: Chapter 3 - Maps, Arrays and Slices / Maps

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00260))_

> There's yet another way to declare and initialize values in Go. Like make , this approach is specific to maps and arrays. We can declare as a composite literal:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00254))_

```
lookup := make(map[string]int, 100)
```

### Technical frame 4: Chapter 3 - Maps, Arrays and Slices / Maps

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00260))_

> There's yet another way to declare and initialize values in Go. Like make , this approach is specific to maps and arrays. We can declare as a composite literal:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00255))_

> If you have some idea of how many keys your map will have, defining an initial size can help with performance.

### Technical frame 5: Chapter 3 - Maps, Arrays and Slices / Maps

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00260))_

> There's yet another way to declare and initialize values in Go. Like make , this approach is specific to maps and arrays. We can declare as a composite literal:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00257))_

```
type Saiyan struct {
  Name string
  Friends map[string]*Saiyan
}
```

### Technical frame 6: Chapter 3 - Maps, Arrays and Slices / Maps

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00260))_

> There's yet another way to declare and initialize values in Go. Like make , this approach is specific to maps and arrays. We can declare as a composite literal:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00259))_

```
goku := &Saiyan{
  Name: "Goku",
  Friends: make(map[string]*Saiyan),
}
goku.Friends["krillin"] = ... //todo load or create Krillin
```

### Technical frame 7: Chapter 3 - Maps, Arrays and Slices / Maps

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00264))_

> Iteration over maps isn't ordered. Each iteration over a lookup will return the key value pair in a random order.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00261))_

```
lookup := map[string]int{
  "goku": 9001,
  "gohan": 2044,
}
```

### Technical frame 8: Chapter 3 - Maps, Arrays and Slices / Maps

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00264))_

> Iteration over maps isn't ordered. Each iteration over a lookup will return the key value pair in a random order.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00263))_

```
for key, value := range lookup {
  ...
}
```


## Related pages

- [[coding-little-go-book-maps-array-and-slice]] - narrower topic: Maps, Arrays and Slices shares source evidence from Chapter 3 - Maps, Arrays and Slices / Maps: Maps in Go are what other languages call hashtables or dictionaries. They work as you expect: you define a key and value, and can get, set and delete values from it.; Maps, Arrays and Slices shares technical record from Chapter 3 - Maps, Arrays and Slices / Maps: func main() { lookup := make(map[string]int) lookup["goku"] = 9001 power, exists := lookup["vegeta"] // prints 0, false // 0 is the default value for an integer fmt. ... [truncated] (7 shared statement(s), 8 shared atom(s))
- [[coding-little-go-book-maps-array]] - narrower topic: Maps Array shares source evidence from Chapter 3 - Maps, Arrays and Slices / Maps: Maps in Go are what other languages call hashtables or dictionaries. They work as you expect: you define a key and value, and can get, set and delete values from it.; Maps Array shares technical record from Chapter 3 - Maps, Arrays and Slices / Maps: func main() { lookup := make(map[string]int) lookup["goku"] = 9001 power, exists := lookup["vegeta"] // prints 0, false // 0 is the default value for an integer fmt. ... [truncated] (4 shared statement(s), 4 shared atom(s))
- [[coding-little-go-book-section-chapter-3-maps-arrays-and-slices-maps-cf61ad17]] - source section: Chapter 3 - Maps, Arrays and Slices / Maps shares source evidence from Chapter 3 - Maps, Arrays and Slices / Maps: Maps in Go are what other languages call hashtables or dictionaries. They work as you expect: you define a key and value, and can get, set and delete values from it.; Chapter 3 - Maps, Arrays and Slices / Maps shares technical record from Chapter 3 - Maps, Arrays and Slices / Maps: func main() { lookup := make(map[string]int) lookup["goku"] = 9001 power, exists := lookup["vegeta"] // prints 0, false // 0 is the default value for an integer fmt. ... [truncated] (7 shared statement(s), 8 shared atom(s))

## Source

- [[coding-little-go-book]]
