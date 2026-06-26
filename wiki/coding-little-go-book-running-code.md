---
page_id: coding-little-go-book-running-code
page_kind: concept
summary: Running Go Code: 8 statement(s) and 1 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-running-code@ed724b080bf950cd67fd4e0e44aded25
---

# Running Go Code

What [[coding-little-go-book]] covers about running go code:

## Statements

- For me, that means typing cd ~/code . _(coding_little_go_book.pdf (source-range-773b6275-00052))_
- go run is a handy command that compiles and runs your code. _(coding_little_go_book.pdf (source-range-773b6275-00054))_
- You can see the location of the temporary file by running: go run --work main.go To explicitly compile code, use go build : go build main.go This will generate an executable main which you can run. _(coding_little_go_book.pdf (source-range-773b6275-00054))_
- For now, you can save it anywhere you want; we don't need to live inside Go's workspace for trivial examples. _(coding_little_go_book.pdf (source-range-773b6275-00051))_
- Next, open a shell/command prompt and change the directory to where you saved the file. _(coding_little_go_book.pdf (source-range-773b6275-00052))_
- It uses a temporary directory to build the program, executes it and then cleans itself up. _(coding_little_go_book.pdf (source-range-773b6275-00054))_
- While developing, you can use either go run or go build . _(coding_little_go_book.pdf (source-range-773b6275-00054))_
- On Linux / OSX, don't forget that you need to prefix the executable with dotslash, so you need to type ./main . _(coding_little_go_book.pdf (source-range-773b6275-00054))_

## Technical atoms

> Context: Let's start our journey by creating a simple program and learning how to compile and execute it. Open your favorite text editor and write the following code: Next, open a shell/command prompt and change the directory to where you saved the file. For me, that means typing cd ~/code .
_(context: coding_little_go_book.pdf (source-range-773b6275-00049, source-range-773b6275-00052))_

```
package main
func main() {
  println("it's over 9000!")
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00050))_


## Source

- [[coding-little-go-book]]
