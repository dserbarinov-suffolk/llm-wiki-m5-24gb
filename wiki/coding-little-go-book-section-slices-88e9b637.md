---
page_id: coding-little-go-book-section-slices-88e9b637
page_kind: source
summary: Slices: 69 source-backed entries and 23 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: sources/coding-little-go-book/sections
source_id: coding_little_go_book.pdf
projection_coverage: section-coding-little-go-book-section-slices-88e9b637@e34960006bc570b20795666cb6ac47bc
---

# Slices

From [[coding-little-go-book]].

## Statements

- A slice is a lightweight structure that wraps and represents a portion of an array. _(coding_little_go_book.pdf (source-range-810ce361-00200))_
- In Go, you rarely, if ever, use arrays directly. _(coding_little_go_book.pdf (source-range-810ce361-00200))_
- Instead, you use slices. _(coding_little_go_book.pdf (source-range-810ce361-00200))_
- There are a few ways to create a slice, and we'll go over when to use which later on. _(coding_little_go_book.pdf (source-range-810ce361-00200))_
- Unlike the array declaration, our slice isn't declared with a length within the square brackets. _(coding_little_go_book.pdf (source-range-810ce361-00202))_
- Unlike the array declaration, our slice isn't declared with a length within the square brackets. _(coding_little_go_book.pdf (source-range-810ce361-00202))_
- We use make instead of new because there's more to creating a slice than just allocating the memory (which is what new does). _(coding_little_go_book.pdf (source-range-810ce361-00204))_
- Specifically, we have to allocate the memory for the underlying array and also initialize the slice. _(coding_little_go_book.pdf (source-range-810ce361-00204))_
- The length is the size of the slice, the capacity is the size of the underlying array. _(coding_little_go_book.pdf (source-range-810ce361-00204))_
- We use make instead of new because there's more to creating a slice than just allocating the memory (which is what new does). _(coding_little_go_book.pdf (source-range-810ce361-00204))_
- (If you're paying attention, you'll note that make and len are overloaded. _(coding_little_go_book.pdf (source-range-810ce361-00206))_
- Go is a language that, to the frustration of some, makes use of features which aren't exposed for developers to use.) _(coding_little_go_book.pdf (source-range-810ce361-00206))_
- Because our slice has a length of 0. _(coding_little_go_book.pdf (source-range-810ce361-00209))_
- Yes, the underlying array has 10 elements, but we need to explicitly expand our slice in order to access those elements. _(coding_little_go_book.pdf (source-range-810ce361-00209))_
- Because our slice has a length of 0. _(coding_little_go_book.pdf (source-range-810ce361-00209))_
- Appending to a slice of length 0 will set the first element. _(coding_little_go_book.pdf (source-range-810ce361-00211))_
- For whatever reason, our crashing code wanted to set the element at index 7. _(coding_little_go_book.pdf (source-range-810ce361-00211))_
- It turns out that append is pretty special. _(coding_little_go_book.pdf (source-range-810ce361-00213))_
- This is why, in the example above that used append , we had to re-assign the value returned by append to our scores variable: append might have created a new value if the original had no more space. _(coding_little_go_book.pdf (source-range-810ce361-00213))_
- You might be thinking this doesn't actually solve the fixed-length issue of arrays. _(coding_little_go_book.pdf (source-range-810ce361-00213))_
- Up to its capacity which, in this case, is 10. _(coding_little_go_book.pdf (source-range-810ce361-00213))_
- If the underlying array is full, it will create a new larger array and copy the values over (this is exactly how dynamic arrays work in PHP , Python, Ruby, JavaScript, ...). _(coding_little_go_book.pdf (source-range-810ce361-00213))_
- In order to hold 25 values, it'll have to be expanded 3 times with a capacity of 10, 20 and finally 40. _(coding_little_go_book.pdf (source-range-810ce361-00217))_
- The initial capacity of scores is 5. _(coding_little_go_book.pdf (source-range-810ce361-00217))_
- To a compiler, you're telling it to append a value to a slice that already holds 5 values. _(coding_little_go_book.pdf (source-range-810ce361-00220))_
- To a human, that might seem logical. _(coding_little_go_book.pdf (source-range-810ce361-00220))_
- Here, the output is going to be [0, 0, 0, 0, 0, 9332] . _(coding_little_go_book.pdf (source-range-810ce361-00220))_
- You use this when you know the values that you want in the array ahead of time. _(coding_little_go_book.pdf (source-range-810ce361-00223))_
- The first one shouldn't need much of an explanation. _(coding_little_go_book.pdf (source-range-810ce361-00223))_
- The second one is useful when you'll be writing into specific indexes of a slice. _(coding_little_go_book.pdf (source-range-810ce361-00224))_
- The third version is a nil slice and is used in conjunction with append , when the number of elements is unknown. _(coding_little_go_book.pdf (source-range-810ce361-00226))_
- The last version lets us specify an initial capacity; useful if we have a general idea of how many elements we'll need. _(coding_little_go_book.pdf (source-range-810ce361-00227))_
- Even when you know the size, append can be used. _(coding_little_go_book.pdf (source-range-810ce361-00228))_
- Many languages have the concept of slicing an array. _(coding_little_go_book.pdf (source-range-810ce361-00230))_
- Slices as wrappers to arrays is a powerful concept. _(coding_little_go_book.pdf (source-range-810ce361-00230))_
- However, in these languages, a slice is actually a new array with the values of the original copied over. _(coding_little_go_book.pdf (source-range-810ce361-00230))_
- Both JavaScript and Ruby arrays have a slice method. _(coding_little_go_book.pdf (source-range-810ce361-00230))_
- This is because our slice is really just a window into scores . _(coding_little_go_book.pdf (source-range-810ce361-00234))_
- However, unlike the Ruby example above, the Go code will produce an output of [1, 2, 999, 4, 5] . _(coding_little_go_book.pdf (source-range-810ce361-00234))_
- This is because our slice is really just a window into scores . _(coding_little_go_book.pdf (source-range-810ce361-00234))_
- However, unlike the Ruby example above, the Go code will produce an output of [1, 2, 999, 4, 5] . _(coding_little_go_book.pdf (source-range-810ce361-00234))_
- We can see from the above example, that [X:] is shorthand for from X to the end while [:X] is shorthand for from the start up until X . _(coding_little_go_book.pdf (source-range-810ce361-00239))_
- Unlike other languages, Go doesn't support negative values. _(coding_little_go_book.pdf (source-range-810ce361-00239))_
- Normally, a method that copies values from one array to another has 5 parameters: source , sourceStart , count , destination and destinationStart . _(coding_little_go_book.pdf (source-range-810ce361-00244))_
- Finally, now that we know about slices, we can look at another commonly used built-in function: copy . _(coding_little_go_book.pdf (source-range-810ce361-00244))_
- copy is one of those functions that highlights how slices change the way we code. _(coding_little_go_book.pdf (source-range-810ce361-00244))_

## Technical atoms

```
scores	:=	[]int{1,4,293,4,9}
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00201))_

```
scores	:=	make([]int,	10)
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00203))_

