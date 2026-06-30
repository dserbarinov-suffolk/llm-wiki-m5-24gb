---
page_id: coding-learn-go-with-tests-excerpt-write-test
page_kind: concept
summary: Write the test first: 35 statement(s) and 26 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
page_family: broad-topic
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-30
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-write-test@98e7b43a2f565e976ae8fb47556bead3
---

# Write the test first

What [[coding-learn-go-with-tests-excerpt]] covers about write the test first:

## Statements

### Hello, YOU

- In the last example, we wrote the test after the code had been written so that you could get an example of how to write a test and declare a function. From this point on, we will be writing tests first . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00044))_

### French / switch

- Write a test to now include a greeting in the language of your choice and you should see how simple it is to extend our amazing function. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00133))_

### The TDD process and why the steps are important

- Write a failing test and see it fail so we know we have written a relevant test for our requirements and seen that it produces an easy to understand description of the failure _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00157))_

### Integers

- Integers work as you would expect. Let's write an Add function to try things out. Create a test file called adder_test.go and write this code. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00164))_

### Integers / Write the test first

- You will notice that we're using %d as our format strings rather than %q . That's because we want it to print an integer rather than a string. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00170))_

- Also note that we are no longer using the main package, instead we've defined a package named integers , as the name suggests this will group functions for working with integers such as Add . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00171))_

### Integers / Write enough code to make it pass

- In the strictest sense of TDD we should now write the minimal amount of code to make the test pass . A pedantic programmer may do this _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00182))_

### Arrays and slices / Write the test first

- Arrays have a fi xed capacity which you define when you declare the variable. We can initialize an array in two ways: _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00282))_

- It is sometimes useful to also print the inputs to the function in the error message. Here, we are using the %v placeholder to print the "default" format, which works well for arrays. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00285))_

### Structs, methods & interfaces / Write the test first

- Notice the new format string? The f is for our float64 and the .2 means print 2 decimal places. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00414))_

### Decoupling / Write the test first

- Adding a new test for our new shape is very easy. Just add {Triangle{12, 6}, 36.0}, to our list. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00504))_

### Maps / Write the test first

- Declaring a Map is somewhat similar to an array. Except, it starts with the map keyword and requires two types. The first is the key type, which is written inside the [] . The second is the value type, which goes right after the [] . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00552))_

- The key type is special. It can only be a comparable type because without the ability to tell if 2 keys are equal, we have no way to ensure that we are getting the correct value. Comparable types are explained in depth in the language spec. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00553))_

- The value type, on the other hand, can be any type you want. It can even be another map. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00554))_

### Using a custom type / Write the test first

- We actually get nothing back. This is good because the program can continue to run, but there is a better approach. The function can report that the word is not in the dictionary. This way, the user isn't left wondering if the word doesn't exist or if there is just no definition (this might not seem very useful for a dictionary. However, it's a scenario that could be key in other usecases). _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00577))_

- The way to handle this scenario in Go is to return a second argument which is an Error type. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00579))_

- Notice that as we've seen in the pointers and error section here in order to assert the error message we first check that the error is not nil and then use .Error() method to get the string which we can then pass to the assertion. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00580))_

### Pointers, copies, et al / Write the test first

- For this test, we modified Add to return an error, which we are validating against a new error variable, ErrWordExists . We also modified the previous test to check for a nil error. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00623))_

- Update is very closely related to Add and will be our next implementation. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00642))_

- We added yet another error type for when the word does not exist. We also modified Update to return an error value. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00657))_

### Note on declaring a new error for Update / Write the test first

- Our test creates a Dictionary with a word and then checks if the word has been removed. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00677))_

- Everything else in this test should be familiar. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00555))_
- However, we have no way to add new words to our dictionary. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00596))_
- We have a great way to search the dictionary. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00596))_
- In this test, we are utilizing our Search function to make the validation of the dictionary a little easier. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00598))_

## Technical atoms

### Technical frame 1: Learn Go with Tests (Excerpt)

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00002))_

> Learn Go with Tests -- Go Fundamentals (Excerpt) Hello, World How it works How to test Go modules? Back to Testing Writing tests Go's documentation Hello, YOU A note on source control Constants Hello, world... again Back to source control Discipline Keep going! More requirements French switch one...last...refactor? Wrapping up Some of Go's syntax around The TDD process and why the steps are important Integers Write the test first Try and run the test Write the minimal amount of code for the test

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00003))_

