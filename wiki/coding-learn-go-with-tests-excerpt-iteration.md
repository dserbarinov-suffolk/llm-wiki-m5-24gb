---
page_id: coding-learn-go-with-tests-excerpt-iteration
page_kind: concept
summary: Iteration: 14 statement(s) and 7 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-29
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-iteration@04df89b1c68b25c851ef9f4e735c50a4
---

# Iteration

What [[coding-learn-go-with-tests-excerpt]] covers about iteration:

## Statements

### Iteration

- To do stuff repeatedly in Go, you'll need for . In Go there are no while , do , until keywords, you can only use for . Which is a good thing! _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00218))_

### Iteration / Write the minimal amount of code for the test to run and check the failing test output

- Keep the discipline! You don't need to know anything new right now to make the test fail properly. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00226))_

- All you need to do right now is enough to make it compile so you can check your test is written well. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00227))_

- Isn't it nice to know you already know enough Go to write tests for some basic problems? This means you can now play with the production code as much as you like and know it's behaving as you'd hope. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00229))_

### Iteration / Write enough code to make it pass

- The for syntax is very unremarkable and follows most C-like languages. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00232))_

- as we've been using := so far to declare and initializing variables. However, := is simply short hand for both steps. Here we are declaring a string variable only. Hence, the explicit version. We can also use var to declare functions, as we'll see later on. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00236))_

- Run the test and it should pass. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00237))_

- Additional variants of the for loop are described here. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00238))_

### Iteration / Refactor

- += called "the Add AND assignment operator" , adds the right operand to the left operand and assigns the result to left operand. It works with other types like integers. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00242))_


## Technical atoms

### Technical frame 1: Iteration / Write the test first

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00222))_

```
package iteration
import "testing"
func TestRepeat(t *testing.T) {
    repeated := Repeat("a")
    expected := "aaaaa"
if repeated != expected {
        t.Errorf("expected %q but got %q", expected, repeated)
    }
}
```

### Technical frame 2: Iteration / Try and run the test

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00224))_

```
./repeat_test.go:6:14: undefined: Repeat
```

### Technical frame 3: Iteration / Write the minimal amount of code for the test to run and check the failing test output

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00229))_

> Isn't it nice to know you already know enough Go to write tests for some basic problems? This means you can now play with the production code as much as you like and know it's behaving as you'd hope.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00228))_

```
package iteration
func Repeat(character string) string {
    return ""
}
```

### Technical frame 4: Iteration / Write the minimal amount of code for the test to run and check the failing test output

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00229))_

> Isn't it nice to know you already know enough Go to write tests for some basic problems? This means you can now play with the production code as much as you like and know it's behaving as you'd hope.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00230))_

```
repeat_test.go:10: expected 'aaaaa' but got ''
```

### Technical frame 5: Iteration / Write enough code to make it pass

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00236))_

> as we've been using := so far to declare and initializing variables. However, := is simply short hand for both steps. Here we are declaring a string variable only. Hence, the explicit version. We can also use var to declare functions, as we'll see later on.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00233))_

```
func Repeat(character string) string {
    var repeated string
    for i := 0; i < 5; i++ {
        repeated = repeated + character
    }
    return repeated
}
```

### Technical frame 6: Iteration / Write enough code to make it pass

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00236))_

> as we've been using := so far to declare and initializing variables. However, := is simply short hand for both steps. Here we are declaring a string variable only. Hence, the explicit version. We can also use var to declare functions, as we'll see later on.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00235))_

```
var repeated string
```

### Technical frame 7: Iteration / Refactor

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00242))_

> += called "the Add AND assignment operator" , adds the right operand to the left operand and assigns the result to left operand. It works with other types like integers.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00241))_

```
const repeatCount = 5
func Repeat(character string) string {
    var repeated string
    for i := 0; i < repeatCount; i++ {
        repeated += character
    }
    return repeated
}
```


## Related pages

- [[coding-learn-go-with-tests-excerpt-test]] - shared statements: Test shares source evidence from Iteration / Write enough code to make it pass: Run the test and it should pass. (1 shared statement(s))
- [[coding-learn-go-with-tests-excerpt-section-iteration-9b1d79ea]] - source section: Iteration shares source evidence from Iteration: To do stuff repeatedly in Go, you'll need for . In Go there are no while , do , until keywords, you can only use for . Which is a good thing!; Iteration shares technical record from Iteration / Write the test first: package iteration import "testing" func TestRepeat(t *testing.T) { repeated := Repeat("a") expected := "aaaaa" if repeated != expected { t.Errorf("expected %q but go ... [truncated] (14 shared statement(s), 7 shared atom(s))

## Source

- [[coding-learn-go-with-tests-excerpt]]
