---
page_id: coding-little-go-book-maps-array-and-slice
page_kind: concept
summary: Maps, Arrays and Slices: 64 statement(s) and 34 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-29
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-maps-array-and-slice@b6275148d5a41ddd6a2b9340ee26d631
---

# Maps, Arrays and Slices

What [[coding-little-go-book]] covers about maps, arrays and slices:

## Statements

### Chapter 3 - Maps, Arrays and Slices / Arrays

- If you come from Python, Ruby, Perl, JavaScript or PHP (and more), you're probably used to programming with dynamic arrays . These are arrays that resize themselves as data is added to them. In Go, like many other languages, arrays are fixed. Declaring an array requires that we specify the size, and once the size is specified, it cannot grow: _(coding_little_go_book.pdf (source-range-23d24eb1-00191))_

- The above array can hold up to 10 scores using indexes scores[0] through scores[9] . Attempts to access an out of range index in the array will result in a compiler or runtime error. _(coding_little_go_book.pdf (source-range-23d24eb1-00193))_

- We can use len to get the length of the array. range can be used to iterate over it: _(coding_little_go_book.pdf (source-range-23d24eb1-00196))_

- Arrays are efficient but rigid. We often don't know the number of elements we'll be dealing with upfront. For this, we turn to slices. _(coding_little_go_book.pdf (source-range-23d24eb1-00198))_

### Chapter 3 - Maps, Arrays and Slices / Slices

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

### Chapter 3 - Maps, Arrays and Slices / Maps

- Maps in Go are what other languages call hashtables or dictionaries. They work as you expect: you define a key and value, and can get, set and delete values from it. _(coding_little_go_book.pdf (source-range-23d24eb1-00248))_

- Maps, like slices, are created with the make function. Let's look at an example: _(coding_little_go_book.pdf (source-range-23d24eb1-00249))_

- To get the number of keys, we use len . To remove a value based on its key, we use delete : _(coding_little_go_book.pdf (source-range-23d24eb1-00251))_

- There's yet another way to declare and initialize values in Go. Like make , this approach is specific to maps and arrays. We can declare as a composite literal: _(coding_little_go_book.pdf (source-range-23d24eb1-00260))_

- Iteration over maps isn't ordered. Each iteration over a lookup will return the key value pair in a random order. _(coding_little_go_book.pdf (source-range-23d24eb1-00264))_

### Chapter 3 - Maps, Arrays and Slices / Pointers versus Values

- We finished Chapter 2 by looking at whether you should assign and pass pointers or values. We'll now have this same conversation with respect to array and map values. Which of these should you use? _(coding_little_go_book.pdf (source-range-23d24eb1-00266))_

- Many developers think that passing b to, or returning it from, a function is going to be more efficient. However, what's being passed/returned is a copy of the slice, which itself is a reference. So with respect to passing/returning the slice itself, there's no difference. Where you will see a difference is when you modify the values of a slice or map. At this point, the same logic that we saw in Chapter 2 applies. So the decision on whether to define an array of pointers versus an array of values comes down to how you use the individual values, not how you use the array or map itself. _(coding_little_go_book.pdf (source-range-23d24eb1-00268))_

### Chapter 3 - Maps, Arrays and Slices / Before You Continue

- Arrays and maps in Go work much like they do in other languages. If you're used to dynamic arrays, there might be a small adjustment, but append should solve most of your discomfort. If we peek beyond the superficial syntax of arrays, we find slices. Slices are powerful and they have a surprisingly large impact on the clarity of your code. There are edge cases that we haven't covered, but you're not likely to run into them. And, if you do, hopefully the foundation we've built here will let you understand what's going on. _(coding_little_go_book.pdf (source-range-23d24eb1-00270))_


## Technical atoms

### Technical frame 1: Chapter 3 - Maps, Arrays and Slices / Arrays

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00193))_

> The above array can hold up to 10 scores using indexes scores[0] through scores[9] . Attempts to access an out of range index in the array will result in a compiler or runtime error.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00192))_

```
var scores [10]int
scores[0] = 339
```

### Technical frame 2: Chapter 3 - Maps, Arrays and Slices / Arrays

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00196))_

> We can use len to get the length of the array. range can be used to iterate over it:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00195))_

```
scores := [4]int{9001, 9333, 212, 33}
```

### Technical frame 3: Chapter 3 - Maps, Arrays and Slices / Arrays

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00198))_

> Arrays are efficient but rigid. We often don't know the number of elements we'll be dealing with upfront. For this, we turn to slices.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00197))_

