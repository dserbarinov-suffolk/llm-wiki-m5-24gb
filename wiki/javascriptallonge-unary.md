---
page_id: javascriptallonge-unary
page_kind: concept
summary: Unary: 7 accepted assertion(s) and 6 technical atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-state-tps_7d54fb19476e82a2@5095ec9658c64ada2e189ec40888ac4b
---

# Unary

Source: [[javascriptallonge]]

## Statements

- The most common use case is to fix a problem. (javascriptallonge.pdf p.82)
- JavaScript has a .map method for arrays, and many libraries offer a map function with the same semantics. (javascriptallonge.pdf p.82)
- But some functions have optional second or even third arguments. (javascriptallonge.pdf p.82)
- And when you call parseInt with map , the index is interpreted as a radix. (javascriptallonge.pdf p.82)
- What we want is to convert parseInt into a function taking only one argument. (javascriptallonge.pdf p.82)
- This doesn't work because parseInt is defined as parseInt(string[, radix]) . (javascriptallonge.pdf p.82)
- Wecould write ['1', '2', '3'].map((s) => parseInt(s)) , or we could come up with a decorator to do the job for us:. (javascriptallonge.pdf p.82)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

```
['1', '2', '3'].map(parseFloat)
//=> [1, 2, 3]
```

<a id="atom-2"></a>
**Atom:** code block

```
[1, 2, 3].map(function (element, index, arr) {
console.log({element: element, index: index, arr: arr})
})
//=> { element: 1, index: 0, arr: [ 1, 2, 3 ] }
//
{ element: 2, index: 1, arr: [ 1, 2, 3 ] }
//
{ element: 3, index: 2, arr: [ 1, 2, 3 ] }
```

<a id="atom-3"></a>
**Atom:** rule

```
If you pass in a function taking only one argument, it simply ignores the additional arguments.
```

<a id="atom-4"></a>
**Atom:** code block

```
['1', '2', '3'].map(parseInt)
//=> [1, NaN, NaN]
```

<a id="atom-5"></a>
**Atom:** code block

```
const unary = (fn) =>
fn.length === 1
? fn
: function (something) {
return fn.call(this, something)
}
```

<a id="atom-6"></a>
**Atom:** code block

```
['1', '2', '3'].map(unary(parseInt))
//=> [1, 2, 3]
```
