---
page_id: coding-learn-go-with-tests-excerpt-array-and-type
page_kind: concept
summary: Arrays and their type: 50 statement(s) and 29 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-29
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-array-and-type@737c6407b738ddbc312043ff5f56a7a2
---

# Arrays and their type

What [[coding-learn-go-with-tests-excerpt]] covers about arrays and their type:

## Statements

### Arrays and their type

- An interesting property of arrays is that the size is encoded in its type. If you try to pass an [4]int into a function that expects [5]int , it won't compile. They are different types so it's just the same as trying to pass a string into a function that wants an int . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00303))_

- You may be thinking it's quite cumbersome that arrays have a fixed length, and most of the time you probably won't be using them! _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00304))_

- Go has slices which do not encode the size of the collection and instead can have any size. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00305))_

- The next requirement will be to sum collections of varying sizes. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00306))_

### Arrays and their type / Write enough code to make it pass

- It turns out that fixing the compiler problems were all we need to do here and the tests pass! _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00323))_

### Arrays and their type / Refactor

- We already refactored Sum - all we did was replace arrays with slices, so no extra changes are required. Remember that we must not neglect our test code in the refactoring stage - we can further improve our Sum tests. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00325))_

- It is important to question the value of your tests. It should not be a goal to have as many tests as possible, but rather to have as much confidence as possible in your code base. Having too many tests can turn in to a real problem and it just adds more overhead in maintenance. Every test has a cost . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00327))_

- In our case, you can see that having two tests for this function is redundant. If it works for a slice of one size it's very likely it'll work for a slice of any size (within reason). _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00328))_

- Go's built-in testing toolkit features a coverage tool. Whilst striving for 100% coverage should not be your end goal, the coverage tool can help identify areas of your code not covered by tests. If you have been strict with TDD, it's quite likely you'll have close to 100% coverage anyway. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00329))_

- Now that we are happy we have a well-tested function you should commit your great work before taking on the next challenge. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00333))_

- We need a new function called SumAll which will take a varying number of slices, returning a new slice containing the totals for each slice passed in. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00334))_

### Arrays and their type / Write the minimal amount of code for the test to run and check the failing test output

- We need to define SumAll according to what our test wants. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00342))_

- Go can let you write variadic functions that can take a variable number of arguments. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00343))_

- This is valid, but our tests still won't compile! _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00345))_

- Go does not let you use equality operators with slices. You could write a function to iterate over each got and want slice and check their values, but what if we had a more convenient way to do this? _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00347))_

- From Go 1.21, slices standard package is available, which has slices.Equal function to do a simple shallow compare on slices, where you don't need to worry about the types like the above case. Note that this function expects the elements to be comparable. So, it can't be applied to slices with non-comparable elements like 2D slices. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00348))_

- You should have test output like the following: sum_test.go:30: got [] want [3 9] _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00351))_

### Arrays and their type / Write enough code to make it pass

- You can index slices like arrays with mySlice[N] to get the value out or assign it a new value with = _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00357))_

- The tests should now pass. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00358))_

### Arrays and their type / Refactor

- As mentioned, slices have a capacity. If you have a slice with a capacity of 2 and try to do mySlice[10] = 1 you will get a runtime error. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00360))_

- However, you can use the append function which takes a slice and a new value, then returns a new slice with all the items in it. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00361))_

- In this implementation, we are worrying less about capacity. We start with an empty slice sums and append to it the result of Sum as we work through the varargs. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00364))_

- Our next requirement is to change SumAll to SumAllTails , where it will calculate the totals of the "tails" of each slice. The tail of a collection is all items in the collection except the first one (the "head"). _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00365))_

### Arrays and their type / Write enough code to make it pass

- Slices can be sliced! The syntax is slice[low:high] . If you omit the value on one of the sides of the : it captures everything to that side of it. In our case, we are saying "take from 1 to the end" with numbers[1:] . You may wish to spend some time writing other tests around slices and experiment with the slice operator to get more familiar with it. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00374))_

### Arrays and their type / Try and run the test

- Oh no! It's important to note that while the test has compiled , it has a runtime error . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00382))_

- Compile time errors are our friend because they help us write software that works, runtime errors are our enemies because they affect our users. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00383))_

### Arrays and their type / Refactor

- We could've created a new function checkSums like we normally do, but in this case, we're showing a new technique, assigning a function to a variable. It might look strange but, it's no different to assigning a variable to a string , or an int , functions in effect are values too. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00389))_