```
scores	:=	make([]int,	0,	10)
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00205))_

```
func main()	{ scores	:=	make([]int,	0,	10) scores[7]	=	9033 fmt.Println(scores) }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00208))_

```
func main()	{ scores	:=	make([]int,	0,	10) scores	=	append(scores,	5) fmt.Println(scores) //	prints	[5] }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00210))_

```
func main()	{ scores	:=	make([]int,	0,	10) scores	=	scores[0:8] scores[7]	=	9033 fmt.Println(scores) }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00212))_

```
func main()	{ scores	:=	make([]int,	0,	5)
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00215))_

```
c	:=	cap(scores) fmt.Println(c) for i	:=	0;	i	<	25;	i++	{ scores	=	append(scores,	i) //	if	our	capacity	has	changed, //	Go	had	to	grow	our	array	to	accommodate	the	new	data if cap(scores)	!=	c	{ c	=	cap(scores) fmt.Println(c) } } }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00216))_

```
func main()	{ scores	:=	make([]int,	5) scores	=	append(scores,	9332) fmt.Println(scores) }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00219))_

```
names	:=	[]string{"leto",	"jessica",	"paul"} checks	:=	make([]bool,	10) var names	[]string scores	:=	make([]int,	0,	20)
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00222))_

```
func extractPowers(saiyans	[]*Saiyan)	[]int	{ powers	:=	make([]int,	len(saiyans)) for index,	saiyan	:= range saiyans	{ powers[index]	=	saiyan.Power } return powers }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00225))_

```
func extractPowers(saiyans	[]*Saiyan)	[]int	{ powers	:=	make([]int,	0,	len(saiyans)) for _,	saiyan	:= range saiyans	{ powers	=	append(powers,	saiyan.Power) } return powers }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00229))_

```
scores = [ 1,2,3,4,5 ] slice = scores [ 2 .. 4 ] slice [ 0 ] = 999 puts	scores
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00231))_

> The answer is [1, 2, 3, 4, 5] . That's because slice is a completely new array with copies of values. Now, consider the Go equivalent:
_(source: coding_little_go_book.pdf (source-range-810ce361-00232))_

```
scores	:=	[]int{1,2,3,4,5} slice	:=	scores[2:4] slice[0]	=	999 fmt.Println(scores)
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00233))_

> This changes how you code. For example, a number of functions take a position parameter. In JavaScript, if we want to find the first space in a string (yes, slices work on strings too!) after the first five characters, we'd write:
_(source: coding_little_go_book.pdf (source-range-810ce361-00235))_

```
haystack	=	"the	spice	must	flow"; console.log(haystack.indexOf("	",	5));
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00236))_

```
strings.Index(haystack[5:],	"	")
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00238))_

> If we want all of the values of a slice except the last, we do:
_(source: coding_little_go_book.pdf (source-range-810ce361-00239))_

```
scores	:=	[]int{1,	2,	3,	4,	5} scores	=	scores[:len(scores)-1]
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00240))_

```
func main()	{ scores	:=	[]int{1,	2,	3,	4,	5} scores	=	removeAtIndex(scores,	2) fmt.Println(scores) //	[1	2	5	4] }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00242))_

```
//	won't	preserve	order func removeAtIndex(source	[]int,	index	int)	[]int	{ lastIndex	:=	len(source)	-	1 //swap	the	last	value	and	the	value	we	want	to	remove source[index],	source[lastIndex]	=	source[lastIndex], source[index] return source[:lastIndex] }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00243))_

```
import ( "fmt" "math/rand" "sort" ) func main()	{ scores	:=	make([]int,	100) for i	:=	0;	i	<	100;	i++	{ scores[i]	=	int(rand.Int31n(1000)) } sort.Ints(scores) worst	:=	make([]int,	5) copy(worst,	scores[:5]) fmt.Println(worst) }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00245))_
