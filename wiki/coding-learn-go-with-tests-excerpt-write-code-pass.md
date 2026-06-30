---
page_id: coding-learn-go-with-tests-excerpt-write-code-pass
page_kind: concept
summary: Write enough code to make it pass: 39 statement(s) and 26 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
page_family: broad-topic
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-30
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-write-code-pass@79fc718804de772cc6cb7131d1750520
---

# Write enough code to make it pass

What [[coding-learn-go-with-tests-excerpt]] covers about write enough code to make it pass:

## Statements

### Hello, World / Back to Testing

- of the code you will write. Writing tests Writing a test is just like writing a function, with a few rules It needs to be in a file with a name like xxx_test.go The test function must start with the word Test The test function takes one argument only t *testing.T To use the *testing.T type, you need to import "testing" , like we did with fmt in the other file For now, it's enough to know that your t of type *testing.T is your "hook" into the testing framework so you can do things like t.Fail() when you want to fail. We've covered some new topics: if If statements in Go are very much like other programming languages. Declaring variables We're declaring some variables with the syntax varName := value , which lets us reuse some values in our test for readability. t.Errorf We are calling the method on our , which will print out a _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00033))_

### Hello, YOU

- In the last example, we wrote the test after the code had been written so that you could get an example of how to write a test and declare a function. From this point on, we will be writing tests first . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00044))_

### Constants / Hello, world... again

- We've refactored our assertion into a new function. This reduces duplication and improves the readability of our tests. We need to pass in t *testing.T so that we can tell the test code to fail when we need to. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00086))_

### Integers

- Integers work as you would expect. Let's write an Add function to try things out. Create a test file called adder_test.go and write this code. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00164))_

### Integers / Write enough code to make it pass

- In the strictest sense of TDD we should now write the minimal amount of code to make the test pass . A pedantic programmer may do this _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00182))_

- Once we're more familiar with Go's syntax I will introduce a technique called "Property Based Testing" , which would stop annoying developers and help you find bugs. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00186))_

### Iteration / Write enough code to make it pass

- The for syntax is very unremarkable and follows most C-like languages. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00232))_

- as we've been using := so far to declare and initializing variables. However, := is simply short hand for both steps. Here we are declaring a string variable only. Hence, the explicit version. We can also use var to declare functions, as we'll see later on. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00236))_

- Run the test and it should pass. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00237))_

### Arrays and slices / Write enough code to make it pass

- To get the value out of an array at a particular index, just use array[index] syntax. In this case, we are using for to iterate 5 times to work through the array and add each item onto sum . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00297))_

### Arrays and their type / Write enough code to make it pass

- You can index slices like arrays with mySlice[N] to get the value out or assign it a new value with = _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00357))_

- The tests should now pass. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00358))_

- Slices can be sliced! The syntax is slice[low:high] . If you omit the value on one of the sides of the : it captures everything to that side of it. In our case, we are saying "take from 1 to the end" with numbers[1:] . You may wish to spend some time writing other tests around slices and experiment with the slice operator to get more familiar with it. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00374))_

### Structs, methods & interfaces / Write enough code to make it pass

- Try to do it yourself, following the TDD cycle. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00422))_

### What are methods? / Write enough code to make it pass

- If you re-run the tests the rectangle tests should be passing but circle should still be failing. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00466))_

### What are methods? / Refactor

- We want to be able to write some kind of checkArea function that we can pass both Rectangle s and Circle s to, but fail to compile if we try to pass in something that isn't a shape. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00472))_

- Once you add this to the code, the tests will pass. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00482))_

### Wait, what?

- This is quite different to interfaces in most other programming languages. Normally you have to write code to say My type Foo implements interface Bar . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00484))_

### Maps / Write enough code to make it pass

- Getting a value out of a Map is the same as getting a value out of Array map[key] . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00562))_

### Using a custom type / Write enough code to make it pass

- In order to make this pass, we are using an interesting property of the map lookup. It can return 2 values. The second value is a boolean which indicates if the key was found successfully. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00589))_

- This property allows us to differentiate between a word that doesn't exist and a word that just doesn't have a definition. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00590))_

- Adding to a map is also similar to an array. You just need to specify a key and set it equal to a value. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00603))_

### Pointers, copies, et al / Write enough code to make it pass

