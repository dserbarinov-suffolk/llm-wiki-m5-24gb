---
page_id: coding-little-go-book-section-chapter-1-the-basics-running-go-code-f8398d4c
page_kind: source
summary: Chapter 1 - The Basics / Running Go Code: 15 source-backed entries and 0 atom(s) from raw/coding_little_go_book.pdf.
page_family: section-reference
sources: raw/coding_little_go_book.pdf
updated: 2026-06-30
domain: coding-little-go-book
category_path: sources/coding-little-go-book/sections
source_id: coding_little_go_book.pdf
projection_coverage: section-coding-little-go-book-section-chapter-1-the-basics-running-go-code-f8398d4c@2aee85cdb1e3013be27690babbc975bc
---

# Chapter 1 - The Basics / Running Go Code

From [[coding-little-go-book]].

## Related pages

- [[coding-little-go-book-section-chapter-1-the-basics-45e21143]] - broader source section: Chapter 1 - The Basics
- [[coding-little-go-book-section-chapter-1-the-basics-running-go-code-main-dad68427]] - narrower source section: Chapter 1 - The Basics / Running Go Code / Main
- [[coding-little-go-book-section-chapter-1-the-basics-garbage-collected-538d2af8]] - previous source section: Chapter 1 - The Basics / Garbage Collected
- [[coding-little-go-book-section-chapter-1-the-basics-imports-2cc727c8]] - next source section: Chapter 1 - The Basics / Imports

## Statements

- Save the file as main.go . For now, you can save it anywhere you want; we don't need to live inside Go's workspace for trivial examples. _(coding_little_go_book.pdf (source-range-23d24eb1-00051))_
- Next, open a shell/command prompt and change the directory to where you saved the file. For me, that means typing cd ~/code . _(coding_little_go_book.pdf (source-range-23d24eb1-00052))_
- go run main.go If everything worked, you should see it's over 9000! . But wait, what about the compilation step? go run is a handy command that compiles and runs your code. It uses a temporary directory to build the program, executes it and then cleans itself up. You can see the location of the temporary file by running: go run --work main.go To explicitly compile code, use go build : go build main.go This will generate an executable main which you can run. On Linux / OSX, don't forget that you need to prefix the executable with dotslash, so you need to type ./main . While developing, you can use either go run or go build . When you deploy your code however, you'll want to deploy a binary via go build and execute that. _(coding_little_go_book.pdf (source-range-23d24eb1-00054))_
- For now, you can save it anywhere you want; we don't need to live inside Go's workspace for trivial examples. _(coding_little_go_book.pdf (source-range-23d24eb1-00051))_
- For me, that means typing cd ~/code . _(coding_little_go_book.pdf (source-range-23d24eb1-00052))_
- It uses a temporary directory to build the program, executes it and then cleans itself up. _(coding_little_go_book.pdf (source-range-23d24eb1-00054))_
