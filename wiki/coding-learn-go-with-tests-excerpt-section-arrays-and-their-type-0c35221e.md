---
page_id: coding-learn-go-with-tests-excerpt-section-arrays-and-their-type-0c35221e
page_kind: source
summary: Arrays and their type: 86 source-backed entries and 2 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
page_family: section-reference
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-30
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-arrays-and-their-type-0c35221e@77cc6ae7830939a2e7811388a542e970
---

# Arrays and their type

From [[coding-learn-go-with-tests-excerpt]].

## Related pages

- [[coding-learn-go-with-tests-excerpt-section-arrays-and-their-type-write-the-test-first-73b871d4]] - narrower source section: Arrays and their type / Write the test first
- [[coding-learn-go-with-tests-excerpt-section-arrays-and-their-type-try-and-run-the-test-19f0372e]] - narrower source section: Arrays and their type / Try and run the test
- [[coding-learn-go-with-tests-excerpt-section-arrays-and-their-type-write-the-minimal-amount-of-code-for-the-test-to-run-and-check-the-failing-ba6a9160]] - narrower source section: Arrays and their type / Write the minimal amount of code for the test to run and check the failing test output
- [[coding-learn-go-with-tests-excerpt-section-arrays-and-their-type-write-enough-code-to-make-it-pass-b28de2ad]] - narrower source section: Arrays and their type / Write enough code to make it pass
- [[coding-learn-go-with-tests-excerpt-section-arrays-and-their-type-refactor-0e79c1f5]] - narrower source section: Arrays and their type / Refactor
- [[coding-learn-go-with-tests-excerpt-section-arrays-and-their-type-write-the-test-first-08e30bdd]] - narrower source section: Arrays and their type / Write the test first
- [[coding-learn-go-with-tests-excerpt-section-arrays-and-their-type-try-and-run-the-test-501a4c76]] - narrower source section: Arrays and their type / Try and run the test
- [[coding-learn-go-with-tests-excerpt-section-arrays-and-their-type-write-the-minimal-amount-of-code-for-the-test-to-run-and-check-the-failing-f1b6d194]] - narrower source section: Arrays and their type / Write the minimal amount of code for the test to run and check the failing test output
- [[coding-learn-go-with-tests-excerpt-section-arrays-and-their-type-write-enough-code-to-make-it-pass-e067099b]] - narrower source section: Arrays and their type / Write enough code to make it pass
- [[coding-learn-go-with-tests-excerpt-section-arrays-and-their-type-refactor-8b9fe3c9]] - narrower source section: Arrays and their type / Refactor
- [[coding-learn-go-with-tests-excerpt-section-arrays-and-their-type-write-the-test-first-6cd5dd08]] - narrower source section: Arrays and their type / Write the test first
- [[coding-learn-go-with-tests-excerpt-section-arrays-and-their-type-try-and-run-the-test-8c8dea3f]] - narrower source section: Arrays and their type / Try and run the test
- [[coding-learn-go-with-tests-excerpt-section-arrays-and-their-type-write-the-minimal-amount-of-code-for-the-test-to-run-and-check-the-failing-682609ea]] - narrower source section: Arrays and their type / Write the minimal amount of code for the test to run and check the failing test output
- [[coding-learn-go-with-tests-excerpt-section-arrays-and-their-type-write-enough-code-to-make-it-pass-5bb60d7b]] - narrower source section: Arrays and their type / Write enough code to make it pass
- [[coding-learn-go-with-tests-excerpt-section-arrays-and-their-type-write-the-test-first-1f50e379]] - narrower source section: Arrays and their type / Write the test first
- [[coding-learn-go-with-tests-excerpt-section-arrays-and-their-type-try-and-run-the-test-dbff4772]] - narrower source section: Arrays and their type / Try and run the test
- [[coding-learn-go-with-tests-excerpt-section-arrays-and-their-type-write-enough-code-to-make-it-pass-e71e4d2b]] - narrower source section: Arrays and their type / Write enough code to make it pass
- [[coding-learn-go-with-tests-excerpt-section-arrays-and-their-type-refactor-1446fc86]] - narrower source section: Arrays and their type / Refactor
- [[coding-learn-go-with-tests-excerpt-section-arrays-and-their-type-wrapping-up-53597979]] - narrower source section: Arrays and their type / Wrapping up
- [[coding-learn-go-with-tests-excerpt-section-arrays-and-slices-648d683c]] - previous source section: Arrays and slices
- [[coding-learn-go-with-tests-excerpt-section-structs-methods-interfaces-82e8585b]] - next source section: Structs, methods & interfaces

## Statements

- An interesting property of arrays is that the size is encoded in its type. If you try to pass an [4]int into a function that expects [5]int , it won't compile. They are different types so it's just the same as trying to pass a string into a function that wants an int . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00303))_
- You may be thinking it's quite cumbersome that arrays have a fixed length, and most of the time you probably won't be using them! _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00304))_
- Go has slices which do not encode the size of the collection and instead can have any size. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00305))_
- The next requirement will be to sum collections of varying sizes. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00306))_

## Statements by subsection

### Arrays and their type / Write enough code to make it pass

- It turns out that fixing the compiler problems were all we need to do here and the tests pass! _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00323))_

### Arrays and their type / Refactor

- We already refactored Sum - all we did was replace arrays with slices, so no extra changes are required. Remember that we must not neglect our test code in the refactoring stage - we can further improve our Sum tests. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00325))_
- It is important to question the value of your tests. It should not be a goal to have as many tests as possible, but rather to have as much confidence as possible in your code base. Having too many tests can turn in to a real problem and it just adds more overhead in maintenance. Every test has a cost . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00327))_
- In our case, you can see that having two tests for this function is redundant. If it works for a slice of one size it's very likely it'll work for a slice of any size (within reason). _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00328))_
- Go's built-in testing toolkit features a coverage tool. Whilst striving for 100% coverage should not be your end goal, the coverage tool can help identify areas of your code not covered by tests. If you have been strict with TDD, it's quite likely you'll have close to 100% coverage anyway. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00329))_
- Now that we are happy we have a well-tested function you should commit your great work before taking on the next challenge. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00333))_
- We need a new function called SumAll which will take a varying number of slices, returning a new slice containing the totals for each slice passed in. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00334))_
- If it works for a slice of one size it's very likely it'll work for a slice of any size (within reason). _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00328))_
- Now that we are happy we have a well-tested function you should commit your great work before taking on the next challenge. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00333))_

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
- However, you can use the append function which takes a slice and a new value, then returns a new slice with all the items in it. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00361))_
- The tail of a collection is all items in the collection except the first one (the "head"). _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00365))_

### Arrays and their type / Write enough code to make it pass

- Slices can be sliced! The syntax is slice[low:high] . If you omit the value on one of the sides of the : it captures everything to that side of it. In our case, we are saying "take from 1 to the end" with numbers[1:] . You may wish to spend some time writing other tests around slices and experiment with the slice operator to get more familiar with it. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00374))_

### Arrays and their type / Try and run the test

- Oh no! It's important to note that while the test has compiled , it has a runtime error . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00382))_
- Compile time errors are our friend because they help us write software that works, runtime errors are our enemies because they affect our users. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00383))_
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
- Another example of why it's a good idea to make a copy of a slice after slicing a very large slice. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00407))_

## Technical atoms

### Technical frame 1: Arrays and their type / Write the test first

**Atoms:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00309, source-range-cb73a893-00311))_

> mySlice := []int{1,2,3}

> myArray := [3]int{1,2,3}
