---
page_id: coding-little-go-book-section-chapter-1-the-basics-45e21143
page_kind: source
summary: Chapter 1 - The Basics: 110 source-backed entries and 28 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-29
domain: coding-little-go-book
category_path: sources/coding-little-go-book/sections
source_id: coding_little_go_book.pdf
projection_coverage: section-coding-little-go-book-section-chapter-1-the-basics-45e21143@39a7828dc06952223119f89034fbc178
---

# Chapter 1 - The Basics

From [[coding-little-go-book]].

## Related pages

- [[coding-little-go-book-section-chapter-1-the-basics-compilation-a383d435]] - narrower source section: Chapter 1 - The Basics / Compilation
- [[coding-little-go-book-section-chapter-1-the-basics-static-typing-475d2733]] - narrower source section: Chapter 1 - The Basics / Static Typing
- [[coding-little-go-book-section-chapter-1-the-basics-c-like-syntax-4fda7deb]] - narrower source section: Chapter 1 - The Basics / C-Like Syntax
- [[coding-little-go-book-section-chapter-1-the-basics-garbage-collected-538d2af8]] - narrower source section: Chapter 1 - The Basics / Garbage Collected
- [[coding-little-go-book-section-chapter-1-the-basics-running-go-code-f8398d4c]] - narrower source section: Chapter 1 - The Basics / Running Go Code
- [[coding-little-go-book-section-chapter-1-the-basics-imports-2cc727c8]] - narrower source section: Chapter 1 - The Basics / Imports
- [[coding-little-go-book-section-chapter-1-the-basics-variables-and-declarations-dd932e02]] - narrower source section: Chapter 1 - The Basics / Variables and Declarations
- [[coding-little-go-book-section-chapter-1-the-basics-function-declarations-0fdfbbc5]] - narrower source section: Chapter 1 - The Basics / Function Declarations
- [[coding-little-go-book-section-chapter-1-the-basics-before-you-continue-b0ff71fd]] - narrower source section: Chapter 1 - The Basics / Before You Continue
- [[coding-little-go-book-section-getting-started-c2e397c0]] - previous source section: Getting Started
- [[coding-little-go-book-section-chapter-2-structures-59a89c52]] - next source section: Chapter 2 - Structures
- [[coding-little-go-book-basic]] - topic hub: opens the topic page for Basic

## Statements

- Go is a compiled, statically typed language with a C-like syntax and garbage collection. What does that mean? _(coding_little_go_book.pdf (source-range-23d24eb1-00032))_

## Statements by subsection

### Chapter 1 - The Basics / Compilation

