---
page_id: javascriptallonge-recipe-inside-out
page_kind: recipe
summary: inside-out: reusable source-backed pattern with 11 statement(s) and 6 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: inside-out
projection_coverage: recipe-javascriptallonge-recipe-inside-out@7fb7acb52190003c4a2b226b929391d2
---

# inside-out

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-and-also-that-constant-coffee-craving-inside-out-1aea92c2]].
- Evidence roles: decision, constraint, explanation, example.

## Applicability And Rationale

- There's another way we can make a function that binds 3.14159265 to the name PI and then uses that in its expression. _(javascriptallonge.pdf (source-range-c98ab3e6-00393))_
- A 'magic literal' like 3.14159265 is anathema to sustainable software development. _(javascriptallonge.pdf (source-range-c98ab3e6-00397))_
- Well, the first one seems simplest, but a half-century of experience has taught us that names matter. _(javascriptallonge.pdf (source-range-c98ab3e6-00397))_
- The third one is easiest for most people to read. _(javascriptallonge.pdf (source-range-c98ab3e6-00398))_
- Explaining the pattern, Ben Alman coined the term [Immediately Invoked Function Expression][iife] for it, often abbreviated 'IIFE.' _(javascriptallonge.pdf (source-range-c98ab3e6-00399))_
- 29 JavaScript programmers regularly use the idea of writing an expression that denotes a function and then immediately applying it to arguments. _(javascriptallonge.pdf (source-range-c98ab3e6-00399))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00394)_

```
(diameter) =>
((PI) =>
diameter * PI)(3.14159265)
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00396)_

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

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00400)_

```
(diameter) =>
// ...
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00402)_

```
((PI) =>
// ...
)(3.14159265)
```

### Atom 5: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00404)_

```
(diameter) =>
((PI) =>
diameter * PI)(3.14159265)
```

### Atom 6: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00406)_

```
((PI) =>
(diameter) => diameter * PI
)(3.14159265)
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-and-also-that-constant-coffee-craving-inside-out-1aea92c2]]
