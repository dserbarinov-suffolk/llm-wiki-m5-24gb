---
page_id: coding-little-go-book-section-chapter-2-structures-composition-06f1b349
page_kind: source
summary: Chapter 2 - Structures / Composition: 16 source-backed entries and 2 atom(s) from raw/coding_little_go_book.pdf.
page_family: section-reference
sources: raw/coding_little_go_book.pdf
updated: 2026-06-30
domain: coding-little-go-book
category_path: sources/coding-little-go-book/sections
source_id: coding_little_go_book.pdf
projection_coverage: section-coding-little-go-book-section-chapter-2-structures-composition-06f1b349@71b2d67756ec5c0f3e178fd61457ae01
---

# Chapter 2 - Structures / Composition

From [[coding-little-go-book]].

## Related pages

- [[coding-little-go-book-section-chapter-2-structures-59a89c52]] - broader source section: Chapter 2 - Structures
- [[coding-little-go-book-section-chapter-2-structures-composition-overloading-8c373927]] - narrower source section: Chapter 2 - Structures / Composition / Overloading
- [[coding-little-go-book-section-chapter-2-structures-fields-of-a-structure-bd0d428b]] - previous source section: Chapter 2 - Structures / Fields of a Structure
- [[coding-little-go-book-section-chapter-2-structures-pointers-versus-values-a51ed683]] - next source section: Chapter 2 - Structures / Pointers versus Values

## Statements

- Go supports composition, which is the act of including one structure into another. In some languages, this is called a trait or a mixin. Languages that don't have an explicit composition mechanism can always do it the long way. In Java, there's the possibility to extend structures with inheritance but, in a scenario where this is not an option, a mixin would be written like this: _(coding_little_go_book.pdf (source-range-23d24eb1-00160))_
- This can get pretty tedious. Every method of Person needs to be duplicated in Saiyan . Go avoids this tediousness: _(coding_little_go_book.pdf (source-range-23d24eb1-00162))_
- Both of the above will print "Goku". _(coding_little_go_book.pdf (source-range-23d24eb1-00166))_
- Is composition better than inheritance? Many people think that it's a more robust way to share code. When using inheritance, your class is tightly coupled to your superclass and you end up focusing on hierarchy rather than behavior. _(coding_little_go_book.pdf (source-range-23d24eb1-00167))_
- In some languages, this is called a trait or a mixin. _(coding_little_go_book.pdf (source-range-23d24eb1-00160))_

## Statements by subsection

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

### Technical frame 2: Chapter 2 - Structures / Composition / Overloading

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00172))_

> The composed version is always available via s.Person.Introduce() .

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00171))_

```
func (s *Saiyan) Introduce() {
  fmt.Printf("Hi, I'm %s. Ya!\n", s.Name)
}
```
