---
page_id: javascriptallonge-functions-that-evaluate-to-functions
page_kind: concept
summary: functions that evaluate to functions: 4 accepted assertion(s) and 5 technical atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-state-tps_30641c1eaedede4b@aa8a42c7772f878e86074e179eae96b2
---

# functions that evaluate to functions

Source: [[javascriptallonge]]

## Statements

- It's a function that when applied , evaluates to a function that when applied, evaluates to 0 . (javascriptallonge.pdf p.38)
- So we have a function, that returns a function, that returns zero . (javascriptallonge.pdf p.38)
- Diffraction of a crystal is beautiful and interesting in its own right, but you can't blame us for wanting to be shown a practical use for it, like being able to determine the composition of a star millions of light years away. (javascriptallonge.pdf p.38)
- We've been very clever, but so far this all seems very abstract. (javascriptallonge.pdf p.38)

## Technical atoms

<a id="atom-1"></a>
**Atom:** rule

```
If an expression that evaluates to a function is, well, an expression, and if a return statement can have any expression on its right side… Can we put an expression that evaluates to a function on the right side of a function expression?
```

<a id="atom-2"></a>
**Atom:** code block

```
() => () => 0
```

<a id="atom-3"></a>
**Atom:** code block

```
() => () => true
```

<a id="atom-4"></a>
**Atom:** code block

```
(() => () => true)()()
//=> true
```

<a id="atom-5"></a>
**Atom:** code block

```
() => () => { return true; }
```
