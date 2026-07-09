---
page_id: javascriptallonge-recipe-inside-out
page_kind: recipe
summary: inside-out: reusable source-backed pattern with 11 statement(s) and 6 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: inside-out
projection_coverage: recipe-javascriptallonge-recipe-inside-out@9a46ffdaa6ecc18388b88133fc305205
---

# inside-out

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-that-constant-coffee-craving-inside-out-6df7936c]].
- Evidence roles: decision, constraint, explanation, example.

## Applicability And Rationale

- There's another way we can make a function that binds 3.14159265 to the name PI and then uses that in its expression. _(javascriptallonge.pdf (source-range-c98ab3e6-00383))_
- A 'magic literal' like 3.14159265 is anathema to sustainable software development. _(javascriptallonge.pdf (source-range-c98ab3e6-00387))_
- Well, the first one seems simplest, but a half-century of experience has taught us that names matter. _(javascriptallonge.pdf (source-range-c98ab3e6-00387))_
- The third one is easiest for most people to read. _(javascriptallonge.pdf (source-range-c98ab3e6-00388))_
- Explaining the pattern, Ben Alman coined the term [Immediately Invoked Function Expression][iife] for it, often abbreviated 'IIFE.' _(javascriptallonge.pdf (source-range-c98ab3e6-00389))_
- 29 JavaScript programmers regularly use the idea of writing an expression that denotes a function and then immediately applying it to arguments. _(javascriptallonge.pdf (source-range-c98ab3e6-00389))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00384)_

```
(diameter) =>
((PI) =>
diameter * PI)(3.14159265)
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00386)_

```
((diameter) => diameter * 3.14159265)(2)
//=> 6.2831853
((PI) =>
(diameter) => diameter * PI
)(3.14159265)(2)
//=> 6.2831853
((diameter) =>
((PI) =>
diameter * PI)(3.14159265))(2)
//=> 6.2831853
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00390)_

```
(diameter) =>
// ...
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00392)_

```
((PI) =>
// ...
)(3.14159265)
```

### Atom 5: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00394)_

```
(diameter) =>
((PI) =>
diameter * PI)(3.14159265)
```

### Atom 6: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00396)_

```
((PI) =>
(diameter) => diameter * PI
)(3.14159265)
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-that-constant-coffee-craving-inside-out-6df7936c]]
