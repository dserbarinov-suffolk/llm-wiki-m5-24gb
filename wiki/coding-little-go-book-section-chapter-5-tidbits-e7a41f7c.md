---
page_id: coding-little-go-book-section-chapter-5-tidbits-e7a41f7c
page_kind: source
summary: Chapter 5 - Tidbits: 70 source-backed entries and 27 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-29
domain: coding-little-go-book
category_path: sources/coding-little-go-book/sections
source_id: coding_little_go_book.pdf
projection_coverage: section-coding-little-go-book-section-chapter-5-tidbits-e7a41f7c@07271a402bc757e68c4259a642155af2
---

# Chapter 5 - Tidbits

From [[coding-little-go-book]].

## Related pages

- [[coding-little-go-book-section-chapter-5-tidbits-error-handling-c2084411]] - narrower source section: Chapter 5 - Tidbits / Error Handling
- [[coding-little-go-book-section-chapter-5-tidbits-defer-9e77b4c5]] - narrower source section: Chapter 5 - Tidbits / Defer
- [[coding-little-go-book-section-chapter-5-tidbits-go-fmt-e0b0680f]] - narrower source section: Chapter 5 - Tidbits / go fmt
- [[coding-little-go-book-section-chapter-5-tidbits-initialized-if-10bfb3a1]] - narrower source section: Chapter 5 - Tidbits / Initialized If
- [[coding-little-go-book-section-chapter-5-tidbits-empty-interface-and-conversions-c4483a93]] - narrower source section: Chapter 5 - Tidbits / Empty Interface and Conversions
- [[coding-little-go-book-section-chapter-5-tidbits-strings-and-byte-arrays-6caeb68b]] - narrower source section: Chapter 5 - Tidbits / Strings and Byte Arrays
- [[coding-little-go-book-section-chapter-5-tidbits-function-type-561f81dd]] - narrower source section: Chapter 5 - Tidbits / Function Type
- [[coding-little-go-book-section-chapter-5-tidbits-before-you-continue-25d54302]] - narrower source section: Chapter 5 - Tidbits / Before You Continue
- [[coding-little-go-book-section-chapter-4-code-organization-and-interfaces-16681a63]] - previous source section: Chapter 4 - Code Organization and Interfaces
- [[coding-little-go-book-section-chapter-6-concurrency-55851f5e]] - next source section: Chapter 6 - Concurrency
- [[coding-little-go-book-tidbit]] - topic hub: opens the topic page for Tidbit

## Statements by subsection

### Chapter 5 - Tidbits / Error Handling

- Go's preferred way to deal with errors is through return values, not exceptions. Consider the strconv.Atoi function which takes a string and tries to convert it to an integer: _(coding_little_go_book.pdf (source-range-23d24eb1-00339))_
- You can create your own error type; the only requirement is that it fulfills the contract of the built-in error interface, which is: _(coding_little_go_book.pdf (source-range-23d24eb1-00341))_
- This is a package variable (it's defined outside of a function) which is publicly accessible (upper-case first letter). Various functions can return this error, say when we're reading from a file or STDIN. If it makes contextual sense, you should use this error, too. As consumers, we can use this singleton: _(coding_little_go_book.pdf (source-range-23d24eb1-00348))_
- As a final note, Go does have panic and recover functions. panic is like throwing an exception while recover is like catch ; they are rarely used. _(coding_little_go_book.pdf (source-range-23d24eb1-00350))_
- You can create your own error type; the only requirement is that it fulfills the contract of the built-in error interface, which is: _(coding_little_go_book.pdf (source-range-23d24eb1-00341))_

### Chapter 5 - Tidbits / Defer

- If you try to run the above code, you'll probably get an error (the file doesn't exist). The point is to show how defer works. Whatever you defer will be executed after the enclosing function (in this case main() ) returns, even if it does so violently. This lets you release resources near where it's initialized and takes care of multiple return points. _(coding_little_go_book.pdf (source-range-23d24eb1-00354))_
- Whatever you defer will be executed after the enclosing function (in this case main() ) returns, even if it does so violently. _(coding_little_go_book.pdf (source-range-23d24eb1-00354))_

### Chapter 5 - Tidbits / go fmt

