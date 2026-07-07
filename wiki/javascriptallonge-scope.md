---
page_id: javascriptallonge-scope
page_kind: concept
summary: Scope: 4 statement(s) and 0 atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-scope@f9e891b7ff8110dcae5eef04d43536c5
---

# Scope

What [[javascriptallonge]] covers about scope:

## Statements

### shadowy variables from a shadowy planet

- When evaluating x + y + z , JavaScript will find x and y in the great-grandparent scope and z in the parent scope. The x in the great-great-grandparent scope is ignored, as are both w s. When a variable has the same name as an ancestor environment's binding, it is said to shadow the ancestor. _(javascriptallonge.pdf (source-range-c98ab3e6-00360))_

### Summary / Functions

- Blocks also create scopes if const statements are within them. _(javascriptallonge.pdf (source-range-c98ab3e6-00633))_

- Scopes are nested and free variable references closed over. _(javascriptallonge.pdf (source-range-c98ab3e6-00634))_

### Reassignment / why const and let were invented

- const and let are recent additions to JavaScript. For nearly twenty years, variables were declared with var (not counting parameters and function declarations, of course). However, its functional scope was a problem. _(javascriptallonge.pdf (source-range-c98ab3e6-01178))_


## Related pages

### Source structure

- [[javascriptallonge-section-and-also-closures-and-scope-77af1b0f]] - source section: And also: / Closures and Scope
- [[javascriptallonge-section-that-constant-coffee-craving-const-and-lexical-scope-bbfe0b3d]] - source section: That Constant Coffee Craving / const and lexical scope

### Shared claims

- [[javascriptallonge-functional]] - shared statements: Functional shares source evidence from Reassignment / why const and let were invented: const and let are recent additions to JavaScript. For nearly twenty years, variables were declared with var (not counting parameters and function declarations, of co ... [truncated] (1 shared statement(s))
- [[javascriptallonge-statement]] - shared statements: Statement shares source evidence from Summary / Functions: Blocks also create scopes if const statements are within them. (1 shared statement(s))

## Source

- [[javascriptallonge]]
