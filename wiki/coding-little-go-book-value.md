---
page_id: coding-little-go-book-value
page_kind: concept
summary: Value: 9 statement(s) and 22 atom(s) from raw/coding_little_go_book.pdf.
page_family: topic-concept
sources: raw/coding_little_go_book.pdf
updated: 2026-06-30
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-value@109e6cc1ff8ab9780f1943a4983b19c9
---

# Value

What [[coding-little-go-book]] covers about value:

## Statements

### Chapter 2 - Structures / Declarations and Initializations

- The answer is 9000, not 19000. Why? Because Super made changes to a copy of our original goku value and thus, changes made in Super weren't reflected in the caller. To make this work as you probably expect, we need to pass a pointer to our value: _(coding_little_go_book.pdf (source-range-23d24eb1-00130))_

- Note that we're still passing a copy of goku's value to Super it just so happens that goku's value has become an address. That copy is the same address as the original, which is what that indirection buys us. Think of it as copying the directions to a restaurant. What you have is a copy, but it still points to the same restaurant as the original. _(coding_little_go_book.pdf (source-range-23d24eb1-00133))_

- It should also be obvious that copying a pointer is going to be cheaper than copying a complex structure. On a 64-bit machine, a pointer is 64 bits large. If we have a structure with many fields, creating copies can be expensive. The real value of pointers though is that they let you share values. Do we want Super to alter a copy of goku or alter the shared goku value itself? _(coding_little_go_book.pdf (source-range-23d24eb1-00137))_

### Chapter 2 - Structures / Pointers versus Values

- As we already saw, passing values is a great way to make data immutable (changes that a function makes to it won't be reflected in the calling code). Sometimes, this is the behavior that you'll want but sometimes not. _(coding_little_go_book.pdf (source-range-23d24eb1-00181))_

### Chapter 3 - Maps, Arrays and Slices / Slices

- Here, the output is going to be [0, 0, 0, 0, 0, 9332] . Maybe you thought it would be [9332, 0, 0, 0, 0] ? To a human, that might seem logical. To a compiler, you're telling it to append a value to a slice that already holds 5 values. _(coding_little_go_book.pdf (source-range-23d24eb1-00220))_

- Finally, now that we know about slices, we can look at another commonly used built-in function: copy . copy is one of those functions that highlights how slices change the way we code. Normally, a method that copies values from one array to another has 5 parameters: source , sourceStart , count , destination and destinationStart . With slices, we only need two: _(coding_little_go_book.pdf (source-range-23d24eb1-00244))_

### Chapter 5 - Tidbits / Initialized If

- Interestingly, while the values aren't available outside the ifstatement, they are available inside any else if or else . _(coding_little_go_book.pdf (source-range-23d24eb1-00366))_

### Chapter 5 - Tidbits / Empty Interface and Conversions

- You'll see and probably use the empty interface more than you might first expect. Admittedly, it won't result in clean code. Converting values back and forth is ugly and dangerous but sometimes, in a static language, it's the only choice. _(coding_little_go_book.pdf (source-range-23d24eb1-00376))_

### Chapter 6 - Concurrency / Channels / Timeout

- Also, time.After is a channel of type chan time.Time . In the above example, we simply discard the value that was sent to the channel. If you want though, you can receive it: _(coding_little_go_book.pdf (source-range-23d24eb1-00457))_


## Technical atoms

### Technical frame 1: Chapter 2 - Structures / Declarations and Initializations

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00120))_

> Note: The trailing , in the above structure is required. Without it, the compiler will give an error. You'll appreciate the required consistency, especially if you've used a language or format that enforces the opposite.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00119))_

```
goku := Saiyan{
  Name: "Goku",
  Power: 9000,
}
```

### Technical frame 2: Chapter 2 - Structures / Declarations and Initializations

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00121))_

> We don't have to set all or even any of the fields. Both of these are valid:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00120))_

> You'll appreciate the required consistency, especially if you've used a language or format that enforces the opposite.

### Technical frame 3: Chapter 2 - Structures / Declarations and Initializations

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00126))_

> What all of the above examples do is declare a variable goku and assign a value to it.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00125))_

```
goku := Saiyan{"Goku", 9000}
```

### Technical frame 4: Chapter 2 - Structures / Declarations and Initializations

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

### Technical frame 5: Chapter 2 - Structures / Declarations and Initializations

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

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00230))_

> Slices as wrappers to arrays is a powerful concept. Many languages have the concept of slicing an array. Both JavaScript and Ruby arrays have a slice method. You can also get a slice in Ruby by using [START..END] or in Python via [START:END] . However, in these languages, a slice is actually a new array with the values of the original copied over. If we take Ruby, what's the output of the following?

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00228))_

> Even when you know the size, append can be used.

### Technical frame 9: Chapter 3 - Maps, Arrays and Slices / Slices

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

### Technical frame 10: Chapter 3 - Maps, Arrays and Slices / Slices

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00234))_

> The [X:Y] syntax creates a slice of scores , starting from index 2 up until (but not including) index 4. However, unlike the Ruby example above, the Go code will produce an output of [1, 2, 999, 4, 5] . This is because our slice is really just a window into scores .

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00230))_

