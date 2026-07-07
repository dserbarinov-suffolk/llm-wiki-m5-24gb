---
page_id: javascriptallonge-recipe-that-constant-coffee-craving
page_kind: recipe
summary: That Constant Coffee Craving: reusable source-backed pattern with 9 statement(s) and 4 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: that-constant-coffee-craving
projection_coverage: recipe-javascriptallonge-recipe-that-constant-coffee-craving@ab00713611ae4220463a6a281c5a6ad5
---

# That Constant Coffee Craving

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-that-constant-coffee-craving-2f2b1a19]].
- Evidence roles: decision, constraint, example.

## Applicability And Rationale

- Naming things is a critical part of programming, but all we've seen so far is how to name arguments. _(javascriptallonge.pdf (source-range-c98ab3e6-00370))_
- Up to now, all we've really seen are anonymous functions , functions that don't have a name. _(javascriptallonge.pdf (source-range-c98ab3e6-00370))_
- This feels very different from programming in most other languages, where the focus is on naming functions, methods, and procedures. _(javascriptallonge.pdf (source-range-c98ab3e6-00370))_
- In order to bind 3.14159265 to the name PI , we'll need a function with a parameter of PI applied to an argument of 3.14159265 . _(javascriptallonge.pdf (source-range-c98ab3e6-00373))_
- This expression, when evaluated, returns a function that calculates circumferences. _(javascriptallonge.pdf (source-range-c98ab3e6-00377))_
- This one has a few more moving parts, that's all. _(javascriptallonge.pdf (source-range-c98ab3e6-00377))_

## Technical Atoms

### Atom 1: `worked-example`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00371)_

```
There are other ways to name things in JavaScript, but before we learn some of those, let's see how to use what we already have to name things. Let's revisit a very simple example:
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00374)_

```
((PI) =>
// ????
)(3.14159265)
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00376)_

```
((PI) =>
(diameter) => diameter * PI
)(3.14159265)
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00380)_

```
((diameter) => diameter * 3.14159265)(2)
//=> 6.2831853
((PI) =>
(diameter) => diameter * PI
)(3.14159265)(2)
//=> 6.2831853
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-that-constant-coffee-craving-2f2b1a19]]
