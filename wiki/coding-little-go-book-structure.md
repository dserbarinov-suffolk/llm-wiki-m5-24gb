---
page_id: coding-little-go-book-structure
page_kind: concept
summary: Structures: 57 statement(s) and 21 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-29
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-structure@6bf9bf37885e9fdf30e8b598323d22fb
---

# Structures

What [[coding-little-go-book]] covers about structures:

## Statements

### Chapter 2 - Structures

- Go isn't an object-oriented (OO) language like C++, Java, Ruby and C#. It doesn't have objects nor inheritance and thus, doesn't have the many concepts associated with OO such as polymorphism and overloading. _(coding_little_go_book.pdf (source-range-23d24eb1-00111))_

- What Go does have are structures, which can be associated with methods. Go also supports a simple but effective form of composition. Overall, it results in simpler code, but there'll be occasions where you'll miss some of what OO has to offer. (It's worth pointing out that composition over inheritance is an old battle cry and Go is the first language I've used that takes a firm stand on the issue.) _(coding_little_go_book.pdf (source-range-23d24eb1-00112))_

- Although Go doesn't do OO like you may be used to, you'll notice a lot of similarities between the definition of a structure and that of a class. A simple example is the following Saiyan structure: _(coding_little_go_book.pdf (source-range-23d24eb1-00113))_

- We'll soon see how to add a method to this structure, much like you'd have methods as part of a class. Before we do that, we have to dive back into declarations. _(coding_little_go_book.pdf (source-range-23d24eb1-00115))_

### Chapter 2 - Structures / Declarations and Initializations

- When we first looked at variables and declarations, we looked only at built-in types, like integers and strings. Now that we're talking about structures, we need to expand that conversation to include pointers. _(coding_little_go_book.pdf (source-range-23d24eb1-00117))_

- Note: The trailing , in the above structure is required. Without it, the compiler will give an error. You'll appreciate the required consistency, especially if you've used a language or format that enforces the opposite. _(coding_little_go_book.pdf (source-range-23d24eb1-00120))_

- We don't have to set all or even any of the fields. Both of these are valid: _(coding_little_go_book.pdf (source-range-23d24eb1-00121))_

- Just like unassigned variables have a zero value, so do fields. _(coding_little_go_book.pdf (source-range-23d24eb1-00123))_

- Furthermore, you can skip the field name and rely on the order of the field declarations (though for the sake of clarity, you should only do this for structures with few fields): _(coding_little_go_book.pdf (source-range-23d24eb1-00124))_

- What all of the above examples do is declare a variable goku and assign a value to it. _(coding_little_go_book.pdf (source-range-23d24eb1-00126))_

- Many times though, we don't want a variable that is directly associated with our value but rather a variable that has a pointer to our value. A pointer is a memory address; it's the location of where to find the actual value. It's a level of indirection. Loosely, it's the difference between being at a house and having directions to the house. _(coding_little_go_book.pdf (source-range-23d24eb1-00127))_

- The answer is 9000, not 19000. Why? Because Super made changes to a copy of our original goku value and thus, changes made in Super weren't reflected in the caller. To make this work as you probably expect, we need to pass a pointer to our value: _(coding_little_go_book.pdf (source-range-23d24eb1-00130))_

