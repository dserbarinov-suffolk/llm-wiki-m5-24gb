---
page_id: coding-learn-go-with-tests-excerpt-requirement
page_kind: concept
summary: Keep going! More requirements: 9 statement(s) and 9 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-requirement@ae44492b02ae10f905f7f99d7a8b2e62
---

# Keep going! More requirements

What [[coding-learn-go-with-tests-excerpt]] covers about keep going! more requirements:

## Statements

- Goodness me, we have more requirements. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00105))_
- If a language is passed in that we do not recognise, just default to English. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00105))_
- We now need to support a second parameter, specifying the language of the greeting. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00105))_
- We should be confident that we can easily use TDD to flesh out this functionality! _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00106))_
- When you try and run the test again it will complain about not passing through enough arguments to Hello in your other tests and in hello.go _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00113))_
- The tests should now pass. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00119))_
- You should see some problems in the code, "magic" strings, some of which are repeated. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00120))_
- Now it is time to refactor . _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00120))_
- Try and refactor it yourself, with every change make sure you re-run the tests to make sure your refactoring isn't breaking anything. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00120))_

## Technical atoms

> Context: We should be confident that we can easily use TDD to flesh out this functionality! Remember not to cheat! Test first . When you try to run the test, the compiler should complain because you are calling Hello with two arguments rather than one.
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00106, source-range-f4b7154d-00109))_

```
t.Run("in Spanish", func(t *testing.T) {
        got := Hello("Elodie", "Spanish")
        want := "Hola, Elodie"
        assertCorrectMessage(t, got, want)
    })
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00108))_

> Context: We should be confident that we can easily use TDD to flesh out this functionality!
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00106))_

> When you try to run the test, the compiler should complain because you are calling Hello with two arguments rather than one.
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00109))_

> Context: Remember not to cheat! Test first . When you try to run the test, the compiler should complain because you are calling Hello with two arguments rather than one.
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00109))_

```
./hello_test.go:27:19: too many arguments in call to Hello
have (string, string)
   want (string)
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00110))_

> Context: Remember not to cheat! Test first . When you try to run the test, the compiler should complain because you are calling Hello with two arguments rather than one.
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00109))_

```
func Hello(name string, language string) string {
    if name == "" {
        name = "World"
    }
    return englishHelloPrefix + name
}
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00112))_

> Context: When you try and run the test again it will complain about not passing through enough arguments to Hello in your other tests and in hello.go
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00113))_

```
./hello.go:15:19: not enough arguments in call to Hello
have (string)
   want (string, string)
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00114))_

> Context: When you try and run the test again it will complain about not passing through enough arguments to Hello in your other tests and in hello.go
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00113))_

> Now all your tests should compile and pass, apart from our new scenario
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00115))_


## Source

- [[coding-learn-go-with-tests-excerpt]]
