---
page_id: javascriptallonge-recipe-applying-functions
page_kind: recipe
summary: applying functions: reusable source-backed pattern with 4 statement(s) and 2 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: applying-functions
projection_coverage: recipe-javascriptallonge-recipe-applying-functions@d0e04ed2cf6f70453b147535dab173fb
---

# applying functions

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-the-first-sip-basic-functions-as-little-as-possible-about-functions-but-no-less-applying-functio-fa7923f6]].
- Evidence roles: decision, explanation, procedure, example.

## Applicability And Rationale

- The way we use functions is to apply them to zero or more values called arguments . _(javascriptallonge.pdf (source-range-0e12e052-00183))_
- We'll put it in parentheses 17 to keep the parser happy, like we did above: (() => 0) . _(javascriptallonge.pdf (source-range-0e12e052-00186))_
- Since we aren't giving it any arguments, we'll simply write () after the expression. _(javascriptallonge.pdf (source-range-0e12e052-00186))_
- 17 If you're used to other programming languages, you've probably internalized the idea that sometimes parentheses are used to group operations in an expression like math, and sometimes to apply a function to arguments. _(javascriptallonge.pdf (source-range-0e12e052-00188))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-00185)_

```
fn_expr(args)
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-00187)_

```
(() => 0)()
//=> 0
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-the-first-sip-basic-functions-as-little-as-possible-about-functions-but-no-less-applying-functio-fa7923f6]]
