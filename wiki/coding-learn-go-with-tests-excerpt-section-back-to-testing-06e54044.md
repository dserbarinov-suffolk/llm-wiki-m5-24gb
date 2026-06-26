---
page_id: coding-learn-go-with-tests-excerpt-section-back-to-testing-06e54044
page_kind: source
summary: Back to Testing: 10 source-backed entries and 2 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-back-to-testing-06e54044@978f02a21cea7b18bbe80d28bb7505e6
---

# Back to Testing

From [[coding-learn-go-with-tests-excerpt]].

## Statements

- Notice how you have not had to pick between multiple testing frameworks and then figure out how to install them. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00032))_
- Notice how you have not had to pick between multiple testing frameworks and then figure out how to install them. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00032))_
- Writing tests Writing a test is just like writing a function, with a few rules It needs to be in a file with a name like xxx_test.go The test function must start with the word Test The test function takes one argument only t *testing.T To use the *testing.T type, you need to import "testing" , like we did with fmt in the other file For now, it's enough to know that your t of type *testing.T is your "hook" into the testing framework so you can do things like t.Fail() when you want to fail. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00033))_
- of the code you will write. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00033))_
- Writing tests Writing a test is just like writing a function, with a few rules It needs to be in a file with a name like xxx_test.go The test function must start with the word Test The test function takes one argument only t *testing.T To use the *testing.T type, you need to import "testing" , like we did with fmt in the other file For now, it's enough to know that your t of type *testing.T is your "hook" into the testing framework so you can do things like t.Fail() when you want to fail. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00033))_
- When you make the test fail, it should be clear how it works. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00034))_
- The f stands for format, which allows us to build a string with values inserted into the placeholder values %q . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00034))_
- For tests, %q is very useful as it wraps your values in double quotes. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00034))_

## Technical atoms

> It should've passed!
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00032))_

> You can read more about the placeholder strings in the fmt documentation.
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00034))_
