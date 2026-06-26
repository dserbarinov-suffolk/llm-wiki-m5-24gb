---
page_id: coding-learn-go-with-tests-excerpt-section-keep-going-more-requirements-ecf6ea01
page_kind: source
summary: Keep going! More requirements: 18 source-backed entries and 9 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-keep-going-more-requirements-ecf6ea01@8d9f9378ddd69a53f610e3036ebf0d13
---

# Keep going! More requirements

From [[coding-learn-go-with-tests-excerpt]].

## Statements

- If a language is passed in that we do not recognise, just default to English. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00105))_
- We now need to support a second parameter, specifying the language of the greeting. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00105))_
- Goodness me, we have more requirements. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00105))_
- We should be confident that we can easily use TDD to flesh out this functionality! _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00106))_
- When you try and run the test again it will complain about not passing through enough arguments to Hello in your other tests and in hello.go _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00113))_
- The tests should now pass. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00119))_
- You should see some problems in the code, "magic" strings, some of which are repeated. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00120))_
- Now it is time to refactor . _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00120))_
- Try and refactor it yourself, with every change make sure you re-run the tests to make sure your refactoring isn't breaking anything. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00120))_

## Technical atoms

```
t.Run("in Spanish", func(t *testing.T) {
        got := Hello("Elodie", "Spanish")
        want := "Hola, Elodie"
        assertCorrectMessage(t, got, want)
    })
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00108))_

> When you try to run the test, the compiler should complain because you are calling Hello with two arguments rather than one.
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00109))_

```
./hello_test.go:27:19: too many arguments in call to Hello
have (string, string)
   want (string)
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00110))_

```
func Hello(name string, language string) string {
    if name == "" {
        name = "World"
    }
    return englishHelloPrefix + name
}
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00112))_

```
./hello.go:15:19: not enough arguments in call to Hello
have (string)
   want (string, string)
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00114))_

> Now all your tests should compile and pass, apart from our new scenario
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00115))_

```
hello_test.go:29: got 'Hello, Elodie' want 'Hola, Elodie'
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00116))_

```
func Hello(name string, language string) string {
    if name == "" {
        name = "World"
    }
if language == "Spanish" {
        return "Hola, " + name
    }
    return englishHelloPrefix + name
}
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00118))_

```
const spanish = "Spanish"
    const englishHelloPrefix = "Hello, "
    const spanishHelloPrefix = "Hola, "
func Hello(name string, language string) string {
        if name == "" {
            name = "World"
        }
if language == spanish {
            return spanishHelloPrefix + name
        }
        return englishHelloPrefix + name
    }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00121))_
