---
page_id: javascriptallonge-recipe-applying-functions
page_kind: recipe
summary: applying functions: reusable source-backed pattern with 4 statement(s) and 2 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: applying-functions
projection_coverage: recipe-javascriptallonge-recipe-applying-functions@fed69bea5fdffdedf30ec184def14e64
---

# applying functions

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-applying-functions-09d5f96e]].
- Evidence roles: decision, explanation, procedure, example.

## Applicability And Rationale

- The way we use functions is to apply them to zero or more values called arguments . _(javascriptallonge.pdf (source-range-c98ab3e6-00175))_
- We'll put it in parentheses 17 to keep the parser happy, like we did above: (() => 0) . _(javascriptallonge.pdf (source-range-c98ab3e6-00178))_
- Since we aren't giving it any arguments, we'll simply write () after the expression. _(javascriptallonge.pdf (source-range-c98ab3e6-00178))_
- 17 If you're used to other programming languages, you've probably internalized the idea that sometimes parentheses are used to group operations in an expression like math, and sometimes to apply a function to arguments. _(javascriptallonge.pdf (source-range-c98ab3e6-00180))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00177)_

```
fn_expr(args)
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00179)_

```
(() => 0)()
//=> 0
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-applying-functions-09d5f96e]]
