---
page_id: coding-little-go-book-section-chapter-3-maps-arrays-and-slices-slices-7f1a7b05
page_kind: source
summary: Chapter 3 - Maps, Arrays and Slices / Slices: 69 source-backed entries and 22 atom(s) from raw/coding_little_go_book.pdf.
page_family: section-reference
sources: raw/coding_little_go_book.pdf
updated: 2026-06-30
domain: coding-little-go-book
category_path: sources/coding-little-go-book/sections
source_id: coding_little_go_book.pdf
projection_coverage: section-coding-little-go-book-section-chapter-3-maps-arrays-and-slices-slices-7f1a7b05@9dce7aeb494bdcfcc984fd1a962cc755
---

# Chapter 3 - Maps, Arrays and Slices / Slices

From [[coding-little-go-book]].

## Related pages

- [[coding-little-go-book-section-chapter-3-maps-arrays-and-slices-4800f0d1]] - broader source section: Chapter 3 - Maps, Arrays and Slices
- [[coding-little-go-book-section-chapter-3-maps-arrays-and-slices-arrays-e5036a27]] - previous source section: Chapter 3 - Maps, Arrays and Slices / Arrays
- [[coding-little-go-book-section-chapter-3-maps-arrays-and-slices-maps-cf61ad17]] - next source section: Chapter 3 - Maps, Arrays and Slices / Maps
- [[coding-little-go-book-slice]] - topic hub: opens the topic page for Slice

## Statements

