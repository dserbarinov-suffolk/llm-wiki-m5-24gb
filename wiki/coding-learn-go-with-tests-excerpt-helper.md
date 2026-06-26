---
page_id: coding-learn-go-with-tests-excerpt-helper
page_kind: concept
summary: Helper: 9 statement(s) and 7 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-helper@b186156d7dda09ea34ad18b12e78b3d0
---

# Helper

What [[coding-learn-go-with-tests-excerpt]] covers about helper:

## Statements

- t.Helper() is needed to tell the test suite that this method is a helper. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00088))_
- I decided to create an assertStrings helper to make the implementation more general. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00565))_
- We made variables for word and definition, and moved the definition assertion into its own helper function. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00618))_
- By doing this, when it fails, the line number reported will be in our function call rather than inside our test helper. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00088))_
- Notice how our helper does not need to concern itself with whether the shape is a Rectangle or a Circle or a Triangle . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00492))_
- We are creating a helper function like we have in other exercises but this time we are asking for a Shape to be passed in. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00478))_
- By declaring an interface, the helper is decoupled from the concrete types and only has the method it needs to do its job. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00492))_
- In our case our test helper code did not need to know the exact shape it was asserting on, only how to "ask" for its area. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00543))_
- By creating a new helper we were able to simplify our test, and start using our ErrNotFound variable so our test doesn't fail if we change the error text in the future. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00594))_

## Technical atoms

```
func TestHello(t	*testing.T)	{ t.Run("saying	hello	to	people", func (t	*testing.T)	{ got	:=	Hello("Chris") want	:=	"Hello,	Chris" assertCorrectMessage(t,	got,	want) }) t.Run("empty	string	defaults	to	'world'", func (t	*testing.T)	{ got	:=	Hello("") want	:=	"Hello,	World" assertCorrectMessage(t,	got,	want) }) } func assertCorrectMessage(t	testing.TB,	got,	want	string)	{ t.Helper() if got	!=	want	{ t.Errorf("got	%q	want	%q",	got,	want) } }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00084))_

> You can comment out the t.Helper() code by adding two forward slashes // at the beginning of the line.
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00088))_

```
func TestSumAllTails(t	*testing.T)	{ checkSums	:= func (t	testing.TB,	got,	want	[]int)	{ t.Helper() if !reflect.DeepEqual(got,	want)	{ t.Errorf("got	%v	want	%v",	got,	want) } } t.Run("make	the	sums	of	tails	of", func (t	*testing.T)	{ got	:=	SumAllTails([]int{1,	2},	[]int{0,	9}) want	:=	[]int{2,	9} checkSums(t,	got,	want) }) t.Run("safely	sum	empty	slices", func (t	*testing.T)	{ got	:=	SumAllTails([]int{},	[]int{3,	4,	5}) want	:=	[]int{0,	9} checkSums(t,	got,	want) }) }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00388))_

```
checkArea	:= func (t	testing.TB,	shape	Shape,	want	float64)	{ t.Helper() got	:=	shape.Area() if got	!=	want	{ t.Errorf("got	%g	want	%g",	got,	want) } } t.Run("rectangles", func (t	*testing.T)	{ rectangle	:=	Rectangle{12,	6} checkArea(t,	rectangle,	72.0) }) t.Run("circles", func (t	*testing.T)	{ circle	:=	Circle{10} checkArea(t,	circle,	314.1592653589793) }) }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00477))_

```
func TestSearch(t	*testing.T)	{ dictionary	:= map [string]string{"test":	"this	is	just	a	test"} got	:=	Search(dictionary,	"test") want	:=	"this	is	just	a	test" assertStrings(t,	got,	want) } func assertStrings(t	testing.TB,	got,	want	string)	{ t.Helper() if got	!=	want	{ t.Errorf("got	%q	want	%q",	got,	want) } }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00564))_

```
}) func assertError(t	testing.TB,	got,	want	error)	{ t.Helper() if got	!=	want	{ t.Errorf("got	error	%q	want	%q",	got,	want) } }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00593))_


## Source

- [[coding-learn-go-with-tests-excerpt]]
