---
page_id: coding-little-go-book-variable-and-declaration
page_kind: concept
summary: Variables and Declarations: 18 statement(s) and 9 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-29
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-variable-and-declaration@85423cb705bce2b8b1c272334c302c42
---

# Variables and Declarations

What [[coding-little-go-book]] covers about variables and declarations:

## Statements

### Chapter 1 - The Basics / Variables and Declarations

- It'd be nice to begin and end our look at variables by saying you declare and assign to a variable by doing x = 4. Unfortunately, things are more complicated in Go. We'll begin our conversation by looking at simple examples. Then, in the next chapter, we'll expand this when we look at creating and using structures. Still, it'll probably take some time before you truly feel comfortable with it. _(coding_little_go_book.pdf (source-range-23d24eb1-00073))_

- You might be thinking Woah! What can be so complicated about this? Let's start looking at some examples. _(coding_little_go_book.pdf (source-range-23d24eb1-00074))_

- The most explicit way to deal with variable declaration and assignment in Go is also the most verbose: _(coding_little_go_book.pdf (source-range-23d24eb1-00075))_

- Here, we declare a variable power of type int . By default, Go assigns a zero value to variables. Integers are assigned 0 , booleans false , strings "" and so on. Next, we assign 9000 to our power variable. We can merge the first two lines: _(coding_little_go_book.pdf (source-range-23d24eb1-00077))_

- Still, that's a lot of typing. Go has a handy short variable declaration operator, := , which can infer the type: _(coding_little_go_book.pdf (source-range-23d24eb1-00079))_

- It's important that you remember that := is used to declare the variable as well as assign a value to it. Why? Because a variable can't be declared twice (not in the same scope anyway). If you try to run the following, you'll get an error. _(coding_little_go_book.pdf (source-range-23d24eb1-00083))_

- The compiler will complain with no new variables on left side of := . This means that when we first declare a variable, we use := but on subsequent assignment, we use the assignment operator = . This makes a lot of sense, but it can be tricky for your muscle memory to remember when to switch between the two. _(coding_little_go_book.pdf (source-range-23d24eb1-00085))_

- If you read the error message closely, you'll notice that variables is plural. That's because Go lets you assign multiple variables (using either = or := ): _(coding_little_go_book.pdf (source-range-23d24eb1-00086))_

- As long as one of the variables is new, := can be used. Consider: _(coding_little_go_book.pdf (source-range-23d24eb1-00088))_

- Although power is being used twice with := , the compiler won't complain the second time we use it, it'll see that the other variable, name , is a new variable and allow := . However, you can't change the type of power . It was declared (implicitly) as an integer and thus, can only be assigned integers. _(coding_little_go_book.pdf (source-range-23d24eb1-00090))_

- For now, the last thing to know is that, like imports, Go won't let you have unused variables. For example, _(coding_little_go_book.pdf (source-range-23d24eb1-00091))_

- won't compile because name is declared but not used. Like unused imports it'll cause some frustration, but overall I think it helps with code cleanliness and readability. _(coding_little_go_book.pdf (source-range-23d24eb1-00093))_

- There's more to learn about declaration and assignments. For now, remember that you'll use var NAME TYPE when declaring a variable to its zero value, NAME := VALUE when declaring and assigning a value, and NAME = VALUE when assigning to a previously declared variable. _(coding_little_go_book.pdf (source-range-23d24eb1-00094))_


## Technical atoms

### Technical frame 1: Chapter 1 - The Basics / Variables and Declarations

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00077))_

> Here, we declare a variable power of type int . By default, Go assigns a zero value to variables. Integers are assigned 0 , booleans false , strings "" and so on. Next, we assign 9000 to our power variable. We can merge the first two lines:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00076))_

```
package main
import (
  "fmt"
)
func main() {
  var power int
  power = 9000
  fmt.Printf("It's over %d\n", power)
}
```

### Technical frame 2: Chapter 1 - The Basics / Variables and Declarations

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00079))_

> Still, that's a lot of typing. Go has a handy short variable declaration operator, := , which can infer the type:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00078))_

```
var power int = 9000
```

### Technical frame 3: Chapter 1 - The Basics / Variables and Declarations

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00083))_

> It's important that you remember that := is used to declare the variable as well as assign a value to it. Why? Because a variable can't be declared twice (not in the same scope anyway). If you try to run the following, you'll get an error.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00080))_

