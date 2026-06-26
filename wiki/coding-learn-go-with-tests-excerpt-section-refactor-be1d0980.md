---
page_id: coding-learn-go-with-tests-excerpt-section-refactor-be1d0980
page_kind: source
summary: Refactor: 3 source-backed entries and 2 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-refactor-be1d0980@88260b354715806b638589667b58682d
---

# Refactor

From [[coding-learn-go-with-tests-excerpt]].

## Statements

- By creating a new helper we were able to simplify our test, and start using our ErrNotFound variable so our test doesn't fail if we change the error text in the future. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00594))_

## Technical atoms

```
We	can	get	rid	of	the	magic	error	in	our Search function	by	extracting it	into	a	variable.	This	will	also	allow	us	to	have	a	better	test. var ErrNotFound	=	errors.New("could	not	find	the	word	you	were looking	for") func (d	Dictionary)	Search(word	string)	(string,	error)	{ definition,	ok	:=	d[word] if !ok	{ return "",	ErrNotFound } return definition,	nil } t.Run("unknown	word", func (t	*testing.T)	{ _,	got	:=	dictionary.Search("unknown") if got	==	nil	{ t.Fatal("expected	to	get	an	error.") } assertError(t,	got,	ErrNotFound)
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00592))_

```
}) func assertError(t	testing.TB,	got,	want	error)	{ t.Helper() if got	!=	want	{ t.Errorf("got	error	%q	want	%q",	got,	want) } }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00593))_
