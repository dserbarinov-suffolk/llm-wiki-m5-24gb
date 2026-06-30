---
page_id: coding-learn-go-with-tests-excerpt-array
page_kind: concept
summary: Array: 12 statement(s) and 4 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
page_family: topic-concept
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-30
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-array@955762311c878d48bc6e8088b1036193
---

# Array

What [[coding-learn-go-with-tests-excerpt]] covers about array:

## Statements

### Arrays and slices

- Arrays allow you to store multiple elements of the same type in a variable in a particular order. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00276))_

- When you have arrays, it is very common to have to iterate over them. So let's use our new-found knowledge of for to make a Sum function. Sum will take an array of numbers and return the total. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00277))_

### Arrays and slices / Write the test first

- Arrays have a fi xed capacity which you define when you declare the variable. We can initialize an array in two ways: _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00282))_

- It is sometimes useful to also print the inputs to the function in the error message. Here, we are using the %v placeholder to print the "default" format, which works well for arrays. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00285))_

### Arrays and slices / Write enough code to make it pass

- To get the value out of an array at a particular index, just use array[index] syntax. In this case, we are using for to iterate 5 times to work through the array and add each item onto sum . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00297))_

### Arrays and their type

- An interesting property of arrays is that the size is encoded in its type. If you try to pass an [4]int into a function that expects [5]int , it won't compile. They are different types so it's just the same as trying to pass a string into a function that wants an int . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00303))_

- You may be thinking it's quite cumbersome that arrays have a fixed length, and most of the time you probably won't be using them! _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00304))_

### Arrays and their type / Refactor

- We already refactored Sum - all we did was replace arrays with slices, so no extra changes are required. Remember that we must not neglect our test code in the refactoring stage - we can further improve our Sum tests. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00325))_

### Arrays and their type / Write enough code to make it pass

- You can index slices like arrays with mySlice[N] to get the value out or assign it a new value with = _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00357))_

### Arrays and their type / Wrapping up

- We've used slices and arrays with integers but they work with any other type too, including arrays/slices themselves. So you can declare a variable of [][]string if you need to. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00404))_

- Here is an example of slicing an array and how changing the slice affects the original array; but a "copy" of the slice will not affect the original array. Another example of why it's a good idea to make a copy of a slice after slicing a very large slice. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00407))_


## Technical atoms

### Technical frame 1: Arrays and slices / Write the test first

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00285))_

> It is sometimes useful to also print the inputs to the function in the error message. Here, we are using the %v placeholder to print the "default" format, which works well for arrays.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00283))_

```
[N]type{value1, value2, ..., valueN} e.g. numbers := [5]int{1, 2, 
3, 4, 5}
[...]type{value1, value2, ..., valueN} e.g. numbers := [...]int{1, 2,
```

### Technical frame 2: Arrays and their type / Write the test first

**Atoms:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00309, source-range-cb73a893-00311))_

> mySlice := []int{1,2,3}

> myArray := [3]int{1,2,3}

### Technical frame 3: Arrays and their type / Refactor

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00327))_

> It is important to question the value of your tests. It should not be a goal to have as many tests as possible, but rather to have as much confidence as possible in your code base. Having too many tests can turn in to a real problem and it just adds more overhead in maintenance. Every test has a cost .

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00326))_

```
func TestSum(t *testing.T) {
t.Run("collection of 5 numbers", func(t *testing.T) {
        numbers := []int{1, 2, 3, 4, 5}
got := Sum(numbers)
        want := 15
if got != want {
            t.Errorf("got %d want %d given, %v", got, want, numbers)
        }
    })
t.Run("collection of any size", func(t *testing.T) {
        numbers := []int{1, 2, 3}
got := Sum(numbers)
        want := 6
if got != want {
            t.Errorf("got %d want %d given, %v", got, want, numbers)
        }
    })
}
```


## Related pages

- [[coding-learn-go-with-tests-excerpt-write-test]] - shared statements and technical atoms: Write the test first shares source evidence from Arrays and slices / Write the test first: Arrays have a fi xed capacity which you define when you declare the variable. We can initialize an array in two ways:; Write the test first shares technical record from Arrays and slices / Write the test first: [N]type{value1, value2, ..., valueN} e.g. numbers := [5]int{1, 2, 3, 4, 5} [...]type{value1, value2, ..., valueN} e.g. numbers := [...]int{1, 2, (2 shared statement(s), 3 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-test]] - shared technical atoms: Test shares technical record from Arrays and their type / Refactor: func TestSum(t *testing.T) { t.Run("collection of 5 numbers", func(t *testing.T) { numbers := []int{1, 2, 3, 4, 5} got := Sum(numbers) want := 15 if got != want { t. ... [truncated] (1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-write-code-pass]] - shared statements: Write enough code to make it pass shares source evidence from Arrays and slices / Write enough code to make it pass: To get the value out of an array at a particular index, just use array[index] syntax. In this case, we are using for to iterate 5 times to work through the array and ... [truncated] (3 shared statement(s))
- [[coding-learn-go-with-tests-excerpt-value]] - shared statements: Value shares source evidence from Arrays and slices / Write enough code to make it pass: To get the value out of an array at a particular index, just use array[index] syntax. In this case, we are using for to iterate 5 times to work through the array and ... [truncated] (1 shared statement(s))

## Source

- [[coding-learn-go-with-tests-excerpt]]