```
output
Write enough code to make it pass
Refactor
Write the test ﬁrst
Try and run the test
Write minimal amount of code for the test to run and check the
failing test output
Write enough code to make it pass
Write the test ﬁrst
Try and run the test
Write the minimal amount of code for the test to run and check the
failing test output
Write enough code to make it pass
Note on declaring a new error for Update
Write the test ﬁrst
Try to run the test
Write the minimal amount of code for the test to run and check the
failing test output
Write enough code to make it pass
Refactor
Try to run test
Write enough code to make it pass
Wrapping up
```

### Technical frame 2: Integers / Write the test first

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

### Technical frame 3: Iteration / Write the test first

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00222))_

```
package iteration
import "testing"
func TestRepeat(t *testing.T) {
    repeated := Repeat("a")
    expected := "aaaaa"
if repeated != expected {
        t.Errorf("expected %q but got %q", expected, repeated)
    }
}
```

### Technical frame 4: Arrays and slices / Write the test first

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00282))_

> Arrays have a fi xed capacity which you define when you declare the variable. We can initialize an array in two ways:

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00281))_

```
package main
import "testing"
func TestSum(t *testing.T) {
numbers := [5]int{1, 2, 3, 4, 5}
got := Sum(numbers)
    want := 15
if got != want {
        t.Errorf("got %d want %d given, %v", got, want, numbers)
    }
}
```

### Technical frame 5: Arrays and slices / Write the test first

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00285))_

> It is sometimes useful to also print the inputs to the function in the error message. Here, we are using the %v placeholder to print the "default" format, which works well for arrays.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00283))_

```
[N]type{value1, value2, ..., valueN} e.g. numbers := [5]int{1, 2, 
3, 4, 5}
[...]type{value1, value2, ..., valueN} e.g. numbers := [...]int{1, 2,
```

### Technical frame 6: Arrays and their type / Write the test first

**Atoms:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00309, source-range-cb73a893-00311))_

> mySlice := []int{1,2,3}

> myArray := [3]int{1,2,3}

### Technical frame 7: Arrays and their type / Write the test first

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00312))_

```
func TestSum(t *testing.T) {
t.Run("collection of 5 numbers", func(t *testing.T) {
        numbers := [5]int{1, 2, 3, 4, 5}
got := Sum(numbers)
        want := 15
if got != want {
            t.Errorf("got %d want %d given, %v", got, want, numbers)
        }
    })
t.Run("collection of any size", func(t *testing.T) {
        numbers := []int{1, 2, 3}
got := Sum(numbers)
        want := 6
if got != want {
            t.Errorf("got %d want %d given, %v", got, want, numbers)
        }
    })
}
```

### Technical frame 8: Arrays and their type / Write the test first

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00338))_

```
func TestSumAll(t *testing.T) {
got := SumAll([]int{1, 2}, []int{0, 9})
    want := []int{3, 9}
if got != want {
        t.Errorf("got %v want %v", got, want)
    }
}
```

### Technical frame 9: Arrays and their type / Write the test first

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00367))_

```
func TestSumAllTails(t *testing.T) {
    got := SumAllTails([]int{1, 2}, []int{0, 9})
    want := []int{2, 9}
if !reflect.DeepEqual(got, want) {
        t.Errorf("got %v want %v", got, want)
    }
}
```

### Technical frame 10: Arrays and their type / Write the test first

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00379))_

```
func TestSumAllTails(t *testing.T) {
t.Run("make the sums of some slices", func(t *testing.T) {
        got := SumAllTails([]int{1, 2}, []int{0, 9})
        want := []int{2, 9}
if !reflect.DeepEqual(got, want) {
            t.Errorf("got %v want %v", got, want)
        }
    })
t.Run("safely sum empty slices", func(t *testing.T) {
        got := SumAllTails([]int{}, []int{3, 4, 5})
        want := []int{0, 9}
if !reflect.DeepEqual(got, want) {
            t.Errorf("got %v want %v", got, want)
        }
    })
}
```

### Technical frame 11: Structs, methods & interfaces / Write the test first

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00414))_

> Notice the new format string? The f is for our float64 and the .2 means print 2 decimal places.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00413))_

```
func TestPerimeter(t *testing.T) {
    got := Perimeter(10.0, 10.0)
    want := 40.0
if got != want {
        t.Errorf("got %.2f want %.2f", got, want)
    }
}
```

