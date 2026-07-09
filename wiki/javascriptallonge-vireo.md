---
page_id: javascriptallonge-vireo
page_kind: concept
summary: topic-concept: 15 supported fragment(s) and 2 related link(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: page-projection-pgp_b18c52e65361d83c@0604a090a4e7e335e221eb3aa26bc996
---

# the vireo

Source: [[javascriptallonge]]

## Statements

- Given that our latin data is represented as the function (selector) => selector("primus")("secundus") , our obvious next step is to make a function that makes data. (javascriptallonge.pdf p.182)
- In both cases, we take two parameters, and return the form of the data. (javascriptallonge.pdf p.182)
- For 'data' we access with K and K(I) , our 'structure' is the function (selector) => selector("primus")("secundus") . (javascriptallonge.pdf p.182)
- For consistency with the way combinators are written as functions taking just one parameter, we'll curry 78 the function:. (javascriptallonge.pdf p.182)
- It says, 'take these two values and apply them to this function.' There are other, similar combinators that apply values to functions. (javascriptallonge.pdf p.183)
- As an aside, the Vireo is a little like JavaScript's .apply function. (javascriptallonge.pdf p.183)
- It is known to most programmers as .tap . (javascriptallonge.pdf p.183)
- One notable example is the 'thrush' or T combinator: It takes one value and applies it to a function. (javascriptallonge.pdf p.183)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

```
(first, second) => (selector) => selector(first)(second)
```

<a id="atom-2"></a>
**Atom:** code block

```
(first) => (second) => (selector) => selector(first)(second)
```

<a id="atom-3"></a>
**Atom:** code block

```
const first = K,
second = K(I),
pair = (first) => (second) => (selector) => selector(first)(second);
const latin = pair("primus")("secundus");
latin(first)
//=> "primus"
latin(second)
//=> "secundus"
```

<a id="atom-4"></a>
**Atom:** rule

```
If we change the names to x , y , and z , we get: (x) => (y) => (z) => z(x)(y) .
```

<a id="atom-5"></a>
**Atom:** code block

```
const first = K,
second = K(I),
pair = V;
const latin = pair("primus")("secundus");
latin(first)
//=> "primus"
latin(second)
//=> "secundus"
```


## Related pages

- [[javascriptallonge-backwardnes]] - contextualizes: source-supported topic dependency
- [[javascriptallonge-lists-with-functions-as-data]] - contextualizes: source-supported topic dependency
