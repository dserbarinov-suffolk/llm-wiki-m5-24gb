---
page_id: coding-little-go-book
page_kind: source
summary: Claim-ledger projection (coding): 662 usable entries, 166 technical atoms, 124 needs-review, 92 linked page(s); write decision write-with-review-work.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: sources
source_id: coding_little_go_book.pdf
projection_coverage: projection-coverage-426f8449c3050c6e@e61b2a3deac0058c
---

# The Little Go Book

## The Little Go Book

- About This Book License Latest Version Introduction A Note from the Author Getting Started OSX / Linux Windows Chapter 1 - The Basics Compilation Static Typing C-Like Syntax Garbage Collected Running Go Code Main Imports Variables and Declarations Function Declarations Before You Continue Chapter 2 - Structures Declarations and Initializations Functions on Structures Constructors New Fields of a Structure Composition Overloading Pointers versus Values Before You Continue Chapter 3 - Maps, Arrays and Slices Arrays Slices Maps Pointers versus Values Before You Continue Chapter 4 - Code Organization and Interfaces Packages Cyclical Imports Visibility Package Management Dependency Management Interfaces Before You Continue Chapter 5 - Tidbits Error Handling Defer go fmt Initialized If Empty Interface and Conversions Strings and Byte Arrays Function Type Before You Continue Chapter 6 - Concurrency Goroutines Synchronization Channels Buffered Channels Select Timeout Before You Continue Conclusion _(coding_little_go_book.pdf (source-range-773b6275-00002))_
- About This Book License Latest Version Introduction A Note from the Author Getting Started OSX / Linux Windows Chapter 1 - The Basics Compilation Static Typing C-Like Syntax Garbage Collected Running Go Code Main Imports Variables and Declarations Function Declarations Before You Continue Chapter 2 - Structures Declarations and Initializations Functions on Structures Constructors New Fields of a Structure Composition Overloading Pointers versus Values Before You Continue Chapter 3 - Maps, Arrays and Slices Arrays Slices Maps Pointers versus Values Before You Continue Chapter 4 - Code Organization and Interfaces Packages Cyclical Imports Visibility Package Management Dependency Management Interfaces Before You Continue Chapter 5 - Tidbits Error Handling Defer go fmt Initialized If Empty Interface and Conversions Strings and Byte Arrays Function Type Before You Continue Chapter 6 - Concurrency Goroutines Synchronization Channels Buffered Channels Select Timeout Before You Continue Conclusion _(coding_little_go_book.pdf (source-range-773b6275-00002))_

## About This Book

## License

- You should not have paid for this book. _(coding_little_go_book.pdf (source-range-773b6275-00005))_
- The Little Go Book is licensed under the Attribution-NonCommercialShareAlike 4.0 International license. _(coding_little_go_book.pdf (source-range-773b6275-00005))_
- You are free to copy, distribute, modify or display the book. _(coding_little_go_book.pdf (source-range-773b6275-00006))_
- However, I ask that you always attribute the book to me, Karl Seguin, and do not use it for commercial purposes. _(coding_little_go_book.pdf (source-range-773b6275-00006))_

## Latest Version

## Introduction

- On the downside, language design is fairly incremental. _(coding_little_go_book.pdf (source-range-773b6275-00012))_
- On the one hand, languages are so fundamental to what we do, that even small changes can have measurable impact. _(coding_little_go_book.pdf (source-range-773b6275-00012))_
- Learning new keywords, type system, coding style as well as new libraries, communities and paradigms is a lot of work that seems hard to justify. _(coding_little_go_book.pdf (source-range-773b6275-00012))_
- That aha moment when something clicks can have a lasting effect on how you program and can redefine your expectations of other languages. _(coding_little_go_book.pdf (source-range-773b6275-00012))_
- That said, we have to move forward. _(coding_little_go_book.pdf (source-range-773b6275-00013))_
- We have to be willing to take incremental steps because, again, languages are the foundation of what we do. _(coding_little_go_book.pdf (source-range-773b6275-00013))_
- Though the changes are often incremental, they tend to have a wide scope and they impact productivity, readability, performance, testability, dependency management, error handling, documentation, profiling, communities, standard libraries, and so on. _(coding_little_go_book.pdf (source-range-773b6275-00013))_
- We have to be willing to take incremental steps because, again, languages are the foundation of what we do. _(coding_little_go_book.pdf (source-range-773b6275-00013))_
- For me, there are two compelling reasons. _(coding_little_go_book.pdf (source-range-773b6275-00014))_
- The other reason is that for many developers, it will complement your existing arsenal. _(coding_little_go_book.pdf (source-range-773b6275-00014))_
- The first is that it's a relatively simple language with a relatively simple standard library. _(coding_little_go_book.pdf (source-range-773b6275-00014))_
- In a lot of ways, the incremental nature of Go is to simplify some of the complexity we've seen being added to languages over the last couple of decades. _(coding_little_go_book.pdf (source-range-773b6275-00014))_
- I don't know what label to give it, but over the course of my career, as systems continue to grow in complexity and as concurrency frequently measures in the tens of thousands, there's clearly been a growing need for custom infrastructure-type systems. _(coding_little_go_book.pdf (source-range-773b6275-00016))_
- You can build such systems with Ruby or Python or something else (and many people do), but these types of systems can benefit from a more rigid type system and greater performance. _(coding_little_go_book.pdf (source-range-773b6275-00016))_
- Similarly, you can use Go to build websites (and many people do), but I still prefer, by a wide margin, the expressiveness of Node or Ruby for such systems. _(coding_little_go_book.pdf (source-range-773b6275-00016))_
- For example, there are no dependencies when running a compiled Go program. _(coding_little_go_book.pdf (source-range-773b6275-00017))_
- For this reason, Go is becoming increasingly popular as a language for command-line interface programs and other types of utility programs you need to distribute (e.g., a log collector). _(coding_little_go_book.pdf (source-range-773b6275-00017))_
- There are other areas where Go excels. _(coding_little_go_book.pdf (source-range-773b6275-00017))_
- For example, there are no dependencies when running a compiled Go program. _(coding_little_go_book.pdf (source-range-773b6275-00017))_
- Put plainly, learning Go is an efficient use of your time. _(coding_little_go_book.pdf (source-range-773b6275-00018))_
- You won't have to spend long hours learning or even mastering Go, and you'll end up with something practical from your effort. _(coding_little_go_book.pdf (source-range-773b6275-00018))_

> I've always had a love-hate relationship when it comes to learning new languages.
_(source: coding_little_go_book.pdf (source-range-773b6275-00012))_

> Go was built as a system language (e.g., operating systems, device drivers) and thus aimed at C and C++ developers. According to the Go team, and which is certainly true of me, application developers, not system developers, have become the primary Go users. Why? I can't speak authoritatively for system developers, but for those of us building websites, services, desktop applications and the like, it partially comes down to the emerging need for a class of systems that sit somewhere in between low-level system applications and higherlevel applications.
_(source: coding_little_go_book.pdf (source-range-773b6275-00015))_

> You don't have to worry if your users have Ruby or the JVM installed, and if so, what version.
_(source: coding_little_go_book.pdf (source-range-773b6275-00017))_

## A Note from the Author

- The other is my discomfort at writing a book about a language. _(coding_little_go_book.pdf (source-range-773b6275-00020))_
- With The Little Redis Book, you could assume a familiarity with a key value store and take it from there. _(coding_little_go_book.pdf (source-range-773b6275-00020))_
- I've hesitated writing this book for a couple reasons. _(coding_little_go_book.pdf (source-range-773b6275-00020))_
- When I wrote The Little MongoDB Book, it was safe to assume most readers understood the basics of relational database and modeling. _(coding_little_go_book.pdf (source-range-773b6275-00020))_
- The first is that Go's own documentation, in particular Effective Go, is solid. _(coding_little_go_book.pdf (source-range-773b6275-00020))_

> that I won't be able to make those same assumptions. How much time do you spend talking about interfaces knowing that for some, the concept will be new, while others won't need much more than Go has interfaces ? Ultimately, I take comfort in knowing that you'll let me know if some parts are too shallow or others too detailed. Consider that the price of this book.
_(source: coding_little_go_book.pdf (source-range-773b6275-00021))_

## Getting Started

> If you're looking to play a little with Go, you should check out the Go Playground which lets you run code online without having to install anything. This is also the most common way to share Go code when seeking help in Go's discussion forum and places like StackOverflow. Installing Go is straightforward. You can install it from source, but I suggest you use one of the pre-compiled binaries. When you go to the download page, you'll see installers for various platforms. Let's avoid these and learn how to set up Go ourselves. As you'll see, it isn't hard. Except for simple examples, Go is designed to work when your code is inside a workspace. The workspace is a folder composed of bin , pkg and src subfolders. You might be tempted to force Go to follow your own style - don't. Normally, I put my projects inside of ~/code . For example, ~/code/blog contains my blog. For Go, my workspace is ~/code/go and my Gopowered blog would be in ~/code/go/src/blog . In short, create a go folder with a src subfolder wherever you expect
_(source: coding_little_go_book.pdf (source-range-773b6275-00023))_

> If you're looking to play a little with Go, you should check out the Go Playground which lets you run code online without having to install anything.
_(source: coding_little_go_book.pdf (source-range-773b6275-00023))_

## OSX / Linux

- For OSX, you'll most likely be interested in go#.#.#.darwin-amd64-osx10.8.tar.gz , where #.#.# is the latest version of Go. _(coding_little_go_book.pdf (source-range-773b6275-00026))_
- We need to append Go's binary to our PATH . _(coding_little_go_book.pdf (source-range-773b6275-00026))_
- You can close and reopen your shell, or you can run source $HOME/.profile . _(coding_little_go_book.pdf (source-range-773b6275-00027))_

## Windows

- If you're on an x64 system, you'll want go#.#.#.windows-amd64.zip , where #.#.# is the latest version of Go. _(coding_little_go_book.pdf (source-range-773b6275-00030))_
- That might be something like c:\users\goku\work\go . _(coding_little_go_book.pdf (source-range-773b6275-00030))_
- Environment variables can be set through the Environment Variables button on the Advanced tab of the System control panel. _(coding_little_go_book.pdf (source-range-773b6275-00030))_
- Some versions of Windows provide this control panel through the Advanced System Settings option inside the System control panel. _(coding_little_go_book.pdf (source-range-773b6275-00030))_
- Some versions of Windows provide this control panel through the Advanced System Settings option inside the System control panel. _(coding_little_go_book.pdf (source-range-773b6275-00030))_

## Chapter 1 - The Basics

- Go is a compiled, statically typed language with a C-like syntax and garbage collection. _(coding_little_go_book.pdf (source-range-773b6275-00032))_

## Compilation

