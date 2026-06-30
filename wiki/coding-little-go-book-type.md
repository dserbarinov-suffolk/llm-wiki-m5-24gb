---
page_id: coding-little-go-book-type
page_kind: concept
summary: Type: 7 statement(s) and 6 atom(s) from raw/coding_little_go_book.pdf.
page_family: topic-concept
sources: raw/coding_little_go_book.pdf
updated: 2026-06-30
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-type@a1439e4a4382401cc6e8a0609fedfd5b
---

# Type

What [[coding-little-go-book]] covers about type:

## Statements

### Introduction

- I've always had a love-hate relationship when it comes to learning new languages. On the one hand, languages are so fundamental to what we do, that even small changes can have measurable impact. That aha moment when something clicks can have a lasting effect on how you program and can redefine your expectations of other languages. On the downside, language design is fairly incremental. Learning new keywords, type system, coding style as well as new libraries, communities and paradigms is a lot of work that seems hard to justify. Compared to everything else we have to learn, new languages often feel like a poor investment of our time. _(coding_little_go_book.pdf (source-range-23d24eb1-00012))_

### Chapter 1 - The Basics / Static Typing

- Being statically typed means that variables must be of a specific type (int, string, bool, []byte, etc.). This is either achieved by specifying the type when the variable is declared or, in many cases, letting the compiler infer the type (we'll look at examples shortly). There's a lot more that can be said about static typing, but I believe it's something better understood by looking at code. If you're used to dynamically typed languages, you might find this cumbersome. You're not wrong, but there are advantages, especially when you pair static typing with compilation. The two are often conflated. It's true that when you have one, you normally have the other but it isn't a hard rule. With a rigid type system, a compiler is able to detect problems beyond mere syntactical mistakes as well as make further optimizations. _(coding_little_go_book.pdf (source-range-23d24eb1-00037))_

### Chapter 2 - Structures / Declarations and Initializations

- We made two changes. The first is the use of the & operator to get the address of our value (it's called the address of operator). Next, we changed the type of parameter Super expects. It used to expect a value of type Saiyan but now expects an address of type *Saiyan , where *X means pointer to value of type X . There's obviously some relation between the types Saiyan and *Saiyan , but they are two distinct types. _(coding_little_go_book.pdf (source-range-23d24eb1-00132))_

### Chapter 2 - Structures / Functions on Structures

- In the above code, we say that the type *Saiyan is the receiver of the Super method. We call Super like so: _(coding_little_go_book.pdf (source-range-23d24eb1-00142))_

### Chapter 4 - Code Organization and Interfaces / Before You Continue

- The way Go handles visibility of types is straightforward and effective. It's also consistent. There are a few things we haven't looked at, such as constants and global variables but rest assured, their visibility is determined by the same naming rule. _(coding_little_go_book.pdf (source-range-23d24eb1-00334))_

### Chapter 5 - Tidbits / Empty Interface and Conversions

- In most object-oriented languages, a built-in base class, often named object , is the superclass for all other classes. Go, having no inheritance, doesn't have such a superclass. What it does have is an empty interface with no methods: interface{} . Since every type implements all 0 of the empty interface's methods, and since interfaces are implicitly implemented, every type fulfills the contract of the empty interface. _(coding_little_go_book.pdf (source-range-23d24eb1-00368))_

- Note that if the underlying type is not int , the above will result in an error. _(coding_little_go_book.pdf (source-range-23d24eb1-00373))_


## Technical atoms

### Technical frame 1: Introduction

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00018))_

> Put plainly, learning Go is an efficient use of your time. You won't have to spend long hours learning or even mastering Go, and you'll end up with something practical from your effort.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00017))_

> You don't have to worry if your users have Ruby or the JVM installed, and if so, what version.

### Technical frame 2: Chapter 2 - Structures / Functions on Structures

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

### Technical frame 3: Chapter 2 - Structures / Functions on Structures

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00142))_

