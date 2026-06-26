---
page_id: coding-little-go-book-code
page_kind: concept
summary: Code: 13 statement(s) and 13 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-code@a3077235faba301c7ae9869071765170
---

# Code

What [[coding-little-go-book]] covers about code:

## Statements

- Code that runs in a goroutine can run concurrently with other code. _(coding_little_go_book.pdf (source-range-773b6275-00399))_
- Overall, it results in simpler code, but there'll be occasions where you'll miss some of what OO has to offer. _(coding_little_go_book.pdf (source-range-773b6275-00112))_
- In the above code, we say that the type *Saiyan is the receiver of the Super method. _(coding_little_go_book.pdf (source-range-773b6275-00142))_
- For whatever reason, our crashing code wanted to set the element at index 7. _(coding_little_go_book.pdf (source-range-773b6275-00211))_
- However, unlike the Ruby example above, the Go code will produce an output of [1, 2, 999, 4, 5] . _(coding_little_go_book.pdf (source-range-773b6275-00234))_
- If a structure field name starts with a lowercase letter, only code within the same package will be able to access them. _(coding_little_go_book.pdf (source-range-773b6275-00300))_
- In a way, our own source code becomes a Gemfile or package.json . _(coding_little_go_book.pdf (source-range-773b6275-00314))_
- Ultimately, how you structure your code around Go's workspace is something that you'll only feel comfortable with after you've written a couple of non-trivial projects. _(coding_little_go_book.pdf (source-range-773b6275-00333))_
- If we just want to run a bit of code, such as the above, we can use an anonymous function. _(coding_little_go_book.pdf (source-range-773b6275-00402))_
- We just say this code should run concurrently and let Go worry about making it happen. _(coding_little_go_book.pdf (source-range-773b6275-00405))_
- Writing concurrent code requires that you pay specific attention to where and how you read and write values. _(coding_little_go_book.pdf (source-range-773b6275-00409))_
- First of all, it isn't always so obvious what code needs to be protected. _(coding_little_go_book.pdf (source-range-773b6275-00418))_
- With a single lock, this isn't a problem, but if you're using two or more locks around the same code, it's dangerously easy to have situations where goroutineA holds lockA but needs access to lockB, while goroutineB holds lockB but needs access to lockA. _(coding_little_go_book.pdf (source-range-773b6275-00419))_

## Technical atoms

> Context: We can associate a method with a structure: In the above code, we say that the type *Saiyan is the receiver of the Super method. We call Super like so:
_(context: coding_little_go_book.pdf (source-range-773b6275-00140, source-range-773b6275-00142))_

```
type Saiyan struct {
  Name string
  Power int
}
func (s *Saiyan) Super() {
  s.Power += 10000
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00141))_

> Context: In the above code, we say that the type *Saiyan is the receiver of the Super method. We call Super like so:
_(context: coding_little_go_book.pdf (source-range-773b6275-00142))_

```
goku := &Saiyan{"Goku", 9001}
goku.Super()
fmt.Println(goku.Power) // will print 19001
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00143))_

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

> Context: The answer is [1, 2, 3, 4, 5] . That's because slice is a completely new array with copies of values. Now, consider the Go equivalent: The [X:Y] syntax creates a slice of scores , starting from index 2 up until (but not including) index 4. However, unlike the Ruby example above, the Go code will produce an output of [1, 2, 999, 4, 5] . This is because our slice is really just a window into scores .
_(context: coding_little_go_book.pdf (source-range-773b6275-00232, source-range-773b6275-00234))_

```
scores := []int{1,2,3,4,5}
slice := scores[2:4]
slice[0] = 999
fmt.Println(scores)
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00233))_

> Context: This changes how you code. For example, a number of functions take a position parameter. In JavaScript, if we want to find the first space in a string (yes, slices work on strings too!) after the first five characters, we'd write:
_(context: coding_little_go_book.pdf (source-range-773b6275-00235))_

```
haystack = "the spice must flow";
console.log(haystack.indexOf(" ", 5));
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00236))_

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


## Source

- [[coding-little-go-book]]