- This is good news for people working on large projects as well as those of us used to a quick feedback cycle offered by interpreted languages. _(coding_little_go_book.pdf (source-range-773b6275-00034))_
- Compilation speed is one of the major design goals of Go. _(coding_little_go_book.pdf (source-range-773b6275-00034))_
- Compilation is the process of translating the source code that you write into a lower level language -- either assembly (as is the case with Go), or some other intermediary language (as with Java and C#). _(coding_little_go_book.pdf (source-range-773b6275-00034))_
- Compiled languages can be unpleasant to work with because compilation can be slow. _(coding_little_go_book.pdf (source-range-773b6275-00034))_

> It's hard to iterate quickly if you have to spend minutes or hours waiting for code to compile.
_(source: coding_little_go_book.pdf (source-range-773b6275-00034))_

## Static Typing

- It's true that when you have one, you normally have the other but it isn't a hard rule. _(coding_little_go_book.pdf (source-range-773b6275-00037))_
- This is either achieved by specifying the type when the variable is declared or, in many cases, letting the compiler infer the type (we'll look at examples shortly). _(coding_little_go_book.pdf (source-range-773b6275-00037))_
- If you're used to dynamically typed languages, you might find this cumbersome. _(coding_little_go_book.pdf (source-range-773b6275-00037))_
- The two are often conflated. _(coding_little_go_book.pdf (source-range-773b6275-00037))_
- With a rigid type system, a compiler is able to detect problems beyond mere syntactical mistakes as well as make further optimizations. _(coding_little_go_book.pdf (source-range-773b6275-00037))_
- You're not wrong, but there are advantages, especially when you pair static typing with compilation. _(coding_little_go_book.pdf (source-range-773b6275-00037))_
- Being statically typed means that variables must be of a specific type (int, string, bool, []byte, etc.). _(coding_little_go_book.pdf (source-range-773b6275-00037))_

## C-Like Syntax

- Saying that a language has a C-like syntax means that if you're used to any other C-like languages such as C, C++, Java, JavaScript and C#, then you're going to find Go familiar -- superficially, at least. _(coding_little_go_book.pdf (source-range-773b6275-00039))_
- Saying that a language has a C-like syntax means that if you're used to any other C-like languages such as C, C++, Java, JavaScript and C#, then you're going to find Go familiar -- superficially, at least. _(coding_little_go_book.pdf (source-range-773b6275-00039))_
- Go does away with both of these, though parentheses are still used to control precedence. _(coding_little_go_book.pdf (source-range-773b6275-00040))_
- C-like syntax also tends to mean semi-colon terminated lines and parentheses around conditions. _(coding_little_go_book.pdf (source-range-773b6275-00040))_
- Beyond this, Go is much closer to C than C# or Java - not only in terms of syntax, but in terms of purpose. _(coding_little_go_book.pdf (source-range-773b6275-00044))_
- That's reflected in the terseness and simplicity of the language which will hopefully start to become obvious as you learn it. _(coding_little_go_book.pdf (source-range-773b6275-00044))_
- Beyond this, Go is much closer to C than C# or Java - not only in terms of syntax, but in terms of purpose. _(coding_little_go_book.pdf (source-range-773b6275-00044))_

```
if name == "Leto" {
  print("the spice must flow")
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00041))_

```
if (name == "Goku" && power > 9000) || (name == "gohan" && power < 
4000)  {
print("super Saiyan")
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00043))_

## Garbage Collected

- Without garbage collection, it's up to developers to free the memory associated with such variables at a point where the developer knows the variable isn't needed. _(coding_little_go_book.pdf (source-range-773b6275-00046))_
- Some variables, when created, have an easy-to-define life. _(coding_little_go_book.pdf (source-range-773b6275-00046))_
- A variable local to a function, for example, disappears when the function exits. _(coding_little_go_book.pdf (source-range-773b6275-00046))_
- Garbage collection adds overhead, but it also eliminates a number of devastating bugs. _(coding_little_go_book.pdf (source-range-773b6275-00047))_
- Languages with garbage collectors (e.g., Ruby, Python, Java, JavaScript, C#, Go) are able to keep track of these and free them when they're no longer used. _(coding_little_go_book.pdf (source-range-773b6275-00047))_

## Running Go Code

- For now, you can save it anywhere you want; we don't need to live inside Go's workspace for trivial examples. _(coding_little_go_book.pdf (source-range-773b6275-00051))_
- For now, you can save it anywhere you want; we don't need to live inside Go's workspace for trivial examples. _(coding_little_go_book.pdf (source-range-773b6275-00051))_
- Next, open a shell/command prompt and change the directory to where you saved the file. _(coding_little_go_book.pdf (source-range-773b6275-00052))_
- For me, that means typing cd ~/code . _(coding_little_go_book.pdf (source-range-773b6275-00052))_
- For me, that means typing cd ~/code . _(coding_little_go_book.pdf (source-range-773b6275-00052))_
- It uses a temporary directory to build the program, executes it and then cleans itself up. _(coding_little_go_book.pdf (source-range-773b6275-00054))_
- While developing, you can use either go run or go build . _(coding_little_go_book.pdf (source-range-773b6275-00054))_
- On Linux / OSX, don't forget that you need to prefix the executable with dotslash, so you need to type ./main . _(coding_little_go_book.pdf (source-range-773b6275-00054))_
- go run is a handy command that compiles and runs your code. _(coding_little_go_book.pdf (source-range-773b6275-00054))_
- You can see the location of the temporary file by running: go run --work main.go To explicitly compile code, use go build : go build main.go This will generate an executable main which you can run. _(coding_little_go_book.pdf (source-range-773b6275-00054))_
- It uses a temporary directory to build the program, executes it and then cleans itself up. _(coding_little_go_book.pdf (source-range-773b6275-00054))_

```
package main
func main() {
  println("it's over 9000!")
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00050))_

> go run main.go If everything worked, you should see it's over 9000!
_(source: coding_little_go_book.pdf (source-range-773b6275-00054))_

## Main

> Hopefully, the code that we just executed is understandable. We've created a function and printed out a string with the built-in println function. Did go run know what to execute because there was only a single choice? No. In Go, the entry point to a program has to be a function called main within a package main . We'll talk more about packages in a later chapter. For now, while we focus on understanding the basics of Go, we'll always write our code within the main package. If you want, you can alter the code and change the package name. Run the code via go run and you should get an error. Then, change the name back to main but use a different function name. You should see a different error message. Try making those same changes but use go build instead. Notice that the code compiles, there's just no entry point to run it. This is perfectly normal when you are, for example, building a library.
_(source: coding_little_go_book.pdf (source-range-773b6275-00056))_

> If you want, you can alter the code and change the package name.
_(source: coding_little_go_book.pdf (source-range-773b6275-00056))_

## Imports

- Go has a number of built-in functions, such as println , which can be used without reference. _(coding_little_go_book.pdf (source-range-773b6275-00058))_
- We can't get very far though, without making use of Go's standard library and eventually using third-party libraries. _(coding_little_go_book.pdf (source-range-773b6275-00058))_
- Go has a number of built-in functions, such as println , which can be used without reference. _(coding_little_go_book.pdf (source-range-773b6275-00058))_
- We've also introduced another built-in function len . _(coding_little_go_book.pdf (source-range-773b6275-00063))_
- For now, knowing how to import and use a package is a good start. _(coding_little_go_book.pdf (source-range-773b6275-00064))_
- You've probably noticed we prefix the function name with the package, e.g., fmt.Println . _(coding_little_go_book.pdf (source-range-773b6275-00064))_
- This is different from many other languages. _(coding_little_go_book.pdf (source-range-773b6275-00064))_
- It will not compile if you import a package but don't use it. _(coding_little_go_book.pdf (source-range-773b6275-00065))_
- Go is strict about importing packages. _(coding_little_go_book.pdf (source-range-773b6275-00065))_
- Go is strict about this because unused imports can slow compilation; admittedly a problem most of us don't have to this degree. _(coding_little_go_book.pdf (source-range-773b6275-00067))_
- Over time, you'll get used to it (it'll still be annoying though). _(coding_little_go_book.pdf (source-range-773b6275-00067))_
- Go is strict about this because unused imports can slow compilation; admittedly a problem most of us don't have to this degree. _(coding_little_go_book.pdf (source-range-773b6275-00067))_
- You can click on that section header and see the source code. _(coding_little_go_book.pdf (source-range-773b6275-00068))_
- Another thing to note is that Go's standard library is well documented. _(coding_little_go_book.pdf (source-range-773b6275-00068))_

> [Figure] (p.7)
_(source: coding_little_go_book.pdf (source-range-773b6275-00059))_

```
func main() {
  if len(os.Args) != 2 {
    os.Exit(1)
  }
  fmt.Println("It's over", os.Args[1])
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00060))_

```
go run main.go 9000
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00062))_

> If you're wondering why we expect 2 arguments, it's because the first argument -- at index 0 -- is always the path of the currently running executable.
_(source: coding_little_go_book.pdf (source-range-773b6275-00063))_

```
package main
import (
  "fmt"
  "os"
)
func main() {
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00066))_

> You should get two errors about fmt and os being imported and not used.
_(source: coding_little_go_book.pdf (source-range-773b6275-00067))_

> If you're ever stuck without internet access, you can get the documentation running locally via:
_(source: coding_little_go_book.pdf (source-range-773b6275-00069))_

```
godoc -http=:6060
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00070))_

## Variables and Declarations

- Unfortunately, things are more complicated in Go. _(coding_little_go_book.pdf (source-range-773b6275-00073))_
- Still, it'll probably take some time before you truly feel comfortable with it. _(coding_little_go_book.pdf (source-range-773b6275-00073))_
- You might be thinking Woah! _(coding_little_go_book.pdf (source-range-773b6275-00074))_
- The most explicit way to deal with variable declaration and assignment in Go is also the most verbose: _(coding_little_go_book.pdf (source-range-773b6275-00075))_
- Integers are assigned 0 , booleans false , strings "" and so on. _(coding_little_go_book.pdf (source-range-773b6275-00077))_
- Go has a handy short variable declaration operator, := , which can infer the type: _(coding_little_go_book.pdf (source-range-773b6275-00079))_
- Because a variable can't be declared twice (not in the same scope anyway). _(coding_little_go_book.pdf (source-range-773b6275-00083))_
- It's important that you remember that := is used to declare the variable as well as assign a value to it. _(coding_little_go_book.pdf (source-range-773b6275-00083))_
- Because a variable can't be declared twice (not in the same scope anyway). _(coding_little_go_book.pdf (source-range-773b6275-00083))_
- This means that when we first declare a variable, we use := but on subsequent assignment, we use the assignment operator = . _(coding_little_go_book.pdf (source-range-773b6275-00085))_
- This makes a lot of sense, but it can be tricky for your muscle memory to remember when to switch between the two. _(coding_little_go_book.pdf (source-range-773b6275-00085))_
- The compiler will complain with no new variables on left side of := . _(coding_little_go_book.pdf (source-range-773b6275-00085))_
- This means that when we first declare a variable, we use := but on subsequent assignment, we use the assignment operator = . _(coding_little_go_book.pdf (source-range-773b6275-00085))_
- If you read the error message closely, you'll notice that variables is plural. _(coding_little_go_book.pdf (source-range-773b6275-00086))_
- As long as one of the variables is new, := can be used. _(coding_little_go_book.pdf (source-range-773b6275-00088))_
- However, you can't change the type of power . _(coding_little_go_book.pdf (source-range-773b6275-00090))_
- It was declared (implicitly) as an integer and thus, can only be assigned integers. _(coding_little_go_book.pdf (source-range-773b6275-00090))_
- Although power is being used twice with := , the compiler won't complain the second time we use it, it'll see that the other variable, name , is a new variable and allow := . _(coding_little_go_book.pdf (source-range-773b6275-00090))_
- It was declared (implicitly) as an integer and thus, can only be assigned integers. _(coding_little_go_book.pdf (source-range-773b6275-00090))_
- For now, the last thing to know is that, like imports, Go won't let you have unused variables. _(coding_little_go_book.pdf (source-range-773b6275-00091))_
- won't compile because name is declared but not used. _(coding_little_go_book.pdf (source-range-773b6275-00093))_
- won't compile because name is declared but not used. _(coding_little_go_book.pdf (source-range-773b6275-00093))_
- For now, remember that you'll use var NAME TYPE when declaring a variable to its zero value, NAME := VALUE when declaring and assigning a value, and NAME = VALUE when assigning to a previously declared variable. _(coding_little_go_book.pdf (source-range-773b6275-00094))_

```
package main
import (
  "fmt"
)
func main() {
  var power int
  power = 9000
  fmt.Printf("It's over %d\n", power)
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00076))_

```
var power int = 9000
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00078))_

```
power := 9000
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00080))_

```
func main() {
  power := getPower()
}
func getPower() int {
  return 9001
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00082))_

> If you try to run the following, you'll get an error.
_(source: coding_little_go_book.pdf (source-range-773b6275-00083))_

```
func main() {
  power := 9000
  fmt.Printf("It's over %d\n", power)
// COMPILER ERROR:
  // no new variables on left side of :=
  power := 9001
  fmt.Printf("It's also over %d\n", power)
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00084))_

```
func main() {
  name, power := "Goku", 9000
  fmt.Printf("%s's power is over %d\n", name, power)
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00087))_

```
func main() {
  power := 1000
  fmt.Printf("default power is %d\n", power)
name, power := "Goku", 9000
  fmt.Printf("%s's power is over %d\n", name, power)
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00089))_

```
func main() {
  name, power := "Goku", 1000
  fmt.Printf("default power is %d\n", power)
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00092))_

## Function Declarations

- This is a good time to point out that functions can return multiple values. _(coding_little_go_book.pdf (source-range-773b6275-00096))_
- Sometimes, you only care about one of the return values. _(coding_little_go_book.pdf (source-range-773b6275-00100))_
- _ , the blank identifier, is special in that the return value isn't actually assigned. _(coding_little_go_book.pdf (source-range-773b6275-00102))_
- This lets you use _ over and over again regardless of the returned type. _(coding_little_go_book.pdf (source-range-773b6275-00102))_
- This is more than a convention. _(coding_little_go_book.pdf (source-range-773b6275-00102))_
- You'll also frequently use _ to discard a value. _(coding_little_go_book.pdf (source-range-773b6275-00105))_

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

```
_, exists := power("goku")
if exists == false {
  // handle this error case
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00101))_

```
func add(a, b int) int {
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00104))_

## Before You Continue

- We'll slowly build larger examples and hopefully, the pieces will start to come together. _(coding_little_go_book.pdf (source-range-773b6275-00107))_
- We looked at a number of small individual pieces and it probably feels disjointed at this point. _(coding_little_go_book.pdf (source-range-773b6275-00107))_
- For some systems, dynamic languages are categorically more productive. _(coding_little_go_book.pdf (source-range-773b6275-00108))_
- If you're coming from a statically typed language, you're probably feeling comfortable with Go. _(coding_little_go_book.pdf (source-range-773b6275-00109))_

## Chapter 2 - Structures

- Go isn't an object-oriented (OO) language like C++, Java, Ruby and C#. _(coding_little_go_book.pdf (source-range-773b6275-00111))_
- It doesn't have objects nor inheritance and thus, doesn't have the many concepts associated with OO such as polymorphism and overloading. _(coding_little_go_book.pdf (source-range-773b6275-00111))_
- It doesn't have objects nor inheritance and thus, doesn't have the many concepts associated with OO such as polymorphism and overloading. _(coding_little_go_book.pdf (source-range-773b6275-00111))_
- What Go does have are structures, which can be associated with methods. _(coding_little_go_book.pdf (source-range-773b6275-00112))_
- (It's worth pointing out that composition over inheritance is an old battle cry and Go is the first language I've used that takes a firm stand on the issue.) _(coding_little_go_book.pdf (source-range-773b6275-00112))_
- Go also supports a simple but effective form of composition. _(coding_little_go_book.pdf (source-range-773b6275-00112))_
- Overall, it results in simpler code, but there'll be occasions where you'll miss some of what OO has to offer. _(coding_little_go_book.pdf (source-range-773b6275-00112))_
- Overall, it results in simpler code, but there'll be occasions where you'll miss some of what OO has to offer. _(coding_little_go_book.pdf (source-range-773b6275-00112))_
- Although Go doesn't do OO like you may be used to, you'll notice a lot of similarities between the definition of a structure and that of a class. _(coding_little_go_book.pdf (source-range-773b6275-00113))_
- Before we do that, we have to dive back into declarations. _(coding_little_go_book.pdf (source-range-773b6275-00115))_
- Before we do that, we have to dive back into declarations. _(coding_little_go_book.pdf (source-range-773b6275-00115))_

```
type Saiyan struct {
  Name string
  Power int
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00114))_