> You can also get a slice in Ruby by using [START..END] or in Python via [START:END] .

### Technical frame 11: Chapter 3 - Maps, Arrays and Slices / Slices

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00234))_

> The [X:Y] syntax creates a slice of scores , starting from index 2 up until (but not including) index 4. However, unlike the Ruby example above, the Go code will produce an output of [1, 2, 999, 4, 5] . This is because our slice is really just a window into scores .

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00231))_

```
scores = [1,2,3,4,5]
slice = scores[2..4]
slice[0] = 999
puts scores
```

### Technical frame 12: Chapter 3 - Maps, Arrays and Slices / Slices

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00234))_

> The [X:Y] syntax creates a slice of scores , starting from index 2 up until (but not including) index 4. However, unlike the Ruby example above, the Go code will produce an output of [1, 2, 999, 4, 5] . This is because our slice is really just a window into scores .

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00233))_

```
scores := []int{1,2,3,4,5}
slice := scores[2:4]
slice[0] = 999
fmt.Println(scores)
```

### Technical frame 13: Chapter 3 - Maps, Arrays and Slices / Slices

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00239))_

> We can see from the above example, that [X:] is shorthand for from X to the end while [:X] is shorthand for from the start up until X . Unlike other languages, Go doesn't support negative values. If we want all of the values of a slice except the last, we do:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00238))_

```
strings.Index(haystack[5:], " ")
```

### Technical frame 14: Chapter 3 - Maps, Arrays and Slices / Slices

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00244))_

> Finally, now that we know about slices, we can look at another commonly used built-in function: copy . copy is one of those functions that highlights how slices change the way we code. Normally, a method that copies values from one array to another has 5 parameters: source , sourceStart , count , destination and destinationStart . With slices, we only need two:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00240))_

```
scores := []int{1, 2, 3, 4, 5}
scores = scores[:len(scores)-1]
```

### Technical frame 15: Chapter 3 - Maps, Arrays and Slices / Slices

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

### Technical frame 16: Chapter 3 - Maps, Arrays and Slices / Slices

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

### Technical frame 17: Chapter 3 - Maps, Arrays and Slices / Slices

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

### Technical frame 18: Chapter 5 - Tidbits / Initialized If

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00366))_

> Interestingly, while the values aren't available outside the ifstatement, they are available inside any else if or else .

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00363))_

```
if x := 10; count > x {
  ...
}
```

### Technical frame 19: Chapter 5 - Tidbits / Empty Interface and Conversions

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00376))_

> You'll see and probably use the empty interface more than you might first expect. Admittedly, it won't result in clean code. Converting values back and forth is ugly and dangerous but sometimes, in a static language, it's the only choice.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00375))_

```
switch a.(type) {
  case int:
    fmt.Printf("a is now an int and equals %d\n", a)
  case bool, string:
    // ...
  default:
    // ...
}
```

### Technical frame 20: Chapter 6 - Concurrency / Channels / Timeout

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00456))_

> Back to our select , there are a couple of things to play with. First, what happens if you add the default case back? Can you guess? Try it. If you aren't sure what's going on, remember that default fires immediately if no channel is available.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00455))_

```
go func() {
    time.Sleep(d)
    c <- true
  }()
  return c
}
```

### Technical frame 21: Chapter 6 - Concurrency / Channels / Timeout

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00457))_

> Also, time.After is a channel of type chan time.Time . In the above example, we simply discard the value that was sent to the channel. If you want though, you can receive it:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00456))_

> First, what happens if you add the default case back?

### Technical frame 22: Chapter 6 - Concurrency / Channels / Timeout

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00460))_

> The first available channel is chosen.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00458))_

```
case t := <-time.After(time.Millisecond * 100):
  fmt.Println("timed out at", t)
```


## Related pages

