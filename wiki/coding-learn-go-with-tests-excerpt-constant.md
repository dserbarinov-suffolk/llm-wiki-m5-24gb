---
page_id: coding-learn-go-with-tests-excerpt-constant
page_kind: concept
summary: Constants: 18 statement(s) and 7 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-29
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-constant@b786daa0e5e59b685d2b328dc1d01544
---

# Constants

What [[coding-learn-go-with-tests-excerpt]] covers about constants:

## Statements

### Constants

- After refactoring, re-run your tests to make sure you haven't broken anything. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00069))_

### Constants / Hello, world... again

- The next requirement is when our function is called with an empty string it defaults to printing "Hello, World", rather than "Hello, ". _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00072))_

- Here, we are introducing another tool in our testing arsenal: subtests. Sometimes, it is useful to group tests around a "thing" and then have subtests describing different scenarios. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00075))_

- A benefit of this approach is you can set up shared code that can be used in the other tests. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00076))_

- If we run our tests we should see it satisfies the new requirement and we haven't accidentally broken the other functionality. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00080))_

- It is important that your tests are clear specifications of what the code needs to do. But there is repeated code when we check if the message is what we expect. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00081))_

- Refactoring is not just for the production code! _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00082))_

- Now that the tests are passing, we can and should refactor our tests. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00083))_

- We've refactored our assertion into a new function. This reduces duplication and improves the readability of our tests. We need to pass in t *testing.T so that we can tell the test code to fail when we need to. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00086))_

- t.Helper() is needed to tell the test suite that this method is a helper. By doing this, when it fails, the line number reported will be in our function call rather than inside our test helper. This will help other developers track down problems more easily. If you still don't understand, comment it out, make a test fail and observe the test output. Comments in Go are a great way to add additional information to your code, or in this case, a quick way to tell the compiler to ignore a line. You can comment out the t.Helper() code by adding two forward slashes // at the beginning of the line. You should see that line turn grey or change to another color than the rest of your code to indicate it's now commented out. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00088))_


## Technical atoms

### Technical frame 1: Constants

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00069))_

> After refactoring, re-run your tests to make sure you haven't broken anything.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00068))_

```
Constants are deﬁned like so
const englishHelloPrefix = "Hello, "
We can now refactor our code
const englishHelloPrefix = "Hello, "
func Hello(name string) string {
    return englishHelloPrefix + name
}
```

### Technical frame 2: Constants / Hello, world... again

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00075))_

> Here, we are introducing another tool in our testing arsenal: subtests. Sometimes, it is useful to group tests around a "thing" and then have subtests describing different scenarios.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00074))_

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

### Technical frame 3: Constants / Hello, world... again

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00080))_

> If we run our tests we should see it satisfies the new requirement and we haven't accidentally broken the other functionality.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00078))_

```
const englishHelloPrefix = "Hello, "
func Hello(name string) string {
    if name == "" {
```

### Technical frame 4: Constants / Hello, world... again

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00080))_

> If we run our tests we should see it satisfies the new requirement and we haven't accidentally broken the other functionality.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00079))_

```
name = "World"
    }
    return englishHelloPrefix + name
}
```

### Technical frame 5: Constants / Hello, world... again

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00086))_

> We've refactored our assertion into a new function. This reduces duplication and improves the readability of our tests. We need to pass in t *testing.T so that we can tell the test code to fail when we need to.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00084))_

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

### Technical frame 6: Constants / Hello, world... again

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00088))_

> t.Helper() is needed to tell the test suite that this method is a helper. By doing this, when it fails, the line number reported will be in our function call rather than inside our test helper. This will help other developers track down problems more easily. If you still don't understand, comment it out, make a test fail and observe the test output. Comments in Go are a great way to add additional information to your code, or in this case, a quick way to tell the compiler to ignore a line. You c

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00087))_

> For helper functions, it's a good idea to accept a testing.TB which is an interface that *testing.T and *testing.B both satisfy, so you can call helper functions from a test, or a benchmark (don't worry if words like "interface" mean nothing to you right now, it will be covered later).

### Technical frame 7: Constants / Hello, world... again

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00088))_

> t.Helper() is needed to tell the test suite that this method is a helper. By doing this, when it fails, the line number reported will be in our function call rather than inside our test helper. This will help other developers track down problems more easily. If you still don't understand, comment it out, make a test fail and observe the test output. Comments in Go are a great way to add additional information to your code, or in this case, a quick way to tell the compiler to ignore a line. You c

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00089))_

> When you have more than one argument of the same type (in our case two strings) rather than having (got string, want string) you can shorten it to (got, want string) .


## Related pages

- [[coding-learn-go-with-tests-excerpt-test]] - shared statements and technical atoms: Test shares source evidence from Constants: After refactoring, re-run your tests to make sure you haven't broken anything.; Test shares technical record from Constants / Hello, world... again: const englishHelloPrefix = "Hello, " func Hello(name string) string { if name == "" { (3 shared statement(s), 5 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-section-constants-374a85cb]] - source section: Constants shares source evidence from Constants: After refactoring, re-run your tests to make sure you haven't broken anything.; Constants shares technical record from Constants: Constants are deﬁned like so const englishHelloPrefix = "Hello, " We can now refactor our code const englishHelloPrefix = "Hello, " func Hello(name string) string { ... [truncated] (18 shared statement(s), 7 shared atom(s))

## Source

- [[coding-learn-go-with-tests-excerpt]]
