---
page_id: coding-learn-go-with-tests-excerpt-section-iteration-write-the-minimal-amount-of-code-for-the-test-to-run-and-check-the-failing-test-output-0144fa59
page_kind: source
summary: Iteration / Write the minimal amount of code for the test to run and check the failing test output: 6 source-backed entries and 2 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-29
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-iteration-write-the-minimal-amount-of-code-for-the-test-to-run-and-check-the-failing-test-output-0144fa59@fbb48e736efd75f877de114fdc95fe97
---

# Iteration / Write the minimal amount of code for the test to run and check the failing test output

From [[coding-learn-go-with-tests-excerpt]].

## Related pages

- [[coding-learn-go-with-tests-excerpt-section-iteration-9b1d79ea]] - broader source section: Iteration
- [[coding-learn-go-with-tests-excerpt-section-iteration-try-and-run-the-test-edfc802d]] - previous source section: Iteration / Try and run the test
- [[coding-learn-go-with-tests-excerpt-section-iteration-write-enough-code-to-make-it-pass-82c13f0e]] - next source section: Iteration / Write enough code to make it pass

## Statements

- Keep the discipline! You don't need to know anything new right now to make the test fail properly. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00226))_
- All you need to do right now is enough to make it compile so you can check your test is written well. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00227))_
- Isn't it nice to know you already know enough Go to write tests for some basic problems? This means you can now play with the production code as much as you like and know it's behaving as you'd hope. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00229))_
- This means you can now play with the production code as much as you like and know it's behaving as you'd hope. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00229))_

## Technical atoms

### Technical frame 1: Iteration / Write the minimal amount of code for the test to run and check the failing test output

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00229))_

> Isn't it nice to know you already know enough Go to write tests for some basic problems? This means you can now play with the production code as much as you like and know it's behaving as you'd hope.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00228))_

```
package iteration
func Repeat(character string) string {
    return ""
}
```

### Technical frame 2: Iteration / Write the minimal amount of code for the test to run and check the failing test output

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00229))_

> Isn't it nice to know you already know enough Go to write tests for some basic problems? This means you can now play with the production code as much as you like and know it's behaving as you'd hope.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00230))_

```
repeat_test.go:10: expected 'aaaaa' but got ''
```
