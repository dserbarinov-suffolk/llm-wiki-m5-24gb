---
page_id: coding-little-go-book-value
page_kind: concept
summary: Value: 9 statement(s) and 22 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-value@45f1ae8943cf82ca31790a20a2412f4a
---

# Value

What [[coding-little-go-book]] covers about value:

## Statements

- The real value of pointers though is that they let you share values. _(coding_little_go_book.pdf (source-range-773b6275-00137))_
- To a compiler, you're telling it to append a value to a slice that already holds 5 values. _(coding_little_go_book.pdf (source-range-773b6275-00220))_
- Because Super made changes to a copy of our original goku value and thus, changes made in Super weren't reflected in the caller. _(coding_little_go_book.pdf (source-range-773b6275-00130))_
- Note that we're still passing a copy of goku's value to Super it just so happens that goku's value has become an address. _(coding_little_go_book.pdf (source-range-773b6275-00133))_
- As we already saw, passing values is a great way to make data immutable (changes that a function makes to it won't be reflected in the calling code). _(coding_little_go_book.pdf (source-range-773b6275-00181))_
- Normally, a method that copies values from one array to another has 5 parameters: source , sourceStart , count , destination and destinationStart . _(coding_little_go_book.pdf (source-range-773b6275-00244))_
- Interestingly, while the values aren't available outside the ifstatement, they are available inside any else if or else . _(coding_little_go_book.pdf (source-range-773b6275-00366))_
- Converting values back and forth is ugly and dangerous but sometimes, in a static language, it's the only choice. _(coding_little_go_book.pdf (source-range-773b6275-00376))_
- In the above example, we simply discard the value that was sent to the channel. _(coding_little_go_book.pdf (source-range-773b6275-00457))_

## Technical atoms

> Context: The simplest way to create a value of our structure is: Note: The trailing , in the above structure is required. Without it, the compiler will give an error. You'll appreciate the required consistency, especially if you've used a language or format that enforces the opposite.
_(context: coding_little_go_book.pdf (source-range-773b6275-00118, source-range-773b6275-00120))_

```
goku := Saiyan{
  Name: "Goku",
  Power: 9000,
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00119))_

> Context: The simplest way to create a value of our structure is:
_(context: coding_little_go_book.pdf (source-range-773b6275-00118))_

> You'll appreciate the required consistency, especially if you've used a language or format that enforces the opposite.
_(source: coding_little_go_book.pdf (source-range-773b6275-00120))_

> Context: Furthermore, you can skip the field name and rely on the order of the field declarations (though for the sake of clarity, you should only do this for structures with few fields): What all of the above examples do is declare a variable goku and assign a value to it.
_(context: coding_little_go_book.pdf (source-range-773b6275-00124, source-range-773b6275-00126))_

```
goku := Saiyan{"Goku", 9000}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00125))_

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
