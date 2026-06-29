---
page_id: coding-learn-go-with-tests-excerpt-refactor
page_kind: concept
summary: one...last...refactor?: 11 statement(s) and 3 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-29
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-refactor@2a1cf3e291abd702cbdf9f4c6bbad742
---

# one...last...refactor?

What [[coding-learn-go-with-tests-excerpt]] covers about one...last...refactor?:

## Statements

### one...last...refactor?

- You could argue that maybe our function is getting a little big. The simplest refactor for this would be to extract out some functionality into another function. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00135))_

- In our function signature we have made a named return value (prefix string) . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00140))_

- This will create a variable called prefix in your function. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00141))_

- It will be assigned the "zero" value. This depends on the type, for example int s are 0 and for string s it is "" . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00142))_

- This will display in the Go Doc for your function so it can make the intent of your code clearer. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00144))_

- default in the switch case will be branched to if none of the other case statements match. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00145))_

- The function name starts with a lowercase letter. In Go, public functions start with a capital letter, and private ones start with a lowercase letter. We don't want the internals of our algorithm exposed to the world, so we made this function private. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00146))_

- Also, we can group constants in a block instead of declaring them on their own line. For readability, it's a good idea to use a line between sets of related constants. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00147))_


## Technical atoms

### Technical frame 1: one...last...refactor?

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00140))_

> In our function signature we have made a named return value (prefix string) .

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00136))_

```
const (
    spanish = "Spanish"
    french  = "French"
englishHelloPrefix = "Hello, "
    spanishHelloPrefix = "Hola, "
    frenchHelloPrefix  = "Bonjour, "
)
func Hello(name string, language string) string {
    if name == "" {
        name = "World"
    }
return greetingPrefix(language) + name
```

### Technical frame 2: one...last...refactor?

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00140))_

> In our function signature we have made a named return value (prefix string) .

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00137))_

```
}
func greetingPrefix(language string) (prefix string) {
    switch language {
    case french:
        prefix = frenchHelloPrefix
    case spanish:
        prefix = spanishHelloPrefix
    default:
        prefix = englishHelloPrefix
    }
    return
```

### Technical frame 3: one...last...refactor?

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00140))_

> In our function signature we have made a named return value (prefix string) .

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00138))_

```
}
```


## Related pages