## Declarations and Initializations

- When we first looked at variables and declarations, we looked only at built-in types, like integers and strings. _(coding_little_go_book.pdf (source-range-773b6275-00117))_
- Now that we're talking about structures, we need to expand that conversation to include pointers. _(coding_little_go_book.pdf (source-range-773b6275-00117))_
- When we first looked at variables and declarations, we looked only at built-in types, like integers and strings. _(coding_little_go_book.pdf (source-range-773b6275-00117))_
- Note: The trailing , in the above structure is required. _(coding_little_go_book.pdf (source-range-773b6275-00120))_
- Without it, the compiler will give an error. _(coding_little_go_book.pdf (source-range-773b6275-00120))_
- We don't have to set all or even any of the fields. _(coding_little_go_book.pdf (source-range-773b6275-00121))_
- Just like unassigned variables have a zero value, so do fields. _(coding_little_go_book.pdf (source-range-773b6275-00123))_
- Furthermore, you can skip the field name and rely on the order of the field declarations (though for the sake of clarity, you should only do this for structures with few fields): _(coding_little_go_book.pdf (source-range-773b6275-00124))_
- Furthermore, you can skip the field name and rely on the order of the field declarations (though for the sake of clarity, you should only do this for structures with few fields): _(coding_little_go_book.pdf (source-range-773b6275-00124))_
- What all of the above examples do is declare a variable goku and assign a value to it. _(coding_little_go_book.pdf (source-range-773b6275-00126))_
- A pointer is a memory address; it's the location of where to find the actual value. _(coding_little_go_book.pdf (source-range-773b6275-00127))_
- Many times though, we don't want a variable that is directly associated with our value but rather a variable that has a pointer to our value. _(coding_little_go_book.pdf (source-range-773b6275-00127))_
- Loosely, it's the difference between being at a house and having directions to the house. _(coding_little_go_book.pdf (source-range-773b6275-00127))_
- To make this work as you probably expect, we need to pass a pointer to our value: _(coding_little_go_book.pdf (source-range-773b6275-00130))_
- Because Super made changes to a copy of our original goku value and thus, changes made in Super weren't reflected in the caller. _(coding_little_go_book.pdf (source-range-773b6275-00130))_
- Because Super made changes to a copy of our original goku value and thus, changes made in Super weren't reflected in the caller. _(coding_little_go_book.pdf (source-range-773b6275-00130))_
- There's obviously some relation between the types Saiyan and *Saiyan , but they are two distinct types. _(coding_little_go_book.pdf (source-range-773b6275-00132))_
- It used to expect a value of type Saiyan but now expects an address of type *Saiyan , where *X means pointer to value of type X . _(coding_little_go_book.pdf (source-range-773b6275-00132))_
- Next, we changed the type of parameter Super expects. _(coding_little_go_book.pdf (source-range-773b6275-00132))_
- The first is the use of the & operator to get the address of our value (it's called the address of operator). _(coding_little_go_book.pdf (source-range-773b6275-00132))_
- It used to expect a value of type Saiyan but now expects an address of type *Saiyan , where *X means pointer to value of type X . _(coding_little_go_book.pdf (source-range-773b6275-00132))_
- That copy is the same address as the original, which is what that indirection buys us. _(coding_little_go_book.pdf (source-range-773b6275-00133))_
- What you have is a copy, but it still points to the same restaurant as the original. _(coding_little_go_book.pdf (source-range-773b6275-00133))_
- Note that we're still passing a copy of goku's value to Super it just so happens that goku's value has become an address. _(coding_little_go_book.pdf (source-range-773b6275-00133))_
- Go, and to some degree C#, simply make the fact visible. _(coding_little_go_book.pdf (source-range-773b6275-00136))_
- This is how many languages behave, including Ruby, Python, Java and C#. _(coding_little_go_book.pdf (source-range-773b6275-00136))_
- On a 64-bit machine, a pointer is 64 bits large. _(coding_little_go_book.pdf (source-range-773b6275-00137))_
- The real value of pointers though is that they let you share values. _(coding_little_go_book.pdf (source-range-773b6275-00137))_
- If we have a structure with many fields, creating copies can be expensive. _(coding_little_go_book.pdf (source-range-773b6275-00137))_
- It should also be obvious that copying a pointer is going to be cheaper than copying a complex structure. _(coding_little_go_book.pdf (source-range-773b6275-00137))_
- At the end of this chapter, after we've seen a bit more of what we can do with structures, we'll re-examine the pointer-versus-value question. _(coding_little_go_book.pdf (source-range-773b6275-00138))_
- At the end of this chapter, after we've seen a bit more of what we can do with structures, we'll re-examine the pointer-versus-value question. _(coding_little_go_book.pdf (source-range-773b6275-00138))_

```
goku := Saiyan{
  Name: "Goku",
  Power: 9000,
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00119))_

> You'll appreciate the required consistency, especially if you've used a language or format that enforces the opposite.
_(source: coding_little_go_book.pdf (source-range-773b6275-00120))_

```
goku := Saiyan{}
// or
goku := Saiyan{Name: "Goku"}
goku.Power = 9000
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00122))_

```
goku := Saiyan{"Goku", 9000}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00125))_

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

## Functions on Structures

- In the above code, we say that the type *Saiyan is the receiver of the Super method. _(coding_little_go_book.pdf (source-range-773b6275-00142))_

```
type Saiyan struct {
  Name string
  Power int
}
func (s *Saiyan) Super() {
  s.Power += 10000
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00141))_

```
goku := &Saiyan{"Goku", 9001}
goku.Super()
fmt.Println(goku.Power) // will print 19001
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00143))_

## Constructors

- Structures don't have constructors. _(coding_little_go_book.pdf (source-range-773b6275-00145))_
- On the one hand, it's a pretty slight syntactical change; on the other, it does feel a little less compartmentalized. _(coding_little_go_book.pdf (source-range-773b6275-00147))_

```
func NewSaiyan(name string, power int) *Saiyan {
  return &Saiyan{
    Name: name,
    Power: power,
  }
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00146))_

```
func NewSaiyan(name string, power int) Saiyan {
  return Saiyan{
    Name: name,
    Power: power,
  }
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00149))_

## New

- Which you use is up to you, but you'll find that most people prefer the latter whenever they have fields to initialize, since it tends to be easier to read: _(coding_little_go_book.pdf (source-range-773b6275-00153))_

```
goku := new(Saiyan)
// same as
goku := &Saiyan{}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00152))_

```
goku := new(Saiyan)
goku.Name = "goku"
goku.Power = 9001
//vs
goku := &Saiyan {
  Name: "goku",
  Power: 9000,
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00154))_

> Whichever approach you choose, if you follow the factory pattern above, you can shield the rest of your code from knowing and worrying about any of the allocation details.
_(source: coding_little_go_book.pdf (source-range-773b6275-00155))_

## Fields of a Structure

- In the example that we've seen so far, Saiyan has two fields Name and Power of types string and int , respectively. _(coding_little_go_book.pdf (source-range-773b6275-00157))_
- Fields can be of any type -including other structures and types that we haven't explored yet such as arrays, maps, interfaces and functions. _(coding_little_go_book.pdf (source-range-773b6275-00157))_
- Fields can be of any type -including other structures and types that we haven't explored yet such as arrays, maps, interfaces and functions. _(coding_little_go_book.pdf (source-range-773b6275-00157))_

```
For example, we could expand our deﬁnition of Saiyan:
type Saiyan struct {
  Name string
  Power int
  Father *Saiyan
}
which we'd initialize via:
gohan := &Saiyan{
  Name: "Gohan",
  Power: 1000,
  Father: &Saiyan {
    Name: "Goku",
    Power: 9001,
    Father: nil,
  },
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00158))_

## Composition

- Languages that don't have an explicit composition mechanism can always do it the long way. _(coding_little_go_book.pdf (source-range-773b6275-00160))_
- In some languages, this is called a trait or a mixin. _(coding_little_go_book.pdf (source-range-773b6275-00160))_
- In Java, there's the possibility to extend structures with inheritance but, in a scenario where this is not an option, a mixin would be written like this: _(coding_little_go_book.pdf (source-range-773b6275-00160))_
- Go supports composition, which is the act of including one structure into another. _(coding_little_go_book.pdf (source-range-773b6275-00160))_
- In some languages, this is called a trait or a mixin. _(coding_little_go_book.pdf (source-range-773b6275-00160))_
- This can get pretty tedious. _(coding_little_go_book.pdf (source-range-773b6275-00162))_
- Every method of Person needs to be duplicated in Saiyan . _(coding_little_go_book.pdf (source-range-773b6275-00162))_
- Both of the above will print "Goku". _(coding_little_go_book.pdf (source-range-773b6275-00166))_
- When using inheritance, your class is tightly coupled to your superclass and you end up focusing on hierarchy rather than behavior. _(coding_little_go_book.pdf (source-range-773b6275-00167))_

```
public class Person {
  private String name;
public String getName() {
    return this.name;
  }
}
public class Saiyan {
  // Saiyan is said to have a person
  private Person person;
// we forward the call to person
  public String getName() {
    return this.person.getName();
  }
  ...
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00161))_

```
type Person struct {
  Name string
}
func (p *Person) Introduce() {
  fmt.Printf("Hi, I'm %s\n", p.Name)
}
type Saiyan struct {
  *Person
  Power int
}
// and to use it:
goku := &Saiyan{
  Person: &Person{"Goku"},
  Power: 9001,
}
goku.Introduce()
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00163))_

> The Saiyan structure has a field of type *Person . Because we didn't give it an explicit field name, we can implicitly access the fields and functions of the composed type. However, the Go compiler did give it a field name, consider the perfectly valid:
_(source: coding_little_go_book.pdf (source-range-773b6275-00164))_

```
goku := &Saiyan{
  Person: &Person{"Goku"},
}
fmt.Println(goku.Name)
fmt.Println(goku.Person.Name)
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00165))_

## Overloading

- The composed version is always available via s.Person.Introduce() . _(coding_little_go_book.pdf (source-range-773b6275-00172))_

> However, because implicit composition is really just a compiler trick, we can "overwrite" the functions of a composed type. For example, our Saiyan structure can have its own Introduce function:
_(source: coding_little_go_book.pdf (source-range-773b6275-00170))_

```
func (s *Saiyan) Introduce() {
  fmt.Printf("Hi, I'm %s. Ya!\n", s.Name)
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00171))_

## Pointers versus Values

- There are two pieces of good news. _(coding_little_go_book.pdf (source-range-773b6275-00174))_
- Secondly, if you aren't sure, use a pointer. _(coding_little_go_book.pdf (source-range-773b6275-00180))_
- Sometimes, this is the behavior that you'll want but sometimes not. _(coding_little_go_book.pdf (source-range-773b6275-00181))_
- As we already saw, passing values is a great way to make data immutable (changes that a function makes to it won't be reflected in the calling code). _(coding_little_go_book.pdf (source-range-773b6275-00181))_
- Again, these are all pretty subtle cases. _(coding_little_go_book.pdf (source-range-773b6275-00185))_
- Unless you're iterating over thousands or possibly tens of thousands of such points, you wouldn't notice a difference. _(coding_little_go_book.pdf (source-range-773b6275-00185))_

```
type Point struct {
  X int
  Y int
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00183))_

## Before You Continue

- From a practical point of view, this chapter introduced structures, how to make an instance of a structure a receiver of a function, and added pointers to our existing knowledge of Go's type system. _(coding_little_go_book.pdf (source-range-773b6275-00187))_
- The following chapters will build on what we know about structures as well as the inner workings that we've explored. _(coding_little_go_book.pdf (source-range-773b6275-00187))_

## Chapter 3 - Maps, Arrays and Slices

## Arrays

- In Go, like many other languages, arrays are fixed. _(coding_little_go_book.pdf (source-range-773b6275-00191))_
- Declaring an array requires that we specify the size, and once the size is specified, it cannot grow: _(coding_little_go_book.pdf (source-range-773b6275-00191))_
- These are arrays that resize themselves as data is added to them. _(coding_little_go_book.pdf (source-range-773b6275-00191))_
- If you come from Python, Ruby, Perl, JavaScript or PHP (and more), you're probably used to programming with dynamic arrays . _(coding_little_go_book.pdf (source-range-773b6275-00191))_
- The above array can hold up to 10 scores using indexes scores[0] through scores[9] . _(coding_little_go_book.pdf (source-range-773b6275-00193))_
- Attempts to access an out of range index in the array will result in a compiler or runtime error. _(coding_little_go_book.pdf (source-range-773b6275-00193))_
- We can use len to get the length of the array. _(coding_little_go_book.pdf (source-range-773b6275-00196))_
- We often don't know the number of elements we'll be dealing with upfront. _(coding_little_go_book.pdf (source-range-773b6275-00198))_
- Arrays are efficient but rigid. _(coding_little_go_book.pdf (source-range-773b6275-00198))_

```
var scores [10]int
scores[0] = 339
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00192))_

```
scores := [4]int{9001, 9333, 212, 33}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00195))_

```
for index, value := range scores {
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00197))_

## Slices

