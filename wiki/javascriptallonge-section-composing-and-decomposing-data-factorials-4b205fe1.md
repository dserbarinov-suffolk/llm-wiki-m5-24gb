---
page_id: javascriptallonge-section-composing-and-decomposing-data-factorials-4b205fe1
page_kind: source
summary: Composing and Decomposing Data / factorials: 9 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-composing-and-decomposing-data-factorials-4b205fe1@139547a27a39b42f7d7b731045a5341f
---

# Composing and Decomposing Data / factorials

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-composing-and-decomposing-data-tail-calls-and-default-arguments-b4311a56]] - previous source section: Composing and Decomposing Data / Tail Calls (and Default Arguments)
- [[javascriptallonge-section-composing-and-decomposing-data-default-arguments-363804ac]] - next source section: Composing and Decomposing Data / default arguments

### Source structure

- [[javascriptallonge-section-composing-and-decomposing-data-99b4771a]] - broader source section: Composing and Decomposing Data

## Statements

- In mathematics, the factorial of a non-negative integer n , denoted by n! , is the product of all positive integers less than or equal to n . For example: _(javascriptallonge.pdf (source-range-c98ab3e6-00970))_
- While this is mathematically elegant, it is computational filigree 63 . _(javascriptallonge.pdf (source-range-c98ab3e6-00974))_
- Once again, it is not tail-recursive, it needs to save the stack with each invocation so that it can take the result returned and compute n * factorial(n -1) . We can do the same conversion, pass in the work to be done: _(javascriptallonge.pdf (source-range-c98ab3e6-00975))_
- Asbefore, we wrote a factorialWithDelayedWork function, then used partial application ( callLast ) to make a factorial function that took just the one argument and supplied the initial work value. _(javascriptallonge.pdf (source-range-c98ab3e6-00980))_
- Asbefore, we wrote a factorialWithDelayedWork function, then used partial application ( callLast ) to make a factorial function that took just the one argument and supplied the initial work value. _(javascriptallonge.pdf (source-range-c98ab3e6-00980))_

## Technical atoms

### Technical frame 1: Composing and Decomposing Data / factorials

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00974))_

> While this is mathematically elegant, it is computational filigree 63 .

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00971))_

<a id="atom-technical-atom-c081bbae741dacd4"></a>
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

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00974))_

> While this is mathematically elegant, it is computational filigree 63 .

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00973))_

<a id="atom-technical-atom-2d3a450d96a5f11f"></a>
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

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00980))_

> Asbefore, we wrote a factorialWithDelayedWork function, then used partial application ( callLast ) to make a factorial function that took just the one argument and supplied the initial work value.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00976))_

<a id="atom-technical-atom-00a9cb4b6c931321"></a>
```
const factorialWithDelayedWork = (n, work) =>
n === 1
? work
: factorialWithDelayedWork(n - 1, n * work);
const factorial = (n) =>
factorialWithDelayedWork(n, 1);
```
