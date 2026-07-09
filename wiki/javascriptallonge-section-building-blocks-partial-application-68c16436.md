---
page_id: javascriptallonge-section-building-blocks-partial-application-68c16436
page_kind: source
summary: Building Blocks / partial application: 14 source-backed entries and 4 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-building-blocks-partial-application-68c16436@dcc7f65ffcb48fc0d9dbdc2a4dceba54
---

# Building Blocks / partial application

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-building-blocks-composition-ed84a096]] - previous source section: Building Blocks / composition

### Source structure

- [[javascriptallonge-section-building-blocks-fdb3fcfb]] - broader source section: Building Blocks

### Recipes

- [[javascriptallonge-recipe-partial-application-68c16436]] - recipe pattern: partial application

### Topics

- [[javascriptallonge-partial-application]] - topic hub: opens the topic page for Partial Application

## Statements

- Another basic building block is partial application . When a function takes multiple arguments, we 'apply' the function to the arguments by evaluating it with all of the arguments, producing a value. But what if we only supply some of the arguments? In that case, we can't get the final value, but we can get a function that represents part of our application. _(javascriptallonge.pdf (source-range-c98ab3e6-00576))_
- Code is easier than words for this. The Underscore 39 library provides a higher-order function called map . 40 It applies another function to each element of an array, like this: _(javascriptallonge.pdf (source-range-c98ab3e6-00577))_
- The resulting functionsquareAll -is still the map function, it's just that we've applied one of its two arguments already. squareAll is nice, but why write one function every time we want to partially apply a function to a map? We can abstract this one level higher. mapWith takes any function as an argument and returns a partially applied map function. _(javascriptallonge.pdf (source-range-c98ab3e6-00582))_
- We'll discuss mapWith again. The important thing to see is that partial application is orthogonal to composition, and that they both work together nicely: _(javascriptallonge.pdf (source-range-c98ab3e6-00584))_
- Wegeneralized composition with the compose combinator. Partial application also has a combinator, which we'll see in the partial recipe. _(javascriptallonge.pdf (source-range-c98ab3e6-00588))_

## Technical atoms

### Technical frame 1: Building Blocks / partial application

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00582))_

> The resulting functionsquareAll -is still the map function, it's just that we've applied one of its two arguments already. squareAll is nice, but why write one function every time we want to partially apply a function to a map? We can abstract this one level higher. mapWith takes any function as an argument and returns a partially applied map function.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00578))_

<a id="atom-technical-atom-bbed966728159c94"></a>
```
_.map([1, 2, 3], (n) => n * n)
//=> [1, 4, 9]
```

### Technical frame 2: Building Blocks / partial application

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00582))_

> The resulting functionsquareAll -is still the map function, it's just that we've applied one of its two arguments already. squareAll is nice, but why write one function every time we want to partially apply a function to a map? We can abstract this one level higher. mapWith takes any function as an argument and returns a partially applied map function.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00581))_

<a id="atom-technical-atom-2d776dba8a34bc3d"></a>
```
const squareAll = (array) => map(array,
(n) => n * n);
```

### Technical frame 3: Building Blocks / partial application

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00588))_

> Wegeneralized composition with the compose combinator. Partial application also has a combinator, which we'll see in the partial recipe.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00586))_

<a id="atom-technical-atom-4c6ddb25dada617c"></a>
```
const safeSquareAll = mapWith(maybe((n) => n * n));
```

### Technical frame 4: Building Blocks / partial application

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00588))_

> Wegeneralized composition with the compose combinator. Partial application also has a combinator, which we'll see in the partial recipe.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00587))_

<a id="atom-technical-atom-408027f80e85f349"></a>
```
safeSquareAll([1, null, 2, 3])
//=> [1, null, 4, 9]
```
