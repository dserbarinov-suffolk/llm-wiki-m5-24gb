---
page_id: coding-learn-go-with-tests-excerpt-section-arrays-and-slices-648d683c
page_kind: source
summary: Arrays and slices: 20 source-backed entries and 0 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
page_family: section-reference
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-30
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-arrays-and-slices-648d683c@32ac6fd6e8ae2d060769d14d40b008a5
---

# Arrays and slices

From [[coding-learn-go-with-tests-excerpt]].

## Related pages

- [[coding-learn-go-with-tests-excerpt-section-arrays-and-slices-write-the-test-first-0df2234d]] - narrower source section: Arrays and slices / Write the test first
- [[coding-learn-go-with-tests-excerpt-section-arrays-and-slices-try-to-run-the-test-781534ae]] - narrower source section: Arrays and slices / Try to run the test
- [[coding-learn-go-with-tests-excerpt-section-arrays-and-slices-write-the-minimal-amount-of-code-for-the-test-to-run-and-check-the-failing-tes-a24fad7d]] - narrower source section: Arrays and slices / Write the minimal amount of code for the test to run and check the failing test output
- [[coding-learn-go-with-tests-excerpt-section-arrays-and-slices-write-enough-code-to-make-it-pass-52249515]] - narrower source section: Arrays and slices / Write enough code to make it pass
- [[coding-learn-go-with-tests-excerpt-section-arrays-and-slices-refactor-d443a668]] - narrower source section: Arrays and slices / Refactor
- [[coding-learn-go-with-tests-excerpt-section-benchmarking-5c1bee15]] - previous source section: Benchmarking
- [[coding-learn-go-with-tests-excerpt-section-arrays-and-their-type-0c35221e]] - next source section: Arrays and their type

## Statements

- Arrays allow you to store multiple elements of the same type in a variable in a particular order. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00276))_
- When you have arrays, it is very common to have to iterate over them. So let's use our new-found knowledge of for to make a Sum function. Sum will take an array of numbers and return the total. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00277))_

## Statements by subsection

### Arrays and slices / Write the test first

- Arrays have a fi xed capacity which you define when you declare the variable. We can initialize an array in two ways: _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00282))_
- It is sometimes useful to also print the inputs to the function in the error message. Here, we are using the %v placeholder to print the "default" format, which works well for arrays. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00285))_

### Arrays and slices / Try to run the test

- If you had initialized go mod with go mod init main you will be presented with an error _testmain.go:13:2: cannot import "main" . This is because according to common practice, package main will only contain integration of other packages and not unit-testable code and hence Go will not allow you to import a package with name main . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00288))_
- To fix this, you can rename the main module in go.mod to any other name. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00289))_
- Once the above error is fixed, if you run go test the compiler will fail with the familiar ./sum_test.go:10:15: undefined: Sum error. Now we can proceed with writing the actual method to be tested. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00290))_
- This is because according to common practice, package main will only contain integration of other packages and not unit-testable code and hence Go will not allow you to import a package with name main . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00288))_

### Arrays and slices / Write enough code to make it pass

- To get the value out of an array at a particular index, just use array[index] syntax. In this case, we are using for to iterate 5 times to work through the array and add each item onto sum . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00297))_
