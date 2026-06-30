---
page_id: coding-little-go-book-language
page_kind: concept
summary: Language: 10 statement(s) and 8 atom(s) from raw/coding_little_go_book.pdf.
page_family: topic-concept
sources: raw/coding_little_go_book.pdf
updated: 2026-06-30
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-language@d48ab96cb06a461d3d78cfbc5bb9d83f
---

# Language

What [[coding-little-go-book]] covers about language:

## Statements

### Introduction

- I've always had a love-hate relationship when it comes to learning new languages. On the one hand, languages are so fundamental to what we do, that even small changes can have measurable impact. That aha moment when something clicks can have a lasting effect on how you program and can redefine your expectations of other languages. On the downside, language design is fairly incremental. Learning new keywords, type system, coding style as well as new libraries, communities and paradigms is a lot of work that seems hard to justify. Compared to everything else we have to learn, new languages often feel like a poor investment of our time. _(coding_little_go_book.pdf (source-range-23d24eb1-00012))_

### Chapter 1 - The Basics / C-Like Syntax

- Saying that a language has a C-like syntax means that if you're used to any other C-like languages such as C, C++, Java, JavaScript and C#, then you're going to find Go familiar -- superficially, at least. For example, it means && is used as a boolean AND, == is used to compare equality, { and } start and end a scope, and array indexes start at 0. _(coding_little_go_book.pdf (source-range-23d24eb1-00039))_

### Chapter 1 - The Basics / Garbage Collected

- Languages with garbage collectors (e.g., Ruby, Python, Java, JavaScript, C#, Go) are able to keep track of these and free them when they're no longer used. Garbage collection adds overhead, but it also eliminates a number of devastating bugs. _(coding_little_go_book.pdf (source-range-23d24eb1-00047))_

### Chapter 1 - The Basics / Before You Continue

- If you're coming from a dynamic language, the complexity around types and declarations might seem like a step backwards. I don't disagree with you. For some systems, dynamic languages are categorically more productive. _(coding_little_go_book.pdf (source-range-23d24eb1-00108))_

### Chapter 2 - Structures / Composition

- Go supports composition, which is the act of including one structure into another. In some languages, this is called a trait or a mixin. Languages that don't have an explicit composition mechanism can always do it the long way. In Java, there's the possibility to extend structures with inheritance but, in a scenario where this is not an option, a mixin would be written like this: _(coding_little_go_book.pdf (source-range-23d24eb1-00160))_

### Chapter 3 - Maps, Arrays and Slices / Arrays

- If you come from Python, Ruby, Perl, JavaScript or PHP (and more), you're probably used to programming with dynamic arrays . These are arrays that resize themselves as data is added to them. In Go, like many other languages, arrays are fixed. Declaring an array requires that we specify the size, and once the size is specified, it cannot grow: _(coding_little_go_book.pdf (source-range-23d24eb1-00191))_

### Chapter 3 - Maps, Arrays and Slices / Slices

- Slices as wrappers to arrays is a powerful concept. Many languages have the concept of slicing an array. Both JavaScript and Ruby arrays have a slice method. You can also get a slice in Ruby by using [START..END] or in Python via [START:END] . However, in these languages, a slice is actually a new array with the values of the original copied over. If we take Ruby, what's the output of the following? _(coding_little_go_book.pdf (source-range-23d24eb1-00230))_


## Technical atoms

### Technical frame 1: Introduction

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00013))_

> That said, we have to move forward. We have to be willing to take incremental steps because, again, languages are the foundation of what we do. Though the changes are often incremental, they tend to have a wide scope and they impact productivity, readability, performance, testability, dependency management, error handling, documentation, profiling, communities, standard libraries, and so on. Is there a positive way to say death by a thousand cuts ?

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00012))_

> I've always had a love-hate relationship when it comes to learning new languages.

### Technical frame 2: Chapter 2 - Structures / Composition

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00162))_

> This can get pretty tedious. Every method of Person needs to be duplicated in Saiyan . Go avoids this tediousness:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00161))_

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

### Technical frame 3: Chapter 3 - Maps, Arrays and Slices / Arrays

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00193))_

> The above array can hold up to 10 scores using indexes scores[0] through scores[9] . Attempts to access an out of range index in the array will result in a compiler or runtime error.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00192))_

```
var scores [10]int
scores[0] = 339
```

### Technical frame 4: Chapter 3 - Maps, Arrays and Slices / Slices

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00230))_

> Slices as wrappers to arrays is a powerful concept. Many languages have the concept of slicing an array. Both JavaScript and Ruby arrays have a slice method. You can also get a slice in Ruby by using [START..END] or in Python via [START:END] . However, in these languages, a slice is actually a new array with the values of the original copied over. If we take Ruby, what's the output of the following?

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00228))_

> Even when you know the size, append can be used.

### Technical frame 5: Chapter 3 - Maps, Arrays and Slices / Slices

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00230))_

> Slices as wrappers to arrays is a powerful concept. Many languages have the concept of slicing an array. Both JavaScript and Ruby arrays have a slice method. You can also get a slice in Ruby by using [START..END] or in Python via [START:END] . However, in these languages, a slice is actually a new array with the values of the original copied over. If we take Ruby, what's the output of the following?

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00229))_

```
func extractPowers(saiyans []*Saiyan) []int {
  powers := make([]int, 0, len(saiyans))
  for _, saiyan := range saiyans {
    powers = append(powers, saiyan.Power)
  }
  return powers
}
```