- In Go, you rarely, if ever, use arrays directly. Instead, you use slices. A slice is a lightweight structure that wraps and represents a portion of an array. There are a few ways to create a slice, and we'll go over when to use which later on. The first is a slight variation on how we created an array: _(coding_little_go_book.pdf (source-range-23d24eb1-00200))_
- Unlike the array declaration, our slice isn't declared with a length within the square brackets. To understand how the two are different, let's see another way to create a slice, using make : _(coding_little_go_book.pdf (source-range-23d24eb1-00202))_
- We use make instead of new because there's more to creating a slice than just allocating the memory (which is what new does). Specifically, we have to allocate the memory for the underlying array and also initialize the slice. In the above, we initialize a slice with a length of 10 and a capacity of 10. The length is the size of the slice, the capacity is the size of the underlying array. Using make we can specify the two separately: _(coding_little_go_book.pdf (source-range-23d24eb1-00204))_
- This creates a slice with a length of 0 but with a capacity of 10. (If you're paying attention, you'll note that make and len are overloaded. Go is a language that, to the frustration of some, makes use of features which aren't exposed for developers to use.) _(coding_little_go_book.pdf (source-range-23d24eb1-00206))_
- Our first example crashes. Why? Because our slice has a length of 0. Yes, the underlying array has 10 elements, but we need to explicitly expand our slice in order to access those elements. One way to expand a slice is via append : _(coding_little_go_book.pdf (source-range-23d24eb1-00209))_
- But that changes the intent of our original code. Appending to a slice of length 0 will set the first element. For whatever reason, our crashing code wanted to set the element at index 7. To do this, we can re-slice our slice: _(coding_little_go_book.pdf (source-range-23d24eb1-00211))_
- How large can we resize a slice? Up to its capacity which, in this case, is 10. You might be thinking this doesn't actually solve the fixed-length issue of arrays. It turns out that append is pretty special. If the underlying array is full, it will create a new larger array and copy the values over (this is exactly how dynamic arrays work in PHP , Python, Ruby, JavaScript, ...). This is why, in the example above that used append , we had to re-assign the value returned by append to our scores variable: append might have created a new value if the original had no more space. _(coding_little_go_book.pdf (source-range-23d24eb1-00213))_
- The initial capacity of scores is 5. In order to hold 25 values, it'll have to be expanded 3 times with a capacity of 10, 20 and finally 40. _(coding_little_go_book.pdf (source-range-23d24eb1-00217))_
- Here, the output is going to be [0, 0, 0, 0, 0, 9332] . Maybe you thought it would be [9332, 0, 0, 0, 0] ? To a human, that might seem logical. To a compiler, you're telling it to append a value to a slice that already holds 5 values. _(coding_little_go_book.pdf (source-range-23d24eb1-00220))_
- When do you use which? The first one shouldn't need much of an explanation. You use this when you know the values that you want in the array ahead of time. _(coding_little_go_book.pdf (source-range-23d24eb1-00223))_
- The second one is useful when you'll be writing into specific indexes of a slice. For example: _(coding_little_go_book.pdf (source-range-23d24eb1-00224))_
- The third version is a nil slice and is used in conjunction with append , when the number of elements is unknown. _(coding_little_go_book.pdf (source-range-23d24eb1-00226))_
- The last version lets us specify an initial capacity; useful if we have a general idea of how many elements we'll need. _(coding_little_go_book.pdf (source-range-23d24eb1-00227))_
- Slices as wrappers to arrays is a powerful concept. Many languages have the concept of slicing an array. Both JavaScript and Ruby arrays have a slice method. You can also get a slice in Ruby by using [START..END] or in Python via [START:END] . However, in these languages, a slice is actually a new array with the values of the original copied over. If we take Ruby, what's the output of the following? _(coding_little_go_book.pdf (source-range-23d24eb1-00230))_
- The [X:Y] syntax creates a slice of scores , starting from index 2 up until (but not including) index 4. However, unlike the Ruby example above, the Go code will produce an output of [1, 2, 999, 4, 5] . This is because our slice is really just a window into scores . _(coding_little_go_book.pdf (source-range-23d24eb1-00234))_
- We can see from the above example, that [X:] is shorthand for from X to the end while [:X] is shorthand for from the start up until X . Unlike other languages, Go doesn't support negative values. If we want all of the values of a slice except the last, we do: _(coding_little_go_book.pdf (source-range-23d24eb1-00239))_
- Finally, now that we know about slices, we can look at another commonly used built-in function: copy . copy is one of those functions that highlights how slices change the way we code. Normally, a method that copies values from one array to another has 5 parameters: source , sourceStart , count , destination and destinationStart . With slices, we only need two: _(coding_little_go_book.pdf (source-range-23d24eb1-00244))_
- Unlike the array declaration, our slice isn't declared with a length within the square brackets. _(coding_little_go_book.pdf (source-range-23d24eb1-00202))_
- We use make instead of new because there's more to creating a slice than just allocating the memory (which is what new does). _(coding_little_go_book.pdf (source-range-23d24eb1-00204))_
- Because our slice has a length of 0. _(coding_little_go_book.pdf (source-range-23d24eb1-00209))_
- However, unlike the Ruby example above, the Go code will produce an output of [1, 2, 999, 4, 5] . _(coding_little_go_book.pdf (source-range-23d24eb1-00234))_
- This is because our slice is really just a window into scores . _(coding_little_go_book.pdf (source-range-23d24eb1-00234))_
- Unlike other languages, Go doesn't support negative values. _(coding_little_go_book.pdf (source-range-23d24eb1-00239))_

## Technical atoms

### Technical frame 1: Chapter 3 - Maps, Arrays and Slices / Slices

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00202))_

> Unlike the array declaration, our slice isn't declared with a length within the square brackets. To understand how the two are different, let's see another way to create a slice, using make :

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00201))_

```
scores := []int{1,4,293,4,9}
```

### Technical frame 2: Chapter 3 - Maps, Arrays and Slices / Slices

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00204))_

> We use make instead of new because there's more to creating a slice than just allocating the memory (which is what new does). Specifically, we have to allocate the memory for the underlying array and also initialize the slice. In the above, we initialize a slice with a length of 10 and a capacity of 10. The length is the size of the slice, the capacity is the size of the underlying array. Using make we can specify the two separately:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00203))_

```
scores := make([]int, 10)
```

### Technical frame 3: Chapter 3 - Maps, Arrays and Slices / Slices

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00206))_

