---
page_id: javascriptallonge-summary
page_kind: concept
summary: summary: 18 accepted assertion(s) and 0 technical atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-state-tps_5e534a35d0de9466@98d967c3280a5cfe7d4e1f79e48fa865
---

# summary

Source: [[javascriptallonge]]

## Statements

- Logical operators are based on truthiness and falsiness, not the strict values true and false . (javascriptallonge.pdf p.99)
- The ternary operator ( ?: ), || , and && are control flow operators, they do not always return true or false , and they have short-cut semantics. (javascriptallonge.pdf p.99)
- Function invocation uses eager evaluation, so if we need to roll our own control-flow semantics, we pass it functions, not expressions. (javascriptallonge.pdf p.99)
- Linear recursion is a basic building block of algorithms. (javascriptallonge.pdf p.116)
- Its basic form parallels the way linear data structures like lists are constructed: This helps make it understandable. (javascriptallonge.pdf p.116)
- Its specialized cases of mapping and folding are especially useful and can be used to build other functions. (javascriptallonge.pdf p.116)
- And finally, while folding is a special case of linear recursion, mapping is a special case of folding. (javascriptallonge.pdf p.116)
- Although we showed how to use tail calls to map and fold over arrays with [first, ..rest] , in reality this is not how it ought to be done. (javascriptallonge.pdf p.131)
- But it is an extremely simple illustration of how recursion works when you have a self-similar means of constructing a data structure. (javascriptallonge.pdf p.131)
- Iterators are a JavaScript feature that allow us to separate the concerns of how to iterate over a collection from what we want to do with the elements of a collection. (javascriptallonge.pdf p.223)
- Iterable ordered collections can be iterated over or gathered into another collection. (javascriptallonge.pdf p.223)
- Separating concerns with iterators speaks to JavaScript's fundamental nature: It's a language that wants to compose functionality out of small, singe-responsibility pieces, whether those pieces are functions or objects built out of functions. (javascriptallonge.pdf p.223)
- And we don't need to worry about wrapping our values in an object with .done and .value properties. (javascriptallonge.pdf p.245)
- Using a generator instead of writing an iterator object that has a .next() method allows us to write code that can be much simpler for cases like recursive iterations or state patterns. (javascriptallonge.pdf p.245)
- A generator is a function that is defined with function * and uses yield (or yield * ) to generate values. (javascriptallonge.pdf p.245)
- This is especially useful for making iterables. (javascriptallonge.pdf p.245)
- We have looked at generators as ways of making iterators over static collections, where state is modelled implicitly in control flow. (javascriptallonge.pdf p.283)
- Again, the salient difference is that an 'interactive' generator is stateful, and it embodies its state in its control flow. (javascriptallonge.pdf p.283)
