---
page_id: javascriptallonge-recipe-a-return-to-backward-thinking
page_kind: recipe
summary: a return to backward thinking: reusable source-backed pattern with 16 statement(s) and 3 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: a-return-to-backward-thinking
projection_coverage: recipe-javascriptallonge-recipe-a-return-to-backward-thinking@85031d14b4586e967b866c59423b77cf
---

# a return to backward thinking

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-copy-on-write-making-data-out-of-functions-a-return-to-backward-thinking-f261e0bd]].
- Evidence roles: decision, constraint, explanation, example.

## Applicability And Rationale

- To make pairs work, we did things backwards , we passed the first and rest functions to the pair, and the pair called our function. _(javascriptallonge.pdf (source-range-0e12e052-01404))_
- We could have written a pair that stored its elements in an array, or a pair that stored its elements in a POJO. _(javascriptallonge.pdf (source-range-0e12e052-01405))_
- But we could have done something completely different. _(javascriptallonge.pdf (source-range-0e12e052-01405))_
- All we know is that we can pass the pair function a function of our own, at it will be called with the elements of the pair. _(javascriptallonge.pdf (source-range-0e12e052-01405))_
- The exact implementation of a pair is hidden from the code that uses a pair. _(javascriptallonge.pdf (source-range-0e12e052-01406))_
- This is a little gratuitous, but it makes the point: The code that uses the data doesn't reach in and touch it: The code that uses the data provides some code and asks the data to do something with it. _(javascriptallonge.pdf (source-range-0e12e052-01408))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-01407)_

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

_Source: javascriptallonge.pdf (source-range-0e12e052-01410)_

```
const length = (list) => list(
() => 0,
(aPair) => 1 + length(aPair(pairRest)))
);
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-01413)_

```
const length = (node, delayed = 0) =>
node === EMPTY
? delayed
: length(node.rest, delayed + 1);
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-copy-on-write-making-data-out-of-functions-a-return-to-backward-thinking-f261e0bd]]
