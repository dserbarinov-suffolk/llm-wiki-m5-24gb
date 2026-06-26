---
page_id: coding-little-go-book-change
page_kind: concept
summary: Change: 4 statement(s) and 5 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-change@4ee5720987f787e108ba785c737decaa
---

# Change

What [[coding-little-go-book]] covers about change:

## Statements

- Though the changes are often incremental, they tend to have a wide scope and they impact productivity, readability, performance, testability, dependency management, error handling, documentation, profiling, communities, standard libraries, and so on. _(coding_little_go_book.pdf (source-range-773b6275-00013))_
- Next, open a shell/command prompt and change the directory to where you saved the file. _(coding_little_go_book.pdf (source-range-773b6275-00052))_
- Because Super made changes to a copy of our original goku value and thus, changes made in Super weren't reflected in the caller. _(coding_little_go_book.pdf (source-range-773b6275-00130))_
- On the one hand, it's a pretty slight syntactical change; on the other, it does feel a little less compartmentalized. _(coding_little_go_book.pdf (source-range-773b6275-00147))_

## Technical atoms

> Context: That said, we have to move forward. We have to be willing to take incremental steps because, again, languages are the foundation of what we do. Though the changes are often incremental, they tend to have a wide scope and they impact productivity, readability, performance, testability, dependency management, error handling, documentation, profiling, communities, standard libraries, and so on. Is there a positive way to say death by a thousand cuts ?
_(context: coding_little_go_book.pdf (source-range-773b6275-00013))_

> I've always had a love-hate relationship when it comes to learning new languages.
_(source: coding_little_go_book.pdf (source-range-773b6275-00012))_

> Context: Let's start our journey by creating a simple program and learning how to compile and execute it. Open your favorite text editor and write the following code: Next, open a shell/command prompt and change the directory to where you saved the file. For me, that means typing cd ~/code .
_(context: coding_little_go_book.pdf (source-range-773b6275-00049, source-range-773b6275-00052))_

```
package main
func main() {
  println("it's over 9000!")
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00050))_

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

> Context: We can prove that it's a copy by trying to change where it points to (not something you'd likely want to actually do): The above, once again, prints 9000. This is how many languages behave, including Ruby, Python, Java and C#. Go, and to some degree C#, simply make the fact visible.
_(context: coding_little_go_book.pdf (source-range-773b6275-00134, source-range-773b6275-00136))_

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
_(source: coding_little_go_book.pdf (source-range-773b6275-00135))_


## Source

- [[coding-little-go-book]]
