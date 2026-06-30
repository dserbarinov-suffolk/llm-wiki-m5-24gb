---
page_id: code
page_kind: concept
summary: Canonical concept 'Code': 2 source(s), 23 statement(s), 20 atom(s), 0 relation(s).
sources: raw/coding_learn_go_with_tests_excerpt.pdf, raw/coding_little_go_book.pdf
updated: 2026-06-30
category_path: concepts
projection_coverage: canonical-concept-code@284e29c6fd592cbbec87c596d3fc7eb1
---

# Code

Compiled concept page from 2 source(s), 23 statement(s), and 20 technical atom(s).

## Source Evidence

### [[coding-learn-go-with-tests-excerpt]]

Source topic: [[coding-learn-go-with-tests-excerpt-code]]

#### Statements

- of the code you will write. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00033))_
- In the last example, we wrote the test after the code had been written so that you could get an example of how to write a test and declare a function. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00044))_
- The compiler understands how your code should snap together and work so you don't have to. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00051))_
- There's not a lot in the actual code we can really improve on here. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00191))_
- Adding this code will cause the example to appear in your documentation, making your code even more accessible. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00203))_
- If ever your code changes so that the example is no longer valid, your build will fail. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00203))_
- Writing better documentation so users of our code can understand its usage quickly _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00214))_
- The number of times the code is run shouldn't matter to you, the framework will determine what is a "good" value for that to let you have some decent results. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00249))_
- Our code does the job, but it doesn't contain anything explicit about rectangles. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00426))_
- In our case our test helper code did not need to know the exact shape it was asserting on, only how to "ask" for its area. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00543))_

#### Technical atoms

> Context: Learn Go with Tests -- Go Fundamentals (Excerpt) Hello, World How it works How to test Go modules? Back to Testing Writing tests Go's documentation Hello, YOU A note on source control Constants Hello, world... again Back to source control Discipline Keep going! More requirements French switch one...last...refactor? Wrapping up Some of Go's syntax around The TDD process and why the steps are important Integers Write the test first Try and run the test Write the minimal amount of code for the test to run and check the failing test output Write enough code to make it pass Refactor Testable Examples Wrapping up Iteration Write the test first Try and run the test Write the minimal amount of code for the test to run and check the failing test output Write enough code to make it pass Refactor Benchmarking Practice exercises Wrapping up Arrays and slices Write the test first Try to run the test Write the minimal amount of code for the test to run and check the failing test output Write enough code to make it pass Refactor Arrays and their type Write the test first Try and run the test Write the minimal amount of code for the test to run and check the failing test output Write enough code to make it pass Refactor Write the test first Try and run the test Write the minimal amount of code for the test to run and check the failing test output Write enough code to make it pass Refactor Write the test first Try and run the test Write the minimal amount of code for the test to run and check the failing test output Write enough code to make it pass Refactor Write the test first Try and run the test Write enough code to make it pass Refactor Wrapping up Structs, methods & interfaces Write the test first Try to run the test Write the minimal amount of code for the test to run and check the failing test output Write enough code to make it pass Refactor Write the test first Try to run the test Write the minimal amount of code for the test to run and check the failing test output What are methods? Write the minimal amount of code for the test to run and check the failing test output Write enough code to make it pass Refactor Wait, what? Decoupling Further refactoring Write the test first Try to run the test Write the minimal amount of code for the test to run and check the failing test output Write enough code to make it pass Refactor Make sure your test output is helpful Wrapping up Maps Write the test first Try to run the test Write the minimal amount of code for the test to run and check the output Write enough code to make it pass Refactor Using a custom type Write the test first Try and run the test Write the minimal amount of code for the test to run and check the output Write enough code to make it pass Refactor Write the test first Write the minimal amount of code for the test to run and check output Write enough code to make it pass Pointers, copies, et al Refactor Write the test first Try to run test Write the minimal amount of code for the test to run and check the
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00002))_

