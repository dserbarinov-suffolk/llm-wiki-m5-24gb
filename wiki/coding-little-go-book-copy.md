---
page_id: coding-little-go-book-copy
page_kind: concept
summary: Copy: 5 statement(s) and 8 atom(s) from raw/coding_little_go_book.pdf.
page_family: topic-concept
sources: raw/coding_little_go_book.pdf
updated: 2026-06-30
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-copy@d38d12f41a2fb107d07738ec6d0a1e66
---

# Copy

What [[coding-little-go-book]] covers about copy:

## Statements

### Chapter 2 - Structures / Declarations and Initializations

- The answer is 9000, not 19000. Why? Because Super made changes to a copy of our original goku value and thus, changes made in Super weren't reflected in the caller. To make this work as you probably expect, we need to pass a pointer to our value: _(coding_little_go_book.pdf (source-range-23d24eb1-00130))_

- Note that we're still passing a copy of goku's value to Super it just so happens that goku's value has become an address. That copy is the same address as the original, which is what that indirection buys us. Think of it as copying the directions to a restaurant. What you have is a copy, but it still points to the same restaurant as the original. _(coding_little_go_book.pdf (source-range-23d24eb1-00133))_

### Chapter 3 - Maps, Arrays and Slices / Slices

- Finally, now that we know about slices, we can look at another commonly used built-in function: copy . copy is one of those functions that highlights how slices change the way we code. Normally, a method that copies values from one array to another has 5 parameters: source , sourceStart , count , destination and destinationStart . With slices, we only need two: _(coding_little_go_book.pdf (source-range-23d24eb1-00244))_


## Technical atoms

### Technical frame 1: Chapter 2 - Structures / Declarations and Initializations

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00130))_

> The answer is 9000, not 19000. Why? Because Super made changes to a copy of our original goku value and thus, changes made in Super weren't reflected in the caller. To make this work as you probably expect, we need to pass a pointer to our value:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00129))_

```
func main() {
  goku := Saiyan{"Goku", 9000}
  Super(goku)
  fmt.Println(goku.Power)
}
func Super(s Saiyan) {
  s.Power += 10000
}
```

### Technical frame 2: Chapter 2 - Structures / Declarations and Initializations

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00132))_

> We made two changes. The first is the use of the & operator to get the address of our value (it's called the address of operator). Next, we changed the type of parameter Super expects. It used to expect a value of type Saiyan but now expects an address of type *Saiyan , where *X means pointer to value of type X . There's obviously some relation between the types Saiyan and *Saiyan , but they are two distinct types.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00131))_

```
func main() {
  goku := &Saiyan{"Goku", 9000}
  Super(goku)
  fmt.Println(goku.Power)
}
func Super(s *Saiyan) {
  s.Power += 10000
}
```

### Technical frame 3: Chapter 2 - Structures / Declarations and Initializations

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00136))_

> The above, once again, prints 9000. This is how many languages behave, including Ruby, Python, Java and C#. Go, and to some degree C#, simply make the fact visible.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00135))_

```
func main() {
  goku := &Saiyan{"Goku", 9000}
  Super(goku)
  fmt.Println(goku.Power)
}
func Super(s *Saiyan) {
  s = &Saiyan{"Gohan", 1000}
}
```

### Technical frame 4: Chapter 3 - Maps, Arrays and Slices / Slices

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

### Technical frame 5: Chapter 3 - Maps, Arrays and Slices / Slices

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00234))_

> The [X:Y] syntax creates a slice of scores , starting from index 2 up until (but not including) index 4. However, unlike the Ruby example above, the Go code will produce an output of [1, 2, 999, 4, 5] . This is because our slice is really just a window into scores .

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00230))_

> You can also get a slice in Ruby by using [START..END] or in Python via [START:END] .

### Technical frame 6: Chapter 3 - Maps, Arrays and Slices / Slices

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00234))_

> The [X:Y] syntax creates a slice of scores , starting from index 2 up until (but not including) index 4. However, unlike the Ruby example above, the Go code will produce an output of [1, 2, 999, 4, 5] . This is because our slice is really just a window into scores .

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00231))_

```
scores = [1,2,3,4,5]
slice = scores[2..4]
slice[0] = 999
puts scores
```

### Technical frame 7: Chapter 3 - Maps, Arrays and Slices / Slices

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00234))_

> The [X:Y] syntax creates a slice of scores , starting from index 2 up until (but not including) index 4. However, unlike the Ruby example above, the Go code will produce an output of [1, 2, 999, 4, 5] . This is because our slice is really just a window into scores .

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00233))_

