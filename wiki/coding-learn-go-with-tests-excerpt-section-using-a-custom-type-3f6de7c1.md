---
page_id: coding-learn-go-with-tests-excerpt-section-using-a-custom-type-3f6de7c1
page_kind: source
summary: Using a custom type: 36 source-backed entries and 0 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
page_family: section-reference
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-30
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-using-a-custom-type-3f6de7c1@340f7d9c3d7ccdb42f29cae3d26bcf90
---

# Using a custom type

From [[coding-learn-go-with-tests-excerpt]].

## Related pages

- [[coding-learn-go-with-tests-excerpt-section-using-a-custom-type-write-the-test-first-4c4dcc55]] - narrower source section: Using a custom type / Write the test first
- [[coding-learn-go-with-tests-excerpt-section-using-a-custom-type-try-and-run-the-test-ebf022ab]] - narrower source section: Using a custom type / Try and run the test
- [[coding-learn-go-with-tests-excerpt-section-using-a-custom-type-write-the-minimal-amount-of-code-for-the-test-to-run-and-check-the-output-96d1b867]] - narrower source section: Using a custom type / Write the minimal amount of code for the test to run and check the output
- [[coding-learn-go-with-tests-excerpt-section-using-a-custom-type-write-enough-code-to-make-it-pass-0fbec14c]] - narrower source section: Using a custom type / Write enough code to make it pass
- [[coding-learn-go-with-tests-excerpt-section-using-a-custom-type-refactor-862871b5]] - narrower source section: Using a custom type / Refactor
- [[coding-learn-go-with-tests-excerpt-section-using-a-custom-type-write-the-test-first-d5397d92]] - narrower source section: Using a custom type / Write the test first
- [[coding-learn-go-with-tests-excerpt-section-using-a-custom-type-write-the-minimal-amount-of-code-for-the-test-to-run-and-check-output-ef8ec6d6]] - narrower source section: Using a custom type / Write the minimal amount of code for the test to run and check output
- [[coding-learn-go-with-tests-excerpt-section-using-a-custom-type-write-enough-code-to-make-it-pass-7b766fd4]] - narrower source section: Using a custom type / Write enough code to make it pass
- [[coding-learn-go-with-tests-excerpt-section-maps-198341ba]] - previous source section: Maps
- [[coding-learn-go-with-tests-excerpt-section-pointers-copies-et-al-36483230]] - next source section: Pointers, copies, et al

## Statements

- We started using the Dictionary type, which we have not defined yet. Then called Search on the Dictionary instance. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00570))_
- We did not need to change assertStrings . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00571))_
- Here we created a Dictionary type which acts as a thin wrapper around map . With the custom type defined, we can create the Search method. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00574))_
- Then called Search on the Dictionary instance. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00570))_

## Statements by subsection

### Using a custom type / Write the test first

- We actually get nothing back. This is good because the program can continue to run, but there is a better approach. The function can report that the word is not in the dictionary. This way, the user isn't left wondering if the word doesn't exist or if there is just no definition (this might not seem very useful for a dictionary. However, it's a scenario that could be key in other usecases). _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00577))_
- The way to handle this scenario in Go is to return a second argument which is an Error type. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00579))_
- Notice that as we've seen in the pointers and error section here in order to assert the error message we first check that the error is not nil and then use .Error() method to get the string which we can then pass to the assertion. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00580))_
- This is good because the program can continue to run, but there is a better approach. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00577))_
- Notice that as we've seen in the pointers and error section here in order to assert the error message we first check that the error is not nil and then use .Error() method to get the string which we can then pass to the assertion. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00580))_

### Using a custom type / Write the minimal amount of code for the test to run and check the output

- Your test should now fail with a much clearer error message. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00585))_
- dictionary_test.go:22: expected to get an error. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00586))_

### Using a custom type / Write enough code to make it pass

- In order to make this pass, we are using an interesting property of the map lookup. It can return 2 values. The second value is a boolean which indicates if the key was found successfully. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00589))_
- This property allows us to differentiate between a word that doesn't exist and a word that just doesn't have a definition. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00590))_

### Using a custom type / Refactor

- By creating a new helper we were able to simplify our test, and start using our ErrNotFound variable so our test doesn't fail if we change the error text in the future. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00594))_

### Using a custom type / Write the test first

- We have a great way to search the dictionary. However, we have no way to add new words to our dictionary. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00596))_
- In this test, we are utilizing our Search function to make the validation of the dictionary a little easier. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00598))_

### Using a custom type / Write enough code to make it pass

- Adding to a map is also similar to an array. You just need to specify a key and set it equal to a value. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00603))_
