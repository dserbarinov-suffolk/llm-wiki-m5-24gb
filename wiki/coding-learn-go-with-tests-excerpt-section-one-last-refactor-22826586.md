---
page_id: coding-learn-go-with-tests-excerpt-section-one-last-refactor-22826586
page_kind: source
summary: one...last...refactor?: 5 source-backed entries and 3 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-one-last-refactor-22826586@d65b4efb507dd3e2ede37c0b33a721e3
---

# one...last...refactor?

From [[coding-learn-go-with-tests-excerpt]].

## Statements

- The simplest refactor for this would be to extract out some functionality into another function. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00135))_
- You could argue that maybe our function is getting a little big. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00135))_

## Technical atoms

```
const (
    spanish = "Spanish"
    french  = "French"
englishHelloPrefix = "Hello, "
    spanishHelloPrefix = "Hola, "
    frenchHelloPrefix  = "Bonjour, "
)
func Hello(name string, language string) string {
    if name == "" {
        name = "World"
    }
return greetingPrefix(language) + name
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00136))_

```
}
func greetingPrefix(language string) (prefix string) {
    switch language {
    case french:
        prefix = frenchHelloPrefix
    case spanish:
        prefix = spanishHelloPrefix
    default:
        prefix = englishHelloPrefix
    }
    return
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00137))_

```
}
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00138))_
