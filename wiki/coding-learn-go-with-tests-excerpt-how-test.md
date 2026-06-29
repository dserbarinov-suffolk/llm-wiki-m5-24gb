---
page_id: coding-learn-go-with-tests-excerpt-how-test
page_kind: concept
summary: How to test: 4 statement(s) and 2 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-29
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-how-test@0a8923101853603689761a58d7c02a5e
---

# How to test

What [[coding-learn-go-with-tests-excerpt]] covers about how to test:

## Statements

### Hello, World / How to test

- How do you test this? It is good to separate your "domain" code from the outside world (side-effects). The fmt.Println is a side effect (printing to stdout), and the string we send in is our domain. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00018))_

- We have created a new function with func , but this time, we've added another keyword, string, to the definition. This means this function returns a string . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00021))_


## Technical atoms

### Technical frame 1: Hello, World / How to test

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00021))_

> We have created a new function with func , but this time, we've added another keyword, string, to the definition. This means this function returns a string .

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00020))_

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

### Technical frame 2: Hello, World / How to test

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00021))_

> We have created a new function with func , but this time, we've added another keyword, string, to the definition. This means this function returns a string .

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00023))_

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


## Related pages

- [[coding-learn-go-with-tests-excerpt-hello]] - shared statements and technical atoms: Hello, World shares source evidence from Hello, World / How to test: How do you test this? It is good to separate your "domain" code from the outside world (side-effects). The fmt.Println is a side effect (printing to stdout), and the ... [truncated]; Hello, World shares technical record from Hello, World / How to test: package main import "fmt" func Hello() string { return "Hello, world" } func main() { fmt.Println(Hello()) } (4 shared statement(s), 2 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-section-hello-world-how-to-test-b6606620]] - source section: Hello, World / How to test shares source evidence from Hello, World / How to test: How do you test this? It is good to separate your "domain" code from the outside world (side-effects). The fmt.Println is a side effect (printing to stdout), and the ... [truncated]; Hello, World / How to test shares technical record from Hello, World / How to test: package main import "fmt" func Hello() string { return "Hello, world" } func main() { fmt.Println(Hello()) } (4 shared statement(s), 2 shared atom(s))

## Source

- [[coding-learn-go-with-tests-excerpt]]