```
for index, value := range scores {
}
```

### Technical frame 4: Chapter 3 - Maps, Arrays and Slices / Slices

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00202))_

> Unlike the array declaration, our slice isn't declared with a length within the square brackets. To understand how the two are different, let's see another way to create a slice, using make :

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00201))_

```
scores := []int{1,4,293,4,9}
```

### Technical frame 5: Chapter 3 - Maps, Arrays and Slices / Slices

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00204))_

> We use make instead of new because there's more to creating a slice than just allocating the memory (which is what new does). Specifically, we have to allocate the memory for the underlying array and also initialize the slice. In the above, we initialize a slice with a length of 10 and a capacity of 10. The length is the size of the slice, the capacity is the size of the underlying array. Using make we can specify the two separately:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00203))_

```
scores := make([]int, 10)
```

### Technical frame 6: Chapter 3 - Maps, Arrays and Slices / Slices

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00206))_

> This creates a slice with a length of 0 but with a capacity of 10. (If you're paying attention, you'll note that make and len are overloaded. Go is a language that, to the frustration of some, makes use of features which aren't exposed for developers to use.)

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00205))_

```
scores := make([]int, 0, 10)
```

### Technical frame 7: Chapter 3 - Maps, Arrays and Slices / Slices

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

### Technical frame 8: Chapter 3 - Maps, Arrays and Slices / Slices

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

### Technical frame 9: Chapter 3 - Maps, Arrays and Slices / Slices

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

### Technical frame 10: Chapter 3 - Maps, Arrays and Slices / Slices

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00217))_

> The initial capacity of scores is 5. In order to hold 25 values, it'll have to be expanded 3 times with a capacity of 10, 20 and finally 40.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00215))_

```
func main() {
  scores := make([]int, 0, 5)
```

### Technical frame 11: Chapter 3 - Maps, Arrays and Slices / Slices

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00217))_

> The initial capacity of scores is 5. In order to hold 25 values, it'll have to be expanded 3 times with a capacity of 10, 20 and finally 40.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00216))_

```
c := cap(scores)
  fmt.Println(c)
for i := 0; i < 25; i++ {
    scores = append(scores, i)
// if our capacity has changed,
    // Go had to grow our array to accommodate the new data
    if cap(scores) != c {
      c = cap(scores)
      fmt.Println(c)
    }
  }
}
```

### Technical frame 12: Chapter 3 - Maps, Arrays and Slices / Slices

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

### Technical frame 13: Chapter 3 - Maps, Arrays and Slices / Slices

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00223))_

> When do you use which? The first one shouldn't need much of an explanation. You use this when you know the values that you want in the array ahead of time.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00222))_

```
names := []string{"leto", "jessica", "paul"}
checks := make([]bool, 10)
var names []string
scores := make([]int, 0, 20)
```

### Technical frame 14: Chapter 3 - Maps, Arrays and Slices / Slices

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

### Technical frame 15: Chapter 3 - Maps, Arrays and Slices / Slices

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00230))_

> Slices as wrappers to arrays is a powerful concept. Many languages have the concept of slicing an array. Both JavaScript and Ruby arrays have a slice method. You can also get a slice in Ruby by using [START..END] or in Python via [START:END] . However, in these languages, a slice is actually a new array with the values of the original copied over. If we take Ruby, what's the output of the following?

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00228))_

> Even when you know the size, append can be used.

### Technical frame 16: Chapter 3 - Maps, Arrays and Slices / Slices

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

### Technical frame 17: Chapter 3 - Maps, Arrays and Slices / Slices

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00234))_

> The [X:Y] syntax creates a slice of scores , starting from index 2 up until (but not including) index 4. However, unlike the Ruby example above, the Go code will produce an output of [1, 2, 999, 4, 5] . This is because our slice is really just a window into scores .

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00230))_

> You can also get a slice in Ruby by using [START..END] or in Python via [START:END] .

### Technical frame 18: Chapter 3 - Maps, Arrays and Slices / Slices

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00234))_

> The [X:Y] syntax creates a slice of scores , starting from index 2 up until (but not including) index 4. However, unlike the Ruby example above, the Go code will produce an output of [1, 2, 999, 4, 5] . This is because our slice is really just a window into scores .

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00231))_

```
scores = [1,2,3,4,5]
slice = scores[2..4]
slice[0] = 999
puts scores
```

### Technical frame 19: Chapter 3 - Maps, Arrays and Slices / Slices

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00234))_

