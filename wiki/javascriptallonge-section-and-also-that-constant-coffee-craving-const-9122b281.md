---
page_id: javascriptallonge-section-and-also-that-constant-coffee-craving-const-9122b281
page_kind: source
summary: And also: / That Constant Coffee Craving / const: 22 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-and-also-that-constant-coffee-craving-const-9122b281@f469815ef96c16bacd1096cb3665831d
---

# And also: / That Constant Coffee Craving / const

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-and-also-that-constant-coffee-craving-inside-out-973a2848]] - previous source section: And also: / That Constant Coffee Craving / inside-out
- [[javascriptallonge-section-and-also-that-constant-coffee-craving-nested-blocks-78bcbfc7]] - next source section: And also: / That Constant Coffee Craving / nested blocks

### Source structure

- [[javascriptallonge-section-and-also-that-constant-coffee-craving-ac9d9918]] - broader source section: And also: / That Constant Coffee Craving

### Topics

- [[javascriptallonge-const]] - topic hub: opens the topic page for Const

## Statements

- Another way to write our 'circumference' function would be to pass PI along with the diameter argument, something like this: _(javascriptallonge.pdf (source-range-0e12e052-00410))_
- This differs from our example above in that there is only one environment, rather than two. We have one binding in the environment representing our regular argument, and another our 'constant.' That's more efficient, and it's almost what we wanted all along: A way to bind 3.14159265 to a readable name. _(javascriptallonge.pdf (source-range-0e12e052-00414))_
- JavaScript gives us a way to do that, the const keyword. We'll learn a lot more about const in future chapters, but here's the most important thing we can do with const : _(javascriptallonge.pdf (source-range-0e12e052-00415))_
- The const keyword introduces one or more bindings in the block that encloses it. It doesn't incur the cost of a function invocation. That's great. Even better, it puts the symbol (like PI ) close to the value ( 3.14159265 ). That's much better than what we were writing. _(javascriptallonge.pdf (source-range-0e12e052-00417))_
- We use the const keyword in a const statement . const statements occur inside blocks, we can't use them when we write a fat arrow that has an expression as its body. _(javascriptallonge.pdf (source-range-0e12e052-00418))_
- We can bind any expression. Functions are expressions, so we can bind helper functions: _(javascriptallonge.pdf (source-range-0e12e052-00425))_
- Notice calc(d) ? This underscores what we've said: if we have an expression that evaluates to a function, we apply it with () . A name that's bound to a function is a valid expression evaluating to a function. 30 _(javascriptallonge.pdf (source-range-0e12e052-00427))_
- Amazing how such an important idea-naming functions-can be explained en passant in just a few words. That emphasizes one of the things JavaScript gets really, really right: Functions as 'first class entities. ' Functions are values that can be bound to names like any other value, passed as arguments, returned from other functions, and so forth. _(javascriptallonge.pdf (source-range-0e12e052-00428))_
- 30 We're into the second chapter and we've finally named a function. Sheesh. _(javascriptallonge.pdf (source-range-0e12e052-00431))_
- This differs from our example above in that there is only one environment, rather than two. _(javascriptallonge.pdf (source-range-0e12e052-00414))_

## Technical atoms

### Technical frame 1: And also: / That Constant Coffee Craving / const

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00417))_

> The const keyword introduces one or more bindings in the block that encloses it. It doesn't incur the cost of a function invocation. That's great. Even better, it puts the symbol (like PI ) close to the value ( 3.14159265 ). That's much better than what we were writing.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00416))_

<a id="atom-technical-atom-68b753908d337989"></a>
```
(diameter) => {
const PI = 3.14159265;
return diameter * PI
}
```
