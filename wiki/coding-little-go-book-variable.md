---
page_id: coding-little-go-book-variable
page_kind: concept
summary: Variable: 11 statement(s) and 8 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-variable@7dfe43785e10ecef0e102b33682f0576
---

# Variable

What [[coding-little-go-book]] covers about variable:

## Statements

- This means that when we first declare a variable, we use := but on subsequent assignment, we use the assignment operator = . _(coding_little_go_book.pdf (source-range-773b6275-00085))_
- The most explicit way to deal with variable declaration and assignment in Go is also the most verbose: _(coding_little_go_book.pdf (source-range-773b6275-00075))_
- Because a variable can't be declared twice (not in the same scope anyway). _(coding_little_go_book.pdf (source-range-773b6275-00083))_
- If you read the error message closely, you'll notice that variables is plural. _(coding_little_go_book.pdf (source-range-773b6275-00086))_
- As long as one of the variables is new, := can be used. _(coding_little_go_book.pdf (source-range-773b6275-00088))_
- Go has a handy short variable declaration operator, := , which can infer the type: _(coding_little_go_book.pdf (source-range-773b6275-00079))_
- It's important that you remember that := is used to declare the variable as well as assign a value to it. _(coding_little_go_book.pdf (source-range-773b6275-00083))_
- The compiler will complain with no new variables on left side of := . _(coding_little_go_book.pdf (source-range-773b6275-00085))_
- Although power is being used twice with := , the compiler won't complain the second time we use it, it'll see that the other variable, name , is a new variable and allow := . _(coding_little_go_book.pdf (source-range-773b6275-00090))_
- For now, the last thing to know is that, like imports, Go won't let you have unused variables. _(coding_little_go_book.pdf (source-range-773b6275-00091))_
- For now, remember that you'll use var NAME TYPE when declaring a variable to its zero value, NAME := VALUE when declaring and assigning a value, and NAME = VALUE when assigning to a previously declared variable. _(coding_little_go_book.pdf (source-range-773b6275-00094))_

## Technical atoms

> Context: The most explicit way to deal with variable declaration and assignment in Go is also the most verbose:
_(context: coding_little_go_book.pdf (source-range-773b6275-00075))_

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
_(source: coding_little_go_book.pdf (source-range-773b6275-00076))_

> Context: Here, we declare a variable power of type int . By default, Go assigns a zero value to variables. Integers are assigned 0 , booleans false , strings "" and so on. Next, we assign 9000 to our power variable. We can merge the first two lines:
_(context: coding_little_go_book.pdf (source-range-773b6275-00077))_

```
var power int = 9000
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00078))_

> Context: Still, that's a lot of typing. Go has a handy short variable declaration operator, := , which can infer the type:
_(context: coding_little_go_book.pdf (source-range-773b6275-00079))_

```
power := 9000
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00080))_

> Context: This is handy, and it works just as well with functions: It's important that you remember that := is used to declare the variable as well as assign a value to it. Why? Because a variable can't be declared twice (not in the same scope anyway). If you try to run the following, you'll get an error.
_(context: coding_little_go_book.pdf (source-range-773b6275-00081, source-range-773b6275-00083))_

```
func main() {
  power := getPower()
}
func getPower() int {
  return 9001
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00082))_

> Context: It's important that you remember that := is used to declare the variable as well as assign a value to it. Why? Because a variable can't be declared twice (not in the same scope anyway). If you try to run the following, you'll get an error. If you read the error message closely, you'll notice that variables is plural. That's because Go lets you assign multiple variables (using either = or := ):
_(context: coding_little_go_book.pdf (source-range-773b6275-00083, source-range-773b6275-00086))_

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
_(source: coding_little_go_book.pdf (source-range-773b6275-00084))_

> Context: If you read the error message closely, you'll notice that variables is plural. That's because Go lets you assign multiple variables (using either = or := ):
_(context: coding_little_go_book.pdf (source-range-773b6275-00086))_

```
func main() {
  name, power := "Goku", 9000
  fmt.Printf("%s's power is over %d\n", name, power)
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00087))_


## Source

- [[coding-little-go-book]]