- We made two changes. The first is the use of the & operator to get the address of our value (it's called the address of operator). Next, we changed the type of parameter Super expects. It used to expect a value of type Saiyan but now expects an address of type *Saiyan , where *X means pointer to value of type X . There's obviously some relation between the types Saiyan and *Saiyan , but they are two distinct types. _(coding_little_go_book.pdf (source-range-23d24eb1-00132))_

- Note that we're still passing a copy of goku's value to Super it just so happens that goku's value has become an address. That copy is the same address as the original, which is what that indirection buys us. Think of it as copying the directions to a restaurant. What you have is a copy, but it still points to the same restaurant as the original. _(coding_little_go_book.pdf (source-range-23d24eb1-00133))_

- The above, once again, prints 9000. This is how many languages behave, including Ruby, Python, Java and C#. Go, and to some degree C#, simply make the fact visible. _(coding_little_go_book.pdf (source-range-23d24eb1-00136))_

- It should also be obvious that copying a pointer is going to be cheaper than copying a complex structure. On a 64-bit machine, a pointer is 64 bits large. If we have a structure with many fields, creating copies can be expensive. The real value of pointers though is that they let you share values. Do we want Super to alter a copy of goku or alter the shared goku value itself? _(coding_little_go_book.pdf (source-range-23d24eb1-00137))_

- All this isn't to say that you'll always want a pointer. At the end of this chapter, after we've seen a bit more of what we can do with structures, we'll re-examine the pointer-versus-value question. _(coding_little_go_book.pdf (source-range-23d24eb1-00138))_

### Chapter 2 - Structures / Functions on Structures

- In the above code, we say that the type *Saiyan is the receiver of the Super method. We call Super like so: _(coding_little_go_book.pdf (source-range-23d24eb1-00142))_

### Chapter 2 - Structures / Constructors

- Structures don't have constructors. Instead, you create a function that returns an instance of the desired type (like a factory): _(coding_little_go_book.pdf (source-range-23d24eb1-00145))_

- This pattern rubs a lot of developers the wrong way. On the one hand, it's a pretty slight syntactical change; on the other, it does feel a little less compartmentalized. _(coding_little_go_book.pdf (source-range-23d24eb1-00147))_

### Chapter 2 - Structures / New

- Which you use is up to you, but you'll find that most people prefer the latter whenever they have fields to initialize, since it tends to be easier to read: _(coding_little_go_book.pdf (source-range-23d24eb1-00153))_

### Chapter 2 - Structures / Fields of a Structure

- In the example that we've seen so far, Saiyan has two fields Name and Power of types string and int , respectively. Fields can be of any type -including other structures and types that we haven't explored yet such as arrays, maps, interfaces and functions. _(coding_little_go_book.pdf (source-range-23d24eb1-00157))_

### Chapter 2 - Structures / Composition

- Go supports composition, which is the act of including one structure into another. In some languages, this is called a trait or a mixin. Languages that don't have an explicit composition mechanism can always do it the long way. In Java, there's the possibility to extend structures with inheritance but, in a scenario where this is not an option, a mixin would be written like this: _(coding_little_go_book.pdf (source-range-23d24eb1-00160))_

- This can get pretty tedious. Every method of Person needs to be duplicated in Saiyan . Go avoids this tediousness: _(coding_little_go_book.pdf (source-range-23d24eb1-00162))_

- Both of the above will print "Goku". _(coding_little_go_book.pdf (source-range-23d24eb1-00166))_

- Is composition better than inheritance? Many people think that it's a more robust way to share code. When using inheritance, your class is tightly coupled to your superclass and you end up focusing on hierarchy rather than behavior. _(coding_little_go_book.pdf (source-range-23d24eb1-00167))_

### Chapter 2 - Structures / Composition / Overloading

- The composed version is always available via s.Person.Introduce() . _(coding_little_go_book.pdf (source-range-23d24eb1-00172))_

### Chapter 2 - Structures / Pointers versus Values

- As you write Go code, it's natural to ask yourself should this be a value, or a pointer to a value? There are two pieces of good news. First, the answer is the same regardless of which of the following we're talking about: _(coding_little_go_book.pdf (source-range-23d24eb1-00174))_

- Secondly, if you aren't sure, use a pointer. _(coding_little_go_book.pdf (source-range-23d24eb1-00180))_

- As we already saw, passing values is a great way to make data immutable (changes that a function makes to it won't be reflected in the calling code). Sometimes, this is the behavior that you'll want but sometimes not. _(coding_little_go_book.pdf (source-range-23d24eb1-00181))_

- Again, these are all pretty subtle cases. Unless you're iterating over thousands or possibly tens of thousands of such points, you wouldn't notice a difference. _(coding_little_go_book.pdf (source-range-23d24eb1-00185))_

### Chapter 2 - Structures / Before You Continue

- From a practical point of view, this chapter introduced structures, how to make an instance of a structure a receiver of a function, and added pointers to our existing knowledge of Go's type system. The following chapters will build on what we know about structures as well as the inner workings that we've explored. _(coding_little_go_book.pdf (source-range-23d24eb1-00187))_


## Technical atoms

### Technical frame 1: Chapter 2 - Structures

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00115))_

> We'll soon see how to add a method to this structure, much like you'd have methods as part of a class. Before we do that, we have to dive back into declarations.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00114))_

```
type Saiyan struct {
  Name string
  Power int
}
```

### Technical frame 2: Chapter 2 - Structures / Declarations and Initializations

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00120))_

> Note: The trailing , in the above structure is required. Without it, the compiler will give an error. You'll appreciate the required consistency, especially if you've used a language or format that enforces the opposite.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00119))_

```
goku := Saiyan{
  Name: "Goku",
  Power: 9000,
}
```

