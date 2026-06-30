---
page_id: coding-learn-go-with-tests-excerpt-section-decoupling-1c6183b3
page_kind: source
summary: Decoupling: 54 source-backed entries and 0 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
page_family: section-reference
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-30
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-decoupling-1c6183b3@f6dcbfe397603116ad5acee6ac5ee7bc
---

# Decoupling

From [[coding-learn-go-with-tests-excerpt]].

## Related pages

- [[coding-learn-go-with-tests-excerpt-section-decoupling-further-refactoring-7cd54aa3]] - narrower source section: Decoupling / Further refactoring
- [[coding-learn-go-with-tests-excerpt-section-decoupling-write-the-test-first-05e88611]] - narrower source section: Decoupling / Write the test first
- [[coding-learn-go-with-tests-excerpt-section-decoupling-write-the-minimal-amount-of-code-for-the-test-to-run-and-check-the-failing-test-outpu-cfea595a]] - narrower source section: Decoupling / Write the minimal amount of code for the test to run and check the failing test output
- [[coding-learn-go-with-tests-excerpt-section-decoupling-write-enough-code-to-make-it-pass-9ad411ad]] - narrower source section: Decoupling / Write enough code to make it pass
- [[coding-learn-go-with-tests-excerpt-section-decoupling-refactor-1b44f28f]] - narrower source section: Decoupling / Refactor
- [[coding-learn-go-with-tests-excerpt-section-decoupling-make-sure-your-test-output-is-helpful-e3d11678]] - narrower source section: Decoupling / Make sure your test output is helpful
- [[coding-learn-go-with-tests-excerpt-section-decoupling-wrapping-up-c20c66cc]] - narrower source section: Decoupling / Wrapping up
- [[coding-learn-go-with-tests-excerpt-section-wait-what-eaeaeb8b]] - previous source section: Wait, what?
- [[coding-learn-go-with-tests-excerpt-section-maps-198341ba]] - next source section: Maps

## Statements

- Notice how our helper does not need to concern itself with whether the shape is a Rectangle or a Circle or a Triangle . By declaring an interface, the helper is decoupled from the concrete types and only has the method it needs to do its job. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00492))_
- This kind of approach of using interfaces to declare only what you need is very important in software design and will be covered in more detail in later sections. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00493))_
- By declaring an interface, the helper is decoupled from the concrete types and only has the method it needs to do its job. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00492))_
- This kind of approach of using interfaces to declare only what you need is very important in software design and will be covered in more detail in later sections. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00493))_

## Statements by subsection

### Decoupling / Further refactoring

- Now that you have some understanding of structs we can introduce "table driven tests". _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00495))_
- The only new syntax here is creating an "anonymous struct", areaTests . We are declaring a slice of structs by using []struct with two fields, the shape and the want . Then we fill the slice with cases. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00498))_
- We then iterate over them just like we do any other slice, using the struct fields to run our tests. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00499))_
- You can see how it would be very easy for a developer to introduce a new shape, implement Area and then add it to the test cases. In addition, if a bug is found with Area it is very easy to add a new test case to exercise it before fixing it. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00500))_
- Table driven tests can be a great item in your toolbox, but be sure that you have a need for the extra noise in the tests. They are a great fit when you wish to test various implementations of an interface, or if the data being passed in to a function has lots of different requirements that need testing. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00501))_
- The only new syntax here is creating an "anonymous struct", areaTests . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00498))_
- Then we fill the slice with cases. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00498))_
- We then iterate over them just like we do any other slice, using the struct fields to run our tests. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00499))_
- In addition, if a bug is found with Area it is very easy to add a new test case to exercise it before fixing it. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00500))_
- You can see how it would be very easy for a developer to introduce a new shape, implement Area and then add it to the test cases. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00500))_

### Decoupling / Write the test first

- Adding a new test for our new shape is very easy. Just add {Triangle{12, 6}, 36.0}, to our list. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00504))_

### Decoupling / Refactor

- Again, the implementation is fine but our tests could do with some improvement. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00514))_
- It's not immediately clear what all the numbers represent and you should be aiming for your tests to be easily understood. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00517))_
- Now our tests - rather, the list of test cases - make assertions of truth about shapes and their areas. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00524))_

### Decoupling / Make sure your test output is helpful

- Remember earlier when we were implementing Triangle and we had the failing test? It printed shapes_test.go:31: got 0.00 want 36.00 . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00526))_
- We knew this was in relation to Triangle because we were just working with it. But what if a bug slipped in to the system in one of 20 cases in the table? How would a developer know which case failed? This is not a great experience for the developer, they will have to manually look through the cases to find out which case actually failed. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00527))_
- We can change our error message into %#v got %g want %g . The %#v format string will print out our struct with the values in its field, so the developer can see at a glance the properties that are being tested. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00528))_
- To increase the readability of our test cases further, we can rename the want field into something more descriptive like hasArea . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00529))_
- One final tip with table driven tests is to use t.Run and to name the test cases. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00530))_
- By wrapping each case in a t.Run you will have clearer test output on failures as it will print the name of the case _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00531))_
- And you can run specific tests within your table with go test -run TestArea/Rectangle . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00533))_
- We knew this was in relation to Triangle because we were just working with it. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00527))_
- And you can run specific tests within your table with go test -run TestArea/Rectangle . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00533))_

### Decoupling / Wrapping up

- This was more TDD practice, iterating over our solutions to basic mathematic problems and learning new language features motivated by our tests. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00537))_
- Declaring structs to create your own data types which lets you bundle related data together and make the intent of your code clearer _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00538))_
- Adding methods so you can add functionality to your data types and so you can implement interfaces _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00540))_
- Table driven tests to make your assertions clearer and your test suites easier to extend & maintain _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00541))_
- This was an important chapter because we are now starting to define our own types. In statically typed languages like Go, being able to design your own types is essential for building software that is easy to understand, to piece together and to test. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00542))_
- Interfaces are a great tool for hiding complexity away from other parts of the system. In our case our test helper code did not need to know the exact shape it was asserting on, only how to "ask" for its area. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00543))_
- As you become more familiar with Go you will start to see the real strength of interfaces and the standard library. You'll learn about interfaces defined in the standard library that are used everywhere and by implementing them against your own types, you can very quickly re-use a lot of great functionality. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00544))_
- This was an important chapter because we are now starting to define our own types. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00542))_
- In our case our test helper code did not need to know the exact shape it was asserting on, only how to "ask" for its area. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00543))_