- Compilation is the process of translating the source code that you write into a lower level language -- either assembly (as is the case with Go), or some other intermediary language (as with Java and C#). Compiled languages can be unpleasant to work with because compilation can be slow. It's hard to iterate quickly if you have to spend minutes or hours waiting for code to compile. Compilation speed is one of the major design goals of Go. This is good news for people working on large projects as well as those of us used to a quick feedback cycle offered by interpreted languages. Compiled languages tend to run faster and the executable can be run without additional dependencies (at least, that's true for languages _(coding_little_go_book.pdf (source-range-23d24eb1-00034))_
- Compiled languages can be unpleasant to work with because compilation can be slow. _(coding_little_go_book.pdf (source-range-23d24eb1-00034))_

### Chapter 1 - The Basics / Static Typing

- Being statically typed means that variables must be of a specific type (int, string, bool, []byte, etc.). This is either achieved by specifying the type when the variable is declared or, in many cases, letting the compiler infer the type (we'll look at examples shortly). There's a lot more that can be said about static typing, but I believe it's something better understood by looking at code. If you're used to dynamically typed languages, you might find this cumbersome. You're not wrong, but there are advantages, especially when you pair static typing with compilation. The two are often conflated. It's true that when you have one, you normally have the other but it isn't a hard rule. With a rigid type system, a compiler is able to detect problems beyond mere syntactical mistakes as well as make further optimizations. _(coding_little_go_book.pdf (source-range-23d24eb1-00037))_
- Being statically typed means that variables must be of a specific type (int, string, bool, []byte, etc.). _(coding_little_go_book.pdf (source-range-23d24eb1-00037))_

### Chapter 1 - The Basics / C-Like Syntax

- Saying that a language has a C-like syntax means that if you're used to any other C-like languages such as C, C++, Java, JavaScript and C#, then you're going to find Go familiar -- superficially, at least. For example, it means && is used as a boolean AND, == is used to compare equality, { and } start and end a scope, and array indexes start at 0. _(coding_little_go_book.pdf (source-range-23d24eb1-00039))_
- C-like syntax also tends to mean semi-colon terminated lines and parentheses around conditions. Go does away with both of these, though parentheses are still used to control precedence. For example, an if statement looks like this: _(coding_little_go_book.pdf (source-range-23d24eb1-00040))_
- Beyond this, Go is much closer to C than C# or Java - not only in terms of syntax, but in terms of purpose. That's reflected in the terseness and simplicity of the language which will hopefully start to become obvious as you learn it. _(coding_little_go_book.pdf (source-range-23d24eb1-00044))_
- Saying that a language has a C-like syntax means that if you're used to any other C-like languages such as C, C++, Java, JavaScript and C#, then you're going to find Go familiar -- superficially, at least. _(coding_little_go_book.pdf (source-range-23d24eb1-00039))_
- Beyond this, Go is much closer to C than C# or Java - not only in terms of syntax, but in terms of purpose. _(coding_little_go_book.pdf (source-range-23d24eb1-00044))_

### Chapter 1 - The Basics / Garbage Collected

- Some variables, when created, have an easy-to-define life. A variable local to a function, for example, disappears when the function exits. In other cases, it isn't so obvious -- at least to a compiler. For example, the lifetime of a variable returned by a function or referenced by other variables and objects can be tricky to determine. Without garbage collection, it's up to developers to free the memory associated with such variables at a point where the developer knows the variable isn't needed. How? In C, you'd literally free(str); the variable. _(coding_little_go_book.pdf (source-range-23d24eb1-00046))_
- Languages with garbage collectors (e.g., Ruby, Python, Java, JavaScript, C#, Go) are able to keep track of these and free them when they're no longer used. Garbage collection adds overhead, but it also eliminates a number of devastating bugs. _(coding_little_go_book.pdf (source-range-23d24eb1-00047))_
- A variable local to a function, for example, disappears when the function exits. _(coding_little_go_book.pdf (source-range-23d24eb1-00046))_

### Chapter 1 - The Basics / Running Go Code

- Save the file as main.go . For now, you can save it anywhere you want; we don't need to live inside Go's workspace for trivial examples. _(coding_little_go_book.pdf (source-range-23d24eb1-00051))_
- Next, open a shell/command prompt and change the directory to where you saved the file. For me, that means typing cd ~/code . _(coding_little_go_book.pdf (source-range-23d24eb1-00052))_
- go run main.go If everything worked, you should see it's over 9000! . But wait, what about the compilation step? go run is a handy command that compiles and runs your code. It uses a temporary directory to build the program, executes it and then cleans itself up. You can see the location of the temporary file by running: go run --work main.go To explicitly compile code, use go build : go build main.go This will generate an executable main which you can run. On Linux / OSX, don't forget that you need to prefix the executable with dotslash, so you need to type ./main . While developing, you can use either go run or go build . When you deploy your code however, you'll want to deploy a binary via go build and execute that. _(coding_little_go_book.pdf (source-range-23d24eb1-00054))_
- For now, you can save it anywhere you want; we don't need to live inside Go's workspace for trivial examples. _(coding_little_go_book.pdf (source-range-23d24eb1-00051))_
- For me, that means typing cd ~/code . _(coding_little_go_book.pdf (source-range-23d24eb1-00052))_
- It uses a temporary directory to build the program, executes it and then cleans itself up. _(coding_little_go_book.pdf (source-range-23d24eb1-00054))_

### Chapter 1 - The Basics / Imports

- Go has a number of built-in functions, such as println , which can be used without reference. We can't get very far though, without making use of Go's standard library and eventually using third-party libraries. In Go, the import keyword is used to declare the packages that are used by the code in the file. Let's change our program: _(coding_little_go_book.pdf (source-range-23d24eb1-00058))_
- We're now using two of Go's standard packages: fmt and os . We've also introduced another built-in function len . len returns the size of a string, or the number of values in a dictionary, or, as we see here, the number of elements in an array. If you're wondering why we expect 2 arguments, it's because the first argument -- at index 0 -- is always the path of the currently running executable. (Change the program to print it out and see for yourself.) _(coding_little_go_book.pdf (source-range-23d24eb1-00063))_
- You've probably noticed we prefix the function name with the package, e.g., fmt.Println . This is different from many other languages. We'll learn more about packages in later chapters. For now, knowing how to import and use a package is a good start. _(coding_little_go_book.pdf (source-range-23d24eb1-00064))_
- Go is strict about importing packages. It will not compile if you import a package but don't use it. Try to run the following: _(coding_little_go_book.pdf (source-range-23d24eb1-00065))_
- You should get two errors about fmt and os being imported and not used. Can this get annoying? Absolutely. Over time, you'll get used to it (it'll still be annoying though). Go is strict about this because unused imports can slow compilation; admittedly a problem most of us don't have to this degree. _(coding_little_go_book.pdf (source-range-23d24eb1-00067))_
- Another thing to note is that Go's standard library is well documented. You can head over to https://golang.org/pkg/fmt/#Println to learn more about the Println function that we used. You can click on that section header and see the source code. Also, scroll to the top to learn more about Go's formatting capabilities. _(coding_little_go_book.pdf (source-range-23d24eb1-00068))_
- Go has a number of built-in functions, such as println , which can be used without reference. _(coding_little_go_book.pdf (source-range-23d24eb1-00058))_
- Go is strict about this because unused imports can slow compilation; admittedly a problem most of us don't have to this degree. _(coding_little_go_book.pdf (source-range-23d24eb1-00067))_

### Chapter 1 - The Basics / Variables and Declarations

- It'd be nice to begin and end our look at variables by saying you declare and assign to a variable by doing x = 4. Unfortunately, things are more complicated in Go. We'll begin our conversation by looking at simple examples. Then, in the next chapter, we'll expand this when we look at creating and using structures. Still, it'll probably take some time before you truly feel comfortable with it. _(coding_little_go_book.pdf (source-range-23d24eb1-00073))_
- You might be thinking Woah! What can be so complicated about this? Let's start looking at some examples. _(coding_little_go_book.pdf (source-range-23d24eb1-00074))_
- The most explicit way to deal with variable declaration and assignment in Go is also the most verbose: _(coding_little_go_book.pdf (source-range-23d24eb1-00075))_
- Here, we declare a variable power of type int . By default, Go assigns a zero value to variables. Integers are assigned 0 , booleans false , strings "" and so on. Next, we assign 9000 to our power variable. We can merge the first two lines: _(coding_little_go_book.pdf (source-range-23d24eb1-00077))_
- Still, that's a lot of typing. Go has a handy short variable declaration operator, := , which can infer the type: _(coding_little_go_book.pdf (source-range-23d24eb1-00079))_
- It's important that you remember that := is used to declare the variable as well as assign a value to it. Why? Because a variable can't be declared twice (not in the same scope anyway). If you try to run the following, you'll get an error. _(coding_little_go_book.pdf (source-range-23d24eb1-00083))_
- The compiler will complain with no new variables on left side of := . This means that when we first declare a variable, we use := but on subsequent assignment, we use the assignment operator = . This makes a lot of sense, but it can be tricky for your muscle memory to remember when to switch between the two. _(coding_little_go_book.pdf (source-range-23d24eb1-00085))_
- If you read the error message closely, you'll notice that variables is plural. That's because Go lets you assign multiple variables (using either = or := ): _(coding_little_go_book.pdf (source-range-23d24eb1-00086))_
- As long as one of the variables is new, := can be used. Consider: _(coding_little_go_book.pdf (source-range-23d24eb1-00088))_
- Although power is being used twice with := , the compiler won't complain the second time we use it, it'll see that the other variable, name , is a new variable and allow := . However, you can't change the type of power . It was declared (implicitly) as an integer and thus, can only be assigned integers. _(coding_little_go_book.pdf (source-range-23d24eb1-00090))_
- For now, the last thing to know is that, like imports, Go won't let you have unused variables. For example, _(coding_little_go_book.pdf (source-range-23d24eb1-00091))_
- won't compile because name is declared but not used. Like unused imports it'll cause some frustration, but overall I think it helps with code cleanliness and readability. _(coding_little_go_book.pdf (source-range-23d24eb1-00093))_
- There's more to learn about declaration and assignments. For now, remember that you'll use var NAME TYPE when declaring a variable to its zero value, NAME := VALUE when declaring and assigning a value, and NAME = VALUE when assigning to a previously declared variable. _(coding_little_go_book.pdf (source-range-23d24eb1-00094))_
- Still, it'll probably take some time before you truly feel comfortable with it. _(coding_little_go_book.pdf (source-range-23d24eb1-00073))_
- Because a variable can't be declared twice (not in the same scope anyway). _(coding_little_go_book.pdf (source-range-23d24eb1-00083))_
- This means that when we first declare a variable, we use := but on subsequent assignment, we use the assignment operator = . _(coding_little_go_book.pdf (source-range-23d24eb1-00085))_
- It was declared (implicitly) as an integer and thus, can only be assigned integers. _(coding_little_go_book.pdf (source-range-23d24eb1-00090))_
- won't compile because name is declared but not used. _(coding_little_go_book.pdf (source-range-23d24eb1-00093))_

### Chapter 1 - The Basics / Function Declarations

- This is a good time to point out that functions can return multiple values. Let's look at three functions: one with no return value, one with one return value, and one with two return values. _(coding_little_go_book.pdf (source-range-23d24eb1-00096))_
- This is more than a convention. _ , the blank identifier, is special in that the return value isn't actually assigned. This lets you use _ over and over again regardless of the returned type. _(coding_little_go_book.pdf (source-range-23d24eb1-00102))_
- Being able to return multiple values is something you'll use often. You'll also frequently use _ to discard a value. Named return values and the slightly less verbose parameter declaration aren't that common. Still, you'll run into all of these sooner than later so it's important to know about them. _(coding_little_go_book.pdf (source-range-23d24eb1-00105))_
- Sometimes, you only care about one of the return values. _(coding_little_go_book.pdf (source-range-23d24eb1-00100))_

### Chapter 1 - The Basics / Before You Continue

- We looked at a number of small individual pieces and it probably feels disjointed at this point. We'll slowly build larger examples and hopefully, the pieces will start to come together. _(coding_little_go_book.pdf (source-range-23d24eb1-00107))_
- If you're coming from a dynamic language, the complexity around types and declarations might seem like a step backwards. I don't disagree with you. For some systems, dynamic languages are categorically more productive. _(coding_little_go_book.pdf (source-range-23d24eb1-00108))_
- If you're coming from a statically typed language, you're probably feeling comfortable with Go. Inferred types and multiple return values are nice (though certainly not exclusive to Go). Hopefully as we learn more, you'll appreciate the clean and terse syntax. _(coding_little_go_book.pdf (source-range-23d24eb1-00109))_

## Technical atoms

### Technical frame 1: Chapter 1 - The Basics / Compilation

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00034))_