### Technical frame 12: Structs, methods & interfaces / Write the test first

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00437))_

```
func TestArea(t *testing.T) {
t.Run("rectangles", func(t *testing.T) {
        rectangle := Rectangle{12, 6}
        got := Area(rectangle)
        want := 72.0
if got != want {
            t.Errorf("got %g want %g", got, want)
        }
    })
t.Run("circles", func(t *testing.T) {
        circle := Circle{10}
        got := Area(circle)
        want := 314.1592653589793
```

### Technical frame 13: Structs, methods & interfaces / Write the test first

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00438))_

```
if got != want {
            t.Errorf("got %g want %g", got, want)
        }
    })
}
```

### Technical frame 14: Decoupling / Write the test first

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00504))_

> Adding a new test for our new shape is very easy. Just add {Triangle{12, 6}, 36.0}, to our list.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00505))_

```
func TestArea(t *testing.T) {
areaTests := []struct {
        shape Shape
        want  float64
```

### Technical frame 15: Decoupling / Write the test first

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00504))_

> Adding a new test for our new shape is very easy. Just add {Triangle{12, 6}, 36.0}, to our list.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00506))_

```
}{
        {Rectangle{12, 6}, 72.0},
        {Circle{10}, 314.1592653589793},
        {Triangle{12, 6}, 36.0},
    }
for _, tt := range areaTests {
        got := tt.shape.Area()
        if got != tt.want {
            t.Errorf("got %g want %g", got, tt.want)
        }
    }
}
```

### Technical frame 16: Maps / Write the test first

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

### Technical frame 17: Maps / Write the test first

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00554))_

> The value type, on the other hand, can be any type you want. It can even be another map.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00553))_

> It can only be a comparable type because without the ability to tell if 2 keys are equal, we have no way to ensure that we are getting the correct value.

### Technical frame 18: Using a custom type / Write the test first

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00579))_

> The way to handle this scenario in Go is to return a second argument which is an Error type.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00578))_

```
func TestSearch(t *testing.T) {
    dictionary := Dictionary{"test": "this is just a test"}
t.Run("known word", func(t *testing.T) {
        got, _ := dictionary.Search("test")
        want := "this is just a test"
assertStrings(t, got, want)
    })
t.Run("unknown word", func(t *testing.T) {
        _, err := dictionary.Search("unknown")
        want := "could not find the word you were looking for"
if err == nil {
            t.Fatal("expected to get an error.")
        }
assertStrings(t, err.Error(), want)
    })
}
```

### Technical frame 19: Using a custom type / Write the test first

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00598))_

> In this test, we are utilizing our Search function to make the validation of the dictionary a little easier.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00597))_

```
func TestAdd(t *testing.T) {
    dictionary := Dictionary{}
    dictionary.Add("test", "this is just a test")
want := "this is just a test"
    got, err := dictionary.Search("test")
    if err != nil {
        t.Fatal("should find added word:", err)
    }
assertStrings(t, got, want)
}
```

### Technical frame 20: Pointers, copies, et al / Write the test first

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00623))_

> For this test, we modified Add to return an error, which we are validating against a new error variable, ErrWordExists . We also modified the previous test to check for a nil error.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00622))_

```
func TestAdd(t *testing.T) {
    t.Run("new word", func(t *testing.T) {
        dictionary := Dictionary{}
        word := "test"
        definition := "this is just a test"
err := dictionary.Add(word, definition)
assertError(t, err, nil)
        assertDefinition(t, dictionary, word, definition)
    })
t.Run("existing word", func(t *testing.T) {
        word := "test"
        definition := "this is just a test"
        dictionary := Dictionary{word: definition}
        err := dictionary.Add(word, "new test")
assertError(t, err, ErrWordExists)
        assertDefinition(t, dictionary, word, definition)
    })
}
```

### Technical frame 21: Pointers, copies, et al / Write the test first

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00642))_

> Update is very closely related to Add and will be our next implementation.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00640))_

```
func TestUpdate(t *testing.T) {
    word := "test"
    definition := "this is just a test"
    dictionary := Dictionary{word: definition}
    newDefinition := "new definition"
```

### Technical frame 22: Pointers, copies, et al / Write the test first

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00642))_

> Update is very closely related to Add and will be our next implementation.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00641))_

```
dictionary.Update(word, newDefinition)
assertDefinition(t, dictionary, word, newDefinition)
}
```

