---
page_id: javascriptallonge-section-composing-and-decomposing-data-factorials-48d5d159
page_kind: source
summary: Composing and Decomposing Data / factorials: 9 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-06-30
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-composing-and-decomposing-data-factorials-48d5d159@f1d692f8a36955ba8f8110f35fbe9a51
---

# Composing and Decomposing Data / factorials

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-composing-and-decomposing-data-58c1e32b]] - broader source section: Composing and Decomposing Data
- [[javascriptallonge-section-composing-and-decomposing-data-tail-calls-and-default-arguments-2f80f1b0]] - previous source section: Composing and Decomposing Data / Tail Calls (and Default Arguments)
- [[javascriptallonge-section-composing-and-decomposing-data-default-arguments-870cb490]] - next source section: Composing and Decomposing Data / default arguments

## Statements

- In mathematics, the factorial of a non-negative integer n , denoted by n! , is the product of all positive integers less than or equal to n . For example: _(javascriptallonge.pdf (source-range-0e12e052-00984))_
- While this is mathematically elegant, it is computational filigree 63 . _(javascriptallonge.pdf (source-range-0e12e052-00988))_
- Once again, it is not tail-recursive, it needs to save the stack with each invocation so that it can take the result returned and compute n * factorial(n -1) . We can do the same conversion, pass in the work to be done: _(javascriptallonge.pdf (source-range-0e12e052-00989))_
- Asbefore, we wrote a factorialWithDelayedWork function, then used partial application ( callLast ) to make a factorial function that took just the one argument and supplied the initial work value. _(javascriptallonge.pdf (source-range-0e12e052-00994))_
- Asbefore, we wrote a factorialWithDelayedWork function, then used partial application ( callLast ) to make a factorial function that took just the one argument and supplied the initial work value. _(javascriptallonge.pdf (source-range-0e12e052-00994))_

## Technical atoms

### Technical frame 1: Composing and Decomposing Data / factorials

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00988))_

> While this is mathematically elegant, it is computational filigree 63 .

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00985))_

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

### Technical frame 2: Composing and Decomposing Data / factorials

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00988))_

> While this is mathematically elegant, it is computational filigree 63 .

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00987))_

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

### Technical frame 3: Composing and Decomposing Data / factorials

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00994))_

> Asbefore, we wrote a factorialWithDelayedWork function, then used partial application ( callLast ) to make a factorial function that took just the one argument and supplied the initial work value.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00990))_

```
const factorialWithDelayedWork = (n, work) =>
n === 1
? work
: factorialWithDelayedWork(n - 1, n * work);
const factorial = (n) =>
factorialWithDelayedWork(n, 1);
```
