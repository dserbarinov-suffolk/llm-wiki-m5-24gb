---
page_id: coding-little-go-book-field-structure
page_kind: concept
summary: Fields of a Structure: 23 statement(s) and 8 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-field-structure@42e1913b1be12bed906ca9e43c45521b
---

# Fields of a Structure

What [[coding-little-go-book]] covers about fields of a structure:

## Statements

- Structures don't have constructors. _(coding_little_go_book.pdf (source-range-810ce361-00145))_
- We don't have to set all or even any of the fields. _(coding_little_go_book.pdf (source-range-810ce361-00121))_
- Just like unassigned variables have a zero value, so do fields. _(coding_little_go_book.pdf (source-range-810ce361-00123))_
- What Go does have are structures, which can be associated with methods. _(coding_little_go_book.pdf (source-range-810ce361-00112))_
- If we have a structure with many fields, creating copies can be expensive. _(coding_little_go_book.pdf (source-range-810ce361-00137))_
- Go supports composition, which is the act of including one structure into another. _(coding_little_go_book.pdf (source-range-810ce361-00160))_
- A slice is a lightweight structure that wraps and represents a portion of an array. _(coding_little_go_book.pdf (source-range-810ce361-00200))_
- which can then be used anywhere -- as a field type, as a parameter, as a return value. _(coding_little_go_book.pdf (source-range-810ce361-00389))_
- Now that we're talking about structures, we need to expand that conversation to include pointers. _(coding_little_go_book.pdf (source-range-810ce361-00117))_
- It does more than indent your code; it also aligns field declarations and alphabetically orders imports. _(coding_little_go_book.pdf (source-range-810ce361-00360))_
- In the example that we've seen so far, Saiyan has two fields Name and Power of types string and int , respectively. _(coding_little_go_book.pdf (source-range-810ce361-00157))_
- The following chapters will build on what we know about structures as well as the inner workings that we've explored. _(coding_little_go_book.pdf (source-range-810ce361-00187))_
- If a structure field name starts with a lowercase letter, only code within the same package will be able to access them. _(coding_little_go_book.pdf (source-range-810ce361-00300))_
- If your structure has a function name Log with a string parameter and no return value, then it can be used as a Logger . _(coding_little_go_book.pdf (source-range-810ce361-00327))_

## Technical atoms

> Note: The trailing , in the above structure is required.
_(source: coding_little_go_book.pdf (source-range-810ce361-00120))_

> Furthermore, you can skip the field name and rely on the order of the field declarations (though for the sake of clarity, you should only do this for structures with few fields):
_(source: coding_little_go_book.pdf (source-range-810ce361-00124))_

> It should also be obvious that copying a pointer is going to be cheaper than copying a complex structure.
_(source: coding_little_go_book.pdf (source-range-810ce361-00137))_

> The Saiyan structure has a field of type *Person . Because we didn't give it an explicit field name, we can implicitly access the fields and functions of the composed type. However, the Go compiler did give it a field name, consider the perfectly valid:
_(source: coding_little_go_book.pdf (source-range-810ce361-00164))_

> However, because implicit composition is really just a compiler trick, we can "overwrite" the functions of a composed type. For example, our Saiyan structure can have its own Introduce function:
_(source: coding_little_go_book.pdf (source-range-810ce361-00170))_

> To keep more complicated libraries and systems organized, we need to learn about packages. In Go, package names follow the directory structure of your Go workspace. If we were building a shopping system, we'd probably start with a package name "shopping" and put our source files in $GOPATH/src/shopping/ . We don't want to put everything inside this folder though. For example, maybe we want to isolate some database logic inside its own folder. To achieve this, we create a subfolder at $GOPATH/src/shopping/db . The package name of the files within this subfolder is simply db , but to access it from another package, including the shopping package, we need to import shopping/db . In other words, when you name a package, via the package keyword, you provide a single value, not a complete hierarchy (e.g., "shopping" or "db"). When you import a package, you specify the complete path. Let's try it. Inside your Go workspace's src folder (which we set up in Getting Started of the Introduction), create a new folder called shopping and a subfolder within it called db . Inside of shopping/db , create a file called db.go and add the following code:
_(source: coding_little_go_book.pdf (source-range-810ce361-00274))_


## Source

- [[coding-little-go-book]]
