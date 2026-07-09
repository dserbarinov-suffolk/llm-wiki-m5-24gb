---
page_id: javascriptallonge-it-s-always-the-environment
page_kind: concept
summary: it's always the environment: 10 accepted assertion(s) and 5 technical atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-state-tps_d9b84c4899974259@76f2c11fe97d294d0d14c057ba089bd5
---

# it's always the environment

Source: [[javascriptallonge]]

## Statements

- As we've said before, all functions are associated with an environment. (javascriptallonge.pdf p.46)
- To understand how closures are evaluated, we need to revisit environments. (javascriptallonge.pdf p.46)
- We also hand- waved something when describing our environment. (javascriptallonge.pdf p.46)
- Some people get so excited by this that they write entire books about them, some are great a , some-how shall I put this-are interesting b if you use Ruby. (javascriptallonge.pdf p.46)
- (x) => x is called the I Combinator, or the Identity Function . (javascriptallonge.pdf p.46)
- (x) => (y) => x is called the K Combinator, or Kestrel . (javascriptallonge.pdf p.46)
- The other big difference is that you can call it with (1) and get a function back that you can later call with (2)(3) . (javascriptallonge.pdf p.46)
- Some programming languages automatically curry and partially evaluate functions without the need to manually nest them. (javascriptallonge.pdf p.47)
- The first function is the result of currying a the second function. (javascriptallonge.pdf p.47)
- Calling a curried function with only some of its arguments is sometimes called partial application b . (javascriptallonge.pdf p.47)

## Technical atoms

<a id="atom-1"></a>
**Atom:** rule

```
So whenever a function is applied to arguments, its environment always has a reference to its parent environment.
```

<a id="atom-2"></a>
**Atom:** code block

```
bh
```

<a id="atom-3"></a>
**Atom:** code block

```
(x) =>
(y) =>
(z) => x + y + z
```

<a id="atom-4"></a>
**Atom:** code block

```
(x, y, z) => x + y + z
```

<a id="atom-5"></a>
**Atom:** code block

```
ah
bh
```