### Technical frame 23: Pointers, copies, et al / Write the test first

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00657))_

> We added yet another error type for when the word does not exist. We also modified Update to return an error value.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00655))_

```
t.Run("existing word", func(t *testing.T) {
    word := "test"
    definition := "this is just a test"
    dictionary := Dictionary{word: definition}
    newDefinition := "new definition"
err := dictionary.Update(word, newDefinition)
assertError(t, err, nil)
    assertDefinition(t, dictionary, word, newDefinition)
})
t.Run("new word", func(t *testing.T) {
    word := "test"
    definition := "this is just a test"
    dictionary := Dictionary{}
```

### Technical frame 24: Pointers, copies, et al / Write the test first

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00657))_

> We added yet another error type for when the word does not exist. We also modified Update to return an error value.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00656))_

```
err := dictionary.Update(word, definition)
assertError(t, err, ErrWordDoesNotExist)
})
```

### Technical frame 25: Note on declaring a new error for Update / Write the test first

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00677))_

> Our test creates a Dictionary with a word and then checks if the word has been removed.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00676))_

```
func TestDelete(t *testing.T) {
    word := "test"
    dictionary := Dictionary{word: "test definition"}
dictionary.Delete(word)
_, err := dictionary.Search(word)
    assertError(t, err, ErrNotFound)
}
```


## Related pages

