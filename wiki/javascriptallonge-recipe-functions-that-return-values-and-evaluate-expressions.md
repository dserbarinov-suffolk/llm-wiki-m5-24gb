---
page_id: javascriptallonge-recipe-functions-that-return-values-and-evaluate-expressions
page_kind: recipe
summary: functions that return values and evaluate expressions: reusable source-backed pattern with 6 statement(s) and 4 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: functions-that-return-values-and-evaluate-expressions
projection_coverage: recipe-javascriptallonge-recipe-functions-that-return-values-and-evaluate-expressions@3983656e6503654bbbc5fe125929f088
---

# functions that return values and evaluate expressions

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-the-first-sip-basic-functions-as-little-as-possible-about-functions-but-no-less-functions-that-r-a65d460b]].
- Evidence roles: decision, constraint, explanation, example.

## Applicability And Rationale

- We know that (() => 0)() returns 0 , and this is unsurprising. _(javascriptallonge.pdf (source-range-c98ab3e6-00182))_
- In the prelude, we looked at expressions. _(javascriptallonge.pdf (source-range-c98ab3e6-00185))_
- Values like 0 are expressions, as are things like 40 + 2 . _(javascriptallonge.pdf (source-range-c98ab3e6-00185))_
- We can put any expression to the right of the arrow. _(javascriptallonge.pdf (source-range-c98ab3e6-00187))_
- For example, (() => 0)() is an expression. _(javascriptallonge.pdf (source-range-c98ab3e6-00187))_
- Functions can return the value of evaluating another function. _(javascriptallonge.pdf (source-range-c98ab3e6-00190))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00183)_

```
(() => 1)()
//=> 1
(() => "Hello, JavaScript")()
//=> "Hello, JavaScript"
(() => Infinity)()
//=> Infinity
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00186)_

```
(() => 1 + 1)()
//=> 2
(() => "Hello, " + "JavaScript")()
//=> "Hello, JavaScript"
(() => Infinity * Infinity)()
//=> Infinity
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00189)_

```
(() => (() => 0)())()
//=> 0
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00192)_

```
(() =>
(() => 0
)()
)()
//=> 0
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-the-first-sip-basic-functions-as-little-as-possible-about-functions-but-no-less-functions-that-r-a65d460b]]
