---
page_id: javascriptallonge-recipe-values-are-expressions
page_kind: recipe
summary: values are expressions: reusable source-backed pattern with 19 statement(s) and 6 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: values-are-expressions
projection_coverage: recipe-javascriptallonge-recipe-values-are-expressions@19c450c04f8bc1b4631dde533d6003d9
---

# values are expressions

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-prelude-values-and-expressions-over-coffee-values-are-expressions-b4b22fa2]].
- Evidence roles: decision, constraint, explanation, structured-state, example.

## Applicability And Rationale

- All values are expressions. _(javascriptallonge.pdf (source-range-c98ab3e6-00099))_
- You say, 'I want one of these.' The barista is no fool, she gives it straight back to you, and you get exactly what you want. _(javascriptallonge.pdf (source-range-c98ab3e6-00099))_
- Yup, you hand over a cup with some coffee infused through partially caramelized sugar. _(javascriptallonge.pdf (source-range-c98ab3e6-00099))_
- Thus, a café Cubano is an expression (you can use it to place an order) and a value (you get it back from the barista). _(javascriptallonge.pdf (source-range-c98ab3e6-00099))_
- The answer is, this is both an expression and a value. _(javascriptallonge.pdf (source-range-c98ab3e6-00103))_
- All values are expressions. _(javascriptallonge.pdf (source-range-c98ab3e6-00105))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00104)_

```
42
//=> 42
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00109)_

```
"JavaScript" + " " + "Allonge"
//=> "JavaScript Allonge"
```

### Atom 3: `worked-example`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00111)_

```
Nowwesee that 'strings' are values, and you can make an expression out of strings and an operator + . Since strings are values, they are also expressions by themselves. But strings with operators are not values, they are expressions. Now we know what was missing with our 'coffee grounds plus hot water' example. The coffee grounds were a value, the boiling hot water was a value, and the 'plus' operator between them made the whole thing an expression that was not a value.
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00114)_

```
2 === 2
//=> true
'hello' !== 'goodbye'
//=> true
```

### Atom 5: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00117)_

```
2 === '2'
//=> false
true !== 'true'
//=> true
```

### Atom 6: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00119)_

```
true === false
//=> false
2 !== 5
//=> true
'two' === 'five'
//=> false
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-prelude-values-and-expressions-over-coffee-values-are-expressions-b4b22fa2]]
