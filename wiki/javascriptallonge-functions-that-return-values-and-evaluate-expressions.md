---
page_id: javascriptallonge-functions-that-return-values-and-evaluate-expressions
page_kind: concept
summary: topic-concept: 14 supported fragment(s) and 1 related link(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: page-projection-pgp_5122fe3f9c7c3d61@6415aef888b9d00b0eb602b9448f21c0
---

# functions that return values and evaluate expressions

Source: [[javascriptallonge]]

## Statements

- We know that (() => 0)() returns 0 , and this is unsurprising. (javascriptallonge.pdf p.32)
- In the prelude, we looked at expressions. (javascriptallonge.pdf p.32)
- Values like 0 are expressions, as are things like 40 + 2 . (javascriptallonge.pdf p.32)
- We can put any expression to the right of the arrow. (javascriptallonge.pdf p.32)
- For example, (() => 0)() is an expression. (javascriptallonge.pdf p.32)
- Functions can return the value of evaluating another function. (javascriptallonge.pdf p.32)

## Rules

- We can put any expression to the right of the arrow. (javascriptallonge.pdf p.32)
- Functions can return the value of evaluating another function. (javascriptallonge.pdf p.32)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

```
(() => 1)()
//=> 1
(() => "Hello, JavaScript")()
//=> "Hello, JavaScript"
(() => Infinity)()
//=> Infinity
```

<a id="atom-2"></a>
**Atom:** code block

```
(() => 1 + 1)()
//=> 2
(() => "Hello, " + "JavaScript")()
//=> "Hello, JavaScript"
(() => Infinity * Infinity)()
//=> Infinity
```

<a id="atom-3"></a>
**Atom:** code block

```
(() => (() => 0)())()
//=> 0
```

<a id="atom-4"></a>
**Atom:** rule

```
When dealing with expressions that have a lot of the same characters (like parentheses), you may find it helpful to format the code to make things stand out.
```

<a id="atom-5"></a>
**Atom:** code block

```
(() =>
(() => 0
)()
)()
//=> 0
```


## Related pages

- [[javascriptallonge-applying-functions]] - contextualizes: source-supported topic dependency