```
output
Write enough code to make it pass
Refactor
Write the test ﬁrst
Try and run the test
Write minimal amount of code for the test to run and check the
failing test output
Write enough code to make it pass
Write the test ﬁrst
Try and run the test
Write the minimal amount of code for the test to run and check the
failing test output
Write enough code to make it pass
Note on declaring a new error for Update
Write the test ﬁrst
Try to run the test
Write the minimal amount of code for the test to run and check the
failing test output
Write enough code to make it pass
Refactor
Try to run test
Write enough code to make it pass
Wrapping up
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00003))_

> Context: When using a statically typed language like Go it is important to listen to the compiler . The compiler understands how your code should snap together and work so you don't have to. If you try and run your tests again your hello.go will fail to compile because you're not passing an argument. Send in "world" to make it compile.
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00051, source-range-cb73a893-00055))_

```
func Hello(name string) string {
    return "Hello, world"
}
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00054))_

> Context: There's not a lot in the actual code we can really improve on here.
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00191))_

> You can add documentation to functions with comments, and these will appear in Go Doc just like when you look at the standard library's documentation.
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00194))_

> Context: Often code examples that can be found outside the codebase, such as a readme file, become out of date and incorrect compared to the actual code because they don't get checked.
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00198))_

> If you really want to go the extra mile you can make Testable Examples.
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00197))_

> Context: The number of times the code is run shouldn't matter to you, the framework will determine what is a "good" value for that to let you have some decent results.
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00249))_

```
goos: darwin
goarch: amd64
pkg: github.com/quii/learn-go-with-tests/for/v4
10000000           136 ns/op
PASS
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00251))_

> Context: Only the body of the loop is timed; it automatically excludes setup and cleanup code from benchmark timing. A typical benchmark is structured like:
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00254))_

```
func Benchmark(b *testing.B) {
    //... setup ...
    for b.Loop() {
        //... code to measure ...
    }
    //... cleanup ...
}
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00255))_


### [[coding-little-go-book]]

Source topic: [[coding-little-go-book-code]]

#### Statements

- Overall, it results in simpler code, but there'll be occasions where you'll miss some of what OO has to offer. _(coding_little_go_book.pdf (source-range-23d24eb1-00112))_
- In the above code, we say that the type *Saiyan is the receiver of the Super method. _(coding_little_go_book.pdf (source-range-23d24eb1-00142))_
- For whatever reason, our crashing code wanted to set the element at index 7. _(coding_little_go_book.pdf (source-range-23d24eb1-00211))_
- However, unlike the Ruby example above, the Go code will produce an output of [1, 2, 999, 4, 5] . _(coding_little_go_book.pdf (source-range-23d24eb1-00234))_
- If a structure field name starts with a lowercase letter, only code within the same package will be able to access them. _(coding_little_go_book.pdf (source-range-23d24eb1-00300))_
- In a way, our own source code becomes a Gemfile or package.json . _(coding_little_go_book.pdf (source-range-23d24eb1-00314))_
- Ultimately, how you structure your code around Go's workspace is something that you'll only feel comfortable with after you've written a couple of non-trivial projects. _(coding_little_go_book.pdf (source-range-23d24eb1-00333))_
- Code that runs in a goroutine can run concurrently with other code. _(coding_little_go_book.pdf (source-range-23d24eb1-00399))_
- If we just want to run a bit of code, such as the above, we can use an anonymous function. _(coding_little_go_book.pdf (source-range-23d24eb1-00402))_
- We just say this code should run concurrently and let Go worry about making it happen. _(coding_little_go_book.pdf (source-range-23d24eb1-00405))_
- Writing concurrent code requires that you pay specific attention to where and how you read and write values. _(coding_little_go_book.pdf (source-range-23d24eb1-00409))_
- First of all, it isn't always so obvious what code needs to be protected. _(coding_little_go_book.pdf (source-range-23d24eb1-00418))_
- With a single lock, this isn't a problem, but if you're using two or more locks around the same code, it's dangerously easy to have situations where goroutineA holds lockA but needs access to lockB, while goroutineB holds lockB but needs access to lockA. _(coding_little_go_book.pdf (source-range-23d24eb1-00419))_

#### Technical atoms

> Context: We can associate a method with a structure: In the above code, we say that the type *Saiyan is the receiver of the Super method. We call Super like so:
_(context: coding_little_go_book.pdf (source-range-23d24eb1-00140, source-range-23d24eb1-00142))_

```
type Saiyan struct {
  Name string
  Power int
}
func (s *Saiyan) Super() {
  s.Power += 10000
}
```
_(source: coding_little_go_book.pdf (source-range-23d24eb1-00141))_

> Context: In the above code, we say that the type *Saiyan is the receiver of the Super method. We call Super like so:
_(context: coding_little_go_book.pdf (source-range-23d24eb1-00142))_

