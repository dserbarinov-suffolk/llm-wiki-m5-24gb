---
page_id: coding-little-go-book-field-structure
page_kind: concept
summary: Fields of a Structure: 16 statement(s) and 20 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-field-structure@7bbb6ec88b048857c9b313b9493f86c2
---

# Fields of a Structure

What [[coding-little-go-book]] covers about fields of a structure:

## Statements

- Structures don't have constructors. _(coding_little_go_book.pdf (source-range-810ce361-00144))_
- Just like unassigned variables have a zero value, so do fields. _(coding_little_go_book.pdf (source-range-810ce361-00122))_
- If we have a structure with many fields, creating copies can be expensive. _(coding_little_go_book.pdf (source-range-810ce361-00136))_
- Go supports composition, which is the act of including one structure into another. _(coding_little_go_book.pdf (source-range-810ce361-00159))_
- A slice is a lightweight structure that wraps and represents a portion of an array. _(coding_little_go_book.pdf (source-range-810ce361-00199))_
- Now that we're talking about structures, we need to expand that conversation to include pointers. _(coding_little_go_book.pdf (source-range-810ce361-00116))_
- It does more than indent your code; it also aligns field declarations and alphabetically orders imports. _(coding_little_go_book.pdf (source-range-810ce361-00359))_
- In the example that we've seen so far, Saiyan has two fields Name and Power of types string and int , respectively. _(coding_little_go_book.pdf (source-range-810ce361-00156))_
- The following chapters will build on what we know about structures as well as the inner workings that we've explored. _(coding_little_go_book.pdf (source-range-810ce361-00186))_
- If your structure has a function name Log with a string parameter and no return value, then it can be used as a Logger . _(coding_little_go_book.pdf (source-range-810ce361-00326))_
- At the end of this chapter, after we've seen a bit more of what we can do with structures, we'll re-examine the pointer-versus-value question. _(coding_little_go_book.pdf (source-range-810ce361-00137))_
- In Java, there's the possibility to extend structures with inheritance but, in a scenario where this is not an option, a mixin would be written like this: _(coding_little_go_book.pdf (source-range-810ce361-00159))_
- Which you use is up to you, but you'll find that most people prefer the latter whenever they have fields to initialize, since it tends to be easier to read: _(coding_little_go_book.pdf (source-range-810ce361-00152))_
- Since we moved the shared Item structure to shopping/models/item.go , we need to change shopping/db/db.go to reference the Item structure from models package: _(coding_little_go_book.pdf (source-range-810ce361-00294))_

## Code, rules, and examples

> It'd be nice to begin and end our look at variables by saying you declare and assign to a variable by doing x = 4. Unfortunately, things are more complicated in Go. We'll begin our conversation by looking at simple examples. Then, in the next chapter, we'll expand this when we look at creating and using structures. Still, it'll probably take some time before you truly feel comfortable with it.
_(source: coding_little_go_book.pdf (source-range-810ce361-00072))_

> What Go does have are structures, which can be associated with methods.
_(source: coding_little_go_book.pdf (source-range-810ce361-00111))_

> Although Go doesn't do OO like you may be used to, you'll notice a lot of similarities between the definition of a structure and that of a class.
_(source: coding_little_go_book.pdf (source-range-810ce361-00112))_

> Note: The trailing , in the above structure is required.
_(source: coding_little_go_book.pdf (source-range-810ce361-00119))_

> We don't have to set all or even any of the fields.
_(source: coding_little_go_book.pdf (source-range-810ce361-00120))_

> Furthermore, you can skip the field name and rely on the order of the field declarations (though for the sake of clarity, you should only do this for structures with few fields):
_(source: coding_little_go_book.pdf (source-range-810ce361-00123))_


## Source

- [[coding-little-go-book]]