- It's not shown here, but this technique can be useful when you want to bind a function to other local variables in "scope" (e.g between some {} ). It also allows you to reduce the surface area of your API. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00390))_

- By defining this function inside the test, it cannot be used by other functions in this package. Hiding variables and functions that don't need to be exported is an important design consideration. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00391))_

- A handy side-effect of this is this adds a little type-safety to our code. If a developer mistakenly adds a new test with checkSums(t, got, "dave") the compiler will stop them in their tracks. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00392))_

### Arrays and their type / Wrapping up

- How they have a fi xed capacity but you can create new slices from old ones using append _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00399))_

- We've used slices and arrays with integers but they work with any other type too, including arrays/slices themselves. So you can declare a variable of [][]string if you need to. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00404))_

- Another handy way to experiment with Go other than writing tests is the Go playground. You can try most things out and you can easily share your code if you need to ask questions. I have made a go playground with a slice in it for you to experiment with. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00406))_

- Here is an example of slicing an array and how changing the slice affects the original array; but a "copy" of the slice will not affect the original array. Another example of why it's a good idea to make a copy of a slice after slicing a very large slice. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00407))_


## Technical atoms

### Technical frame 1: Arrays and their type / Write the test first

**Atoms:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00309, source-range-cb73a893-00311))_

> mySlice := []int{1,2,3}

> myArray := [3]int{1,2,3}

### Technical frame 2: Arrays and their type / Write the test first

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00312))_