```
scores := []int{1,2,3,4,5}
slice := scores[2:4]
slice[0] = 999
fmt.Println(scores)
```

### Technical frame 8: Chapter 3 - Maps, Arrays and Slices / Slices

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00244))_

> Finally, now that we know about slices, we can look at another commonly used built-in function: copy . copy is one of those functions that highlights how slices change the way we code. Normally, a method that copies values from one array to another has 5 parameters: source , sourceStart , count , destination and destinationStart . With slices, we only need two:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00245))_

```
import (
  "fmt"
  "math/rand"
  "sort"
)
func main() {
  scores := make([]int, 100)
  for i := 0; i < 100; i++ {
    scores[i] = int(rand.Int31n(1000))
  }
  sort.Ints(scores)
worst := make([]int, 5)
  copy(worst, scores[:5])
  fmt.Println(worst)
}
```


## Related pages

- [[coding-little-go-book-value]] - shared statements and technical atoms: Value shares source evidence from Chapter 2 - Structures / Declarations and Initializations: The answer is 9000, not 19000. Why? Because Super made changes to a copy of our original goku value and thus, changes made in Super weren't reflected in the caller. ... [truncated]; Value shares technical record from Chapter 2 - Structures / Declarations and Initializations: func main() { goku := Saiyan{"Goku", 9000} Super(goku) fmt.Println(goku.Power) } func Super(s Saiyan) { s.Power += 10000 } (3 shared statement(s), 7 shared atom(s))
- [[coding-little-go-book-array]] - shared statements and technical atoms: Array shares source evidence from Chapter 3 - Maps, Arrays and Slices / Slices: Finally, now that we know about slices, we can look at another commonly used built-in function: copy . copy is one of those functions that highlights how slices chan ... [truncated]; Array shares technical record from Chapter 3 - Maps, Arrays and Slices / Slices: func main() { scores := make([]int, 0, 10) scores = scores[0:8] scores[7] = 9033 fmt.Println(scores) } (1 shared statement(s), 5 shared atom(s))
- [[coding-little-go-book-slice]] - shared statements and technical atoms: Slice shares source evidence from Chapter 3 - Maps, Arrays and Slices / Slices: Finally, now that we know about slices, we can look at another commonly used built-in function: copy . copy is one of those functions that highlights how slices chan ... [truncated]; Slice shares technical record from Chapter 3 - Maps, Arrays and Slices / Slices: func main() { scores := make([]int, 0, 10) scores = scores[0:8] scores[7] = 9033 fmt.Println(scores) } (1 shared statement(s), 5 shared atom(s))
- [[coding-little-go-book-change]] - shared statements and technical atoms: Change shares source evidence from Chapter 2 - Structures / Declarations and Initializations: The answer is 9000, not 19000. Why? Because Super made changes to a copy of our original goku value and thus, changes made in Super weren't reflected in the caller. ... [truncated]; Change shares technical record from Chapter 2 - Structures / Declarations and Initializations: func main() { goku := Saiyan{"Goku", 9000} Super(goku) fmt.Println(goku.Power) } func Super(s Saiyan) { s.Power += 10000 } (1 shared statement(s), 3 shared atom(s))
- [[coding-little-go-book-code]] - shared technical atoms: Code shares technical record from Chapter 3 - Maps, Arrays and Slices / Slices: func main() { scores := make([]int, 0, 10) scores = scores[0:8] scores[7] = 9033 fmt.Println(scores) } (3 shared atom(s))
- [[coding-little-go-book-ruby]] - shared technical atoms: Ruby shares technical record from Chapter 3 - Maps, Arrays and Slices / Slices: func main() { scores := make([]int, 0, 10) scores = scores[0:8] scores[7] = 9033 fmt.Println(scores) } (3 shared atom(s))
- [[coding-little-go-book-language]] - shared technical atoms: Language shares technical record from Chapter 3 - Maps, Arrays and Slices / Slices: scores = [1,2,3,4,5] slice = scores[2..4] slice[0] = 999 puts scores (1 shared atom(s))
- [[coding-little-go-book-reason]] - shared technical atoms: Reason shares technical record from Chapter 3 - Maps, Arrays and Slices / Slices: func main() { scores := make([]int, 0, 10) scores = scores[0:8] scores[7] = 9033 fmt.Println(scores) } (1 shared atom(s))
- [[coding-little-go-book-note]] - shared statements: Note shares source evidence from Chapter 2 - Structures / Declarations and Initializations: Note that we're still passing a copy of goku's value to Super it just so happens that goku's value has become an address. That copy is the same address as the origin ... [truncated] (1 shared statement(s))

## Source

- [[coding-little-go-book]]
