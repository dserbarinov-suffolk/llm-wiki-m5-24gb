---
page_id: coding-little-go-book-copy
page_kind: concept
summary: Copy: 4 statement(s) and 8 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-copy@9ab707399d17eecf8021859d9e102d10
---

# Copy

What [[coding-little-go-book]] covers about copy:

## Statements

- Because Super made changes to a copy of our original goku value and thus, changes made in Super weren't reflected in the caller. _(coding_little_go_book.pdf (source-range-773b6275-00130))_
- That copy is the same address as the original, which is what that indirection buys us. _(coding_little_go_book.pdf (source-range-773b6275-00133))_
- Note that we're still passing a copy of goku's value to Super it just so happens that goku's value has become an address. _(coding_little_go_book.pdf (source-range-773b6275-00133))_
- copy is one of those functions that highlights how slices change the way we code. _(coding_little_go_book.pdf (source-range-773b6275-00244))_

## Technical atoms

> Context: Why do we want a pointer to the value, rather than the actual value? It comes down to the way Go passes arguments to a function: as copies. Knowing this, what does the following print? The answer is 9000, not 19000. Why? Because Super made changes to a copy of our original goku value and thus, changes made in Super weren't reflected in the caller. To make this work as you probably expect, we need to pass a pointer to our value:
_(context: coding_little_go_book.pdf (source-range-773b6275-00128, source-range-773b6275-00130))_

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
_(source: coding_little_go_book.pdf (source-range-773b6275-00129))_

> Context: The answer is 9000, not 19000. Why? Because Super made changes to a copy of our original goku value and thus, changes made in Super weren't reflected in the caller. To make this work as you probably expect, we need to pass a pointer to our value:
_(context: coding_little_go_book.pdf (source-range-773b6275-00130))_

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
_(source: coding_little_go_book.pdf (source-range-773b6275-00131))_

> Context: We can prove that it's a copy by trying to change where it points to (not something you'd likely want to actually do): The above, once again, prints 9000. This is how many languages behave, including Ruby, Python, Java and C#. Go, and to some degree C#, simply make the fact visible.
_(context: coding_little_go_book.pdf (source-range-773b6275-00134, source-range-773b6275-00136))_

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
_(source: coding_little_go_book.pdf (source-range-773b6275-00135))_

> Context: But that changes the intent of our original code. Appending to a slice of length 0 will set the first element. For whatever reason, our crashing code wanted to set the element at index 7. To do this, we can re-slice our slice: How large can we resize a slice? Up to its capacity which, in this case, is 10. You might be thinking this doesn't actually solve the fixed-length issue of arrays. It turns out that append is pretty special. If the underlying array is full, it will create a new larger array and copy the values over (this is exactly how dynamic arrays work in PHP , Python, Ruby, JavaScript, ...). This is why, in the example above that used append , we had to re-assign the value returned by append to our scores variable: append might have created a new value if the original had no more space.
_(context: coding_little_go_book.pdf (source-range-773b6275-00211, source-range-773b6275-00213))_

```
func main() {
  scores := make([]int, 0, 10)
  scores = scores[0:8]
  scores[7] = 9033
  fmt.Println(scores)
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00212))_

> Context: Even when you know the size, append can be used. It's largely a matter of preference: The answer is [1, 2, 3, 4, 5] . That's because slice is a completely new array with copies of values. Now, consider the Go equivalent:
_(context: coding_little_go_book.pdf (source-range-773b6275-00228, source-range-773b6275-00232))_

> You can also get a slice in Ruby by using [START..END] or in Python via [START:END] .
_(source: coding_little_go_book.pdf (source-range-773b6275-00230))_

> Context: Slices as wrappers to arrays is a powerful concept. Many languages have the concept of slicing an array. Both JavaScript and Ruby arrays have a slice method. You can also get a slice in Ruby by using [START..END] or in Python via [START:END] . However, in these languages, a slice is actually a new array with the values of the original copied over. If we take Ruby, what's the output of the following? The answer is [1, 2, 3, 4, 5] . That's because slice is a completely new array with copies of values. Now, consider the Go equivalent:
_(context: coding_little_go_book.pdf (source-range-773b6275-00230, source-range-773b6275-00232))_

```
scores = [1,2,3,4,5]
slice = scores[2..4]
slice[0] = 999
puts scores
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00231))_


## Source

- [[coding-little-go-book]]
