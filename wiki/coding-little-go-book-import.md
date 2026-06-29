---
page_id: coding-little-go-book-import
page_kind: concept
summary: Imports: 12 statement(s) and 7 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-29
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-import@71469802c9b78c6f449c7ba624864b6e
---

# Imports

What [[coding-little-go-book]] covers about imports:

## Statements

### Chapter 1 - The Basics / Imports

- Go has a number of built-in functions, such as println , which can be used without reference. We can't get very far though, without making use of Go's standard library and eventually using third-party libraries. In Go, the import keyword is used to declare the packages that are used by the code in the file. Let's change our program: _(coding_little_go_book.pdf (source-range-23d24eb1-00058))_

- We're now using two of Go's standard packages: fmt and os . We've also introduced another built-in function len . len returns the size of a string, or the number of values in a dictionary, or, as we see here, the number of elements in an array. If you're wondering why we expect 2 arguments, it's because the first argument -- at index 0 -- is always the path of the currently running executable. (Change the program to print it out and see for yourself.) _(coding_little_go_book.pdf (source-range-23d24eb1-00063))_

- You've probably noticed we prefix the function name with the package, e.g., fmt.Println . This is different from many other languages. We'll learn more about packages in later chapters. For now, knowing how to import and use a package is a good start. _(coding_little_go_book.pdf (source-range-23d24eb1-00064))_

- Go is strict about importing packages. It will not compile if you import a package but don't use it. Try to run the following: _(coding_little_go_book.pdf (source-range-23d24eb1-00065))_

- You should get two errors about fmt and os being imported and not used. Can this get annoying? Absolutely. Over time, you'll get used to it (it'll still be annoying though). Go is strict about this because unused imports can slow compilation; admittedly a problem most of us don't have to this degree. _(coding_little_go_book.pdf (source-range-23d24eb1-00067))_

- Another thing to note is that Go's standard library is well documented. You can head over to https://golang.org/pkg/fmt/#Println to learn more about the Println function that we used. You can click on that section header and see the source code. Also, scroll to the top to learn more about Go's formatting capabilities. _(coding_little_go_book.pdf (source-range-23d24eb1-00068))_


## Technical atoms

### Technical frame 1: Chapter 1 - The Basics / Imports

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

### Technical frame 2: Chapter 1 - The Basics / Imports

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00063))_

> We're now using two of Go's standard packages: fmt and os . We've also introduced another built-in function len . len returns the size of a string, or the number of values in a dictionary, or, as we see here, the number of elements in an array. If you're wondering why we expect 2 arguments, it's because the first argument -- at index 0 -- is always the path of the currently running executable. (Change the program to print it out and see for yourself.)

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00062))_

```
go run main.go 9000
```

### Technical frame 3: Chapter 1 - The Basics / Imports

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00064))_

> You've probably noticed we prefix the function name with the package, e.g., fmt.Println . This is different from many other languages. We'll learn more about packages in later chapters. For now, knowing how to import and use a package is a good start.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00063))_

> If you're wondering why we expect 2 arguments, it's because the first argument -- at index 0 -- is always the path of the currently running executable.

### Technical frame 4: Chapter 1 - The Basics / Imports

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

### Technical frame 5: Chapter 1 - The Basics / Imports

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00068))_

> Another thing to note is that Go's standard library is well documented. You can head over to https://golang.org/pkg/fmt/#Println to learn more about the Println function that we used. You can click on that section header and see the source code. Also, scroll to the top to learn more about Go's formatting capabilities.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00067))_

> You should get two errors about fmt and os being imported and not used.

### Technical frame 6: Chapter 1 - The Basics / Imports

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00068))_

> Another thing to note is that Go's standard library is well documented. You can head over to https://golang.org/pkg/fmt/#Println to learn more about the Println function that we used. You can click on that section header and see the source code. Also, scroll to the top to learn more about Go's formatting capabilities.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00069))_

> If you're ever stuck without internet access, you can get the documentation running locally via:

### Technical frame 7: Chapter 1 - The Basics / Imports

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00068))_

> Another thing to note is that Go's standard library is well documented. You can head over to https://golang.org/pkg/fmt/#Println to learn more about the Println function that we used. You can click on that section header and see the source code. Also, scroll to the top to learn more about Go's formatting capabilities.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00070))_

```
godoc -http=:6060
```


## Related pages

- [[coding-little-go-book-basic]] - shared statements and technical atoms: The Basics shares source evidence from Chapter 1 - The Basics / Imports: Go has a number of built-in functions, such as println , which can be used without reference. We can't get very far though, without making use of Go's standard libra ... [truncated]; The Basics shares technical record from Chapter 1 - The Basics / Imports: func main() { if len(os.Args) != 2 { os.Exit(1) } fmt.Println("It's over", os.Args[1]) } (12 shared statement(s), 7 shared atom(s))
- [[coding-little-go-book-section-chapter-1-the-basics-imports-2cc727c8]] - source section: Chapter 1 - The Basics / Imports shares source evidence from Chapter 1 - The Basics / Imports: Go has a number of built-in functions, such as println , which can be used without reference. We can't get very far though, without making use of Go's standard libra ... [truncated]; Chapter 1 - The Basics / Imports shares technical record from Chapter 1 - The Basics / Imports: func main() { if len(os.Args) != 2 { os.Exit(1) } fmt.Println("It's over", os.Args[1]) } (12 shared statement(s), 7 shared atom(s))

## Source

- [[coding-little-go-book]]