- A slice is a lightweight structure that wraps and represents a portion of an array. _(coding_little_go_book.pdf (source-range-773b6275-00200))_
- Instead, you use slices. _(coding_little_go_book.pdf (source-range-773b6275-00200))_
- In Go, you rarely, if ever, use arrays directly. _(coding_little_go_book.pdf (source-range-773b6275-00200))_
- There are a few ways to create a slice, and we'll go over when to use which later on. _(coding_little_go_book.pdf (source-range-773b6275-00200))_
- Unlike the array declaration, our slice isn't declared with a length within the square brackets. _(coding_little_go_book.pdf (source-range-773b6275-00202))_
- Unlike the array declaration, our slice isn't declared with a length within the square brackets. _(coding_little_go_book.pdf (source-range-773b6275-00202))_
- Specifically, we have to allocate the memory for the underlying array and also initialize the slice. _(coding_little_go_book.pdf (source-range-773b6275-00204))_
- The length is the size of the slice, the capacity is the size of the underlying array. _(coding_little_go_book.pdf (source-range-773b6275-00204))_
- We use make instead of new because there's more to creating a slice than just allocating the memory (which is what new does). _(coding_little_go_book.pdf (source-range-773b6275-00204))_
- We use make instead of new because there's more to creating a slice than just allocating the memory (which is what new does). _(coding_little_go_book.pdf (source-range-773b6275-00204))_
- (If you're paying attention, you'll note that make and len are overloaded. _(coding_little_go_book.pdf (source-range-773b6275-00206))_
- Go is a language that, to the frustration of some, makes use of features which aren't exposed for developers to use.) _(coding_little_go_book.pdf (source-range-773b6275-00206))_
- Yes, the underlying array has 10 elements, but we need to explicitly expand our slice in order to access those elements. _(coding_little_go_book.pdf (source-range-773b6275-00209))_
- Because our slice has a length of 0. _(coding_little_go_book.pdf (source-range-773b6275-00209))_
- Because our slice has a length of 0. _(coding_little_go_book.pdf (source-range-773b6275-00209))_
- For whatever reason, our crashing code wanted to set the element at index 7. _(coding_little_go_book.pdf (source-range-773b6275-00211))_
- Appending to a slice of length 0 will set the first element. _(coding_little_go_book.pdf (source-range-773b6275-00211))_
- It turns out that append is pretty special. _(coding_little_go_book.pdf (source-range-773b6275-00213))_
- This is why, in the example above that used append , we had to re-assign the value returned by append to our scores variable: append might have created a new value if the original had no more space. _(coding_little_go_book.pdf (source-range-773b6275-00213))_
- You might be thinking this doesn't actually solve the fixed-length issue of arrays. _(coding_little_go_book.pdf (source-range-773b6275-00213))_
- Up to its capacity which, in this case, is 10. _(coding_little_go_book.pdf (source-range-773b6275-00213))_
- If the underlying array is full, it will create a new larger array and copy the values over (this is exactly how dynamic arrays work in PHP , Python, Ruby, JavaScript, ...). _(coding_little_go_book.pdf (source-range-773b6275-00213))_
- The initial capacity of scores is 5. _(coding_little_go_book.pdf (source-range-773b6275-00217))_
- In order to hold 25 values, it'll have to be expanded 3 times with a capacity of 10, 20 and finally 40. _(coding_little_go_book.pdf (source-range-773b6275-00217))_
- To a human, that might seem logical. _(coding_little_go_book.pdf (source-range-773b6275-00220))_
- To a compiler, you're telling it to append a value to a slice that already holds 5 values. _(coding_little_go_book.pdf (source-range-773b6275-00220))_
- Here, the output is going to be [0, 0, 0, 0, 0, 9332] . _(coding_little_go_book.pdf (source-range-773b6275-00220))_
- You use this when you know the values that you want in the array ahead of time. _(coding_little_go_book.pdf (source-range-773b6275-00223))_
- The first one shouldn't need much of an explanation. _(coding_little_go_book.pdf (source-range-773b6275-00223))_
- The second one is useful when you'll be writing into specific indexes of a slice. _(coding_little_go_book.pdf (source-range-773b6275-00224))_
- The third version is a nil slice and is used in conjunction with append , when the number of elements is unknown. _(coding_little_go_book.pdf (source-range-773b6275-00226))_
- The last version lets us specify an initial capacity; useful if we have a general idea of how many elements we'll need. _(coding_little_go_book.pdf (source-range-773b6275-00227))_
- Slices as wrappers to arrays is a powerful concept. _(coding_little_go_book.pdf (source-range-773b6275-00230))_
- Many languages have the concept of slicing an array. _(coding_little_go_book.pdf (source-range-773b6275-00230))_
- Both JavaScript and Ruby arrays have a slice method. _(coding_little_go_book.pdf (source-range-773b6275-00230))_
- However, in these languages, a slice is actually a new array with the values of the original copied over. _(coding_little_go_book.pdf (source-range-773b6275-00230))_
- This is because our slice is really just a window into scores . _(coding_little_go_book.pdf (source-range-773b6275-00234))_
- However, unlike the Ruby example above, the Go code will produce an output of [1, 2, 999, 4, 5] . _(coding_little_go_book.pdf (source-range-773b6275-00234))_
- This is because our slice is really just a window into scores . _(coding_little_go_book.pdf (source-range-773b6275-00234))_
- However, unlike the Ruby example above, the Go code will produce an output of [1, 2, 999, 4, 5] . _(coding_little_go_book.pdf (source-range-773b6275-00234))_
- We can see from the above example, that [X:] is shorthand for from X to the end while [:X] is shorthand for from the start up until X . _(coding_little_go_book.pdf (source-range-773b6275-00239))_
- Unlike other languages, Go doesn't support negative values. _(coding_little_go_book.pdf (source-range-773b6275-00239))_
- Normally, a method that copies values from one array to another has 5 parameters: source , sourceStart , count , destination and destinationStart . _(coding_little_go_book.pdf (source-range-773b6275-00244))_
- Finally, now that we know about slices, we can look at another commonly used built-in function: copy . _(coding_little_go_book.pdf (source-range-773b6275-00244))_
- copy is one of those functions that highlights how slices change the way we code. _(coding_little_go_book.pdf (source-range-773b6275-00244))_

```
scores := []int{1,4,293,4,9}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00201))_

```
scores := make([]int, 10)
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00203))_

```
scores := make([]int, 0, 10)
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00205))_

```
func main() {
  scores := make([]int, 0, 10)
  scores[7] = 9033
  fmt.Println(scores)
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00208))_

```
func main() {
  scores := make([]int, 0, 10)
  scores = append(scores, 5)
  fmt.Println(scores) // prints [5]
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00210))_

```
func main() {
  scores := make([]int, 0, 10)
  scores = scores[0:8]
  scores[7] = 9033
  fmt.Println(scores)
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00212))_

```
func main() {
  scores := make([]int, 0, 5)
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00215))_

```
c := cap(scores)
  fmt.Println(c)
for i := 0; i < 25; i++ {
    scores = append(scores, i)
// if our capacity has changed,
    // Go had to grow our array to accommodate the new data
    if cap(scores) != c {
      c = cap(scores)
      fmt.Println(c)
    }
  }
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00216))_

```
func main() {
  scores := make([]int, 5)
  scores = append(scores, 9332)
  fmt.Println(scores)
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00219))_

```
names := []string{"leto", "jessica", "paul"}
checks := make([]bool, 10)
var names []string
scores := make([]int, 0, 20)
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00222))_

```
func extractPowers(saiyans []*Saiyan) []int {
  powers := make([]int, len(saiyans))
  for index, saiyan := range saiyans {
    powers[index] = saiyan.Power
  }
  return powers
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00225))_

> Even when you know the size, append can be used.
_(source: coding_little_go_book.pdf (source-range-773b6275-00228))_

```
func extractPowers(saiyans []*Saiyan) []int {
  powers := make([]int, 0, len(saiyans))
  for _, saiyan := range saiyans {
    powers = append(powers, saiyan.Power)
  }
  return powers
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00229))_

> You can also get a slice in Ruby by using [START..END] or in Python via [START:END] .
_(source: coding_little_go_book.pdf (source-range-773b6275-00230))_

```
scores = [1,2,3,4,5]
slice = scores[2..4]
slice[0] = 999
puts scores
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00231))_

> The answer is [1, 2, 3, 4, 5] . That's because slice is a completely new array with copies of values. Now, consider the Go equivalent:
_(source: coding_little_go_book.pdf (source-range-773b6275-00232))_

```
scores := []int{1,2,3,4,5}
slice := scores[2:4]
slice[0] = 999
fmt.Println(scores)
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00233))_

> This changes how you code. For example, a number of functions take a position parameter. In JavaScript, if we want to find the first space in a string (yes, slices work on strings too!) after the first five characters, we'd write:
_(source: coding_little_go_book.pdf (source-range-773b6275-00235))_

```
haystack = "the spice must flow";
console.log(haystack.indexOf(" ", 5));
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00236))_

```
strings.Index(haystack[5:], " ")
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00238))_

```
scores := []int{1, 2, 3, 4, 5}
scores = scores[:len(scores)-1]
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00240))_

```
func main() {
  scores := []int{1, 2, 3, 4, 5}
  scores = removeAtIndex(scores, 2)
  fmt.Println(scores) // [1 2 5 4]
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00242))_

```
// won't preserve order
func removeAtIndex(source []int, index int) []int {
  lastIndex := len(source) - 1
  //swap the last value and the value we want to remove
  source[index], source[lastIndex] = source[lastIndex], 
source[index]
return source[:lastIndex]
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00243))_

```
import (
  "fmt"
  "math/rand"
  "sort"
)
func main() {
  scores := make([]int, 100)
  for i := 0; i < 100; i++ {
    scores[i] = int(rand.Int31n(1000))
  }
  sort.Ints(scores)
worst := make([]int, 5)
  copy(worst, scores[:5])
  fmt.Println(worst)
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00245))_

## Maps

- Maps in Go are what other languages call hashtables or dictionaries. _(coding_little_go_book.pdf (source-range-773b6275-00248))_
- They work as you expect: you define a key and value, and can get, set and delete values from it. _(coding_little_go_book.pdf (source-range-773b6275-00248))_
- Maps, like slices, are created with the make function. _(coding_little_go_book.pdf (source-range-773b6275-00249))_
- To get the number of keys, we use len . _(coding_little_go_book.pdf (source-range-773b6275-00251))_
- Like make , this approach is specific to maps and arrays. _(coding_little_go_book.pdf (source-range-773b6275-00260))_
- Each iteration over a lookup will return the key value pair in a random order. _(coding_little_go_book.pdf (source-range-773b6275-00264))_
- Iteration over maps isn't ordered. _(coding_little_go_book.pdf (source-range-773b6275-00264))_

```
func main() {
  lookup := make(map[string]int)
  lookup["goku"] = 9001
  power, exists := lookup["vegeta"]
// prints 0, false
  // 0 is the default value for an integer
  fmt.Println(power, exists)
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00250))_

```
// returns 1
total := len(lookup)
// has no return, can be called on a non-existing key
delete(lookup, "goku")
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00252))_

```
lookup := make(map[string]int, 100)
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00254))_

> If you have some idea of how many keys your map will have, defining an initial size can help with performance.
_(source: coding_little_go_book.pdf (source-range-773b6275-00255))_

```
type Saiyan struct {
  Name string
  Friends map[string]*Saiyan
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00257))_

```
goku := &Saiyan{
  Name: "Goku",
  Friends: make(map[string]*Saiyan),
}
goku.Friends["krillin"] = ... //todo load or create Krillin
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00259))_

```
lookup := map[string]int{
  "goku": 9001,
  "gohan": 2044,
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00261))_

```
for key, value := range lookup {
  ...
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00263))_

## Pointers versus Values

- We'll now have this same conversation with respect to array and map values. _(coding_little_go_book.pdf (source-range-773b6275-00266))_
- So the decision on whether to define an array of pointers versus an array of values comes down to how you use the individual values, not how you use the array or map itself. _(coding_little_go_book.pdf (source-range-773b6275-00268))_
- Many developers think that passing b to, or returning it from, a function is going to be more efficient. _(coding_little_go_book.pdf (source-range-773b6275-00268))_
- Where you will see a difference is when you modify the values of a slice or map. _(coding_little_go_book.pdf (source-range-773b6275-00268))_
- However, what's being passed/returned is a copy of the slice, which itself is a reference. _(coding_little_go_book.pdf (source-range-773b6275-00268))_

```
a := make([]Saiyan, 10)
//or
b := make([]*Saiyan, 10)
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00267))_

## Before You Continue

- Slices are powerful and they have a surprisingly large impact on the clarity of your code. _(coding_little_go_book.pdf (source-range-773b6275-00270))_
- And, if you do, hopefully the foundation we've built here will let you understand what's going on. _(coding_little_go_book.pdf (source-range-773b6275-00270))_
- If you're used to dynamic arrays, there might be a small adjustment, but append should solve most of your discomfort. _(coding_little_go_book.pdf (source-range-773b6275-00270))_
- There are edge cases that we haven't covered, but you're not likely to run into them. _(coding_little_go_book.pdf (source-range-773b6275-00270))_

## Chapter 4 - Code Organization and Interfaces

## Packages

> To keep more complicated libraries and systems organized, we need to learn about packages. In Go, package names follow the directory structure of your Go workspace. If we were building a shopping system, we'd probably start with a package name "shopping" and put our source files in $GOPATH/src/shopping/ . We don't want to put everything inside this folder though. For example, maybe we want to isolate some database logic inside its own folder. To achieve this, we create a subfolder at $GOPATH/src/shopping/db . The package name of the files within this subfolder is simply db , but to access it from another package, including the shopping package, we need to import shopping/db . In other words, when you name a package, via the package keyword, you provide a single value, not a complete hierarchy (e.g., "shopping" or "db"). When you import a package, you specify the complete path. Let's try it. Inside your Go workspace's src folder (which we set up in Getting Started of the Introduction), create a new folder called shopping and a subfolder within it called db . Inside of shopping/db , create a file called db.go and add the following code:
_(source: coding_little_go_book.pdf (source-range-773b6275-00274))_