### Technical frame 3: Chapter 2 - Structures / Declarations and Initializations

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00121))_

> We don't have to set all or even any of the fields. Both of these are valid:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00120))_

> You'll appreciate the required consistency, especially if you've used a language or format that enforces the opposite.

### Technical frame 4: Chapter 2 - Structures / Declarations and Initializations

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00123))_

> Just like unassigned variables have a zero value, so do fields.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00122))_

```
goku := Saiyan{}
// or
goku := Saiyan{Name: "Goku"}
goku.Power = 9000
```

### Technical frame 5: Chapter 2 - Structures / Declarations and Initializations

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00126))_

> What all of the above examples do is declare a variable goku and assign a value to it.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00125))_

```
goku := Saiyan{"Goku", 9000}
```

### Technical frame 6: Chapter 2 - Structures / Declarations and Initializations

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00130))_

> The answer is 9000, not 19000. Why? Because Super made changes to a copy of our original goku value and thus, changes made in Super weren't reflected in the caller. To make this work as you probably expect, we need to pass a pointer to our value:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00129))_

```
func main() {
  goku := Saiyan{"Goku", 9000}
  Super(goku)
  fmt.Println(goku.Power)
}
func Super(s Saiyan) {
  s.Power += 10000
}
```

### Technical frame 7: Chapter 2 - Structures / Declarations and Initializations

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00132))_

> We made two changes. The first is the use of the & operator to get the address of our value (it's called the address of operator). Next, we changed the type of parameter Super expects. It used to expect a value of type Saiyan but now expects an address of type *Saiyan , where *X means pointer to value of type X . There's obviously some relation between the types Saiyan and *Saiyan , but they are two distinct types.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00131))_

```
func main() {
  goku := &Saiyan{"Goku", 9000}
  Super(goku)
  fmt.Println(goku.Power)
}
func Super(s *Saiyan) {
  s.Power += 10000
}
```

### Technical frame 8: Chapter 2 - Structures / Declarations and Initializations

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00136))_

> The above, once again, prints 9000. This is how many languages behave, including Ruby, Python, Java and C#. Go, and to some degree C#, simply make the fact visible.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00135))_

```
func main() {
  goku := &Saiyan{"Goku", 9000}
  Super(goku)
  fmt.Println(goku.Power)
}
func Super(s *Saiyan) {
  s = &Saiyan{"Gohan", 1000}
}
```

### Technical frame 9: Chapter 2 - Structures / Functions on Structures

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00142))_

> In the above code, we say that the type *Saiyan is the receiver of the Super method. We call Super like so:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00141))_

```
type Saiyan struct {
  Name string
  Power int
}
func (s *Saiyan) Super() {
  s.Power += 10000
}
```

### Technical frame 10: Chapter 2 - Structures / Functions on Structures

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00142))_

> In the above code, we say that the type *Saiyan is the receiver of the Super method. We call Super like so:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00143))_

```
goku := &Saiyan{"Goku", 9001}
goku.Super()
fmt.Println(goku.Power) // will print 19001
```

### Technical frame 11: Chapter 2 - Structures / Constructors

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

### Technical frame 12: Chapter 2 - Structures / Constructors

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00147))_

> This pattern rubs a lot of developers the wrong way. On the one hand, it's a pretty slight syntactical change; on the other, it does feel a little less compartmentalized.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00149))_

```
func NewSaiyan(name string, power int) Saiyan {
  return Saiyan{
    Name: name,
    Power: power,
  }
}
```

### Technical frame 13: Chapter 2 - Structures / New

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00153))_

> Which you use is up to you, but you'll find that most people prefer the latter whenever they have fields to initialize, since it tends to be easier to read:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00152))_

```
goku := new(Saiyan)
// same as
goku := &Saiyan{}
```

### Technical frame 14: Chapter 2 - Structures / New

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00153))_

> Which you use is up to you, but you'll find that most people prefer the latter whenever they have fields to initialize, since it tends to be easier to read:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00154))_

```
goku := new(Saiyan)
goku.Name = "goku"
goku.Power = 9001
//vs
goku := &Saiyan {
  Name: "goku",
  Power: 9000,
}
```

### Technical frame 15: Chapter 2 - Structures / New

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00153))_

> Which you use is up to you, but you'll find that most people prefer the latter whenever they have fields to initialize, since it tends to be easier to read:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00155))_

> Whichever approach you choose, if you follow the factory pattern above, you can shield the rest of your code from knowing and worrying about any of the allocation details.

### Technical frame 16: Chapter 2 - Structures / Fields of a Structure

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00157))_

