---
page_id: javascriptallonge-recipe-factorials
page_kind: recipe
summary: factorials: reusable source-backed pattern with 4 statement(s) and 4 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-01
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: factorials
projection_coverage: recipe-javascriptallonge-recipe-factorials@9cdc06055adb1f5d53fb0ba6d24e8a9b
---

# factorials

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-composing-and-decomposing-data-factorials-48d5d159]].
- Evidence roles: decision, constraint, procedure, explanation, example.

## Applicability And Rationale

- , is the product of all positive integers less than or equal to n . _(javascriptallonge.pdf (source-range-0e12e052-00984))_
- While this is mathematically elegant, it is computational filigree 63 . _(javascriptallonge.pdf (source-range-0e12e052-00988))_
- Once again, it is not tail-recursive, it needs to save the stack with each invocation so that it can take the result returned and compute n * factorial(n -1) . _(javascriptallonge.pdf (source-range-0e12e052-00989))_
- Asbefore, we wrote a factorialWithDelayedWork function, then used partial application ( callLast ) to make a factorial function that took just the one argument and supplied the initial work value. _(javascriptallonge.pdf (source-range-0e12e052-00994))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-00985)_

```
5! = 5
x
4
x
3
x
2
x
1 = 120.
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-00987)_

```
const factorial = (n) =>
n == 1
? n
: n * factorial(n - 1);
factorial(1)
//=> 1
factorial(5)
//=> 120
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-00990)_

```
const factorialWithDelayedWork = (n, work) =>
n === 1
? work
: factorialWithDelayedWork(n - 1, n * work);
const factorial = (n) =>
factorialWithDelayedWork(n, 1);
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-00993)_

```
const callLast = (fn, ...args) =>
(...remainingArgs) =>
fn(...remainingArgs, ...args);
const factorial = callLast(factorialWithDelayedWork, 1);
factorial(1)
//=> 1
factorial(5)
//=> 120
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-composing-and-decomposing-data-factorials-48d5d159]]
