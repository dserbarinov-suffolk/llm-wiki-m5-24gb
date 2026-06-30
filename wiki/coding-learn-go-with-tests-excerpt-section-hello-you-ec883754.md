---
page_id: coding-learn-go-with-tests-excerpt-section-hello-you-ec883754
page_kind: source
summary: Hello, YOU: 22 source-backed entries and 4 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
page_family: section-reference
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-30
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-hello-you-ec883754@be894d4bab3b8ff9ce89f50480425773
---

# Hello, YOU

From [[coding-learn-go-with-tests-excerpt]].

## Related pages

- [[coding-learn-go-with-tests-excerpt-section-go-s-documentation-38415959]] - previous source section: Go's documentation
- [[coding-learn-go-with-tests-excerpt-section-a-note-on-source-control-a3be3365]] - next source section: A note on source control

## Statements

- Now that we have a test, we can iterate on our software safely. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00043))_
- In the last example, we wrote the test after the code had been written so that you could get an example of how to write a test and declare a function. From this point on, we will be writing tests first . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00044))_
- Let's start by capturing these requirements in a test. This is basic testdriven development and allows us to make sure our test is actually testing what we want. When you retrospectively write tests, there is the risk that your test may continue to pass even if the code doesn't work as intended. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00046))_
- When using a statically typed language like Go it is important to listen to the compiler . The compiler understands how your code should snap together and work so you don't have to. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00051))_
- In this case the compiler is telling you what you need to do to continue. We have to change our function Hello to accept an argument. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00052))_
- If you try and run your tests again your hello.go will fail to compile because you're not passing an argument. Send in "world" to make it compile. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00055))_
- We finally have a compiling program but it is not meeting our requirements according to the test. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00059))_
- When you run the tests, they should now pass. Normally, as part of the TDD cycle, we should now refactor . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00062))_
- In the last example, we wrote the test after the code had been written so that you could get an example of how to write a test and declare a function. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00044))_
- If you try and run your tests again your hello.go will fail to compile because you're not passing an argument. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00055))_

## Technical atoms

### Technical frame 1: Hello, YOU

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00055))_

> If you try and run your tests again your hello.go will fail to compile because you're not passing an argument. Send in "world" to make it compile.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00054))_

```
func Hello(name string) string {
    return "Hello, world"
}
```

### Technical frame 2: Hello, YOU

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00059))_

> We finally have a compiling program but it is not meeting our requirements according to the test.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00056))_

```
func main() {
    fmt.Println(Hello("world"))
}
```

### Technical frame 3: Hello, YOU

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00059))_

> We finally have a compiling program but it is not meeting our requirements according to the test.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00057))_

> Now when you run your tests, you should see something like

### Technical frame 4: Hello, YOU

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00059))_

> We finally have a compiling program but it is not meeting our requirements according to the test.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00058))_

```
hello_test.go:10: got 'Hello, world' want 'Hello, Chris''
```
