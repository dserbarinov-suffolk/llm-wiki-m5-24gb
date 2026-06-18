---
category: source
summary: Naming Functions from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.62-78
updated: 2026-06-18
domain: javascriptallonge
category_path: source-sections
source_id: javascriptallonge.pdf
---

## Naming Functions

JavaScript provides multiple ways to define and name functions. Here's a concise summary of the key points from the source:

### Anonymous Functions

- Functions defined with `const` or arrow syntax (`=>`) are **anonymous** by default. For example:
  ```javascript
  const repeat = (str) => str + str;
  ```
  Here, `repeat` is a binding in the environment, but the function itself remains unnamed.

### Named Function Expressions

- The `function` keyword allows defining **named functions**. For example:
  ```javascript
  const repeat = function repeat(str) { return str + str; };
  ```
  This creates a **named function expression**. The name `repeat` is bound to the function itself, not the environment.

- The function's name is a property of the function object:
  ```javascript
  repeat.name; // => 'repeat'
  ```

### Function Declarations

- Function declarations use the `function` keyword and are **hoisted** to the top of their scope:
  ```javascript
  function fizzbuzz() { return "Fizz" + "Buzz"; }
  ```

- This allows the function to be used before it is declared in the code:
  ```javascript
  fizzbuzz(); // Works even if declared later
  ```

### Recursive Functions

- Named functions are useful for **recursive functions** because the function can refer to itself by name:
  ```javascript
  (function even(n) {
    if (n === 0) return true;
    else return !even(n - 1);
  })(5);
  ```

- The name `even` is accessible **only within the function body**, not outside it.

### Summary

- Use named functions (`function`) for **recursive** or **debuggable** functions.
- Use anonymous functions (`const` or arrow syntax) when the function does not need to refer to itself.
- Named function expressions allow naming without binding to the environment.
- Function declarations are **hoisted**, making them available before their definition in the code.

**Source**: `raw/javascriptallonge.pdf p.62-78`
