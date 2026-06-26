---
page_id: coding-little-go-book-language
page_kind: concept
summary: Language: 10 statement(s) and 8 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-language@0fd65e9872309321871006399db2cc98
---

# Language

What [[coding-little-go-book]] covers about language:

## Statements

- Saying that a language has a C-like syntax means that if you're used to any other C-like languages such as C, C++, Java, JavaScript and C#, then you're going to find Go familiar -- superficially, at least. _(coding_little_go_book.pdf (source-range-773b6275-00039))_
- On the downside, language design is fairly incremental. _(coding_little_go_book.pdf (source-range-773b6275-00012))_
- On the one hand, languages are so fundamental to what we do, that even small changes can have measurable impact. _(coding_little_go_book.pdf (source-range-773b6275-00012))_
- Languages with garbage collectors (e.g., Ruby, Python, Java, JavaScript, C#, Go) are able to keep track of these and free them when they're no longer used. _(coding_little_go_book.pdf (source-range-773b6275-00047))_
- For some systems, dynamic languages are categorically more productive. _(coding_little_go_book.pdf (source-range-773b6275-00108))_
- Languages that don't have an explicit composition mechanism can always do it the long way. _(coding_little_go_book.pdf (source-range-773b6275-00160))_
- In some languages, this is called a trait or a mixin. _(coding_little_go_book.pdf (source-range-773b6275-00160))_
- In Go, like many other languages, arrays are fixed. _(coding_little_go_book.pdf (source-range-773b6275-00191))_
- Many languages have the concept of slicing an array. _(coding_little_go_book.pdf (source-range-773b6275-00230))_
- However, in these languages, a slice is actually a new array with the values of the original copied over. _(coding_little_go_book.pdf (source-range-773b6275-00230))_

## Technical atoms

> Context: That said, we have to move forward. We have to be willing to take incremental steps because, again, languages are the foundation of what we do. Though the changes are often incremental, they tend to have a wide scope and they impact productivity, readability, performance, testability, dependency management, error handling, documentation, profiling, communities, standard libraries, and so on. Is there a positive way to say death by a thousand cuts ?
_(context: coding_little_go_book.pdf (source-range-773b6275-00013))_

> I've always had a love-hate relationship when it comes to learning new languages.
_(source: coding_little_go_book.pdf (source-range-773b6275-00012))_

> Context: Go supports composition, which is the act of including one structure into another. In some languages, this is called a trait or a mixin. Languages that don't have an explicit composition mechanism can always do it the long way. In Java, there's the possibility to extend structures with inheritance but, in a scenario where this is not an option, a mixin would be written like this:
_(context: coding_little_go_book.pdf (source-range-773b6275-00160))_

```
public class Person {
  private String name;
public String getName() {
    return this.name;
  }
}
public class Saiyan {
  // Saiyan is said to have a person
  private Person person;
// we forward the call to person
  public String getName() {
    return this.person.getName();
  }
  ...
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00161))_

> Context: If you come from Python, Ruby, Perl, JavaScript or PHP (and more), you're probably used to programming with dynamic arrays . These are arrays that resize themselves as data is added to them. In Go, like many other languages, arrays are fixed. Declaring an array requires that we specify the size, and once the size is specified, it cannot grow: The above array can hold up to 10 scores using indexes scores[0] through scores[9] . Attempts to access an out of range index in the array will result in a compiler or runtime error.
_(context: coding_little_go_book.pdf (source-range-773b6275-00191, source-range-773b6275-00193))_

```
var scores [10]int
scores[0] = 339
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00192))_

> Context: The last version lets us specify an initial capacity; useful if we have a general idea of how many elements we'll need. Slices as wrappers to arrays is a powerful concept. Many languages have the concept of slicing an array. Both JavaScript and Ruby arrays have a slice method. You can also get a slice in Ruby by using [START..END] or in Python via [START:END] . However, in these languages, a slice is actually a new array with the values of the original copied over. If we take Ruby, what's the output of the following?
_(context: coding_little_go_book.pdf (source-range-773b6275-00227, source-range-773b6275-00230))_

> Even when you know the size, append can be used.
_(source: coding_little_go_book.pdf (source-range-773b6275-00228))_

> Context: Even when you know the size, append can be used. It's largely a matter of preference: Slices as wrappers to arrays is a powerful concept. Many languages have the concept of slicing an array. Both JavaScript and Ruby arrays have a slice method. You can also get a slice in Ruby by using [START..END] or in Python via [START:END] . However, in these languages, a slice is actually a new array with the values of the original copied over. If we take Ruby, what's the output of the following?
_(context: coding_little_go_book.pdf (source-range-773b6275-00228, source-range-773b6275-00230))_

```
func extractPowers(saiyans []*Saiyan) []int {
  powers := make([]int, 0, len(saiyans))
  for _, saiyan := range saiyans {
    powers = append(powers, saiyan.Power)
  }
  return powers
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00229))_

> Context: Slices as wrappers to arrays is a powerful concept. Many languages have the concept of slicing an array. Both JavaScript and Ruby arrays have a slice method. You can also get a slice in Ruby by using [START..END] or in Python via [START:END] . However, in these languages, a slice is actually a new array with the values of the original copied over. If we take Ruby, what's the output of the following? The answer is [1, 2, 3, 4, 5] . That's because slice is a completely new array with copies of values. Now, consider the Go equivalent:
_(context: coding_little_go_book.pdf (source-range-773b6275-00230, source-range-773b6275-00232))_

```
scores = [1,2,3,4,5]
slice = scores[2..4]
slice[0] = 999
puts scores
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00231))_


## Source

- [[coding-little-go-book]]
