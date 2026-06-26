---
page_id: coding-little-go-book-composition
page_kind: concept
summary: Composition: 8 statement(s) and 1 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-composition@3f8ac5dde06129e86d811ef3eacfda5d
---

# Composition

What [[coding-little-go-book]] covers about composition:

## Statements

- Go supports composition, which is the act of including one structure into another. _(coding_little_go_book.pdf (source-range-773b6275-00160))_
- Languages that don't have an explicit composition mechanism can always do it the long way. _(coding_little_go_book.pdf (source-range-773b6275-00160))_
- In some languages, this is called a trait or a mixin. _(coding_little_go_book.pdf (source-range-773b6275-00160))_
- In Java, there's the possibility to extend structures with inheritance but, in a scenario where this is not an option, a mixin would be written like this: _(coding_little_go_book.pdf (source-range-773b6275-00160))_
- This can get pretty tedious. _(coding_little_go_book.pdf (source-range-773b6275-00162))_
- Every method of Person needs to be duplicated in Saiyan . _(coding_little_go_book.pdf (source-range-773b6275-00162))_
- Both of the above will print "Goku". _(coding_little_go_book.pdf (source-range-773b6275-00166))_
- When using inheritance, your class is tightly coupled to your superclass and you end up focusing on hierarchy rather than behavior. _(coding_little_go_book.pdf (source-range-773b6275-00167))_

## Technical atoms

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


## Source

- [[coding-little-go-book]]