## package db

- We're just using this as an example to show how to organize code. _(coding_little_go_book.pdf (source-range-773b6275-00277))_
- Notice that the name of the package is the same as the name of the folder. _(coding_little_go_book.pdf (source-range-773b6275-00277))_
- Now, create a file called pricecheck.go inside of the main shopping folder. _(coding_little_go_book.pdf (source-range-773b6275-00278))_
- Now, create a file called pricecheck.go inside of the main shopping folder. _(coding_little_go_book.pdf (source-range-773b6275-00278))_
- It's tempting to think that importing shopping/db is somehow special because we're inside the shopping package/folder already. _(coding_little_go_book.pdf (source-range-773b6275-00280))_
- It's tempting to think that importing shopping/db is somehow special because we're inside the shopping package/folder already. _(coding_little_go_book.pdf (source-range-773b6275-00280))_
- To build an executable, you still need a main . _(coding_little_go_book.pdf (source-range-773b6275-00281))_
- If you're building a package, you don't need anything more than what we've seen. _(coding_little_go_book.pdf (source-range-773b6275-00281))_
- The way I prefer to do this is to create a subfolder called main inside of shopping with a file called main.go and the following content: _(coding_little_go_book.pdf (source-range-773b6275-00281))_
- The way I prefer to do this is to create a subfolder called main inside of shopping with a file called main.go and the following content: _(coding_little_go_book.pdf (source-range-773b6275-00281))_

```
type Item struct {
  Price float64
}
func LoadItem(id int) *Item {
  return &Item{
    Price: 9.001,
  }
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00276))_

```
package shopping
import (
  "shopping/db"
)
func PriceCheck(itemId int) (float64, bool) {
  item := db.LoadItem(itemId)
  if item == nil {
    return 0, false
  }
  return item.Price, true
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00279))_

```
package main
import (
  "shopping"
  "fmt"
)
func main() {
  fmt.Println(shopping.PriceCheck(4343))
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00282))_

## Cyclical Imports

- This is something the compiler won't allow. _(coding_little_go_book.pdf (source-range-773b6275-00286))_
- Item no longer exists in the db package; it's been moved to the shopping package. _(coding_little_go_book.pdf (source-range-773b6275-00290))_

```
package shopping
import (
  "shopping/db"
)
type Item struct {
  Price float64
}
func PriceCheck(itemId int) (float64, bool) {
  item := db.LoadItem(itemId)
  if item == nil {
    return 0, false
  }
  return item.Price, true
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00289))_

> If you try to run the code, you'll get a couple of errors from db/db.go about Item being undefined.
_(source: coding_little_go_book.pdf (source-range-773b6275-00290))_

```
package db
import (
  "shopping"
)
func LoadItem(id int) *shopping.Item {
  return &shopping.Item{
    Price: 9.001,
  }
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00291))_

> Now when you try to run the code, you'll get a dreaded import cycle not allowed error.
_(source: coding_little_go_book.pdf (source-range-773b6275-00292))_

## $GOPATH/src

- pricecheck.go will still import shopping/db , but db.go will now import shopping/models instead of shopping , thus breaking the cycle. _(coding_little_go_book.pdf (source-range-773b6275-00295))_
- Since we moved the shared Item structure to shopping/models/item.go , we need to change shopping/db/db.go to reference the Item structure from models package: _(coding_little_go_book.pdf (source-range-773b6275-00295))_
- pricecheck.go will still import shopping/db , but db.go will now import shopping/models instead of shopping , thus breaking the cycle. _(coding_little_go_book.pdf (source-range-773b6275-00295))_
- You'll often need to share more than just models , so you might have other similar folders named utilities and such. _(coding_little_go_book.pdf (source-range-773b6275-00297))_
- In a few sections, we'll look at interfaces which can help us untangle these types of dependencies. _(coding_little_go_book.pdf (source-range-773b6275-00297))_
- The important rule about these shared packages is that they shouldn't import anything from the shopping package or any sub-packages. _(coding_little_go_book.pdf (source-range-773b6275-00297))_

```
- shopping
   pricecheck.go
   - db
     db.go
   - models
     item.go
   - main
     main.go
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00294))_

```
package db
import (
  "shopping/models"
)
func LoadItem(id int) *models.Item {
  return &models.Item{
    Price: 9.001,
  }
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00296))_

## Visibility

- Go uses a simple rule to define what types and functions are visible outside of a package. _(coding_little_go_book.pdf (source-range-773b6275-00299))_
- If a structure field name starts with a lowercase letter, only code within the same package will be able to access them. _(coding_little_go_book.pdf (source-range-773b6275-00300))_
- If a structure field name starts with a lowercase letter, only code within the same package will be able to access them. _(coding_little_go_book.pdf (source-range-773b6275-00300))_
- But if the function was named newItem , we wouldn't be able to access it from a different package. _(coding_little_go_book.pdf (source-range-773b6275-00303))_
- it could be called via models.NewItem() . _(coding_little_go_book.pdf (source-range-773b6275-00303))_

```
func NewItem() *Item {
  // ...
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00302))_

> For example, if you rename the Item's Price field to price , you should get an error.
_(source: coding_little_go_book.pdf (source-range-773b6275-00304))_

## Package Management

- The go command we've been using to run and build has a get subcommand which is used to fetch third-party libraries. _(coding_little_go_book.pdf (source-range-773b6275-00306))_
- go get supports various protocols but for this example, we'll be getting a library from Github, meaning, you'll need git installed on your computer. _(coding_little_go_book.pdf (source-range-773b6275-00306))_
- Assuming you already have git installed, from a shell/command prompt, enter: _(coding_little_go_book.pdf (source-range-773b6275-00307))_
- In addition to the shopping project that we created, you'll now see a github.com folder. _(coding_little_go_book.pdf (source-range-773b6275-00309))_
- Within, you'll see a mattn folder which contains a go-sqlite3 folder. _(coding_little_go_book.pdf (source-range-773b6275-00309))_
- Within, you'll see a mattn folder which contains a go-sqlite3 folder. _(coding_little_go_book.pdf (source-range-773b6275-00309))_
- We just talked about how to import packages that live in our workspace. _(coding_little_go_book.pdf (source-range-773b6275-00310))_

```
go get github.com/mattn/go-sqlite3
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00308))_

```
import (
  "github.com/mattn/go-sqlite3"
)
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00311))_

## Dependency Management

- go get has a couple of other tricks up its sleeve. _(coding_little_go_book.pdf (source-range-773b6275-00314))_
- In a way, our own source code becomes a Gemfile or package.json . _(coding_little_go_book.pdf (source-range-773b6275-00314))_
- This is an even larger problem if you have two projects needing different versions of the same library. _(coding_little_go_book.pdf (source-range-773b6275-00316))_
- Eventually, you might find go get inadequate. _(coding_little_go_book.pdf (source-range-773b6275-00316))_
- To solve this, you can use a third-party dependency management tool. _(coding_little_go_book.pdf (source-range-773b6275-00317))_
- A more complete list is available at the go-wiki. _(coding_little_go_book.pdf (source-range-773b6275-00317))_
- They are still young, but two promising ones are goop and godep. _(coding_little_go_book.pdf (source-range-773b6275-00317))_

> If you call go get -u it'll update the packages (or you can update a specific package via go get -u FULL_PACKAGE_NAME ).
_(source: coding_little_go_book.pdf (source-range-773b6275-00315))_

## Interfaces

- Interfaces are types that define a contract but not an implementation. _(coding_little_go_book.pdf (source-range-773b6275-00319))_
- You might be wondering what purpose this could possibly serve. _(coding_little_go_book.pdf (source-range-773b6275-00321))_
- Yet by programming against the interface, rather than these concrete implementations, we can easily change (and test) which we use without any impact to our code. _(coding_little_go_book.pdf (source-range-773b6275-00323))_
- If your structure has a function name Log with a string parameter and no return value, then it can be used as a Logger . _(coding_little_go_book.pdf (source-range-773b6275-00327))_
- If your structure has a function name Log with a string parameter and no return value, then it can be used as a Logger . _(coding_little_go_book.pdf (source-range-773b6275-00327))_
- The standard library is full of interfaces. _(coding_little_go_book.pdf (source-range-773b6275-00329))_
- It also tends to promote small and focused interfaces. _(coding_little_go_book.pdf (source-range-773b6275-00329))_
- The io package has a handful of popular ones such as io.Reader , io.Writer , and io.Closer . _(coding_little_go_book.pdf (source-range-773b6275-00329))_
- If you write a function that expects a parameter that you'll only be calling Close() on, you absolutely should accept an io.Closer rather than whatever concrete type you're using. _(coding_little_go_book.pdf (source-range-773b6275-00329))_
- The io package has a handful of popular ones such as io.Reader , io.Writer , and io.Closer . _(coding_little_go_book.pdf (source-range-773b6275-00329))_
- If you write a function that expects a parameter that you'll only be calling Close() on, you absolutely should accept an io.Closer rather than whatever concrete type you're using. _(coding_little_go_book.pdf (source-range-773b6275-00329))_
- Interfaces can also participate in composition. _(coding_little_go_book.pdf (source-range-773b6275-00330))_
- For example, io.ReadCloser is an interface composed of the io.Reader interface as well as the io.Closer interface. _(coding_little_go_book.pdf (source-range-773b6275-00330))_
- And, interfaces themselves can be composed of other interfaces. _(coding_little_go_book.pdf (source-range-773b6275-00330))_
- For example, io.ReadCloser is an interface composed of the io.Reader interface as well as the io.Closer interface. _(coding_little_go_book.pdf (source-range-773b6275-00330))_
- Finally, interfaces are commonly used to avoid cyclical imports. _(coding_little_go_book.pdf (source-range-773b6275-00331))_
- Since they don't have implementations, they'll have limited dependencies. _(coding_little_go_book.pdf (source-range-773b6275-00331))_
- Since they don't have implementations, they'll have limited dependencies. _(coding_little_go_book.pdf (source-range-773b6275-00331))_

```
type Logger interface {
  Log(message string)
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00320))_

```
type SqlLogger struct { ... }
type ConsoleLogger struct { ... }
type FileLogger struct { ... }
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00322))_

```
type Server struct {
  logger Logger
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00325))_

```
or a function parameter (or return value):
func process(logger Logger) {
  logger.Log("hello!")
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00326))_

> In a language like C# or Java, we have to be explicit when a class implements an interface: In Go, this happens implicitly.
_(source: coding_little_go_book.pdf (source-range-773b6275-00327))_

```
func (l ConsoleLogger) 
  fmt.Println(message)
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00328))_

## Before You Continue

- What's most important for you to remember is the tight relationship between package names and your directory structure (not just within a project, but within the entire workspace). _(coding_little_go_book.pdf (source-range-773b6275-00333))_
- Ultimately, how you structure your code around Go's workspace is something that you'll only feel comfortable with after you've written a couple of non-trivial projects. _(coding_little_go_book.pdf (source-range-773b6275-00333))_
- What's most important for you to remember is the tight relationship between package names and your directory structure (not just within a project, but within the entire workspace). _(coding_little_go_book.pdf (source-range-773b6275-00333))_
- Ultimately, how you structure your code around Go's workspace is something that you'll only feel comfortable with after you've written a couple of non-trivial projects. _(coding_little_go_book.pdf (source-range-773b6275-00333))_
- There are a few things we haven't looked at, such as constants and global variables but rest assured, their visibility is determined by the same naming rule. _(coding_little_go_book.pdf (source-range-773b6275-00334))_
- The way Go handles visibility of types is straightforward and effective. _(coding_little_go_book.pdf (source-range-773b6275-00334))_
- There are a few things we haven't looked at, such as constants and global variables but rest assured, their visibility is determined by the same naming rule. _(coding_little_go_book.pdf (source-range-773b6275-00334))_
- However, the first time you see a function that expects something like io.Reader , you'll find yourself thanking the author for not demanding more than he or she needed. _(coding_little_go_book.pdf (source-range-773b6275-00335))_

> Finally, if you're new to interfaces, it might take some time before you get a feel for them.
_(source: coding_little_go_book.pdf (source-range-773b6275-00335))_

## Chapter 5 - Tidbits

## Error Handling

- Go's preferred way to deal with errors is through return values, not exceptions. _(coding_little_go_book.pdf (source-range-773b6275-00339))_
- You can create your own error type; the only requirement is that it fulfills the contract of the built-in error interface, which is: _(coding_little_go_book.pdf (source-range-773b6275-00341))_
- You can create your own error type; the only requirement is that it fulfills the contract of the built-in error interface, which is: _(coding_little_go_book.pdf (source-range-773b6275-00341))_
- This is a package variable (it's defined outside of a function) which is publicly accessible (upper-case first letter). _(coding_little_go_book.pdf (source-range-773b6275-00348))_
- If it makes contextual sense, you should use this error, too. _(coding_little_go_book.pdf (source-range-773b6275-00348))_
- As a final note, Go does have panic and recover functions. _(coding_little_go_book.pdf (source-range-773b6275-00350))_
- panic is like throwing an exception while recover is like catch ; they are rarely used. _(coding_little_go_book.pdf (source-range-773b6275-00350))_

```
package main
import (
  "fmt"
  "os"
  "strconv"
)
func main() {
  if len(os.Args) != 2 {
    os.Exit(1)
  }
n, err := strconv.Atoi(os.Args[1])
  if err != nil {
    fmt.Println("not a valid number")
  } else {
    fmt.Println(n)
  }
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00340))_

```
type error interface {
  Error() string
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00342))_

```
import (
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00344))_

```
"errors"
)
func process(count int) error {
  if count < 1 {
    return errors.New("Invalid count")
  }
  ...
  return nil
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00345))_

```
var EOF = errors.New("EOF")
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00347))_

