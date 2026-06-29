---
page_id: coding-learn-go-with-tests-excerpt-array-and-slice
page_kind: concept
summary: Arrays and slices: 12 statement(s) and 7 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-29
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-array-and-slice@26eba3b3e0ba7b4fdbc0fe0231a1e3a5
---

# Arrays and slices

What [[coding-learn-go-with-tests-excerpt]] covers about arrays and slices:

## Statements

### Arrays and slices

- Arrays allow you to store multiple elements of the same type in a variable in a particular order. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00276))_

- When you have arrays, it is very common to have to iterate over them. So let's use our new-found knowledge of for to make a Sum function. Sum will take an array of numbers and return the total. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00277))_

### Arrays and slices / Write the test first

- Arrays have a fi xed capacity which you define when you declare the variable. We can initialize an array in two ways: _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00282))_

- It is sometimes useful to also print the inputs to the function in the error message. Here, we are using the %v placeholder to print the "default" format, which works well for arrays. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00285))_

### Arrays and slices / Try to run the test

- If you had initialized go mod with go mod init main you will be presented with an error _testmain.go:13:2: cannot import "main" . This is because according to common practice, package main will only contain integration of other packages and not unit-testable code and hence Go will not allow you to import a package with name main . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00288))_

- To fix this, you can rename the main module in go.mod to any other name. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00289))_

- Once the above error is fixed, if you run go test the compiler will fail with the familiar ./sum_test.go:10:15: undefined: Sum error. Now we can proceed with writing the actual method to be tested. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00290))_

### Arrays and slices / Write enough code to make it pass

- To get the value out of an array at a particular index, just use array[index] syntax. In this case, we are using for to iterate 5 times to work through the array and add each item onto sum . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00297))_


## Technical atoms

### Technical frame 1: Arrays and slices

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00276))_

> Arrays allow you to store multiple elements of the same type in a variable in a particular order.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00277))_

> When you have arrays, it is very common to have to iterate over them.

### Technical frame 2: Arrays and slices / Write the test first

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00282))_

> Arrays have a fi xed capacity which you define when you declare the variable. We can initialize an array in two ways:

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00281))_

```
package main
import "testing"
func TestSum(t *testing.T) {
numbers := [5]int{1, 2, 3, 4, 5}
got := Sum(numbers)
    want := 15
if got != want {
        t.Errorf("got %d want %d given, %v", got, want, numbers)
    }
}
```

### Technical frame 3: Arrays and slices / Write the test first

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00285))_

> It is sometimes useful to also print the inputs to the function in the error message. Here, we are using the %v placeholder to print the "default" format, which works well for arrays.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00283))_

```
[N]type{value1, value2, ..., valueN} e.g. numbers := [5]int{1, 2, 
3, 4, 5}
[...]type{value1, value2, ..., valueN} e.g. numbers := [...]int{1, 2,
```

### Technical frame 4: Arrays and slices / Write the minimal amount of code for the test to run and check the failing test output

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00292))_

```
package main
func Sum(numbers [5]int) int {
    return 0
}
```

### Technical frame 5: Arrays and slices / Write the minimal amount of code for the test to run and check the failing test output

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00294))_

```
sum_test.go:13: got 0 want 15 given, [1 2 3 4 5]
```

### Technical frame 6: Arrays and slices / Write enough code to make it pass

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00297))_

> To get the value out of an array at a particular index, just use array[index] syntax. In this case, we are using for to iterate 5 times to work through the array and add each item onto sum .

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00296))_

```
func Sum(numbers [5]int) int {
    sum := 0
    for i := 0; i < 5; i++ {
        sum += numbers[i]
    }
    return sum
}
```

### Technical frame 7: Arrays and slices / Refactor

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00300))_

```
func Sum(numbers [5]int) int {
    sum := 0
    for _, number := range numbers {
        sum += number
    }
    return sum
}
```


## Related pages

- [[coding-learn-go-with-tests-excerpt-array]] - broader topic: Array shares source evidence from Arrays and slices: Arrays allow you to store multiple elements of the same type in a variable in a particular order.; Array shares technical record from Arrays and slices / Write the test first: [N]type{value1, value2, ..., valueN} e.g. numbers := [5]int{1, 2, 3, 4, 5} [...]type{value1, value2, ..., valueN} e.g. numbers := [...]int{1, 2, (6 shared statement(s), 1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-section-arrays-and-slices-648d683c]] - source section: Arrays and slices shares source evidence from Arrays and slices: Arrays allow you to store multiple elements of the same type in a variable in a particular order.; Arrays and slices shares technical record from Arrays and slices: When you have arrays, it is very common to have to iterate over them. (12 shared statement(s), 7 shared atom(s))

## Source

- [[coding-learn-go-with-tests-excerpt]]