- Most programs written in Go follow the same formatting rules, namely, a tab is used to indent and braces go on the same line as their statement. _(coding_little_go_book.pdf (source-range-23d24eb1-00356))_
- I know, you have your own style and you want to stick to it. That's what I did for a long time, but I'm glad I eventually gave in. A big reason for this is the go fmt command. It's easy to use and authoritative (so no one argues over meaningless preferences). _(coding_little_go_book.pdf (source-range-23d24eb1-00357))_
- Give it a try. It does more than indent your code; it also aligns field declarations and alphabetically orders imports. _(coding_little_go_book.pdf (source-range-23d24eb1-00360))_

### Chapter 5 - Tidbits / Initialized If

- Interestingly, while the values aren't available outside the ifstatement, they are available inside any else if or else . _(coding_little_go_book.pdf (source-range-23d24eb1-00366))_
- Interestingly, while the values aren't available outside the ifstatement, they are available inside any else if or else . _(coding_little_go_book.pdf (source-range-23d24eb1-00366))_

### Chapter 5 - Tidbits / Empty Interface and Conversions

- In most object-oriented languages, a built-in base class, often named object , is the superclass for all other classes. Go, having no inheritance, doesn't have such a superclass. What it does have is an empty interface with no methods: interface{} . Since every type implements all 0 of the empty interface's methods, and since interfaces are implicitly implemented, every type fulfills the contract of the empty interface. _(coding_little_go_book.pdf (source-range-23d24eb1-00368))_
- Note that if the underlying type is not int , the above will result in an error. _(coding_little_go_book.pdf (source-range-23d24eb1-00373))_
- You'll see and probably use the empty interface more than you might first expect. Admittedly, it won't result in clean code. Converting values back and forth is ugly and dangerous but sometimes, in a static language, it's the only choice. _(coding_little_go_book.pdf (source-range-23d24eb1-00376))_
- Converting values back and forth is ugly and dangerous but sometimes, in a static language, it's the only choice. _(coding_little_go_book.pdf (source-range-23d24eb1-00376))_

### Chapter 5 - Tidbits / Strings and Byte Arrays

- Strings and byte arrays are closely related. We can easily convert one to the other: _(coding_little_go_book.pdf (source-range-23d24eb1-00378))_
- In fact, this way of converting is common across various types as well. Some functions explicitly expect an int32 or an int64 or their unsigned counterparts. You might find yourself having to do things like: _(coding_little_go_book.pdf (source-range-23d24eb1-00380))_
- Still, when it comes to bytes and strings, it's probably something you'll end up doing often. Do note that when you use []byte(X) or string(X) , you're creating a copy of the data. This is necessary because strings are immutable. _(coding_little_go_book.pdf (source-range-23d24eb1-00382))_
- Strings are made of runes which are unicode code points. If you take the length of a string, you might not get what you expect. The following prints 3: _(coding_little_go_book.pdf (source-range-23d24eb1-00383))_
- This is necessary because strings are immutable. _(coding_little_go_book.pdf (source-range-23d24eb1-00382))_

### Chapter 5 - Tidbits / Function Type

- which can then be used anywhere -- as a field type, as a parameter, as a return value. _(coding_little_go_book.pdf (source-range-23d24eb1-00389))_
- which can then be used anywhere -- as a field type, as a parameter, as a return value. _(coding_little_go_book.pdf (source-range-23d24eb1-00389))_

### Chapter 5 - Tidbits / Before You Continue

- We looked at various aspects of programming with Go. Most notably, we saw how error handling behaves and how to release resources such as connections and open files. Many people dislike Go's approach to error handling. It can feel like a step backwards. Sometimes, I agree. Yet, I also find that it results in code that's easier to follow. defer is an unusual but practical approach to resource management. In fact, it isn't tied to resource management only. You can use defer for any purpose, such as logging when a function exits. _(coding_little_go_book.pdf (source-range-23d24eb1-00394))_
- Certainly, we haven't looked at all of the tidbits Go has to offer. But you should be feeling comfortable enough to tackle whatever you come across. _(coding_little_go_book.pdf (source-range-23d24eb1-00395))_
- Most notably, we saw how error handling behaves and how to release resources such as connections and open files. _(coding_little_go_book.pdf (source-range-23d24eb1-00394))_
- Yet, I also find that it results in code that's easier to follow. _(coding_little_go_book.pdf (source-range-23d24eb1-00394))_
- In fact, it isn't tied to resource management only. _(coding_little_go_book.pdf (source-range-23d24eb1-00394))_