### Technical frame 6: Chapter 3 - Maps, Arrays and Slices / Slices

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00234))_

> The [X:Y] syntax creates a slice of scores , starting from index 2 up until (but not including) index 4. However, unlike the Ruby example above, the Go code will produce an output of [1, 2, 999, 4, 5] . This is because our slice is really just a window into scores .

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00231))_

```
scores = [1,2,3,4,5]
slice = scores[2..4]
slice[0] = 999
puts scores
```

### Technical frame 7: Chapter 3 - Maps, Arrays and Slices / Slices

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00239))_

> We can see from the above example, that [X:] is shorthand for from X to the end while [:X] is shorthand for from the start up until X . Unlike other languages, Go doesn't support negative values. If we want all of the values of a slice except the last, we do:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00238))_

```
strings.Index(haystack[5:], " ")
```

### Technical frame 8: Chapter 3 - Maps, Arrays and Slices / Slices

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00244))_

> Finally, now that we know about slices, we can look at another commonly used built-in function: copy . copy is one of those functions that highlights how slices change the way we code. Normally, a method that copies values from one array to another has 5 parameters: source , sourceStart , count , destination and destinationStart . With slices, we only need two:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00240))_

```
scores := []int{1, 2, 3, 4, 5}
scores = scores[:len(scores)-1]
```


## Related pages

- [[coding-little-go-book-slice]] - shared statements and technical atoms: Slice shares source evidence from Chapter 3 - Maps, Arrays and Slices / Slices: Slices as wrappers to arrays is a powerful concept. Many languages have the concept of slicing an array. Both JavaScript and Ruby arrays have a slice method. You can ... [truncated]; Slice shares technical record from Chapter 3 - Maps, Arrays and Slices / Slices: Even when you know the size, append can be used. (1 shared statement(s), 5 shared atom(s))
- [[coding-little-go-book-array]] - shared statements and technical atoms: Array shares source evidence from Chapter 3 - Maps, Arrays and Slices / Arrays: If you come from Python, Ruby, Perl, JavaScript or PHP (and more), you're probably used to programming with dynamic arrays . These are arrays that resize themselves ... [truncated]; Array shares technical record from Chapter 3 - Maps, Arrays and Slices / Arrays: var scores [10]int scores[0] = 339 (1 shared statement(s), 4 shared atom(s))
- [[coding-little-go-book-ruby]] - shared statements and technical atoms: Ruby shares source evidence from Chapter 1 - The Basics / Garbage Collected: Languages with garbage collectors (e.g., Ruby, Python, Java, JavaScript, C#, Go) are able to keep track of these and free them when they're no longer used. Garbage c ... [truncated]; Ruby shares technical record from Chapter 3 - Maps, Arrays and Slices / Arrays: var scores [10]int scores[0] = 339 (1 shared statement(s), 4 shared atom(s))
- [[coding-little-go-book-value]] - shared technical atoms: Value shares technical record from Chapter 3 - Maps, Arrays and Slices / Slices: Even when you know the size, append can be used. (5 shared atom(s))
- [[coding-little-go-book-change]] - shared technical atoms: Change shares technical record from Introduction: I've always had a love-hate relationship when it comes to learning new languages. (1 shared atom(s))
- [[coding-little-go-book-copy]] - shared technical atoms: Copy shares technical record from Chapter 3 - Maps, Arrays and Slices / Slices: scores = [1,2,3,4,5] slice = scores[2..4] slice[0] = 999 puts scores (1 shared atom(s))
- [[coding-little-go-book-inheritance]] - shared technical atoms: Inheritance shares technical record from Chapter 2 - Structures / Composition: public class Person { private String name; public String getName() { return this.name; } } public class Saiyan { // Saiyan is said to have a person private Person pe ... [truncated] (1 shared atom(s))
- [[coding-little-go-book-structure]] - shared technical atoms: Structure shares technical record from Chapter 2 - Structures / Composition: public class Person { private String name; public String getName() { return this.name; } } public class Saiyan { // Saiyan is said to have a person private Person pe ... [truncated] (1 shared atom(s))
- [[coding-little-go-book-version]] - shared technical atoms: Version shares technical record from Chapter 3 - Maps, Arrays and Slices / Slices: Even when you know the size, append can be used. (1 shared atom(s))
- [[coding-little-go-book-garbage]] - shared statements: Garbage shares source evidence from Chapter 1 - The Basics / Garbage Collected: Languages with garbage collectors (e.g., Ruby, Python, Java, JavaScript, C#, Go) are able to keep track of these and free them when they're no longer used. Garbage c ... [truncated] (1 shared statement(s))
- [[coding-little-go-book-saying]] - shared statements: Saying shares source evidence from Chapter 1 - The Basics / C-Like Syntax: Saying that a language has a C-like syntax means that if you're used to any other C-like languages such as C, C++, Java, JavaScript and C#, then you're going to find ... [truncated] (1 shared statement(s))
- [[coding-little-go-book-system]] - shared statements: System shares source evidence from Chapter 1 - The Basics / Before You Continue: If you're coming from a dynamic language, the complexity around types and declarations might seem like a step backwards. I don't disagree with you. For some systems, ... [truncated] (1 shared statement(s))

## Source

- [[coding-little-go-book]]