- Here we are using a switch statement to match on the error. Having a switch like this provides an extra safety net, in case Search returns an error other than ErrNotFound . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00633))_

- We already saw how to do this when we fixed the issue with Add . So let's implement something really similar to Add . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00651))_

- There is no refactoring we need to do on this since it was a simple change. However, we now have the same issue as with Add . If we pass in a new word, Update will add it to the dictionary. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00653))_

### Note on declaring a new error for Update / Write enough code to make it pass

- Go has a built-in function delete that works on maps. It takes two arguments and returns nothing. The first argument is the map and the second is the key to be removed. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00687))_

- We are again using a switch statement to match on the error when we attempt to delete a word that doesn't exist. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00696))_

- This function looks almost identical to Add except we switched when we update the dictionary and when we return an error. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00669))_

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

### Technical frame 2: Integers / Write enough code to make it pass

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00186))_

> Once we're more familiar with Go's syntax I will introduce a technique called "Property Based Testing" , which would stop annoying developers and help you find bugs.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00183))_

```
func Add(x, y int) int {
    return 4
}
```

### Technical frame 3: Integers / Write enough code to make it pass

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00186))_

> Once we're more familiar with Go's syntax I will introduce a technique called "Property Based Testing" , which would stop annoying developers and help you find bugs.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00188))_

```
func Add(x, y int) int {
    return x + y
}
```

### Technical frame 4: Integers / Write enough code to make it pass

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00186))_

> Once we're more familiar with Go's syntax I will introduce a technique called "Property Based Testing" , which would stop annoying developers and help you find bugs.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00189))_

> If you re-run the tests they should pass.

### Technical frame 5: Iteration / Write enough code to make it pass

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00236))_

> as we've been using := so far to declare and initializing variables. However, := is simply short hand for both steps. Here we are declaring a string variable only. Hence, the explicit version. We can also use var to declare functions, as we'll see later on.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00233))_

```
func Repeat(character string) string {
    var repeated string
    for i := 0; i < 5; i++ {
        repeated = repeated + character
    }
    return repeated
}
```

### Technical frame 6: Iteration / Write enough code to make it pass

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00236))_

> as we've been using := so far to declare and initializing variables. However, := is simply short hand for both steps. Here we are declaring a string variable only. Hence, the explicit version. We can also use var to declare functions, as we'll see later on.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00235))_

```
var repeated string
```

### Technical frame 7: Arrays and slices / Write enough code to make it pass

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00297))_

> To get the value out of an array at a particular index, just use array[index] syntax. In this case, we are using for to iterate 5 times to work through the array and add each item onto sum .

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00296))_

```
func Sum(numbers [5]int) int {
    sum := 0
    for i := 0; i < 5; i++ {
        sum += numbers[i]
    }
    return sum
}
```

### Technical frame 8: Arrays and their type / Write enough code to make it pass

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00357))_

> You can index slices like arrays with mySlice[N] to get the value out or assign it a new value with =

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00354))_

```
func SumAll(numbersToSum ...[]int) []int {
    lengthOfNumbers := len(numbersToSum)
    sums := make([]int, lengthOfNumbers)
for i, numbers := range numbersToSum {
        sums[i] = Sum(numbers)
    }
return sums
}
```

### Technical frame 9: Arrays and their type / Write enough code to make it pass

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00374))_

> Slices can be sliced! The syntax is slice[low:high] . If you omit the value on one of the sides of the : it captures everything to that side of it. In our case, we are saying "take from 1 to the end" with numbers[1:] . You may wish to spend some time writing other tests around slices and experiment with the slice operator to get more familiar with it.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00373))_

```
func SumAllTails(numbersToSum ...[]int) []int {
    var sums []int
    for _, numbers := range numbersToSum {
        tail := numbers[1:]
        sums = append(sums, Sum(tail))
    }
return sums
}
```

### Technical frame 10: Arrays and their type / Write enough code to make it pass

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00385))_

```
func SumAllTails(numbersToSum ...[]int) []int {
    var sums []int
    for _, numbers := range numbersToSum {
        if len(numbers) == 0 {
            sums = append(sums, 0)
        } else {
            tail := numbers[1:]
            sums = append(sums, Sum(tail))
        }
    }
return sums
}
```

### Technical frame 11: Structs, methods & interfaces / Write enough code to make it pass

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00422))_

> Try to do it yourself, following the TDD cycle.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00420))_

