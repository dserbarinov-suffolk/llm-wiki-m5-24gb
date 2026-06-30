---
page_id: coding-little-go-book-change
page_kind: concept
summary: Change: 4 statement(s) and 5 atom(s) from raw/coding_little_go_book.pdf.
page_family: topic-concept
sources: raw/coding_little_go_book.pdf
updated: 2026-06-30
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-change@3c238d429a93d966e8158dfcb620e30d
---

# Change

What [[coding-little-go-book]] covers about change:

## Statements

### Introduction

- That said, we have to move forward. We have to be willing to take incremental steps because, again, languages are the foundation of what we do. Though the changes are often incremental, they tend to have a wide scope and they impact productivity, readability, performance, testability, dependency management, error handling, documentation, profiling, communities, standard libraries, and so on. Is there a positive way to say death by a thousand cuts ? _(coding_little_go_book.pdf (source-range-23d24eb1-00013))_

### Chapter 1 - The Basics / Running Go Code

- Next, open a shell/command prompt and change the directory to where you saved the file. For me, that means typing cd ~/code . _(coding_little_go_book.pdf (source-range-23d24eb1-00052))_

### Chapter 2 - Structures / Declarations and Initializations

- The answer is 9000, not 19000. Why? Because Super made changes to a copy of our original goku value and thus, changes made in Super weren't reflected in the caller. To make this work as you probably expect, we need to pass a pointer to our value: _(coding_little_go_book.pdf (source-range-23d24eb1-00130))_

### Chapter 2 - Structures / Constructors

- This pattern rubs a lot of developers the wrong way. On the one hand, it's a pretty slight syntactical change; on the other, it does feel a little less compartmentalized. _(coding_little_go_book.pdf (source-range-23d24eb1-00147))_


## Technical atoms

### Technical frame 1: Introduction

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00013))_

> That said, we have to move forward. We have to be willing to take incremental steps because, again, languages are the foundation of what we do. Though the changes are often incremental, they tend to have a wide scope and they impact productivity, readability, performance, testability, dependency management, error handling, documentation, profiling, communities, standard libraries, and so on. Is there a positive way to say death by a thousand cuts ?

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00012))_

> I've always had a love-hate relationship when it comes to learning new languages.

### Technical frame 2: Chapter 1 - The Basics / Running Go Code

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00051))_

> Save the file as main.go . For now, you can save it anywhere you want; we don't need to live inside Go's workspace for trivial examples.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00050))_

```
package main
func main() {
  println("it's over 9000!")
}
```

### Technical frame 3: Chapter 2 - Structures / Declarations and Initializations

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

### Technical frame 4: Chapter 2 - Structures / Declarations and Initializations

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

### Technical frame 5: Chapter 2 - Structures / Declarations and Initializations

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00136))_

> The above, once again, prints 9000. This is how many languages behave, including Ruby, Python, Java and C#. Go, and to some degree C#, simply make the fact visible.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00135))_

```
func main() {
  goku := &Saiyan{"Goku", 9000}
  Super(goku)
  fmt.Println(goku.Power)
}
func Super(s *Saiyan) {
  s = &Saiyan{"Gohan", 1000}
}
```


## Related pages

- [[coding-little-go-book-copy]] - shared statements and technical atoms: Copy shares source evidence from Chapter 2 - Structures / Declarations and Initializations: The answer is 9000, not 19000. Why? Because Super made changes to a copy of our original goku value and thus, changes made in Super weren't reflected in the caller. ... [truncated]; Copy shares technical record from Chapter 2 - Structures / Declarations and Initializations: func main() { goku := Saiyan{"Goku", 9000} Super(goku) fmt.Println(goku.Power) } func Super(s Saiyan) { s.Power += 10000 } (1 shared statement(s), 3 shared atom(s))
- [[coding-little-go-book-value]] - shared statements and technical atoms: Value shares source evidence from Chapter 2 - Structures / Declarations and Initializations: The answer is 9000, not 19000. Why? Because Super made changes to a copy of our original goku value and thus, changes made in Super weren't reflected in the caller. ... [truncated]; Value shares technical record from Chapter 2 - Structures / Declarations and Initializations: func main() { goku := Saiyan{"Goku", 9000} Super(goku) fmt.Println(goku.Power) } func Super(s Saiyan) { s.Power += 10000 } (1 shared statement(s), 2 shared atom(s))
- [[coding-little-go-book-language]] - shared technical atoms: Language shares technical record from Introduction: I've always had a love-hate relationship when it comes to learning new languages. (1 shared atom(s))

## Source

- [[coding-little-go-book]]
