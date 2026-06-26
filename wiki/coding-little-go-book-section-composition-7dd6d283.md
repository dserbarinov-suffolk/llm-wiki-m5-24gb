---
page_id: coding-little-go-book-section-composition-7dd6d283
page_kind: source
summary: Composition: 13 source-backed entries and 4 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: sources/coding-little-go-book/sections
source_id: coding_little_go_book.pdf
projection_coverage: section-coding-little-go-book-section-composition-7dd6d283@ae3f02df9043fb22392bc95cff6af694
---

# Composition

From [[coding-little-go-book]].

## Statements

- Languages that don't have an explicit composition mechanism can always do it the long way. _(coding_little_go_book.pdf (source-range-773b6275-00160))_
- In some languages, this is called a trait or a mixin. _(coding_little_go_book.pdf (source-range-773b6275-00160))_
- In Java, there's the possibility to extend structures with inheritance but, in a scenario where this is not an option, a mixin would be written like this: _(coding_little_go_book.pdf (source-range-773b6275-00160))_
- Go supports composition, which is the act of including one structure into another. _(coding_little_go_book.pdf (source-range-773b6275-00160))_
- In some languages, this is called a trait or a mixin. _(coding_little_go_book.pdf (source-range-773b6275-00160))_
- This can get pretty tedious. _(coding_little_go_book.pdf (source-range-773b6275-00162))_
- Every method of Person needs to be duplicated in Saiyan . _(coding_little_go_book.pdf (source-range-773b6275-00162))_
- Both of the above will print "Goku". _(coding_little_go_book.pdf (source-range-773b6275-00166))_
- When using inheritance, your class is tightly coupled to your superclass and you end up focusing on hierarchy rather than behavior. _(coding_little_go_book.pdf (source-range-773b6275-00167))_

## Technical atoms

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
_(source: coding_little_go_book.pdf (source-range-773b6275-00163))_

> The Saiyan structure has a field of type *Person . Because we didn't give it an explicit field name, we can implicitly access the fields and functions of the composed type. However, the Go compiler did give it a field name, consider the perfectly valid:
_(source: coding_little_go_book.pdf (source-range-773b6275-00164))_

```
goku := &Saiyan{
  Person: &Person{"Goku"},
}
fmt.Println(goku.Name)
fmt.Println(goku.Person.Name)
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00165))_
