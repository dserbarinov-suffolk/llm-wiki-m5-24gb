---
page_id: coding-little-go-book-section-chapter-5-tidbits-e7a41f7c
page_kind: source
summary: Chapter 5 - Tidbits: 70 source-backed entries and 0 atom(s) from raw/coding_little_go_book.pdf.
page_family: section-reference
sources: raw/coding_little_go_book.pdf
updated: 2026-06-30
domain: coding-little-go-book
category_path: sources/coding-little-go-book/sections
source_id: coding_little_go_book.pdf
projection_coverage: section-coding-little-go-book-section-chapter-5-tidbits-e7a41f7c@9a1bf093e2c99e1c98caab4bd7a30ea5
---

# Chapter 5 - Tidbits

From [[coding-little-go-book]].

## Related pages

- [[coding-little-go-book-section-chapter-5-tidbits-error-handling-c2084411]] - narrower source section: Chapter 5 - Tidbits / Error Handling
- [[coding-little-go-book-section-chapter-5-tidbits-defer-9e77b4c5]] - narrower source section: Chapter 5 - Tidbits / Defer
- [[coding-little-go-book-section-chapter-5-tidbits-go-fmt-e0b0680f]] - narrower source section: Chapter 5 - Tidbits / go fmt
- [[coding-little-go-book-section-chapter-5-tidbits-initialized-if-10bfb3a1]] - narrower source section: Chapter 5 - Tidbits / Initialized If
- [[coding-little-go-book-section-chapter-5-tidbits-empty-interface-and-conversions-c4483a93]] - narrower source section: Chapter 5 - Tidbits / Empty Interface and Conversions
- [[coding-little-go-book-section-chapter-5-tidbits-strings-and-byte-arrays-6caeb68b]] - narrower source section: Chapter 5 - Tidbits / Strings and Byte Arrays
- [[coding-little-go-book-section-chapter-5-tidbits-function-type-561f81dd]] - narrower source section: Chapter 5 - Tidbits / Function Type
- [[coding-little-go-book-section-chapter-5-tidbits-before-you-continue-25d54302]] - narrower source section: Chapter 5 - Tidbits / Before You Continue
- [[coding-little-go-book-section-chapter-4-code-organization-and-interfaces-16681a63]] - previous source section: Chapter 4 - Code Organization and Interfaces
- [[coding-little-go-book-section-chapter-6-concurrency-55851f5e]] - next source section: Chapter 6 - Concurrency

## Statements by subsection

### Chapter 5 - Tidbits / Error Handling

- Go's preferred way to deal with errors is through return values, not exceptions. Consider the strconv.Atoi function which takes a string and tries to convert it to an integer: _(coding_little_go_book.pdf (source-range-23d24eb1-00339))_
- You can create your own error type; the only requirement is that it fulfills the contract of the built-in error interface, which is: _(coding_little_go_book.pdf (source-range-23d24eb1-00341))_
- This is a package variable (it's defined outside of a function) which is publicly accessible (upper-case first letter). Various functions can return this error, say when we're reading from a file or STDIN. If it makes contextual sense, you should use this error, too. As consumers, we can use this singleton: _(coding_little_go_book.pdf (source-range-23d24eb1-00348))_
- As a final note, Go does have panic and recover functions. panic is like throwing an exception while recover is like catch ; they are rarely used. _(coding_little_go_book.pdf (source-range-23d24eb1-00350))_
- You can create your own error type; the only requirement is that it fulfills the contract of the built-in error interface, which is: _(coding_little_go_book.pdf (source-range-23d24eb1-00341))_

### Chapter 5 - Tidbits / Defer

- If you try to run the above code, you'll probably get an error (the file doesn't exist). The point is to show how defer works. Whatever you defer will be executed after the enclosing function (in this case main() ) returns, even if it does so violently. This lets you release resources near where it's initialized and takes care of multiple return points. _(coding_little_go_book.pdf (source-range-23d24eb1-00354))_
- Whatever you defer will be executed after the enclosing function (in this case main() ) returns, even if it does so violently. _(coding_little_go_book.pdf (source-range-23d24eb1-00354))_

### Chapter 5 - Tidbits / go fmt

