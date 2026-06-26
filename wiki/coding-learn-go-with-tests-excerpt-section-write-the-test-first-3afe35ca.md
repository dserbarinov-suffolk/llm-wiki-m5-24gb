---
page_id: coding-learn-go-with-tests-excerpt-section-write-the-test-first-3afe35ca
page_kind: source
summary: Write the test first: 1 source-backed entries and 1 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-write-the-test-first-3afe35ca@89c822db99270405c53a844efc64c09b
---

# Write the test first

From [[coding-learn-go-with-tests-excerpt]].

## Technical atoms

```
func TestSumAll(t *testing.T) {
got := SumAll([]int{1, 2}, []int{0, 9})
    want := []int{3, 9}
if got != want {
        t.Errorf("got %v want %v", got, want)
    }
}
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00338))_
