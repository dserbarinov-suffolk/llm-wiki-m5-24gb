---
page_id: coding-little-go-book-ruby
page_kind: concept
summary: Ruby: 4 statement(s) and 6 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-ruby@0583c156d37f395796cbecb869d4b69f
---

# Ruby

What [[coding-little-go-book]] covers about ruby:

## Statements

- Languages with garbage collectors (e.g., Ruby, Python, Java, JavaScript, C#, Go) are able to keep track of these and free them when they're no longer used. _(coding_little_go_book.pdf (source-range-773b6275-00047))_
- If you come from Python, Ruby, Perl, JavaScript or PHP (and more), you're probably used to programming with dynamic arrays . _(coding_little_go_book.pdf (source-range-773b6275-00191))_
- Both JavaScript and Ruby arrays have a slice method. _(coding_little_go_book.pdf (source-range-773b6275-00230))_
- However, unlike the Ruby example above, the Go code will produce an output of [1, 2, 999, 4, 5] . _(coding_little_go_book.pdf (source-range-773b6275-00234))_

## Technical atoms

> Context: If you come from Python, Ruby, Perl, JavaScript or PHP (and more), you're probably used to programming with dynamic arrays . These are arrays that resize themselves as data is added to them. In Go, like many other languages, arrays are fixed. Declaring an array requires that we specify the size, and once the size is specified, it cannot grow: The above array can hold up to 10 scores using indexes scores[0] through scores[9] . Attempts to access an out of range index in the array will result in a compiler or runtime error.
_(context: coding_little_go_book.pdf (source-range-773b6275-00191, source-range-773b6275-00193))_

```
var scores [10]int
scores[0] = 339
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00192))_

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

> Context: The last version lets us specify an initial capacity; useful if we have a general idea of how many elements we'll need. Slices as wrappers to arrays is a powerful concept. Many languages have the concept of slicing an array. Both JavaScript and Ruby arrays have a slice method. You can also get a slice in Ruby by using [START..END] or in Python via [START:END] . However, in these languages, a slice is actually a new array with the values of the original copied over. If we take Ruby, what's the output of the following?
_(context: coding_little_go_book.pdf (source-range-773b6275-00227, source-range-773b6275-00230))_

> Even when you know the size, append can be used.
_(source: coding_little_go_book.pdf (source-range-773b6275-00228))_

> Context: Even when you know the size, append can be used. It's largely a matter of preference: Slices as wrappers to arrays is a powerful concept. Many languages have the concept of slicing an array. Both JavaScript and Ruby arrays have a slice method. You can also get a slice in Ruby by using [START..END] or in Python via [START:END] . However, in these languages, a slice is actually a new array with the values of the original copied over. If we take Ruby, what's the output of the following?
_(context: coding_little_go_book.pdf (source-range-773b6275-00228, source-range-773b6275-00230))_

```
func extractPowers(saiyans []*Saiyan) []int {
  powers := make([]int, 0, len(saiyans))
  for _, saiyan := range saiyans {
    powers = append(powers, saiyan.Power)
  }
  return powers
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00229))_

> Context: Slices as wrappers to arrays is a powerful concept. Many languages have the concept of slicing an array. Both JavaScript and Ruby arrays have a slice method. You can also get a slice in Ruby by using [START..END] or in Python via [START:END] . However, in these languages, a slice is actually a new array with the values of the original copied over. If we take Ruby, what's the output of the following? The answer is [1, 2, 3, 4, 5] . That's because slice is a completely new array with copies of values. Now, consider the Go equivalent:
_(context: coding_little_go_book.pdf (source-range-773b6275-00230, source-range-773b6275-00232))_

```
scores = [1,2,3,4,5]
slice = scores[2..4]
slice[0] = 999
puts scores
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00231))_

> Context: The answer is [1, 2, 3, 4, 5] . That's because slice is a completely new array with copies of values. Now, consider the Go equivalent: The [X:Y] syntax creates a slice of scores , starting from index 2 up until (but not including) index 4. However, unlike the Ruby example above, the Go code will produce an output of [1, 2, 999, 4, 5] . This is because our slice is really just a window into scores .
_(context: coding_little_go_book.pdf (source-range-773b6275-00232, source-range-773b6275-00234))_

```
scores := []int{1,2,3,4,5}
slice := scores[2:4]
slice[0] = 999
fmt.Println(scores)
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00233))_


## Source

- [[coding-little-go-book]]
