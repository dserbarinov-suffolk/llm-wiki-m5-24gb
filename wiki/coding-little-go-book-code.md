---
page_id: coding-little-go-book-code
page_kind: concept
summary: Code: 26 statement(s) and 27 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-code@6974d47453dbcaf549715297d87b3c0a
---

# Code

What [[coding-little-go-book]] covers about code:

## Statements

- For me, that means typing cd ~/code . _(coding_little_go_book.pdf (source-range-810ce361-00052))_
- To solve this, we need to coordinate our code. _(coding_little_go_book.pdf (source-range-810ce361-00405))_
- Strings are made of runes which are unicode code points. _(coding_little_go_book.pdf (source-range-810ce361-00382))_
- go run is a handy command that compiles and runs your code. _(coding_little_go_book.pdf (source-range-810ce361-00054))_
- You can click on that section header and see the source code. _(coding_little_go_book.pdf (source-range-810ce361-00067))_
- We're just using this as an example to show how to organize code. _(coding_little_go_book.pdf (source-range-810ce361-00276))_
- In a way, our own source code becomes a Gemfile or package.json . _(coding_little_go_book.pdf (source-range-810ce361-00313))_
- Goroutines effectively abstract what's needed to run concurrent code. _(coding_little_go_book.pdf (source-range-810ce361-00467))_
- First of all, it isn't always so obvious what code needs to be protected. _(coding_little_go_book.pdf (source-range-810ce361-00417))_
- Beyond this, Go gives us a simple but effective way to organize our code. _(coding_little_go_book.pdf (source-range-810ce361-00473))_
- For whatever reason, our crashing code wanted to set the element at index 7. _(coding_little_go_book.pdf (source-range-810ce361-00210))_
- copy is one of those functions that highlights how slices change the way we code. _(coding_little_go_book.pdf (source-range-810ce361-00243))_
- In the above code, we say that the type *Saiyan is the receiver of the Super method. _(coding_little_go_book.pdf (source-range-810ce361-00141))_
- Slices are powerful and they have a surprisingly large impact on the clarity of your code. _(coding_little_go_book.pdf (source-range-810ce361-00269))_

## Code, rules, and examples

> If you're looking to play a little with Go, you should check out the Go Playground which lets you run code online without having to install anything.
_(source: coding_little_go_book.pdf (source-range-810ce361-00023))_

> If you're looking to play a little with Go, you should check out the Go Playground which lets you run code online without having to install anything. This is also the most common way to share Go code when seeking help in Go's discussion forum and places like StackOverflow. Installing Go is straightforward. You can install it from source, but I suggest you use one of the pre-compiled binaries. When you go to the download page, you'll see installers for various platforms. Let's avoid these and learn how to set up Go ourselves. As you'll see, it isn't hard. Except for simple examples, Go is designed to work when your code is inside a workspace. The workspace is a folder composed of bin , pkg and src subfolders. You might be tempted to force Go to follow your own style - don't. Normally, I put my projects inside of ~/code . For example, ~/code/blog contains my blog. For Go, my workspace is ~/code/go and my Gopowered blog would be in ~/code/go/src/blog . In short, create a go folder with a src subfolder wherever you expect
_(source: coding_little_go_book.pdf (source-range-810ce361-00023))_

> Hopefully, the code that we just executed is understandable. We've created a function and printed out a string with the built-in println function. Did go run know what to execute because there was only a single choice? No. In Go, the entry point to a program has to be a function called main within a package main . We'll talk more about packages in a later chapter. For now, while we focus on understanding the basics of Go, we'll always write our code within the main package. If you want, you can alter the code and change the package name. Run the code via go run and you should get an error. Then, change the name back to main but use a different function name. You should see a different error message. Try making those same changes but use go build instead. Notice that the code compiles, there's just no entry point to run it. This is perfectly normal when you are, for example, building a library.
_(source: coding_little_go_book.pdf (source-range-810ce361-00056))_

> Whichever approach you choose, if you follow the factory pattern above, you can shield the rest of your code from knowing and worrying about any of the allocation details.
_(source: coding_little_go_book.pdf (source-range-810ce361-00154))_

> As you write Go code, it's natural to ask yourself should this be a value, or a pointer to a value?
_(source: coding_little_go_book.pdf (source-range-810ce361-00173))_

> This changes how you code. For example, a number of functions take a position parameter. In JavaScript, if we want to find the first space in a string (yes, slices work on strings too!) after the first five characters, we'd write:
_(source: coding_little_go_book.pdf (source-range-810ce361-00234))_


## Source

- [[coding-little-go-book]]