- [[coding-learn-go-with-tests-excerpt-function]] - shared statements: Function shares source evidence from one...last...refactor?: In our function signature we have made a named return value (prefix string) . (1 shared statement(s))
- [[coding-learn-go-with-tests-excerpt-type]] - shared statements: Type shares source evidence from one...last...refactor?: It will be assigned the "zero" value. This depends on the type, for example int s are 0 and for string s it is "" . (1 shared statement(s))
- [[coding-learn-go-with-tests-excerpt-section-one-last-refactor-09b754e6]] - source section: one...last...refactor? shares source evidence from one...last...refactor?: You could argue that maybe our function is getting a little big. The simplest refactor for this would be to extract out some functionality into another function.; one...last...refactor? shares technical record from one...last...refactor?: const ( spanish = "Spanish" french  = "French" englishHelloPrefix = "Hello, " spanishHelloPrefix = "Hola, " frenchHelloPrefix  = "Bonjour, " ) func Hello(name string ... [truncated] (11 shared statement(s), 3 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-section-integers-refactor-acc9e7fe]] - source section: Integers / Refactor shares source evidence from Integers / Refactor: There's not a lot in the actual code we can really improve on here.; Integers / Refactor shares technical record from Integers / Refactor: You can add documentation to functions with comments, and these will appear in Go Doc just like when you look at the standard library's documentation. (2 shared statement(s), 2 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-section-iteration-refactor-5810cb18]] - source section: Iteration / Refactor shares source evidence from Iteration / Refactor: += called "the Add AND assignment operator" , adds the right operand to the left operand and assigns the result to left operand. It works with other types like integers.; Iteration / Refactor shares technical record from Iteration / Refactor: const repeatCount = 5 func Repeat(character string) string { var repeated string for i := 0; i < repeatCount; i++ { repeated += character } return repeated } (1 shared statement(s), 1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-section-arrays-and-slices-refactor-d443a668]] - source section: Arrays and slices / Refactor shares technical record from Arrays and slices / Refactor: func Sum(numbers [5]int) int { sum := 0 for _, number := range numbers { sum += number } return sum } (1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-section-arrays-and-their-type-refactor-0e79c1f5]] - source section: Arrays and their type / Refactor shares source evidence from Arrays and their type / Refactor: We already refactored Sum - all we did was replace arrays with slices, so no extra changes are required. Remember that we must not neglect our test code in the refac ... [truncated]; Arrays and their type / Refactor shares technical record from Arrays and their type / Refactor: func TestSum(t *testing.T) { t.Run("collection of 5 numbers", func(t *testing.T) { numbers := []int{1, 2, 3, 4, 5} got := Sum(numbers) want := 15 if got != want { t. ... [truncated] (11 shared statement(s), 4 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-section-arrays-and-their-type-refactor-8b9fe3c9]] - source section: Arrays and their type / Refactor shares source evidence from Arrays and their type / Refactor: As mentioned, slices have a capacity. If you have a slice with a capacity of 2 and try to do mySlice[10] = 1 you will get a runtime error.; Arrays and their type / Refactor shares technical record from Arrays and their type / Refactor: func SumAll(numbersToSum ...[]int) []int { var sums []int for _, numbers := range numbersToSum { sums = append(sums, Sum(numbers)) } (6 shared statement(s), 2 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-section-arrays-and-their-type-refactor-1446fc86]] - source section: Arrays and their type / Refactor shares source evidence from Arrays and their type / Refactor: We could've created a new function checkSums like we normally do, but in this case, we're showing a new technique, assigning a function to a variable. It might look ... [truncated]; Arrays and their type / Refactor shares technical record from Arrays and their type / Refactor: func TestSumAllTails(t *testing.T) { checkSums := func(t testing.TB, got, want []int) { t.Helper() if !reflect.DeepEqual(got, want) { t.Errorf("got %v want %v", got, ... [truncated] (6 shared statement(s), 2 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-section-structs-methods-interfaces-refactor-d4181327]] - source section: Structs, methods & interfaces / Refactor shares source evidence from Structs, methods & interfaces / Refactor: Our code does the job, but it doesn't contain anything explicit about rectangles. An unwary developer might try to supply the width and height of a triangle to these ... [truncated]; Structs, methods & interfaces / Refactor shares technical record from Structs, methods & interfaces / Refactor: type Rectangle struct { Width  float64 Height float64 } (7 shared statement(s), 3 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-section-what-are-methods-refactor-1d16bf7b]] - source section: What are methods? / Refactor shares source evidence from What are methods? / Refactor: There is some duplication in our tests.; What are methods? / Refactor shares technical record from What are methods? / Refactor: func TestArea(t *testing.T) { (9 shared statement(s), 3 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-section-decoupling-refactor-1b44f28f]] - source section: Decoupling / Refactor shares source evidence from Decoupling / Refactor: Again, the implementation is fine but our tests could do with some improvement.; Decoupling / Refactor shares technical record from Decoupling / Refactor: {Rectangle{12, 6}, 72.0}, {Circle{10}, 314.1592653589793}, {Triangle{12, 6}, 36.0}, (3 shared statement(s), 2 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-section-maps-refactor-a6824beb]] - source section: Maps / Refactor shares source evidence from Maps / Refactor: I decided to create an assertStrings helper to make the implementation more general.; Maps / Refactor shares technical record from Maps / Refactor: func TestSearch(t *testing.T) { dictionary := map[string]string{"test": "this is just a test"} got := Search(dictionary, "test") want := "this is just a test" assert ... [truncated] (1 shared statement(s), 1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-section-using-a-custom-type-refactor-862871b5]] - source section: Using a custom type / Refactor shares source evidence from Using a custom type / Refactor: By creating a new helper we were able to simplify our test, and start using our ErrNotFound variable so our test doesn't fail if we change the error text in the future.; Using a custom type / Refactor shares technical record from Using a custom type / Refactor: var ErrNotFound = errors.New("could not find the word you were looking for") func (d Dictionary) Search(word string) (string, error) { definition, ok := d[word] if ! ... [truncated] (1 shared statement(s), 2 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-section-pointers-copies-et-al-refactor-5d607a3f]] - source section: Pointers, copies, et al / Refactor shares source evidence from Pointers, copies, et al / Refactor: There isn't much to refactor in our implementation but the test could use a little simplification.; Pointers, copies, et al / Refactor shares technical record from Pointers, copies, et al / Refactor: func TestAdd(t *testing.T) { dictionary := Dictionary{} word := "test" definition := "this is just a test" dictionary.Add(word, definition) assertDefinition(t, dicti ... [truncated] (8 shared statement(s), 1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-section-pointers-copies-et-al-refactor-c066e9e2]] - source section: Pointers, copies, et al / Refactor shares source evidence from Pointers, copies, et al / Refactor: We don't have too much to refactor, but as our error usage grows we can make a few modifications.; Pointers, copies, et al / Refactor shares technical record from Pointers, copies, et al / Refactor: const ( ErrNotFound   = DictionaryErr("could not find the word you were looking for") ErrWordExists = DictionaryErr("cannot add word because it already exists") ) ty ... [truncated] (3 shared statement(s), 1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-section-note-on-declaring-a-new-error-for-update-refactor-6eade47d]] - source section: Note on declaring a new error for Update / Refactor shares source evidence from Note on declaring a new error for Update / Refactor: There isn't much to refactor, but we can implement the same logic from Update to handle cases where word doesn't exist.; Note on declaring a new error for Update / Refactor shares technical record from Note on declaring a new error for Update / Refactor: func TestDelete(t *testing.T) { t.Run("existing word", func(t *testing.T) { word := "test" dictionary := Dictionary{word: "test definition"} err := dictionary.Delete ... [truncated] (1 shared statement(s), 1 shared atom(s))

## Source

- [[coding-learn-go-with-tests-excerpt]]
