---
page_id: coding-learn-go-with-tests-excerpt-value
page_kind: concept
summary: Value: 27 statement(s) and 9 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-value@81468c96e25a33889542a2f378f7a2d7
---

# Value

What [[coding-learn-go-with-tests-excerpt]] covers about value:

## Statements

- It will be assigned the "zero" value. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00142))_
- We also modified Update to return an error value. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00657))_
- A gotcha with maps is that they can be a nil value. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00609))_
- It is important to question the value of your tests. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00327))_
- Map will not throw an error if the value already exists. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00620))_
- You just need to specify a key and set it equal to a value. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00603))_
- The value type, on the other hand, can be any type you want. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00554))_
- We are still modifying the value, and returning a nil error. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00629))_
- The second is the value type, which goes right after the [] . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00552))_
- You can think of the key as the word and the value as the definition. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00548))_
- The compiler will fail because we are not returning a value for Add . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00625))_
- For tests, %q is very useful as it wraps your values in double quotes. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00034))_
- The compiler will fail because we are not returning a value for Delete . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00692))_
- In our function signature we have made a named return value (prefix string) . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00140))_

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
./shapes_test.go:25:4:	undefined:	Triangle We	have	not	defined Triangle yet Try	again ./shapes_test.go:25:8:	cannot	use	Triangle	literal	(type	Triangle) as	type	Shape	in	field	value: Triangle	does	not	implement	Shape	(missing	Area	method) It's	telling	us	we	cannot	use	a Triangle as	a	shape	because	it	does	not have	an Area() method,	so	add	an	empty	implementation	to	get	the test	working Finally	the	code	compiles	and	we	get	our	error shapes_test.go:31:	got	0.00	want	36.00 type Triangle struct { Base			float64 Height	float64 } func (t	Triangle)	Area()	float64	{ return 0 }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00510))_

```
This	does	not	compile ./dictionary_test.go:18:10:	assignment	mismatch:	2	variables	but	1 values
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00582))_

```
A	map	value	is	a	pointer	to	a	runtime.hmap	structure.
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00607))_

> Except, we didn't consider what happens when the value we are trying to add already exists!
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00619))_


## Source

- [[coding-learn-go-with-tests-excerpt]]