> Various functions can return this error, say when we're reading from a file or STDIN.
_(source: coding_little_go_book.pdf (source-range-773b6275-00348))_

```
package main
import (
  "fmt"
  "io"
)
func main() {
  var input int
  _, err := fmt.Scan(&input)
  if err == io.EOF {
    fmt.Println("no more input!")
  }
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00349))_

## Defer

- This lets you release resources near where it's initialized and takes care of multiple return points. _(coding_little_go_book.pdf (source-range-773b6275-00354))_
- Whatever you defer will be executed after the enclosing function (in this case main() ) returns, even if it does so violently. _(coding_little_go_book.pdf (source-range-773b6275-00354))_
- The point is to show how defer works. _(coding_little_go_book.pdf (source-range-773b6275-00354))_
- Whatever you defer will be executed after the enclosing function (in this case main() ) returns, even if it does so violently. _(coding_little_go_book.pdf (source-range-773b6275-00354))_

> Even though Go has a garbage collector, some resources require that we explicitly release them. For example, we need to Close() files after we're done with them. This sort of code is always dangerous. For one thing, as we're writing a function, it's easy to forget to Close something that we declared 10 lines up. For another, a function might have multiple return points. Go's solution is the defer keyword:
_(source: coding_little_go_book.pdf (source-range-773b6275-00352))_

```
package main
import (
  "fmt"
  "os"
)
func main() {
  file, err := os.Open("a_file_to_read")
  if err != nil {
    fmt.Println(err)
    return
  }
  defer file.Close()
  // read the file
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00353))_

> If you try to run the above code, you'll probably get an error (the file doesn't exist).
_(source: coding_little_go_book.pdf (source-range-773b6275-00354))_

## go fmt

- Most programs written in Go follow the same formatting rules, namely, a tab is used to indent and braces go on the same line as their statement. _(coding_little_go_book.pdf (source-range-773b6275-00356))_
- That's what I did for a long time, but I'm glad I eventually gave in. _(coding_little_go_book.pdf (source-range-773b6275-00357))_
- It's easy to use and authoritative (so no one argues over meaningless preferences). _(coding_little_go_book.pdf (source-range-773b6275-00357))_
- A big reason for this is the go fmt command. _(coding_little_go_book.pdf (source-range-773b6275-00357))_
- I know, you have your own style and you want to stick to it. _(coding_little_go_book.pdf (source-range-773b6275-00357))_
- It does more than indent your code; it also aligns field declarations and alphabetically orders imports. _(coding_little_go_book.pdf (source-range-773b6275-00360))_

> When you're inside a project, you can apply the formatting rule to it and all sub-projects via:
_(source: coding_little_go_book.pdf (source-range-773b6275-00358))_

```
go fmt ./...
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00359))_

## Initialized If

- Interestingly, while the values aren't available outside the ifstatement, they are available inside any else if or else . _(coding_little_go_book.pdf (source-range-773b6275-00366))_
- Interestingly, while the values aren't available outside the ifstatement, they are available inside any else if or else . _(coding_little_go_book.pdf (source-range-773b6275-00366))_

> Go supports a slightly modified if-statement, one where a value can be initiated prior to the condition being evaluated:
_(source: coding_little_go_book.pdf (source-range-773b6275-00362))_

```
if x := 10; count > x {
  ...
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00363))_

```
if err := process(); err != nil {
  return err
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00365))_

## Empty Interface and Conversions

- In most object-oriented languages, a built-in base class, often named object , is the superclass for all other classes. _(coding_little_go_book.pdf (source-range-773b6275-00368))_
- Since every type implements all 0 of the empty interface's methods, and since interfaces are implicitly implemented, every type fulfills the contract of the empty interface. _(coding_little_go_book.pdf (source-range-773b6275-00368))_
- Go, having no inheritance, doesn't have such a superclass. _(coding_little_go_book.pdf (source-range-773b6275-00368))_
- Note that if the underlying type is not int , the above will result in an error. _(coding_little_go_book.pdf (source-range-773b6275-00373))_
- Converting values back and forth is ugly and dangerous but sometimes, in a static language, it's the only choice. _(coding_little_go_book.pdf (source-range-773b6275-00376))_
- You'll see and probably use the empty interface more than you might first expect. _(coding_little_go_book.pdf (source-range-773b6275-00376))_
- Converting values back and forth is ugly and dangerous but sometimes, in a static language, it's the only choice. _(coding_little_go_book.pdf (source-range-773b6275-00376))_

```
func add(a interface{}, b interface{}) interface{} {
  ...
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00370))_

```
return a.(int) + b.(int)
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00372))_

```
switch a.(type) {
  case int:
    fmt.Printf("a is now an int and equals %d\n", a)
  case bool, string:
    // ...
  default:
    // ...
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00375))_

## Strings and Byte Arrays

- Strings and byte arrays are closely related. _(coding_little_go_book.pdf (source-range-773b6275-00378))_
- In fact, this way of converting is common across various types as well. _(coding_little_go_book.pdf (source-range-773b6275-00380))_
- Some functions explicitly expect an int32 or an int64 or their unsigned counterparts. _(coding_little_go_book.pdf (source-range-773b6275-00380))_
- Still, when it comes to bytes and strings, it's probably something you'll end up doing often. _(coding_little_go_book.pdf (source-range-773b6275-00382))_
- This is necessary because strings are immutable. _(coding_little_go_book.pdf (source-range-773b6275-00382))_
- This is necessary because strings are immutable. _(coding_little_go_book.pdf (source-range-773b6275-00382))_
- Strings are made of runes which are unicode code points. _(coding_little_go_book.pdf (source-range-773b6275-00383))_

```
stra := "the spice must flow"
byts := []byte(stra)
strb := string(byts)
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00379))_

```
int64(count)
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00381))_

> If you take the length of a string, you might not get what you expect.
_(source: coding_little_go_book.pdf (source-range-773b6275-00383))_

```
fmt.Println(len("椒"))
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00384))_

> If you iterate over a string using range , you'll get runes, not bytes.
_(source: coding_little_go_book.pdf (source-range-773b6275-00385))_

## Function Type

- which can then be used anywhere -- as a field type, as a parameter, as a return value. _(coding_little_go_book.pdf (source-range-773b6275-00389))_
- which can then be used anywhere -- as a field type, as a parameter, as a return value. _(coding_little_go_book.pdf (source-range-773b6275-00389))_

```
type Add func(a int, b int) int
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00388))_

```
package main
import (
  "fmt"
)
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00390))_

```
type Add func(a int, b int) int
func main() {
  fmt.Println(process(func(a int, b int) int{
      return a + b
  }))
}
func process(adder Add) int {
  return adder(1, 2)
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00391))_

## Before You Continue

- defer is an unusual but practical approach to resource management. _(coding_little_go_book.pdf (source-range-773b6275-00394))_
- In fact, it isn't tied to resource management only. _(coding_little_go_book.pdf (source-range-773b6275-00394))_
- We looked at various aspects of programming with Go. _(coding_little_go_book.pdf (source-range-773b6275-00394))_
- In fact, it isn't tied to resource management only. _(coding_little_go_book.pdf (source-range-773b6275-00394))_
- Yet, I also find that it results in code that's easier to follow. _(coding_little_go_book.pdf (source-range-773b6275-00394))_
- Most notably, we saw how error handling behaves and how to release resources such as connections and open files. _(coding_little_go_book.pdf (source-range-773b6275-00394))_
- Certainly, we haven't looked at all of the tidbits Go has to offer. _(coding_little_go_book.pdf (source-range-773b6275-00395))_
- But you should be feeling comfortable enough to tackle whatever you come across. _(coding_little_go_book.pdf (source-range-773b6275-00395))_

> You can use defer for any purpose, such as logging when a function exits.
_(source: coding_little_go_book.pdf (source-range-773b6275-00394))_

## Chapter 6 - Concurrency

- Go is often described as a concurrent-friendly language. _(coding_little_go_book.pdf (source-range-773b6275-00397))_
- The reason for this is that it provides a simple syntax over two powerful mechanisms: goroutines and channels. _(coding_little_go_book.pdf (source-range-773b6275-00397))_

## Goroutines

- Code that runs in a goroutine can run concurrently with other code. _(coding_little_go_book.pdf (source-range-773b6275-00399))_
- If we just want to run a bit of code, such as the above, we can use an anonymous function. _(coding_little_go_book.pdf (source-range-773b6275-00402))_
- There are a few interesting things going on here, but the most important is how we start a goroutine. _(coding_little_go_book.pdf (source-range-773b6275-00402))_
- If we just want to run a bit of code, such as the above, we can use an anonymous function. _(coding_little_go_book.pdf (source-range-773b6275-00402))_
- Do note that anonymous functions aren't only used with goroutines, however. _(coding_little_go_book.pdf (source-range-773b6275-00402))_
- Goroutines are easy to create and have little overhead. _(coding_little_go_book.pdf (source-range-773b6275-00404))_
- Multiple goroutines will end up running on the same underlying OS thread. _(coding_little_go_book.pdf (source-range-773b6275-00404))_
- The result is that a goroutine has a fraction of overhead (a few KB) than OS threads. _(coding_little_go_book.pdf (source-range-773b6275-00404))_
- This is often called an M:N threading model because we have M application threads (goroutines) running on N OS threads. _(coding_little_go_book.pdf (source-range-773b6275-00404))_
- On modern hardware, it's possible to have millions of goroutines. _(coding_little_go_book.pdf (source-range-773b6275-00404))_
- This is often called an M:N threading model because we have M application threads (goroutines) running on N OS threads. _(coding_little_go_book.pdf (source-range-773b6275-00404))_
- Furthermore, the complexity of mapping and scheduling is hidden. _(coding_little_go_book.pdf (source-range-773b6275-00405))_
- We just say this code should run concurrently and let Go worry about making it happen. _(coding_little_go_book.pdf (source-range-773b6275-00405))_
- If we go back to our example, you'll notice that we had to Sleep for a few milliseconds. _(coding_little_go_book.pdf (source-range-773b6275-00406))_
- To solve this, we need to coordinate our code. _(coding_little_go_book.pdf (source-range-773b6275-00406))_
- That's because the main process exits before the goroutine gets a chance to execute (the process doesn't wait until all goroutines are finished before exiting). _(coding_little_go_book.pdf (source-range-773b6275-00406))_
- That's because the main process exits before the goroutine gets a chance to execute (the process doesn't wait until all goroutines are finished before exiting). _(coding_little_go_book.pdf (source-range-773b6275-00406))_

```
package main
import (
  "fmt"
  "time"
)
func main() {
  fmt.Println("start")
  go process()
  time.Sleep(time.Millisecond * 10) // this is bad, don't do this!
  fmt.Println("done")
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00400))_

```
func process() {
  fmt.Println("processing")
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00401))_

```
go func() {
  fmt.Println("processing")
}()
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00403))_

## Synchronization

- Creating goroutines is trivial, and they are so cheap that we can start many; however, concurrent code needs to be coordinated. _(coding_little_go_book.pdf (source-range-773b6275-00408))_
- To help with this problem, Go provides channels . _(coding_little_go_book.pdf (source-range-773b6275-00408))_
- In some ways, it's like programming without a garbage collector -- it requires that you think about your data from a new angle, always watchful for possible danger. _(coding_little_go_book.pdf (source-range-773b6275-00409))_
- Writing concurrent code requires that you pay specific attention to where and how you read and write values. _(coding_little_go_book.pdf (source-range-773b6275-00409))_
- However, the reality is that the behavior is undefined. _(coding_little_go_book.pdf (source-range-773b6275-00413))_
- If you think the output is 1, 2, ... _(coding_little_go_book.pdf (source-range-773b6275-00413))_
- Because we potentially have multiple (two in this case) goroutines writing to the same variable, counter , at the same time. _(coding_little_go_book.pdf (source-range-773b6275-00413))_
- Because we potentially have multiple (two in this case) goroutines writing to the same variable, counter , at the same time. _(coding_little_go_book.pdf (source-range-773b6275-00413))_
- If you run this example, you'll see that very often the numbers are printed in a weird order, and/or numbers are duplicated/missing. _(coding_little_go_book.pdf (source-range-773b6275-00414))_
- There are worse possibilities too, such as system crashes or accessing an arbitrary piece of data and incrementing it! _(coding_little_go_book.pdf (source-range-773b6275-00414))_
- There are worse possibilities too, such as system crashes or accessing an arbitrary piece of data and incrementing it! _(coding_little_go_book.pdf (source-range-773b6275-00414))_
- The only concurrent thing you can safely do to a variable is to read from it. _(coding_little_go_book.pdf (source-range-773b6275-00415))_
- You can have as many readers as you want, but writes need to be synchronized. _(coding_little_go_book.pdf (source-range-773b6275-00415))_
- There are various ways to do this, including using some truly atomic operations that rely on special CPU instructions. _(coding_little_go_book.pdf (source-range-773b6275-00415))_
- The only concurrent thing you can safely do to a variable is to read from it. _(coding_little_go_book.pdf (source-range-773b6275-00415))_
- The reason we simply define our lock as lock sync.Mutex is because the default value of a sync.Mutex is unlocked. _(coding_little_go_book.pdf (source-range-773b6275-00417))_
- The reason we simply define our lock as lock sync.Mutex is because the default value of a sync.Mutex is unlocked. _(coding_little_go_book.pdf (source-range-773b6275-00417))_
- While it might be tempting to use coarse locks (locks that cover a large amount of code), that undermines the very reason we're doing concurrent programming in the first place. _(coding_little_go_book.pdf (source-range-773b6275-00418))_
- First of all, it isn't always so obvious what code needs to be protected. _(coding_little_go_book.pdf (source-range-773b6275-00418))_
- There's a whole class of serious bugs that can arise when doing concurrent programming. _(coding_little_go_book.pdf (source-range-773b6275-00418))_
- We generally want fine locks; else, we end up with a ten-lane highway that suddenly turns into a one-lane road. _(coding_little_go_book.pdf (source-range-773b6275-00418))_
- The example above is deceptive. _(coding_little_go_book.pdf (source-range-773b6275-00418))_
- With a single lock, this isn't a problem, but if you're using two or more locks around the same code, it's dangerously easy to have situations where goroutineA holds lockA but needs access to lockB, while goroutineB holds lockB but needs access to lockA. _(coding_little_go_book.pdf (source-range-773b6275-00419))_
- The other problem has to do with deadlocks. _(coding_little_go_book.pdf (source-range-773b6275-00419))_
- It actually is possible to deadlock with a single lock, if we forget to release it. _(coding_little_go_book.pdf (source-range-773b6275-00420))_
- This isn't as dangerous as a multi-lock deadlock (because those are really tough to spot), but just so you can see what happens, try running: _(coding_little_go_book.pdf (source-range-773b6275-00420))_
- This isn't as dangerous as a multi-lock deadlock (because those are really tough to spot), but just so you can see what happens, try running: _(coding_little_go_book.pdf (source-range-773b6275-00420))_

```
package main
import (
  "fmt"
  "time"
)
var counter = 0
func main() {
  for i := 0; i < 20; i++ {
    go incr()
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00410))_

