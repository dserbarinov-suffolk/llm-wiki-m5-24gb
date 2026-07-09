---
page_id: javascriptallonge-closures-and-scope
page_kind: concept
summary: topic-concept: 12 supported fragment(s) and 2 related link(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: page-projection-pgp_e607f7ec67998620@6ae7691ae82f541d095d2d3c881d8405
---

# Closures and Scope

Source: [[javascriptallonge]]

## Statements

- It makes sense that the result value is a function, because the expression for (x) => .. (javascriptallonge.pdf p.44)
- So now we have a value representing that function. (javascriptallonge.pdf p.44)
- There is no x in its environment, it must come from somewhere else. (javascriptallonge.pdf p.44)
- This, by the way, is one of the great defining characteristics of JavaScript and languages in the same family: Whether they allow things like functions to nest inside each other, and if so, how they handle variables from 'outside' of a function that are referenced inside a function. (javascriptallonge.pdf p.44)

## Rules

- There is no x in its environment, it must come from somewhere else. (javascriptallonge.pdf p.44)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

```
((x) => (y) => x)(1)(2)
//=> 1
```

<a id="atom-2"></a>
**Atom:** code block

```
((x) => (y) => x)(1)
//=> [Function]
```

<a id="atom-3"></a>
**Atom:** code block

```
(y) => x
```

<a id="atom-4"></a>
**Atom:** code block

```
((y) => x)(2)
```

<a id="atom-5"></a>
**Atom:** code block

```
lambda { |x|
lambda { |y| x }
}[1][2]
#=> 1
```


## Related pages

- [[javascriptallonge-call-by-sharing]] - contextualizes: source-supported topic dependency
- [[javascriptallonge-that-constant-coffee-craving]] - contextualizes: source-supported topic dependency
