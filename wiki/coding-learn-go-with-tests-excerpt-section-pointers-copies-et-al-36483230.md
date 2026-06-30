---
page_id: coding-learn-go-with-tests-excerpt-section-pointers-copies-et-al-36483230
page_kind: source
summary: Pointers, copies, et al: 60 source-backed entries and 0 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
page_family: section-reference
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-30
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-pointers-copies-et-al-36483230@ee6697eb6a96c267458f639b5bdf32e7
---

# Pointers, copies, et al

From [[coding-learn-go-with-tests-excerpt]].

## Related pages

- [[coding-learn-go-with-tests-excerpt-section-pointers-copies-et-al-refactor-5d607a3f]] - narrower source section: Pointers, copies, et al / Refactor
- [[coding-learn-go-with-tests-excerpt-section-pointers-copies-et-al-write-the-test-first-195162d9]] - narrower source section: Pointers, copies, et al / Write the test first
- [[coding-learn-go-with-tests-excerpt-section-pointers-copies-et-al-try-to-run-test-66becf89]] - narrower source section: Pointers, copies, et al / Try to run test
- [[coding-learn-go-with-tests-excerpt-section-pointers-copies-et-al-write-the-minimal-amount-of-code-for-the-test-to-run-and-check-the-output-7f59b214]] - narrower source section: Pointers, copies, et al / Write the minimal amount of code for the test to run and check the output
- [[coding-learn-go-with-tests-excerpt-section-pointers-copies-et-al-write-enough-code-to-make-it-pass-6f139db5]] - narrower source section: Pointers, copies, et al / Write enough code to make it pass
- [[coding-learn-go-with-tests-excerpt-section-pointers-copies-et-al-refactor-c066e9e2]] - narrower source section: Pointers, copies, et al / Refactor
- [[coding-learn-go-with-tests-excerpt-section-pointers-copies-et-al-write-the-test-first-764407b8]] - narrower source section: Pointers, copies, et al / Write the test first
- [[coding-learn-go-with-tests-excerpt-section-pointers-copies-et-al-try-and-run-the-test-22b48658]] - narrower source section: Pointers, copies, et al / Try and run the test
- [[coding-learn-go-with-tests-excerpt-section-pointers-copies-et-al-write-minimal-amount-of-code-for-the-test-to-run-and-check-the-failing-tes-7802db7d]] - narrower source section: Pointers, copies, et al / Write minimal amount of code for the test to run and check the failing test output
- [[coding-learn-go-with-tests-excerpt-section-pointers-copies-et-al-write-enough-code-to-make-it-pass-618028a3]] - narrower source section: Pointers, copies, et al / Write enough code to make it pass
- [[coding-learn-go-with-tests-excerpt-section-pointers-copies-et-al-write-the-test-first-9d6f8acb]] - narrower source section: Pointers, copies, et al / Write the test first
- [[coding-learn-go-with-tests-excerpt-section-pointers-copies-et-al-try-and-run-the-test-e2eb73b2]] - narrower source section: Pointers, copies, et al / Try and run the test
- [[coding-learn-go-with-tests-excerpt-section-pointers-copies-et-al-write-the-minimal-amount-of-code-for-the-test-to-run-and-check-the-failing-80732c5f]] - narrower source section: Pointers, copies, et al / Write the minimal amount of code for the test to run and check the failing test output
- [[coding-learn-go-with-tests-excerpt-section-pointers-copies-et-al-write-enough-code-to-make-it-pass-e62dfd1d]] - narrower source section: Pointers, copies, et al / Write enough code to make it pass
- [[coding-learn-go-with-tests-excerpt-section-using-a-custom-type-3f6de7c1]] - previous source section: Using a custom type
- [[coding-learn-go-with-tests-excerpt-section-note-on-declaring-a-new-error-for-update-a49f3aa6]] - next source section: Note on declaring a new error for Update

## Statements

- An interesting property of maps is that you can modify them without passing as an address to it (e.g &myMap ) _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00605))_
- So when you pass a map to a function/method, you are indeed copying it, but just the pointer part, not the underlying data structure that contains the data. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00608))_
- A gotcha with maps is that they can be a nil value. A nil map behaves like an empty map when reading, but attempts to write to a nil map will cause a runtime panic. You can read more about maps here. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00609))_
- Instead, you can initialize an empty map or use the make keyword to create a map for you: _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00612))_

## Statements by subsection

### Pointers, copies, et al / Refactor

- There isn't much to refactor in our implementation but the test could use a little simplification. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00616))_
- We made variables for word and definition, and moved the definition assertion into its own helper function. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00618))_
- Our Add is looking good. Except, we didn't consider what happens when the value we are trying to add already exists! _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00619))_
- Map will not throw an error if the value already exists. Instead, they will go ahead and overwrite the value with the newly provided value. This can be convenient in practice, but makes our function name less than accurate. Add should not modify existing values. It should only add new words to our dictionary. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00620))_
- Except, we didn't consider what happens when the value we are trying to add already exists! _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00619))_
- It should only add new words to our dictionary. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00620))_

### Pointers, copies, et al / Write the test first

- For this test, we modified Add to return an error, which we are validating against a new error variable, ErrWordExists . We also modified the previous test to check for a nil error. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00623))_

### Pointers, copies, et al / Try to run test

- The compiler will fail because we are not returning a value for Add . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00625))_
- The compiler will fail because we are not returning a value for Add . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00625))_

### Pointers, copies, et al / Write the minimal amount of code for the test to run and check the output

- Now we get two more errors. We are still modifying the value, and returning a nil error. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00629))_

### Pointers, copies, et al / Write enough code to make it pass

- Here we are using a switch statement to match on the error. Having a switch like this provides an extra safety net, in case Search returns an error other than ErrNotFound . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00633))_

### Pointers, copies, et al / Refactor

- We don't have too much to refactor, but as our error usage grows we can make a few modifications. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00635))_
- We made the errors constant; this required us to create our own DictionaryErr type which implements the error interface. You can read more about the details in this excellent article by Dave Cheney. Simply put, it makes the errors more reusable and immutable. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00637))_

### Pointers, copies, et al / Write the test first

- Update is very closely related to Add and will be our next implementation. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00642))_

### Pointers, copies, et al / Write minimal amount of code for the test to run and check the failing test output

- We already know how to deal with an error like this. We need to define our function. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00646))_
- With that in place, we are able to see that we need to change the definition of the word. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00648))_

### Pointers, copies, et al / Write enough code to make it pass

- We already saw how to do this when we fixed the issue with Add . So let's implement something really similar to Add . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00651))_
- There is no refactoring we need to do on this since it was a simple change. However, we now have the same issue as with Add . If we pass in a new word, Update will add it to the dictionary. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00653))_

### Pointers, copies, et al / Write the test first

- We added yet another error type for when the word does not exist. We also modified Update to return an error value. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00657))_

### Pointers, copies, et al / Write the minimal amount of code for the test to run and check the failing test output

- We added our own error type and are returning a nil error. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00663))_

### Pointers, copies, et al / Write enough code to make it pass

- This function looks almost identical to Add except we switched when we update the dictionary and when we return an error. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00669))_
- This function looks almost identical to Add except we switched when we update the dictionary and when we return an error. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00669))_
