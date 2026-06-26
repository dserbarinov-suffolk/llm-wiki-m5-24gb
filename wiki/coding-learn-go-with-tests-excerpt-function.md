---
page_id: coding-learn-go-with-tests-excerpt-function
page_kind: concept
summary: Function: 7 statement(s) and 6 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-function@f2e7c6bb9d7eb3f4f67877719d1f06fc
---

# Function

What [[coding-learn-go-with-tests-excerpt]] covers about function:

## Statements

- In our function signature we have made a named return value (prefix string) . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00140))_
- Example functions are compiled whenever tests are executed. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00199))_
- Note that this function expects the elements to be comparable. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00348))_
- Hiding variables and functions that don't need to be exported is an important design consideration. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00391))_
- The function can report that the word is not in the dictionary. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00577))_
- So when you pass a map to a function/method, you are indeed copying it, but just the pointer part, not the underlying data structure that contains the data. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00608))_
- This function looks almost identical to Add except we switched when we update the dictionary and when we return an error. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00669))_

## Technical atoms

> Context: Example functions begin with Example (much like test functions begin with Test ), and reside in a package's _test.go files. Add the following ExampleAdd function to the adder_test.go file. (If your editor doesn't automatically import packages for you, the compilation step will fail because you will be missing import "fmt" in adder_test.go . It is strongly recommended you research how to have these kind of errors fixed for you automatically in whatever editor you are using.)
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00200, source-range-559be4b1-00202))_

```
func ExampleAdd()	{ sum	:=	Add(1,	5) fmt.Println(sum) //	Output:	6 }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00201))_

> Context: Running the package's test suite, we can see the example ExampleAdd function is executed with no further arrangement from us: Notice the special format of the comment, // Output: 6 . While the example will always be compiled, adding this comment means the example will also be executed. Go ahead and temporarily remove the comment // Output: 6 , then run go test , and you will see ExampleAdd is no longer executed.
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00204, source-range-559be4b1-00206))_

```
$	go	test	-v ===	RUN			TestAdder ---	PASS:	TestAdder ( 0.00s ) ===	RUN			ExampleAdd ---	PASS:	ExampleAdd ( 0.00s )
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00205))_

> Context: From Go 1.21, slices standard package is available, which has slices.Equal function to do a simple shallow compare on slices, where you don't need to worry about the types like the above case. Note that this function expects the elements to be comparable. So, it can't be applied to slices with non-comparable elements like 2D slices.
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00348))_

```
./sum_test.go:26:9:	invalid	operation:	got	!=	want	(slice	can	only be	compared	to	nil)
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00346))_

> Context: Go does not let you use equality operators with slices. You could write a function to iterate over each got and want slice and check their values, but what if we had a more convenient way to do this? You should have test output like the following: sum_test.go:30: got [] want [3 9]
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00347, source-range-559be4b1-00351))_

```
func TestSumAll(t	*testing.T)	{ got	:=	SumAll([]int{1,	2},	[]int{0,	9}) want	:=	[]int{3,	9} if !slices.Equal(got,	want)	{ t.Errorf("got	%v	want	%v",	got,	want) } }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00350))_

> Context: By defining this function inside the test, it cannot be used by other functions in this package. Hiding variables and functions that don't need to be exported is an important design consideration.
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00391))_

```
$	go	test ./sum_test.go:52:21:	cannot	use	"dave" ( type	string ) as	type	[]int in	argument	to	checkSums
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00393))_

> Context: We actually get nothing back. This is good because the program can continue to run, but there is a better approach. The function can report that the word is not in the dictionary. This way, the user isn't left wondering if the word doesn't exist or if there is just no definition (this might not seem very useful for a dictionary. However, it's a scenario that could be key in other usecases).
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00577))_

```
func TestSearch(t	*testing.T)	{ dictionary	:=	Dictionary{"test":	"this	is	just	a	test"} t.Run("known	word", func (t	*testing.T)	{ got,	_	:=	dictionary.Search("test") want	:=	"this	is	just	a	test" assertStrings(t,	got,	want) }) t.Run("unknown	word", func (t	*testing.T)	{ _,	err	:=	dictionary.Search("unknown") want	:=	"could	not	find	the	word	you	were	looking	for" if err	==	nil	{ t.Fatal("expected	to	get	an	error.") } assertStrings(t,	err.Error(),	want) }) }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00578))_


## Source

- [[coding-learn-go-with-tests-excerpt]]