```
func TestSum(t *testing.T) {
t.Run("collection of 5 numbers", func(t *testing.T) {
        numbers := [5]int{1, 2, 3, 4, 5}
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

### Technical frame 3: Arrays and their type / Try and run the test

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00314))_

```
This does not compile
./sum_test.go:22:13: cannot use numbers (type []int) as type [5]int 
in argument to Sum
```

### Technical frame 4: Arrays and their type / Write the minimal amount of code for the test to run and check the failing test output

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00320))_

```
func Sum(numbers []int) int {
    sum := 0
    for _, number := range numbers {
        sum += number
    }
    return sum
}
```

### Technical frame 5: Arrays and their type / Write the minimal amount of code for the test to run and check the failing test output

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00321))_

> If you try to run the tests they will still not compile, you will have to change the first test to pass in a slice rather than an array.

### Technical frame 6: Arrays and their type / Refactor

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

### Technical frame 7: Arrays and their type / Refactor

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00333))_

> Now that we are happy we have a well-tested function you should commit your great work before taking on the next challenge.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00330))_

```
Try running
go test -cover
You should see
```

### Technical frame 8: Arrays and their type / Refactor

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00333))_

> Now that we are happy we have a well-tested function you should commit your great work before taking on the next challenge.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00331))_

```
PASS
coverage: 100.0% of statements
```

### Technical frame 9: Arrays and their type / Refactor

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00334))_

> We need a new function called SumAll which will take a varying number of slices, returning a new slice containing the totals for each slice passed in.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00336))_

```
SumAll([]int{1,2}, []int{0,9}) would return []int{3, 9}
or
SumAll([]int{1,1,1}) would return []int{3}
```

### Technical frame 10: Arrays and their type / Write the test first

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00338))_

```
func TestSumAll(t *testing.T) {
got := SumAll([]int{1, 2}, []int{0, 9})
    want := []int{3, 9}
if got != want {
        t.Errorf("got %v want %v", got, want)
    }
}
```

### Technical frame 11: Arrays and their type / Try and run the test

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00340))_

```
./sum_test.go:23:9: undefined: SumAll
```

### Technical frame 12: Arrays and their type / Write the minimal amount of code for the test to run and check the failing test output

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00345))_

> This is valid, but our tests still won't compile!

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00344))_

```
func SumAll(numbersToSum ...[]int) []int {
    return nil
}
```

### Technical frame 13: Arrays and their type / Write the minimal amount of code for the test to run and check the failing test output

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00347))_

> Go does not let you use equality operators with slices. You could write a function to iterate over each got and want slice and check their values, but what if we had a more convenient way to do this?

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00346))_

```
./sum_test.go:26:9: invalid operation: got != want (slice can only 
be compared to nil)
```

### Technical frame 14: Arrays and their type / Write the minimal amount of code for the test to run and check the failing test output

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00351))_

> You should have test output like the following: sum_test.go:30: got [] want [3 9]

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00350))_

```
func TestSumAll(t *testing.T) {
got := SumAll([]int{1, 2}, []int{0, 9})
    want := []int{3, 9}
if !slices.Equal(got, want) {
        t.Errorf("got %v want %v", got, want)
    }
}
```

### Technical frame 15: Arrays and their type / Write enough code to make it pass

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00357))_

> You can index slices like arrays with mySlice[N] to get the value out or assign it a new value with =

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00354))_

```
func SumAll(numbersToSum ...[]int) []int {
    lengthOfNumbers := len(numbersToSum)
    sums := make([]int, lengthOfNumbers)
for i, numbers := range numbersToSum {
        sums[i] = Sum(numbers)
    }
return sums
}
```

### Technical frame 16: Arrays and their type / Refactor

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00364))_

> In this implementation, we are worrying less about capacity. We start with an empty slice sums and append to it the result of Sum as we work through the varargs.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00362))_

```
func SumAll(numbersToSum ...[]int) []int {
    var sums []int
    for _, numbers := range numbersToSum {
        sums = append(sums, Sum(numbers))
    }
```

### Technical frame 17: Arrays and their type / Refactor

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00364))_

> In this implementation, we are worrying less about capacity. We start with an empty slice sums and append to it the result of Sum as we work through the varargs.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00363))_

```
return sums
}
```

### Technical frame 18: Arrays and their type / Write the test first

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00367))_

```
func TestSumAllTails(t *testing.T) {
    got := SumAllTails([]int{1, 2}, []int{0, 9})
    want := []int{2, 9}
if !reflect.DeepEqual(got, want) {
        t.Errorf("got %v want %v", got, want)
    }
}
```

### Technical frame 19: Arrays and their type / Try and run the test

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00369))_

```
./sum_test.go:26:9: undefined: SumAllTails
```

### Technical frame 20: Arrays and their type / Write the minimal amount of code for the test to run and check the failing test output

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00371))_

```
Rename the function to SumAllTails and re-run the test
sum_test.go:30: got [3 9] want [2 9]
```

### Technical frame 21: Arrays and their type / Write enough code to make it pass

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00374))_

> Slices can be sliced! The syntax is slice[low:high] . If you omit the value on one of the sides of the : it captures everything to that side of it. In our case, we are saying "take from 1 to the end" with numbers[1:] . You may wish to spend some time writing other tests around slices and experiment with the slice operator to get more familiar with it.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00373))_

```
func SumAllTails(numbersToSum ...[]int) []int {
    var sums []int
    for _, numbers := range numbersToSum {
        tail := numbers[1:]
        sums = append(sums, Sum(tail))
    }
return sums
}
```

### Technical frame 22: Arrays and their type / Write the test first

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00379))_

```
func TestSumAllTails(t *testing.T) {
t.Run("make the sums of some slices", func(t *testing.T) {
        got := SumAllTails([]int{1, 2}, []int{0, 9})
        want := []int{2, 9}
if !reflect.DeepEqual(got, want) {
            t.Errorf("got %v want %v", got, want)
        }
    })
t.Run("safely sum empty slices", func(t *testing.T) {
        got := SumAllTails([]int{}, []int{3, 4, 5})
        want := []int{0, 9}
if !reflect.DeepEqual(got, want) {
            t.Errorf("got %v want %v", got, want)
        }
    })
}
```

### Technical frame 23: Arrays and their type / Try and run the test

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00382))_

> Oh no! It's important to note that while the test has compiled , it has a runtime error .

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00381))_

```
panic: runtime error: slice bounds out of range [recovered]
panic: runtime error: slice bounds out of range
```

### Technical frame 24: Arrays and their type / Write enough code to make it pass

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00385))_

```
func SumAllTails(numbersToSum ...[]int) []int {
    var sums []int
    for _, numbers := range numbersToSum {
        if len(numbers) == 0 {
            sums = append(sums, 0)
        } else {
            tail := numbers[1:]
            sums = append(sums, Sum(tail))
        }
    }
return sums
}
```

### Technical frame 25: Arrays and their type / Refactor

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00389))_

> We could've created a new function checkSums like we normally do, but in this case, we're showing a new technique, assigning a function to a variable. It might look strange but, it's no different to assigning a variable to a string , or an int , functions in effect are values too.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00388))_

```
func TestSumAllTails(t *testing.T) {
checkSums := func(t testing.TB, got, want []int) {
        t.Helper()
        if !reflect.DeepEqual(got, want) {
            t.Errorf("got %v want %v", got, want)
        }
    }
t.Run("make the sums of tails of", func(t *testing.T) {
        got := SumAllTails([]int{1, 2}, []int{0, 9})
        want := []int{2, 9}
        checkSums(t, got, want)
    })
t.Run("safely sum empty slices", func(t *testing.T) {
        got := SumAllTails([]int{}, []int{3, 4, 5})
        want := []int{0, 9}
        checkSums(t, got, want)
    })
}
```

### Technical frame 26: Arrays and their type / Refactor

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00392))_

> A handy side-effect of this is this adds a little type-safety to our code. If a developer mistakenly adds a new test with checkSums(t, got, "dave") the compiler will stop them in their tracks.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00393))_

```
$ go test
./sum_test.go:52:21: cannot use "dave" (type string) as type []int 
in argument to checkSums
```

### Technical frame 27: Arrays and their type / Wrapping up

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00406))_

> Another handy way to experiment with Go other than writing tests is the Go playground. You can try most things out and you can easily share your code if you need to ask questions. I have made a go playground with a slice in it for you to experiment with.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00404))_

> So you can declare a variable of [][]string if you need to.

### Technical frame 28: Arrays and their type / Wrapping up

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00407))_

> Here is an example of slicing an array and how changing the slice affects the original array; but a "copy" of the slice will not affect the original array. Another example of why it's a good idea to make a copy of a slice after slicing a very large slice.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00406))_

> You can try most things out and you can easily share your code if you need to ask questions.


## Related pages

- [[coding-learn-go-with-tests-excerpt-array]] - broader topic: Array shares source evidence from Arrays and their type: An interesting property of arrays is that the size is encoded in its type. If you try to pass an [4]int into a function that expects [5]int , it won't compile. They ... [truncated]; Array shares technical record from Arrays and their type / Write the test first: mySlice := []int{1,2,3} (6 shared statement(s), 3 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-wrapping]] - shared statements and technical atoms: Wrapping up shares source evidence from Arrays and their type / Wrapping up: How they have a fi xed capacity but you can create new slices from old ones using append; Wrapping up shares technical record from Arrays and their type / Wrapping up: So you can declare a variable of [][]string if you need to. (6 shared statement(s), 2 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-test]] - shared statements and technical atoms: Test shares source evidence from Arrays and their type / Refactor: It is important to question the value of your tests. It should not be a goal to have as many tests as possible, but rather to have as much confidence as possible in ... [truncated]; Test shares technical record from Arrays and their type / Refactor: func TestSum(t *testing.T) { t.Run("collection of 5 numbers", func(t *testing.T) { numbers := []int{1, 2, 3, 4, 5} got := Sum(numbers) want := 15 if got != want { t. ... [truncated] (5 shared statement(s), 2 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-function]] - shared statements and technical atoms: Function shares source evidence from Arrays and their type / Write the minimal amount of code for the test to run and check the failing test output: From Go 1.21, slices standard package is available, which has slices.Equal function to do a simple shallow compare on slices, where you don't need to worry about the ... [truncated]; Function shares technical record from Arrays and their type / Write the minimal amount of code for the test to run and check the failing test output: ./sum_test.go:26:9: invalid operation: got != want (slice can only be compared to nil) (2 shared statement(s), 3 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-package]] - shared statements and technical atoms: Package shares source evidence from Arrays and their type / Write the minimal amount of code for the test to run and check the failing test output: From Go 1.21, slices standard package is available, which has slices.Equal function to do a simple shallow compare on slices, where you don't need to worry about the ... [truncated]; Package shares technical record from Arrays and their type / Write the minimal amount of code for the test to run and check the failing test output: ./sum_test.go:26:9: invalid operation: got != want (slice can only be compared to nil) (1 shared statement(s), 1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-section-arrays-and-their-type-0c35221e]] - source section: Arrays and their type shares source evidence from Arrays and their type: An interesting property of arrays is that the size is encoded in its type. If you try to pass an [4]int into a function that expects [5]int , it won't compile. They ... [truncated]; Arrays and their type shares technical record from Arrays and their type / Write the test first: mySlice := []int{1,2,3} (50 shared statement(s), 29 shared atom(s))

## Source

- [[coding-learn-go-with-tests-excerpt]]
