---
page_id: coding-learn-go-with-tests-excerpt-how-test
page_kind: concept
summary: How to test: 4 statement(s) and 2 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-how-test@6ae8df3230cd54e867b83c5303a1c0d3
---

# How to test

What [[coding-learn-go-with-tests-excerpt]] covers about how to test:

## Statements

- This means this function returns a string . _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00021))_
- The fmt.Println is a side effect (printing to stdout), and the string we send in is our domain. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00018))_
- It is good to separate your "domain" code from the outside world (side-effects). _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00018))_
- We have created a new function with func , but this time, we've added another keyword, string, to the definition. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00021))_

## Technical atoms

```
package main
import "fmt"
func Hello() string {
    return "Hello, world"
}
func main() {
    fmt.Println(Hello())
}
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00020))_

> Context: We have created a new function with func , but this time, we've added another keyword, string, to the definition. This means this function returns a string .
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00021))_

```
package main
import "testing"
func TestHello(t *testing.T) {
    got := Hello()
    want := "Hello, world"
if got != want {
        t.Errorf("got %q want %q", got, want)
    }
}
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00023))_


## Source

- [[coding-learn-go-with-tests-excerpt]]
