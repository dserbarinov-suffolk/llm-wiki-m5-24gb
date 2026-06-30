---
page_id: coding-learn-go-with-tests-excerpt-section-one-last-refactor-09b754e6
page_kind: source
summary: one...last...refactor?: 15 source-backed entries and 0 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
page_family: section-reference
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-30
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-one-last-refactor-09b754e6@5eab78c6b1a53be1eeb5797baeb19185
---

# one...last...refactor?

From [[coding-learn-go-with-tests-excerpt]].

## Related pages

- [[coding-learn-go-with-tests-excerpt-section-french-bcb73222]] - previous source section: French
- [[coding-learn-go-with-tests-excerpt-refactor]] - topic hub: opens the topic page for Refactor

## Statements

- You could argue that maybe our function is getting a little big. The simplest refactor for this would be to extract out some functionality into another function. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00135))_
- In our function signature we have made a named return value (prefix string) . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00140))_
- This will create a variable called prefix in your function. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00141))_
- It will be assigned the "zero" value. This depends on the type, for example int s are 0 and for string s it is "" . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00142))_
- This will display in the Go Doc for your function so it can make the intent of your code clearer. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00144))_
- default in the switch case will be branched to if none of the other case statements match. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00145))_
- The function name starts with a lowercase letter. In Go, public functions start with a capital letter, and private ones start with a lowercase letter. We don't want the internals of our algorithm exposed to the world, so we made this function private. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00146))_
- Also, we can group constants in a block instead of declaring them on their own line. For readability, it's a good idea to use a line between sets of related constants. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00147))_
- This depends on the type, for example int s are 0 and for string s it is "" . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00142))_
