---
page_id: coding-learn-go-with-tests-excerpt-try-run-test
page_kind: concept
summary: Try and run the test: 27 statement(s) and 19 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
page_family: broad-topic
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-30
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-try-run-test@f9e7a1a9b99c52ed4d54e16f0a0aee57
---

# Try and run the test

What [[coding-learn-go-with-tests-excerpt]] covers about try and run the test:

## Statements

### Hello, World / Go modules?

- The next step is to run the tests. Enter go test in your terminal. If the tests pass, then you are probably using an earlier version of Go. However, if you are using Go 1.16 or later, the tests will likely not run. Instead, you will see an error message like this in the terminal: _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00025))_

- This file tells the go tools essential information about your code. If you planned to distribute your application, you would include where the code was available for download as well as information about dependencies. The name of the module, example.com/hello, usually refers to a URL where the module can be found and downloaded. For compatibility with tools we'll start using soon, make sure your module's name has a dot somewhere in it, like the dot in .com of example.com/hello. For now, your module file is minimal, and you can leave it that way. To read more about modules, you can check out the reference in the Golang documentation. We can get back to testing and learning Go now since the tests should run, even on Go 1.16. In future chapters, you will need to run go mod init SOMENAME in each _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00029))_

### Hello, YOU

- If you try and run your tests again your hello.go will fail to compile because you're not passing an argument. Send in "world" to make it compile. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00055))_

### Constants

- After refactoring, re-run your tests to make sure you haven't broken anything. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00069))_

### Constants / Hello, world... again

- If we run our tests we should see it satisfies the new requirement and we haven't accidentally broken the other functionality. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00080))_

### Discipline / Keep going! More requirements

- When you try and run the test again it will complain about not passing through enough arguments to Hello in your other tests and in hello.go _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00113))_

- Now it is time to refactor . You should see some problems in the code, "magic" strings, some of which are repeated. Try and refactor it yourself, with every change make sure you re-run the tests to make sure your refactoring isn't breaking anything. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00120))_

### Integers / Write the minimal amount of code for the test to run and check the failing test output

- Now run the tests, and we should be happy that the test is correctly reporting what is wrong. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00178))_

### Testable Examples

- Notice the special format of the comment, // Output: 6 . While the example will always be compiled, adding this comment means the example will also be executed. Go ahead and temporarily remove the comment // Output: 6 , then run go test , and you will see ExampleAdd is no longer executed. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00206))_

- Examples without output comments are useful for demonstrating code that cannot run as unit tests, such as that which accesses the network, while guaranteeing the example at least compiles. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00207))_

### Iteration / Write enough code to make it pass

- Run the test and it should pass. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00237))_

### Benchmarking

- To run the benchmarks do go test -bench=. (or if you're in Windows Powershell go test -bench="." ) _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00250))_

### Arrays and slices / Try to run the test

- If you had initialized go mod with go mod init main you will be presented with an error _testmain.go:13:2: cannot import "main" . This is because according to common practice, package main will only contain integration of other packages and not unit-testable code and hence Go will not allow you to import a package with name main . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00288))_

- To fix this, you can rename the main module in go.mod to any other name. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00289))_

- Once the above error is fixed, if you run go test the compiler will fail with the familiar ./sum_test.go:10:15: undefined: Sum error. Now we can proceed with writing the actual method to be tested. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00290))_

### Arrays and their type / Try and run the test

- Oh no! It's important to note that while the test has compiled , it has a runtime error . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00382))_

- Compile time errors are our friend because they help us write software that works, runtime errors are our enemies because they affect our users. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00383))_

### What are methods? / Write enough code to make it pass

- If you re-run the tests the rectangle tests should be passing but circle should still be failing. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00466))_

### Decoupling / Further refactoring

- We then iterate over them just like we do any other slice, using the struct fields to run our tests. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00499))_

### Decoupling / Make sure your test output is helpful

- One final tip with table driven tests is to use t.Run and to name the test cases. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00530))_

- By wrapping each case in a t.Run you will have clearer test output on failures as it will print the name of the case _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00531))_

- And you can run specific tests within your table with go test -run TestArea/Rectangle . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00533))_

### Pointers, copies, et al / Try to run test

