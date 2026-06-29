---
page_id: coding-learn-go-with-tests-excerpt-type
page_kind: concept
summary: Type: 8 statement(s) and 3 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-29
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-type@3d4f82b559889c211a2d76a363e31be2
---

# Type

What [[coding-learn-go-with-tests-excerpt]] covers about type:

## Statements

### one...last...refactor?

- It will be assigned the "zero" value. This depends on the type, for example int s are 0 and for string s it is "" . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00142))_

### What are methods? / Refactor

- We're creating a new type just like we did with Rectangle and Circle but this time it is an interface rather than a struct . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00481))_

### Wait, what?

- In Go interface resolution is implicit . If the type you pass in matches what the interface is asking for, it will compile. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00490))_

### Decoupling / Wrapping up

- Declaring structs to create your own data types which lets you bundle related data together and make the intent of your code clearer _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00538))_

### Maps / Write the test first

- The key type is special. It can only be a comparable type because without the ability to tell if 2 keys are equal, we have no way to ensure that we are getting the correct value. Comparable types are explained in depth in the language spec. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00553))_

- The value type, on the other hand, can be any type you want. It can even be another map. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00554))_

### Using a custom type

- Here we created a Dictionary type which acts as a thin wrapper around map . With the custom type defined, we can create the Search method. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00574))_


## Technical atoms

### Technical frame 1: Maps / Write the test first

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00552))_

> Declaring a Map is somewhat similar to an array. Except, it starts with the map keyword and requires two types. The first is the key type, which is written inside the [] . The second is the value type, which goes right after the [] .

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00551))_

```
In dictionary_test.go
package main
import "testing"
func TestSearch(t *testing.T) {
    dictionary := map[string]string{"test": "this is just a test"}
got := Search(dictionary, "test")
    want := "this is just a test"
if got != want {
        t.Errorf("got %q want %q given, %q", got, want, "test")
    }
}
```

### Technical frame 2: Using a custom type

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00570))_

> We started using the Dictionary type, which we have not defined yet. Then called Search on the Dictionary instance.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00568))_

```
In dictionary_test.go:
func TestSearch(t *testing.T) {
    dictionary := Dictionary{"test": "this is just a test"}
got := dictionary.Search("test")
    want := "this is just a test"
```

### Technical frame 3: Using a custom type

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00570))_

> We started using the Dictionary type, which we have not defined yet. Then called Search on the Dictionary instance.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00569))_

```
assertStrings(t, got, want)
}
```


## Related pages

- [[coding-learn-go-with-tests-excerpt-custom-type]] - narrower topic: Using a custom type shares source evidence from Using a custom type: Here we created a Dictionary type which acts as a thin wrapper around map . With the custom type defined, we can create the Search method.; Using a custom type shares technical record from Using a custom type: In dictionary_test.go: func TestSearch(t *testing.T) { dictionary := Dictionary{"test": "this is just a test"} got := dictionary.Search("test") want := "this is just a test" (1 shared statement(s), 2 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-maps]] - shared statements and technical atoms: Maps shares source evidence from Maps / Write the test first: The key type is special. It can only be a comparable type because without the ability to tell if 2 keys are equal, we have no way to ensure that we are getting the c ... [truncated]; Maps shares technical record from Maps / Write the test first: In dictionary_test.go package main import "testing" func TestSearch(t *testing.T) { dictionary := map[string]string{"test": "this is just a test"} got := Search(dict ... [truncated] (3 shared statement(s), 1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-decoupling]] - shared statements: Decoupling shares source evidence from Decoupling / Wrapping up: Declaring structs to create your own data types which lets you bundle related data together and make the intent of your code clearer (1 shared statement(s))
- [[coding-learn-go-with-tests-excerpt-method]] - shared statements: What are methods? shares source evidence from What are methods? / Refactor: We're creating a new type just like we did with Rectangle and Circle but this time it is an interface rather than a struct . (1 shared statement(s))
- [[coding-learn-go-with-tests-excerpt-refactor]] - shared statements: one...last...refactor? shares source evidence from one...last...refactor?: It will be assigned the "zero" value. This depends on the type, for example int s are 0 and for string s it is "" . (1 shared statement(s))

## Source

- [[coding-learn-go-with-tests-excerpt]]
