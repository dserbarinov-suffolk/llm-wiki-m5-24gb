---
page_id: coding-little-go-book-ruby
page_kind: concept
summary: Ruby: 4 statement(s) and 6 atom(s) from raw/coding_little_go_book.pdf.
page_family: topic-concept
sources: raw/coding_little_go_book.pdf
updated: 2026-06-30
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-ruby@cfe8b7ac250be91bb28d97fb2a864f24
---

# Ruby

What [[coding-little-go-book]] covers about ruby:

## Statements

### Chapter 1 - The Basics / Garbage Collected

- Languages with garbage collectors (e.g., Ruby, Python, Java, JavaScript, C#, Go) are able to keep track of these and free them when they're no longer used. Garbage collection adds overhead, but it also eliminates a number of devastating bugs. _(coding_little_go_book.pdf (source-range-23d24eb1-00047))_

### Chapter 3 - Maps, Arrays and Slices / Arrays

- If you come from Python, Ruby, Perl, JavaScript or PHP (and more), you're probably used to programming with dynamic arrays . These are arrays that resize themselves as data is added to them. In Go, like many other languages, arrays are fixed. Declaring an array requires that we specify the size, and once the size is specified, it cannot grow: _(coding_little_go_book.pdf (source-range-23d24eb1-00191))_

### Chapter 3 - Maps, Arrays and Slices / Slices

- Slices as wrappers to arrays is a powerful concept. Many languages have the concept of slicing an array. Both JavaScript and Ruby arrays have a slice method. You can also get a slice in Ruby by using [START..END] or in Python via [START:END] . However, in these languages, a slice is actually a new array with the values of the original copied over. If we take Ruby, what's the output of the following? _(coding_little_go_book.pdf (source-range-23d24eb1-00230))_

- The [X:Y] syntax creates a slice of scores , starting from index 2 up until (but not including) index 4. However, unlike the Ruby example above, the Go code will produce an output of [1, 2, 999, 4, 5] . This is because our slice is really just a window into scores . _(coding_little_go_book.pdf (source-range-23d24eb1-00234))_


## Technical atoms

### Technical frame 1: Chapter 3 - Maps, Arrays and Slices / Arrays

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00193))_

> The above array can hold up to 10 scores using indexes scores[0] through scores[9] . Attempts to access an out of range index in the array will result in a compiler or runtime error.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00192))_

```
var scores [10]int
scores[0] = 339
```

### Technical frame 2: Chapter 3 - Maps, Arrays and Slices / Slices

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00213))_

> How large can we resize a slice? Up to its capacity which, in this case, is 10. You might be thinking this doesn't actually solve the fixed-length issue of arrays. It turns out that append is pretty special. If the underlying array is full, it will create a new larger array and copy the values over (this is exactly how dynamic arrays work in PHP , Python, Ruby, JavaScript, ...). This is why, in the example above that used append , we had to re-assign the value returned by append to our scores va

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00212))_

```
func main() {
  scores := make([]int, 0, 10)
  scores = scores[0:8]
  scores[7] = 9033
  fmt.Println(scores)
}
```

### Technical frame 3: Chapter 3 - Maps, Arrays and Slices / Slices

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00230))_

> Slices as wrappers to arrays is a powerful concept. Many languages have the concept of slicing an array. Both JavaScript and Ruby arrays have a slice method. You can also get a slice in Ruby by using [START..END] or in Python via [START:END] . However, in these languages, a slice is actually a new array with the values of the original copied over. If we take Ruby, what's the output of the following?

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00228))_

> Even when you know the size, append can be used.

### Technical frame 4: Chapter 3 - Maps, Arrays and Slices / Slices

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00230))_

> Slices as wrappers to arrays is a powerful concept. Many languages have the concept of slicing an array. Both JavaScript and Ruby arrays have a slice method. You can also get a slice in Ruby by using [START..END] or in Python via [START:END] . However, in these languages, a slice is actually a new array with the values of the original copied over. If we take Ruby, what's the output of the following?

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00229))_

```
func extractPowers(saiyans []*Saiyan) []int {
  powers := make([]int, 0, len(saiyans))
  for _, saiyan := range saiyans {
    powers = append(powers, saiyan.Power)
  }
  return powers
}
```

### Technical frame 5: Chapter 3 - Maps, Arrays and Slices / Slices

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00234))_

