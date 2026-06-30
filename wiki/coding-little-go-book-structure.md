---
page_id: coding-little-go-book-structure
page_kind: concept
summary: Structure: 7 statement(s) and 12 atom(s) from raw/coding_little_go_book.pdf.
page_family: topic-concept
sources: raw/coding_little_go_book.pdf
updated: 2026-06-30
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-structure@52aee2171f5a4238449b7f086b7cf690
---

# Structure

What [[coding-little-go-book]] covers about structure:

## Statements

### Chapter 2 - Structures / Declarations and Initializations

- When we first looked at variables and declarations, we looked only at built-in types, like integers and strings. Now that we're talking about structures, we need to expand that conversation to include pointers. _(coding_little_go_book.pdf (source-range-23d24eb1-00117))_

- Note: The trailing , in the above structure is required. Without it, the compiler will give an error. You'll appreciate the required consistency, especially if you've used a language or format that enforces the opposite. _(coding_little_go_book.pdf (source-range-23d24eb1-00120))_

### Chapter 2 - Structures / Constructors

- Structures don't have constructors. Instead, you create a function that returns an instance of the desired type (like a factory): _(coding_little_go_book.pdf (source-range-23d24eb1-00145))_

### Chapter 2 - Structures / Composition

- Go supports composition, which is the act of including one structure into another. In some languages, this is called a trait or a mixin. Languages that don't have an explicit composition mechanism can always do it the long way. In Java, there's the possibility to extend structures with inheritance but, in a scenario where this is not an option, a mixin would be written like this: _(coding_little_go_book.pdf (source-range-23d24eb1-00160))_

### Chapter 4 - Code Organization and Interfaces / Packages / Visibility

- This also applies to structure fields. If a structure field name starts with a lowercase letter, only code within the same package will be able to access them. _(coding_little_go_book.pdf (source-range-23d24eb1-00300))_

### Chapter 4 - Code Organization and Interfaces / Interfaces

- In a language like C# or Java, we have to be explicit when a class implements an interface: In Go, this happens implicitly. If your structure has a function name Log with a string parameter and no return value, then it can be used as a Logger . This cuts down on the verboseness of using interfaces: } public class ConsoleLogger : Logger { public void Logger(message string) { Console.WriteLine(message) } } type ConsoleLogger struct {} (l ConsoleLogger) Log(message string) { _(coding_little_go_book.pdf (source-range-23d24eb1-00327))_

### Chapter 4 - Code Organization and Interfaces / Before You Continue

- Ultimately, how you structure your code around Go's workspace is something that you'll only feel comfortable with after you've written a couple of non-trivial projects. What's most important for you to remember is the tight relationship between package names and your directory structure (not just within a project, but within the entire workspace). _(coding_little_go_book.pdf (source-range-23d24eb1-00333))_


## Technical atoms

### Technical frame 1: Chapter 2 - Structures / Declarations and Initializations

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00120))_

> Note: The trailing , in the above structure is required. Without it, the compiler will give an error. You'll appreciate the required consistency, especially if you've used a language or format that enforces the opposite.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00119))_

```
goku := Saiyan{
  Name: "Goku",
  Power: 9000,
}
```

### Technical frame 2: Chapter 2 - Structures / Declarations and Initializations

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00121))_

> We don't have to set all or even any of the fields. Both of these are valid:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00120))_

> You'll appreciate the required consistency, especially if you've used a language or format that enforces the opposite.

### Technical frame 3: Chapter 2 - Structures / Declarations and Initializations

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00126))_

> What all of the above examples do is declare a variable goku and assign a value to it.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00125))_

```
goku := Saiyan{"Goku", 9000}
```

### Technical frame 4: Chapter 2 - Structures / Constructors

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00147))_

> This pattern rubs a lot of developers the wrong way. On the one hand, it's a pretty slight syntactical change; on the other, it does feel a little less compartmentalized.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00146))_

```
func NewSaiyan(name string, power int) *Saiyan {
  return &Saiyan{
    Name: name,
    Power: power,
  }
}
```

### Technical frame 5: Chapter 2 - Structures / Composition

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

### Technical frame 6: Chapter 2 - Structures / Composition

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

### Technical frame 7: Chapter 2 - Structures / Composition

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

### Technical frame 8: Chapter 2 - Structures / Composition / Overloading

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00172))_

> The composed version is always available via s.Person.Introduce() .

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00171))_

```
func (s *Saiyan) Introduce() {
  fmt.Printf("Hi, I'm %s. Ya!\n", s.Name)
}
```

### Technical frame 9: Chapter 4 - Code Organization and Interfaces / Interfaces

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00327))_

> In a language like C# or Java, we have to be explicit when a class implements an interface: In Go, this happens implicitly. If your structure has a function name Log with a string parameter and no return value, then it can be used as a Logger . This cuts down on the verboseness of using interfaces: } public class ConsoleLogger : Logger { public void Logger(message string) { Console.WriteLine(message) } } type ConsoleLogger struct {} (l ConsoleLogger) Log(message string) {

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00325))_

```
type Server struct {
  logger Logger
}
```

### Technical frame 10: Chapter 4 - Code Organization and Interfaces / Interfaces

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00327))_

