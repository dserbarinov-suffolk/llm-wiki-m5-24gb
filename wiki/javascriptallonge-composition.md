---
page_id: javascriptallonge-composition
page_kind: concept
summary: composition: 8 accepted assertion(s) and 5 technical atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-state-tps_a4ab9db01f20a4e6@68f8dcde56f7e813f1fe1271708f060f
---

# composition

Source: [[javascriptallonge]]

## Statements

- It's really that simple: Whenever you are chaining two or more functions together, you're composing them. (javascriptallonge.pdf p.71)
- You can compose them with explicit JavaScript code as we've just done. (javascriptallonge.pdf p.71)
- If that was all there was to it, composition wouldn't matter much. (javascriptallonge.pdf p.71)
- But like many patterns, using it when it applies is only 20% of the benefit. (javascriptallonge.pdf p.71)
- In the recipes, we'll look at a decorator called once: It ensures that a function can only be executed once. (javascriptallonge.pdf p.71)
- We'll also look at maybe: It ensures that a function does nothing if it is given nothing (like null or undefined ) as an argument. (javascriptallonge.pdf p.71)
- Once is useful for ensuring that certain side effects are not repeated. (javascriptallonge.pdf p.71)
- But once and maybe compose, so you can chain them together as you see fit:. (javascriptallonge.pdf p.71)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

```
const cookAndEat = (food) => eat(cook(food));
```

<a id="atom-2"></a>
**Atom:** code block

```
const compose = (a, b) => (c) => a(b(c));
const cookAndEat = compose(eat, cook);
```

<a id="atom-3"></a>
**Atom:** rule

```
The other 80% comes from organizing your code such that you can use it: Writing functions that can be composed in various ways.
```

<a id="atom-4"></a>
**Atom:** rule

```
Of course, you needn't use combinators to implement either of these ideas, you can use if statements.
```

<a id="atom-5"></a>
**Atom:** code block

```
const actuallyTransfer= (from, to, amount) =>
// do something
const invokeTransfer = once(maybe(actuallyTransfer(...)));
```
