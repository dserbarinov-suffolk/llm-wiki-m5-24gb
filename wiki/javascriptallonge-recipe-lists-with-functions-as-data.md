---
page_id: javascriptallonge-recipe-lists-with-functions-as-data
page_kind: recipe
summary: lists with functions as data: reusable source-backed pattern with 4 statement(s) and 3 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: lists-with-functions-as-data
projection_coverage: recipe-javascriptallonge-recipe-lists-with-functions-as-data@36acc89c8dd6b22d1b851f4d5761dbcc
---

# lists with functions as data

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-making-data-out-of-functions-lists-with-functions-as-data-e74e34a2]].
- Evidence roles: decision, procedure, constraint, example.

## Applicability And Rationale

- Here's another look at linked lists using POJOs. _(javascriptallonge.pdf (source-range-c98ab3e6-01351))_
- Presto, we can use pure functions to represent a linked list . _(javascriptallonge.pdf (source-range-c98ab3e6-01359))_
- And with care, we can do amazing things like use functions to represent numbers, build more complex data structures like trees, and in fact, anything that can be computed can be computed using just functions and nothing else. _(javascriptallonge.pdf (source-range-c98ab3e6-01359))_
- We used functions to replace arrays and POJOs, but we still use JavaScript's built-in operators to test for equality ( === ) and to branch ?: . _(javascriptallonge.pdf (source-range-c98ab3e6-01361))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01352)_

```
const first = ({first, rest}) => first,
rest
= ({first, rest}) => rest,
pair = (first, rest) => ({first, rest}),
EMPTY = ({});
const l123 = pair(1, pair(2, pair(3, EMPTY)));
first(l123)
//=> 1
first(rest(l123))
//=> 2
first(rest(rest(l123)))
//=3
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01355)_

```
rest
= K(I),
pair = V,
EMPTY = (() => {});
const l123 = pair(1)(pair(
l123(first)
//=> 1
l123(rest)(first)
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01358)_

```
const length = (aPair) =>
aPair === EMPTY
? 0
: 1 + length(aPair(rest));
length(l123)
//=> 3
And mapWith?
const reverse = (aPair, delayed = EMPTY) =>
aPair === EMPTY
? delayed
: reverse(aPair(rest), pair(aPair(first))(delayed));
const mapWith = (fn, aPair, delayed = EMPTY) =>
aPair === EMPTY
? reverse(delayed)
: mapWith(fn, aPair(rest), pair(fn(aPair(first)))(delayed));
const doubled = mapWith((x) => x * 2, l123)
doubled(first)
//=> 2
doubled(rest)(first)
//=> 4
doubled(rest)(rest)(first)
//=> 6
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-making-data-out-of-functions-lists-with-functions-as-data-e74e34a2]]
