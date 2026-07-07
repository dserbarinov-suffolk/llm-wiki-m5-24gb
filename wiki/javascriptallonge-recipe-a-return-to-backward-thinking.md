---
page_id: javascriptallonge-recipe-a-return-to-backward-thinking
page_kind: recipe
summary: a return to backward thinking: reusable source-backed pattern with 16 statement(s) and 3 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: a-return-to-backward-thinking
projection_coverage: recipe-javascriptallonge-recipe-a-return-to-backward-thinking@989aad8ee29e7e60f6a000461c297b40
---

# a return to backward thinking

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-making-data-out-of-functions-a-return-to-backward-thinking-0d028ef6]].
- Evidence roles: decision, constraint, explanation, example.

## Applicability And Rationale

- To make pairs work, we did things backwards , we passed the first and rest functions to the pair, and the pair called our function. _(javascriptallonge.pdf (source-range-c98ab3e6-01383))_
- But we could have done something completely different. _(javascriptallonge.pdf (source-range-c98ab3e6-01384))_
- All we know is that we can pass the pair function a function of our own, at it will be called with the elements of the pair. _(javascriptallonge.pdf (source-range-c98ab3e6-01384))_
- We could have written a pair that stored its elements in an array, or a pair that stored its elements in a POJO. _(javascriptallonge.pdf (source-range-c98ab3e6-01384))_
- The exact implementation of a pair is hidden from the code that uses a pair. _(javascriptallonge.pdf (source-range-c98ab3e6-01385))_
- This is a little gratuitous, but it makes the point: The code that uses the data doesn't reach in and touch it: The code that uses the data provides some code and asks the data to do something with it. _(javascriptallonge.pdf (source-range-c98ab3e6-01387))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01386)_

```
const first = K,
second = K(I),
pair = (first) => (second) => {
const pojo = {first, second};
return (selector) => selector(pojo.first)(pojo.second);
};
const latin = pair("primus")("secundus");
latin(first)
//=> "primus"
latin(second)
//=> "secundus"
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01389)_

```
const length = (list) => list(
() => 0,
(aPair) => 1 + length(aPair(pairRest)))
);
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01392)_

```
const length = (node, delayed = 0) =>
node === EMPTY
? delayed
: length(node.rest, delayed + 1);
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-making-data-out-of-functions-a-return-to-backward-thinking-0d028ef6]]