## Technical atoms

### Technical frame 1: Chapter 5 - Tidbits / Error Handling

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00341))_

> You can create your own error type; the only requirement is that it fulfills the contract of the built-in error interface, which is:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00340))_

```
package main
import (
  "fmt"
  "os"
  "strconv"
)
func main() {
  if len(os.Args) != 2 {
    os.Exit(1)
  }
n, err := strconv.Atoi(os.Args[1])
  if err != nil {
    fmt.Println("not a valid number")
  } else {
    fmt.Println(n)
  }
}
```

### Technical frame 2: Chapter 5 - Tidbits / Error Handling

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00348))_

> This is a package variable (it's defined outside of a function) which is publicly accessible (upper-case first letter). Various functions can return this error, say when we're reading from a file or STDIN. If it makes contextual sense, you should use this error, too. As consumers, we can use this singleton:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00342))_

```
type error interface {
  Error() string
}
```

### Technical frame 3: Chapter 5 - Tidbits / Error Handling

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00348))_

> This is a package variable (it's defined outside of a function) which is publicly accessible (upper-case first letter). Various functions can return this error, say when we're reading from a file or STDIN. If it makes contextual sense, you should use this error, too. As consumers, we can use this singleton:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00344))_

```
import (
```

### Technical frame 4: Chapter 5 - Tidbits / Error Handling

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00348))_

> This is a package variable (it's defined outside of a function) which is publicly accessible (upper-case first letter). Various functions can return this error, say when we're reading from a file or STDIN. If it makes contextual sense, you should use this error, too. As consumers, we can use this singleton:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00345))_

```
"errors"
)
func process(count int) error {
  if count < 1 {
    return errors.New("Invalid count")
  }
  ...
  return nil
}
```

### Technical frame 5: Chapter 5 - Tidbits / Error Handling

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00348))_

> This is a package variable (it's defined outside of a function) which is publicly accessible (upper-case first letter). Various functions can return this error, say when we're reading from a file or STDIN. If it makes contextual sense, you should use this error, too. As consumers, we can use this singleton:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00347))_

```
var EOF = errors.New("EOF")
```

### Technical frame 6: Chapter 5 - Tidbits / Error Handling

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00350))_

> As a final note, Go does have panic and recover functions. panic is like throwing an exception while recover is like catch ; they are rarely used.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00348))_

> Various functions can return this error, say when we're reading from a file or STDIN.

### Technical frame 7: Chapter 5 - Tidbits / Error Handling

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00350))_

> As a final note, Go does have panic and recover functions. panic is like throwing an exception while recover is like catch ; they are rarely used.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00349))_

```
package main
import (
  "fmt"
  "io"
)
func main() {
  var input int
  _, err := fmt.Scan(&input)
  if err == io.EOF {
    fmt.Println("no more input!")
  }
}
```

### Technical frame 8: Chapter 5 - Tidbits / Defer

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00354))_

> If you try to run the above code, you'll probably get an error (the file doesn't exist). The point is to show how defer works. Whatever you defer will be executed after the enclosing function (in this case main() ) returns, even if it does so violently. This lets you release resources near where it's initialized and takes care of multiple return points.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00352))_

> Even though Go has a garbage collector, some resources require that we explicitly release them. For example, we need to Close() files after we're done with them. This sort of code is always dangerous. For one thing, as we're writing a function, it's easy to forget to Close something that we declared 10 lines up. For another, a function might have multiple return points. Go's solution is the defer keyword:

### Technical frame 9: Chapter 5 - Tidbits / Defer

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00354))_

> If you try to run the above code, you'll probably get an error (the file doesn't exist). The point is to show how defer works. Whatever you defer will be executed after the enclosing function (in this case main() ) returns, even if it does so violently. This lets you release resources near where it's initialized and takes care of multiple return points.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00353))_

```
package main
import (
  "fmt"
  "os"
)
func main() {
  file, err := os.Open("a_file_to_read")
  if err != nil {
    fmt.Println(err)
    return
  }
  defer file.Close()
  // read the file
}
```

### Technical frame 10: Chapter 5 - Tidbits / Defer

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00354))_

> If you try to run the above code, you'll probably get an error (the file doesn't exist).

### Technical frame 11: Chapter 5 - Tidbits / go fmt

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00360))_

> Give it a try. It does more than indent your code; it also aligns field declarations and alphabetically orders imports.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00358))_

