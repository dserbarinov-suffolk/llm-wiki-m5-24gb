---
page_id: coding-learn-go-with-tests-excerpt-case
page_kind: concept
summary: But in our case: 21 statement(s) and 8 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-case@35c10aaaf515469cf4b7e97b60e61c58
---

# But in our case

What [[coding-learn-go-with-tests-excerpt]] covers about but in our case:

## Statements

- In our case, we are saying "take from 1 to the end" with numbers[1:] . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00374))_
- In this case the compiler is telling you what you need to do to continue. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00052))_
- In our case, you can see that having two tests for this function is redundant. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00328))_
- One final tip with table driven tests is to use t.Run and to name the test cases. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00530))_
- default in the switch case will be branched to if none of the other case statements match. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00145))_
- Now our tests - rather, the list of test cases - make assertions of truth about shapes and their areas. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00524))_
- In this case, we are using for to iterate 5 times to work through the array and add each item onto sum . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00297))_
- Table driven tests are useful when you want to build a list of test cases that can be tested in the same manner. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00496))_
- In addition, if a bug is found with Area it is very easy to add a new test case to exercise it before fixing it. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00500))_
- Having a switch like this provides an extra safety net, in case Search returns an error other than ErrNotFound . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00633))_
- By wrapping each case in a t.Run you will have clearer test output on failures as it will print the name of the case _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00531))_
- There isn't much to refactor, but we can implement the same logic from Update to handle cases where word doesn't exist. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00689))_
- In our case our test helper code did not need to know the exact shape it was asserting on, only how to "ask" for its area. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00543))_
- You can see how it would be very easy for a developer to introduce a new shape, implement Area and then add it to the test cases. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00500))_

## Technical atoms

> It is nice to commit at this point in case you somehow get into a mess with refactoring - you can always go back to the working version.
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00065))_

```
func Hello(name	string,	language	string)	string	{ if name	==	""	{ name	=	"World" } prefix	:=	englishHelloPrefix switch language	{ case spanish: prefix	=	spanishHelloPrefix case french: prefix	=	frenchHelloPrefix } return prefix	+	name }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00132))_

```
} func greetingPrefix(language	string)	(prefix	string)	{ switch language	{ case french: prefix	=	frenchHelloPrefix case spanish: prefix	=	spanishHelloPrefix default : prefix	=	englishHelloPrefix } return
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00137))_

> It should generally be used when the meaning of the result isn't clear from context, in our case it's pretty much clear that Add function will add the parameters.
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00180))_

```
func TestArea(t	*testing.T)	{ areaTests	:=	[] struct { name				string shape			Shape hasArea	float64 }{ {name:	"Rectangle",	shape:	Rectangle{Width:	12,	Height:	6}, hasArea:	72.0}, {name:	"Circle",	shape:	Circle{Radius:	10},	hasArea: 314.1592653589793}, {name:	"Triangle",	shape:	Triangle{Base:	12,	Height:	6}, hasArea:	36.0}, } for _,	tt	:= range areaTests	{ //	using	tt.name	from	the	case	to	use	it	as	the	`t.Run`	test name t.Run(tt.name, func (t	*testing.T)	{ got	:=	tt.shape.Area() if got	!=	tt.hasArea	{ t.Errorf("%#v	got	%g	want	%g",	tt.shape,	got, tt.hasArea) } }) } }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00535))_

```
func (d	Dictionary)	Add(word,	definition	string)	error	{ _,	err	:=	d.Search(word) switch err	{ case ErrNotFound: d[word]	=	definition case nil: return ErrWordExists default : return err } return nil }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00632))_


## Source

- [[coding-learn-go-with-tests-excerpt]]
