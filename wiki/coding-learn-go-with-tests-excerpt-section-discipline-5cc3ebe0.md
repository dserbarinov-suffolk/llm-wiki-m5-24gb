---
page_id: coding-learn-go-with-tests-excerpt-section-discipline-5cc3ebe0
page_kind: source
summary: Discipline: 27 source-backed entries and 11 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-29
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-discipline-5cc3ebe0@0c06fe747543a6aad7ee5735b7d6aaf9
---

# Discipline

From [[coding-learn-go-with-tests-excerpt]].

## Related pages

- [[coding-learn-go-with-tests-excerpt-section-discipline-keep-going-more-requirements-45919b2d]] - narrower source section: Discipline / Keep going! More requirements
- [[coding-learn-go-with-tests-excerpt-section-back-to-source-control-86d1680c]] - previous source section: Back to source control
- [[coding-learn-go-with-tests-excerpt-section-french-bcb73222]] - next source section: French
- [[coding-learn-go-with-tests-excerpt-discipline]] - topic hub: opens the topic page for Discipline

## Statements

- On the face of it this may seem tedious but sticking to the feedback loop is important. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00099))_
- Not only does it ensure that you have relevant tests , it helps ensure you design good software by refactoring with the safety of tests. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00100))_
- Seeing the test fail is an important check because it also lets you see what the error message looks like. As a developer it can be very hard to work with a codebase when failing tests do not give a clear idea as to what the problem is. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00101))_
- By not writing tests, you are committing to manually checking your code by running your software, which breaks your state of flow. You won't be saving yourself any time, especially in the long run. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00103))_
- Not only does it ensure that you have relevant tests , it helps ensure you design good software by refactoring with the safety of tests. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00100))_
- Seeing the test fail is an important check because it also lets you see what the error message looks like. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00101))_

## Statements by subsection

### Discipline / Keep going! More requirements

- Goodness me, we have more requirements. We now need to support a second parameter, specifying the language of the greeting. If a language is passed in that we do not recognise, just default to English. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00105))_
- We should be confident that we can easily use TDD to flesh out this functionality! _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00106))_
- When you try and run the test again it will complain about not passing through enough arguments to Hello in your other tests and in hello.go _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00113))_
- The tests should now pass. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00119))_
- Now it is time to refactor . You should see some problems in the code, "magic" strings, some of which are repeated. Try and refactor it yourself, with every change make sure you re-run the tests to make sure your refactoring isn't breaking anything. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00120))_

## Technical atoms

### Technical frame 1: Discipline

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00103))_

> By not writing tests, you are committing to manually checking your code by running your software, which breaks your state of flow. You won't be saving yourself any time, especially in the long run.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00101))_

> As a developer it can be very hard to work with a codebase when failing tests do not give a clear idea as to what the problem is.

### Technical frame 2: Discipline

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00103))_

> By not writing tests, you are committing to manually checking your code by running your software, which breaks your state of flow. You won't be saving yourself any time, especially in the long run.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00102))_

> By ensuring your tests are fast and setting up your tools so that running tests is simple you can get in to a state of flow when writing your code.

### Technical frame 3: Discipline / Keep going! More requirements

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

### Technical frame 4: Discipline / Keep going! More requirements

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00113))_

> When you try and run the test again it will complain about not passing through enough arguments to Hello in your other tests and in hello.go

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00109))_

> When you try to run the test, the compiler should complain because you are calling Hello with two arguments rather than one.

### Technical frame 5: Discipline / Keep going! More requirements

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00113))_

> When you try and run the test again it will complain about not passing through enough arguments to Hello in your other tests and in hello.go

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00110))_

```
./hello_test.go:27:19: too many arguments in call to Hello
have (string, string)
   want (string)
```

### Technical frame 6: Discipline / Keep going! More requirements

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

### Technical frame 7: Discipline / Keep going! More requirements

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00119))_

> The tests should now pass.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00114))_

```
./hello.go:15:19: not enough arguments in call to Hello
have (string)
   want (string, string)
```

### Technical frame 8: Discipline / Keep going! More requirements

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00119))_

> The tests should now pass.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00115))_

> Now all your tests should compile and pass, apart from our new scenario

### Technical frame 9: Discipline / Keep going! More requirements

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00119))_

> The tests should now pass.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00116))_

```
hello_test.go:29: got 'Hello, Elodie' want 'Hola, Elodie'
```

### Technical frame 10: Discipline / Keep going! More requirements

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

### Technical frame 11: Discipline / Keep going! More requirements

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
