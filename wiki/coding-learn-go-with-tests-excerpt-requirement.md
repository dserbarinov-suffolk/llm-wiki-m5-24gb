---
page_id: coding-learn-go-with-tests-excerpt-requirement
page_kind: concept
summary: Keep going! More requirements: 9 statement(s) and 9 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-29
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-requirement@f9b3b951c1269ae0387457e96a8fb2db
---

# Keep going! More requirements

What [[coding-learn-go-with-tests-excerpt]] covers about keep going! more requirements:

## Statements

### Discipline / Keep going! More requirements

- Goodness me, we have more requirements. We now need to support a second parameter, specifying the language of the greeting. If a language is passed in that we do not recognise, just default to English. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00105))_

- We should be confident that we can easily use TDD to flesh out this functionality! _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00106))_

- When you try and run the test again it will complain about not passing through enough arguments to Hello in your other tests and in hello.go _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00113))_

- The tests should now pass. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00119))_

- Now it is time to refactor . You should see some problems in the code, "magic" strings, some of which are repeated. Try and refactor it yourself, with every change make sure you re-run the tests to make sure your refactoring isn't breaking anything. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00120))_


## Technical atoms

### Technical frame 1: Discipline / Keep going! More requirements

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00113))_

> When you try and run the test again it will complain about not passing through enough arguments to Hello in your other tests and in hello.go

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00108))_

```
t.Run("in Spanish", func(t *testing.T) {
        got := Hello("Elodie", "Spanish")
        want := "Hola, Elodie"
        assertCorrectMessage(t, got, want)
    })
```

### Technical frame 2: Discipline / Keep going! More requirements

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00113))_

> When you try and run the test again it will complain about not passing through enough arguments to Hello in your other tests and in hello.go

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00109))_

> When you try to run the test, the compiler should complain because you are calling Hello with two arguments rather than one.

### Technical frame 3: Discipline / Keep going! More requirements

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00113))_

> When you try and run the test again it will complain about not passing through enough arguments to Hello in your other tests and in hello.go

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00110))_

```
./hello_test.go:27:19: too many arguments in call to Hello
have (string, string)
   want (string)
```

### Technical frame 4: Discipline / Keep going! More requirements

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00113))_

> When you try and run the test again it will complain about not passing through enough arguments to Hello in your other tests and in hello.go

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00112))_

```
func Hello(name string, language string) string {
    if name == "" {
        name = "World"
    }
    return englishHelloPrefix + name
}
```

### Technical frame 5: Discipline / Keep going! More requirements

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00119))_

> The tests should now pass.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00114))_

```
./hello.go:15:19: not enough arguments in call to Hello
have (string)
   want (string, string)
```

### Technical frame 6: Discipline / Keep going! More requirements

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00119))_

> The tests should now pass.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00115))_

> Now all your tests should compile and pass, apart from our new scenario

### Technical frame 7: Discipline / Keep going! More requirements

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00119))_

> The tests should now pass.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00116))_

```
hello_test.go:29: got 'Hello, Elodie' want 'Hola, Elodie'
```

### Technical frame 8: Discipline / Keep going! More requirements

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00119))_

> The tests should now pass.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00118))_

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

### Technical frame 9: Discipline / Keep going! More requirements

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00120))_

> Now it is time to refactor . You should see some problems in the code, "magic" strings, some of which are repeated. Try and refactor it yourself, with every change make sure you re-run the tests to make sure your refactoring isn't breaking anything.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00121))_

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


## Related pages

- [[coding-learn-go-with-tests-excerpt-discipline]] - shared statements and technical atoms: Discipline shares source evidence from Discipline / Keep going! More requirements: Goodness me, we have more requirements. We now need to support a second parameter, specifying the language of the greeting. If a language is passed in that we do not ... [truncated]; Discipline shares technical record from Discipline / Keep going! More requirements: t.Run("in Spanish", func(t *testing.T) { got := Hello("Elodie", "Spanish") want := "Hola, Elodie" assertCorrectMessage(t, got, want) }) (9 shared statement(s), 9 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-test]] - shared statements and technical atoms: Test shares source evidence from Discipline / Keep going! More requirements: When you try and run the test again it will complain about not passing through enough arguments to Hello in your other tests and in hello.go; Test shares technical record from Discipline / Keep going! More requirements: t.Run("in Spanish", func(t *testing.T) { got := Hello("Elodie", "Spanish") want := "Hola, Elodie" assertCorrectMessage(t, got, want) }) (2 shared statement(s), 7 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-section-discipline-keep-going-more-requirements-45919b2d]] - source section: Discipline / Keep going! More requirements shares source evidence from Discipline / Keep going! More requirements: Goodness me, we have more requirements. We now need to support a second parameter, specifying the language of the greeting. If a language is passed in that we do not ... [truncated]; Discipline / Keep going! More requirements shares technical record from Discipline / Keep going! More requirements: t.Run("in Spanish", func(t *testing.T) { got := Hello("Elodie", "Spanish") want := "Hola, Elodie" assertCorrectMessage(t, got, want) }) (9 shared statement(s), 9 shared atom(s))

## Source

- [[coding-learn-go-with-tests-excerpt]]
