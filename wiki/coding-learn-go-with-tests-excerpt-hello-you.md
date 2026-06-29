---
page_id: coding-learn-go-with-tests-excerpt-hello-you
page_kind: concept
summary: Hello, YOU: 11 statement(s) and 9 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-29
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-hello-you@03897ac02de3a8e37633e8c526d9db14
---

# Hello, YOU

What [[coding-learn-go-with-tests-excerpt]] covers about hello, you:

## Statements

### Hello, YOU

- Now that we have a test, we can iterate on our software safely. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00043))_

- In the last example, we wrote the test after the code had been written so that you could get an example of how to write a test and declare a function. From this point on, we will be writing tests first . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00044))_

- Let's start by capturing these requirements in a test. This is basic testdriven development and allows us to make sure our test is actually testing what we want. When you retrospectively write tests, there is the risk that your test may continue to pass even if the code doesn't work as intended. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00046))_

- When using a statically typed language like Go it is important to listen to the compiler . The compiler understands how your code should snap together and work so you don't have to. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00051))_

- In this case the compiler is telling you what you need to do to continue. We have to change our function Hello to accept an argument. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00052))_

- If you try and run your tests again your hello.go will fail to compile because you're not passing an argument. Send in "world" to make it compile. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00055))_

- We finally have a compiling program but it is not meeting our requirements according to the test. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00059))_

- When you run the tests, they should now pass. Normally, as part of the TDD cycle, we should now refactor . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00062))_


## Technical atoms

### Technical frame 1: Hello, YOU

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00051))_

> When using a statically typed language like Go it is important to listen to the compiler . The compiler understands how your code should snap together and work so you don't have to.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00046))_

> When you retrospectively write tests, there is the risk that your test may continue to pass even if the code doesn't work as intended.

### Technical frame 2: Hello, YOU

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00051))_

> When using a statically typed language like Go it is important to listen to the compiler . The compiler understands how your code should snap together and work so you don't have to.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00048))_

```
import "testing"
func TestHello(t *testing.T) {
    got := Hello("Chris")
    want := "Hello, Chris"
if got != want {
        t.Errorf("got %q want %q", got, want)
    }
}
```

### Technical frame 3: Hello, YOU

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00051))_

> When using a statically typed language like Go it is important to listen to the compiler . The compiler understands how your code should snap together and work so you don't have to.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00050))_

```
./hello_test.go:6:18: too many arguments in call to Hello
have (string)
   want ()
```

### Technical frame 4: Hello, YOU

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00055))_

> If you try and run your tests again your hello.go will fail to compile because you're not passing an argument. Send in "world" to make it compile.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00054))_

```
func Hello(name string) string {
    return "Hello, world"
}
```

### Technical frame 5: Hello, YOU

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00059))_

> We finally have a compiling program but it is not meeting our requirements according to the test.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00056))_

```
func main() {
    fmt.Println(Hello("world"))
}
```

### Technical frame 6: Hello, YOU

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00059))_

> We finally have a compiling program but it is not meeting our requirements according to the test.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00057))_

> Now when you run your tests, you should see something like

### Technical frame 7: Hello, YOU

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00059))_

> We finally have a compiling program but it is not meeting our requirements according to the test.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00058))_

```
hello_test.go:10: got 'Hello, world' want 'Hello, Chris''
```

### Technical frame 8: Hello, YOU

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00062))_

> When you run the tests, they should now pass. Normally, as part of the TDD cycle, we should now refactor .

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00061))_

```
func Hello(name string) string {
    return "Hello, " + name
}
```

### Technical frame 9: Hello, YOU

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00059))_

> We finally have a compiling program but it is not meeting our requirements according to the test.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00062))_

> When you run the tests, they should now pass.


## Related pages

- [[coding-learn-go-with-tests-excerpt-test]] - shared statements and technical atoms: Test shares source evidence from Hello, YOU: In the last example, we wrote the test after the code had been written so that you could get an example of how to write a test and declare a function. From this poin ... [truncated]; Test shares technical record from Hello, YOU: func Hello(name string) string { return "Hello, world" } (2 shared statement(s), 6 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-code]] - shared statements and technical atoms: Code shares source evidence from Hello, YOU: In the last example, we wrote the test after the code had been written so that you could get an example of how to write a test and declare a function. From this poin ... [truncated]; Code shares technical record from Hello, YOU: func Hello(name string) string { return "Hello, world" } (2 shared statement(s), 1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-section-hello-you-ec883754]] - source section: Hello, YOU shares source evidence from Hello, YOU: Now that we have a test, we can iterate on our software safely.; Hello, YOU shares technical record from Hello, YOU: When you retrospectively write tests, there is the risk that your test may continue to pass even if the code doesn't work as intended. (11 shared statement(s), 9 shared atom(s))

## Source

- [[coding-learn-go-with-tests-excerpt]]