> This creates a slice with a length of 0 but with a capacity of 10. (If you're paying attention, you'll note that make and len are overloaded. Go is a language that, to the frustration of some, makes use of features which aren't exposed for developers to use.)

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00205))_

```
scores := make([]int, 0, 10)
```

### Technical frame 4: Chapter 3 - Maps, Arrays and Slices / Slices

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00209))_

> Our first example crashes. Why? Because our slice has a length of 0. Yes, the underlying array has 10 elements, but we need to explicitly expand our slice in order to access those elements. One way to expand a slice is via append :

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00208))_

```
func main() {
  scores := make([]int, 0, 10)
  scores[7] = 9033
  fmt.Println(scores)
}
```

### Technical frame 5: Chapter 3 - Maps, Arrays and Slices / Slices

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00211))_

> But that changes the intent of our original code. Appending to a slice of length 0 will set the first element. For whatever reason, our crashing code wanted to set the element at index 7. To do this, we can re-slice our slice:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00210))_

```
func main() {
  scores := make([]int, 0, 10)
  scores = append(scores, 5)
  fmt.Println(scores) // prints [5]
}
```

### Technical frame 6: Chapter 3 - Maps, Arrays and Slices / Slices

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

### Technical frame 7: Chapter 3 - Maps, Arrays and Slices / Slices

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00220))_

> Here, the output is going to be [0, 0, 0, 0, 0, 9332] . Maybe you thought it would be [9332, 0, 0, 0, 0] ? To a human, that might seem logical. To a compiler, you're telling it to append a value to a slice that already holds 5 values.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00219))_

```
func main() {
  scores := make([]int, 5)
  scores = append(scores, 9332)
  fmt.Println(scores)
}
```

### Technical frame 8: Chapter 3 - Maps, Arrays and Slices / Slices

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00223))_

> When do you use which? The first one shouldn't need much of an explanation. You use this when you know the values that you want in the array ahead of time.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00222))_

```
names := []string{"leto", "jessica", "paul"}
checks := make([]bool, 10)
var names []string
scores := make([]int, 0, 20)
```

### Technical frame 9: Chapter 3 - Maps, Arrays and Slices / Slices

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00226))_

> The third version is a nil slice and is used in conjunction with append , when the number of elements is unknown.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00225))_

```
func extractPowers(saiyans []*Saiyan) []int {
  powers := make([]int, len(saiyans))
  for index, saiyan := range saiyans {
    powers[index] = saiyan.Power
  }
  return powers
}
```

### Technical frame 10: Chapter 3 - Maps, Arrays and Slices / Slices

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00230))_

> Slices as wrappers to arrays is a powerful concept. Many languages have the concept of slicing an array. Both JavaScript and Ruby arrays have a slice method. You can also get a slice in Ruby by using [START..END] or in Python via [START:END] . However, in these languages, a slice is actually a new array with the values of the original copied over. If we take Ruby, what's the output of the following?

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00228))_

> Even when you know the size, append can be used.

### Technical frame 11: Chapter 3 - Maps, Arrays and Slices / Slices

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

### Technical frame 12: Chapter 3 - Maps, Arrays and Slices / Slices

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00234))_

> The [X:Y] syntax creates a slice of scores , starting from index 2 up until (but not including) index 4. However, unlike the Ruby example above, the Go code will produce an output of [1, 2, 999, 4, 5] . This is because our slice is really just a window into scores .

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00230))_

> You can also get a slice in Ruby by using [START..END] or in Python via [START:END] .

### Technical frame 13: Chapter 3 - Maps, Arrays and Slices / Slices

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00234))_

> The [X:Y] syntax creates a slice of scores , starting from index 2 up until (but not including) index 4. However, unlike the Ruby example above, the Go code will produce an output of [1, 2, 999, 4, 5] . This is because our slice is really just a window into scores .

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00231))_

```
scores = [1,2,3,4,5]
slice = scores[2..4]
slice[0] = 999
puts scores
```