- The compiler will fail because we are not returning a value for Add . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00625))_

### Note on declaring a new error for Update / Try to run test

- The compiler will fail because we are not returning a value for Delete . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00692))_


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

### Technical frame 2: Hello, YOU

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00059))_

> We finally have a compiling program but it is not meeting our requirements according to the test.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00057))_

> Now when you run your tests, you should see something like

### Technical frame 3: Integers / Try and run the test

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00173))_

```
Run the test go test
Inspect the compilation error
./adder_test.go:6:9: undefined: Add
```

### Technical frame 4: Testable Examples

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00206))_

> Notice the special format of the comment, // Output: 6 . While the example will always be compiled, adding this comment means the example will also be executed. Go ahead and temporarily remove the comment // Output: 6 , then run go test , and you will see ExampleAdd is no longer executed.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00205))_

```
$ go test -v
=== RUN   TestAdder
--- PASS: TestAdder (0.00s)
=== RUN   ExampleAdd
--- PASS: ExampleAdd (0.00s)
```

### Technical frame 5: Iteration / Try and run the test

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00224))_

```
./repeat_test.go:6:14: undefined: Repeat
```

### Technical frame 6: Benchmarking

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00260))_

> We can use BenchmarkRepeat to confirm that strings.Builder significantly improves performance. Run go test -bench=. -benchmem

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00262))_

```
p
g
signiﬁcantly improves performance. Run go test -bench=. -benchmem:
goos: darwin
goarch: amd64
pkg: github.com/quii/learn-go-with-tests/for/v4
10000000           25.70 ns/op           8 B/op           1
```

### Technical frame 7: Arrays and their type / Try and run the test

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00314))_

```
This does not compile
./sum_test.go:22:13: cannot use numbers (type []int) as type [5]int 
in argument to Sum
```

### Technical frame 8: Arrays and their type / Try and run the test

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00340))_

```
./sum_test.go:23:9: undefined: SumAll
```

### Technical frame 9: Arrays and their type / Try and run the test

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00369))_

```
./sum_test.go:26:9: undefined: SumAllTails
```

### Technical frame 10: Arrays and their type / Try and run the test

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00382))_

> Oh no! It's important to note that while the test has compiled , it has a runtime error .

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00381))_

```
panic: runtime error: slice bounds out of range [recovered]
panic: runtime error: slice bounds out of range
```

### Technical frame 11: Structs, methods & interfaces / Try to run the test

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00416))_

```
./shapes_test.go:6:9: undefined: Perimeter
```

### Technical frame 12: Structs, methods & interfaces / Try to run the test

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00441))_

```
./shapes_test.go:28:13: undefined: Circle
```

### Technical frame 13: Decoupling / Make sure your test output is helpful

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00533))_

> And you can run specific tests within your table with go test -run TestArea/Rectangle .

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00535))_

```
func TestArea(t *testing.T) {
areaTests := []struct {
        name    string
        shape   Shape
        hasArea float64
    }{
        {name: "Rectangle", shape: Rectangle{Width: 12, Height: 6}, 
hasArea: 72.0},
{name: "Circle", shape: Circle{Radius: 10}, hasArea: 
314.1592653589793},
{name: "Triangle", shape: Triangle{Base: 12, Height: 6}, 
hasArea: 36.0},
}
for _, tt := range areaTests {
        // using tt.name from the case to use it as the `t.Run` test 
name
t.Run(tt.name, func(t *testing.T) {
            got := tt.shape.Area()
            if got != tt.hasArea {
                t.Errorf("%#v got %g want %g", tt.shape, got, 
tt.hasArea)
}
        })
}
}
```

### Technical frame 14: Using a custom type / Try and run the test

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00582))_

```
This does not compile
./dictionary_test.go:18:10: assignment mismatch: 2 variables but 1 
values
```

### Technical frame 15: Pointers, copies, et al / Try to run test

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00625))_

> The compiler will fail because we are not returning a value for Add .

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00626))_

```
./dictionary_test.go:30:13: dictionary.Add(word, definition) used as 
value
./dictionary_test.go:41:13: dictionary.Add(word, "new test") used as 
value
```

### Technical frame 16: Pointers, copies, et al / Try and run the test

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00644))_

