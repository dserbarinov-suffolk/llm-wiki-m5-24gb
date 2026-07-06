---
page_id: javascriptallonge-section-composing-and-decomposing-data-factorials-f9cc315b
page_kind: source
summary: Composing and Decomposing Data / factorials: 9 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-composing-and-decomposing-data-factorials-f9cc315b@a226dc014ff189c4bbc2308d56119789
---

# Composing and Decomposing Data / factorials

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-composing-and-decomposing-data-tail-calls-and-default-arguments-e940a84d]] - previous source section: Composing and Decomposing Data / Tail Calls (and Default Arguments)
- [[javascriptallonge-section-composing-and-decomposing-data-default-arguments-d8781602]] - next source section: Composing and Decomposing Data / default arguments

### Source structure

- [[javascriptallonge-section-composing-and-decomposing-data-d80dc70f]] - broader source section: Composing and Decomposing Data

## Statements

- In mathematics, the factorial of a non-negative integer n , denoted by n! , is the product of all positive integers less than or equal to n . For example: _(javascriptallonge.pdf (source-range-c98ab3e6-00984))_
- While this is mathematically elegant, it is computational filigree 63 . _(javascriptallonge.pdf (source-range-c98ab3e6-00988))_
- Once again, it is not tail-recursive, it needs to save the stack with each invocation so that it can take the result returned and compute n * factorial(n -1) . We can do the same conversion, pass in the work to be done: _(javascriptallonge.pdf (source-range-c98ab3e6-00989))_
- Asbefore, we wrote a factorialWithDelayedWork function, then used partial application ( callLast ) to make a factorial function that took just the one argument and supplied the initial work value. _(javascriptallonge.pdf (source-range-c98ab3e6-00994))_
- Asbefore, we wrote a factorialWithDelayedWork function, then used partial application ( callLast ) to make a factorial function that took just the one argument and supplied the initial work value. _(javascriptallonge.pdf (source-range-c98ab3e6-00994))_

## Technical atoms

### Technical frame 1: Composing and Decomposing Data / factorials

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00988))_

> While this is mathematically elegant, it is computational filigree 63 .

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00985))_

<a id="atom-technical-atom-66c12e56f188fe0a"></a>
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

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00988))_

> While this is mathematically elegant, it is computational filigree 63 .

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00987))_

<a id="atom-technical-atom-ef4a1d3f3f2fe8cd"></a>
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

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00994))_

> Asbefore, we wrote a factorialWithDelayedWork function, then used partial application ( callLast ) to make a factorial function that took just the one argument and supplied the initial work value.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00990))_

<a id="atom-technical-atom-99f4e40557a672ad"></a>
```
const factorialWithDelayedWork = (n, work) =>
n === 1
? work
: factorialWithDelayedWork(n - 1, n * work);
const factorial = (n) =>
factorialWithDelayedWork(n, 1);
```
