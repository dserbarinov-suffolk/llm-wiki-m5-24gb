---
page_id: coding-little-go-book-slice
page_kind: concept
summary: Slices: 39 statement(s) and 20 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-slice@21bfbac5202151c2bf420a586ce5fae3
---

# Slices

What [[coding-little-go-book]] covers about slices:

## Statements

- A slice is a lightweight structure that wraps and represents a portion of an array. _(coding_little_go_book.pdf (source-range-773b6275-00200))_
- Unlike the array declaration, our slice isn't declared with a length within the square brackets. _(coding_little_go_book.pdf (source-range-773b6275-00202))_
- Because our slice has a length of 0. _(coding_little_go_book.pdf (source-range-773b6275-00209))_
- Appending to a slice of length 0 will set the first element. _(coding_little_go_book.pdf (source-range-773b6275-00211))_
- To a compiler, you're telling it to append a value to a slice that already holds 5 values. _(coding_little_go_book.pdf (source-range-773b6275-00220))_
- Slices as wrappers to arrays is a powerful concept. _(coding_little_go_book.pdf (source-range-773b6275-00230))_
- However, in these languages, a slice is actually a new array with the values of the original copied over. _(coding_little_go_book.pdf (source-range-773b6275-00230))_
- Finally, now that we know about slices, we can look at another commonly used built-in function: copy . _(coding_little_go_book.pdf (source-range-773b6275-00244))_
- Instead, you use slices. _(coding_little_go_book.pdf (source-range-773b6275-00200))_
- There are a few ways to create a slice, and we'll go over when to use which later on. _(coding_little_go_book.pdf (source-range-773b6275-00200))_
- Specifically, we have to allocate the memory for the underlying array and also initialize the slice. _(coding_little_go_book.pdf (source-range-773b6275-00204))_
- The length is the size of the slice, the capacity is the size of the underlying array. _(coding_little_go_book.pdf (source-range-773b6275-00204))_
- We use make instead of new because there's more to creating a slice than just allocating the memory (which is what new does). _(coding_little_go_book.pdf (source-range-773b6275-00204))_
- Yes, the underlying array has 10 elements, but we need to explicitly expand our slice in order to access those elements. _(coding_little_go_book.pdf (source-range-773b6275-00209))_

## Technical atoms

> Context: In Go, you rarely, if ever, use arrays directly. Instead, you use slices. A slice is a lightweight structure that wraps and represents a portion of an array. There are a few ways to create a slice, and we'll go over when to use which later on. The first is a slight variation on how we created an array:
_(context: coding_little_go_book.pdf (source-range-773b6275-00200))_

```
scores := []int{1,4,293,4,9}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00201))_

> Context: Unlike the array declaration, our slice isn't declared with a length within the square brackets. To understand how the two are different, let's see another way to create a slice, using make : We use make instead of new because there's more to creating a slice than just allocating the memory (which is what new does). Specifically, we have to allocate the memory for the underlying array and also initialize the slice. In the above, we initialize a slice with a length of 10 and a capacity of 10. The length is the size of the slice, the capacity is the size of the underlying array. Using make we can specify the two separately:
_(context: coding_little_go_book.pdf (source-range-773b6275-00202, source-range-773b6275-00204))_

```
scores := make([]int, 10)
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00203))_

> Context: We use make instead of new because there's more to creating a slice than just allocating the memory (which is what new does). Specifically, we have to allocate the memory for the underlying array and also initialize the slice. In the above, we initialize a slice with a length of 10 and a capacity of 10. The length is the size of the slice, the capacity is the size of the underlying array. Using make we can specify the two separately:
_(context: coding_little_go_book.pdf (source-range-773b6275-00204))_

```
scores := make([]int, 0, 10)
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00205))_

> Context: To better understand the interplay between length and capacity, let's look at some examples: Our first example crashes. Why? Because our slice has a length of 0. Yes, the underlying array has 10 elements, but we need to explicitly expand our slice in order to access those elements. One way to expand a slice is via append :
_(context: coding_little_go_book.pdf (source-range-773b6275-00207, source-range-773b6275-00209))_

```
func main() {
  scores := make([]int, 0, 10)
  scores[7] = 9033
  fmt.Println(scores)
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00208))_

> Context: Our first example crashes. Why? Because our slice has a length of 0. Yes, the underlying array has 10 elements, but we need to explicitly expand our slice in order to access those elements. One way to expand a slice is via append :
_(context: coding_little_go_book.pdf (source-range-773b6275-00209))_

```
func main() {
  scores := make([]int, 0, 10)
  scores = append(scores, 5)
  fmt.Println(scores) // prints [5]
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00210))_

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


## Source

- [[coding-little-go-book]]
