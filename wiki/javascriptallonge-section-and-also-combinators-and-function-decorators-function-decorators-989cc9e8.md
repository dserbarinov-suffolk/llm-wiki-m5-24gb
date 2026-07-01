---
page_id: javascriptallonge-section-and-also-combinators-and-function-decorators-function-decorators-989cc9e8
page_kind: source
summary: And also: / Combinators and Function Decorators / function decorators: 9 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-01
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-and-also-combinators-and-function-decorators-function-decorators-989cc9e8@31a7e6ef34d47392bf78112debed8474
---

# And also: / Combinators and Function Decorators / function decorators

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-and-also-combinators-and-function-decorators-4a7771ac]] - broader source section: And also: / Combinators and Function Decorators
- [[javascriptallonge-section-and-also-combinators-and-function-decorators-a-balanced-statement-about-combinators-09d1a71e]] - previous source section: And also: / Combinators and Function Decorators / a balanced statement about combinators
- [[javascriptallonge-function-decorator]] - topic hub: opens the topic page for Function Decorator

## Statements

- So instead of writing !someFunction(42) , we can write not(someFunction)(42) . Hardly progress. But like compose , we could write either: _(javascriptallonge.pdf (source-range-0e12e052-00567))_
- not is a function decorator because it modifies a function while remaining strongly related to the original function's semantics. You'll see other function decorators in the recipes, like once and maybe. Function decorators aren't strict about being pure functions, so there's more latitude for making decorators than combinators. _(javascriptallonge.pdf (source-range-0e12e052-00573))_
- not is a function decorator because it modifies a function while remaining strongly related to the original function's semantics. _(javascriptallonge.pdf (source-range-0e12e052-00573))_

## Technical atoms

### Technical frame 1: And also: / Combinators and Function Decorators / function decorators

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00573))_

> not is a function decorator because it modifies a function while remaining strongly related to the original function's semantics. You'll see other function decorators in the recipes, like once and maybe. Function decorators aren't strict about being pure functions, so there's more latitude for making decorators than combinators.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00565))_

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

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00573))_

> not is a function decorator because it modifies a function while remaining strongly related to the original function's semantics. You'll see other function decorators in the recipes, like once and maybe. Function decorators aren't strict about being pure functions, so there's more latitude for making decorators than combinators.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00572))_

```
const nothing = not(something);
```
