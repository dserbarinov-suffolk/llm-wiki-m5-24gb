---
page_id: javascriptallonge-recipe-the-vireo
page_kind: recipe
summary: the vireo: reusable source-backed pattern with 8 statement(s) and 4 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-01
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: the-vireo
projection_coverage: recipe-javascriptallonge-recipe-the-vireo@79bd17eea2485cd2fc6c9d930ed64a05
---

# the vireo

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-copy-on-write-making-data-out-of-functions-the-vireo-b7923ab5]].
- Evidence roles: decision, procedure, example, structured-state.

## Applicability And Rationale

- In both cases, we take two parameters, and return the form of the data. _(javascriptallonge.pdf (source-range-0e12e052-01359))_
- Given that our latin data is represented as the function (selector) => selector("primus")("secundus") , our obvious next step is to make a function that makes data. _(javascriptallonge.pdf (source-range-0e12e052-01359))_
- For 'data' we access with K and K(I) , our 'structure' is the function (selector) => selector("primus")("secundus") . _(javascriptallonge.pdf (source-range-0e12e052-01360))_
- For consistency with the way combinators are written as functions taking just one parameter, we'll curry 78 the function: _(javascriptallonge.pdf (source-range-0e12e052-01362))_
- It says, 'take these two values and apply them to this function.' There are other, similar combinators that apply values to functions. _(javascriptallonge.pdf (source-range-0e12e052-01369))_
- It is known to most programmers as .tap . _(javascriptallonge.pdf (source-range-0e12e052-01369))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-01361)_

```
(first, second) => (selector) => selector(first)(second)
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-01363)_

```
(first) => (second) => (selector) => selector(first)(second)
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-01365)_

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

_Source: javascriptallonge.pdf (source-range-0e12e052-01368)_

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
- Source section: [[javascriptallonge-section-copy-on-write-making-data-out-of-functions-the-vireo-b7923ab5]]
