---
page_id: coding-learn-go-with-tests-excerpt-section-iteration-write-the-test-first-ac988ca6
page_kind: source
summary: Iteration / Write the test first: 1 source-backed entries and 1 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-29
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-iteration-write-the-test-first-ac988ca6@5528fa0cffca0c1270dd01c2f3bc7ce0
---

# Iteration / Write the test first

From [[coding-learn-go-with-tests-excerpt]].

## Related pages

- [[coding-learn-go-with-tests-excerpt-section-iteration-9b1d79ea]] - broader source section: Iteration
- [[coding-learn-go-with-tests-excerpt-section-iteration-try-and-run-the-test-edfc802d]] - next source section: Iteration / Try and run the test

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
