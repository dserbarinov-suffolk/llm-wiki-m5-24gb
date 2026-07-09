---
page_id: javascriptallonge-factorial
page_kind: concept
summary: topic-concept: 9 supported fragment(s) and 2 related link(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: page-projection-pgp_2ba5aeef7a560aff@c422bc00e6e5823cd48fe9e01e05116a
---

# factorials

Source: [[javascriptallonge]]

## Statements

- While this is mathematically elegant, it is computational filigree 63 . (javascriptallonge.pdf p.122)
- Once again, it is not tail-recursive, it needs to save the stack with each invocation so that it can take the result returned and compute n * factorial(n -1) . (javascriptallonge.pdf p.122)
- Asbefore, we wrote a factorialWithDelayedWork function, then used partial application ( callLast ) to make a factorial function that took just the one argument and supplied the initial work value. (javascriptallonge.pdf p.123)

## Rules

- Once again, it is not tail-recursive, it needs to save the stack with each invocation so that it can take the result returned and compute n * factorial(n -1) . (javascriptallonge.pdf p.122)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

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

<a id="atom-2"></a>
**Atom:** code block

```
const factorialWithDelayedWork = (n, work) =>
n === 1
? work
: factorialWithDelayedWork(n - 1, n * work);
const factorial = (n) =>
factorialWithDelayedWork(n, 1);
```

<a id="atom-3"></a>
**Atom:** code block

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


## Related pages

- [[javascriptallonge-tail-calls-and-default-arguments]] - contextualizes: source-supported topic dependency
- [[javascriptallonge-default-arguments]] - contextualizes: source-supported topic dependency
