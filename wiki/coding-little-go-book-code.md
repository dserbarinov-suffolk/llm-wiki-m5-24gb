---
page_id: coding-little-go-book-code
page_kind: concept
summary: Code: 13 statement(s) and 14 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-29
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-code@ca369fb9ad7eb15fee81c6e1b838a29b
---

# Code

What [[coding-little-go-book]] covers about code:

## Statements

### Chapter 2 - Structures

- What Go does have are structures, which can be associated with methods. Go also supports a simple but effective form of composition. Overall, it results in simpler code, but there'll be occasions where you'll miss some of what OO has to offer. (It's worth pointing out that composition over inheritance is an old battle cry and Go is the first language I've used that takes a firm stand on the issue.) _(coding_little_go_book.pdf (source-range-23d24eb1-00112))_

### Chapter 2 - Structures / Functions on Structures

- In the above code, we say that the type *Saiyan is the receiver of the Super method. We call Super like so: _(coding_little_go_book.pdf (source-range-23d24eb1-00142))_

### Chapter 3 - Maps, Arrays and Slices / Slices

- But that changes the intent of our original code. Appending to a slice of length 0 will set the first element. For whatever reason, our crashing code wanted to set the element at index 7. To do this, we can re-slice our slice: _(coding_little_go_book.pdf (source-range-23d24eb1-00211))_

- The [X:Y] syntax creates a slice of scores , starting from index 2 up until (but not including) index 4. However, unlike the Ruby example above, the Go code will produce an output of [1, 2, 999, 4, 5] . This is because our slice is really just a window into scores . _(coding_little_go_book.pdf (source-range-23d24eb1-00234))_

### Chapter 4 - Code Organization and Interfaces / Packages / Visibility

- This also applies to structure fields. If a structure field name starts with a lowercase letter, only code within the same package will be able to access them. _(coding_little_go_book.pdf (source-range-23d24eb1-00300))_

### Chapter 4 - Code Organization and Interfaces / Packages / Dependency Management

- go get has a couple of other tricks up its sleeve. If we go get within a project, it'll scan all the files, looking for imports to third-party libraries and will download them. In a way, our own source code becomes a Gemfile or package.json . _(coding_little_go_book.pdf (source-range-23d24eb1-00314))_

### Chapter 4 - Code Organization and Interfaces / Before You Continue

- Ultimately, how you structure your code around Go's workspace is something that you'll only feel comfortable with after you've written a couple of non-trivial projects. What's most important for you to remember is the tight relationship between package names and your directory structure (not just within a project, but within the entire workspace). _(coding_little_go_book.pdf (source-range-23d24eb1-00333))_

### Chapter 6 - Concurrency / Goroutines

- A goroutine is similar to a thread, but it is scheduled by Go, not the OS. Code that runs in a goroutine can run concurrently with other code. Let's look at an example: _(coding_little_go_book.pdf (source-range-23d24eb1-00399))_

- There are a few interesting things going on here, but the most important is how we start a goroutine. We simply use the go keyword followed by the function we want to execute. If we just want to run a bit of code, such as the above, we can use an anonymous function. Do note that anonymous functions aren't only used with goroutines, however. _(coding_little_go_book.pdf (source-range-23d24eb1-00402))_

- Furthermore, the complexity of mapping and scheduling is hidden. We just say this code should run concurrently and let Go worry about making it happen. _(coding_little_go_book.pdf (source-range-23d24eb1-00405))_

### Chapter 6 - Concurrency / Synchronization

- Writing concurrent code requires that you pay specific attention to where and how you read and write values. In some ways, it's like programming without a garbage collector -- it requires that you think about your data from a new angle, always watchful for possible danger. Consider: _(coding_little_go_book.pdf (source-range-23d24eb1-00409))_

- Seems simple enough? The example above is deceptive. There's a whole class of serious bugs that can arise when doing concurrent programming. First of all, it isn't always so obvious what code needs to be protected. While it might be tempting to use coarse locks (locks that cover a large amount of code), that undermines the very reason we're doing concurrent programming in the first place. We generally want fine locks; else, we end up with a ten-lane highway that suddenly turns into a one-lane road. _(coding_little_go_book.pdf (source-range-23d24eb1-00418))_

- The other problem has to do with deadlocks. With a single lock, this isn't a problem, but if you're using two or more locks around the same code, it's dangerously easy to have situations where goroutineA holds lockA but needs access to lockB, while goroutineB holds lockB but needs access to lockA. _(coding_little_go_book.pdf (source-range-23d24eb1-00419))_


## Technical atoms

### Technical frame 1: Chapter 2 - Structures / Functions on Structures

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00142))_

> In the above code, we say that the type *Saiyan is the receiver of the Super method. We call Super like so:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00141))_

```
type Saiyan struct {
  Name string
  Power int
}
func (s *Saiyan) Super() {
  s.Power += 10000
}
```

