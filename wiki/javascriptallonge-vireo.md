---
page_id: javascriptallonge-vireo
page_kind: concept
summary: the vireo: 8 accepted assertion(s) and 5 technical atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-state-tps_13832b47e3c6e97d@70fe35048c65ebbb45a424df7f5cf242
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
