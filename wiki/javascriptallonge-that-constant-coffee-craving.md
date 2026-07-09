---
page_id: javascriptallonge-that-constant-coffee-craving
page_kind: concept
summary: That Constant Coffee Craving: 9 accepted assertion(s) and 4 technical atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-state-tps_46401491c74df1eb@670ffd5cc0c1809f44c47782fb47b4b9
---

# That Constant Coffee Craving

Source: [[javascriptallonge]]

## Statements

- Naming things is a critical part of programming, but all we've seen so far is how to name arguments. (javascriptallonge.pdf p.49)
- Up to now, all we've really seen are anonymous functions , functions that don't have a name. (javascriptallonge.pdf p.49)
- This feels very different from programming in most other languages, where the focus is on naming functions, methods, and procedures. (javascriptallonge.pdf p.49)
- In order to bind 3.14159265 to the name PI , we'll need a function with a parameter of PI applied to an argument of 3.14159265 . (javascriptallonge.pdf p.49)
- This expression, when evaluated , returns a function that calculates circumferences. (javascriptallonge.pdf p.49)
- This one has a few more moving parts, that's all. (javascriptallonge.pdf p.49)
- All of our 'functions' are expressions. (javascriptallonge.pdf p.49)
- That sounds bad, but when we think about it, (diameter) => diameter * 3.14159265 is also an expression, that when evaluated, returns a function that calculates circumferences. (javascriptallonge.pdf p.49)
- But we can use it just like (diameter) => diameter * 3.14159265 . (javascriptallonge.pdf p.49)

## Technical atoms

<a id="atom-1"></a>
**Atom:** example

```
There are other ways to name things in JavaScript, but before we learn some of those, let's see how to use what we already have to name things. Let's revisit a very simple example:
```

<a id="atom-2"></a>
**Atom:** code block

```
((PI) =>
// ????
)(3.14159265)
```

<a id="atom-3"></a>
**Atom:** code block

```
((PI) =>
(diameter) => diameter * PI
)(3.14159265)
```

<a id="atom-4"></a>
**Atom:** code block

```
((diameter) => diameter * 3.14159265)(2)
//=> 6.2831853
((PI) =>
(diameter) => diameter * PI
)(3.14159265)(2)
//=> 6.2831853
```
