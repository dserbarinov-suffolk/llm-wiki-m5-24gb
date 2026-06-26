---
page_id: coding-little-go-book-section-running-go-code-6d16a5d0
page_kind: source
summary: Running Go Code: 13 source-backed entries and 2 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: sources/coding-little-go-book/sections
source_id: coding_little_go_book.pdf
projection_coverage: section-coding-little-go-book-section-running-go-code-6d16a5d0@fcc606f0b33d894e549beaf131633ae9
---

# Running Go Code

From [[coding-little-go-book]].

## Statements

- For now, you can save it anywhere you want; we don't need to live inside Go's workspace for trivial examples. _(coding_little_go_book.pdf (source-range-810ce361-00051))_
- For now, you can save it anywhere you want; we don't need to live inside Go's workspace for trivial examples. _(coding_little_go_book.pdf (source-range-810ce361-00051))_
- Next, open a shell/command prompt and change the directory to where you saved the file. _(coding_little_go_book.pdf (source-range-810ce361-00052))_
- For me, that means typing cd ~/code . _(coding_little_go_book.pdf (source-range-810ce361-00052))_
- For me, that means typing cd ~/code . _(coding_little_go_book.pdf (source-range-810ce361-00052))_
- go run is a handy command that compiles and runs your code. _(coding_little_go_book.pdf (source-range-810ce361-00054))_
- You can see the location of the temporary file by running: go run --work main.go To explicitly compile code, use go build : go build main.go This will generate an executable main which you can run. _(coding_little_go_book.pdf (source-range-810ce361-00054))_
- On Linux / OSX, don't forget that you need to prefix the executable with dotslash, so you need to type ./main . _(coding_little_go_book.pdf (source-range-810ce361-00054))_
- While developing, you can use either go run or go build . _(coding_little_go_book.pdf (source-range-810ce361-00054))_
- It uses a temporary directory to build the program, executes it and then cleans itself up. _(coding_little_go_book.pdf (source-range-810ce361-00054))_
- It uses a temporary directory to build the program, executes it and then cleans itself up. _(coding_little_go_book.pdf (source-range-810ce361-00054))_

## Technical atoms

```
package main func main()	{ println("it's	over	9000!") }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00050))_

> go run main.go If everything worked, you should see it's over 9000!
_(source: coding_little_go_book.pdf (source-range-810ce361-00054))_
