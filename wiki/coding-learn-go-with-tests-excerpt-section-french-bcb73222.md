---
page_id: coding-learn-go-with-tests-excerpt-section-french-bcb73222
page_kind: source
summary: French: 6 source-backed entries and 3 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-29
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-french-bcb73222@2994c77a2d7834cc57db0faf5c4e00d0
---

# French

From [[coding-learn-go-with-tests-excerpt]].

## Related pages

- [[coding-learn-go-with-tests-excerpt-section-french-switch-356fb07d]] - narrower source section: French / switch
- [[coding-learn-go-with-tests-excerpt-section-discipline-5cc3ebe0]] - previous source section: Discipline
- [[coding-learn-go-with-tests-excerpt-section-one-last-refactor-09b754e6]] - next source section: one...last...refactor?
- [[coding-learn-go-with-tests-excerpt-french]] - topic hub: opens the topic page for French

## Statements by subsection

### French / switch

- When you have lots of if statements checking a particular value it is common to use a switch statement instead. We can use switch to refactor the code to make it easier to read and more extensible if we wish to add more language support later _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00131))_
- Write a test to now include a greeting in the language of your choice and you should see how simple it is to extend our amazing function. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00133))_

## Technical atoms

### Technical frame 1: French

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00128))_

```
func Hello(name string, language string) string {
```

### Technical frame 2: French

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00129))_

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

### Technical frame 3: French / switch

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
