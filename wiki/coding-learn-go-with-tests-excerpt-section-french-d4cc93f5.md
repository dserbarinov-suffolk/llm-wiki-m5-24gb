---
page_id: coding-learn-go-with-tests-excerpt-section-french-d4cc93f5
page_kind: source
summary: French: 2 source-backed entries and 2 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-french-d4cc93f5@ff667967496acfbcb126abb17844ed7c
---

# French

From [[coding-learn-go-with-tests-excerpt]].

## Technical atoms

```
func Hello(name string, language string) string {
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00128))_

```
if name == "" {
        name = "World"
    }
if language == spanish {
        return spanishHelloPrefix + name
    }
    if language == french {
        return frenchHelloPrefix + name
    }
    return englishHelloPrefix + name
}
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00129))_