> The [X:Y] syntax creates a slice of scores , starting from index 2 up until (but not including) index 4. However, unlike the Ruby example above, the Go code will produce an output of [1, 2, 999, 4, 5] . This is because our slice is really just a window into scores .

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00233))_

```
scores := []int{1,2,3,4,5}
slice := scores[2:4]
slice[0] = 999
fmt.Println(scores)
```

### Technical frame 20: Chapter 3 - Maps, Arrays and Slices / Slices

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00239))_

> We can see from the above example, that [X:] is shorthand for from X to the end while [:X] is shorthand for from the start up until X . Unlike other languages, Go doesn't support negative values. If we want all of the values of a slice except the last, we do:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00236))_

```
haystack = "the spice must flow";
console.log(haystack.indexOf(" ", 5));
```

### Technical frame 21: Chapter 3 - Maps, Arrays and Slices / Slices

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00239))_

> We can see from the above example, that [X:] is shorthand for from X to the end while [:X] is shorthand for from the start up until X . Unlike other languages, Go doesn't support negative values. If we want all of the values of a slice except the last, we do:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00238))_

```
strings.Index(haystack[5:], " ")
```

### Technical frame 22: Chapter 3 - Maps, Arrays and Slices / Slices

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00244))_

> Finally, now that we know about slices, we can look at another commonly used built-in function: copy . copy is one of those functions that highlights how slices change the way we code. Normally, a method that copies values from one array to another has 5 parameters: source , sourceStart , count , destination and destinationStart . With slices, we only need two:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00240))_

```
scores := []int{1, 2, 3, 4, 5}
scores = scores[:len(scores)-1]
```

### Technical frame 23: Chapter 3 - Maps, Arrays and Slices / Slices

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

### Technical frame 24: Chapter 3 - Maps, Arrays and Slices / Slices

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

### Technical frame 25: Chapter 3 - Maps, Arrays and Slices / Slices

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

### Technical frame 26: Chapter 3 - Maps, Arrays and Slices / Maps

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

### Technical frame 27: Chapter 3 - Maps, Arrays and Slices / Maps

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00260))_

> There's yet another way to declare and initialize values in Go. Like make , this approach is specific to maps and arrays. We can declare as a composite literal:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00252))_

```
// returns 1
total := len(lookup)
// has no return, can be called on a non-existing key
delete(lookup, "goku")
```

### Technical frame 28: Chapter 3 - Maps, Arrays and Slices / Maps

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00260))_

> There's yet another way to declare and initialize values in Go. Like make , this approach is specific to maps and arrays. We can declare as a composite literal:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00254))_

```
lookup := make(map[string]int, 100)
```

### Technical frame 29: Chapter 3 - Maps, Arrays and Slices / Maps

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00260))_

> There's yet another way to declare and initialize values in Go. Like make , this approach is specific to maps and arrays. We can declare as a composite literal:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00255))_

> If you have some idea of how many keys your map will have, defining an initial size can help with performance.

### Technical frame 30: Chapter 3 - Maps, Arrays and Slices / Maps

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00260))_

> There's yet another way to declare and initialize values in Go. Like make , this approach is specific to maps and arrays. We can declare as a composite literal:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00257))_

```
type Saiyan struct {
  Name string
  Friends map[string]*Saiyan
}
```

### Technical frame 31: Chapter 3 - Maps, Arrays and Slices / Maps

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

### Technical frame 32: Chapter 3 - Maps, Arrays and Slices / Maps

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00264))_

> Iteration over maps isn't ordered. Each iteration over a lookup will return the key value pair in a random order.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00261))_

```
lookup := map[string]int{
  "goku": 9001,
  "gohan": 2044,
}
```

### Technical frame 33: Chapter 3 - Maps, Arrays and Slices / Maps

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00264))_

> Iteration over maps isn't ordered. Each iteration over a lookup will return the key value pair in a random order.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00263))_

```
for key, value := range lookup {
  ...
}
```

### Technical frame 34: Chapter 3 - Maps, Arrays and Slices / Pointers versus Values

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00268))_

> Many developers think that passing b to, or returning it from, a function is going to be more efficient. However, what's being passed/returned is a copy of the slice, which itself is a reference. So with respect to passing/returning the slice itself, there's no difference. Where you will see a difference is when you modify the values of a slice or map. At this point, the same logic that we saw in Chapter 2 applies. So the decision on whether to define an array of pointers versus an array of valu

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00267))_

```
a := make([]Saiyan, 10)
//or
b := make([]*Saiyan, 10)
```


