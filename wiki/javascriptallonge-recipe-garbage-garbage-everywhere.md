---
page_id: javascriptallonge-recipe-garbage-garbage-everywhere
page_kind: recipe
summary: Garbage, Garbage Everywhere: reusable source-backed pattern with 12 statement(s) and 1 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: garbage-garbage-everywhere
projection_coverage: recipe-javascriptallonge-recipe-garbage-garbage-everywhere@cdb32fc663a74163bc7b63159f7a50f1
---

# Garbage, Garbage Everywhere

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-garbage-garbage-everywhere-8c9764a5]].
- Evidence roles: decision, procedure, explanation, constraint, example.

## Applicability And Rationale

- We have now seen how to use Tail Calls to execute mapWith in constant space: _(javascriptallonge.pdf (source-range-c98ab3e6-00997))_
- The right tool to discover why it's still slow is a memory profiler, but a simple inspection of the program will reveal the following: _(javascriptallonge.pdf (source-range-c98ab3e6-00999))_
- But when we try it on very large arrays, we discover that it is still very slow. _(javascriptallonge.pdf (source-range-c98ab3e6-00999))_
- To do that, we take the array in prepend and push fn(first) onto the end, creating a new array that will be passed to the next invocation of mapWith . _(javascriptallonge.pdf (source-range-c98ab3e6-01000))_
- The array we had in prepend is no longer used. _(javascriptallonge.pdf (source-range-c98ab3e6-01002))_
- In GC environments, it is marked as no longer being used, and eventually the garbage collector recycles the memory it is using. _(javascriptallonge.pdf (source-range-c98ab3e6-01002))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00998)_

```
const mapWith = (fn, [first, ...rest], prepend = []) =>
first === undefined
? prepend
: mapWith(fn, rest, [...prepend, fn(first)]);
mapWith((x) => x * x, [1, 2, 3, 4, 5])
//=> [1,4,9,16,25]
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-garbage-garbage-everywhere-8c9764a5]]
