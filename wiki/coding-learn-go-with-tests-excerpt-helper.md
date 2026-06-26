---
page_id: coding-learn-go-with-tests-excerpt-helper
page_kind: concept
summary: Helper: 5 statement(s) and 1 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-helper@d442d26bd9bcb043683d1f165d39ebc4
---

# Helper

What [[coding-learn-go-with-tests-excerpt]] covers about helper:

## Statements

- t.Helper() is needed to tell the test suite that this method is a helper. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00088))_
- Notice how our helper does not need to concern itself with whether the shape is a Rectangle or a Circle or a Triangle . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00492))_
- By declaring an interface, the helper is decoupled from the concrete types and only has the method it needs to do its job. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00492))_
- In our case our test helper code did not need to know the exact shape it was asserting on, only how to "ask" for its area. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00543))_
- By creating a new helper we were able to simplify our test, and start using our ErrNotFound variable so our test doesn't fail if we change the error text in the future. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00594))_

## Technical atoms

> Context: We've refactored our assertion into a new function. This reduces duplication and improves the readability of our tests. We need to pass in t *testing.T so that we can tell the test code to fail when we need to. t.Helper() is needed to tell the test suite that this method is a helper. By doing this, when it fails, the line number reported will be in our function call rather than inside our test helper. This will help other developers track down problems more easily. If you still don't understand, comment it out, make a test fail and observe the test output. Comments in Go are a great way to add additional information to your code, or in this case, a quick way to tell the compiler to ignore a line. You can comment out the t.Helper() code by adding two forward slashes // at the beginning of the line. You should see that line turn grey or change to another color than the rest of your code to indicate it's now commented out.
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00086, source-range-559be4b1-00088))_

> For helper functions, it's a good idea to accept a testing.TB which is an interface that *testing.T and *testing.B both satisfy, so you can call helper functions from a test, or a benchmark (don't worry if words like "interface" mean nothing to you right now, it will be covered later).
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00087))_


## Source

- [[coding-learn-go-with-tests-excerpt]]
