---
page_id: type
page_kind: concept
summary: Canonical concept 'Type': 2 source(s), 15 statement(s), 9 atom(s), 0 relation(s).
sources: raw/coding_learn_go_with_tests_excerpt.pdf, raw/coding_little_go_book.pdf
updated: 2026-06-26
category_path: concepts
projection_coverage: canonical-concept-type@03d6e81e3bbd23e107596f84f633d757
---

# Type

Compiled concept page from 2 source(s), 15 statement(s), and 9 technical atom(s).

## Source Evidence

### [[coding-learn-go-with-tests-excerpt]]

Source topic: [[coding-learn-go-with-tests-excerpt-type]]

#### Statements

- The value type, on the other hand, can be any type you want. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00554))_
- This depends on the type, for example int s are 0 and for string s it is "" . _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00142))_
- We're creating a new type just like we did with Rectangle and Circle but this time it is an interface rather than a struct . _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00481))_
- If the type you pass in matches what the interface is asking for, it will compile. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00490))_
- Declaring structs to create your own data types which lets you bundle related data together and make the intent of your code clearer _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00538))_
- The key type is special. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00553))_
- Comparable types are explained in depth in the language spec. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00553))_
- With the custom type defined, we can create the Search method. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00574))_

#### Technical atoms

> Context: The key type is special. It can only be a comparable type because without the ability to tell if 2 keys are equal, we have no way to ensure that we are getting the correct value. Comparable types are explained in depth in the language spec.
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00553))_

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
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00551))_

> Context: We can improve our dictionary's usage by creating a new type around map and making Search a method.
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00567))_

```
In dictionary_test.go:
func TestSearch(t *testing.T) {
    dictionary := Dictionary{"test": "this is just a test"}
got := dictionary.Search("test")
    want := "this is just a test"
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00568))_

> Context: We can improve our dictionary's usage by creating a new type around map and making Search a method.
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00567))_

```
assertStrings(t, got, want)
}
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00569))_


### [[coding-little-go-book]]

Source topic: [[coding-little-go-book-type]]

#### Statements

- There's obviously some relation between the types Saiyan and *Saiyan , but they are two distinct types. _(coding_little_go_book.pdf (source-range-773b6275-00132))_
- Since every type implements all 0 of the empty interface's methods, and since interfaces are implicitly implemented, every type fulfills the contract of the empty interface. _(coding_little_go_book.pdf (source-range-773b6275-00368))_
- Learning new keywords, type system, coding style as well as new libraries, communities and paradigms is a lot of work that seems hard to justify. _(coding_little_go_book.pdf (source-range-773b6275-00012))_
- With a rigid type system, a compiler is able to detect problems beyond mere syntactical mistakes as well as make further optimizations. _(coding_little_go_book.pdf (source-range-773b6275-00037))_
- In the above code, we say that the type *Saiyan is the receiver of the Super method. _(coding_little_go_book.pdf (source-range-773b6275-00142))_
- The way Go handles visibility of types is straightforward and effective. _(coding_little_go_book.pdf (source-range-773b6275-00334))_
- Note that if the underlying type is not int , the above will result in an error. _(coding_little_go_book.pdf (source-range-773b6275-00373))_

#### Technical atoms

> Context: Maybe it's a messaging, caching, computational-heavy data analysis, command line interface, logging or monitoring. I don't know what label to give it, but over the course of my career, as systems continue to grow in complexity and as concurrency frequently measures in the tens of thousands, there's clearly been a growing need for custom infrastructure-type systems. You can build such systems with Ruby or Python or something else (and many people do), but these types of systems can benefit from a more rigid type system and greater performance. Similarly, you can use Go to build websites (and many people do), but I still prefer, by a wide margin, the expressiveness of Node or Ruby for such systems.
_(context: coding_little_go_book.pdf (source-range-773b6275-00016))_

> You don't have to worry if your users have Ruby or the JVM installed, and if so, what version.
_(source: coding_little_go_book.pdf (source-range-773b6275-00017))_

> Context: We can associate a method with a structure: In the above code, we say that the type *Saiyan is the receiver of the Super method. We call Super like so:
_(context: coding_little_go_book.pdf (source-range-773b6275-00140, source-range-773b6275-00142))_

```
type Saiyan struct {
  Name string
  Power int
}
func (s *Saiyan) Super() {
  s.Power += 10000
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00141))_

> Context: In the above code, we say that the type *Saiyan is the receiver of the Super method. We call Super like so:
_(context: coding_little_go_book.pdf (source-range-773b6275-00142))_

```
goku := &Saiyan{"Goku", 9001}
goku.Super()
fmt.Println(goku.Power) // will print 19001
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00143))_

> Context: The way Go handles visibility of types is straightforward and effective. It's also consistent. There are a few things we haven't looked at, such as constants and global variables but rest assured, their visibility is determined by the same naming rule.
_(context: coding_little_go_book.pdf (source-range-773b6275-00334))_

> Finally, if you're new to interfaces, it might take some time before you get a feel for them.
_(source: coding_little_go_book.pdf (source-range-773b6275-00335))_

> Context: To convert an interface variable to an explicit type, you use .(TYPE) : Note that if the underlying type is not int , the above will result in an error.
_(context: coding_little_go_book.pdf (source-range-773b6275-00371, source-range-773b6275-00373))_

```
return a.(int) + b.(int)
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00372))_

> Context: You also have access to a powerful type switch: You'll see and probably use the empty interface more than you might first expect. Admittedly, it won't result in clean code. Converting values back and forth is ugly and dangerous but sometimes, in a static language, it's the only choice.
_(context: coding_little_go_book.pdf (source-range-773b6275-00374, source-range-773b6275-00376))_

```
switch a.(type) {
  case int:
    fmt.Printf("a is now an int and equals %d\n", a)
  case bool, string:
    // ...
  default:
    // ...
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00375))_


## Cross-Source Comparison

- No typed cross-source relationships detected yet.
