---
page_id: coding-learn-go-with-tests-excerpt-section-hello-world-back-to-testing-7ab34920
page_kind: source
summary: Hello, World / Back to Testing: 9 source-backed entries and 0 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-29
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-hello-world-back-to-testing-7ab34920@c99bd5a35b59e4e8628daed0c27f0c0b
---

# Hello, World / Back to Testing

From [[coding-learn-go-with-tests-excerpt]].

## Related pages

- [[coding-learn-go-with-tests-excerpt-section-hello-world-72ad81c1]] - broader source section: Hello, World
- [[coding-learn-go-with-tests-excerpt-section-hello-world-go-modules-3cb7c993]] - previous source section: Hello, World / Go modules?

## Statements

- Run go test in your terminal. It should've passed! Just to check, try deliberately breaking the test by changing the want string. Notice how you have not had to pick between multiple testing frameworks and then figure out how to install them. Everything you need is built into the language, and the syntax is the same as the rest _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00032))_
- of the code you will write. Writing tests Writing a test is just like writing a function, with a few rules It needs to be in a file with a name like xxx_test.go The test function must start with the word Test The test function takes one argument only t *testing.T To use the *testing.T type, you need to import "testing" , like we did with fmt in the other file For now, it's enough to know that your t of type *testing.T is your "hook" into the testing framework so you can do things like t.Fail() when you want to fail. We've covered some new topics: if If statements in Go are very much like other programming languages. Declaring variables We're declaring some variables with the syntax varName := value , which lets us reuse some values in our test for readability. t.Errorf We are calling the method on our , which will print out a _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00033))_
- Errorf t message and fail the test. The f stands for format, which allows us to build a string with values inserted into the placeholder values %q . When you make the test fail, it should be clear how it works. You can read more about the placeholder strings in the fmt documentation. For tests, %q is very useful as it wraps your values in double quotes. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00034))_
- Notice how you have not had to pick between multiple testing frameworks and then figure out how to install them. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00032))_
- Writing tests Writing a test is just like writing a function, with a few rules It needs to be in a file with a name like xxx_test.go The test function must start with the word Test The test function takes one argument only t *testing.T To use the *testing.T type, you need to import "testing" , like we did with fmt in the other file For now, it's enough to know that your t of type *testing.T is your "hook" into the testing framework so you can do things like t.Fail() when you want to fail. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00033))_