```
power := 9000
```

### Technical frame 4: Chapter 1 - The Basics / Variables and Declarations

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00083))_

> It's important that you remember that := is used to declare the variable as well as assign a value to it. Why? Because a variable can't be declared twice (not in the same scope anyway). If you try to run the following, you'll get an error.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00082))_

```
func main() {
  power := getPower()
}
func getPower() int {
  return 9001
}
```

### Technical frame 5: Chapter 1 - The Basics / Variables and Declarations

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00085))_

> The compiler will complain with no new variables on left side of := . This means that when we first declare a variable, we use := but on subsequent assignment, we use the assignment operator = . This makes a lot of sense, but it can be tricky for your muscle memory to remember when to switch between the two.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00083))_

> If you try to run the following, you'll get an error.

### Technical frame 6: Chapter 1 - The Basics / Variables and Declarations

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00085))_

> The compiler will complain with no new variables on left side of := . This means that when we first declare a variable, we use := but on subsequent assignment, we use the assignment operator = . This makes a lot of sense, but it can be tricky for your muscle memory to remember when to switch between the two.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00084))_

```
func main() {
  power := 9000
  fmt.Printf("It's over %d\n", power)
// COMPILER ERROR:
  // no new variables on left side of :=
  power := 9001
  fmt.Printf("It's also over %d\n", power)
}
```

### Technical frame 7: Chapter 1 - The Basics / Variables and Declarations

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00088))_

> As long as one of the variables is new, := can be used. Consider:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00087))_

```
func main() {
  name, power := "Goku", 9000
  fmt.Printf("%s's power is over %d\n", name, power)
}
```

### Technical frame 8: Chapter 1 - The Basics / Variables and Declarations

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00090))_

> Although power is being used twice with := , the compiler won't complain the second time we use it, it'll see that the other variable, name , is a new variable and allow := . However, you can't change the type of power . It was declared (implicitly) as an integer and thus, can only be assigned integers.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00089))_

```
func main() {
  power := 1000
  fmt.Printf("default power is %d\n", power)
name, power := "Goku", 9000
  fmt.Printf("%s's power is over %d\n", name, power)
}
```

### Technical frame 9: Chapter 1 - The Basics / Variables and Declarations

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00093))_

> won't compile because name is declared but not used. Like unused imports it'll cause some frustration, but overall I think it helps with code cleanliness and readability.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00092))_

```
func main() {
  name, power := "Goku", 1000
  fmt.Printf("default power is %d\n", power)
}
```


## Related pages

- [[coding-little-go-book-variable]] - broader topic: Variable shares source evidence from Chapter 1 - The Basics / Variables and Declarations: The most explicit way to deal with variable declaration and assignment in Go is also the most verbose:; Variable shares technical record from Chapter 1 - The Basics / Variables and Declarations: package main import ( "fmt" ) func main() { var power int power = 9000 fmt.Printf("It's over %d\n", power) } (11 shared statement(s), 8 shared atom(s))
- [[coding-little-go-book-basic]] - shared statements and technical atoms: The Basics shares source evidence from Chapter 1 - The Basics / Variables and Declarations: It'd be nice to begin and end our look at variables by saying you declare and assign to a variable by doing x = 4. Unfortunately, things are more complicated in Go. ... [truncated]; The Basics shares technical record from Chapter 1 - The Basics / Variables and Declarations: package main import ( "fmt" ) func main() { var power int power = 9000 fmt.Printf("It's over %d\n", power) } (18 shared statement(s), 9 shared atom(s))
- [[coding-little-go-book-section-chapter-1-the-basics-variables-and-declarations-dd932e02]] - source section: Chapter 1 - The Basics / Variables and Declarations shares source evidence from Chapter 1 - The Basics / Variables and Declarations: It'd be nice to begin and end our look at variables by saying you declare and assign to a variable by doing x = 4. Unfortunately, things are more complicated in Go. ... [truncated]; Chapter 1 - The Basics / Variables and Declarations shares technical record from Chapter 1 - The Basics / Variables and Declarations: package main import ( "fmt" ) func main() { var power int power = 9000 fmt.Printf("It's over %d\n", power) } (18 shared statement(s), 9 shared atom(s))

## Source

- [[coding-little-go-book]]