```
goku := &Saiyan{"Goku", 9001}
goku.Super()
fmt.Println(goku.Power) // will print 19001
```
_(source: coding_little_go_book.pdf (source-range-23d24eb1-00143))_

> Context: Which you use is up to you, but you'll find that most people prefer the latter whenever they have fields to initialize, since it tends to be easier to read: Whichever approach you choose, if you follow the factory pattern above, you can shield the rest of your code from knowing and worrying about any of the allocation details.
_(context: coding_little_go_book.pdf (source-range-23d24eb1-00153, source-range-23d24eb1-00155))_

```
goku := new(Saiyan)
goku.Name = "goku"
goku.Power = 9001
//vs
goku := &Saiyan {
  Name: "goku",
  Power: 9000,
}
```
_(source: coding_little_go_book.pdf (source-range-23d24eb1-00154))_

> Context: But that changes the intent of our original code. Appending to a slice of length 0 will set the first element. For whatever reason, our crashing code wanted to set the element at index 7. To do this, we can re-slice our slice: How large can we resize a slice? Up to its capacity which, in this case, is 10. You might be thinking this doesn't actually solve the fixed-length issue of arrays. It turns out that append is pretty special. If the underlying array is full, it will create a new larger array and copy the values over (this is exactly how dynamic arrays work in PHP , Python, Ruby, JavaScript, ...). This is why, in the example above that used append , we had to re-assign the value returned by append to our scores variable: append might have created a new value if the original had no more space.
_(context: coding_little_go_book.pdf (source-range-23d24eb1-00211, source-range-23d24eb1-00213))_

```
func main() {
  scores := make([]int, 0, 10)
  scores = scores[0:8]
  scores[7] = 9033
  fmt.Println(scores)
}
```
_(source: coding_little_go_book.pdf (source-range-23d24eb1-00212))_

> Context: The answer is [1, 2, 3, 4, 5] . That's because slice is a completely new array with copies of values. Now, consider the Go equivalent: The [X:Y] syntax creates a slice of scores , starting from index 2 up until (but not including) index 4. However, unlike the Ruby example above, the Go code will produce an output of [1, 2, 999, 4, 5] . This is because our slice is really just a window into scores .
_(context: coding_little_go_book.pdf (source-range-23d24eb1-00232, source-range-23d24eb1-00234))_

```
scores := []int{1,2,3,4,5}
slice := scores[2:4]
slice[0] = 999
fmt.Println(scores)
```
_(source: coding_little_go_book.pdf (source-range-23d24eb1-00233))_

> Context: This changes how you code. For example, a number of functions take a position parameter. In JavaScript, if we want to find the first space in a string (yes, slices work on strings too!) after the first five characters, we'd write:
_(context: coding_little_go_book.pdf (source-range-23d24eb1-00235))_

```
haystack = "the spice must flow";
console.log(haystack.indexOf(" ", 5));
```
_(source: coding_little_go_book.pdf (source-range-23d24eb1-00236))_

> Context: Finally, now that we know about slices, we can look at another commonly used built-in function: copy . copy is one of those functions that highlights how slices change the way we code. Normally, a method that copies values from one array to another has 5 parameters: source , sourceStart , count , destination and destinationStart . With slices, we only need two: Take some time and play with the above code. Try variations. See what happens if you change copy to something like copy(worst[2:4], scores[:5]) , or what if you try to copy more or less than 5 values into worst ?
_(context: coding_little_go_book.pdf (source-range-23d24eb1-00244, source-range-23d24eb1-00246))_

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
_(source: coding_little_go_book.pdf (source-range-23d24eb1-00245))_

> Context: A goroutine is similar to a thread, but it is scheduled by Go, not the OS. Code that runs in a goroutine can run concurrently with other code. Let's look at an example: There are a few interesting things going on here, but the most important is how we start a goroutine. We simply use the go keyword followed by the function we want to execute. If we just want to run a bit of code, such as the above, we can use an anonymous function. Do note that anonymous functions aren't only used with goroutines, however.
_(context: coding_little_go_book.pdf (source-range-23d24eb1-00399, source-range-23d24eb1-00402))_

```
package main
import (
  "fmt"
  "time"
)
func main() {
  fmt.Println("start")
  go process()
  time.Sleep(time.Millisecond * 10) // this is bad, don't do this!
  fmt.Println("done")
}
```
_(source: coding_little_go_book.pdf (source-range-23d24eb1-00400))_

