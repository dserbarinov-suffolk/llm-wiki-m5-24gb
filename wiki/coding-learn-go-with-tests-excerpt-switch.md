---
page_id: coding-learn-go-with-tests-excerpt-switch
page_kind: concept
summary: switch: 6 statement(s) and 6 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-switch@f71b29b518df1fb0ee1e9b5cf59f2146
---

# switch

What [[coding-learn-go-with-tests-excerpt]] covers about switch:

## Statements

- Here we are using a switch statement to match on the error. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00633))_
- default in the switch case will be branched to if none of the other case statements match. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00145))_
- When you have lots of if statements checking a particular value it is common to use a switch statement instead. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00131))_
- Having a switch like this provides an extra safety net, in case Search returns an error other than ErrNotFound . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00633))_
- We are again using a switch statement to match on the error when we attempt to delete a word that doesn't exist. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00696))_
- We can use switch to refactor the code to make it easier to read and more extensible if we wish to add more language support later _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00131))_

## Technical atoms

```
func Hello(name	string,	language	string)	string	{ if name	==	""	{ name	=	"World" } prefix	:=	englishHelloPrefix switch language	{ case spanish: prefix	=	spanishHelloPrefix case french: prefix	=	frenchHelloPrefix } return prefix	+	name }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00132))_

```
} func greetingPrefix(language	string)	(prefix	string)	{ switch language	{ case french: prefix	=	frenchHelloPrefix case spanish: prefix	=	spanishHelloPrefix default : prefix	=	englishHelloPrefix } return
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00137))_

```
func (d	Dictionary)	Add(word,	definition	string)	error	{ _,	err	:=	d.Search(word) switch err	{ case ErrNotFound: d[word]	=	definition case nil: return ErrWordExists default : return err } return nil }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00632))_

```
func (d	Dictionary)	Update(word,	definition	string)	error	{ _,	err	:=	d.Search(word) switch err	{ case ErrNotFound: return ErrWordDoesNotExist case nil: d[word]	=	definition default : return err } return nil
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00667))_

> This function looks almost identical to Add except we switched when we update the dictionary and when we return an error.
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00669))_

```
func (d	Dictionary)	Delete(word	string)	error	{ _,	err	:=	d.Search(word) switch err	{ case ErrNotFound: return ErrWordDoesNotExist case nil: delete(d,	word) default : return err } return nil }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00695))_


## Source

- [[coding-learn-go-with-tests-excerpt]]