- [[coding-little-go-book-pointer-versus-value]] - narrower topic: Pointers versus Values shares source evidence from Chapter 2 - Structures / Declarations and Initializations: It should also be obvious that copying a pointer is going to be cheaper than copying a complex structure. On a 64-bit machine, a pointer is 64 bits large. If we have ... [truncated] (2 shared statement(s))
- [[coding-little-go-book-slice]] - shared statements and technical atoms: Slice shares source evidence from Chapter 3 - Maps, Arrays and Slices / Slices: Here, the output is going to be [0, 0, 0, 0, 0, 9332] . Maybe you thought it would be [9332, 0, 0, 0, 0] ? To a human, that might seem logical. To a compiler, you're ... [truncated]; Slice shares technical record from Chapter 3 - Maps, Arrays and Slices / Slices: func main() { scores := make([]int, 0, 10) scores = scores[0:8] scores[7] = 9033 fmt.Println(scores) } (1 shared statement(s), 12 shared atom(s))
- [[coding-little-go-book-copy]] - shared statements and technical atoms: Copy shares source evidence from Chapter 2 - Structures / Declarations and Initializations: The answer is 9000, not 19000. Why? Because Super made changes to a copy of our original goku value and thus, changes made in Super weren't reflected in the caller. ... [truncated]; Copy shares technical record from Chapter 2 - Structures / Declarations and Initializations: func main() { goku := Saiyan{"Goku", 9000} Super(goku) fmt.Println(goku.Power) } func Super(s Saiyan) { s.Power += 10000 } (3 shared statement(s), 7 shared atom(s))
- [[coding-little-go-book-array]] - shared statements and technical atoms: Array shares source evidence from Chapter 3 - Maps, Arrays and Slices / Slices: Finally, now that we know about slices, we can look at another commonly used built-in function: copy . copy is one of those functions that highlights how slices chan ... [truncated]; Array shares technical record from Chapter 3 - Maps, Arrays and Slices / Slices: func main() { scores := make([]int, 0, 10) scores = scores[0:8] scores[7] = 9033 fmt.Println(scores) } (1 shared statement(s), 7 shared atom(s))
- [[coding-little-go-book-change]] - shared statements and technical atoms: Change shares source evidence from Chapter 2 - Structures / Declarations and Initializations: The answer is 9000, not 19000. Why? Because Super made changes to a copy of our original goku value and thus, changes made in Super weren't reflected in the caller. ... [truncated]; Change shares technical record from Chapter 2 - Structures / Declarations and Initializations: func main() { goku := Saiyan{"Goku", 9000} Super(goku) fmt.Println(goku.Power) } func Super(s Saiyan) { s.Power += 10000 } (1 shared statement(s), 2 shared atom(s))
- [[coding-little-go-book-compiler]] - shared statements and technical atoms: Compiler shares source evidence from Chapter 3 - Maps, Arrays and Slices / Slices: Here, the output is going to be [0, 0, 0, 0, 0, 9332] . Maybe you thought it would be [9332, 0, 0, 0, 0] ? To a human, that might seem logical. To a compiler, you're ... [truncated]; Compiler shares technical record from Chapter 2 - Structures / Declarations and Initializations: goku := Saiyan{ Name: "Goku", Power: 9000, } (1 shared statement(s), 2 shared atom(s))
- [[coding-little-go-book-note]] - shared statements and technical atoms: Note shares source evidence from Chapter 2 - Structures / Declarations and Initializations: Note that we're still passing a copy of goku's value to Super it just so happens that goku's value has become an address. That copy is the same address as the origin ... [truncated]; Note shares technical record from Chapter 2 - Structures / Declarations and Initializations: goku := Saiyan{ Name: "Goku", Power: 9000, } (1 shared statement(s), 1 shared atom(s))
- [[coding-little-go-book-language]] - shared technical atoms: Language shares technical record from Chapter 3 - Maps, Arrays and Slices / Slices: Even when you know the size, append can be used. (5 shared atom(s))
- [[coding-little-go-book-ruby]] - shared technical atoms: Ruby shares technical record from Chapter 3 - Maps, Arrays and Slices / Slices: func main() { scores := make([]int, 0, 10) scores = scores[0:8] scores[7] = 9033 fmt.Println(scores) } (5 shared atom(s))
- [[coding-little-go-book-channel]] - shared technical atoms: Channel shares technical record from Chapter 6 - Concurrency / Channels / Timeout: go func() { time.Sleep(d) c <- true }() return c } (3 shared atom(s))
- [[coding-little-go-book-code]] - shared technical atoms: Code shares technical record from Chapter 3 - Maps, Arrays and Slices / Slices: func main() { scores := make([]int, 0, 10) scores = scores[0:8] scores[7] = 9033 fmt.Println(scores) } (3 shared atom(s))
- [[coding-little-go-book-structure]] - shared technical atoms: Structure shares technical record from Chapter 2 - Structures / Declarations and Initializations: goku := Saiyan{ Name: "Goku", Power: 9000, } (3 shared atom(s))
- [[coding-little-go-book-declaration]] - shared technical atoms: Declaration shares technical record from Chapter 2 - Structures / Declarations and Initializations: goku := Saiyan{"Goku", 9000} (1 shared atom(s))
- [[coding-little-go-book-empty-interface]] - shared technical atoms: Empty Interface shares technical record from Chapter 5 - Tidbits / Empty Interface and Conversions: switch a.(type) { case int: fmt.Printf("a is now an int and equals %d\n", a) case bool, string: // ... default: // ... } (1 shared atom(s))
- [[coding-little-go-book-reason]] - shared technical atoms: Reason shares technical record from Chapter 3 - Maps, Arrays and Slices / Slices: func main() { scores := make([]int, 0, 10) scores = scores[0:8] scores[7] = 9033 fmt.Println(scores) } (1 shared atom(s))
- [[coding-little-go-book-type]] - shared technical atoms: Type shares technical record from Chapter 5 - Tidbits / Empty Interface and Conversions: switch a.(type) { case int: fmt.Printf("a is now an int and equals %d\n", a) case bool, string: // ... default: // ... } (1 shared atom(s))
- [[coding-little-go-book-version]] - shared technical atoms: Version shares technical record from Chapter 3 - Maps, Arrays and Slices / Slices: Even when you know the size, append can be used. (1 shared atom(s))

## Source

- [[coding-little-go-book]]
