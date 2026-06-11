---
category: source
summary: JavaScript arrays, array literals, destructuring, gathering, and control-flow semantics in function parameters.
sources: raw/javascriptallonge.pdf
updated: 2026-06-11
---

## Composing and Decomposing Data

JavaScript arrays are reference types. Array literals use `[ ]` syntax. Destructuring allows extracting elements from arrays using patterns like `const [x, y] = array`. Gathering with `...` spreads elements into new arrays. Examples:

- `const [car, ...cdr] = [1, 2, 3]` → `car=1`, `cdr=[2,3]`
- Destructuring parameters: `function headAndTail(head, ...tail) { ... }`
- Function parameters are eagerly evaluated, unlike control-flow operators.

[figure text (OCR, unverified): EXERCISE SELF SERVICE. Coffee Tin Coffee Coffee Tim Coffee Re fee Ti Coffee offee]

**Sources**: [raw/javascriptallonge.pdf p.94-108]
