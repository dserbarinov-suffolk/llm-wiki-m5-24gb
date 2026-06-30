---
page_id: coding-learn-go-with-tests-excerpt-section-french-switch-356fb07d
page_kind: source
summary: French / switch: 4 source-backed entries and 1 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
page_family: section-reference
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-30
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-french-switch-356fb07d@f4725ef243d476aa446dd0b9a656c4bf
---

# French / switch

From [[coding-learn-go-with-tests-excerpt]].

## Related pages

- [[coding-learn-go-with-tests-excerpt-section-french-bcb73222]] - broader source section: French

## Statements

- When you have lots of if statements checking a particular value it is common to use a switch statement instead. We can use switch to refactor the code to make it easier to read and more extensible if we wish to add more language support later _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00131))_
- Write a test to now include a greeting in the language of your choice and you should see how simple it is to extend our amazing function. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00133))_

## Technical atoms

### Technical frame 1: French / switch

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00133))_

> Write a test to now include a greeting in the language of your choice and you should see how simple it is to extend our amazing function.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00132))_

```
func Hello(name string, language string) string {
    if name == "" {
        name = "World"
    }
prefix := englishHelloPrefix
switch language {
    case spanish:
        prefix = spanishHelloPrefix
    case french:
        prefix = frenchHelloPrefix
    }
return prefix + name
}
```
