---
category: source
summary: Object.assign from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.198-205
updated: 2026-06-18
domain: javascriptallonge
category_path: source-sections
source_id: javascriptallonge.pdf
---

## Object.assign

Object.assign is a standard function used to copy an object by extending an empty object or to extend one object with another. For example:

- Copy an object: `Object.assign({}, { apples: 12, oranges: 12 })` results in `{ apples: 12, oranges: 12 }`.
- Extend one object with another: `Object.assign(inventory, shipment)` merges the properties of `shipment` into `inventory`.

It is also used in object construction, such as in the `Queue` example where properties are assigned to `this` and `Queue.prototype`.

Assigning properties from one object to another is a basic building block for more advanced paradigms like mixins.

### Why?

The Y Combinator is a recursive function that enables recursive functions without needing to bind a function to a name in an environment. It is essential in combinatory logic but has limited practical use in JavaScript.

### Quasi-literals

JavaScript supports quasi-literal strings (Template Strings) denoted with back quotes. They allow for string interpolation using `${expression}`. For example:

- `A popular number for nerds is ${40 + 2}` results in `'A popular number for nerds is 42'`.

Quasi-literals are computationally equivalent to expressions using `+`, but they provide a more readable and expressive way to construct strings with embedded expressions.

### Sources
- (raw/javascriptallonge.pdf p.198-205)
