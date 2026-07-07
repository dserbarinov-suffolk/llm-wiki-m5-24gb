---
page_id: javascriptallonge-section-closures-and-scope-a674d15d
page_kind: source
summary: Closures and Scope: 11 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-closures-and-scope-a674d15d@6c8ace3c72c71fc4e05f40f8e494a7d6
---

# Closures and Scope

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-call-by-sharing-4054593f]] - previous source section: call by sharing
- [[javascriptallonge-section-if-functions-without-free-variables-are-pure-are-closures-impure-7e6951b6]] - next source section: if functions without free variables are pure, are closures impure?

## Statements

- The environment belonging to the function with signature (x) => ... becomes {x: 1, ...} , and the result of applying the function is another function value. It makes sense that the result value is a function, because the expression for (x) => ... 's body is: _(javascriptallonge.pdf (source-range-c98ab3e6-00320))_
- So now we have a value representing that function. Then we're going to take the value of that function and apply it to the argument 2 , something like this: _(javascriptallonge.pdf (source-range-c98ab3e6-00322))_
- So we seem to get a new environment {y: 2, ...} . How is the expression x going to be evaluated in that function's environment? There is no x in its environment, it must come from somewhere else. _(javascriptallonge.pdf (source-range-c98ab3e6-00324))_
- This, by the way, is one of the great defining characteristics of JavaScript and languages in the same family: Whether they allow things like functions to nest inside each other, and if so, how they handle variables from 'outside' of a function that are referenced inside a function. For example, here's the equivalent code in Ruby: _(javascriptallonge.pdf (source-range-c98ab3e6-00325))_
- It makes sense that the result value is a function, because the expression for (x) => ... _(javascriptallonge.pdf (source-range-c98ab3e6-00320))_
- This, by the way, is one of the great defining characteristics of JavaScript and languages in the same family: Whether they allow things like functions to nest inside each other, and if so, how they handle variables from 'outside' of a function that are referenced inside a function. _(javascriptallonge.pdf (source-range-c98ab3e6-00325))_
