---
category: source
summary: Closures and Scope from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.44-48
updated: 2026-06-18
domain: javascriptallonge
category_path: source-sections
source_id: javascriptallonge.pdf
---

## Closures and Scope

This page summarizes the discussion on closures and scope from *JavaScript Allongé* (raw/javascriptallonge.pdf p.44-48).

### Key Concepts
- **Closures**: Functions that contain free variables (variables not bound within the function itself) are called closures.
- **Pure Functions**: Functions with no free variables are called pure functions. They are easier to understand as their behavior is fully determined by their arguments.
- **Environment**: When a function is evaluated, it has access to its environment, including the parent environment. This allows closures to access variables from outer scopes.

### Example
- The expression `((x) => (y) => x)(1)(2)` evaluates to `1`. Here, the inner function `(y) => x` references the variable `x` from the outer function's environment, even though `x` is not bound in the inner function.

### Pure vs. Closures
- Pure functions always return the same result for the same inputs. Closures, however, depend on the environment in which they are evaluated, making their behavior context-sensitive.

### Additional Notes
- A closure can contain a pure function, but a pure function cannot contain a closure (as it would then have free variables).
- The environment for nested functions includes references to the parent environment, enabling access to variables from outer scopes.

### Related Topics
- [[javascriptallonge-closures-and-scope]]
- [[functional-programming]]
- [[javascriptallonge-as-little-as-possible-about-functions-but-no-less]]
- [[function]]
- [[javascriptallonge-recipes-with-basic-functions]]
