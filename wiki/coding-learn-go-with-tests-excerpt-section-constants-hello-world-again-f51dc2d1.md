---
page_id: coding-learn-go-with-tests-excerpt-section-constants-hello-world-again-f51dc2d1
page_kind: source
summary: Constants / Hello, world... again: 26 source-backed entries and 0 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
page_family: section-reference
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-30
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-constants-hello-world-again-f51dc2d1@adde285816825f15a970c76bb572955b
---

# Constants / Hello, world... again

From [[coding-learn-go-with-tests-excerpt]].

## Related pages

- [[coding-learn-go-with-tests-excerpt-section-constants-374a85cb]] - broader source section: Constants

## Statements

- The next requirement is when our function is called with an empty string it defaults to printing "Hello, World", rather than "Hello, ". _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00072))_
- Here, we are introducing another tool in our testing arsenal: subtests. Sometimes, it is useful to group tests around a "thing" and then have subtests describing different scenarios. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00075))_
- A benefit of this approach is you can set up shared code that can be used in the other tests. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00076))_
- If we run our tests we should see it satisfies the new requirement and we haven't accidentally broken the other functionality. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00080))_
- It is important that your tests are clear specifications of what the code needs to do. But there is repeated code when we check if the message is what we expect. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00081))_
- Refactoring is not just for the production code! _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00082))_
- Now that the tests are passing, we can and should refactor our tests. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00083))_
- We've refactored our assertion into a new function. This reduces duplication and improves the readability of our tests. We need to pass in t *testing.T so that we can tell the test code to fail when we need to. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00086))_
- t.Helper() is needed to tell the test suite that this method is a helper. By doing this, when it fails, the line number reported will be in our function call rather than inside our test helper. This will help other developers track down problems more easily. If you still don't understand, comment it out, make a test fail and observe the test output. Comments in Go are a great way to add additional information to your code, or in this case, a quick way to tell the compiler to ignore a line. You can comment out the t.Helper() code by adding two forward slashes // at the beginning of the line. You should see that line turn grey or change to another color than the rest of your code to indicate it's now commented out. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00088))_
- The next requirement is when our function is called with an empty string it defaults to printing "Hello, World", rather than "Hello, ". _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00072))_
- Sometimes, it is useful to group tests around a "thing" and then have subtests describing different scenarios. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00075))_
- By doing this, when it fails, the line number reported will be in our function call rather than inside our test helper. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00088))_
