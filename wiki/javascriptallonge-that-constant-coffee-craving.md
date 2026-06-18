---
category: source
summary: That Constant Coffee Craving from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.49-61
updated: 2026-06-18
domain: javascriptallonge
category_path: source-sections
source_id: javascriptallonge.pdf
---

## That Constant Coffee Craving

This section discusses how to name constants in JavaScript, using the example of calculating the circumference of a circle. It explores different approaches to bind values to names, such as using immediately invoked function expressions (IIFEs) and the `const` keyword.

### Key Concepts:
- **Anonymous Functions**: Functions without names, commonly used in JavaScript.
- **Immediately Invoked Function Expressions (IIFEs)**: A pattern where a function is defined and immediately invoked to bind values to names.
- **const Keyword**: A way to bind values to names within a block without the overhead of function invocation.

### Example:
To bind the value of π (3.14159265) to the name `PI`:
- Using IIFE: `((PI) => (diameter) => diameter * PI)(3.14159265)`
- Using `const`: `(diameter) => { const PI = 3.14159265; return diameter * PI }`

### Summary:
JavaScript provides multiple ways to bind values to names, with `const` being a more readable and efficient approach for constants. This section emphasizes the importance of naming in sustainable software development and highlights the benefits of using `const` over IIFEs for clarity and performance.

**Sources:** (raw/javascriptallonge.pdf p.49-61)
