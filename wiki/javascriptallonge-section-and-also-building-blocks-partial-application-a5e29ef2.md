---
page_id: javascriptallonge-section-and-also-building-blocks-partial-application-a5e29ef2
page_kind: source
summary: And also: / Building Blocks / partial application: 15 source-backed entries and 5 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-01
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-and-also-building-blocks-partial-application-a5e29ef2@1f263b625a52de1fdd092c28050b31e2
---

# And also: / Building Blocks / partial application

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-and-also-building-blocks-d30b6215]] - broader source section: And also: / Building Blocks
- [[javascriptallonge-section-and-also-building-blocks-composition-b488e601]] - previous source section: And also: / Building Blocks / composition
- [[javascriptallonge-partial-application]] - topic hub: opens the topic page for Partial Application

## Statements

- Another basic building block is partial application . When a function takes multiple arguments, we 'apply' the function to the arguments by evaluating it with all of the arguments, producing a value. But what if we only supply some of the arguments? In that case, we can't get the final value, but we can get a function that represents part of our application. _(javascriptallonge.pdf (source-range-0e12e052-00586))_
- Code is easier than words for this. The Underscore 39 library provides a higher-order function called map . 40 It applies another function to each element of an array, like this: _(javascriptallonge.pdf (source-range-0e12e052-00587))_
- The resulting functionsquareAll -is still the map function, it's just that we've applied one of its two arguments already. squareAll is nice, but why write one function every time we want to partially apply a function to a map? We can abstract this one level higher. mapWith takes any function as an argument and returns a partially applied map function. _(javascriptallonge.pdf (source-range-0e12e052-00592))_
- We'll discuss mapWith again. The important thing to see is that partial application is orthogonal to composition, and that they both work together nicely: _(javascriptallonge.pdf (source-range-0e12e052-00594))_
- Wegeneralized composition with the compose combinator. Partial application also has a combinator, which we'll see in the partial recipe. _(javascriptallonge.pdf (source-range-0e12e052-00598))_

## Technical atoms

### Technical frame 1: And also: / Building Blocks / partial application

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00592))_

> The resulting functionsquareAll -is still the map function, it's just that we've applied one of its two arguments already. squareAll is nice, but why write one function every time we want to partially apply a function to a map? We can abstract this one level higher. mapWith takes any function as an argument and returns a partially applied map function.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00588))_

```
_.map([1, 2, 3], (n) => n * n)
//=> [1, 4, 9]
```

### Technical frame 2: And also: / Building Blocks / partial application

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00592))_

> The resulting functionsquareAll -is still the map function, it's just that we've applied one of its two arguments already. squareAll is nice, but why write one function every time we want to partially apply a function to a map? We can abstract this one level higher. mapWith takes any function as an argument and returns a partially applied map function.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00591))_

```
const squareAll = (array) => map(array,
(n) => n * n);
```

### Technical frame 3: And also: / Building Blocks / partial application

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00598))_

> Wegeneralized composition with the compose combinator. Partial application also has a combinator, which we'll see in the partial recipe.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00595))_

```text
39 http://underscorejs.org
41 If we don't want to sort out Underscore, we can also write the following: const map = (a, fn) => a.map(fn); , and trust that it works even though we haven't discussed methods yet.
40 Modern JavaScript implementations provide a map method for arrays, but Underscore's implementation also works with older browsers if you are working with that headache.
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 39 | http://underscorejs.org |
| 41 | If we don't want to sort out Underscore, we can also write the following: const map = (a, fn) => a.map(fn);, and trust that it works even though we haven't discussed methods yet. |
| 40 | Modern JavaScript implementations provide a map method for arrays, but Underscore's implementation also works with older browsers if you are working with that headache. |

</details>

### Technical frame 4: And also: / Building Blocks / partial application

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00598))_

> Wegeneralized composition with the compose combinator. Partial application also has a combinator, which we'll see in the partial recipe.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00596))_

```
const safeSquareAll = mapWith(maybe((n) => n * n));
```

### Technical frame 5: And also: / Building Blocks / partial application

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00598))_

> Wegeneralized composition with the compose combinator. Partial application also has a combinator, which we'll see in the partial recipe.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00597))_

```
safeSquareAll([1, null, 2, 3])
//=> [1, null, 4, 9]
```
