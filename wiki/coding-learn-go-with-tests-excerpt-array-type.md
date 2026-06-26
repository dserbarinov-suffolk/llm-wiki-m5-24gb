---
page_id: coding-learn-go-with-tests-excerpt-array-type
page_kind: concept
summary: Arrays and their type: 49 statement(s) and 19 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-array-type@f8a56ed1d7853a714e3edb4214ac02ed
---

# Arrays and their type

What [[coding-learn-go-with-tests-excerpt]] covers about arrays and their type:

## Statements

- The key type is special. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00553))_
- We can create a simple type using a struct . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00428))_
- Sum will take an array of numbers and return the total. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00277))_
- We added our own error type and are returning a nil error. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00663))_
- We can define methods on our newly defined types instead. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00446))_
- The first is the key type, which is written inside the [] . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00552))_
- The value type, on the other hand, can be any type you want. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00554))_
- The second is the value type, which goes right after the [] . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00552))_
- Comparable types are explained in depth in the language spec. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00553))_
- With the custom type defined, we can create the Search method. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00574))_
- We added yet another error type for when the word does not exist. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00657))_
- We started using the Dictionary type, which we have not defined yet. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00570))_
- When you have arrays, it is very common to have to iterate over them. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00277))_
- An interesting property of arrays is that the size is encoded in its type. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00303))_

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

> We already refactored Sum - all we did was replace arrays with slices, so no extra changes are required.
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00325))_

> There's a new way to create a slice. make allows you to create a slice with a starting capacity of the len of the numbersToSum we need to work through. The length of a slice is the number of elements it holds len(mySlice) , while the capacity is the number of elements it can hold in the underlying array cap(mySlice) , e.g., make([]int, 0, 5) creates a slice with length 0 and capacity 5.
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00356))_

```
$	go	test ./sum_test.go:52:21:	cannot	use	"dave" ( type	string ) as	type	[]int in	argument	to	checkSums
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00393))_


## Source

- [[coding-learn-go-with-tests-excerpt]]