### Technical frame 2: Chapter 2 - Structures / Functions on Structures

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00142))_

> In the above code, we say that the type *Saiyan is the receiver of the Super method. We call Super like so:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00143))_

```
goku := &Saiyan{"Goku", 9001}
goku.Super()
fmt.Println(goku.Power) // will print 19001
```

### Technical frame 3: Chapter 2 - Structures / New

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00153))_

> Which you use is up to you, but you'll find that most people prefer the latter whenever they have fields to initialize, since it tends to be easier to read:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00154))_

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

### Technical frame 4: Chapter 3 - Maps, Arrays and Slices / Slices

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

### Technical frame 5: Chapter 3 - Maps, Arrays and Slices / Slices

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00234))_

> The [X:Y] syntax creates a slice of scores , starting from index 2 up until (but not including) index 4. However, unlike the Ruby example above, the Go code will produce an output of [1, 2, 999, 4, 5] . This is because our slice is really just a window into scores .

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00233))_

```
scores := []int{1,2,3,4,5}
slice := scores[2:4]
slice[0] = 999
fmt.Println(scores)
```

### Technical frame 6: Chapter 3 - Maps, Arrays and Slices / Slices

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00239))_

> We can see from the above example, that [X:] is shorthand for from X to the end while [:X] is shorthand for from the start up until X . Unlike other languages, Go doesn't support negative values. If we want all of the values of a slice except the last, we do:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00236))_

```
haystack = "the spice must flow";
console.log(haystack.indexOf(" ", 5));
```

### Technical frame 7: Chapter 3 - Maps, Arrays and Slices / Slices

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

### Technical frame 8: Chapter 6 - Concurrency / Goroutines

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00402))_

> There are a few interesting things going on here, but the most important is how we start a goroutine. We simply use the go keyword followed by the function we want to execute. If we just want to run a bit of code, such as the above, we can use an anonymous function. Do note that anonymous functions aren't only used with goroutines, however.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00400))_

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

### Technical frame 9: Chapter 6 - Concurrency / Goroutines

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00402))_

> There are a few interesting things going on here, but the most important is how we start a goroutine. We simply use the go keyword followed by the function we want to execute. If we just want to run a bit of code, such as the above, we can use an anonymous function. Do note that anonymous functions aren't only used with goroutines, however.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00401))_

```
func process() {
  fmt.Println("processing")
}
```

### Technical frame 10: Chapter 6 - Concurrency / Goroutines

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00404))_

> Goroutines are easy to create and have little overhead. Multiple goroutines will end up running on the same underlying OS thread. This is often called an M:N threading model because we have M application threads (goroutines) running on N OS threads. The result is that a goroutine has a fraction of overhead (a few KB) than OS threads. On modern hardware, it's possible to have millions of goroutines.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00403))_

```
go func() {
  fmt.Println("processing")
}()
```

### Technical frame 11: Chapter 6 - Concurrency / Synchronization

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00413))_

> If you think the output is 1, 2, ... 20 you're both right and wrong. It's true that if you run the above code, you'll sometimes get that output. However, the reality is that the behavior is undefined. Why? Because we potentially have multiple (two in this case) goroutines writing to the same variable, counter , at the same time. Or, just as bad, one goroutine would be reading counter while another writes to it.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00410))_

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

### Technical frame 12: Chapter 6 - Concurrency / Synchronization

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00413))_

> If you think the output is 1, 2, ... 20 you're both right and wrong. It's true that if you run the above code, you'll sometimes get that output. However, the reality is that the behavior is undefined. Why? Because we potentially have multiple (two in this case) goroutines writing to the same variable, counter , at the same time. Or, just as bad, one goroutine would be reading counter while another writes to it.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00411))_

```
}
  time.Sleep(time.Millisecond * 10)
}
func incr() {
  counter++
  fmt.Println(counter)
}
```

### Technical frame 13: Chapter 6 - Concurrency / Synchronization

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00414))_

> Is that really a danger? Yes, absolutely. counter++ might seem like a simple line of code, but it actually gets broken down into multiple assembly statements -- the exact nature is dependent on the platform that you're running. If you run this example, you'll see that very often the numbers are printed in a weird order, and/or numbers are duplicated/missing. There are worse possibilities too, such as system crashes or accessing an arbitrary piece of data and incrementing it!

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00413))_

> It's true that if you run the above code, you'll sometimes get that output.

### Technical frame 14: Chapter 6 - Concurrency / Synchronization

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00417))_

> A mutex serializes access to the code under lock. The reason we simply define our lock as lock sync.Mutex is because the default value of a sync.Mutex is unlocked.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00416))_

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


## Related pages