```
./dictionary_test.go:53:2: dictionary.Update undefined (type 
Dictionary has no field or method Update)
```

### Technical frame 17: Pointers, copies, et al / Try and run the test

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00659))_

```
./dictionary_test.go:53:16: dictionary.Update(word, newDefinition) 
used as value
./dictionary_test.go:64:16: dictionary.Update(word, definition) used 
as value
./dictionary_test.go:66:23: undefined: ErrWordDoesNotExist
```

### Technical frame 18: Note on declaring a new error for Update / Try to run the test

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00679))_

```
By running go test we get:
./dictionary_test.go:74:6: dictionary.Delete undefined (type 
Dictionary has no field or method Delete)
```

### Technical frame 19: Note on declaring a new error for Update / Try to run test

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00692))_

> The compiler will fail because we are not returning a value for Delete .

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00693))_

```
./dictionary_test.go:77:10: dictionary.Delete(word) (no value) used 
as value
./dictionary_test.go:90:10: dictionary.Delete(word) (no value) used 
as value
```


## Related pages

- [[coding-learn-go-with-tests-excerpt-test]] - broader topic: Test shares source evidence from Hello, YOU: If you try and run your tests again your hello.go will fail to compile because you're not passing an argument. Send in "world" to make it compile.; Test shares technical record from Learn Go with Tests (Excerpt): output Write enough code to make it pass Refactor Write the test ﬁrst Try and run the test Write minimal amount of code for the test to run and check the failing tes ... [truncated] (10 shared statement(s), 4 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-error]] - shared statements and technical atoms: Error shares source evidence from Arrays and slices / Try to run the test: Once the above error is fixed, if you run go test the compiler will fail with the familiar ./sum_test.go:10:15: undefined: Sum error. Now we can proceed with writing ... [truncated]; Error shares technical record from Arrays and their type / Try and run the test: panic: runtime error: slice bounds out of range [recovered] panic: runtime error: slice bounds out of range (2 shared statement(s), 1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-write-code-pass]] - shared statements and technical atoms: Write enough code to make it pass shares source evidence from Iteration / Write enough code to make it pass: Run the test and it should pass.; Write enough code to make it pass shares technical record from Learn Go with Tests (Excerpt): output Write enough code to make it pass Refactor Write the test ﬁrst Try and run the test Write minimal amount of code for the test to run and check the failing tes ... [truncated] (2 shared statement(s), 1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-code]] - shared technical atoms: Code shares technical record from Learn Go with Tests (Excerpt): output Write enough code to make it pass Refactor Write the test ﬁrst Try and run the test Write minimal amount of code for the test to run and check the failing tes ... [truncated] (1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-write]] - shared technical atoms: Write shares technical record from Learn Go with Tests (Excerpt): output Write enough code to make it pass Refactor Write the test ﬁrst Try and run the test Write minimal amount of code for the test to run and check the failing tes ... [truncated] (1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-write-test]] - shared technical atoms: Write the test first shares technical record from Learn Go with Tests (Excerpt): output Write enough code to make it pass Refactor Write the test ﬁrst Try and run the test Write minimal amount of code for the test to run and check the failing tes ... [truncated] (1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-note]] - shared statements: Note shares source evidence from Arrays and their type / Try and run the test: Oh no! It's important to note that while the test has compiled , it has a runtime error . (1 shared statement(s))
- [[coding-learn-go-with-tests-excerpt-section-integers-try-and-run-the-test-ce54b37e]] - source section: Integers / Try and run the test shares technical record from Integers / Try and run the test: Run the test go test Inspect the compilation error ./adder_test.go:6:9: undefined: Add (1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-section-iteration-try-and-run-the-test-edfc802d]] - source section: Iteration / Try and run the test shares technical record from Iteration / Try and run the test: ./repeat_test.go:6:14: undefined: Repeat (1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-section-arrays-and-slices-try-to-run-the-test-781534ae]] - source section: Arrays and slices / Try to run the test shares source evidence from Arrays and slices / Try to run the test: If you had initialized go mod with go mod init main you will be presented with an error _testmain.go:13:2: cannot import "main" . This is because according to common ... [truncated] (5 shared statement(s))
- [[coding-learn-go-with-tests-excerpt-section-arrays-and-their-type-try-and-run-the-test-19f0372e]] - source section: Arrays and their type / Try and run the test shares technical record from Arrays and their type / Try and run the test: This does not compile ./sum_test.go:22:13: cannot use numbers (type []int) as type [5]int in argument to Sum (1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-section-arrays-and-their-type-try-and-run-the-test-501a4c76]] - source section: Arrays and their type / Try and run the test shares technical record from Arrays and their type / Try and run the test: ./sum_test.go:23:9: undefined: SumAll (1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-section-arrays-and-their-type-try-and-run-the-test-8c8dea3f]] - source section: Arrays and their type / Try and run the test shares technical record from Arrays and their type / Try and run the test: ./sum_test.go:26:9: undefined: SumAllTails (1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-section-arrays-and-their-type-try-and-run-the-test-dbff4772]] - source section: Arrays and their type / Try and run the test shares source evidence from Arrays and their type / Try and run the test: Oh no! It's important to note that while the test has compiled , it has a runtime error .; Arrays and their type / Try and run the test shares technical record from Arrays and their type / Try and run the test: panic: runtime error: slice bounds out of range [recovered] panic: runtime error: slice bounds out of range (2 shared statement(s), 1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-section-structs-methods-interfaces-try-to-run-the-test-45f95e1a]] - source section: Structs, methods & interfaces / Try to run the test shares technical record from Structs, methods & interfaces / Try to run the test: ./shapes_test.go:6:9: undefined: Perimeter (1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-section-structs-methods-interfaces-try-to-run-the-test-fadb70be]] - source section: Structs, methods & interfaces / Try to run the test shares technical record from Structs, methods & interfaces / Try to run the test: ./shapes_test.go:28:13: undefined: Circle (1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-section-using-a-custom-type-try-and-run-the-test-ebf022ab]] - source section: Using a custom type / Try and run the test shares technical record from Using a custom type / Try and run the test: This does not compile ./dictionary_test.go:18:10: assignment mismatch: 2 variables but 1 values (1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-section-pointers-copies-et-al-try-to-run-test-66becf89]] - source section: Pointers, copies, et al / Try to run test shares source evidence from Pointers, copies, et al / Try to run test: The compiler will fail because we are not returning a value for Add .; Pointers, copies, et al / Try to run test shares technical record from Pointers, copies, et al / Try to run test: ./dictionary_test.go:30:13: dictionary.Add(word, definition) used as value ./dictionary_test.go:41:13: dictionary.Add(word, "new test") used as value (1 shared statement(s), 1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-section-pointers-copies-et-al-try-and-run-the-test-22b48658]] - source section: Pointers, copies, et al / Try and run the test shares technical record from Pointers, copies, et al / Try and run the test: ./dictionary_test.go:53:2: dictionary.Update undefined (type Dictionary has no field or method Update) (1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-section-pointers-copies-et-al-try-and-run-the-test-e2eb73b2]] - source section: Pointers, copies, et al / Try and run the test shares technical record from Pointers, copies, et al / Try and run the test: ./dictionary_test.go:53:16: dictionary.Update(word, newDefinition) used as value ./dictionary_test.go:64:16: dictionary.Update(word, definition) used as value ./dict ... [truncated] (1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-section-note-on-declaring-a-new-error-for-update-try-to-run-the-test-8cf14f42]] - source section: Note on declaring a new error for Update / Try to run the test shares technical record from Note on declaring a new error for Update / Try to run the test: By running go test we get: ./dictionary_test.go:74:6: dictionary.Delete undefined (type Dictionary has no field or method Delete) (1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-section-note-on-declaring-a-new-error-for-update-try-to-run-test-a79de4fc]] - source section: Note on declaring a new error for Update / Try to run test shares source evidence from Note on declaring a new error for Update / Try to run test: The compiler will fail because we are not returning a value for Delete .; Note on declaring a new error for Update / Try to run test shares technical record from Note on declaring a new error for Update / Try to run test: ./dictionary_test.go:77:10: dictionary.Delete(word) (no value) used as value ./dictionary_test.go:90:10: dictionary.Delete(word) (no value) used as value (1 shared statement(s), 1 shared atom(s))

## Source

- [[coding-learn-go-with-tests-excerpt]]
