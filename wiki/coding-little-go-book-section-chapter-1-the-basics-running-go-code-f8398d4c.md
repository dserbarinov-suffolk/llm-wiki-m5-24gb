---
page_id: coding-little-go-book-section-chapter-1-the-basics-running-go-code-f8398d4c
page_kind: source
summary: Chapter 1 - The Basics / Running Go Code: 15 source-backed entries and 4 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-29
domain: coding-little-go-book
category_path: sources/coding-little-go-book/sections
source_id: coding_little_go_book.pdf
projection_coverage: section-coding-little-go-book-section-chapter-1-the-basics-running-go-code-f8398d4c@3923cc4450a52c87717407381d0e63ff
---

# Chapter 1 - The Basics / Running Go Code

From [[coding-little-go-book]].

## Related pages

- [[coding-little-go-book-section-chapter-1-the-basics-45e21143]] - broader source section: Chapter 1 - The Basics
- [[coding-little-go-book-section-chapter-1-the-basics-running-go-code-main-dad68427]] - narrower source section: Chapter 1 - The Basics / Running Go Code / Main
- [[coding-little-go-book-section-chapter-1-the-basics-garbage-collected-538d2af8]] - previous source section: Chapter 1 - The Basics / Garbage Collected
- [[coding-little-go-book-section-chapter-1-the-basics-imports-2cc727c8]] - next source section: Chapter 1 - The Basics / Imports
- [[coding-little-go-book-running-code]] - topic hub: opens the topic page for Running Code

## Statements

- Save the file as main.go . For now, you can save it anywhere you want; we don't need to live inside Go's workspace for trivial examples. _(coding_little_go_book.pdf (source-range-23d24eb1-00051))_
- Next, open a shell/command prompt and change the directory to where you saved the file. For me, that means typing cd ~/code . _(coding_little_go_book.pdf (source-range-23d24eb1-00052))_
- go run main.go If everything worked, you should see it's over 9000! . But wait, what about the compilation step? go run is a handy command that compiles and runs your code. It uses a temporary directory to build the program, executes it and then cleans itself up. You can see the location of the temporary file by running: go run --work main.go To explicitly compile code, use go build : go build main.go This will generate an executable main which you can run. On Linux / OSX, don't forget that you need to prefix the executable with dotslash, so you need to type ./main . While developing, you can use either go run or go build . When you deploy your code however, you'll want to deploy a binary via go build and execute that. _(coding_little_go_book.pdf (source-range-23d24eb1-00054))_
- For now, you can save it anywhere you want; we don't need to live inside Go's workspace for trivial examples. _(coding_little_go_book.pdf (source-range-23d24eb1-00051))_
- For me, that means typing cd ~/code . _(coding_little_go_book.pdf (source-range-23d24eb1-00052))_
- It uses a temporary directory to build the program, executes it and then cleans itself up. _(coding_little_go_book.pdf (source-range-23d24eb1-00054))_

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

### Technical frame 4: Chapter 1 - The Basics / Running Go Code / Main

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00056))_

> Hopefully, the code that we just executed is understandable. We've created a function and printed out a string with the built-in println function. Did go run know what to execute because there was only a single choice? No. In Go, the entry point to a program has to be a function called main within a package main . We'll talk more about packages in a later chapter. For now, while we focus on understanding the basics of Go, we'll always write our code within the main package. If you want, you can alter the code and change the package name. Run the code via go run and you should get an error. Then, change the name back to main but use a different function name. You should see a different error message. Try making those same changes but use go build instead. Notice that the code compiles, there's just no entry point to run it. This is perfectly normal when you are, for example, building a library.
