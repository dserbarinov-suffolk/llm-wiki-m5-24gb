---
category: source
summary: Recipes with Basic Functions from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.79-93
updated: 2026-06-18
domain: javascriptallonge
category_path: source-sections
source_id: javascriptallonge.pdf
---

## Recipes with Basic Functions

This page summarizes key concepts from the section **Recipes with Basic Functions** in *JavaScript Allongé* (raw/javascriptallonge.pdf p.79-93). The section explores practical applications of functions that return functions, focusing on partial application, unary functions, and the tap combinator.

### Partial Application

The text provides two recipes for partial application: `callFirst` and `callLast`, which apply a single argument to the leftmost or rightmost position of a function's argument list. It also introduces generalized versions, `callLeft` and `callRight`, which allow partial application with multiple arguments.

### Unary

The `unary` function decorator ensures that a function takes exactly one argument. This is useful for fixing issues like the unexpected behavior of `parseInt` when used with `.map`, where extra arguments (like the index) can cause unintended results.

### Tap

The `tap` combinator allows for side-effect operations on a value without changing it. It is useful for debugging or performing actions like logging. The text includes an implementation of `tap` and shows how it can be used in both curried and uncurried forms.

These recipes demonstrate practical uses of functional programming techniques in JavaScript, even if they introduce features not previously discussed in the book.