```
}
  time.Sleep(time.Millisecond * 10)
}
func incr() {
  counter++
  fmt.Println(counter)
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00411))_

> It's true that if you run the above code, you'll sometimes get that output.
_(source: coding_little_go_book.pdf (source-range-773b6275-00413))_

```
package main
import (
  "fmt"
  "time"
  "sync"
)
var (
  counter = 0
  lock sync.Mutex
)
func main() {
  for i := 0; i < 20; i++ {
    go incr()
  }
  time.Sleep(time.Millisecond * 10)
}
func incr() {
  lock.Lock()
  defer lock.Unlock()
  counter++
  fmt.Println(counter)
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00416))_

## package main

- This distinction allows multiple simultaneous readers while ensuring that writing is exclusive. _(coding_little_go_book.pdf (source-range-773b6275-00423))_
- While read-write mutexes are commonly used, they place an additional burden on developers: we must now pay attention to not only when we're accessing data, but also how. _(coding_little_go_book.pdf (source-range-773b6275-00423))_
- In Go, sync.RWMutex is such a lock. _(coding_little_go_book.pdf (source-range-773b6275-00423))_
- For one thing, there's another common mutex called a read-write mutex. _(coding_little_go_book.pdf (source-range-773b6275-00423))_
- While read-write mutexes are commonly used, they place an additional burden on developers: we must now pay attention to not only when we're accessing data, but also how. _(coding_little_go_book.pdf (source-range-773b6275-00423))_
- For example, sleeping for 10 milliseconds isn't a particularly elegant solution. _(coding_little_go_book.pdf (source-range-773b6275-00424))_
- These are all things that are doable without channels . _(coding_little_go_book.pdf (source-range-773b6275-00425))_

```
import (
  "time"
  "sync"
)
var (
  lock sync.Mutex
)
func main() {
  go func() { lock.Lock() }()
  time.Sleep(time.Millisecond * 10)
  lock.Lock()
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00422))_

> What if a goroutine takes more than 10 milliseconds?
_(source: coding_little_go_book.pdf (source-range-773b6275-00424))_

## Channels

- It waits until data is available then "processes" it. _(coding_little_go_book.pdf (source-range-773b6275-00429))_
- Dutifully, it does this in a loop, forever waiting for more data to process. _(coding_little_go_book.pdf (source-range-773b6275-00429))_
- Our worker is simple. _(coding_little_go_book.pdf (source-range-773b6275-00429))_
- It waits until data is available then "processes" it. _(coding_little_go_book.pdf (source-range-773b6275-00429))_
- We don't know which worker is going to get what data. _(coding_little_go_book.pdf (source-range-773b6275-00430))_
- Notice that the only shared state is the channel, which we can safely receive from and send to concurrently. _(coding_little_go_book.pdf (source-range-773b6275-00431))_
- Channels provide all of the synchronization code we need and also ensure that, at any given time, only one goroutine has access to a specific piece of data. _(coding_little_go_book.pdf (source-range-773b6275-00431))_
- Notice that the only shared state is the channel, which we can safely receive from and send to concurrently. _(coding_little_go_book.pdf (source-range-773b6275-00431))_
- Channels provide all of the synchronization code we need and also ensure that, at any given time, only one goroutine has access to a specific piece of data. _(coding_little_go_book.pdf (source-range-773b6275-00431))_

> The challenge with concurrent programming stems from sharing data. If your goroutines share no data, you needn't worry about synchronizing them. That isn't an option for all systems, however. In fact, many systems are built with the exact opposite goal in mind: to share data across multiple requests. An in-memory cache or a database, are good examples of this. This is becoming an increasingly common reality. Channels help make concurrent programming saner by taking shared data out of the picture. A channel is a communication pipe between goroutines which is used to pass data. In other words, a goroutine that has data can pass it to another goroutine via a channel. The result is that, at any point in time, only one goroutine has access to the data. A channel, like everything else, has a type. This is the type of data that we'll be passing through our channel. For example, to create a channel which can be used to pass an integer around, we'd do: The type of this channel is chan int . Therefore, to pass this channel to a function, our signature looks like: Channels support two operations: receiving and sending. We send to a channel by doing: CHANNEL <- DATA and receive from one by doing VAR := <-CHANNEL The arrow points in the direction that data flows. When sending, the data flows into the channel. When receiving, the data flows out of the channel. The final thing to know before we look at our first example is that receiving and sending to and from a channel is blocking. That is, when we receive from a channel, execution of the goroutine won't continue until data is available. Similarly, when we send to a channel, execution won't continue until the data is received. Consider a system with incoming data that we want to handle in separate goroutines. This is a common requirement. If we did our data-intensive processing on the goroutine which accepts the incoming data, we'd risk timing out clients. First, we'll write our worker. This could be a simple function, but I'll make it part of a structure since we haven't seen goroutines used like this before: c := make( chan int) func worker(c chan int) { ... } type Worker struct {
_(source: coding_little_go_book.pdf (source-range-773b6275-00427))_

```
id int
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00428))_

## Buffered Channels

- What's happening is that our main code, the one that accepts the user's incoming data (which we just simulated with a random number generator) is blocking as it sends to the channel because no receiver is available. _(coding_little_go_book.pdf (source-range-773b6275-00435))_
- What's happening is that our main code, the one that accepts the user's incoming data (which we just simulated with a random number generator) is blocking as it sends to the channel because no receiver is available. _(coding_little_go_book.pdf (source-range-773b6275-00435))_
- In cases where you need high guarantees that the data is being processed, you probably will want to start blocking the client. _(coding_little_go_book.pdf (source-range-773b6275-00436))_
- Channels have this buffering capability built-in. _(coding_little_go_book.pdf (source-range-773b6275-00436))_
- There are a few popular strategies to do this. _(coding_little_go_book.pdf (source-range-773b6275-00436))_
- If no worker is available, we want to temporarily store the data in some sort of queue. _(coding_little_go_book.pdf (source-range-773b6275-00436))_
- The first is to buffer the data. _(coding_little_go_book.pdf (source-range-773b6275-00436))_
- In other cases, you might be willing to loosen those guarantees. _(coding_little_go_book.pdf (source-range-773b6275-00436))_
- In our example, we're continuously pushing more data than our workers can handle. _(coding_little_go_book.pdf (source-range-773b6275-00438))_
- You can make this change, but you'll notice that the processing is still choppy. _(coding_little_go_book.pdf (source-range-773b6275-00438))_
- You can see that it grows and grows until it fills up, at which point sending to our channel start to block again. _(coding_little_go_book.pdf (source-range-773b6275-00441))_

```
for {
  data := <-c
  fmt.Printf("worker %d got %d\n", w.id, data)
  time.Sleep(time.Millisecond * 500)
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00434))_

```
c := make(chan int, 100)
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00437))_

```
for {
  c <- rand.Int()
  fmt.Println(len(c))
  time.Sleep(time.Millisecond * 50)
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00440))_

## Select

- We can't use up an infinite amount of memory hoping a worker frees up. _(coding_little_go_book.pdf (source-range-773b6275-00443))_
- Even with buffering, there comes a point where we need to start dropping messages. _(coding_little_go_book.pdf (source-range-773b6275-00443))_
- With it, we can provide code for when the channel isn't available to send to. _(coding_little_go_book.pdf (source-range-773b6275-00444))_
- We're pushing out 20 messages per second, but our workers can only handle 10 per second; thus, half the messages get dropped. _(coding_little_go_book.pdf (source-range-773b6275-00446))_
- We're pushing out 20 messages per second, but our workers can only handle 10 per second; thus, half the messages get dropped. _(coding_little_go_book.pdf (source-range-773b6275-00446))_
- A main purpose of select is to manage multiple channels. _(coding_little_go_book.pdf (source-range-773b6275-00447))_
- If no channel is available, default is executed if one is provided. _(coding_little_go_book.pdf (source-range-773b6275-00447))_
- A channel is randomly picked when multiple are available. _(coding_little_go_book.pdf (source-range-773b6275-00447))_
- Given multiple channels, select will block until the first one becomes available. _(coding_little_go_book.pdf (source-range-773b6275-00447))_
- This is only the start of what we can accomplish with select . _(coding_little_go_book.pdf (source-range-773b6275-00447))_
- This is only the start of what we can accomplish with select . _(coding_little_go_book.pdf (source-range-773b6275-00447))_
- It's hard to come up with a simple example that demonstrates this behavior as it's a fairly advanced feature. _(coding_little_go_book.pdf (source-range-773b6275-00448))_

```
c := make(chan int)
Next, we change our for loop:
for {
  select {
  case c <- rand.Int():
    //optional code here
  default:
    //this can be left empty to silently drop the data
    fmt.Println("dropped")
  }
  time.Sleep(time.Millisecond * 50)
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00445))_

## Timeout

- Another popular option is to timeout. _(coding_little_go_book.pdf (source-range-773b6275-00450))_
- This is also something easy to achieve in Go. _(coding_little_go_book.pdf (source-range-773b6275-00450))_
- We've looked at buffering messages as well as simply dropping them. _(coding_little_go_book.pdf (source-range-773b6275-00450))_
- To block for a maximum amount of time, we can use the time.After function. _(coding_little_go_book.pdf (source-range-773b6275-00451))_
- To block for a maximum amount of time, we can use the time.After function. _(coding_little_go_book.pdf (source-range-773b6275-00451))_
- The channel is written to after the specified time expires. _(coding_little_go_book.pdf (source-range-773b6275-00453))_
- time.After returns a channel, so we can select from it. _(coding_little_go_book.pdf (source-range-773b6275-00453))_
- time.After returns a channel, so we can select from it. _(coding_little_go_book.pdf (source-range-773b6275-00453))_
- The channel is written to after the specified time expires. _(coding_little_go_book.pdf (source-range-773b6275-00453))_
- Back to our select , there are a couple of things to play with. _(coding_little_go_book.pdf (source-range-773b6275-00456))_
- If you aren't sure what's going on, remember that default fires immediately if no channel is available. _(coding_little_go_book.pdf (source-range-773b6275-00456))_
- In the above example, we simply discard the value that was sent to the channel. _(coding_little_go_book.pdf (source-range-773b6275-00457))_
- Also, time.After is a channel of type chan time.Time . _(coding_little_go_book.pdf (source-range-773b6275-00457))_
- Also, time.After is a channel of type chan time.Time . _(coding_little_go_book.pdf (source-range-773b6275-00457))_
- Notice that we're sending to c but receiving from time.After . _(coding_little_go_book.pdf (source-range-773b6275-00459))_
- - The first available channel is chosen. _(coding_little_go_book.pdf (source-range-773b6275-00460))_
- - If multiple channels are available, one is randomly picked. _(coding_little_go_book.pdf (source-range-773b6275-00461))_
- - If no channel is available, the default case is executed. _(coding_little_go_book.pdf (source-range-773b6275-00462))_
- Finally, it's common to see a select inside a for . _(coding_little_go_book.pdf (source-range-773b6275-00464))_

```
for {
  select {
  case c <- rand.Int():
  case <-time.After(time.Millisecond * 100):
    fmt.Println("timed out")
  }
  time.Sleep(time.Millisecond * 50)
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00452))_

```
func after(d time.Duration) chan bool {
  c := make(chan bool)
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00454))_

```
go func() {
    time.Sleep(d)
    c <- true
  }()
  return c
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00455))_

> First, what happens if you add the default case back?
_(source: coding_little_go_book.pdf (source-range-773b6275-00456))_

> If you want though, you can receive it:
_(source: coding_little_go_book.pdf (source-range-773b6275-00457))_

```
case t := <-time.After(time.Millisecond * 100):
  fmt.Println("timed out at", t)
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00458))_