> It's hard to iterate quickly if you have to spend minutes or hours waiting for code to compile.

### Technical frame 2: Chapter 1 - The Basics / C-Like Syntax

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00044))_

> Beyond this, Go is much closer to C than C# or Java - not only in terms of syntax, but in terms of purpose. That's reflected in the terseness and simplicity of the language which will hopefully start to become obvious as you learn it.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00041))_

```
if name == "Leto" {
  print("the spice must flow")
}
```

### Technical frame 3: Chapter 1 - The Basics / C-Like Syntax

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00044))_

> Beyond this, Go is much closer to C than C# or Java - not only in terms of syntax, but in terms of purpose. That's reflected in the terseness and simplicity of the language which will hopefully start to become obvious as you learn it.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00043))_

```
if (name == "Goku" && power > 9000) || (name == "gohan" && power < 
4000)  {
print("super Saiyan")
}
```

### Technical frame 4: Chapter 1 - The Basics / Running Go Code

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00051))_

> Save the file as main.go . For now, you can save it anywhere you want; we don't need to live inside Go's workspace for trivial examples.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00050))_

```
package main
func main() {
  println("it's over 9000!")
}
```

### Technical frame 5: Chapter 1 - The Basics / Running Go Code

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00052))_

> Next, open a shell/command prompt and change the directory to where you saved the file. For me, that means typing cd ~/code .

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00054))_

