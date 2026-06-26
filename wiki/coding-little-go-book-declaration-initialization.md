---
page_id: coding-little-go-book-declaration-initialization
page_kind: concept
summary: Declarations and Initializations: 27 statement(s) and 1 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-declaration-initialization@62ca07d7e3199c4751f43a7026460879
---

# Declarations and Initializations

What [[coding-little-go-book]] covers about declarations and initializations:

## Statements

- When we first looked at variables and declarations, we looked only at built-in types, like integers and strings. _(coding_little_go_book.pdf (source-range-773b6275-00117))_
- Furthermore, you can skip the field name and rely on the order of the field declarations (though for the sake of clarity, you should only do this for structures with few fields): _(coding_little_go_book.pdf (source-range-773b6275-00124))_
- It used to expect a value of type Saiyan but now expects an address of type *Saiyan , where *X means pointer to value of type X . _(coding_little_go_book.pdf (source-range-773b6275-00132))_
- Now that we're talking about structures, we need to expand that conversation to include pointers. _(coding_little_go_book.pdf (source-range-773b6275-00117))_
- Note: The trailing , in the above structure is required. _(coding_little_go_book.pdf (source-range-773b6275-00120))_
- Without it, the compiler will give an error. _(coding_little_go_book.pdf (source-range-773b6275-00120))_
- We don't have to set all or even any of the fields. _(coding_little_go_book.pdf (source-range-773b6275-00121))_
- Just like unassigned variables have a zero value, so do fields. _(coding_little_go_book.pdf (source-range-773b6275-00123))_
- What all of the above examples do is declare a variable goku and assign a value to it. _(coding_little_go_book.pdf (source-range-773b6275-00126))_
- A pointer is a memory address; it's the location of where to find the actual value. _(coding_little_go_book.pdf (source-range-773b6275-00127))_
- Many times though, we don't want a variable that is directly associated with our value but rather a variable that has a pointer to our value. _(coding_little_go_book.pdf (source-range-773b6275-00127))_
- Loosely, it's the difference between being at a house and having directions to the house. _(coding_little_go_book.pdf (source-range-773b6275-00127))_
- To make this work as you probably expect, we need to pass a pointer to our value: _(coding_little_go_book.pdf (source-range-773b6275-00130))_
- Because Super made changes to a copy of our original goku value and thus, changes made in Super weren't reflected in the caller. _(coding_little_go_book.pdf (source-range-773b6275-00130))_

## Technical atoms

> Context: Furthermore, you can skip the field name and rely on the order of the field declarations (though for the sake of clarity, you should only do this for structures with few fields): What all of the above examples do is declare a variable goku and assign a value to it.
_(context: coding_little_go_book.pdf (source-range-773b6275-00124, source-range-773b6275-00126))_

```
goku := Saiyan{"Goku", 9000}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00125))_


## Source

- [[coding-little-go-book]]
