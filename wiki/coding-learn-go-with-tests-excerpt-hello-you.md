---
page_id: coding-learn-go-with-tests-excerpt-hello-you
page_kind: concept
summary: Hello, YOU: 11 statement(s) and 9 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-hello-you@19d667394250b49eb0d229481ace565e
---

# Hello, YOU

What [[coding-learn-go-with-tests-excerpt]] covers about hello, you:

## Statements

- The compiler understands how your code should snap together and work so you don't have to. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00051))_
- If you try and run your tests again your hello.go will fail to compile because you're not passing an argument. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00055))_
- In the last example, we wrote the test after the code had been written so that you could get an example of how to write a test and declare a function. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00044))_
- We have to change our function Hello to accept an argument. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00052))_
- In this case the compiler is telling you what you need to do to continue. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00052))_
- Now that we have a test, we can iterate on our software safely. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00043))_
- This is basic testdriven development and allows us to make sure our test is actually testing what we want. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00046))_
- When using a statically typed language like Go it is important to listen to the compiler . _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00051))_
- Send in "world" to make it compile. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00055))_
- We finally have a compiling program but it is not meeting our requirements according to the test. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00059))_
- Normally, as part of the TDD cycle, we should now refactor . _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00062))_

## Technical atoms

> Context: Our next requirement is to let us specify the recipient of the greeting.
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00045))_

> When you retrospectively write tests, there is the risk that your test may continue to pass even if the code doesn't work as intended.
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00046))_

> Context: Our next requirement is to let us specify the recipient of the greeting.
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00045))_

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
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00048))_

```
./hello_test.go:6:18: too many arguments in call to Hello
have (string)
   want ()
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00050))_

> Context: When using a statically typed language like Go it is important to listen to the compiler . The compiler understands how your code should snap together and work so you don't have to. If you try and run your tests again your hello.go will fail to compile because you're not passing an argument. Send in "world" to make it compile.
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00051, source-range-f4b7154d-00055))_

```
func Hello(name string) string {
    return "Hello, world"
}
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00054))_

> Context: If you try and run your tests again your hello.go will fail to compile because you're not passing an argument. Send in "world" to make it compile.
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00055))_

```
func main() {
    fmt.Println(Hello("world"))
}
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00056))_

> Context: If you try and run your tests again your hello.go will fail to compile because you're not passing an argument. Send in "world" to make it compile.
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00055))_

> Now when you run your tests, you should see something like
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00057))_


## Source

- [[coding-learn-go-with-tests-excerpt]]
