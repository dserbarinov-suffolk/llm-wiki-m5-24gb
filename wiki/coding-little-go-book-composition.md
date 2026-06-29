---
page_id: coding-little-go-book-composition
page_kind: concept
summary: Composition: 9 statement(s) and 4 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-29
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-composition@01db5df9b725f3819e3f9ab3ba24d70b
---

# Composition

What [[coding-little-go-book]] covers about composition:

## Statements

### Chapter 2 - Structures / Composition

- Go supports composition, which is the act of including one structure into another. In some languages, this is called a trait or a mixin. Languages that don't have an explicit composition mechanism can always do it the long way. In Java, there's the possibility to extend structures with inheritance but, in a scenario where this is not an option, a mixin would be written like this: _(coding_little_go_book.pdf (source-range-23d24eb1-00160))_

- This can get pretty tedious. Every method of Person needs to be duplicated in Saiyan . Go avoids this tediousness: _(coding_little_go_book.pdf (source-range-23d24eb1-00162))_

- Both of the above will print "Goku". _(coding_little_go_book.pdf (source-range-23d24eb1-00166))_

- Is composition better than inheritance? Many people think that it's a more robust way to share code. When using inheritance, your class is tightly coupled to your superclass and you end up focusing on hierarchy rather than behavior. _(coding_little_go_book.pdf (source-range-23d24eb1-00167))_

### Chapter 2 - Structures / Composition / Overloading

- The composed version is always available via s.Person.Introduce() . _(coding_little_go_book.pdf (source-range-23d24eb1-00172))_


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

### Technical frame 2: Chapter 2 - Structures / Composition

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00166))_

> Both of the above will print "Goku".

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00163))_

```
type Person struct {
  Name string
}
func (p *Person) Introduce() {
  fmt.Printf("Hi, I'm %s\n", p.Name)
}
type Saiyan struct {
  *Person
  Power int
}
// and to use it:
goku := &Saiyan{
  Person: &Person{"Goku"},
  Power: 9001,
}
goku.Introduce()
```

### Technical frame 3: Chapter 2 - Structures / Composition

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00166))_

> Both of the above will print "Goku".

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00165))_

```
goku := &Saiyan{
  Person: &Person{"Goku"},
}
fmt.Println(goku.Name)
fmt.Println(goku.Person.Name)
```

### Technical frame 4: Chapter 2 - Structures / Composition / Overloading

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00172))_

> The composed version is always available via s.Person.Introduce() .

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00171))_

```
func (s *Saiyan) Introduce() {
  fmt.Printf("Hi, I'm %s. Ya!\n", s.Name)
}
```


## Related pages

- [[coding-little-go-book-structure]] - shared statements and technical atoms: Structures shares source evidence from Chapter 2 - Structures / Composition: Go supports composition, which is the act of including one structure into another. In some languages, this is called a trait or a mixin. Languages that don't have an ... [truncated]; Structures shares technical record from Chapter 2 - Structures / Composition: public class Person { private String name; public String getName() { return this.name; } } public class Saiyan { // Saiyan is said to have a person private Person pe ... [truncated] (9 shared statement(s), 4 shared atom(s))
- [[coding-little-go-book-language]] - shared statements and technical atoms: Language shares source evidence from Chapter 2 - Structures / Composition: Go supports composition, which is the act of including one structure into another. In some languages, this is called a trait or a mixin. Languages that don't have an ... [truncated]; Language shares technical record from Chapter 2 - Structures / Composition: public class Person { private String name; public String getName() { return this.name; } } public class Saiyan { // Saiyan is said to have a person private Person pe ... [truncated] (2 shared statement(s), 1 shared atom(s))
- [[coding-little-go-book-section-chapter-2-structures-composition-06f1b349]] - source section: Chapter 2 - Structures / Composition shares source evidence from Chapter 2 - Structures / Composition: Go supports composition, which is the act of including one structure into another. In some languages, this is called a trait or a mixin. Languages that don't have an ... [truncated]; Chapter 2 - Structures / Composition shares technical record from Chapter 2 - Structures / Composition: public class Person { private String name; public String getName() { return this.name; } } public class Saiyan { // Saiyan is said to have a person private Person pe ... [truncated] (9 shared statement(s), 4 shared atom(s))

## Source

- [[coding-little-go-book]]
