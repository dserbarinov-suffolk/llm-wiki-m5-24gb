---
page_id: coding-learn-go-with-tests-excerpt-section-write-enough-code-to-make-it-pass-011dcf21
page_kind: source
summary: Write enough code to make it pass: 4 source-backed entries and 1 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-write-enough-code-to-make-it-pass-011dcf21@87ed442a2553e5e960aa12a5ee71ca27
---

# Write enough code to make it pass

From [[coding-learn-go-with-tests-excerpt]].

## Statements

- The second value is a boolean which indicates if the key was found successfully. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00589))_
- In order to make this pass, we are using an interesting property of the map lookup. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00589))_
- This property allows us to differentiate between a word that doesn't exist and a word that just doesn't have a definition. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00590))_

## Technical atoms

```
func (d	Dictionary)	Search(word	string)	(string,	error)	{ definition,	ok	:=	d[word] if !ok	{ return "",	errors.New("could	not	find	the	word	you	were looking	for") } return definition,	nil }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00588))_
