---
page_id: javascriptallonge-recipe-the-vireo
page_kind: recipe
summary: the vireo: reusable source-backed pattern with 8 statement(s) and 4 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: the-vireo
projection_coverage: recipe-javascriptallonge-recipe-the-vireo@38ac248fe770d39040c5c852b0585d58
---

# the vireo

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-the-vireo-15cde3c9]].
- Evidence roles: decision, procedure, example, structured-state.

## Applicability And Rationale

- Given that our latin data is represented as the function (selector) => selector("primus")("secundus") , our obvious next step is to make a function that makes data. _(javascriptallonge.pdf (source-range-c98ab3e6-01338))_
- In both cases, we take two parameters, and return the form of the data. _(javascriptallonge.pdf (source-range-c98ab3e6-01338))_
- For 'data' we access with K and K(I) , our 'structure' is the function (selector) => selector("primus")("secundus") . _(javascriptallonge.pdf (source-range-c98ab3e6-01339))_
- For consistency with the way combinators are written as functions taking just one parameter, we'll curry 78 the function: _(javascriptallonge.pdf (source-range-c98ab3e6-01341))_
- It says, 'take these two values and apply them to this function.' There are other, similar combinators that apply values to functions. _(javascriptallonge.pdf (source-range-c98ab3e6-01348))_
- As an aside, the Vireo is a little like JavaScript's .apply function. _(javascriptallonge.pdf (source-range-c98ab3e6-01348))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01340)_

```
(first, second) => (selector) => selector(first)(second)
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01342)_

```
(first) => (second) => (selector) => selector(first)(second)
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01344)_

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

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01347)_

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

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-the-vireo-15cde3c9]]