- [[coding-learn-go-with-tests-excerpt-test]] - broader topic: Test shares source evidence from Hello, YOU: In the last example, we wrote the test after the code had been written so that you could get an example of how to write a test and declare a function. From this poin ... [truncated]; Test shares technical record from Learn Go with Tests (Excerpt): func TestArea(t *testing.T) { areaTests := []struct { shape Shape want  float64 (9 shared statement(s), 3 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-write]] - broader topic: Write shares source evidence from French / switch: Write a test to now include a greeting in the language of your choice and you should see how simple it is to extend our amazing function.; Write shares technical record from Learn Go with Tests (Excerpt): output Write enough code to make it pass Refactor Write the test ﬁrst Try and run the test Write minimal amount of code for the test to run and check the failing tes ... [truncated] (2 shared statement(s), 1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-array]] - shared statements and technical atoms: Array shares source evidence from Arrays and slices / Write the test first: Arrays have a fi xed capacity which you define when you declare the variable. We can initialize an array in two ways:; Array shares technical record from Arrays and slices / Write the test first: [N]type{value1, value2, ..., valueN} e.g. numbers := [5]int{1, 2, 3, 4, 5} [...]type{value1, value2, ..., valueN} e.g. numbers := [...]int{1, 2, (2 shared statement(s), 3 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-type]] - shared statements and technical atoms: Type shares source evidence from Maps / Write the test first: The key type is special. It can only be a comparable type because without the ability to tell if 2 keys are equal, we have no way to ensure that we are getting the c ... [truncated]; Type shares technical record from Maps / Write the test first: In dictionary_test.go package main import "testing" func TestSearch(t *testing.T) { dictionary := map[string]string{"test": "this is just a test"} got := Search(dict ... [truncated] (3 shared statement(s), 1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-write-code-pass]] - shared statements and technical atoms: Write enough code to make it pass shares source evidence from Hello, YOU: In the last example, we wrote the test after the code had been written so that you could get an example of how to write a test and declare a function. From this poin ... [truncated]; Write enough code to make it pass shares technical record from Learn Go with Tests (Excerpt): output Write enough code to make it pass Refactor Write the test ﬁrst Try and run the test Write minimal amount of code for the test to run and check the failing tes ... [truncated] (3 shared statement(s), 1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-code]] - shared statements and technical atoms: Code shares source evidence from Hello, YOU: In the last example, we wrote the test after the code had been written so that you could get an example of how to write a test and declare a function. From this poin ... [truncated]; Code shares technical record from Learn Go with Tests (Excerpt): output Write enough code to make it pass Refactor Write the test ﬁrst Try and run the test Write minimal amount of code for the test to run and check the failing tes ... [truncated] (1 shared statement(s), 1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-try-run-test]] - shared technical atoms: Try and run the test shares technical record from Learn Go with Tests (Excerpt): output Write enough code to make it pass Refactor Write the test ﬁrst Try and run the test Write minimal amount of code for the test to run and check the failing tes ... [truncated] (1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-error]] - shared statements: Error shares source evidence from Using a custom type / Write the test first: Notice that as we've seen in the pointers and error section here in order to assert the error message we first check that the error is not nil and then use .Error() ... [truncated] (1 shared statement(s))
- [[coding-learn-go-with-tests-excerpt-note]] - shared statements: Note shares source evidence from Integers / Write the test first: Also note that we are no longer using the main package, instead we've defined a package named integers , as the name suggests this will group functions for working w ... [truncated] (1 shared statement(s))
- [[coding-learn-go-with-tests-excerpt-section-integers-write-the-test-first-7d2f9399]] - source section: Integers / Write the test first shares source evidence from Integers / Write the test first: You will notice that we're using %d as our format strings rather than %q . That's because we want it to print an integer rather than a string.; Integers / Write the test first shares technical record from Integers / Write the test first: package integers import "testing" func TestAdder(t *testing.T) { sum := Add(2, 2) expected := 4 if sum != expected { t.Errorf("expected '%d' but got '%d'", expected, sum) } } (2 shared statement(s), 1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-section-iteration-write-the-test-first-ac988ca6]] - source section: Iteration / Write the test first shares technical record from Iteration / Write the test first: package iteration import "testing" func TestRepeat(t *testing.T) { repeated := Repeat("a") expected := "aaaaa" if repeated != expected { t.Errorf("expected %q but go ... [truncated] (1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-section-arrays-and-slices-write-the-test-first-0df2234d]] - source section: Arrays and slices / Write the test first shares source evidence from Arrays and slices / Write the test first: Arrays have a fi xed capacity which you define when you declare the variable. We can initialize an array in two ways:; Arrays and slices / Write the test first shares technical record from Arrays and slices / Write the test first: package main import "testing" func TestSum(t *testing.T) { numbers := [5]int{1, 2, 3, 4, 5} got := Sum(numbers) want := 15 if got != want { t.Errorf("got %d want %d ... [truncated] (3 shared statement(s), 2 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-section-arrays-and-their-type-write-the-test-first-73b871d4]] - source section: Arrays and their type / Write the test first shares technical record from Arrays and their type / Write the test first: mySlice := []int{1,2,3} (3 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-section-arrays-and-their-type-write-the-test-first-08e30bdd]] - source section: Arrays and their type / Write the test first shares technical record from Arrays and their type / Write the test first: func TestSumAll(t *testing.T) { got := SumAll([]int{1, 2}, []int{0, 9}) want := []int{3, 9} if got != want { t.Errorf("got %v want %v", got, want) } } (1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-section-arrays-and-their-type-write-the-test-first-6cd5dd08]] - source section: Arrays and their type / Write the test first shares technical record from Arrays and their type / Write the test first: func TestSumAllTails(t *testing.T) { got := SumAllTails([]int{1, 2}, []int{0, 9}) want := []int{2, 9} if !reflect.DeepEqual(got, want) { t.Errorf("got %v want %v", got, want) } } (1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-section-arrays-and-their-type-write-the-test-first-1f50e379]] - source section: Arrays and their type / Write the test first shares technical record from Arrays and their type / Write the test first: func TestSumAllTails(t *testing.T) { t.Run("make the sums of some slices", func(t *testing.T) { got := SumAllTails([]int{1, 2}, []int{0, 9}) want := []int{2, 9} if ! ... [truncated] (1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-section-structs-methods-interfaces-write-the-test-first-cbb1567f]] - source section: Structs, methods & interfaces / Write the test first shares source evidence from Structs, methods & interfaces / Write the test first: Notice the new format string? The f is for our float64 and the .2 means print 2 decimal places.; Structs, methods & interfaces / Write the test first shares technical record from Structs, methods & interfaces / Write the test first: func TestPerimeter(t *testing.T) { got := Perimeter(10.0, 10.0) want := 40.0 if got != want { t.Errorf("got %.2f want %.2f", got, want) } } (1 shared statement(s), 1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-section-structs-methods-interfaces-write-the-test-first-5ffd50f2]] - source section: Structs, methods & interfaces / Write the test first shares technical record from Structs, methods & interfaces / Write the test first: func TestArea(t *testing.T) { t.Run("rectangles", func(t *testing.T) { rectangle := Rectangle{12, 6} got := Area(rectangle) want := 72.0 if got != want { t.Errorf("g ... [truncated] (2 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-section-decoupling-write-the-test-first-05e88611]] - source section: Decoupling / Write the test first shares source evidence from Decoupling / Write the test first: Adding a new test for our new shape is very easy. Just add {Triangle{12, 6}, 36.0}, to our list.; Decoupling / Write the test first shares technical record from Decoupling / Write the test first: func TestArea(t *testing.T) { areaTests := []struct { shape Shape want  float64 (1 shared statement(s), 2 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-section-maps-write-the-test-first-3b38a417]] - source section: Maps / Write the test first shares source evidence from Maps / Write the test first: Declaring a Map is somewhat similar to an array. Except, it starts with the map keyword and requires two types. The first is the key type, which is written inside th ... [truncated]; Maps / Write the test first shares technical record from Maps / Write the test first: In dictionary_test.go package main import "testing" func TestSearch(t *testing.T) { dictionary := map[string]string{"test": "this is just a test"} got := Search(dict ... [truncated] (8 shared statement(s), 2 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-section-using-a-custom-type-write-the-test-first-4c4dcc55]] - source section: Using a custom type / Write the test first shares source evidence from Using a custom type / Write the test first: We actually get nothing back. This is good because the program can continue to run, but there is a better approach. The function can report that the word is not in t ... [truncated]; Using a custom type / Write the test first shares technical record from Using a custom type / Write the test first: func TestSearch(t *testing.T) { dictionary := Dictionary{"test": "this is just a test"} t.Run("known word", func(t *testing.T) { got, _ := dictionary.Search("test") ... [truncated] (6 shared statement(s), 1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-section-using-a-custom-type-write-the-test-first-d5397d92]] - source section: Using a custom type / Write the test first shares source evidence from Using a custom type / Write the test first: We have a great way to search the dictionary. However, we have no way to add new words to our dictionary.; Using a custom type / Write the test first shares technical record from Using a custom type / Write the test first: func TestAdd(t *testing.T) { dictionary := Dictionary{} dictionary.Add("test", "this is just a test") want := "this is just a test" got, err := dictionary.Search("te ... [truncated] (3 shared statement(s), 1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-section-pointers-copies-et-al-write-the-test-first-195162d9]] - source section: Pointers, copies, et al / Write the test first shares source evidence from Pointers, copies, et al / Write the test first: For this test, we modified Add to return an error, which we are validating against a new error variable, ErrWordExists . We also modified the previous test to check ... [truncated]; Pointers, copies, et al / Write the test first shares technical record from Pointers, copies, et al / Write the test first: func TestAdd(t *testing.T) { t.Run("new word", func(t *testing.T) { dictionary := Dictionary{} word := "test" definition := "this is just a test" err := dictionary.A ... [truncated] (2 shared statement(s), 1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-section-pointers-copies-et-al-write-the-test-first-764407b8]] - source section: Pointers, copies, et al / Write the test first shares source evidence from Pointers, copies, et al / Write the test first: Update is very closely related to Add and will be our next implementation.; Pointers, copies, et al / Write the test first shares technical record from Pointers, copies, et al / Write the test first: func TestUpdate(t *testing.T) { word := "test" definition := "this is just a test" dictionary := Dictionary{word: definition} newDefinition := "new definition" (1 shared statement(s), 2 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-section-pointers-copies-et-al-write-the-test-first-9d6f8acb]] - source section: Pointers, copies, et al / Write the test first shares source evidence from Pointers, copies, et al / Write the test first: We added yet another error type for when the word does not exist. We also modified Update to return an error value.; Pointers, copies, et al / Write the test first shares technical record from Pointers, copies, et al / Write the test first: t.Run("existing word", func(t *testing.T) { word := "test" definition := "this is just a test" dictionary := Dictionary{word: definition} newDefinition := "new defin ... [truncated] (2 shared statement(s), 2 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-section-note-on-declaring-a-new-error-for-update-write-the-test-first-601be12a]] - source section: Note on declaring a new error for Update / Write the test first shares source evidence from Note on declaring a new error for Update / Write the test first: Our test creates a Dictionary with a word and then checks if the word has been removed.; Note on declaring a new error for Update / Write the test first shares technical record from Note on declaring a new error for Update / Write the test first: func TestDelete(t *testing.T) { word := "test" dictionary := Dictionary{word: "test definition"} dictionary.Delete(word) _, err := dictionary.Search(word) assertErro ... [truncated] (1 shared statement(s), 1 shared atom(s))

## Source

- [[coding-learn-go-with-tests-excerpt]]