> In the above code, we say that the type *Saiyan is the receiver of the Super method. We call Super like so:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00143))_

```
goku := &Saiyan{"Goku", 9001}
goku.Super()
fmt.Println(goku.Power) // will print 19001
```

### Technical frame 4: Chapter 4 - Code Organization and Interfaces / Before You Continue

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00334))_

> The way Go handles visibility of types is straightforward and effective. It's also consistent. There are a few things we haven't looked at, such as constants and global variables but rest assured, their visibility is determined by the same naming rule.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00335))_

> Finally, if you're new to interfaces, it might take some time before you get a feel for them.

### Technical frame 5: Chapter 5 - Tidbits / Empty Interface and Conversions

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00373))_

> Note that if the underlying type is not int , the above will result in an error.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00372))_

```
return a.(int) + b.(int)
```

### Technical frame 6: Chapter 5 - Tidbits / Empty Interface and Conversions

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


## Related pages

- [[coding-little-go-book-code]] - shared statements and technical atoms: Code shares source evidence from Chapter 2 - Structures / Functions on Structures: In the above code, we say that the type *Saiyan is the receiver of the Super method. We call Super like so:; Code shares technical record from Chapter 2 - Structures / Functions on Structures: type Saiyan struct { Name string Power int } func (s *Saiyan) Super() { s.Power += 10000 } (1 shared statement(s), 2 shared atom(s))
- [[coding-little-go-book-system]] - shared statements and technical atoms: System shares source evidence from Introduction: I've always had a love-hate relationship when it comes to learning new languages. On the one hand, languages are so fundamental to what we do, that even small change ... [truncated]; System shares technical record from Introduction: You don't have to worry if your users have Ruby or the JVM installed, and if so, what version. (2 shared statement(s), 1 shared atom(s))
- [[coding-little-go-book-empty-interface]] - shared statements and technical atoms: Empty Interface shares source evidence from Chapter 5 - Tidbits / Empty Interface and Conversions: In most object-oriented languages, a built-in base class, often named object , is the superclass for all other classes. Go, having no inheritance, doesn't have such ... [truncated]; Empty Interface shares technical record from Chapter 5 - Tidbits / Empty Interface and Conversions: switch a.(type) { case int: fmt.Printf("a is now an int and equals %d\n", a) case bool, string: // ... default: // ... } (1 shared statement(s), 1 shared atom(s))
- [[coding-little-go-book-note]] - shared statements and technical atoms: Note shares source evidence from Chapter 5 - Tidbits / Empty Interface and Conversions: Note that if the underlying type is not int , the above will result in an error.; Note shares technical record from Chapter 5 - Tidbits / Empty Interface and Conversions: return a.(int) + b.(int) (1 shared statement(s), 1 shared atom(s))
- [[coding-little-go-book-you-continue]] - shared statements and technical atoms: Before You Continue shares source evidence from Chapter 4 - Code Organization and Interfaces / Before You Continue: The way Go handles visibility of types is straightforward and effective. It's also consistent. There are a few things we haven't looked at, such as constants and glo ... [truncated]; Before You Continue shares technical record from Chapter 4 - Code Organization and Interfaces / Before You Continue: Finally, if you're new to interfaces, it might take some time before you get a feel for them. (1 shared statement(s), 1 shared atom(s))
- [[coding-little-go-book-value]] - shared technical atoms: Value shares technical record from Chapter 5 - Tidbits / Empty Interface and Conversions: switch a.(type) { case int: fmt.Printf("a is now an int and equals %d\n", a) case bool, string: // ... default: // ... } (1 shared atom(s))
- [[coding-little-go-book-compiler]] - shared statements: Compiler shares source evidence from Chapter 1 - The Basics / Static Typing: Being statically typed means that variables must be of a specific type (int, string, bool, []byte, etc.). This is either achieved by specifying the type when the var ... [truncated] (1 shared statement(s))

## Source

- [[coding-little-go-book]]
