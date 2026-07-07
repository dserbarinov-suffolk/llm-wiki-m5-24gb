---
page_id: javascriptallonge-section-and-also-building-blocks-composition-ed84a096
page_kind: source
summary: And also: / Building Blocks / composition: 15 source-backed entries and 4 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-and-also-building-blocks-composition-ed84a096@e2f04770a2b2ff8568a489b24ec62ada
---

# And also: / Building Blocks / composition

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-and-also-building-blocks-partial-application-68c16436]] - next source section: And also: / Building Blocks / partial application

### Source structure

- [[javascriptallonge-section-and-also-building-blocks-fdb3fcfb]] - broader source section: And also: / Building Blocks

## Statements

- It's really that simple: Whenever you are chaining two or more functions together, you're composing them. You can compose them with explicit JavaScript code as we've just done. You can also generalize composition with the B Combinator or 'compose' that we saw in Combinators and Decorators: _(javascriptallonge.pdf (source-range-c98ab3e6-00569))_
- If that was all there was to it, composition wouldn't matter much. But like many patterns, using it when it applies is only 20% of the benefit. The other 80% comes from organizing your code such that you can use it: Writing functions that can be composed in various ways. _(javascriptallonge.pdf (source-range-c98ab3e6-00571))_
- In the recipes, we'll look at a decorator called once: It ensures that a function can only be executed once. Thereafter, it does nothing. Once is useful for ensuring that certain side effects are not repeated. We'll also look at maybe: It ensures that a function does nothing if it is given nothing (like null or undefined ) as an argument. _(javascriptallonge.pdf (source-range-c98ab3e6-00572))_
- Of course, you needn't use combinators to implement either of these ideas, you can use if statements. But once and maybe compose, so you can chain them together as you see fit: _(javascriptallonge.pdf (source-range-c98ab3e6-00573))_
- But like many patterns, using it when it applies is only 20% of the benefit. _(javascriptallonge.pdf (source-range-c98ab3e6-00571))_
- In the recipes, we'll look at a decorator called once: It ensures that a function can only be executed once. _(javascriptallonge.pdf (source-range-c98ab3e6-00572))_

## Technical atoms

### Technical frame 1: And also: / Building Blocks / composition

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00569))_

> It's really that simple: Whenever you are chaining two or more functions together, you're composing them. You can compose them with explicit JavaScript code as we've just done. You can also generalize composition with the B Combinator or 'compose' that we saw in Combinators and Decorators:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00568))_

<a id="atom-technical-atom-42e6b43d90db5e45"></a>
```
const cookAndEat = (food) => eat(cook(food));
```

### Technical frame 2: And also: / Building Blocks / composition

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00571))_

> If that was all there was to it, composition wouldn't matter much. But like many patterns, using it when it applies is only 20% of the benefit. The other 80% comes from organizing your code such that you can use it: Writing functions that can be composed in various ways.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00570))_

<a id="atom-technical-atom-70f9079dd32050af"></a>
```
const compose = (a, b) => (c) => a(b(c));
const cookAndEat = compose(eat, cook);
```

### Technical frame 3: And also: / Building Blocks / composition

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00572))_

> In the recipes, we'll look at a decorator called once: It ensures that a function can only be executed once. Thereafter, it does nothing. Once is useful for ensuring that certain side effects are not repeated. We'll also look at maybe: It ensures that a function does nothing if it is given nothing (like null or undefined ) as an argument.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00571))_

<a id="atom-technical-atom-cfaa3155b7ac1dea"></a>
> The other 80% comes from organizing your code such that you can use it: Writing functions that can be composed in various ways.

### Technical frame 4: And also: / Building Blocks / composition

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00572))_

> In the recipes, we'll look at a decorator called once: It ensures that a function can only be executed once. Thereafter, it does nothing. Once is useful for ensuring that certain side effects are not repeated. We'll also look at maybe: It ensures that a function does nothing if it is given nothing (like null or undefined ) as an argument.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00573))_

<a id="atom-technical-atom-4f6b1bb5af0460d2"></a>
> Of course, you needn't use combinators to implement either of these ideas, you can use if statements.
