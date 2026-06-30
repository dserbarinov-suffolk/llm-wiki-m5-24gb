---
page_id: coding-little-go-book-pointer-versus-value
page_kind: concept
summary: Pointers versus Values: 16 statement(s) and 2 atom(s) from raw/coding_little_go_book.pdf.
page_family: topic-concept
sources: raw/coding_little_go_book.pdf
updated: 2026-06-30
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-pointer-versus-value@8752cbc94b45c9799c71884f9b55b917
---

# Pointers versus Values

What [[coding-little-go-book]] covers about pointers versus values:

## Statements

### Chapter 2 - Structures / Declarations and Initializations

- Many times though, we don't want a variable that is directly associated with our value but rather a variable that has a pointer to our value. A pointer is a memory address; it's the location of where to find the actual value. It's a level of indirection. Loosely, it's the difference between being at a house and having directions to the house. _(coding_little_go_book.pdf (source-range-23d24eb1-00127))_

- The answer is 9000, not 19000. Why? Because Super made changes to a copy of our original goku value and thus, changes made in Super weren't reflected in the caller. To make this work as you probably expect, we need to pass a pointer to our value: _(coding_little_go_book.pdf (source-range-23d24eb1-00130))_

- We made two changes. The first is the use of the & operator to get the address of our value (it's called the address of operator). Next, we changed the type of parameter Super expects. It used to expect a value of type Saiyan but now expects an address of type *Saiyan , where *X means pointer to value of type X . There's obviously some relation between the types Saiyan and *Saiyan , but they are two distinct types. _(coding_little_go_book.pdf (source-range-23d24eb1-00132))_

- It should also be obvious that copying a pointer is going to be cheaper than copying a complex structure. On a 64-bit machine, a pointer is 64 bits large. If we have a structure with many fields, creating copies can be expensive. The real value of pointers though is that they let you share values. Do we want Super to alter a copy of goku or alter the shared goku value itself? _(coding_little_go_book.pdf (source-range-23d24eb1-00137))_

- All this isn't to say that you'll always want a pointer. At the end of this chapter, after we've seen a bit more of what we can do with structures, we'll re-examine the pointer-versus-value question. _(coding_little_go_book.pdf (source-range-23d24eb1-00138))_

### Chapter 2 - Structures / Pointers versus Values

- As you write Go code, it's natural to ask yourself should this be a value, or a pointer to a value? There are two pieces of good news. First, the answer is the same regardless of which of the following we're talking about: _(coding_little_go_book.pdf (source-range-23d24eb1-00174))_

- Secondly, if you aren't sure, use a pointer. _(coding_little_go_book.pdf (source-range-23d24eb1-00180))_

- As we already saw, passing values is a great way to make data immutable (changes that a function makes to it won't be reflected in the calling code). Sometimes, this is the behavior that you'll want but sometimes not. _(coding_little_go_book.pdf (source-range-23d24eb1-00181))_

- Again, these are all pretty subtle cases. Unless you're iterating over thousands or possibly tens of thousands of such points, you wouldn't notice a difference. _(coding_little_go_book.pdf (source-range-23d24eb1-00185))_

### Chapter 3 - Maps, Arrays and Slices / Pointers versus Values

- We finished Chapter 2 by looking at whether you should assign and pass pointers or values. We'll now have this same conversation with respect to array and map values. Which of these should you use? _(coding_little_go_book.pdf (source-range-23d24eb1-00266))_

- Many developers think that passing b to, or returning it from, a function is going to be more efficient. However, what's being passed/returned is a copy of the slice, which itself is a reference. So with respect to passing/returning the slice itself, there's no difference. Where you will see a difference is when you modify the values of a slice or map. At this point, the same logic that we saw in Chapter 2 applies. So the decision on whether to define an array of pointers versus an array of values comes down to how you use the individual values, not how you use the array or map itself. _(coding_little_go_book.pdf (source-range-23d24eb1-00268))_


## Technical atoms

### Technical frame 1: Chapter 2 - Structures / Pointers versus Values

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00185))_

> Again, these are all pretty subtle cases. Unless you're iterating over thousands or possibly tens of thousands of such points, you wouldn't notice a difference.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00183))_

```
type Point struct {
  X int
  Y int
}
```

### Technical frame 2: Chapter 3 - Maps, Arrays and Slices / Pointers versus Values

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00268))_

> Many developers think that passing b to, or returning it from, a function is going to be more efficient. However, what's being passed/returned is a copy of the slice, which itself is a reference. So with respect to passing/returning the slice itself, there's no difference. Where you will see a difference is when you modify the values of a slice or map. At this point, the same logic that we saw in Chapter 2 applies. So the decision on whether to define an array of pointers versus an array of valu

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00267))_

```
a := make([]Saiyan, 10)
//or
b := make([]*Saiyan, 10)
```


## Related pages

- [[coding-little-go-book-value]] - broader topic: Value shares source evidence from Chapter 2 - Structures / Declarations and Initializations: It should also be obvious that copying a pointer is going to be cheaper than copying a complex structure. On a 64-bit machine, a pointer is 64 bits large. If we have ... [truncated] (2 shared statement(s))
- [[coding-little-go-book-slice]] - shared statements: Slice shares source evidence from Chapter 3 - Maps, Arrays and Slices / Pointers versus Values: Many developers think that passing b to, or returning it from, a function is going to be more efficient. However, what's being passed/returned is a copy of the slice ... [truncated] (2 shared statement(s))
- [[coding-little-go-book-function]] - shared statements: Function shares source evidence from Chapter 3 - Maps, Arrays and Slices / Pointers versus Values: Many developers think that passing b to, or returning it from, a function is going to be more efficient. However, what's being passed/returned is a copy of the slice ... [truncated] (1 shared statement(s))
- [[coding-little-go-book-section-chapter-2-structures-pointers-versus-values-a51ed683]] - source section: Chapter 2 - Structures / Pointers versus Values shares source evidence from Chapter 2 - Structures / Pointers versus Values: As you write Go code, it's natural to ask yourself should this be a value, or a pointer to a value? There are two pieces of good news. First, the answer is the same ... [truncated]; Chapter 2 - Structures / Pointers versus Values shares technical record from Chapter 2 - Structures / Pointers versus Values: type Point struct { X int Y int } (5 shared statement(s), 1 shared atom(s))
- [[coding-little-go-book-section-chapter-3-maps-arrays-and-slices-pointers-versus-values-61a54414]] - source section: Chapter 3 - Maps, Arrays and Slices / Pointers versus Values shares source evidence from Chapter 3 - Maps, Arrays and Slices / Pointers versus Values: We finished Chapter 2 by looking at whether you should assign and pass pointers or values. We'll now have this same conversation with respect to array and map values ... [truncated]; Chapter 3 - Maps, Arrays and Slices / Pointers versus Values shares technical record from Chapter 3 - Maps, Arrays and Slices / Pointers versus Values: a := make([]Saiyan, 10) //or b := make([]*Saiyan, 10) (5 shared statement(s), 1 shared atom(s))

## Source

- [[coding-little-go-book]]
