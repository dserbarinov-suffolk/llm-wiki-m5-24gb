---
page_id: coding-little-go-book-inheritance
page_kind: concept
summary: Inheritance: 4 statement(s) and 1 atom(s) from raw/coding_little_go_book.pdf.
page_family: topic-concept
sources: raw/coding_little_go_book.pdf
updated: 2026-06-30
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-inheritance@ea9deeec8de19dab5a847de27ce177bb
---

# Inheritance

What [[coding-little-go-book]] covers about inheritance:

## Statements

### Chapter 2 - Structures

- What Go does have are structures, which can be associated with methods. Go also supports a simple but effective form of composition. Overall, it results in simpler code, but there'll be occasions where you'll miss some of what OO has to offer. (It's worth pointing out that composition over inheritance is an old battle cry and Go is the first language I've used that takes a firm stand on the issue.) _(coding_little_go_book.pdf (source-range-23d24eb1-00112))_

### Chapter 2 - Structures / Composition

- Go supports composition, which is the act of including one structure into another. In some languages, this is called a trait or a mixin. Languages that don't have an explicit composition mechanism can always do it the long way. In Java, there's the possibility to extend structures with inheritance but, in a scenario where this is not an option, a mixin would be written like this: _(coding_little_go_book.pdf (source-range-23d24eb1-00160))_

- Is composition better than inheritance? Many people think that it's a more robust way to share code. When using inheritance, your class is tightly coupled to your superclass and you end up focusing on hierarchy rather than behavior. _(coding_little_go_book.pdf (source-range-23d24eb1-00167))_

### Chapter 5 - Tidbits / Empty Interface and Conversions

- In most object-oriented languages, a built-in base class, often named object , is the superclass for all other classes. Go, having no inheritance, doesn't have such a superclass. What it does have is an empty interface with no methods: interface{} . Since every type implements all 0 of the empty interface's methods, and since interfaces are implicitly implemented, every type fulfills the contract of the empty interface. _(coding_little_go_book.pdf (source-range-23d24eb1-00368))_


## Technical atoms

### Technical frame 1: Chapter 2 - Structures / Composition

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


## Related pages

- [[coding-little-go-book-structure]] - shared statements and technical atoms: Structure shares source evidence from Chapter 2 - Structures / Composition: Go supports composition, which is the act of including one structure into another. In some languages, this is called a trait or a mixin. Languages that don't have an ... [truncated]; Structure shares technical record from Chapter 2 - Structures / Composition: public class Person { private String name; public String getName() { return this.name; } } public class Saiyan { // Saiyan is said to have a person private Person pe ... [truncated] (1 shared statement(s), 1 shared atom(s))
- [[coding-little-go-book-language]] - shared technical atoms: Language shares technical record from Chapter 2 - Structures / Composition: public class Person { private String name; public String getName() { return this.name; } } public class Saiyan { // Saiyan is said to have a person private Person pe ... [truncated] (1 shared atom(s))

## Source

- [[coding-little-go-book]]
