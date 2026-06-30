---
page_id: coding-learn-go-with-tests-excerpt-helper
page_kind: concept
summary: Helper: 5 statement(s) and 1 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
page_family: topic-concept
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-30
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-helper@19fef22f9384d994c164a810d2ffd380
---

# Helper

What [[coding-learn-go-with-tests-excerpt]] covers about helper:

## Statements

### Constants / Hello, world... again

- t.Helper() is needed to tell the test suite that this method is a helper. By doing this, when it fails, the line number reported will be in our function call rather than inside our test helper. This will help other developers track down problems more easily. If you still don't understand, comment it out, make a test fail and observe the test output. Comments in Go are a great way to add additional information to your code, or in this case, a quick way to tell the compiler to ignore a line. You can comment out the t.Helper() code by adding two forward slashes // at the beginning of the line. You should see that line turn grey or change to another color than the rest of your code to indicate it's now commented out. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00088))_

### Decoupling

- Notice how our helper does not need to concern itself with whether the shape is a Rectangle or a Circle or a Triangle . By declaring an interface, the helper is decoupled from the concrete types and only has the method it needs to do its job. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00492))_

### Decoupling / Wrapping up

- Interfaces are a great tool for hiding complexity away from other parts of the system. In our case our test helper code did not need to know the exact shape it was asserting on, only how to "ask" for its area. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00543))_

### Using a custom type / Refactor

- By creating a new helper we were able to simplify our test, and start using our ErrNotFound variable so our test doesn't fail if we change the error text in the future. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00594))_


## Technical atoms

### Technical frame 1: Constants / Hello, world... again

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00088))_

> t.Helper() is needed to tell the test suite that this method is a helper. By doing this, when it fails, the line number reported will be in our function call rather than inside our test helper. This will help other developers track down problems more easily. If you still don't understand, comment it out, make a test fail and observe the test output. Comments in Go are a great way to add additional information to your code, or in this case, a quick way to tell the compiler to ignore a line. You c

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00087))_

> For helper functions, it's a good idea to accept a testing.TB which is an interface that *testing.T and *testing.B both satisfy, so you can call helper functions from a test, or a benchmark (don't worry if words like "interface" mean nothing to you right now, it will be covered later).


## Related pages

- [[coding-learn-go-with-tests-excerpt-test]] - shared statements and technical atoms: Test shares source evidence from Decoupling / Wrapping up: Interfaces are a great tool for hiding complexity away from other parts of the system. In our case our test helper code did not need to know the exact shape it was a ... [truncated]; Test shares technical record from Constants / Hello, world... again: For helper functions, it's a good idea to accept a testing.TB which is an interface that *testing.T and *testing.B both satisfy, so you can call helper functions fro ... [truncated] (1 shared statement(s), 1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-comment]] - shared technical atoms: Comment shares technical record from Constants / Hello, world... again: For helper functions, it's a good idea to accept a testing.TB which is an interface that *testing.T and *testing.B both satisfy, so you can call helper functions fro ... [truncated] (1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-code]] - shared statements: Code shares source evidence from Decoupling / Wrapping up: Interfaces are a great tool for hiding complexity away from other parts of the system. In our case our test helper code did not need to know the exact shape it was a ... [truncated] (1 shared statement(s))
- [[coding-learn-go-with-tests-excerpt-interface]] - shared statements: Interface shares source evidence from Decoupling: Notice how our helper does not need to concern itself with whether the shape is a Rectangle or a Circle or a Triangle . By declaring an interface, the helper is deco ... [truncated] (1 shared statement(s))

## Source

- [[coding-learn-go-with-tests-excerpt]]