```
func Perimeter(width float64, height float64) float64 {
    return 2 * (width + height)
}
```

### Technical frame 12: Structs, methods & interfaces / Write enough code to make it pass

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00422))_

> Try to do it yourself, following the TDD cycle.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00424))_

```
func TestPerimeter(t *testing.T) {
    got := Perimeter(10.0, 10.0)
    want := 40.0
if got != want {
        t.Errorf("got %.2f want %.2f", got, want)
    }
}
func TestArea(t *testing.T) {
    got := Area(12.0, 6.0)
    want := 72.0
if got != want {
        t.Errorf("got %.2f want %.2f", got, want)
    }
}
And code like this
func Perimeter(width float64, height float64) float64 {
    return 2 * (width + height)
}
func Area(width float64, height float64) float64 {
    return width * height
}
```

### Technical frame 13: What are methods? / Write enough code to make it pass

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00466))_

> If you re-run the tests the rectangle tests should be passing but circle should still be failing.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00465))_

```
func (r Rectangle) Area() float64 {
    return r.Width * r.Height
}
```

### Technical frame 14: What are methods? / Write enough code to make it pass

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00466))_

> If you re-run the tests the rectangle tests should be passing but circle should still be failing.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00468))_

```
func (c Circle) Area() float64 {
    return math.Pi * c.Radius * c.Radius
}
```

### Technical frame 15: Decoupling / Write enough code to make it pass

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00512))_

```
func (t Triangle) Area() float64 {
    return (t.Base * t.Height) * 0.5
}
And our tests pass!
```

### Technical frame 16: Maps / Write enough code to make it pass

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00562))_

> Getting a value out of a Map is the same as getting a value out of Array map[key] .

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00561))_

```
func Search(dictionary map[string]string, word string) string {
    return dictionary[word]
}
```

### Technical frame 17: Using a custom type / Write enough code to make it pass

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00589))_

> In order to make this pass, we are using an interesting property of the map lookup. It can return 2 values. The second value is a boolean which indicates if the key was found successfully.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00588))_

```
func (d Dictionary) Search(word string) (string, error) {
    definition, ok := d[word]
    if !ok {
        return "", errors.New("could not find the word you were 
looking for")
}
return definition, nil
}
```

### Technical frame 18: Using a custom type / Write enough code to make it pass

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00603))_

> Adding to a map is also similar to an array. You just need to specify a key and set it equal to a value.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00602))_

```
func (d Dictionary) Add(word, definition string) {
    d[word] = definition
}
```

### Technical frame 19: Pointers, copies, et al / Write enough code to make it pass

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00633))_

> Here we are using a switch statement to match on the error. Having a switch like this provides an extra safety net, in case Search returns an error other than ErrNotFound .

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00632))_

```
func (d Dictionary) Add(word, definition string) error {
    _, err := d.Search(word)
switch err {
    case ErrNotFound:
        d[word] = definition
    case nil:
        return ErrWordExists
    default:
        return err
    }
return nil
}
```

### Technical frame 20: Pointers, copies, et al / Write enough code to make it pass

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00653))_

> There is no refactoring we need to do on this since it was a simple change. However, we now have the same issue as with Add . If we pass in a new word, Update will add it to the dictionary.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00652))_

```
func (d Dictionary) Update(word, definition string) {
    d[word] = definition
}
```

### Technical frame 21: Pointers, copies, et al / Write enough code to make it pass

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00651))_

> We already saw how to do this when we fixed the issue with Add . So let's implement something really similar to Add .

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00653))_

> If we pass in a new word, Update will add it to the dictionary.

### Technical frame 22: Pointers, copies, et al / Write enough code to make it pass

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00669))_

> This function looks almost identical to Add except we switched when we update the dictionary and when we return an error.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00667))_

```
func (d Dictionary) Update(word, definition string) error {
    _, err := d.Search(word)
switch err {
    case ErrNotFound:
        return ErrWordDoesNotExist
    case nil:
        d[word] = definition
    default:
        return err
    }
return nil
```

### Technical frame 23: Pointers, copies, et al / Write enough code to make it pass

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00669))_

> This function looks almost identical to Add except we switched when we update the dictionary and when we return an error.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00668))_

```
}
```

### Technical frame 24: Note on declaring a new error for Update / Write enough code to make it pass

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00687))_

