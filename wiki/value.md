---
page_id: value
page_kind: concept
summary: Canonical concept 'Value': 2 source(s), 14 statement(s), 23 atom(s), 0 relation(s).
sources: raw/coding_learn_go_with_tests_excerpt.pdf, raw/coding_little_go_book.pdf
updated: 2026-06-26
category_path: concepts
projection_coverage: canonical-concept-value@534fb5121605e2932d8d27f7126ece2d
---

# Value

Compiled concept page from 2 source(s), 14 statement(s), and 23 technical atom(s).

## Source Evidence

### [[coding-learn-go-with-tests-excerpt]]

Source topic: [[coding-learn-go-with-tests-excerpt-value]]

#### Statements

- Getting a value out of a Map is the same as getting a value out of Array map[key] . _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00562))_
- To get the value out of an array at a particular index, just use array[index] syntax. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00297))_
- The value type, on the other hand, can be any type you want. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00554))_
- The second value is a boolean which indicates if the key was found successfully. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00589))_
- Except, we didn't consider what happens when the value we are trying to add already exists! _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00619))_

#### Technical atoms

> Context: The key type is special. It can only be a comparable type because without the ability to tell if 2 keys are equal, we have no way to ensure that we are getting the correct value. Comparable types are explained in depth in the language spec.
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00553))_

```
In dictionary_test.go
package main
import "testing"
func TestSearch(t *testing.T) {
    dictionary := map[string]string{"test": "this is just a test"}
got := Search(dictionary, "test")
    want := "this is just a test"
if got != want {
        t.Errorf("got %q want %q given, %q", got, want, "test")
    }
}
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00551))_


### [[coding-little-go-book]]

Source topic: [[coding-little-go-book-value]]

#### Statements

- The real value of pointers though is that they let you share values. _(coding_little_go_book.pdf (source-range-773b6275-00137))_
- To a compiler, you're telling it to append a value to a slice that already holds 5 values. _(coding_little_go_book.pdf (source-range-773b6275-00220))_
- Because Super made changes to a copy of our original goku value and thus, changes made in Super weren't reflected in the caller. _(coding_little_go_book.pdf (source-range-773b6275-00130))_
- Note that we're still passing a copy of goku's value to Super it just so happens that goku's value has become an address. _(coding_little_go_book.pdf (source-range-773b6275-00133))_
- As we already saw, passing values is a great way to make data immutable (changes that a function makes to it won't be reflected in the calling code). _(coding_little_go_book.pdf (source-range-773b6275-00181))_
- Normally, a method that copies values from one array to another has 5 parameters: source , sourceStart , count , destination and destinationStart . _(coding_little_go_book.pdf (source-range-773b6275-00244))_
- Interestingly, while the values aren't available outside the ifstatement, they are available inside any else if or else . _(coding_little_go_book.pdf (source-range-773b6275-00366))_
- Converting values back and forth is ugly and dangerous but sometimes, in a static language, it's the only choice. _(coding_little_go_book.pdf (source-range-773b6275-00376))_
- In the above example, we simply discard the value that was sent to the channel. _(coding_little_go_book.pdf (source-range-773b6275-00457))_

#### Technical atoms

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

> Context: As a final example, consider: Here, the output is going to be [0, 0, 0, 0, 0, 9332] . Maybe you thought it would be [9332, 0, 0, 0, 0] ? To a human, that might seem logical. To a compiler, you're telling it to append a value to a slice that already holds 5 values.
_(context: coding_little_go_book.pdf (source-range-773b6275-00218, source-range-773b6275-00220))_

```
func main() {
  scores := make([]int, 5)
  scores = append(scores, 9332)
  fmt.Println(scores)
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00219))_

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

> Context: The answer is [1, 2, 3, 4, 5] . That's because slice is a completely new array with copies of values. Now, consider the Go equivalent: The [X:Y] syntax creates a slice of scores , starting from index 2 up until (but not including) index 4. However, unlike the Ruby example above, the Go code will produce an output of [1, 2, 999, 4, 5] . This is because our slice is really just a window into scores .
_(context: coding_little_go_book.pdf (source-range-773b6275-00232, source-range-773b6275-00234))_

