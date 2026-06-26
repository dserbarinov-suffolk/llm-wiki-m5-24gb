---
page_id: coding-learn-go-with-tests-excerpt-section-write-the-test-first-5c035218
page_kind: source
summary: Write the test first: 5 source-backed entries and 1 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-write-the-test-first-5c035218@1a3d5a117e0197d6a76911b9d47a788b
---

# Write the test first

From [[coding-learn-go-with-tests-excerpt]].

## Statements

- You will notice that we're using %d as our format strings rather than %q . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00170))_
- That's because we want it to print an integer rather than a string. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00170))_
- Also note that we are no longer using the main package, instead we've defined a package named integers , as the name suggests this will group functions for working with integers such as Add . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00171))_
- Also note that we are no longer using the main package, instead we've defined a package named integers , as the name suggests this will group functions for working with integers such as Add . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00171))_

## Technical atoms

```
package integers import "testing" func TestAdder(t	*testing.T)	{ sum	:=	Add(2,	2) expected	:=	4 if sum	!=	expected	{ t.Errorf("expected	'%d'	but	got	'%d'",	expected,	sum) } }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00169))_