> In a language like C# or Java, we have to be explicit when a class implements an interface: In Go, this happens implicitly. If your structure has a function name Log with a string parameter and no return value, then it can be used as a Logger . This cuts down on the verboseness of using interfaces: } public class ConsoleLogger : Logger { public void Logger(message string) { Console.WriteLine(message) } } type ConsoleLogger struct {} (l ConsoleLogger) Log(message string) {

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00326))_

```
or a function parameter (or return value):
func process(logger Logger) {
  logger.Log("hello!")
```

### Technical frame 11: Chapter 4 - Code Organization and Interfaces / Interfaces

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00329))_

> It also tends to promote small and focused interfaces. The standard library is full of interfaces. The io package has a handful of popular ones such as io.Reader , io.Writer , and io.Closer . If you write a function that expects a parameter that you'll only be calling Close() on, you absolutely should accept an io.Closer rather than whatever concrete type you're using.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00327))_

> In a language like C# or Java, we have to be explicit when a class implements an interface: In Go, this happens implicitly.

### Technical frame 12: Chapter 4 - Code Organization and Interfaces / Interfaces

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00329))_

> It also tends to promote small and focused interfaces. The standard library is full of interfaces. The io package has a handful of popular ones such as io.Reader , io.Writer , and io.Closer . If you write a function that expects a parameter that you'll only be calling Close() on, you absolutely should accept an io.Closer rather than whatever concrete type you're using.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00328))_

```
func (l ConsoleLogger) 
  fmt.Println(message)
}
```


## Related pages

- [[coding-little-go-book-inheritance]] - shared statements and technical atoms: Inheritance shares source evidence from Chapter 2 - Structures / Composition: Go supports composition, which is the act of including one structure into another. In some languages, this is called a trait or a mixin. Languages that don't have an ... [truncated]; Inheritance shares technical record from Chapter 2 - Structures / Composition: public class Person { private String name; public String getName() { return this.name; } } public class Saiyan { // Saiyan is said to have a person private Person pe ... [truncated] (1 shared statement(s), 1 shared atom(s))
- [[coding-little-go-book-note]] - shared statements and technical atoms: Note shares source evidence from Chapter 2 - Structures / Declarations and Initializations: Note: The trailing , in the above structure is required. Without it, the compiler will give an error. You'll appreciate the required consistency, especially if you'v ... [truncated]; Note shares technical record from Chapter 2 - Structures / Declarations and Initializations: goku := Saiyan{ Name: "Goku", Power: 9000, } (1 shared statement(s), 1 shared atom(s))
- [[coding-little-go-book-value]] - shared technical atoms: Value shares technical record from Chapter 2 - Structures / Declarations and Initializations: goku := Saiyan{ Name: "Goku", Power: 9000, } (3 shared atom(s))
- [[coding-little-go-book-compiler]] - shared technical atoms: Compiler shares technical record from Chapter 2 - Structures / Declarations and Initializations: goku := Saiyan{ Name: "Goku", Power: 9000, } (1 shared atom(s))
- [[coding-little-go-book-declaration]] - shared technical atoms: Declaration shares technical record from Chapter 2 - Structures / Declarations and Initializations: goku := Saiyan{"Goku", 9000} (1 shared atom(s))
- [[coding-little-go-book-function]] - shared technical atoms: Function shares technical record from Chapter 4 - Code Organization and Interfaces / Interfaces: func (l ConsoleLogger) fmt.Println(message) } (1 shared atom(s))
- [[coding-little-go-book-interface]] - shared technical atoms: Interface shares technical record from Chapter 4 - Code Organization and Interfaces / Interfaces: func (l ConsoleLogger) fmt.Println(message) } (1 shared atom(s))
- [[coding-little-go-book-language]] - shared technical atoms: Language shares technical record from Chapter 2 - Structures / Composition: public class Person { private String name; public String getName() { return this.name; } } public class Saiyan { // Saiyan is said to have a person private Person pe ... [truncated] (1 shared atom(s))
- [[coding-little-go-book-code]] - shared statements: Code shares source evidence from Chapter 4 - Code Organization and Interfaces / Packages / Visibility: This also applies to structure fields. If a structure field name starts with a lowercase letter, only code within the same package will be able to access them. (2 shared statement(s))
- [[coding-little-go-book-package]] - shared statements: Package shares source evidence from Chapter 4 - Code Organization and Interfaces / Packages / Visibility: This also applies to structure fields. If a structure field name starts with a lowercase letter, only code within the same package will be able to access them. (1 shared statement(s))
- [[coding-little-go-book-you-continue]] - shared statements: Before You Continue shares source evidence from Chapter 4 - Code Organization and Interfaces / Before You Continue: Ultimately, how you structure your code around Go's workspace is something that you'll only feel comfortable with after you've written a couple of non-trivial projec ... [truncated] (1 shared statement(s))
- [[coding-little-go-book-section-chapter-2-structures-59a89c52]] - source section: Chapter 2 - Structures shares source evidence from Chapter 2 - Structures: Go isn't an object-oriented (OO) language like C++, Java, Ruby and C#. It doesn't have objects nor inheritance and thus, doesn't have the many concepts associated wi ... [truncated]; Chapter 2 - Structures shares technical record from Chapter 2 - Structures: type Saiyan struct { Name string Power int } (57 shared statement(s), 21 shared atom(s))

## Source

- [[coding-little-go-book]]