```
for {
  select {
  case data := <-c:
    fmt.Printf("worker %d got %d\n", w.id, data)
  case <-time.After(time.Millisecond * 10):
    fmt.Println("Break time")
    time.Sleep(time.Second)
  }
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00465))_

## Before You Continue

- Go aims to make it easier. _(coding_little_go_book.pdf (source-range-773b6275-00467))_
- If you're new to the world of concurrent programming, it might all seem rather overwhelming. _(coding_little_go_book.pdf (source-range-773b6275-00467))_
- Goroutines effectively abstract what's needed to run concurrent code. _(coding_little_go_book.pdf (source-range-773b6275-00468))_
- I encourage you to first focus on channels, but when you see a simple example that needs a short-lived lock, consider using a mutex or readwrite mutex. _(coding_little_go_book.pdf (source-range-773b6275-00469))_
- Having said that, I still make extensive use of the various synchronization primitives found in the sync and sync/atomic packages. _(coding_little_go_book.pdf (source-range-773b6275-00469))_

> Channels help eliminate some serious bugs that can happen when data is shared by eliminating the sharing of data.
_(source: coding_little_go_book.pdf (source-range-773b6275-00468))_

## Conclusion

- Perhaps, I did this reality a disservice. _(coding_little_go_book.pdf (source-range-773b6275-00471))_
- I recently heard Go described as a boring language. _(coding_little_go_book.pdf (source-range-773b6275-00471))_
- We did spend three chapters talking about types and how to declare variables after all. _(coding_little_go_book.pdf (source-range-773b6275-00471))_
- We did spend three chapters talking about types and how to declare variables after all. _(coding_little_go_book.pdf (source-range-773b6275-00471))_
- Boring because it's easy to learn, easy to write and, most importantly, easy to read. _(coding_little_go_book.pdf (source-range-773b6275-00471))_
- That Go makes pointers visible and that slices are thin wrappers around arrays probably isn't overwhelming to seasoned Java or C# developers. _(coding_little_go_book.pdf (source-range-773b6275-00472))_
- If you have a background in a statically typed language, much of what we saw was probably, at best, a refresher. _(coding_little_go_book.pdf (source-range-773b6275-00472))_
- Not least of which is the various syntax around declaration and initialization. _(coding_little_go_book.pdf (source-range-773b6275-00473))_
- It is a fair bit to learn. _(coding_little_go_book.pdf (source-range-773b6275-00473))_
- If you've mostly been making use of dynamic languages, you might feel a little different. _(coding_little_go_book.pdf (source-range-773b6275-00473))_
- Despite being a fan of Go, I find that for all the progress towards simplicity, there's something less than simple about it. _(coding_little_go_book.pdf (source-range-773b6275-00473))_
- Beyond this, Go gives us a simple but effective way to organize our code. _(coding_little_go_book.pdf (source-range-773b6275-00474))_
- Interfaces, return-based error handling, defer for resource management and a simple way to achieve composition. _(coding_little_go_book.pdf (source-range-773b6275-00474))_
- Given how hard concurrent programming can be, that is definitely a good thing. _(coding_little_go_book.pdf (source-range-773b6275-00475))_
- They are almost their own fundamental building block. _(coding_little_go_book.pdf (source-range-773b6275-00475))_
- There's little to say about goroutines other than they're effective and simple (simple to use anyway). _(coding_little_go_book.pdf (source-range-773b6275-00475))_
- Last but not least is the built-in support for concurrency. _(coding_little_go_book.pdf (source-range-773b6275-00475))_
- I do think learning about concurrent programming without channels is useful. _(coding_little_go_book.pdf (source-range-773b6275-00475))_
- Channels are more complicated. _(coding_little_go_book.pdf (source-range-773b6275-00475))_
- I always think it's important to understand basics before using high-level wrappers. _(coding_little_go_book.pdf (source-range-773b6275-00475))_
- I say this because they change how you write and think about concurrent programming. _(coding_little_go_book.pdf (source-range-773b6275-00475))_

> Still, it comes down to some basic rules (like you can only declare variable once and := does declare the variable) and fundamental understanding (like new(X) or &X{} only allocate memory, but slices, maps and channels require more initialization and thus, make ).
_(source: coding_little_go_book.pdf (source-range-773b6275-00473))_

## Source review

### Needs review

- Maybe it's a messaging, caching, computational-heavy data analysis, command line interface, logging or monitoring. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00016))_
- to put your projects. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00024))_
- Extract the file to /usr/local via tar -C /usr/local -xzf go#.#.#.darwin-amd64-osx10.8.tar.gz . — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00026))_
- Set up two environment variables: 1. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00026))_
- GOPATH points to your workspace, for me, that's $HOME/code/go . — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00026))_
- echo 'export GOPATH=$HOME/code/go' >> $HOME/.profile echo 'export PATH=$PATH:/usr/local/go/bin' >> $HOME/.profile You'll want to activate these variables. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00027))_
- go version version go1.3.3 darwin/amd64 . — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00028))_
- You'll hopefully get an output that looks like go version go1.3.3 windows/amd64 . — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00030))_
- GOPATH points to your workspace. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00030))_
- Set up two environment variables: 1. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00030))_
- Add c:\Go\bin to your PATH environment variable. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00030))_
- Unzip it at a location of your choosing. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00030))_
- Open a command prompt and type go version . — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00030))_
- Compiled languages can be unpleasant to work with because compilation can be slow. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00034))_
- Compiled languages tend to run faster and the executable can be run without additional dependencies (at least, that's true for languages — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00034))_
- like C, C++ and Go which compile directly to assembly). — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00035))_
- Being statically typed means that variables must be of a specific type (int, string, bool, []byte, etc.). — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00037))_
- In C, you'd literally free(str); the variable. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00046))_
- A variable local to a function, for example, disappears when the function exits. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00046))_
- In other cases, it isn't so obvious -- at least to a compiler. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00046))_
- Save the file as main.go . — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00051))_
- When you deploy your code however, you'll want to deploy a binary via go build and execute that. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00054))_
- We're now using two of Go's standard packages: fmt and os . — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00063))_
- len returns the size of a string, or the number of values in a dictionary, or, as we see here, the number of elements in an array. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00063))_
- We'll learn more about packages in later chapters. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00064))_
- Also, scroll to the top to learn more about Go's formatting capabilities. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00068))_
- Still, it'll probably take some time before you truly feel comfortable with it. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00073))_
- By default, Go assigns a zero value to variables. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00077))_
- Here, we declare a variable power of type int . — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00077))_
- Next, we assign 9000 to our power variable. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00077))_
- Still, that's a lot of typing. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00079))_
- There's more to learn about declaration and assignments. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00094))_
- Sometimes, you only care about one of the return values. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00100))_
- Finally, there's something else that you're likely to run into with function declarations. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00103))_
- Still, you'll run into all of these sooner than later so it's important to know about them. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00105))_
- Being able to return multiple values is something you'll use often. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00105))_
- Named return values and the slightly less verbose parameter declaration aren't that common. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00105))_
- I don't disagree with you. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00108))_
- Hopefully as we learn more, you'll appreciate the clean and terse syntax. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00109))_
- Inferred types and multiple return values are nice (though certainly not exclusive to Go). — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00109))_
- It comes down to the way Go passes arguments to a function: as copies. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00128))_
- We made two changes. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00132))_
- Think of it as copying the directions to a restaurant. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00133))_
- The above, once again, prints 9000. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00136))_
- All this isn't to say that you'll always want a pointer. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00138))_
- This pattern rubs a lot of developers the wrong way. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00147))_
- Despite the lack of constructors, Go does have a built-in new function which is used to allocate the memory required by a type. The result of new(X) is the same as &X{} : — _unextracted: segment carries subject matter but no structured claim was recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00151))_
- Many people think that it's a more robust way to share code. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00167))_
- For this reason, you'll see (and write) a lot of functions that look like Load , LoadById , LoadByName and so on. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00169))_
- Simply, Go doesn't support overloading. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00169))_
- While overloading isn't specific to structures, it's worth addressing. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00169))_
- - Return value from a function — _unextracted: segment carries subject matter but no structured claim was recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00177))_
- - The receiver of a method — _unextracted: segment carries subject matter but no structured claim was recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00179))_
- Even if you don't intend to change the data, consider the cost of creating a copy of large structures. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00182))_
- Unless you're iterating over thousands or possibly tens of thousands of such points, you wouldn't notice a difference. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00185))_
- It's now time to look at arrays, slices and maps. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00189))_
- So far we've seen a number of simple types and structures. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00189))_
- For this, we turn to slices. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00198))_
- In the above, we initialize a slice with a length of 10 and a capacity of 10. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00204))_
- This creates a slice with a length of 0 but with a capacity of 10. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00206))_
- To better understand the interplay between length and capacity, let's look at some examples: — _unextracted: segment carries subject matter but no structured claim was recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00207))_
- Our first example crashes. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00209))_
- But that changes the intent of our original code. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00211))_
- If I told you that Go grew arrays with a 2x algorithm, can you guess what the following will output? — _unextracted: segment carries subject matter but no structured claim was recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00214))_
- The [X:Y] syntax creates a slice of scores , starting from index 2 up until (but not including) index 4. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00234))_
- Unlike other languages, Go doesn't support negative values. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00239))_
- Take some time and play with the above code. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00246))_
- Maps grow dynamically. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00253))_
- There's yet another way to declare and initialize values in Go. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00260))_
- At this point, the same logic that we saw in Chapter 2 applies. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00268))_
- So with respect to passing/returning the slice itself, there's no difference. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00268))_
- If we peek beyond the superficial syntax of arrays, we find slices. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00270))_
- It's now time to look at how to organize our code. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00272))_
- Also, obviously, we aren't actually accessing the database. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00277))_
- As you start writing more complex systems, you're bound to run into cyclical imports. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00286))_
- This happens when package A imports package B but package B imports package A (either directly or indirectly through another package). — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00286))_
- Let's change our shopping structure to cause the error. — _unextracted: segment carries subject matter but no structured claim was recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00287))_
- Move the Item definition from shopping/db/db.go into shopping/pricecheck.go . — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00288))_
- If the name of the type or function starts with an uppercase letter, it's visible. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00299))_
- If it starts with a lowercase letter, it isn't. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00299))_
- This also applies to structure fields. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00300))_
- Go ahead and change the name of the various functions, types and fields from the shopping code. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00304))_
- go get fetches the remote files and stores them in your workspace. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00309))_
- Go ahead and check your $GOPATH/src . — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00309))_
- I know this looks like a URL but in reality, it'll simply import the gosqlite3 package which it expects to find in $GOPATH/src/github.com/mattn/go-sqlite3 . — _unextracted: segment carries subject matter but no structured claim was recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00312))_
- For one thing, there's no way to specify a revision, it always points to the master/head/trunk/default. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00316))_
- Interfaces help decouple your code from specific implementations. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00321))_
- How would you use one? Just like any other type, it could be a structure's field: — _unextracted: segment carries subject matter but no structured claim was recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00324))_
- This cuts down on the verboseness of using interfaces: } public class ConsoleLogger : Logger { public void Logger(message string) { Console.WriteLine(message) } } type ConsoleLogger struct {} (l ConsoleLogger) Log(message string) { — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00327))_
- In this chapter, we'll talk about a miscellany of Go's feature which didn't quite fit anywhere else. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00337))_
- Consider the strconv.Atoi function which takes a string and tries to convert it to an integer: — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00339))_
- There's a common pattern in Go's standard library of using error variables. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00346))_
- That's a pretty silly example. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00364))_
- Admittedly, it won't result in clean code. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00376))_
- Do note that when you use []byte(X) or string(X) , you're creating a copy of the data. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00382))_
- Of course, when you turn a string into a []byte you'll get the correct data. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00385))_
- Using functions like this can help decouple code from specific implementations much like we achieve with interfaces. — _unextracted: segment carries subject matter but no structured claim was recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00392))_
- Most notably, we saw how error handling behaves and how to release resources such as connections and open files. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00394))_
- Yet, I also find that it results in code that's easier to follow. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00394))_
- Many people dislike Go's approach to error handling. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00394))_
- Do note that anonymous functions aren't only used with goroutines, however. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00402))_
- What do you think the output will be? — _unextracted: segment carries subject matter but no structured claim was recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00412))_
- 20 you're both right and wrong. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00413))_
- A mutex serializes access to the code under lock. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00417))_
- In addition to the Lock and Unlock methods of a sync.Mutex , it also exposes RLock and RUnlock methods; where R stands for Read . — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00423))_
- This exposes two locking functions: one to lock for reading and one to lock for writing. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00423))_
- There's more to concurrent programming than what we've seen so far. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00423))_
- Furthermore, part of concurrent programming isn't so much about serializing access across the narrowest possible piece of code; it's also about coordinating multiple goroutines. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00424))_
- For example, sleeping for 10 milliseconds isn't a particularly elegant solution. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00424))_
- Given the above code, what happens if we have more data coming in than we can handle? You can simulate this by changing the worker to sleep after it has received data: — _unextracted: segment carries subject matter but no structured claim was recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00433))_
- Buffered channels don't add more capacity; they merely provide a queue for pending work and a good way to deal with a sudden spike. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00438))_
- We're willing to block for some time, but not forever. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00450))_
- There's nothing more magical than that. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00453))_
- select works the same regardless of whether we're receiving from, sending to, or any combination of channels: — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00459))_
- Pay close attention to our select . — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00459))_
- Notice that we're sending to c but receiving from time.After . — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00459))_
- - If there's no default, select blocks. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00463))_
- Finally, it's common to see a select inside a for . — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00464))_
- It categorically demands considerably more attention and care. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00467))_
- You start to think about concurrency with respect to message passing, rather than dangerous areas of code. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00468))_
- This doesn't just eliminate bugs, but it changes how one approaches concurrent programming. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00468))_
- Boring because it's easy to learn, easy to write and, most importantly, easy to read. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00471))_
- I always think it's important to understand basics before using high-level wrappers. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00475))_
- I say this because they change how you write and think about concurrent programming. — _fragmentary: no subject/predicate region recovered_ _(coding_little_go_book.pdf (source-range-773b6275-00475))_

### Disposition counts

- non-claim: 35
