---
page_id: coding-little-go-book-function-declaration
page_kind: concept
summary: Function Declarations: 5 statement(s) and 4 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-function-declaration@0c5eaffc059686f4b06355c0c9616bc5
---

# Function Declarations

What [[coding-little-go-book]] covers about function declarations:

## Statements

- This is a good time to point out that functions can return multiple values. _(coding_little_go_book.pdf (source-range-773b6275-00096))_
- _ , the blank identifier, is special in that the return value isn't actually assigned. _(coding_little_go_book.pdf (source-range-773b6275-00102))_
- This lets you use _ over and over again regardless of the returned type. _(coding_little_go_book.pdf (source-range-773b6275-00102))_
- This is more than a convention. _(coding_little_go_book.pdf (source-range-773b6275-00102))_
- You'll also frequently use _ to discard a value. _(coding_little_go_book.pdf (source-range-773b6275-00105))_

## Technical atoms

```
func log(message string) {
}
func add(a int, b int) int {
}
func power(name string) (int, bool) {
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00097))_

```
value, exists := power("goku")
if exists == false {
  // handle this error case
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00099))_

> Context: Sometimes, you only care about one of the return values. In these cases, you assign the other values to _ :
_(context: coding_little_go_book.pdf (source-range-773b6275-00100))_

```
_, exists := power("goku")
if exists == false {
  // handle this error case
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00101))_

> Context: Finally, there's something else that you're likely to run into with function declarations. If parameters share the same type, we can use a shorter syntax:
_(context: coding_little_go_book.pdf (source-range-773b6275-00103))_

```
func add(a, b int) int {
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00104))_


## Source

- [[coding-little-go-book]]