> Go has a built-in function delete that works on maps. It takes two arguments and returns nothing. The first argument is the map and the second is the key to be removed.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00685))_

```
func (d Dictionary) Delete(word string) {
    delete(d, word)
```

### Technical frame 25: Note on declaring a new error for Update / Write enough code to make it pass

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00687))_

> Go has a built-in function delete that works on maps. It takes two arguments and returns nothing. The first argument is the map and the second is the key to be removed.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00686))_

```
}
```

### Technical frame 26: Note on declaring a new error for Update / Write enough code to make it pass

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00696))_

> We are again using a switch statement to match on the error when we attempt to delete a word that doesn't exist.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00695))_

```
func (d Dictionary) Delete(word string) error {
    _, err := d.Search(word)
switch err {
    case ErrNotFound:
        return ErrWordDoesNotExist
    case nil:
        delete(d, word)
    default:
        return err
    }
return nil
}
```


## Related pages

- [[coding-learn-go-with-tests-excerpt-code]] - broader topic: Code shares source evidence from Hello, World / Back to Testing: of the code you will write. Writing tests Writing a test is just like writing a function, with a few rules It needs to be in a file with a name like xxx_test.go The ... [truncated]; Code shares technical record from Learn Go with Tests (Excerpt): output Write enough code to make it pass Refactor Write the test ﬁrst Try and run the test Write minimal amount of code for the test to run and check the failing tes ... [truncated] (2 shared statement(s), 1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-write]] - broader topic: Write shares technical record from Learn Go with Tests (Excerpt): output Write enough code to make it pass Refactor Write the test ﬁrst Try and run the test Write minimal amount of code for the test to run and check the failing tes ... [truncated] (1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-test]] - shared statements and technical atoms: Test shares source evidence from Hello, YOU: In the last example, we wrote the test after the code had been written so that you could get an example of how to write a test and declare a function. From this poin ... [truncated]; Test shares technical record from Learn Go with Tests (Excerpt): output Write enough code to make it pass Refactor Write the test ﬁrst Try and run the test Write minimal amount of code for the test to run and check the failing tes ... [truncated] (5 shared statement(s), 1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-write-test]] - shared statements and technical atoms: Write the test first shares source evidence from Hello, YOU: In the last example, we wrote the test after the code had been written so that you could get an example of how to write a test and declare a function. From this poin ... [truncated]; Write the test first shares technical record from Learn Go with Tests (Excerpt): output Write enough code to make it pass Refactor Write the test ﬁrst Try and run the test Write minimal amount of code for the test to run and check the failing tes ... [truncated] (3 shared statement(s), 1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-try-run-test]] - shared statements and technical atoms: Try and run the test shares source evidence from Iteration / Write enough code to make it pass: Run the test and it should pass.; Try and run the test shares technical record from Learn Go with Tests (Excerpt): output Write enough code to make it pass Refactor Write the test ﬁrst Try and run the test Write minimal amount of code for the test to run and check the failing tes ... [truncated] (2 shared statement(s), 1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-array]] - shared statements: Array shares source evidence from Arrays and slices / Write enough code to make it pass: To get the value out of an array at a particular index, just use array[index] syntax. In this case, we are using for to iterate 5 times to work through the array and ... [truncated] (3 shared statement(s))
- [[coding-learn-go-with-tests-excerpt-syntax]] - shared statements: Syntax shares source evidence from Integers / Write enough code to make it pass: Once we're more familiar with Go's syntax I will introduce a technique called "Property Based Testing" , which would stop annoying developers and help you find bugs. (3 shared statement(s))
- [[coding-learn-go-with-tests-excerpt-section-integers-write-enough-code-to-make-it-pass-edef33e0]] - source section: Integers / Write enough code to make it pass shares source evidence from Integers / Write enough code to make it pass: In the strictest sense of TDD we should now write the minimal amount of code to make the test pass . A pedantic programmer may do this; Integers / Write enough code to make it pass shares technical record from Integers / Write enough code to make it pass: func Add(x, y int) int { return 4 } (2 shared statement(s), 3 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-section-iteration-write-enough-code-to-make-it-pass-82c13f0e]] - source section: Iteration / Write enough code to make it pass shares source evidence from Iteration / Write enough code to make it pass: The for syntax is very unremarkable and follows most C-like languages.; Iteration / Write enough code to make it pass shares technical record from Iteration / Write enough code to make it pass: func Repeat(character string) string { var repeated string for i := 0; i < 5; i++ { repeated = repeated + character } return repeated } (7 shared statement(s), 2 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-section-arrays-and-slices-write-enough-code-to-make-it-pass-52249515]] - source section: Arrays and slices / Write enough code to make it pass shares source evidence from Arrays and slices / Write enough code to make it pass: To get the value out of an array at a particular index, just use array[index] syntax. In this case, we are using for to iterate 5 times to work through the array and ... [truncated]; Arrays and slices / Write enough code to make it pass shares technical record from Arrays and slices / Write enough code to make it pass: func Sum(numbers [5]int) int { sum := 0 for i := 0; i < 5; i++ { sum += numbers[i] } return sum } (2 shared statement(s), 1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-section-arrays-and-their-type-write-enough-code-to-make-it-pass-e067099b]] - source section: Arrays and their type / Write enough code to make it pass shares source evidence from Arrays and their type / Write enough code to make it pass: You can index slices like arrays with mySlice[N] to get the value out or assign it a new value with =; Arrays and their type / Write enough code to make it pass shares technical record from Arrays and their type / Write enough code to make it pass: func SumAll(numbersToSum ...[]int) []int { lengthOfNumbers := len(numbersToSum) sums := make([]int, lengthOfNumbers) for i, numbers := range numbersToSum { sums[i] = ... [truncated] (2 shared statement(s), 1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-section-arrays-and-their-type-write-enough-code-to-make-it-pass-5bb60d7b]] - source section: Arrays and their type / Write enough code to make it pass shares source evidence from Arrays and their type / Write enough code to make it pass: Slices can be sliced! The syntax is slice[low:high] . If you omit the value on one of the sides of the : it captures everything to that side of it. In our case, we a ... [truncated]; Arrays and their type / Write enough code to make it pass shares technical record from Arrays and their type / Write enough code to make it pass: func SumAllTails(numbersToSum ...[]int) []int { var sums []int for _, numbers := range numbersToSum { tail := numbers[1:] sums = append(sums, Sum(tail)) } return sums } (3 shared statement(s), 1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-section-arrays-and-their-type-write-enough-code-to-make-it-pass-e71e4d2b]] - source section: Arrays and their type / Write enough code to make it pass shares technical record from Arrays and their type / Write enough code to make it pass: func SumAllTails(numbersToSum ...[]int) []int { var sums []int for _, numbers := range numbersToSum { if len(numbers) == 0 { sums = append(sums, 0) } else { tail := ... [truncated] (1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-section-structs-methods-interfaces-write-enough-code-to-make-it-pass-075da993]] - source section: Structs, methods & interfaces / Write enough code to make it pass shares source evidence from Structs, methods & interfaces / Write enough code to make it pass: Try to do it yourself, following the TDD cycle.; Structs, methods & interfaces / Write enough code to make it pass shares technical record from Structs, methods & interfaces / Write enough code to make it pass: func Perimeter(width float64, height float64) float64 { return 2 * (width + height) } (1 shared statement(s), 2 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-section-what-are-methods-write-enough-code-to-make-it-pass-43d2ca7f]] - source section: What are methods? / Write enough code to make it pass shares source evidence from What are methods? / Write enough code to make it pass: If you re-run the tests the rectangle tests should be passing but circle should still be failing.; What are methods? / Write enough code to make it pass shares technical record from What are methods? / Write enough code to make it pass: func (r Rectangle) Area() float64 { return r.Width * r.Height } (1 shared statement(s), 2 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-section-decoupling-write-enough-code-to-make-it-pass-9ad411ad]] - source section: Decoupling / Write enough code to make it pass shares technical record from Decoupling / Write enough code to make it pass: func (t Triangle) Area() float64 { return (t.Base * t.Height) * 0.5 } And our tests pass! (1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-section-maps-write-enough-code-to-make-it-pass-e76e129f]] - source section: Maps / Write enough code to make it pass shares source evidence from Maps / Write enough code to make it pass: Getting a value out of a Map is the same as getting a value out of Array map[key] .; Maps / Write enough code to make it pass shares technical record from Maps / Write enough code to make it pass: func Search(dictionary map[string]string, word string) string { return dictionary[word] } (1 shared statement(s), 1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-section-using-a-custom-type-write-enough-code-to-make-it-pass-0fbec14c]] - source section: Using a custom type / Write enough code to make it pass shares source evidence from Using a custom type / Write enough code to make it pass: In order to make this pass, we are using an interesting property of the map lookup. It can return 2 values. The second value is a boolean which indicates if the key ... [truncated]; Using a custom type / Write enough code to make it pass shares technical record from Using a custom type / Write enough code to make it pass: func (d Dictionary) Search(word string) (string, error) { definition, ok := d[word] if !ok { return "", errors.New("could not find the word you were looking for") } ... [truncated] (3 shared statement(s), 1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-section-using-a-custom-type-write-enough-code-to-make-it-pass-7b766fd4]] - source section: Using a custom type / Write enough code to make it pass shares source evidence from Using a custom type / Write enough code to make it pass: Adding to a map is also similar to an array. You just need to specify a key and set it equal to a value.; Using a custom type / Write enough code to make it pass shares technical record from Using a custom type / Write enough code to make it pass: func (d Dictionary) Add(word, definition string) { d[word] = definition } (1 shared statement(s), 1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-section-pointers-copies-et-al-write-enough-code-to-make-it-pass-6f139db5]] - source section: Pointers, copies, et al / Write enough code to make it pass shares source evidence from Pointers, copies, et al / Write enough code to make it pass: Here we are using a switch statement to match on the error. Having a switch like this provides an extra safety net, in case Search returns an error other than ErrNotFound .; Pointers, copies, et al / Write enough code to make it pass shares technical record from Pointers, copies, et al / Write enough code to make it pass: func (d Dictionary) Add(word, definition string) error { _, err := d.Search(word) switch err { case ErrNotFound: d[word] = definition case nil: return ErrWordExists ... [truncated] (2 shared statement(s), 1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-section-pointers-copies-et-al-write-enough-code-to-make-it-pass-618028a3]] - source section: Pointers, copies, et al / Write enough code to make it pass shares source evidence from Pointers, copies, et al / Write enough code to make it pass: We already saw how to do this when we fixed the issue with Add . So let's implement something really similar to Add .; Pointers, copies, et al / Write enough code to make it pass shares technical record from Pointers, copies, et al / Write enough code to make it pass: func (d Dictionary) Update(word, definition string) { d[word] = definition } (3 shared statement(s), 2 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-section-pointers-copies-et-al-write-enough-code-to-make-it-pass-e62dfd1d]] - source section: Pointers, copies, et al / Write enough code to make it pass shares source evidence from Pointers, copies, et al / Write enough code to make it pass: This function looks almost identical to Add except we switched when we update the dictionary and when we return an error.; Pointers, copies, et al / Write enough code to make it pass shares technical record from Pointers, copies, et al / Write enough code to make it pass: func (d Dictionary) Update(word, definition string) error { _, err := d.Search(word) switch err { case ErrNotFound: return ErrWordDoesNotExist case nil: d[word] = de ... [truncated] (1 shared statement(s), 2 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-section-note-on-declaring-a-new-error-for-update-write-enough-code-to-make-it-pass-23382f56]] - source section: Note on declaring a new error for Update / Write enough code to make it pass shares source evidence from Note on declaring a new error for Update / Write enough code to make it pass: Go has a built-in function delete that works on maps. It takes two arguments and returns nothing. The first argument is the map and the second is the key to be removed.; Note on declaring a new error for Update / Write enough code to make it pass shares technical record from Note on declaring a new error for Update / Write enough code to make it pass: func (d Dictionary) Delete(word string) { delete(d, word) (2 shared statement(s), 2 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-section-note-on-declaring-a-new-error-for-update-write-enough-code-to-make-it-pass-39912f70]] - source section: Note on declaring a new error for Update / Write enough code to make it pass shares source evidence from Note on declaring a new error for Update / Write enough code to make it pass: We are again using a switch statement to match on the error when we attempt to delete a word that doesn't exist.; Note on declaring a new error for Update / Write enough code to make it pass shares technical record from Note on declaring a new error for Update / Write enough code to make it pass: func (d Dictionary) Delete(word string) error { _, err := d.Search(word) switch err { case ErrNotFound: return ErrWordDoesNotExist case nil: delete(d, word) default: ... [truncated] (1 shared statement(s), 1 shared atom(s))

## Source

- [[coding-learn-go-with-tests-excerpt]]
