---
page_id: coding-learn-go-with-tests-excerpt-section-integers-write-the-test-first-7d2f9399
page_kind: source
summary: Integers / Write the test first: 5 source-backed entries and 1 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-29
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-integers-write-the-test-first-7d2f9399@e8bcd78d804c63117de6b13400eb0559
---

# Integers / Write the test first

From [[coding-learn-go-with-tests-excerpt]].

## Related pages

- [[coding-learn-go-with-tests-excerpt-section-integers-771ce4c7]] - broader source section: Integers
- [[coding-learn-go-with-tests-excerpt-section-integers-try-and-run-the-test-ce54b37e]] - next source section: Integers / Try and run the test

## Statements

- You will notice that we're using %d as our format strings rather than %q . That's because we want it to print an integer rather than a string. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00170))_
- Also note that we are no longer using the main package, instead we've defined a package named integers , as the name suggests this will group functions for working with integers such as Add . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00171))_
- That's because we want it to print an integer rather than a string. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00170))_
- Also note that we are no longer using the main package, instead we've defined a package named integers , as the name suggests this will group functions for working with integers such as Add . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00171))_

## Technical atoms

### Technical frame 1: Integers / Write the test first

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00170))_

> You will notice that we're using %d as our format strings rather than %q . That's because we want it to print an integer rather than a string.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00169))_

```
package integers
import "testing"
func TestAdder(t *testing.T) {
    sum := Add(2, 2)
    expected := 4
if sum != expected {
        t.Errorf("expected '%d' but got '%d'", expected, sum)
    }
}
```