> Context: A goroutine is similar to a thread, but it is scheduled by Go, not the OS. Code that runs in a goroutine can run concurrently with other code. Let's look at an example: There are a few interesting things going on here, but the most important is how we start a goroutine. We simply use the go keyword followed by the function we want to execute. If we just want to run a bit of code, such as the above, we can use an anonymous function. Do note that anonymous functions aren't only used with goroutines, however.
_(context: coding_little_go_book.pdf (source-range-23d24eb1-00399, source-range-23d24eb1-00402))_

```
func process() {
  fmt.Println("processing")
}
```
_(source: coding_little_go_book.pdf (source-range-23d24eb1-00401))_

> Context: There are a few interesting things going on here, but the most important is how we start a goroutine. We simply use the go keyword followed by the function we want to execute. If we just want to run a bit of code, such as the above, we can use an anonymous function. Do note that anonymous functions aren't only used with goroutines, however. Goroutines are easy to create and have little overhead. Multiple goroutines will end up running on the same underlying OS thread. This is often called an M:N threading model because we have M application threads (goroutines) running on N OS threads. The result is that a goroutine has a fraction of overhead (a few KB) than OS threads. On modern hardware, it's possible to have millions of goroutines.
_(context: coding_little_go_book.pdf (source-range-23d24eb1-00402, source-range-23d24eb1-00404))_

```
go func() {
  fmt.Println("processing")
}()
```
_(source: coding_little_go_book.pdf (source-range-23d24eb1-00403))_

> Context: Writing concurrent code requires that you pay specific attention to where and how you read and write values. In some ways, it's like programming without a garbage collector -- it requires that you think about your data from a new angle, always watchful for possible danger. Consider: What do you think the output will be?
_(context: coding_little_go_book.pdf (source-range-23d24eb1-00409, source-range-23d24eb1-00412))_

```
package main
import (
  "fmt"
  "time"
)
var counter = 0
func main() {
  for i := 0; i < 20; i++ {
    go incr()
```
_(source: coding_little_go_book.pdf (source-range-23d24eb1-00410))_

> Context: Writing concurrent code requires that you pay specific attention to where and how you read and write values. In some ways, it's like programming without a garbage collector -- it requires that you think about your data from a new angle, always watchful for possible danger. Consider: What do you think the output will be?
_(context: coding_little_go_book.pdf (source-range-23d24eb1-00409, source-range-23d24eb1-00412))_

```
}
  time.Sleep(time.Millisecond * 10)
}
func incr() {
  counter++
  fmt.Println(counter)
}
```
_(source: coding_little_go_book.pdf (source-range-23d24eb1-00411))_

> Context: Is that really a danger? Yes, absolutely. counter++ might seem like a simple line of code, but it actually gets broken down into multiple assembly statements -- the exact nature is dependent on the platform that you're running. If you run this example, you'll see that very often the numbers are printed in a weird order, and/or numbers are duplicated/missing. There are worse possibilities too, such as system crashes or accessing an arbitrary piece of data and incrementing it!
_(context: coding_little_go_book.pdf (source-range-23d24eb1-00414))_

> It's true that if you run the above code, you'll sometimes get that output.
_(source: coding_little_go_book.pdf (source-range-23d24eb1-00413))_

> Context: The only concurrent thing you can safely do to a variable is to read from it. You can have as many readers as you want, but writes need to be synchronized. There are various ways to do this, including using some truly atomic operations that rely on special CPU instructions. However, the most common approach is to use a mutex: A mutex serializes access to the code under lock. The reason we simply define our lock as lock sync.Mutex is because the default value of a sync.Mutex is unlocked.
_(context: coding_little_go_book.pdf (source-range-23d24eb1-00415, source-range-23d24eb1-00417))_

```
package main
import (
  "fmt"
  "time"
  "sync"
)
var (
  counter = 0
  lock sync.Mutex
)
func main() {
  for i := 0; i < 20; i++ {
    go incr()
  }
  time.Sleep(time.Millisecond * 10)
}
func incr() {
  lock.Lock()
  defer lock.Unlock()
  counter++
  fmt.Println(counter)
}
```
_(source: coding_little_go_book.pdf (source-range-23d24eb1-00416))_


## Cross-Source Comparison

- No typed cross-source relationships detected yet.
