---
page_id: javascriptallonge-recipe-tail-call-optimization
page_kind: recipe
summary: tail-call optimization: reusable source-backed pattern with 11 statement(s) and 2 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: tail-call-optimization
projection_coverage: recipe-javascriptallonge-recipe-tail-call-optimization@f3898fd6cfc055908acf94a7dee1b9d3
---

# tail-call optimization

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-tail-call-optimization-d8a69702]].
- Evidence roles: decision, explanation, constraint, example.

## Applicability And Rationale

- A'tail-call' occurs when a function's last act is to invoke another function, and then return whatever the other function returns. _(javascriptallonge.pdf (source-range-c98ab3e6-00948))_
- This is a tail-call, because it invokes another function and returns its result. _(javascriptallonge.pdf (source-range-c98ab3e6-00950))_
- It isn't going to do any more work, so it can throw its existing stack frame away. _(javascriptallonge.pdf (source-range-c98ab3e6-00950))_
- There are three places it returns. _(javascriptallonge.pdf (source-range-c98ab3e6-00950))_
- This is interesting, because after sorting out what to supply as arguments ( this , args ), JavaScript can throw away everything in its current stack frame. _(javascriptallonge.pdf (source-range-c98ab3e6-00950))_
- But the third is fn.apply(this, args) . _(javascriptallonge.pdf (source-range-c98ab3e6-00950))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00949)_

```
const maybe = (fn) =>
function (...args) {
if (args.length === 0) {
return;
}
else {
for (let arg of args) {
if (arg == null) return;
}
return fn.apply(this, args);
}
}
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00953)_

```
const length = ([first, ...rest]) =>
first === undefined
? 0
: 1 + length(rest);
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-tail-call-optimization-d8a69702]]
