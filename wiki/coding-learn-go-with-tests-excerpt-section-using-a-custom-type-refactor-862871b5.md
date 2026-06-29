---
page_id: coding-learn-go-with-tests-excerpt-section-using-a-custom-type-refactor-862871b5
page_kind: source
summary: Using a custom type / Refactor: 3 source-backed entries and 2 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-29
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-using-a-custom-type-refactor-862871b5@e6ded9b650eb55f85bea26cc8eb2f357
---

# Using a custom type / Refactor

From [[coding-learn-go-with-tests-excerpt]].

## Related pages

- [[coding-learn-go-with-tests-excerpt-section-using-a-custom-type-3f6de7c1]] - broader source section: Using a custom type
- [[coding-learn-go-with-tests-excerpt-section-using-a-custom-type-write-enough-code-to-make-it-pass-0fbec14c]] - previous source section: Using a custom type / Write enough code to make it pass
- [[coding-learn-go-with-tests-excerpt-section-using-a-custom-type-write-the-test-first-d5397d92]] - next source section: Using a custom type / Write the test first
- [[coding-learn-go-with-tests-excerpt-refactor]] - topic hub: opens the topic page for Refactor

## Statements

- By creating a new helper we were able to simplify our test, and start using our ErrNotFound variable so our test doesn't fail if we change the error text in the future. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00594))_

## Technical atoms

### Technical frame 1: Using a custom type / Refactor

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00594))_

> By creating a new helper we were able to simplify our test, and start using our ErrNotFound variable so our test doesn't fail if we change the error text in the future.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00592))_

```
var ErrNotFound = errors.New("could not find the word you were 
looking for")
func (d Dictionary) Search(word string) (string, error) {
    definition, ok := d[word]
    if !ok {
        return "", ErrNotFound
    }
return definition, nil
}
We can get rid of the magic error in our Search function by extracting
it into a variable. This will also allow us to have a better test.
t.Run("unknown word", func(t *testing.T) {
    _, got := dictionary.Search("unknown")
    if got == nil {
        t.Fatal("expected to get an error.")
    }
    assertError(t, got, ErrNotFound)
```

### Technical frame 2: Using a custom type / Refactor

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00594))_

> By creating a new helper we were able to simplify our test, and start using our ErrNotFound variable so our test doesn't fail if we change the error text in the future.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00593))_

```
})
func assertError(t testing.TB, got, want error) {
    t.Helper()
if got != want {
        t.Errorf("got error %q want %q", got, want)
    }
}
```
