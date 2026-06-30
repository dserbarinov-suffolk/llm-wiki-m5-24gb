---
page_id: coding-little-go-book-section-chapter-2-structures-declarations-and-initializations-aa4f849c
page_kind: source
summary: Chapter 2 - Structures / Declarations and Initializations: 39 source-backed entries and 0 atom(s) from raw/coding_little_go_book.pdf.
page_family: section-reference
sources: raw/coding_little_go_book.pdf
updated: 2026-06-30
domain: coding-little-go-book
category_path: sources/coding-little-go-book/sections
source_id: coding_little_go_book.pdf
projection_coverage: section-coding-little-go-book-section-chapter-2-structures-declarations-and-initializations-aa4f849c@28a25b7f3b22b7589807bce55a1e04e9
---

# Chapter 2 - Structures / Declarations and Initializations

From [[coding-little-go-book]].

## Related pages

- [[coding-little-go-book-section-chapter-2-structures-59a89c52]] - broader source section: Chapter 2 - Structures
- [[coding-little-go-book-section-chapter-2-structures-functions-on-structures-7fcf1fb2]] - next source section: Chapter 2 - Structures / Functions on Structures

## Statements

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
- When we first looked at variables and declarations, we looked only at built-in types, like integers and strings. _(coding_little_go_book.pdf (source-range-23d24eb1-00117))_
- Furthermore, you can skip the field name and rely on the order of the field declarations (though for the sake of clarity, you should only do this for structures with few fields): _(coding_little_go_book.pdf (source-range-23d24eb1-00124))_
- Because Super made changes to a copy of our original goku value and thus, changes made in Super weren't reflected in the caller. _(coding_little_go_book.pdf (source-range-23d24eb1-00130))_
- It used to expect a value of type Saiyan but now expects an address of type *Saiyan , where *X means pointer to value of type X . _(coding_little_go_book.pdf (source-range-23d24eb1-00132))_
- At the end of this chapter, after we've seen a bit more of what we can do with structures, we'll re-examine the pointer-versus-value question. _(coding_little_go_book.pdf (source-range-23d24eb1-00138))_
