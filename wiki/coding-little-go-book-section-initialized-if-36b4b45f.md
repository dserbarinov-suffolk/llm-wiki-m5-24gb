---
page_id: coding-little-go-book-section-initialized-if-36b4b45f
page_kind: source
summary: Initialized If: 5 source-backed entries and 3 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: sources/coding-little-go-book/sections
source_id: coding_little_go_book.pdf
projection_coverage: section-coding-little-go-book-section-initialized-if-36b4b45f@6a550ea7e6ddbc924fbc52b13af69e57
---

# Initialized If

From [[coding-little-go-book]].

## Statements

- Interestingly, while the values aren't available outside the ifstatement, they are available inside any else if or else . _(coding_little_go_book.pdf (source-range-773b6275-00366))_
- Interestingly, while the values aren't available outside the ifstatement, they are available inside any else if or else . _(coding_little_go_book.pdf (source-range-773b6275-00366))_

## Technical atoms

> Go supports a slightly modified if-statement, one where a value can be initiated prior to the condition being evaluated:
_(source: coding_little_go_book.pdf (source-range-773b6275-00362))_

```
if x := 10; count > x {
  ...
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00363))_

```
if err := process(); err != nil {
  return err
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00365))_