> go run main.go If everything worked, you should see it's over 9000!

### Technical frame 6: Chapter 1 - The Basics / Running Go Code / Main

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00056))_

> If you want, you can alter the code and change the package name.

### Technical frame 7: Chapter 1 - The Basics / Running Go Code / Main

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00056))_

> Hopefully, the code that we just executed is understandable. We've created a function and printed out a string with the built-in println function. Did go run know what to execute because there was only a single choice? No. In Go, the entry point to a program has to be a function called main within a package main . We'll talk more about packages in a later chapter. For now, while we focus on understanding the basics of Go, we'll always write our code within the main package. If you want, you can alter the code and change the package name. Run the code via go run and you should get an error. Then, change the name back to main but use a different function name. You should see a different error message. Try making those same changes but use go build instead. Notice that the code compiles, there's just no entry point to run it. This is perfectly normal when you are, for example, building a library.

### Technical frame 8: Chapter 1 - The Basics / Imports

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00063))_

> We're now using two of Go's standard packages: fmt and os . We've also introduced another built-in function len . len returns the size of a string, or the number of values in a dictionary, or, as we see here, the number of elements in an array. If you're wondering why we expect 2 arguments, it's because the first argument -- at index 0 -- is always the path of the currently running executable. (Change the program to print it out and see for yourself.)

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00059))_

