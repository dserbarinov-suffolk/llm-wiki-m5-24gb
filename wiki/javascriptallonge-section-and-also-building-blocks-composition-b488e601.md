---
page_id: javascriptallonge-section-and-also-building-blocks-composition-b488e601
page_kind: source
summary: And also: / Building Blocks / composition: 15 source-backed entries and 4 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-01
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-and-also-building-blocks-composition-b488e601@fb63f36817639e6b5a57ff5fc36db9b0
---

# And also: / Building Blocks / composition

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-and-also-building-blocks-d30b6215]] - broader source section: And also: / Building Blocks
- [[javascriptallonge-section-and-also-building-blocks-partial-application-a5e29ef2]] - next source section: And also: / Building Blocks / partial application

## Statements

- It's really that simple: Whenever you are chaining two or more functions together, you're composing them. You can compose them with explicit JavaScript code as we've just done. You can also generalize composition with the B Combinator or 'compose' that we saw in Combinators and Decorators: _(javascriptallonge.pdf (source-range-0e12e052-00579))_
- If that was all there was to it, composition wouldn't matter much. But like many patterns, using it when it applies is only 20% of the benefit. The other 80% comes from organizing your code such that you can use it: Writing functions that can be composed in various ways. _(javascriptallonge.pdf (source-range-0e12e052-00581))_
- In the recipes, we'll look at a decorator called once: It ensures that a function can only be executed once. Thereafter, it does nothing. Once is useful for ensuring that certain side effects are not repeated. We'll also look at maybe: It ensures that a function does nothing if it is given nothing (like null or undefined ) as an argument. _(javascriptallonge.pdf (source-range-0e12e052-00582))_
- Of course, you needn't use combinators to implement either of these ideas, you can use if statements. But once and maybe compose, so you can chain them together as you see fit: _(javascriptallonge.pdf (source-range-0e12e052-00583))_
- But like many patterns, using it when it applies is only 20% of the benefit. _(javascriptallonge.pdf (source-range-0e12e052-00581))_
- In the recipes, we'll look at a decorator called once: It ensures that a function can only be executed once. _(javascriptallonge.pdf (source-range-0e12e052-00582))_

## Technical atoms

### Technical frame 1: And also: / Building Blocks / composition

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00579))_

> It's really that simple: Whenever you are chaining two or more functions together, you're composing them. You can compose them with explicit JavaScript code as we've just done. You can also generalize composition with the B Combinator or 'compose' that we saw in Combinators and Decorators:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00578))_

```
const cookAndEat = (food) => eat(cook(food));
```

### Technical frame 2: And also: / Building Blocks / composition

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00581))_

> If that was all there was to it, composition wouldn't matter much. But like many patterns, using it when it applies is only 20% of the benefit. The other 80% comes from organizing your code such that you can use it: Writing functions that can be composed in various ways.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00580))_

```
const compose = (a, b) => (c) => a(b(c));
const cookAndEat = compose(eat, cook);
```

### Technical frame 3: And also: / Building Blocks / composition

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00582))_

> In the recipes, we'll look at a decorator called once: It ensures that a function can only be executed once. Thereafter, it does nothing. Once is useful for ensuring that certain side effects are not repeated. We'll also look at maybe: It ensures that a function does nothing if it is given nothing (like null or undefined ) as an argument.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00581))_

> The other 80% comes from organizing your code such that you can use it: Writing functions that can be composed in various ways.

### Technical frame 4: And also: / Building Blocks / composition

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00582))_

> In the recipes, we'll look at a decorator called once: It ensures that a function can only be executed once. Thereafter, it does nothing. Once is useful for ensuring that certain side effects are not repeated. We'll also look at maybe: It ensures that a function does nothing if it is given nothing (like null or undefined ) as an argument.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00583))_

> Of course, you needn't use combinators to implement either of these ideas, you can use if statements.