- [[coding-little-go-book-code-organization]] - narrower topic: Code Organization shares source evidence from Chapter 4 - Code Organization and Interfaces / Packages / Visibility: This also applies to structure fields. If a structure field name starts with a lowercase letter, only code within the same package will be able to access them. (3 shared statement(s))
- [[coding-little-go-book-code-organization-and-interface]] - narrower topic: Code Organization and Interfaces shares source evidence from Chapter 4 - Code Organization and Interfaces / Packages / Visibility: This also applies to structure fields. If a structure field name starts with a lowercase letter, only code within the same package will be able to access them. (3 shared statement(s))
- [[coding-little-go-book-concurrency]] - shared statements and technical atoms: Concurrency shares source evidence from Chapter 6 - Concurrency / Goroutines: A goroutine is similar to a thread, but it is scheduled by Go, not the OS. Code that runs in a goroutine can run concurrently with other code. Let's look at an example:; Concurrency shares technical record from Chapter 6 - Concurrency / Goroutines: package main import ( "fmt" "time" ) func main() { fmt.Println("start") go process() time.Sleep(time.Millisecond * 10) // this is bad, don't do this! fmt.Println("done") } (6 shared statement(s), 7 shared atom(s))
- [[coding-little-go-book-synchronization]] - shared statements and technical atoms: Synchronization shares source evidence from Chapter 6 - Concurrency / Synchronization: Writing concurrent code requires that you pay specific attention to where and how you read and write values. In some ways, it's like programming without a garbage co ... [truncated]; Synchronization shares technical record from Chapter 6 - Concurrency / Synchronization: package main import ( "fmt" "time" ) var counter = 0 func main() { for i := 0; i < 20; i++ { go incr() (3 shared statement(s), 4 shared atom(s))
- [[coding-little-go-book-maps-array-and-slice]] - shared statements and technical atoms: Maps, Arrays and Slices shares source evidence from Chapter 3 - Maps, Arrays and Slices / Slices: But that changes the intent of our original code. Appending to a slice of length 0 will set the first element. For whatever reason, our crashing code wanted to set t ... [truncated]; Maps, Arrays and Slices shares technical record from Chapter 3 - Maps, Arrays and Slices / Slices: func main() { scores := make([]int, 0, 10) scores = scores[0:8] scores[7] = 9033 fmt.Println(scores) } (2 shared statement(s), 4 shared atom(s))
- [[coding-little-go-book-slice]] - shared statements and technical atoms: Slices shares source evidence from Chapter 3 - Maps, Arrays and Slices / Slices: But that changes the intent of our original code. Appending to a slice of length 0 will set the first element. For whatever reason, our crashing code wanted to set t ... [truncated]; Slices shares technical record from Chapter 3 - Maps, Arrays and Slices / Slices: func main() { scores := make([]int, 0, 10) scores = scores[0:8] scores[7] = 9033 fmt.Println(scores) } (2 shared statement(s), 4 shared atom(s))
- [[coding-little-go-book-goroutine]] - shared statements and technical atoms: Goroutines shares source evidence from Chapter 6 - Concurrency / Goroutines: A goroutine is similar to a thread, but it is scheduled by Go, not the OS. Code that runs in a goroutine can run concurrently with other code. Let's look at an example:; Goroutines shares technical record from Chapter 6 - Concurrency / Goroutines: package main import ( "fmt" "time" ) func main() { fmt.Println("start") go process() time.Sleep(time.Millisecond * 10) // this is bad, don't do this! fmt.Println("done") } (3 shared statement(s), 3 shared atom(s))
- [[coding-little-go-book-structure]] - shared statements and technical atoms: Structures shares source evidence from Chapter 2 - Structures: What Go does have are structures, which can be associated with methods. Go also supports a simple but effective form of composition. Overall, it results in simpler c ... [truncated]; Structures shares technical record from Chapter 2 - Structures / Functions on Structures: type Saiyan struct { Name string Power int } func (s *Saiyan) Super() { s.Power += 10000 } (2 shared statement(s), 3 shared atom(s))
- [[coding-little-go-book-maps-array]] - shared technical atoms: Maps Array shares technical record from Chapter 3 - Maps, Arrays and Slices / Slices: func main() { scores := make([]int, 0, 10) scores = scores[0:8] scores[7] = 9033 fmt.Println(scores) } (3 shared atom(s))
- [[coding-little-go-book-value]] - shared technical atoms: Value shares technical record from Chapter 3 - Maps, Arrays and Slices / Slices: func main() { scores := make([]int, 0, 10) scores = scores[0:8] scores[7] = 9033 fmt.Println(scores) } (3 shared atom(s))
- [[coding-little-go-book-package]] - shared statements: Packages shares source evidence from Chapter 4 - Code Organization and Interfaces / Packages / Visibility: This also applies to structure fields. If a structure field name starts with a lowercase letter, only code within the same package will be able to access them. (2 shared statement(s))

## Source

- [[coding-little-go-book]]
