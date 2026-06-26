---
page_id: coding-little-go-book-section-overloading-99c8afdf
page_kind: source
summary: Overloading: 3 source-backed entries and 2 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: sources/coding-little-go-book/sections
source_id: coding_little_go_book.pdf
projection_coverage: section-coding-little-go-book-section-overloading-99c8afdf@b58c4479fa08739e984023eae312fcc3
---

# Overloading

From [[coding-little-go-book]].

## Statements

- The composed version is always available via s.Person.Introduce() . _(coding_little_go_book.pdf (source-range-773b6275-00172))_

## Technical atoms

> However, because implicit composition is really just a compiler trick, we can "overwrite" the functions of a composed type. For example, our Saiyan structure can have its own Introduce function:
_(source: coding_little_go_book.pdf (source-range-773b6275-00170))_

```
func (s *Saiyan) Introduce() {
  fmt.Printf("Hi, I'm %s. Ya!\n", s.Name)
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00171))_
