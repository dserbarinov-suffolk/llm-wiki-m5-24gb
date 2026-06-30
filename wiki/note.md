---
page_id: note
page_kind: concept
summary: Canonical concept 'Note': 2 source(s), 11 statement(s), 4 atom(s), 0 relation(s).
sources: raw/coding_learn_go_with_tests_excerpt.pdf, raw/coding_little_go_book.pdf
updated: 2026-06-30
category_path: concepts
projection_coverage: canonical-concept-note@10466653e782b94e735568f2e27397af
---

# Note

Compiled concept page from 2 source(s), 11 statement(s), and 4 technical atom(s).

## Source Evidence

### [[coding-learn-go-with-tests-excerpt]]

Source topic: [[coding-learn-go-with-tests-excerpt-note]]

#### Statements

- Note: Go source files can only have one package per directory. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00165))_
- Also note that we are no longer using the main package, instead we've defined a package named integers , as the name suggests this will group functions for working with integers such as Add . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00171))_
- Note : We have to call the String method to retrieve the final result. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00259))_
- Note that this function expects the elements to be comparable. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00348))_
- It's important to note that while the test has compiled , it has a runtime error . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00382))_

#### Technical atoms

> Context: The standard library provides the strings.Builder stringsBuilder type which minimizes memory copying. It implements a WriteString method which we can use to concatenate strings: Note : We have to call the String method to retrieve the final result.
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00257, source-range-cb73a893-00259))_

```
const repeatCount = 5
func Repeat(character string) string {
    var repeated strings.Builder
    for i := 0; i < repeatCount; i++ {
        repeated.WriteString(character)
    }
    return repeated.String()
}
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00258))_

> Context: From Go 1.21, slices standard package is available, which has slices.Equal function to do a simple shallow compare on slices, where you don't need to worry about the types like the above case. Note that this function expects the elements to be comparable. So, it can't be applied to slices with non-comparable elements like 2D slices.
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00348))_

```
./sum_test.go:26:9: invalid operation: got != want (slice can only 
be compared to nil)
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00346))_


### [[coding-little-go-book]]

Source topic: [[coding-little-go-book-note]]

#### Statements

- Another thing to note is that Go's standard library is well documented. _(coding_little_go_book.pdf (source-range-23d24eb1-00068))_
- Note: The trailing , in the above structure is required. _(coding_little_go_book.pdf (source-range-23d24eb1-00120))_
- Note that we're still passing a copy of goku's value to Super it just so happens that goku's value has become an address. _(coding_little_go_book.pdf (source-range-23d24eb1-00133))_
- (If you're paying attention, you'll note that make and len are overloaded. _(coding_little_go_book.pdf (source-range-23d24eb1-00206))_
- As a final note, Go does have panic and recover functions. _(coding_little_go_book.pdf (source-range-23d24eb1-00350))_
- Note that if the underlying type is not int , the above will result in an error. _(coding_little_go_book.pdf (source-range-23d24eb1-00373))_

#### Technical atoms

> Context: The simplest way to create a value of our structure is: Note: The trailing , in the above structure is required. Without it, the compiler will give an error. You'll appreciate the required consistency, especially if you've used a language or format that enforces the opposite.
_(context: coding_little_go_book.pdf (source-range-23d24eb1-00118, source-range-23d24eb1-00120))_

```
goku := Saiyan{
  Name: "Goku",
  Power: 9000,
}
```
_(source: coding_little_go_book.pdf (source-range-23d24eb1-00119))_

> Context: To convert an interface variable to an explicit type, you use .(TYPE) : Note that if the underlying type is not int , the above will result in an error.
_(context: coding_little_go_book.pdf (source-range-23d24eb1-00371, source-range-23d24eb1-00373))_

```
return a.(int) + b.(int)
```
_(source: coding_little_go_book.pdf (source-range-23d24eb1-00372))_


## Cross-Source Comparison

- No typed cross-source relationships detected yet.
