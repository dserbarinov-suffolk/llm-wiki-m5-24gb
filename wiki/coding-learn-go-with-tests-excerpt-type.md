---
page_id: coding-learn-go-with-tests-excerpt-type
page_kind: concept
summary: Type: 38 statement(s) and 17 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-type@99c6f1ebdd40be304c8226cfb0ffc61a
---

# Type

What [[coding-learn-go-with-tests-excerpt]] covers about type:

## Statements

- The key type is special. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00553))_
- We can create a simple type using a struct . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00428))_
- We added our own error type and are returning a nil error. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00663))_
- We can define methods on our newly defined types instead. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00446))_
- The first is the key type, which is written inside the [] . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00552))_
- The value type, on the other hand, can be any type you want. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00554))_
- The second is the value type, which goes right after the [] . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00552))_
- Comparable types are explained in depth in the language spec. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00553))_
- With the custom type defined, we can create the Search method. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00574))_
- We added yet another error type for when the word does not exist. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00657))_
- We started using the Dictionary type, which we have not defined yet. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00570))_
- An interesting property of arrays is that the size is encoded in its type. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00303))_
- A handy side-effect of this is this adds a little type-safety to our code. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00392))_
- Here we created a Dictionary type which acts as a thin wrapper around map . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00574))_

## Technical atoms

```
$	go	doc	fmt package	fmt	//	import	"fmt" Package	fmt	implements	formatted	I/O	with	functions	analogous	to	C's printf	and scanf.	The	format	'verbs'	are	derived	from	C's	but	are	simpler. #	Printing The	verbs: General: %v		the	value	in	a	default	format when	printing	structs,	the	plus	flag	(%+v)	adds	field	names %#v	a	Go-syntax	representation	of	the	value %T		a	Go-syntax	representation	of	the	type	of	the	value %%		a	literal	percent	sign;	consumes	no	value ...
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00039))_

```
[N]type{value1,	value2,	...,	valueN}	e.g. numbers	:=	[5]int{1,	2, 3,	4,	5} [...]type{value1,	value2,	...,	valueN}	e.g. numbers	:=	[...]int{1,	2,
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00283))_

```
This	does	not	compile ./sum_test.go:22:13:	cannot	use	numbers	(type	[]int)	as	type	[5]int in	argument	to	Sum
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00314))_

```
$	go	test ./sum_test.go:52:21:	cannot	use	"dave" ( type	string ) as	type	[]int in	argument	to	checkSums
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00393))_

```
type Rectangle struct { Width		float64 Height	float64 }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00430))_

```
We	need	to	define	our Circle type. Now	try	to	run	the	tests	again ./shapes_test.go:29:14:	cannot	use	circle	(type	Circle)	as	type Rectangle	in	argument	to	Area Some	programming	languages	allow	you	to	do	something	like	this: But	you	cannot	in	Go ./shapes.go:20:32:	Area	redeclared	in	this	block type Circle struct { Radius	float64 } func Area(circle	Circle)	float64							{} func Area(rectangle	Rectangle)	float64	{}
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00443))_


## Source

- [[coding-learn-go-with-tests-excerpt]]
