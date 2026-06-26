---
page_id: coding-little-go-book-structure
page_kind: concept
summary: Structures: 8 statement(s) and 1 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-structure@9172697b536d56edcc6980dbef7c3b6f
---

# Structures

What [[coding-little-go-book]] covers about structures:

## Statements

- What Go does have are structures, which can be associated with methods. _(coding_little_go_book.pdf (source-range-773b6275-00112))_
- Although Go doesn't do OO like you may be used to, you'll notice a lot of similarities between the definition of a structure and that of a class. _(coding_little_go_book.pdf (source-range-773b6275-00113))_
- Go isn't an object-oriented (OO) language like C++, Java, Ruby and C#. _(coding_little_go_book.pdf (source-range-773b6275-00111))_
- It doesn't have objects nor inheritance and thus, doesn't have the many concepts associated with OO such as polymorphism and overloading. _(coding_little_go_book.pdf (source-range-773b6275-00111))_
- (It's worth pointing out that composition over inheritance is an old battle cry and Go is the first language I've used that takes a firm stand on the issue.) _(coding_little_go_book.pdf (source-range-773b6275-00112))_
- Go also supports a simple but effective form of composition. _(coding_little_go_book.pdf (source-range-773b6275-00112))_
- Overall, it results in simpler code, but there'll be occasions where you'll miss some of what OO has to offer. _(coding_little_go_book.pdf (source-range-773b6275-00112))_
- Before we do that, we have to dive back into declarations. _(coding_little_go_book.pdf (source-range-773b6275-00115))_

## Technical atoms

> Context: Although Go doesn't do OO like you may be used to, you'll notice a lot of similarities between the definition of a structure and that of a class. A simple example is the following Saiyan structure:
_(context: coding_little_go_book.pdf (source-range-773b6275-00113))_

```
type Saiyan struct {
  Name string
  Power int
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00114))_


## Source

- [[coding-little-go-book]]