```
scores := []int{1,2,3,4,5}
slice := scores[2:4]
slice[0] = 999
fmt.Println(scores)
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00233))_

> Context: In Go, we leverage slices: We can see from the above example, that [X:] is shorthand for from X to the end while [:X] is shorthand for from the start up until X . Unlike other languages, Go doesn't support negative values. If we want all of the values of a slice except the last, we do:
_(context: coding_little_go_book.pdf (source-range-773b6275-00237, source-range-773b6275-00239))_

```
strings.Index(haystack[5:], " ")
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00238))_

> Context: We can see from the above example, that [X:] is shorthand for from X to the end while [:X] is shorthand for from the start up until X . Unlike other languages, Go doesn't support negative values. If we want all of the values of a slice except the last, we do: The above is the start of an efficient way to remove a value from an unsorted slice:
_(context: coding_little_go_book.pdf (source-range-773b6275-00239, source-range-773b6275-00241))_

```
scores := []int{1, 2, 3, 4, 5}
scores = scores[:len(scores)-1]
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00240))_

> Context: The above is the start of an efficient way to remove a value from an unsorted slice:
_(context: coding_little_go_book.pdf (source-range-773b6275-00241))_

```
func main() {
  scores := []int{1, 2, 3, 4, 5}
  scores = removeAtIndex(scores, 2)
  fmt.Println(scores) // [1 2 5 4]
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00242))_

> Context: The above is the start of an efficient way to remove a value from an unsorted slice:
_(context: coding_little_go_book.pdf (source-range-773b6275-00241))_

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
_(source: coding_little_go_book.pdf (source-range-773b6275-00243))_

> Context: Finally, now that we know about slices, we can look at another commonly used built-in function: copy . copy is one of those functions that highlights how slices change the way we code. Normally, a method that copies values from one array to another has 5 parameters: source , sourceStart , count , destination and destinationStart . With slices, we only need two: Take some time and play with the above code. Try variations. See what happens if you change copy to something like copy(worst[2:4], scores[:5]) , or what if you try to copy more or less than 5 values into worst ?
_(context: coding_little_go_book.pdf (source-range-773b6275-00244, source-range-773b6275-00246))_

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
_(source: coding_little_go_book.pdf (source-range-773b6275-00245))_

> Context: Go supports a slightly modified if-statement, one where a value can be initiated prior to the condition being evaluated:
_(context: coding_little_go_book.pdf (source-range-773b6275-00362))_

```
if x := 10; count > x {
  ...
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00363))_

> Context: You also have access to a powerful type switch: You'll see and probably use the empty interface more than you might first expect. Admittedly, it won't result in clean code. Converting values back and forth is ugly and dangerous but sometimes, in a static language, it's the only choice.
_(context: coding_little_go_book.pdf (source-range-773b6275-00374, source-range-773b6275-00376))_

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
_(source: coding_little_go_book.pdf (source-range-773b6275-00375))_

> Context: time.After returns a channel, so we can select from it. The channel is written to after the specified time expires. That's it. There's nothing more magical than that. If you're curious, here's what an implementation of after could look like: Also, time.After is a channel of type chan time.Time . In the above example, we simply discard the value that was sent to the channel. If you want though, you can receive it:
_(context: coding_little_go_book.pdf (source-range-773b6275-00453, source-range-773b6275-00457))_

```
go func() {
    time.Sleep(d)
    c <- true
  }()
  return c
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00455))_

> Context: time.After returns a channel, so we can select from it. The channel is written to after the specified time expires. That's it. There's nothing more magical than that. If you're curious, here's what an implementation of after could look like: Also, time.After is a channel of type chan time.Time . In the above example, we simply discard the value that was sent to the channel. If you want though, you can receive it:
_(context: coding_little_go_book.pdf (source-range-773b6275-00453, source-range-773b6275-00457))_

> First, what happens if you add the default case back?
_(source: coding_little_go_book.pdf (source-range-773b6275-00456))_

> Context: Also, time.After is a channel of type chan time.Time . In the above example, we simply discard the value that was sent to the channel. If you want though, you can receive it:
_(context: coding_little_go_book.pdf (source-range-773b6275-00457))_

```
case t := <-time.After(time.Millisecond * 100):
  fmt.Println("timed out at", t)
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00458))_


## Cross-Source Comparison

- No typed cross-source relationships detected yet.
