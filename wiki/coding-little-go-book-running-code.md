---
page_id: coding-little-go-book-running-code
page_kind: concept
summary: Running Go Code: 8 statement(s) and 3 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-29
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-running-code@3d0f5a89f3f691810e7f91db98dd5e6c
---

# Running Go Code

What [[coding-little-go-book]] covers about running go code:

## Statements

### Chapter 1 - The Basics / Running Go Code

- Save the file as main.go . For now, you can save it anywhere you want; we don't need to live inside Go's workspace for trivial examples. _(coding_little_go_book.pdf (source-range-23d24eb1-00051))_

- Next, open a shell/command prompt and change the directory to where you saved the file. For me, that means typing cd ~/code . _(coding_little_go_book.pdf (source-range-23d24eb1-00052))_

- go run main.go If everything worked, you should see it's over 9000! . But wait, what about the compilation step? go run is a handy command that compiles and runs your code. It uses a temporary directory to build the program, executes it and then cleans itself up. You can see the location of the temporary file by running: go run --work main.go To explicitly compile code, use go build : go build main.go This will generate an executable main which you can run. On Linux / OSX, don't forget that you need to prefix the executable with dotslash, so you need to type ./main . While developing, you can use either go run or go build . When you deploy your code however, you'll want to deploy a binary via go build and execute that. _(coding_little_go_book.pdf (source-range-23d24eb1-00054))_


## Technical atoms

### Technical frame 1: Chapter 1 - The Basics / Running Go Code

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00051))_

> Save the file as main.go . For now, you can save it anywhere you want; we don't need to live inside Go's workspace for trivial examples.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00050))_

```
package main
func main() {
  println("it's over 9000!")
}
```

### Technical frame 2: Chapter 1 - The Basics / Running Go Code

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00052))_

> Next, open a shell/command prompt and change the directory to where you saved the file. For me, that means typing cd ~/code .

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00054))_

> go run main.go If everything worked, you should see it's over 9000!

### Technical frame 3: Chapter 1 - The Basics / Running Go Code / Main

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00056))_

> If you want, you can alter the code and change the package name.


## Related pages

- [[coding-little-go-book-basic]] - shared statements and technical atoms: The Basics shares source evidence from Chapter 1 - The Basics / Running Go Code: Save the file as main.go . For now, you can save it anywhere you want; we don't need to live inside Go's workspace for trivial examples.; The Basics shares technical record from Chapter 1 - The Basics / Running Go Code: package main func main() { println("it's over 9000!") } (8 shared statement(s), 3 shared atom(s))
- [[coding-little-go-book-section-chapter-1-the-basics-running-go-code-f8398d4c]] - source section: Chapter 1 - The Basics / Running Go Code shares source evidence from Chapter 1 - The Basics / Running Go Code: Save the file as main.go . For now, you can save it anywhere you want; we don't need to live inside Go's workspace for trivial examples.; Chapter 1 - The Basics / Running Go Code shares technical record from Chapter 1 - The Basics / Running Go Code: package main func main() { println("it's over 9000!") } (8 shared statement(s), 3 shared atom(s))

## Source

- [[coding-little-go-book]]
