---
page_id: coding-little-go-book-variable
page_kind: concept
summary: Variable: 7 statement(s) and 9 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-variable@1de069b91c6c1da562ea8e14e815a884
---

# Variable

What [[coding-little-go-book]] covers about variable:

## Statements

- Environment variables can be set through the Environment Variables button on the Advanced tab of the System control panel. _(coding_little_go_book.pdf (source-range-773b6275-00030))_
- Many times though, we don't want a variable that is directly associated with our value but rather a variable that has a pointer to our value. _(coding_little_go_book.pdf (source-range-773b6275-00127))_
- Some variables, when created, have an easy-to-define life. _(coding_little_go_book.pdf (source-range-773b6275-00046))_
- The most explicit way to deal with variable declaration and assignment in Go is also the most verbose: _(coding_little_go_book.pdf (source-range-773b6275-00075))_
- Because a variable can't be declared twice (not in the same scope anyway). _(coding_little_go_book.pdf (source-range-773b6275-00083))_
- If you read the error message closely, you'll notice that variables is plural. _(coding_little_go_book.pdf (source-range-773b6275-00086))_
- As long as one of the variables is new, := can be used. _(coding_little_go_book.pdf (source-range-773b6275-00088))_

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
