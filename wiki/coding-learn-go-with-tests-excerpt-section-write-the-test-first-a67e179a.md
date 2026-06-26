---
page_id: coding-learn-go-with-tests-excerpt-section-write-the-test-first-a67e179a
page_kind: source
summary: Write the test first: 1 source-backed entries and 1 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-write-the-test-first-a67e179a@907df2ef5f65f31d8d48da50d3db25da
---

# Write the test first

From [[coding-learn-go-with-tests-excerpt]].

## Technical atoms

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
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00222))_