> In the example that we've seen so far, Saiyan has two fields Name and Power of types string and int , respectively. Fields can be of any type -including other structures and types that we haven't explored yet such as arrays, maps, interfaces and functions.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00158))_

```
For example, we could expand our deﬁnition of Saiyan:
type Saiyan struct {
  Name string
  Power int
  Father *Saiyan
}
which we'd initialize via:
gohan := &Saiyan{
  Name: "Gohan",
  Power: 1000,
  Father: &Saiyan {
    Name: "Goku",
    Power: 9001,
    Father: nil,
  },
}
```

### Technical frame 17: Chapter 2 - Structures / Composition

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

### Technical frame 18: Chapter 2 - Structures / Composition

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

### Technical frame 19: Chapter 2 - Structures / Composition

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

### Technical frame 20: Chapter 2 - Structures / Composition / Overloading

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00172))_

> The composed version is always available via s.Person.Introduce() .

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00171))_

```
func (s *Saiyan) Introduce() {
  fmt.Printf("Hi, I'm %s. Ya!\n", s.Name)
}
```

### Technical frame 21: Chapter 2 - Structures / Pointers versus Values

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00185))_

> Again, these are all pretty subtle cases. Unless you're iterating over thousands or possibly tens of thousands of such points, you wouldn't notice a difference.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00183))_

```
type Point struct {
  X int
  Y int
}
```


## Related pages

- [[coding-little-go-book-declaration-and-initialization]] - shared statements and technical atoms: Declarations and Initializations shares source evidence from Chapter 2 - Structures / Declarations and Initializations: When we first looked at variables and declarations, we looked only at built-in types, like integers and strings. Now that we're talking about structures, we need to ... [truncated]; Declarations and Initializations shares technical record from Chapter 2 - Structures / Declarations and Initializations: goku := Saiyan{ Name: "Goku", Power: 9000, } (27 shared statement(s), 7 shared atom(s))
- [[coding-little-go-book-composition]] - shared statements and technical atoms: Composition shares source evidence from Chapter 2 - Structures / Composition: Go supports composition, which is the act of including one structure into another. In some languages, this is called a trait or a mixin. Languages that don't have an ... [truncated]; Composition shares technical record from Chapter 2 - Structures / Composition: public class Person { private String name; public String getName() { return this.name; } } public class Saiyan { // Saiyan is said to have a person private Person pe ... [truncated] (9 shared statement(s), 4 shared atom(s))
- [[coding-little-go-book-value]] - shared statements and technical atoms: Value shares source evidence from Chapter 2 - Structures / Declarations and Initializations: The answer is 9000, not 19000. Why? Because Super made changes to a copy of our original goku value and thus, changes made in Super weren't reflected in the caller. ... [truncated]; Value shares technical record from Chapter 2 - Structures / Declarations and Initializations: goku := Saiyan{ Name: "Goku", Power: 9000, } (4 shared statement(s), 5 shared atom(s))
- [[coding-little-go-book-code]] - shared statements and technical atoms: Code shares source evidence from Chapter 2 - Structures: What Go does have are structures, which can be associated with methods. Go also supports a simple but effective form of composition. Overall, it results in simpler c ... [truncated]; Code shares technical record from Chapter 2 - Structures / Functions on Structures: type Saiyan struct { Name string Power int } func (s *Saiyan) Super() { s.Power += 10000 } (2 shared statement(s), 3 shared atom(s))
- [[coding-little-go-book-language]] - shared statements and technical atoms: Language shares source evidence from Chapter 2 - Structures / Composition: Go supports composition, which is the act of including one structure into another. In some languages, this is called a trait or a mixin. Languages that don't have an ... [truncated]; Language shares technical record from Chapter 2 - Structures / Composition: public class Person { private String name; public String getName() { return this.name; } } public class Saiyan { // Saiyan is said to have a person private Person pe ... [truncated] (2 shared statement(s), 1 shared atom(s))
- [[coding-little-go-book-section-chapter-2-structures-59a89c52]] - source section: Chapter 2 - Structures shares source evidence from Chapter 2 - Structures: Go isn't an object-oriented (OO) language like C++, Java, Ruby and C#. It doesn't have objects nor inheritance and thus, doesn't have the many concepts associated wi ... [truncated]; Chapter 2 - Structures shares technical record from Chapter 2 - Structures: type Saiyan struct { Name string Power int } (57 shared statement(s), 21 shared atom(s))

## Source

- [[coding-little-go-book]]
