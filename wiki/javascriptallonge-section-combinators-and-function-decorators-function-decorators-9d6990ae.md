---
page_id: javascriptallonge-section-combinators-and-function-decorators-function-decorators-9d6990ae
page_kind: source
summary: Combinators and Function Decorators / function decorators: 9 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-combinators-and-function-decorators-function-decorators-9d6990ae@ca6653c84a44fbda5f5b4577c958b3bd
---

# Combinators and Function Decorators / function decorators

From [[javascriptallonge]].

## Related pages

### Source structure

- [[javascriptallonge-section-combinators-and-function-decorators-901f172c]] - broader source section: Combinators and Function Decorators

### Topics

- [[javascriptallonge-function-decorator]] - topic hub: opens the topic page for Function Decorator

## Statements

- So instead of writing !someFunction(42) , we can write not(someFunction)(42) . Hardly progress. But like compose , we could write either: _(javascriptallonge.pdf (source-range-c98ab3e6-00557))_
- not is a function decorator because it modifies a function while remaining strongly related to the original function's semantics. You'll see other function decorators in the recipes, like once and maybe. Function decorators aren't strict about being pure functions, so there's more latitude for making decorators than combinators. _(javascriptallonge.pdf (source-range-c98ab3e6-00563))_
- not is a function decorator because it modifies a function while remaining strongly related to the original function's semantics. _(javascriptallonge.pdf (source-range-c98ab3e6-00563))_

## Technical atoms

### Technical frame 1: Combinators and Function Decorators / function decorators

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00563))_

> not is a function decorator because it modifies a function while remaining strongly related to the original function's semantics. You'll see other function decorators in the recipes, like once and maybe. Function decorators aren't strict about being pure functions, so there's more latitude for making decorators than combinators.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00555))_

<a id="atom-technical-atom-73d86f3bb2def087"></a>
```text
function decorators
A function decorator is a higher-order function that takes one function as an argument, returns another function, and the returned function is a variation of the argument function. Here's a ridiculously simple decorator: 38
37 As we'll discuss later, this implementation of the B Combinator is correct in languages like Scheme, but for truly general-purpose use in JavaScript, it needs to correctly manage the function context.
38 We'll see later why an even more useful version would be written (fn) => (...args) => !fn(...args)
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 37 | As we'll discuss later, this implementation of the B Combinator is correct in languages like Scheme, but for truly general-purpose use in JavaScript, it needs to correctly manage the function context. |
| 38 | We'll see later why an even more useful version would be written (fn) => (...args) =>!fn(...args) |

</details>

### Technical frame 2: Combinators and Function Decorators / function decorators

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00563))_

> not is a function decorator because it modifies a function while remaining strongly related to the original function's semantics. You'll see other function decorators in the recipes, like once and maybe. Function decorators aren't strict about being pure functions, so there's more latitude for making decorators than combinators.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00562))_

<a id="atom-technical-atom-b5e17c842f1f8e4e"></a>
```
const nothing = not(something);
```
