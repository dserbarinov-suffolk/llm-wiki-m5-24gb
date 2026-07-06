---
page_id: javascriptallonge-section-and-also-combinators-and-function-decorators-function-decorators-a89378c3
page_kind: source
summary: And also: / Combinators and Function Decorators / function decorators: 9 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-and-also-combinators-and-function-decorators-function-decorators-a89378c3@d8dbb0319e43cf79e6d400509c01333f
---

# And also: / Combinators and Function Decorators / function decorators

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-and-also-combinators-and-function-decorators-a-balanced-statement-about-combinators-3591f357]] - previous source section: And also: / Combinators and Function Decorators / a balanced statement about combinators

### Source structure

- [[javascriptallonge-section-and-also-combinators-and-function-decorators-f08ca983]] - broader source section: And also: / Combinators and Function Decorators

### Topics

- [[javascriptallonge-function-decorator]] - topic hub: opens the topic page for Function Decorator

## Statements

- So instead of writing !someFunction(42) , we can write not(someFunction)(42) . Hardly progress. But like compose , we could write either: _(javascriptallonge.pdf (source-range-c98ab3e6-00567))_
- not is a function decorator because it modifies a function while remaining strongly related to the original function's semantics. You'll see other function decorators in the recipes, like once and maybe. Function decorators aren't strict about being pure functions, so there's more latitude for making decorators than combinators. _(javascriptallonge.pdf (source-range-c98ab3e6-00573))_
- not is a function decorator because it modifies a function while remaining strongly related to the original function's semantics. _(javascriptallonge.pdf (source-range-c98ab3e6-00573))_

## Technical atoms

### Technical frame 1: And also: / Combinators and Function Decorators / function decorators

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00573))_

> not is a function decorator because it modifies a function while remaining strongly related to the original function's semantics. You'll see other function decorators in the recipes, like once and maybe. Function decorators aren't strict about being pure functions, so there's more latitude for making decorators than combinators.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00565))_

<a id="atom-technical-atom-ece2f4b7b92ce2c5"></a>
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

### Technical frame 2: And also: / Combinators and Function Decorators / function decorators

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00573))_

> not is a function decorator because it modifies a function while remaining strongly related to the original function's semantics. You'll see other function decorators in the recipes, like once and maybe. Function decorators aren't strict about being pure functions, so there's more latitude for making decorators than combinators.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00572))_

<a id="atom-technical-atom-48b9732f10355b03"></a>
```
const nothing = not(something);
```
