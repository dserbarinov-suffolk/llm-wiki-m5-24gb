---
page_id: coding-learn-go-with-tests-excerpt-section-write-the-test-first-eb39ecc1
page_kind: source
summary: Write the test first: 9 source-backed entries and 1 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-write-the-test-first-eb39ecc1@a222ee7023c278ee549aba7365d94ed8
---

# Write the test first

From [[coding-learn-go-with-tests-excerpt]].

## Statements

- This way, the user isn't left wondering if the word doesn't exist or if there is just no definition (this might not seem very useful for a dictionary. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00577))_
- This is good because the program can continue to run, but there is a better approach. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00577))_
- However, it's a scenario that could be key in other usecases). _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00577))_
- The function can report that the word is not in the dictionary. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00577))_
- This is good because the program can continue to run, but there is a better approach. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00577))_
- The way to handle this scenario in Go is to return a second argument which is an Error type. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00579))_
- Notice that as we've seen in the pointers and error section here in order to assert the error message we first check that the error is not nil and then use .Error() method to get the string which we can then pass to the assertion. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00580))_
- Notice that as we've seen in the pointers and error section here in order to assert the error message we first check that the error is not nil and then use .Error() method to get the string which we can then pass to the assertion. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00580))_

## Technical atoms

```
func TestSearch(t	*testing.T)	{ dictionary	:=	Dictionary{"test":	"this	is	just	a	test"} t.Run("known	word", func (t	*testing.T)	{ got,	_	:=	dictionary.Search("test") want	:=	"this	is	just	a	test" assertStrings(t,	got,	want) }) t.Run("unknown	word", func (t	*testing.T)	{ _,	err	:=	dictionary.Search("unknown") want	:=	"could	not	find	the	word	you	were	looking	for" if err	==	nil	{ t.Fatal("expected	to	get	an	error.") } assertStrings(t,	err.Error(),	want) }) }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00578))_