- Most programs written in Go follow the same formatting rules, namely, a tab is used to indent and braces go on the same line as their statement. _(coding_little_go_book.pdf (source-range-23d24eb1-00356))_
- I know, you have your own style and you want to stick to it. That's what I did for a long time, but I'm glad I eventually gave in. A big reason for this is the go fmt command. It's easy to use and authoritative (so no one argues over meaningless preferences). _(coding_little_go_book.pdf (source-range-23d24eb1-00357))_
- Give it a try. It does more than indent your code; it also aligns field declarations and alphabetically orders imports. _(coding_little_go_book.pdf (source-range-23d24eb1-00360))_

### Chapter 5 - Tidbits / Initialized If

- Interestingly, while the values aren't available outside the ifstatement, they are available inside any else if or else . _(coding_little_go_book.pdf (source-range-23d24eb1-00366))_
- Interestingly, while the values aren't available outside the ifstatement, they are available inside any else if or else . _(coding_little_go_book.pdf (source-range-23d24eb1-00366))_

### Chapter 5 - Tidbits / Empty Interface and Conversions

- In most object-oriented languages, a built-in base class, often named object , is the superclass for all other classes. Go, having no inheritance, doesn't have such a superclass. What it does have is an empty interface with no methods: interface{} . Since every type implements all 0 of the empty interface's methods, and since interfaces are implicitly implemented, every type fulfills the contract of the empty interface. _(coding_little_go_book.pdf (source-range-23d24eb1-00368))_
- Note that if the underlying type is not int , the above will result in an error. _(coding_little_go_book.pdf (source-range-23d24eb1-00373))_
- You'll see and probably use the empty interface more than you might first expect. Admittedly, it won't result in clean code. Converting values back and forth is ugly and dangerous but sometimes, in a static language, it's the only choice. _(coding_little_go_book.pdf (source-range-23d24eb1-00376))_
- Converting values back and forth is ugly and dangerous but sometimes, in a static language, it's the only choice. _(coding_little_go_book.pdf (source-range-23d24eb1-00376))_

### Chapter 5 - Tidbits / Strings and Byte Arrays

- Strings and byte arrays are closely related. We can easily convert one to the other: _(coding_little_go_book.pdf (source-range-23d24eb1-00378))_
- In fact, this way of converting is common across various types as well. Some functions explicitly expect an int32 or an int64 or their unsigned counterparts. You might find yourself having to do things like: _(coding_little_go_book.pdf (source-range-23d24eb1-00380))_
- Still, when it comes to bytes and strings, it's probably something you'll end up doing often. Do note that when you use []byte(X) or string(X) , you're creating a copy of the data. This is necessary because strings are immutable. _(coding_little_go_book.pdf (source-range-23d24eb1-00382))_
- Strings are made of runes which are unicode code points. If you take the length of a string, you might not get what you expect. The following prints 3: _(coding_little_go_book.pdf (source-range-23d24eb1-00383))_
- This is necessary because strings are immutable. _(coding_little_go_book.pdf (source-range-23d24eb1-00382))_

### Chapter 5 - Tidbits / Function Type

- which can then be used anywhere -- as a field type, as a parameter, as a return value. _(coding_little_go_book.pdf (source-range-23d24eb1-00389))_
- which can then be used anywhere -- as a field type, as a parameter, as a return value. _(coding_little_go_book.pdf (source-range-23d24eb1-00389))_

### Chapter 5 - Tidbits / Before You Continue

- We looked at various aspects of programming with Go. Most notably, we saw how error handling behaves and how to release resources such as connections and open files. Many people dislike Go's approach to error handling. It can feel like a step backwards. Sometimes, I agree. Yet, I also find that it results in code that's easier to follow. defer is an unusual but practical approach to resource management. In fact, it isn't tied to resource management only. You can use defer for any purpose, such as logging when a function exits. _(coding_little_go_book.pdf (source-range-23d24eb1-00394))_
- Certainly, we haven't looked at all of the tidbits Go has to offer. But you should be feeling comfortable enough to tackle whatever you come across. _(coding_little_go_book.pdf (source-range-23d24eb1-00395))_
- Most notably, we saw how error handling behaves and how to release resources such as connections and open files. _(coding_little_go_book.pdf (source-range-23d24eb1-00394))_
- Yet, I also find that it results in code that's easier to follow. _(coding_little_go_book.pdf (source-range-23d24eb1-00394))_
- In fact, it isn't tied to resource management only. _(coding_little_go_book.pdf (source-range-23d24eb1-00394))_
