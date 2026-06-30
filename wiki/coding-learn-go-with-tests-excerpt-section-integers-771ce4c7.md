---
page_id: coding-learn-go-with-tests-excerpt-section-integers-771ce4c7
page_kind: source
summary: Integers: 29 source-backed entries and 1 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
page_family: section-reference
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-30
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-integers-771ce4c7@a56d4ba32044df7a9ffd0d03806a5b73
---

# Integers

From [[coding-learn-go-with-tests-excerpt]].

## Related pages

- [[coding-learn-go-with-tests-excerpt-section-integers-write-the-test-first-7d2f9399]] - narrower source section: Integers / Write the test first
- [[coding-learn-go-with-tests-excerpt-section-integers-try-and-run-the-test-ce54b37e]] - narrower source section: Integers / Try and run the test
- [[coding-learn-go-with-tests-excerpt-section-integers-write-the-minimal-amount-of-code-for-the-test-to-run-and-check-the-failing-test-output-4c223d77]] - narrower source section: Integers / Write the minimal amount of code for the test to run and check the failing test output
- [[coding-learn-go-with-tests-excerpt-section-integers-write-enough-code-to-make-it-pass-edef33e0]] - narrower source section: Integers / Write enough code to make it pass
- [[coding-learn-go-with-tests-excerpt-section-integers-refactor-acc9e7fe]] - narrower source section: Integers / Refactor
- [[coding-learn-go-with-tests-excerpt-section-the-tdd-process-and-why-the-steps-are-important-9302843f]] - previous source section: The TDD process and why the steps are important
- [[coding-learn-go-with-tests-excerpt-section-testable-examples-80b8a2ce]] - next source section: Testable Examples

## Statements

- Integers work as you would expect. Let's write an Add function to try things out. Create a test file called adder_test.go and write this code. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00164))_
- Note: Go source files can only have one package per directory. Make sure that your files are organised into their own packages. Here is a good explanation on this. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00165))_
- Note: Go source files can only have one package per directory. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00165))_

## Statements by subsection

### Integers / Write the test first

- You will notice that we're using %d as our format strings rather than %q . That's because we want it to print an integer rather than a string. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00170))_
- Also note that we are no longer using the main package, instead we've defined a package named integers , as the name suggests this will group functions for working with integers such as Add . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00171))_
- That's because we want it to print an integer rather than a string. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00170))_
- Also note that we are no longer using the main package, instead we've defined a package named integers , as the name suggests this will group functions for working with integers such as Add . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00171))_

### Integers / Write the minimal amount of code for the test to run and check the failing test output

- Now run the tests, and we should be happy that the test is correctly reporting what is wrong. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00178))_
- If you have noticed we learnt about named return value in the last section but aren't using the same here. It should generally be used when the meaning of the result isn't clear from context, in our case it's pretty much clear that Add function will add the parameters. You can refer this wiki for more details. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00180))_

### Integers / Write enough code to make it pass

- In the strictest sense of TDD we should now write the minimal amount of code to make the test pass . A pedantic programmer may do this _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00182))_
- Once we're more familiar with Go's syntax I will introduce a technique called "Property Based Testing" , which would stop annoying developers and help you find bugs. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00186))_

### Integers / Refactor

- There's not a lot in the actual code we can really improve on here. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00191))_
- This is great because it aids the usability of code you are writing. It is preferable that a user can understand the usage of your code by just looking at the type signature and documentation. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00193))_
- This is great because it aids the usability of code you are writing. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00193))_

## Technical atoms

### Technical frame 1: Integers / Write the test first

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00170))_

> You will notice that we're using %d as our format strings rather than %q . That's because we want it to print an integer rather than a string.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00169))_

```
package integers
import "testing"
func TestAdder(t *testing.T) {
    sum := Add(2, 2)
    expected := 4
if sum != expected {
        t.Errorf("expected '%d' but got '%d'", expected, sum)
    }
}
```
