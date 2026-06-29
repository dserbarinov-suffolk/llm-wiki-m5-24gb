---
page_id: coding-learn-go-with-tests-excerpt-section-hello-world-how-to-test-b6606620
page_kind: source
summary: Hello, World / How to test: 7 source-backed entries and 2 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-29
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-hello-world-how-to-test-b6606620@4d621ecd48e3ec8b6391deef201de427
---

# Hello, World / How to test

From [[coding-learn-go-with-tests-excerpt]].

## Related pages

- [[coding-learn-go-with-tests-excerpt-section-hello-world-72ad81c1]] - broader source section: Hello, World
- [[coding-learn-go-with-tests-excerpt-section-hello-world-how-it-works-e2369fdb]] - previous source section: Hello, World / How it works
- [[coding-learn-go-with-tests-excerpt-section-hello-world-go-modules-3cb7c993]] - next source section: Hello, World / Go modules?
- [[coding-learn-go-with-tests-excerpt-how-test]] - topic hub: opens the topic page for How Test

## Statements

- How do you test this? It is good to separate your "domain" code from the outside world (side-effects). The fmt.Println is a side effect (printing to stdout), and the string we send in is our domain. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00018))_
- We have created a new function with func , but this time, we've added another keyword, string, to the definition. This means this function returns a string . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00021))_
- This means this function returns a string . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00021))_

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