> The [X:Y] syntax creates a slice of scores , starting from index 2 up until (but not including) index 4. However, unlike the Ruby example above, the Go code will produce an output of [1, 2, 999, 4, 5] . This is because our slice is really just a window into scores .

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00231))_

```
scores = [1,2,3,4,5]
slice = scores[2..4]
slice[0] = 999
puts scores
```

### Technical frame 6: Chapter 3 - Maps, Arrays and Slices / Slices

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00234))_

> The [X:Y] syntax creates a slice of scores , starting from index 2 up until (but not including) index 4. However, unlike the Ruby example above, the Go code will produce an output of [1, 2, 999, 4, 5] . This is because our slice is really just a window into scores .

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00233))_

```
scores := []int{1,2,3,4,5}
slice := scores[2:4]
slice[0] = 999
fmt.Println(scores)
```


## Related pages

- [[coding-little-go-book-array]] - shared statements and technical atoms: Array shares source evidence from Chapter 3 - Maps, Arrays and Slices / Slices: Slices as wrappers to arrays is a powerful concept. Many languages have the concept of slicing an array. Both JavaScript and Ruby arrays have a slice method. You can ... [truncated]; Array shares technical record from Chapter 3 - Maps, Arrays and Slices / Arrays: var scores [10]int scores[0] = 339 (1 shared statement(s), 6 shared atom(s))
- [[coding-little-go-book-slice]] - shared statements and technical atoms: Slice shares source evidence from Chapter 3 - Maps, Arrays and Slices / Slices: Slices as wrappers to arrays is a powerful concept. Many languages have the concept of slicing an array. Both JavaScript and Ruby arrays have a slice method. You can ... [truncated]; Slice shares technical record from Chapter 3 - Maps, Arrays and Slices / Slices: func main() { scores := make([]int, 0, 10) scores = scores[0:8] scores[7] = 9033 fmt.Println(scores) } (1 shared statement(s), 5 shared atom(s))
- [[coding-little-go-book-language]] - shared statements and technical atoms: Language shares source evidence from Chapter 1 - The Basics / Garbage Collected: Languages with garbage collectors (e.g., Ruby, Python, Java, JavaScript, C#, Go) are able to keep track of these and free them when they're no longer used. Garbage c ... [truncated]; Language shares technical record from Chapter 3 - Maps, Arrays and Slices / Arrays: var scores [10]int scores[0] = 339 (1 shared statement(s), 4 shared atom(s))
- [[coding-little-go-book-code]] - shared statements and technical atoms: Code shares source evidence from Chapter 3 - Maps, Arrays and Slices / Slices: The [X:Y] syntax creates a slice of scores , starting from index 2 up until (but not including) index 4. However, unlike the Ruby example above, the Go code will pro ... [truncated]; Code shares technical record from Chapter 3 - Maps, Arrays and Slices / Slices: func main() { scores := make([]int, 0, 10) scores = scores[0:8] scores[7] = 9033 fmt.Println(scores) } (1 shared statement(s), 2 shared atom(s))
- [[coding-little-go-book-value]] - shared technical atoms: Value shares technical record from Chapter 3 - Maps, Arrays and Slices / Slices: func main() { scores := make([]int, 0, 10) scores = scores[0:8] scores[7] = 9033 fmt.Println(scores) } (5 shared atom(s))
- [[coding-little-go-book-copy]] - shared technical atoms: Copy shares technical record from Chapter 3 - Maps, Arrays and Slices / Slices: func main() { scores := make([]int, 0, 10) scores = scores[0:8] scores[7] = 9033 fmt.Println(scores) } (3 shared atom(s))
- [[coding-little-go-book-reason]] - shared technical atoms: Reason shares technical record from Chapter 3 - Maps, Arrays and Slices / Slices: func main() { scores := make([]int, 0, 10) scores = scores[0:8] scores[7] = 9033 fmt.Println(scores) } (1 shared atom(s))
- [[coding-little-go-book-version]] - shared technical atoms: Version shares technical record from Chapter 3 - Maps, Arrays and Slices / Slices: Even when you know the size, append can be used. (1 shared atom(s))
- [[coding-little-go-book-garbage]] - shared statements: Garbage shares source evidence from Chapter 1 - The Basics / Garbage Collected: Languages with garbage collectors (e.g., Ruby, Python, Java, JavaScript, C#, Go) are able to keep track of these and free them when they're no longer used. Garbage c ... [truncated] (1 shared statement(s))

## Source

- [[coding-little-go-book]]
