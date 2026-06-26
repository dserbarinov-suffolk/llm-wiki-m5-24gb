---
page_id: coding-learn-go-with-tests-excerpt-array-slice
page_kind: concept
summary: Arrays and slices: 29 statement(s) and 8 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-array-slice@4c5a75ba5288f302e5b011dbee2ad5d0
---

# Arrays and slices

What [[coding-learn-go-with-tests-excerpt]] covers about arrays and slices:

## Statements

- The syntax is slice[low:high] . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00374))_
- As mentioned, slices have a capacity. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00360))_
- Sum will take an array of numbers and return the total. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00277))_
- Go does not let you use equality operators with slices. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00347))_
- When you have arrays, it is very common to have to iterate over them. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00277))_
- An interesting property of arrays is that the size is encoded in its type. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00303))_
- I have made a go playground with a slice in it for you to experiment with. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00406))_
- Arrays have a fi xed capacity which you define when you declare the variable. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00282))_
- So, it can't be applied to slices with non-comparable elements like 2D slices. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00348))_
- Getting a value out of a Map is the same as getting a value out of Array map[key] . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00562))_
- To get the value out of an array at a particular index, just use array[index] syntax. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00297))_
- How they have a fi xed capacity but you can create new slices from old ones using append _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00399))_
- Go has slices which do not encode the size of the collection and instead can have any size. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00305))_
- Arrays allow you to store multiple elements of the same type in a variable in a particular order. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00276))_

## Technical atoms

> We already refactored Sum - all we did was replace arrays with slices, so no extra changes are required.
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00325))_

```
./sum_test.go:26:9:	invalid	operation:	got	!=	want	(slice	can	only be	compared	to	nil)
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00346))_

```
func TestSumAll(t	*testing.T)	{ got	:=	SumAll([]int{1,	2},	[]int{0,	9}) want	:=	[]int{3,	9} if !slices.Equal(got,	want)	{ t.Errorf("got	%v	want	%v",	got,	want) } }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00350))_

> There's a new way to create a slice. make allows you to create a slice with a starting capacity of the len of the numbersToSum we need to work through. The length of a slice is the number of elements it holds len(mySlice) , while the capacity is the number of elements it can hold in the underlying array cap(mySlice) , e.g., make([]int, 0, 5) creates a slice with length 0 and capacity 5.
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00356))_

> Slices can be sliced!
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00374))_

```
func TestSumAllTails(t	*testing.T)	{ t.Run("make	the	sums	of	some	slices", func (t	*testing.T)	{ got	:=	SumAllTails([]int{1,	2},	[]int{0,	9}) want	:=	[]int{2,	9} if !reflect.DeepEqual(got,	want)	{ t.Errorf("got	%v	want	%v",	got,	want) } }) t.Run("safely	sum	empty	slices", func (t	*testing.T)	{ got	:=	SumAllTails([]int{},	[]int{3,	4,	5}) want	:=	[]int{0,	9} if !reflect.DeepEqual(got,	want)	{ t.Errorf("got	%v	want	%v",	got,	want) } }) }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00379))_


## Source

- [[coding-learn-go-with-tests-excerpt]]
