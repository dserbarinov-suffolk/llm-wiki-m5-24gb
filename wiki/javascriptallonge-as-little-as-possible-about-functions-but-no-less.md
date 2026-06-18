---
category: source
summary: As Little As Possible About Functions, But No Less from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.30-43
updated: 2026-06-18
domain: javascriptallonge
category_path: source-sections
source_id: javascriptallonge.pdf
---

## As Little As Possible About Functions, But No Less

JavaScript functions are values, but they are also more than simple data structures. They represent computations to be performed. Here's a simple function: `() => 0`, which returns 0 when applied.

### Functions and Identities

Functions are reference types. Even if two functions have the same expression, they are not identical:

```javascript
(() => 0) === (() => 0) // => false
```

### Applying Functions

Functions are applied to zero or more arguments. For example:

```javascript
(() => 0)() // => 0
```

### Functions Returning Values

Functions can return values by placing them to the right of the arrow:

```javascript
(() => 1)() // => 1
(() => "Hello, JavaScript")() // => "Hello, JavaScript"
```

### Commas

The comma operator evaluates multiple expressions, returning the last one:

```javascript
(() => (1 + 1, 2 + 2))() // => 4
```

### The Simplest Block

A block with no statements returns `undefined`:

```javascript
(() => {})() // => undefined
```

### Undefined

`undefined` represents the absence of a value in JavaScript. It is its own type of value and will appear again in the context of functions and variables.
