---
page_id: coding-little-go-book-declaration-and-initialization
page_kind: concept
summary: Declarations and Initializations: 27 statement(s) and 7 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-declaration-and-initialization@d2fe1057afcf360d703b042c118b17d1
---

# Declarations and Initializations

What [[coding-little-go-book]] covers about declarations and initializations:

## Statements

- Because Super made changes to a copy of our original goku value and thus, changes made in Super weren't reflected in the caller. _(coding_little_go_book.pdf (source-range-773b6275-00130))_
- There's obviously some relation between the types Saiyan and *Saiyan , but they are two distinct types. _(coding_little_go_book.pdf (source-range-773b6275-00132))_
- Go, and to some degree C#, simply make the fact visible. _(coding_little_go_book.pdf (source-range-773b6275-00136))_
- When we first looked at variables and declarations, we looked only at built-in types, like integers and strings. _(coding_little_go_book.pdf (source-range-773b6275-00117))_
- Furthermore, you can skip the field name and rely on the order of the field declarations (though for the sake of clarity, you should only do this for structures with few fields): _(coding_little_go_book.pdf (source-range-773b6275-00124))_
- What all of the above examples do is declare a variable goku and assign a value to it. _(coding_little_go_book.pdf (source-range-773b6275-00126))_
- Loosely, it's the difference between being at a house and having directions to the house. _(coding_little_go_book.pdf (source-range-773b6275-00127))_
- This is how many languages behave, including Ruby, Python, Java and C#. _(coding_little_go_book.pdf (source-range-773b6275-00136))_
- It used to expect a value of type Saiyan but now expects an address of type *Saiyan , where *X means pointer to value of type X . _(coding_little_go_book.pdf (source-range-773b6275-00132))_
- Now that we're talking about structures, we need to expand that conversation to include pointers. _(coding_little_go_book.pdf (source-range-773b6275-00117))_
- Note: The trailing , in the above structure is required. _(coding_little_go_book.pdf (source-range-773b6275-00120))_
- Without it, the compiler will give an error. _(coding_little_go_book.pdf (source-range-773b6275-00120))_
- We don't have to set all or even any of the fields. _(coding_little_go_book.pdf (source-range-773b6275-00121))_
- Just like unassigned variables have a zero value, so do fields. _(coding_little_go_book.pdf (source-range-773b6275-00123))_

## Technical atoms

> Context: The simplest way to create a value of our structure is: Note: The trailing , in the above structure is required. Without it, the compiler will give an error. You'll appreciate the required consistency, especially if you've used a language or format that enforces the opposite.
_(context: coding_little_go_book.pdf (source-range-773b6275-00118, source-range-773b6275-00120))_

```
goku := Saiyan{
  Name: "Goku",
  Power: 9000,
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00119))_

> Context: The simplest way to create a value of our structure is:
_(context: coding_little_go_book.pdf (source-range-773b6275-00118))_

> You'll appreciate the required consistency, especially if you've used a language or format that enforces the opposite.
_(source: coding_little_go_book.pdf (source-range-773b6275-00120))_

> Context: We don't have to set all or even any of the fields. Both of these are valid:
_(context: coding_little_go_book.pdf (source-range-773b6275-00121))_

```
goku := Saiyan{}
// or
goku := Saiyan{Name: "Goku"}
goku.Power = 9000
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00122))_

> Context: Furthermore, you can skip the field name and rely on the order of the field declarations (though for the sake of clarity, you should only do this for structures with few fields): What all of the above examples do is declare a variable goku and assign a value to it.
_(context: coding_little_go_book.pdf (source-range-773b6275-00124, source-range-773b6275-00126))_

```
goku := Saiyan{"Goku", 9000}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00125))_

> Context: Why do we want a pointer to the value, rather than the actual value? It comes down to the way Go passes arguments to a function: as copies. Knowing this, what does the following print? The answer is 9000, not 19000. Why? Because Super made changes to a copy of our original goku value and thus, changes made in Super weren't reflected in the caller. To make this work as you probably expect, we need to pass a pointer to our value:
_(context: coding_little_go_book.pdf (source-range-773b6275-00128, source-range-773b6275-00130))_

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
_(source: coding_little_go_book.pdf (source-range-773b6275-00129))_

> Context: The answer is 9000, not 19000. Why? Because Super made changes to a copy of our original goku value and thus, changes made in Super weren't reflected in the caller. To make this work as you probably expect, we need to pass a pointer to our value:
_(context: coding_little_go_book.pdf (source-range-773b6275-00130))_

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
_(source: coding_little_go_book.pdf (source-range-773b6275-00131))_


## Source

- [[coding-little-go-book]]
