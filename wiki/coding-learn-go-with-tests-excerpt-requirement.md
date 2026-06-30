---
page_id: coding-learn-go-with-tests-excerpt-requirement
page_kind: concept
summary: Requirement: 4 statement(s) and 0 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
page_family: topic-concept
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-30
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-requirement@e1da23870120240f56ba55a03c851148
---

# Requirement

What [[coding-learn-go-with-tests-excerpt]] covers about requirement:

## Statements

### Constants / Hello, world... again

- The next requirement is when our function is called with an empty string it defaults to printing "Hello, World", rather than "Hello, ". _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00072))_

### Arrays and their type

- The next requirement will be to sum collections of varying sizes. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00306))_

### Arrays and their type / Refactor

- Our next requirement is to change SumAll to SumAllTails , where it will calculate the totals of the "tails" of each slice. The tail of a collection is all items in the collection except the first one (the "head"). _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00365))_

### Structs, methods & interfaces / Refactor

- Our next requirement is to write an Area function for circles. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00435))_


## Related pages

- [[coding-learn-go-with-tests-excerpt-section-discipline-keep-going-more-requirements-45919b2d]] - source section: Discipline / Keep going! More requirements shares source evidence from Discipline / Keep going! More requirements: Goodness me, we have more requirements. We now need to support a second parameter, specifying the language of the greeting. If a language is passed in that we do not ... [truncated]; Discipline / Keep going! More requirements shares technical record from Discipline / Keep going! More requirements: t.Run("in Spanish", func(t *testing.T) { got := Hello("Elodie", "Spanish") want := "Hola, Elodie" assertCorrectMessage(t, got, want) }) (9 shared statement(s), 9 shared atom(s))

## Source

- [[coding-learn-go-with-tests-excerpt]]
