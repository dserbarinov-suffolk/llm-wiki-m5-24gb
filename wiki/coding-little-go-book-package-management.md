---
page_id: coding-little-go-book-package-management
page_kind: concept
summary: Package Management: 25 statement(s) and 18 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-package-management@a420bc658ba0c27da0a0b77ada405e01
---

# Package Management

What [[coding-little-go-book]] covers about package management:

## Statements

- Go is strict about importing packages. _(coding_little_go_book.pdf (source-range-810ce361-00065))_
- In fact, it isn't tied to resource management only. _(coding_little_go_book.pdf (source-range-810ce361-00394))_
- It will not compile if you import a package but don't use it. _(coding_little_go_book.pdf (source-range-810ce361-00065))_
- For now, knowing how to import and use a package is a good start. _(coding_little_go_book.pdf (source-range-810ce361-00064))_
- In a way, our own source code becomes a Gemfile or package.json . _(coding_little_go_book.pdf (source-range-810ce361-00314))_
- defer is an unusual but practical approach to resource management. _(coding_little_go_book.pdf (source-range-810ce361-00394))_
- To solve this, you can use a third-party dependency management tool. _(coding_little_go_book.pdf (source-range-810ce361-00317))_
- We just talked about how to import packages that live in our workspace. _(coding_little_go_book.pdf (source-range-810ce361-00310))_
- Notice that the name of the package is the same as the name of the folder. _(coding_little_go_book.pdf (source-range-810ce361-00277))_
- If you're building a package, you don't need anything more than what we've seen. _(coding_little_go_book.pdf (source-range-810ce361-00281))_
- Item no longer exists in the db package; it's been moved to the shopping package. _(coding_little_go_book.pdf (source-range-810ce361-00290))_
- You've probably noticed we prefix the function name with the package, e.g., fmt.Println . _(coding_little_go_book.pdf (source-range-810ce361-00064))_
- Go uses a simple rule to define what types and functions are visible outside of a package. _(coding_little_go_book.pdf (source-range-810ce361-00299))_
- The io package has a handful of popular ones such as io.Reader , io.Writer , and io.Closer . _(coding_little_go_book.pdf (source-range-810ce361-00329))_

## Technical atoms

```
package main func main()	{ println("it's	over	9000!") }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00050))_

> For now, while we focus on understanding the basics of Go, we'll always write our code within the main package.
_(source: coding_little_go_book.pdf (source-range-810ce361-00056))_

> Hopefully, the code that we just executed is understandable. We've created a function and printed out a string with the built-in println function. Did go run know what to execute because there was only a single choice? No. In Go, the entry point to a program has to be a function called main within a package main . We'll talk more about packages in a later chapter. For now, while we focus on understanding the basics of Go, we'll always write our code within the main package. If you want, you can alter the code and change the package name. Run the code via go run and you should get an error. Then, change the name back to main but use a different function name. You should see a different error message. Try making those same changes but use go build instead. Notice that the code compiles, there's just no entry point to run it. This is perfectly normal when you are, for example, building a library.
_(source: coding_little_go_book.pdf (source-range-810ce361-00056))_

```
package main import ( "fmt" "os" ) func main()	{ }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00066))_

```
package main import ( "fmt" ) func main()	{ var power	int power	=	9000 fmt.Printf("It's	over	%d\n",	power) }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00076))_

> To keep more complicated libraries and systems organized, we need to learn about packages. In Go, package names follow the directory structure of your Go workspace. If we were building a shopping system, we'd probably start with a package name "shopping" and put our source files in $GOPATH/src/shopping/ . We don't want to put everything inside this folder though. For example, maybe we want to isolate some database logic inside its own folder. To achieve this, we create a subfolder at $GOPATH/src/shopping/db . The package name of the files within this subfolder is simply db , but to access it from another package, including the shopping package, we need to import shopping/db . In other words, when you name a package, via the package keyword, you provide a single value, not a complete hierarchy (e.g., "shopping" or "db"). When you import a package, you specify the complete path. Let's try it. Inside your Go workspace's src folder (which we set up in Getting Started of the Introduction), create a new folder called shopping and a subfolder within it called db . Inside of shopping/db , create a file called db.go and add the following code:
_(source: coding_little_go_book.pdf (source-range-810ce361-00274))_


## Source

- [[coding-little-go-book]]
