---
page_id: javascriptallonge-section-that-constant-coffee-craving-const-37801120
page_kind: source
summary: That Constant Coffee Craving / const: 22 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-that-constant-coffee-craving-const-37801120@76a1f7ee5308745c6fdcc55d3d7cc84e
---

# That Constant Coffee Craving / const

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-that-constant-coffee-craving-inside-out-6df7936c]] - previous source section: That Constant Coffee Craving / inside-out
- [[javascriptallonge-section-that-constant-coffee-craving-nested-blocks-f1c29f4e]] - next source section: That Constant Coffee Craving / nested blocks

### Source structure

- [[javascriptallonge-section-that-constant-coffee-craving-614e2fd3]] - broader source section: That Constant Coffee Craving

### Topics

- [[javascriptallonge-const]] - topic hub: opens the topic page for Const

## Statements

- Another way to write our 'circumference' function would be to pass PI along with the diameter argument, something like this: _(javascriptallonge.pdf (source-range-c98ab3e6-00400))_
- This differs from our example above in that there is only one environment, rather than two. We have one binding in the environment representing our regular argument, and another our 'constant.' That's more efficient, and it's almost what we wanted all along: A way to bind 3.14159265 to a readable name. _(javascriptallonge.pdf (source-range-c98ab3e6-00404))_
- JavaScript gives us a way to do that, the const keyword. We'll learn a lot more about const in future chapters, but here's the most important thing we can do with const : _(javascriptallonge.pdf (source-range-c98ab3e6-00405))_
- The const keyword introduces one or more bindings in the block that encloses it. It doesn't incur the cost of a function invocation. That's great. Even better, it puts the symbol (like PI ) close to the value ( 3.14159265 ). That's much better than what we were writing. _(javascriptallonge.pdf (source-range-c98ab3e6-00407))_
- We use the const keyword in a const statement . const statements occur inside blocks, we can't use them when we write a fat arrow that has an expression as its body. _(javascriptallonge.pdf (source-range-c98ab3e6-00408))_
- We can bind any expression. Functions are expressions, so we can bind helper functions: _(javascriptallonge.pdf (source-range-c98ab3e6-00415))_
- Notice calc(d) ? This underscores what we've said: if we have an expression that evaluates to a function, we apply it with () . A name that's bound to a function is a valid expression evaluating to a function. 30 _(javascriptallonge.pdf (source-range-c98ab3e6-00417))_
- Amazing how such an important idea-naming functions-can be explained en passant in just a few words. That emphasizes one of the things JavaScript gets really, really right: Functions as 'first class entities. ' Functions are values that can be bound to names like any other value, passed as arguments, returned from other functions, and so forth. _(javascriptallonge.pdf (source-range-c98ab3e6-00418))_
- 30 We're into the second chapter and we've finally named a function. Sheesh. _(javascriptallonge.pdf (source-range-c98ab3e6-00421))_
- This differs from our example above in that there is only one environment, rather than two. _(javascriptallonge.pdf (source-range-c98ab3e6-00404))_

## Technical atoms

### Technical frame 1: That Constant Coffee Craving / const

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00407))_

> The const keyword introduces one or more bindings in the block that encloses it. It doesn't incur the cost of a function invocation. That's great. Even better, it puts the symbol (like PI ) close to the value ( 3.14159265 ). That's much better than what we were writing.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00406))_

<a id="atom-technical-atom-0589efc09f36452c"></a>
```
(diameter) => {
const PI = 3.14159265;
return diameter * PI
}
```
