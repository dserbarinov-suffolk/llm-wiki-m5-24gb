---
page_id: coding-learn-go-with-tests-excerpt-section-structs-methods-interfaces-82e8585b
page_kind: source
summary: Structs, methods & interfaces: 28 source-backed entries and 0 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
page_family: section-reference
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-30
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-structs-methods-interfaces-82e8585b@a5dfe2cd382f3eb01a2ad797d1cef861
---

# Structs, methods & interfaces

From [[coding-learn-go-with-tests-excerpt]].

## Related pages

- [[coding-learn-go-with-tests-excerpt-section-structs-methods-interfaces-write-the-test-first-cbb1567f]] - narrower source section: Structs, methods & interfaces / Write the test first
- [[coding-learn-go-with-tests-excerpt-section-structs-methods-interfaces-try-to-run-the-test-45f95e1a]] - narrower source section: Structs, methods & interfaces / Try to run the test
- [[coding-learn-go-with-tests-excerpt-section-structs-methods-interfaces-write-the-minimal-amount-of-code-for-the-test-to-run-and-check-the-fa-e190e01d]] - narrower source section: Structs, methods & interfaces / Write the minimal amount of code for the test to run and check the failing test output
- [[coding-learn-go-with-tests-excerpt-section-structs-methods-interfaces-write-enough-code-to-make-it-pass-075da993]] - narrower source section: Structs, methods & interfaces / Write enough code to make it pass
- [[coding-learn-go-with-tests-excerpt-section-structs-methods-interfaces-refactor-d4181327]] - narrower source section: Structs, methods & interfaces / Refactor
- [[coding-learn-go-with-tests-excerpt-section-structs-methods-interfaces-write-the-test-first-5ffd50f2]] - narrower source section: Structs, methods & interfaces / Write the test first
- [[coding-learn-go-with-tests-excerpt-section-structs-methods-interfaces-try-to-run-the-test-fadb70be]] - narrower source section: Structs, methods & interfaces / Try to run the test
- [[coding-learn-go-with-tests-excerpt-section-structs-methods-interfaces-write-the-minimal-amount-of-code-for-the-test-to-run-and-check-the-fa-44e30158]] - narrower source section: Structs, methods & interfaces / Write the minimal amount of code for the test to run and check the failing test output
- [[coding-learn-go-with-tests-excerpt-section-arrays-and-their-type-0c35221e]] - previous source section: Arrays and their type
- [[coding-learn-go-with-tests-excerpt-section-what-are-methods-997bc0f7]] - next source section: What are methods?

## Statements

- Suppose that we need some geometry code to calculate the perimeter of a rectangle given a height and width. We can write a Perimeter(width float64, height float64) function, where float64 is for floating-point numbers like 123.45 . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00410))_

## Statements by subsection

### Structs, methods & interfaces / Write the test first

- Notice the new format string? The f is for our float64 and the .2 means print 2 decimal places. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00414))_
- The f is for our float64 and the .2 means print 2 decimal places. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00414))_

### Structs, methods & interfaces / Write enough code to make it pass

- Try to do it yourself, following the TDD cycle. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00422))_

### Structs, methods & interfaces / Refactor

- Our code does the job, but it doesn't contain anything explicit about rectangles. An unwary developer might try to supply the width and height of a triangle to these functions without realising they will return the wrong answer. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00426))_
- We could just give the functions more specific names like RectangleArea . A neater solution is to define our own type called Rectangle which encapsulates this concept for us. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00427))_
- We can create a simple type using a struct . A struct is just a named collection of fields where you can store data. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00428))_
- Our next requirement is to write an Area function for circles. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00435))_

### Structs, methods & interfaces / Write the minimal amount of code for the test to run and check the failing test output

- You can have functions with the same name declared in different packages . So we could create our Area(Circle) in a new package, but that feels overkill here. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00445))_
- We can define methods on our newly defined types instead. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00446))_