### Technical frame 14: Chapter 3 - Maps, Arrays and Slices / Slices

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00234))_

> The [X:Y] syntax creates a slice of scores , starting from index 2 up until (but not including) index 4. However, unlike the Ruby example above, the Go code will produce an output of [1, 2, 999, 4, 5] . This is because our slice is really just a window into scores .

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00232))_

> The answer is [1, 2, 3, 4, 5] . That's because slice is a completely new array with copies of values. Now, consider the Go equivalent:

### Technical frame 15: Chapter 3 - Maps, Arrays and Slices / Slices

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00234))_

> The [X:Y] syntax creates a slice of scores , starting from index 2 up until (but not including) index 4. However, unlike the Ruby example above, the Go code will produce an output of [1, 2, 999, 4, 5] . This is because our slice is really just a window into scores .

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00233))_

```
scores := []int{1,2,3,4,5}
slice := scores[2:4]
slice[0] = 999
fmt.Println(scores)
```

### Technical frame 16: Chapter 3 - Maps, Arrays and Slices / Slices

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00239))_

> We can see from the above example, that [X:] is shorthand for from X to the end while [:X] is shorthand for from the start up until X . Unlike other languages, Go doesn't support negative values. If we want all of the values of a slice except the last, we do:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00235))_

> This changes how you code. For example, a number of functions take a position parameter. In JavaScript, if we want to find the first space in a string (yes, slices work on strings too!) after the first five characters, we'd write:

### Technical frame 17: Chapter 3 - Maps, Arrays and Slices / Slices

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00239))_

> We can see from the above example, that [X:] is shorthand for from X to the end while [:X] is shorthand for from the start up until X . Unlike other languages, Go doesn't support negative values. If we want all of the values of a slice except the last, we do:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00236))_

```
haystack = "the spice must flow";
console.log(haystack.indexOf(" ", 5));
```

### Technical frame 18: Chapter 3 - Maps, Arrays and Slices / Slices

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00239))_

> We can see from the above example, that [X:] is shorthand for from X to the end while [:X] is shorthand for from the start up until X . Unlike other languages, Go doesn't support negative values. If we want all of the values of a slice except the last, we do:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00238))_

```
strings.Index(haystack[5:], " ")
```

### Technical frame 19: Chapter 3 - Maps, Arrays and Slices / Slices

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00244))_

> Finally, now that we know about slices, we can look at another commonly used built-in function: copy . copy is one of those functions that highlights how slices change the way we code. Normally, a method that copies values from one array to another has 5 parameters: source , sourceStart , count , destination and destinationStart . With slices, we only need two:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00240))_

```
scores := []int{1, 2, 3, 4, 5}
scores = scores[:len(scores)-1]
```

### Technical frame 20: Chapter 3 - Maps, Arrays and Slices / Slices

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00244))_

> Finally, now that we know about slices, we can look at another commonly used built-in function: copy . copy is one of those functions that highlights how slices change the way we code. Normally, a method that copies values from one array to another has 5 parameters: source , sourceStart , count , destination and destinationStart . With slices, we only need two:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00242))_

```
func main() {
  scores := []int{1, 2, 3, 4, 5}
  scores = removeAtIndex(scores, 2)
  fmt.Println(scores) // [1 2 5 4]
}
```

### Technical frame 21: Chapter 3 - Maps, Arrays and Slices / Slices

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00244))_

> Finally, now that we know about slices, we can look at another commonly used built-in function: copy . copy is one of those functions that highlights how slices change the way we code. Normally, a method that copies values from one array to another has 5 parameters: source , sourceStart , count , destination and destinationStart . With slices, we only need two:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00243))_

```
// won't preserve order
func removeAtIndex(source []int, index int) []int {
  lastIndex := len(source) - 1
  //swap the last value and the value we want to remove
  source[index], source[lastIndex] = source[lastIndex], 
source[index]
return source[:lastIndex]
}
```

### Technical frame 22: Chapter 3 - Maps, Arrays and Slices / Slices

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
