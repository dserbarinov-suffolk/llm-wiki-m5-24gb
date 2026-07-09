---
page_id: javascriptallonge-function-decorators
page_kind: concept
summary: function decorators: 3 accepted assertion(s) and 5 technical atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-state-tps_f28c0c921fc52977@94e69125379819188e50e687de1769e5
---

# function decorators

Source: [[javascriptallonge]]

## Statements

- So instead of writing !someFunction(42) , we can write not(someFunction)(42) . (javascriptallonge.pdf p.70)
- not is a function decorator because it modifies a function while remaining strongly related to the original function's semantics. (javascriptallonge.pdf p.70)
- Function decorators aren't strict about being pure functions, so there's more latitude for making decorators than combinators. (javascriptallonge.pdf p.70)

## Technical atoms

<a id="atom-1"></a>
**Atom:** table

```text
function decorators
A function decorator is a higher-order function that takes one function as an argument, returns another function, and the returned function is a variation of the argument function. Here's a ridiculously simple decorator: 38
37 As we'll discuss later, this implementation of the B Combinator is correct in languages like Scheme, but for truly general-purpose use in JavaScript, it needs to correctly manage the function context.
38 We'll see later why an even more useful version would be written (fn) => (...args) => !fn(...args)
```

<a id="atom-2"></a>
**Atom:** code block

```
const not = (fn) => (x) => !fn(x)
```

<a id="atom-3"></a>
**Atom:** code block

```
const something = (x) => x != null;
```

<a id="atom-4"></a>
**Atom:** code block

```
const nothing = (x) => !something(x);
```

<a id="atom-5"></a>
**Atom:** code block

```
const nothing = not(something);
```
