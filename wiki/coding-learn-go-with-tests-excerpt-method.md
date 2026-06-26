---
page_id: coding-learn-go-with-tests-excerpt-method
page_kind: concept
summary: What are methods?: 18 statement(s) and 4 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-method@cd120c53c7f4c81a40df88eac9305d98
---

# What are methods?

What [[coding-learn-go-with-tests-excerpt]] covers about what are methods?:

## Statements

- We can define methods on our newly defined types instead. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00446))_
- With the custom type defined, we can create the Search method. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00574))_
- Now we can proceed with writing the actual method to be tested. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00290))_
- Note : We have to call the String method to retrieve the final result. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00259))_
- t.Helper() is needed to tell the test suite that this method is a helper. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00088))_
- So far we have only been writing functions but we have been using some methods. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00448))_
- Circle has a method called Area that returns a float64 so it satisfies the Shape interface _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00487))_
- When we call t.Errorf we are calling the method Errorf on the instance of our t ( testing.T ). _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00448))_
- Rectangle has a method called Area that returns a float64 so it satisfies the Shape interface _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00486))_
- Adding methods so you can add functionality to your data types and so you can implement interfaces _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00540))_
- The syntax for declaring methods is almost the same as functions and that's because they're so similar. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00458))_
- The only difference is the syntax of the method receiver func (receiverName ReceiverType) MethodName(args) . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00458))_
- All we want to do is take a collection of shapes , call the Area() method on them and then check the result. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00471))_
- Where you can just call functions wherever you like, such as Area(rectangle) you can only call methods on "things". _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00450))_

## Technical atoms

```
If	we	try	to	run	the	tests,	we	get ./shapes_test.go:19:19:	rectangle.Area	undefined	(type	Rectangle	has no	field	or	method	Area) ./shapes_test.go:29:16:	circle.Area	undefined	(type	Circle	has	no field	or	method	Area) type	Circle	has	no	field	or	method	Area func TestArea(t	*testing.T)	{ t.Run("rectangles", func (t	*testing.T)	{ rectangle	:=	Rectangle{12,	6} got	:=	rectangle.Area() want	:=	72.0 if got	!=	want	{ t.Errorf("got	%g	want	%g",	got,	want) } }) t.Run("circles", func (t	*testing.T)	{ circle	:=	Circle{10} got	:=	circle.Area() want	:=	314.1592653589793 if got	!=	want	{ t.Errorf("got	%g	want	%g",	got,	want) } }) }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00452))_

```
./shapes_test.go:25:4:	undefined:	Triangle We	have	not	defined Triangle yet Try	again ./shapes_test.go:25:8:	cannot	use	Triangle	literal	(type	Triangle) as	type	Shape	in	field	value: Triangle	does	not	implement	Shape	(missing	Area	method) It's	telling	us	we	cannot	use	a Triangle as	a	shape	because	it	does	not have	an Area() method,	so	add	an	empty	implementation	to	get	the test	working Finally	the	code	compiles	and	we	get	our	error shapes_test.go:31:	got	0.00	want	36.00 type Triangle struct { Base			float64 Height	float64 } func (t	Triangle)	Area()	float64	{ return 0 }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00510))_

```
./dictionary_test.go:53:2:	dictionary.Update	undefined	(type Dictionary	has	no	field	or	method	Update)
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00644))_

```
By	running go	test we	get: ./dictionary_test.go:74:6:	dictionary.Delete	undefined	(type Dictionary	has	no	field	or	method	Delete)
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00679))_


## Source

- [[coding-learn-go-with-tests-excerpt]]
