---
page_id: coding-learn-go-with-tests-excerpt-word
page_kind: concept
summary: Word: 16 statement(s) and 33 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-word@24eda9c57c661f3d3f2acfd7f011bc12
---

# Word

What [[coding-learn-go-with-tests-excerpt]] covers about word:

## Statements

- It should only add new words to our dictionary. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00620))_
- However, we have no way to add new words to our dictionary. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00596))_
- The function can report that the word is not in the dictionary. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00577))_
- If we pass in a new word, Update will add it to the dictionary. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00653))_
- We added yet another error type for when the word does not exist. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00657))_
- After we add this, the test tells us we are not deleting the word. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00682))_
- You can think of the key as the word and the value as the definition. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00548))_
- Our test creates a Dictionary with a word and then checks if the word has been removed. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00677))_
- With that in place, we are able to see that we need to change the definition of the word. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00648))_
- dictionary_test.go:78: got error '%!q(<nil>)' want 'could not find the word you were looking for' _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00683))_
- We made variables for word and definition, and moved the definition assertion into its own helper function. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00618))_
- We are again using a switch statement to match on the error when we attempt to delete a word that doesn't exist. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00696))_
- There isn't much to refactor, but we can implement the same logic from Update to handle cases where word doesn't exist. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00689))_
- This property allows us to differentiate between a word that doesn't exist and a word that just doesn't have a definition. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00590))_

## Technical atoms

```
In dictionary.go Your	test	should	now	fail	with	a clear	error	message dictionary_test.go:12:	got	''	want	'this	is	just	a	test'	given, 'test' . package main func Search(dictionary map [string]string,	word	string)	string	{ return "" }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00559))_

```
func Search(dictionary map [string]string,	word	string)	string	{ return dictionary[word] }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00561))_

```
type Dictionary map [string]string func (d	Dictionary)	Search(word	string)	string	{ return d[word] }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00573))_

```
func TestSearch(t	*testing.T)	{ dictionary	:=	Dictionary{"test":	"this	is	just	a	test"} t.Run("known	word", func (t	*testing.T)	{ got,	_	:=	dictionary.Search("test") want	:=	"this	is	just	a	test" assertStrings(t,	got,	want) }) t.Run("unknown	word", func (t	*testing.T)	{ _,	err	:=	dictionary.Search("unknown") want	:=	"could	not	find	the	word	you	were	looking	for" if err	==	nil	{ t.Fatal("expected	to	get	an	error.") } assertStrings(t,	err.Error(),	want) }) }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00578))_

```
func (d	Dictionary)	Search(word	string)	(string,	error)	{ return d[word],	nil }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00584))_

```
func (d	Dictionary)	Search(word	string)	(string,	error)	{ definition,	ok	:=	d[word] if !ok	{ return "",	errors.New("could	not	find	the	word	you	were looking	for") } return definition,	nil }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00588))_


## Source

- [[coding-learn-go-with-tests-excerpt]]
