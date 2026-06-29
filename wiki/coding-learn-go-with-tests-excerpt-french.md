---
page_id: coding-learn-go-with-tests-excerpt-french
page_kind: concept
summary: French: 3 statement(s) and 3 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-29
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-french@40a49f6fba966671dc49b7873fa3806a
---

# French

What [[coding-learn-go-with-tests-excerpt]] covers about french:

## Statements

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


## Related pages

- [[coding-learn-go-with-tests-excerpt-test]] - shared statements: Test shares source evidence from French / switch: Write a test to now include a greeting in the language of your choice and you should see how simple it is to extend our amazing function. (1 shared statement(s))
- [[coding-learn-go-with-tests-excerpt-section-french-bcb73222]] - source section: French shares source evidence from French / switch: When you have lots of if statements checking a particular value it is common to use a switch statement instead. We can use switch to refactor the code to make it eas ... [truncated]; French shares technical record from French: func Hello(name string, language string) string { (3 shared statement(s), 3 shared atom(s))

## Source

- [[coding-learn-go-with-tests-excerpt]]
