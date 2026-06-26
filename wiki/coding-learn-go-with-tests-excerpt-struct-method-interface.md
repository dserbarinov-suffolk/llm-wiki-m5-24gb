---
page_id: coding-learn-go-with-tests-excerpt-struct-method-interface
page_kind: concept
summary: Structs, methods & interfaces: 38 statement(s) and 15 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-struct-method-interface@5f9fe91675fb6ff64d46d2edd6ee4b33
---

# Structs, methods & interfaces

What [[coding-learn-go-with-tests-excerpt]] covers about structs, methods & interfaces:

## Statements

- In Go interface resolution is implicit . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00490))_
- We can create a simple type using a struct . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00428))_
- With Go, we can codify this intent with interfaces . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00473))_
- We can define methods on our newly defined types instead. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00446))_
- With the custom type defined, we can create the Search method. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00574))_
- Now we can proceed with writing the actual method to be tested. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00290))_
- Note : We have to call the String method to retrieve the final result. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00259))_
- A struct is just a named collection of fields where you can store data. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00428))_
- The only new syntax here is creating an "anonymous struct", areaTests . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00498))_
- t.Helper() is needed to tell the test suite that this method is a helper. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00088))_
- This is quite different to interfaces in most other programming languages. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00484))_
- Normally you have to write code to say My type Foo implements interface Bar . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00484))_
- So far we have only been writing functions but we have been using some methods. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00448))_
- If the type you pass in matches what the interface is asking for, it will compile. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00490))_

## Technical atoms

```
$	go	doc	fmt package	fmt	//	import	"fmt" Package	fmt	implements	formatted	I/O	with	functions	analogous	to	C's printf	and scanf.	The	format	'verbs'	are	derived	from	C's	but	are	simpler. #	Printing The	verbs: General: %v		the	value	in	a	default	format when	printing	structs,	the	plus	flag	(%+v)	adds	field	names %#v	a	Go-syntax	representation	of	the	value %T		a	Go-syntax	representation	of	the	type	of	the	value %%		a	literal	percent	sign;	consumes	no	value ...
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00039))_

```
type Rectangle struct { Width		float64 Height	float64 }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00430))_

```
Remember	to	run	your	tests	before	attempting	to	fix.	The	tests	should show	a	helpful	error	like ./shapes_test.go:7:18:	not	enough	arguments	in	call	to	Perimeter have	(Rectangle) want	(float64,	float64) You	can	access	the	fields	of	a	struct	with	the	syntax	of myStruct.field . Change	the	two	functions	to	fix	the	test. func TestPerimeter(t	*testing.T)	{ rectangle	:=	Rectangle{10.0,	10.0} got	:=	Perimeter(rectangle) want	:=	40.0 if got	!=	want	{ t.Errorf("got	%.2f	want	%.2f",	got,	want) } } func TestArea(t	*testing.T)	{ rectangle	:=	Rectangle{12.0,	6.0} got	:=	Area(rectangle) want	:=	72.0 if got	!=	want	{ t.Errorf("got	%.2f	want	%.2f",	got,	want) } } 2	*	(rectangle.Width	+	rectangle.Height)
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00432))_

```
We	need	to	define	our Circle type. Now	try	to	run	the	tests	again ./shapes_test.go:29:14:	cannot	use	circle	(type	Circle)	as	type Rectangle	in	argument	to	Area Some	programming	languages	allow	you	to	do	something	like	this: But	you	cannot	in	Go ./shapes.go:20:32:	Area	redeclared	in	this	block type Circle struct { Radius	float64 } func Area(circle	Circle)	float64							{} func Area(rectangle	Rectangle)	float64	{}
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00443))_

```
If	we	try	to	run	the	tests,	we	get ./shapes_test.go:19:19:	rectangle.Area	undefined	(type	Rectangle	has no	field	or	method	Area) ./shapes_test.go:29:16:	circle.Area	undefined	(type	Circle	has	no field	or	method	Area) type	Circle	has	no	field	or	method	Area func TestArea(t	*testing.T)	{ t.Run("rectangles", func (t	*testing.T)	{ rectangle	:=	Rectangle{12,	6} got	:=	rectangle.Area() want	:=	72.0 if got	!=	want	{ t.Errorf("got	%g	want	%g",	got,	want) } }) t.Run("circles", func (t	*testing.T)	{ circle	:=	Circle{10} got	:=	circle.Area() want	:=	314.1592653589793 if got	!=	want	{ t.Errorf("got	%g	want	%g",	got,	want) } }) }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00452))_

```
type Rectangle struct { Width		float64 Height	float64 } func (r	Rectangle)	Area()	float64	{ return 0 } type Circle struct { Radius	float64
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00456))_


## Source

- [[coding-learn-go-with-tests-excerpt]]
