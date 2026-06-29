---
page_id: coding-little-go-book-error-handling
page_kind: concept
summary: Error Handling: 6 statement(s) and 7 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-29
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-error-handling@b90ac0cb783297f1695d2f944c3b17c2
---

# Error Handling

What [[coding-little-go-book]] covers about error handling:

## Statements

### Chapter 5 - Tidbits / Error Handling

- Go's preferred way to deal with errors is through return values, not exceptions. Consider the strconv.Atoi function which takes a string and tries to convert it to an integer: _(coding_little_go_book.pdf (source-range-23d24eb1-00339))_

- You can create your own error type; the only requirement is that it fulfills the contract of the built-in error interface, which is: _(coding_little_go_book.pdf (source-range-23d24eb1-00341))_

- This is a package variable (it's defined outside of a function) which is publicly accessible (upper-case first letter). Various functions can return this error, say when we're reading from a file or STDIN. If it makes contextual sense, you should use this error, too. As consumers, we can use this singleton: _(coding_little_go_book.pdf (source-range-23d24eb1-00348))_

- As a final note, Go does have panic and recover functions. panic is like throwing an exception while recover is like catch ; they are rarely used. _(coding_little_go_book.pdf (source-range-23d24eb1-00350))_


## Technical atoms

### Technical frame 1: Chapter 5 - Tidbits / Error Handling

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00341))_

> You can create your own error type; the only requirement is that it fulfills the contract of the built-in error interface, which is:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00340))_

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

### Technical frame 2: Chapter 5 - Tidbits / Error Handling

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00348))_

> This is a package variable (it's defined outside of a function) which is publicly accessible (upper-case first letter). Various functions can return this error, say when we're reading from a file or STDIN. If it makes contextual sense, you should use this error, too. As consumers, we can use this singleton:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00342))_

```
type error interface {
  Error() string
}
```

### Technical frame 3: Chapter 5 - Tidbits / Error Handling

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00348))_

> This is a package variable (it's defined outside of a function) which is publicly accessible (upper-case first letter). Various functions can return this error, say when we're reading from a file or STDIN. If it makes contextual sense, you should use this error, too. As consumers, we can use this singleton:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00344))_

```
import (
```

### Technical frame 4: Chapter 5 - Tidbits / Error Handling

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00348))_

> This is a package variable (it's defined outside of a function) which is publicly accessible (upper-case first letter). Various functions can return this error, say when we're reading from a file or STDIN. If it makes contextual sense, you should use this error, too. As consumers, we can use this singleton:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00345))_

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

### Technical frame 5: Chapter 5 - Tidbits / Error Handling

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00348))_

> This is a package variable (it's defined outside of a function) which is publicly accessible (upper-case first letter). Various functions can return this error, say when we're reading from a file or STDIN. If it makes contextual sense, you should use this error, too. As consumers, we can use this singleton:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00347))_

```
var EOF = errors.New("EOF")
```

### Technical frame 6: Chapter 5 - Tidbits / Error Handling

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00350))_

> As a final note, Go does have panic and recover functions. panic is like throwing an exception while recover is like catch ; they are rarely used.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00348))_

> Various functions can return this error, say when we're reading from a file or STDIN.

### Technical frame 7: Chapter 5 - Tidbits / Error Handling

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00350))_

> As a final note, Go does have panic and recover functions. panic is like throwing an exception while recover is like catch ; they are rarely used.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00349))_

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


## Related pages

- [[coding-little-go-book-tidbit]] - shared statements and technical atoms: Tidbits shares source evidence from Chapter 5 - Tidbits / Error Handling: Go's preferred way to deal with errors is through return values, not exceptions. Consider the strconv.Atoi function which takes a string and tries to convert it to an integer:; Tidbits shares technical record from Chapter 5 - Tidbits / Error Handling: package main import ( "fmt" "os" "strconv" ) func main() { if len(os.Args) != 2 { os.Exit(1) } n, err := strconv.Atoi(os.Args[1]) if err != nil { fmt.Println("not a ... [truncated] (6 shared statement(s), 7 shared atom(s))
- [[coding-little-go-book-section-chapter-5-tidbits-error-handling-c2084411]] - source section: Chapter 5 - Tidbits / Error Handling shares source evidence from Chapter 5 - Tidbits / Error Handling: Go's preferred way to deal with errors is through return values, not exceptions. Consider the strconv.Atoi function which takes a string and tries to convert it to an integer:; Chapter 5 - Tidbits / Error Handling shares technical record from Chapter 5 - Tidbits / Error Handling: package main import ( "fmt" "os" "strconv" ) func main() { if len(os.Args) != 2 { os.Exit(1) } n, err := strconv.Atoi(os.Args[1]) if err != nil { fmt.Println("not a ... [truncated] (6 shared statement(s), 7 shared atom(s))

## Source

- [[coding-little-go-book]]