> [Figure] (p.7)

### Technical frame 9: Chapter 1 - The Basics / Imports

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00063))_

> We're now using two of Go's standard packages: fmt and os . We've also introduced another built-in function len . len returns the size of a string, or the number of values in a dictionary, or, as we see here, the number of elements in an array. If you're wondering why we expect 2 arguments, it's because the first argument -- at index 0 -- is always the path of the currently running executable. (Change the program to print it out and see for yourself.)

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00060))_

```
func main() {
  if len(os.Args) != 2 {
    os.Exit(1)
  }
  fmt.Println("It's over", os.Args[1])
}
```

### Technical frame 10: Chapter 1 - The Basics / Imports

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00063))_

> We're now using two of Go's standard packages: fmt and os . We've also introduced another built-in function len . len returns the size of a string, or the number of values in a dictionary, or, as we see here, the number of elements in an array. If you're wondering why we expect 2 arguments, it's because the first argument -- at index 0 -- is always the path of the currently running executable. (Change the program to print it out and see for yourself.)

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00062))_

```
go run main.go 9000
```

### Technical frame 11: Chapter 1 - The Basics / Imports

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00064))_

> You've probably noticed we prefix the function name with the package, e.g., fmt.Println . This is different from many other languages. We'll learn more about packages in later chapters. For now, knowing how to import and use a package is a good start.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00063))_

> If you're wondering why we expect 2 arguments, it's because the first argument -- at index 0 -- is always the path of the currently running executable.

### Technical frame 12: Chapter 1 - The Basics / Imports

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00067))_

> You should get two errors about fmt and os being imported and not used. Can this get annoying? Absolutely. Over time, you'll get used to it (it'll still be annoying though). Go is strict about this because unused imports can slow compilation; admittedly a problem most of us don't have to this degree.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00066))_

```
package main
import (
  "fmt"
  "os"
)
func main() {
}
```

### Technical frame 13: Chapter 1 - The Basics / Imports

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00068))_

> Another thing to note is that Go's standard library is well documented. You can head over to https://golang.org/pkg/fmt/#Println to learn more about the Println function that we used. You can click on that section header and see the source code. Also, scroll to the top to learn more about Go's formatting capabilities.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00067))_

> You should get two errors about fmt and os being imported and not used.

### Technical frame 14: Chapter 1 - The Basics / Imports

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00068))_

> Another thing to note is that Go's standard library is well documented. You can head over to https://golang.org/pkg/fmt/#Println to learn more about the Println function that we used. You can click on that section header and see the source code. Also, scroll to the top to learn more about Go's formatting capabilities.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00069))_

> If you're ever stuck without internet access, you can get the documentation running locally via:

### Technical frame 15: Chapter 1 - The Basics / Imports

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00068))_

> Another thing to note is that Go's standard library is well documented. You can head over to https://golang.org/pkg/fmt/#Println to learn more about the Println function that we used. You can click on that section header and see the source code. Also, scroll to the top to learn more about Go's formatting capabilities.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00070))_

```
godoc -http=:6060
```

### Technical frame 16: Chapter 1 - The Basics / Variables and Declarations

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00077))_

