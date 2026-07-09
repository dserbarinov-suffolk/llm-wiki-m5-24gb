---
page_id: javascriptallonge-recipe-why-const-and-let-were-invented
page_kind: recipe
summary: why const and let were invented: reusable source-backed pattern with 10 statement(s) and 1 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: why-const-and-let-were-invented
projection_coverage: recipe-javascriptallonge-recipe-why-const-and-let-were-invented@e6207c00e390423c395c696b872cd55d
---

# why const and let were invented

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-reassignment-why-const-and-let-were-invented-cf53c7fd]].
- Evidence roles: decision, constraint, example.

## Applicability And Rationale

- For nearly twenty years, variables were declared with var (not counting parameters and function declarations, of course). _(javascriptallonge.pdf (source-range-c98ab3e6-01178))_
- However, its functional scope was a problem. _(javascriptallonge.pdf (source-range-c98ab3e6-01178))_
- We haven't looked at it yet, but JavaScript provides a for loop for your iterating pleasure and convenience. _(javascriptallonge.pdf (source-range-c98ab3e6-01179))_
- Hopefully, you can think of a faster way to calculate this sum. _(javascriptallonge.pdf (source-range-c98ab3e6-01181))_
- 72 And perhaps you have noticed that var i = 1 is tucked away instead of being at the top as we prefer. _(javascriptallonge.pdf (source-range-c98ab3e6-01181))_
- 72 There is a well known story about Karl Friedrich Gauss when he was in elementary school. _(javascriptallonge.pdf (source-range-c98ab3e6-01182))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01180)_

```
var sum = 0;
for (var i = 1; i <= 100; i++) {
sum = sum + i
}
sum
#=> 5050
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-reassignment-why-const-and-let-were-invented-cf53c7fd]]