> When you're inside a project, you can apply the formatting rule to it and all sub-projects via:

### Technical frame 12: Chapter 5 - Tidbits / go fmt

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00360))_

> Give it a try. It does more than indent your code; it also aligns field declarations and alphabetically orders imports.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00359))_

```
go fmt ./...
```

### Technical frame 13: Chapter 5 - Tidbits / Initialized If

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00366))_

> Interestingly, while the values aren't available outside the ifstatement, they are available inside any else if or else .

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00362))_

> Go supports a slightly modified if-statement, one where a value can be initiated prior to the condition being evaluated:

### Technical frame 14: Chapter 5 - Tidbits / Initialized If

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00366))_

> Interestingly, while the values aren't available outside the ifstatement, they are available inside any else if or else .

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00363))_

```
if x := 10; count > x {
  ...
}
```

### Technical frame 15: Chapter 5 - Tidbits / Initialized If

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00366))_

> Interestingly, while the values aren't available outside the ifstatement, they are available inside any else if or else .

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00365))_

```
if err := process(); err != nil {
  return err
}
```

### Technical frame 16: Chapter 5 - Tidbits / Empty Interface and Conversions

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00373))_

> Note that if the underlying type is not int , the above will result in an error.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00370))_

```
func add(a interface{}, b interface{}) interface{} {
  ...
}
```

### Technical frame 17: Chapter 5 - Tidbits / Empty Interface and Conversions

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00373))_

> Note that if the underlying type is not int , the above will result in an error.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00372))_

```
return a.(int) + b.(int)
```

### Technical frame 18: Chapter 5 - Tidbits / Empty Interface and Conversions

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

### Technical frame 19: Chapter 5 - Tidbits / Strings and Byte Arrays

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00380))_

> In fact, this way of converting is common across various types as well. Some functions explicitly expect an int32 or an int64 or their unsigned counterparts. You might find yourself having to do things like:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00379))_

```
stra := "the spice must flow"
byts := []byte(stra)
strb := string(byts)
```

### Technical frame 20: Chapter 5 - Tidbits / Strings and Byte Arrays

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00382))_

> Still, when it comes to bytes and strings, it's probably something you'll end up doing often. Do note that when you use []byte(X) or string(X) , you're creating a copy of the data. This is necessary because strings are immutable.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00381))_

```
int64(count)
```

### Technical frame 21: Chapter 5 - Tidbits / Strings and Byte Arrays

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00382))_

> Still, when it comes to bytes and strings, it's probably something you'll end up doing often. Do note that when you use []byte(X) or string(X) , you're creating a copy of the data. This is necessary because strings are immutable.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00383))_

> If you take the length of a string, you might not get what you expect.

### Technical frame 22: Chapter 5 - Tidbits / Strings and Byte Arrays

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00383))_

> Strings are made of runes which are unicode code points. If you take the length of a string, you might not get what you expect. The following prints 3:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00384))_

```
fmt.Println(len("椒"))
```

### Technical frame 23: Chapter 5 - Tidbits / Strings and Byte Arrays

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00383))_

> Strings are made of runes which are unicode code points. If you take the length of a string, you might not get what you expect. The following prints 3:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00385))_

> If you iterate over a string using range , you'll get runes, not bytes.

### Technical frame 24: Chapter 5 - Tidbits / Function Type

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00389))_

> which can then be used anywhere -- as a field type, as a parameter, as a return value.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00388))_

```
type Add func(a int, b int) int
```

### Technical frame 25: Chapter 5 - Tidbits / Function Type

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00389))_

> which can then be used anywhere -- as a field type, as a parameter, as a return value.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00390))_

```
package main
import (
  "fmt"
)
```

### Technical frame 26: Chapter 5 - Tidbits / Function Type

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00389))_

> which can then be used anywhere -- as a field type, as a parameter, as a return value.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00391))_

```
type Add func(a int, b int) int
func main() {
  fmt.Println(process(func(a int, b int) int{
      return a + b
  }))
}
func process(adder Add) int {
  return adder(1, 2)
}
```

### Technical frame 27: Chapter 5 - Tidbits / Before You Continue

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00395))_

> Certainly, we haven't looked at all of the tidbits Go has to offer. But you should be feeling comfortable enough to tackle whatever you come across.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00394))_

> You can use defer for any purpose, such as logging when a function exits.