> Here, we declare a variable power of type int . By default, Go assigns a zero value to variables. Integers are assigned 0 , booleans false , strings "" and so on. Next, we assign 9000 to our power variable. We can merge the first two lines:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00076))_

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

### Technical frame 17: Chapter 1 - The Basics / Variables and Declarations

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00079))_

> Still, that's a lot of typing. Go has a handy short variable declaration operator, := , which can infer the type:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00078))_

```
var power int = 9000
```

### Technical frame 18: Chapter 1 - The Basics / Variables and Declarations

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00083))_

> It's important that you remember that := is used to declare the variable as well as assign a value to it. Why? Because a variable can't be declared twice (not in the same scope anyway). If you try to run the following, you'll get an error.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00080))_

```
power := 9000
```

### Technical frame 19: Chapter 1 - The Basics / Variables and Declarations

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00083))_

> It's important that you remember that := is used to declare the variable as well as assign a value to it. Why? Because a variable can't be declared twice (not in the same scope anyway). If you try to run the following, you'll get an error.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00082))_

```
func main() {
  power := getPower()
}
func getPower() int {
  return 9001
}
```

### Technical frame 20: Chapter 1 - The Basics / Variables and Declarations

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00085))_

> The compiler will complain with no new variables on left side of := . This means that when we first declare a variable, we use := but on subsequent assignment, we use the assignment operator = . This makes a lot of sense, but it can be tricky for your muscle memory to remember when to switch between the two.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00083))_

> If you try to run the following, you'll get an error.

### Technical frame 21: Chapter 1 - The Basics / Variables and Declarations

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00085))_

> The compiler will complain with no new variables on left side of := . This means that when we first declare a variable, we use := but on subsequent assignment, we use the assignment operator = . This makes a lot of sense, but it can be tricky for your muscle memory to remember when to switch between the two.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00084))_

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

### Technical frame 22: Chapter 1 - The Basics / Variables and Declarations

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00088))_

> As long as one of the variables is new, := can be used. Consider:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00087))_

```
func main() {
  name, power := "Goku", 9000
  fmt.Printf("%s's power is over %d\n", name, power)
}
```

### Technical frame 23: Chapter 1 - The Basics / Variables and Declarations

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00090))_

> Although power is being used twice with := , the compiler won't complain the second time we use it, it'll see that the other variable, name , is a new variable and allow := . However, you can't change the type of power . It was declared (implicitly) as an integer and thus, can only be assigned integers.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00089))_

```
func main() {
  power := 1000
  fmt.Printf("default power is %d\n", power)
name, power := "Goku", 9000
  fmt.Printf("%s's power is over %d\n", name, power)
}
```

### Technical frame 24: Chapter 1 - The Basics / Variables and Declarations

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00093))_

> won't compile because name is declared but not used. Like unused imports it'll cause some frustration, but overall I think it helps with code cleanliness and readability.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00092))_

```
func main() {
  name, power := "Goku", 1000
  fmt.Printf("default power is %d\n", power)
}
```

### Technical frame 25: Chapter 1 - The Basics / Function Declarations

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00102))_

> This is more than a convention. _ , the blank identifier, is special in that the return value isn't actually assigned. This lets you use _ over and over again regardless of the returned type.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00097))_

```
func log(message string) {
}
func add(a int, b int) int {
}
func power(name string) (int, bool) {
}
```

### Technical frame 26: Chapter 1 - The Basics / Function Declarations

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00102))_

> This is more than a convention. _ , the blank identifier, is special in that the return value isn't actually assigned. This lets you use _ over and over again regardless of the returned type.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00099))_

```
value, exists := power("goku")
if exists == false {
  // handle this error case
}
```

### Technical frame 27: Chapter 1 - The Basics / Function Declarations

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00102))_

> This is more than a convention. _ , the blank identifier, is special in that the return value isn't actually assigned. This lets you use _ over and over again regardless of the returned type.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00101))_

```
_, exists := power("goku")
if exists == false {
  // handle this error case
}
```

### Technical frame 28: Chapter 1 - The Basics / Function Declarations

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00105))_

> Being able to return multiple values is something you'll use often. You'll also frequently use _ to discard a value. Named return values and the slightly less verbose parameter declaration aren't that common. Still, you'll run into all of these sooner than later so it's important to know about them.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00104))_

```
func add(a, b int) int {
}
```
