---
category: source
summary: Picking the Bean: Choice and Truthiness from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.94-108
updated: 2026-06-18
domain: javascriptallonge
category_path: source-sections
source_id: javascriptallonge.pdf
---

## Picking the Bean: Choice and Truthiness

JavaScript introduces the concept of truthiness, where values are either truthy or falsy. The falsy values include `false`, `null`, `undefined`, `NaN`, `0`, and the empty string `''`. All other values are considered truthy.

### Logical Operators

- **! (not)**: Negates its argument. `!true` evaluates to `false`, and `!false` evaluates to `true`.
- **&& (and)**: Returns the left-hand value if it is falsy, otherwise returns the right-hand value.
- **|| (or)**: Returns the left-hand value if it is truthy, otherwise returns the right-hand value.

### Truthiness and the Ternary Operator

JavaScript also includes the ternary operator (`? :`), which evaluates the first expression. If it is truthy, it evaluates and returns the second expression; otherwise, it evaluates and returns the third expression. This is useful for concise conditional expressions.

### Examples

- `true ? 'Hello' : 'Good bye'` evaluates to `'Hello'`.
- `0 ? 'Hello' : 'Good bye'` evaluates to `'Good bye'`.
- `[1, 2, 3, 4, 5].length === 5 ? 'Pentatonic' : 'Quasimodal'` evaluates to `'Pentatonic'`.

### Practical Use

The truthiness concept is crucial when using logical operators and the ternary operator. For example, `!!currentUser()` is a common idiom to check if `currentUser()` returns a truthy value.

This section discusses how truthiness affects the behavior of logical operators and the ternary operator in JavaScript, highlighting the importance of understanding these concepts for effective programming.