## Related pages

- [[coding-little-go-book-slice]] - broader topic: Slices shares source evidence from Chapter 3 - Maps, Arrays and Slices / Slices: In Go, you rarely, if ever, use arrays directly. Instead, you use slices. A slice is a lightweight structure that wraps and represents a portion of an array. There a ... [truncated]; Slices shares technical record from Chapter 3 - Maps, Arrays and Slices / Slices: scores := []int{1,4,293,4,9} (39 shared statement(s), 22 shared atom(s))
- [[coding-little-go-book-maps-array]] - broader topic: Maps Array shares source evidence from Chapter 3 - Maps, Arrays and Slices / Arrays: If you come from Python, Ruby, Perl, JavaScript or PHP (and more), you're probably used to programming with dynamic arrays . These are arrays that resize themselves ... [truncated]; Maps Array shares technical record from Chapter 3 - Maps, Arrays and Slices / Arrays: var scores [10]int scores[0] = 339 (29 shared statement(s), 22 shared atom(s))
- [[coding-little-go-book-maps]] - broader topic: Maps shares source evidence from Chapter 3 - Maps, Arrays and Slices / Maps: Maps in Go are what other languages call hashtables or dictionaries. They work as you expect: you define a key and value, and can get, set and delete values from it.; Maps shares technical record from Chapter 3 - Maps, Arrays and Slices / Maps: func main() { lookup := make(map[string]int) lookup["goku"] = 9001 power, exists := lookup["vegeta"] // prints 0, false // 0 is the default value for an integer fmt. ... [truncated] (7 shared statement(s), 8 shared atom(s))
- [[coding-little-go-book-array]] - broader topic: Arrays shares source evidence from Chapter 3 - Maps, Arrays and Slices / Arrays: If you come from Python, Ruby, Perl, JavaScript or PHP (and more), you're probably used to programming with dynamic arrays . These are arrays that resize themselves ... [truncated]; Arrays shares technical record from Chapter 3 - Maps, Arrays and Slices / Arrays: var scores [10]int scores[0] = 339 (9 shared statement(s), 3 shared atom(s))
- [[coding-little-go-book-value]] - shared statements and technical atoms: Value shares source evidence from Chapter 3 - Maps, Arrays and Slices / Slices: Here, the output is going to be [0, 0, 0, 0, 0, 9332] . Maybe you thought it would be [9332, 0, 0, 0, 0] ? To a human, that might seem logical. To a compiler, you're ... [truncated]; Value shares technical record from Chapter 3 - Maps, Arrays and Slices / Slices: func main() { scores := make([]int, 0, 10) scores = scores[0:8] scores[7] = 9033 fmt.Println(scores) } (2 shared statement(s), 12 shared atom(s))
- [[coding-little-go-book-language]] - shared statements and technical atoms: Language shares source evidence from Chapter 3 - Maps, Arrays and Slices / Arrays: If you come from Python, Ruby, Perl, JavaScript or PHP (and more), you're probably used to programming with dynamic arrays . These are arrays that resize themselves ... [truncated]; Language shares technical record from Chapter 3 - Maps, Arrays and Slices / Arrays: var scores [10]int scores[0] = 339 (3 shared statement(s), 6 shared atom(s))
- [[coding-little-go-book-code]] - shared statements and technical atoms: Code shares source evidence from Chapter 3 - Maps, Arrays and Slices / Slices: But that changes the intent of our original code. Appending to a slice of length 0 will set the first element. For whatever reason, our crashing code wanted to set t ... [truncated]; Code shares technical record from Chapter 3 - Maps, Arrays and Slices / Slices: func main() { scores := make([]int, 0, 10) scores = scores[0:8] scores[7] = 9033 fmt.Println(scores) } (2 shared statement(s), 4 shared atom(s))
- [[coding-little-go-book-section-chapter-3-maps-arrays-and-slices-4800f0d1]] - source section: Chapter 3 - Maps, Arrays and Slices shares source evidence from Chapter 3 - Maps, Arrays and Slices / Arrays: If you come from Python, Ruby, Perl, JavaScript or PHP (and more), you're probably used to programming with dynamic arrays . These are arrays that resize themselves ... [truncated]; Chapter 3 - Maps, Arrays and Slices shares technical record from Chapter 3 - Maps, Arrays and Slices / Arrays: var scores [10]int scores[0] = 339 (64 shared statement(s), 34 shared atom(s))

## Source

- [[coding-little-go-book]]
