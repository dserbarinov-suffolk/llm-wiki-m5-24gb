---
page_id: coding-learn-go-with-tests-excerpt-hello
page_kind: concept
summary: Hello, world... again: 17 statement(s) and 6 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-hello@58e3fe156fe5fb8b9f2e0faaee42d5c5
---

# Hello, world... again

What [[coding-learn-go-with-tests-excerpt]] covers about hello, world... again:

## Statements

- The next requirement is when our function is called with an empty string it defaults to printing "Hello, World", rather than "Hello, ". _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00072))_
- Here, we are introducing another tool in our testing arsenal: subtests. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00075))_
- Sometimes, it is useful to group tests around a "thing" and then have subtests describing different scenarios. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00075))_
- A benefit of this approach is you can set up shared code that can be used in the other tests. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00076))_
- If we run our tests we should see it satisfies the new requirement and we haven't accidentally broken the other functionality. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00080))_
- It is important that your tests are clear specifications of what the code needs to do. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00081))_
- But there is repeated code when we check if the message is what we expect. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00081))_
- Refactoring is not just for the production code! _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00082))_
- Now that the tests are passing, we can and should refactor our tests. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00083))_
- We need to pass in t *testing.T so that we can tell the test code to fail when we need to. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00086))_
- We've refactored our assertion into a new function. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00086))_
- If you still don't understand, comment it out, make a test fail and observe the test output. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00088))_
- t.Helper() is needed to tell the test suite that this method is a helper. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00088))_
- This will help other developers track down problems more easily. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00088))_

## Technical atoms

```
func TestHello(t *testing.T) {
    t.Run("saying hello to people", func(t *testing.T) {
        got := Hello("Chris")
        want := "Hello, Chris"
if got != want {
            t.Errorf("got %q want %q", got, want)
        }
    })
    t.Run("say 'Hello, World' when an empty string is supplied", 
func(t *testing.T) {
got := Hello("")
        want := "Hello, World"
if got != want {
            t.Errorf("got %q want %q", got, want)
        }
    })
}
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00074))_

> Context: While we have a failing test, let's fix the code, using an if .
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00077))_

```
const englishHelloPrefix = "Hello, "
func Hello(name string) string {
    if name == "" {
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00078))_

> Context: While we have a failing test, let's fix the code, using an if .
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00077))_

```
name = "World"
    }
    return englishHelloPrefix + name
}
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00079))_

> Context: Now that the tests are passing, we can and should refactor our tests.
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00083))_

```
func TestHello(t *testing.T) {
    t.Run("saying hello to people", func(t *testing.T) {
        got := Hello("Chris")
        want := "Hello, Chris"
        assertCorrectMessage(t, got, want)
    })
t.Run("empty string defaults to 'world'", func(t *testing.T) {
        got := Hello("")
        want := "Hello, World"
        assertCorrectMessage(t, got, want)
    })
}
func assertCorrectMessage(t testing.TB, got, want string) {
    t.Helper()
    if got != want {
        t.Errorf("got %q want %q", got, want)
    }
}
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00084))_

> Context: We've refactored our assertion into a new function. This reduces duplication and improves the readability of our tests. We need to pass in t *testing.T so that we can tell the test code to fail when we need to. t.Helper() is needed to tell the test suite that this method is a helper. By doing this, when it fails, the line number reported will be in our function call rather than inside our test helper. This will help other developers track down problems more easily. If you still don't understand, comment it out, make a test fail and observe the test output. Comments in Go are a great way to add additional information to your code, or in this case, a quick way to tell the compiler to ignore a line. You can comment out the t.Helper() code by adding two forward slashes // at the beginning of the line. You should see that line turn grey or change to another color than the rest of your code to indicate it's now commented out.
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00086, source-range-f4b7154d-00088))_

> For helper functions, it's a good idea to accept a testing.TB which is an interface that *testing.T and *testing.B both satisfy, so you can call helper functions from a test, or a benchmark (don't worry if words like "interface" mean nothing to you right now, it will be covered later).
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00087))_

> Context: We've refactored our assertion into a new function. This reduces duplication and improves the readability of our tests. We need to pass in t *testing.T so that we can tell the test code to fail when we need to.
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00086))_

> When you have more than one argument of the same type (in our case two strings) rather than having (got string, want string) you can shorten it to (got, want string) .
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00089))_


## Source

- [[coding-learn-go-with-tests-excerpt]]
