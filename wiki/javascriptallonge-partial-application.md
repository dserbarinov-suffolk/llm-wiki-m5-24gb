---
page_id: javascriptallonge-partial-application
page_kind: concept
summary: topic-concept: 21 supported fragment(s) and 1 related link(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: page-projection-pgp_10e35733b23224d4@8d472b78c91b23d5203c884169f6160c
---

# partial application

Source: [[javascriptallonge]]

## Procedure

- In that case, we can 't get the final value, but we can get a function that represents part of our application. (javascriptallonge.pdf p.72)
- Another basic building block is partial application . (javascriptallonge.pdf p.72)
- Code is easier than words for this. (javascriptallonge.pdf p.72)
- The Underscore 39 library provides a higher-order function called map . (javascriptallonge.pdf p.72)
- We can abstract this one level higher. (javascriptallonge.pdf p.72)
- The resulting functionsquareAll - is still the map function, it's just that we've applied one of its two arguments already. (javascriptallonge.pdf p.72)
- mapWith takes any function as an argument and returns a partially applied map function. (javascriptallonge.pdf p.72)
- The important thing to see is that partial application is orthogonal to composition, and that they both work together nicely:. (javascriptallonge.pdf p.72)
- Partial application also has a combinator, which we'll see in the partial recipe. (javascriptallonge.pdf p.73)
- 48 If you want to bind more than one argument, or you want to leave a 'hole' in the argument list, you will need to either use a generalized partial recipe, or you will need to repeatedly apply arguments. (javascriptallonge.pdf p.80)
- These two recipes are for quickly and simply applying a single argument, either the leftmost or rightmost. (javascriptallonge.pdf p.80)
- We'd need a different recipe if we wish to create partial applications of object methods. (javascriptallonge.pdf p.80)
- As noted above, our partial recipe allows us to create functions that are partial applications of functions that are context aware. (javascriptallonge.pdf p.80)
- We take it a step further, and can use gathering and spreading to allow for partial application with more than one argument:. (javascriptallonge.pdf p.81)

## Required tables and formulas

<a id="atom-1"></a>
**Atom:** table

```text
39 http://underscorejs.org
41 If we don't want to sort out Underscore, we can also write the following: const map = (a, fn) => a.map(fn); , and trust that it works even though we haven't discussed methods yet.
40 Modern JavaScript implementations provide a map method for arrays, but Underscore's implementation also works with older browsers if you are working with that headache.
```

<a id="atom-2"></a>
**Atom:** table

```text
Partial Application
In Building Blocks, we discussed partial application, but we didn't write a generalized recipe for it. This is such a common tool that many libraries provide some form of partial application. You'll find examples in Lemonad 45 from Michael Fogus, Functional JavaScript 46 from Oliver Steele and the terse but handy node-ap 47 from James Halliday.
```

<a id="atom-3"></a>
**Atom:** table

```text
45 https://github.com/fogus/lemonad 46 http://osteele.com/sources/javascript/functional/ 47 https://github.com/substack/node-ap 48
```


## Rules and exceptions

- In that case, we can 't get the final value, but we can get a function that represents part of our application. (javascriptallonge.pdf p.72)
- We can abstract this one level higher. (javascriptallonge.pdf p.72)
- We take it a step further, and can use gathering and spreading to allow for partial application with more than one argument:. (javascriptallonge.pdf p.81)

## Related pages

- [[javascriptallonge-composition]] - contextualizes: source-supported topic dependency
