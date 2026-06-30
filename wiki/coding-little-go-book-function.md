---
page_id: coding-little-go-book-function
page_kind: concept
summary: Function: 5 statement(s) and 4 atom(s) from raw/coding_little_go_book.pdf.
page_family: topic-concept
sources: raw/coding_little_go_book.pdf
updated: 2026-06-30
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-function@9a8fc7e2d710a8ca4665320a4afff685
---

# Function

What [[coding-little-go-book]] covers about function:

## Statements

### Chapter 3 - Maps, Arrays and Slices / Pointers versus Values

- Many developers think that passing b to, or returning it from, a function is going to be more efficient. However, what's being passed/returned is a copy of the slice, which itself is a reference. So with respect to passing/returning the slice itself, there's no difference. Where you will see a difference is when you modify the values of a slice or map. At this point, the same logic that we saw in Chapter 2 applies. So the decision on whether to define an array of pointers versus an array of values comes down to how you use the individual values, not how you use the array or map itself. _(coding_little_go_book.pdf (source-range-23d24eb1-00268))_

### Chapter 4 - Code Organization and Interfaces / Packages / Visibility

- it could be called via models.NewItem() . But if the function was named newItem , we wouldn't be able to access it from a different package. _(coding_little_go_book.pdf (source-range-23d24eb1-00303))_

### Chapter 4 - Code Organization and Interfaces / Interfaces

- It also tends to promote small and focused interfaces. The standard library is full of interfaces. The io package has a handful of popular ones such as io.Reader , io.Writer , and io.Closer . If you write a function that expects a parameter that you'll only be calling Close() on, you absolutely should accept an io.Closer rather than whatever concrete type you're using. _(coding_little_go_book.pdf (source-range-23d24eb1-00329))_

### Chapter 4 - Code Organization and Interfaces / Before You Continue

- Finally, if you're new to interfaces, it might take some time before you get a feel for them. However, the first time you see a function that expects something like io.Reader , you'll find yourself thanking the author for not demanding more than he or she needed. _(coding_little_go_book.pdf (source-range-23d24eb1-00335))_

### Chapter 5 - Tidbits / Strings and Byte Arrays

- In fact, this way of converting is common across various types as well. Some functions explicitly expect an int32 or an int64 or their unsigned counterparts. You might find yourself having to do things like: _(coding_little_go_book.pdf (source-range-23d24eb1-00380))_


## Technical atoms

### Technical frame 1: Chapter 4 - Code Organization and Interfaces / Packages / Visibility

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00303))_

> it could be called via models.NewItem() . But if the function was named newItem , we wouldn't be able to access it from a different package.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00302))_

```
func NewItem() *Item {
  // ...
}
```

### Technical frame 2: Chapter 4 - Code Organization and Interfaces / Packages / Visibility

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00303))_

> it could be called via models.NewItem() . But if the function was named newItem , we wouldn't be able to access it from a different package.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00304))_

> For example, if you rename the Item's Price field to price , you should get an error.

### Technical frame 3: Chapter 4 - Code Organization and Interfaces / Interfaces

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00329))_

> It also tends to promote small and focused interfaces. The standard library is full of interfaces. The io package has a handful of popular ones such as io.Reader , io.Writer , and io.Closer . If you write a function that expects a parameter that you'll only be calling Close() on, you absolutely should accept an io.Closer rather than whatever concrete type you're using.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00328))_

```
func (l ConsoleLogger) 
  fmt.Println(message)
}
```

### Technical frame 4: Chapter 5 - Tidbits / Strings and Byte Arrays

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00382))_

> Still, when it comes to bytes and strings, it's probably something you'll end up doing often. Do note that when you use []byte(X) or string(X) , you're creating a copy of the data. This is necessary because strings are immutable.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00381))_

```
int64(count)
```


## Related pages

- [[coding-little-go-book-interface]] - shared technical atoms: Interface shares technical record from Chapter 4 - Code Organization and Interfaces / Interfaces: func (l ConsoleLogger) fmt.Println(message) } (1 shared atom(s))
- [[coding-little-go-book-string]] - shared technical atoms: String shares technical record from Chapter 5 - Tidbits / Strings and Byte Arrays: int64(count) (1 shared atom(s))
- [[coding-little-go-book-pointer-versus-value]] - shared statements: Pointers versus Values shares source evidence from Chapter 3 - Maps, Arrays and Slices / Pointers versus Values: Many developers think that passing b to, or returning it from, a function is going to be more efficient. However, what's being passed/returned is a copy of the slice ... [truncated] (1 shared statement(s))
- [[coding-little-go-book-you-continue]] - shared statements: Before You Continue shares source evidence from Chapter 4 - Code Organization and Interfaces / Before You Continue: Finally, if you're new to interfaces, it might take some time before you get a feel for them. However, the first time you see a function that expects something like ... [truncated] (1 shared statement(s))

## Source

- [[coding-little-go-book]]
