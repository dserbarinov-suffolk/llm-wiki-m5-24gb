---
page_id: coding-learn-go-with-tests-excerpt-function
page_kind: concept
summary: Function: 57 statement(s) and 9 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-function@5750080b4e6b23c7b1831ec3a9b5e9f3
---

# Function

What [[coding-learn-go-with-tests-excerpt]] covers about function:

## Statements

- We need to define our function. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00646))_
- This means this function returns a string . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00021))_
- We've refactored our assertion into a new function. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00086))_
- The testing.B gives you access to the loop function. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00247))_
- Go has a built-in function delete that works on maps. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00687))_
- The func keyword defines a function with a name and a body. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00015))_
- We have to change our function Hello to accept an argument. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00052))_
- Example functions are compiled whenever tests are executed. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00199))_
- This will create a variable called prefix in your function. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00141))_
- Note that this function expects the elements to be comparable. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00348))_
- Our next requirement is to write an Area function for circles. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00435))_
- The function can report that the word is not in the dictionary. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00577))_
- You could argue that maybe our function is getting a little big. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00135))_
- We can also use var to declare functions, as we'll see later on. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00236))_

## Technical atoms

```
$	go	doc	fmt package	fmt	//	import	"fmt" Package	fmt	implements	formatted	I/O	with	functions	analogous	to	C's printf	and scanf.	The	format	'verbs'	are	derived	from	C's	but	are	simpler. #	Printing The	verbs: General: %v		the	value	in	a	default	format when	printing	structs,	the	plus	flag	(%+v)	adds	field	names %#v	a	Go-syntax	representation	of	the	value %T		a	Go-syntax	representation	of	the	type	of	the	value %%		a	literal	percent	sign;	consumes	no	value ...
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00039))_

> Write a test to now include a greeting in the language of your choice and you should see how simple it is to extend our amazing function.
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00133))_

> It should generally be used when the meaning of the result isn't clear from context, in our case it's pretty much clear that Add function will add the parameters.
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00180))_

```
Rename	the	function	to SumAllTails and	re-run	the	test sum_test.go:30:	got	[3	9]	want	[2	9]
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00371))_

> By defining this function inside the test, it cannot be used by other functions in this package.
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00391))_

```
Remember	to	run	your	tests	before	attempting	to	fix.	The	tests	should show	a	helpful	error	like ./shapes_test.go:7:18:	not	enough	arguments	in	call	to	Perimeter have	(Rectangle) want	(float64,	float64) You	can	access	the	fields	of	a	struct	with	the	syntax	of myStruct.field . Change	the	two	functions	to	fix	the	test. func TestPerimeter(t	*testing.T)	{ rectangle	:=	Rectangle{10.0,	10.0} got	:=	Perimeter(rectangle) want	:=	40.0 if got	!=	want	{ t.Errorf("got	%.2f	want	%.2f",	got,	want) } } func TestArea(t	*testing.T)	{ rectangle	:=	Rectangle{12.0,	6.0} got	:=	Area(rectangle) want	:=	72.0 if got	!=	want	{ t.Errorf("got	%.2f	want	%.2f",	got,	want) } } 2	*	(rectangle.Width	+	rectangle.Height)
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00432))_


## Source

- [[coding-learn-go-with-tests-excerpt]]
