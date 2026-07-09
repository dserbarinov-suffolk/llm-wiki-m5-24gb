---
page_id: javascriptallonge-recipe-the-kestrel-and-the-idiot
page_kind: recipe
summary: the kestrel and the idiot: reusable source-backed pattern with 7 statement(s) and 6 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: the-kestrel-and-the-idiot
projection_coverage: recipe-javascriptallonge-recipe-the-kestrel-and-the-idiot@7f3918cb79ef5de8440a66d8b9317e35
---

# the kestrel and the idiot

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-making-data-out-of-functions-the-kestrel-and-the-idiot-203dea45]].
- Evidence roles: decision, explanation, constraint, example.

## Applicability And Rationale

- A constant function is a function that always returns the same thing, no matter what you give it. _(javascriptallonge.pdf (source-range-c98ab3e6-01312))_
- For example, (x) => 42 is a constant function that always evaluates to 42. _(javascriptallonge.pdf (source-range-c98ab3e6-01312))_
- The kestrel, or K , is a function that makes constant functions. _(javascriptallonge.pdf (source-range-c98ab3e6-01312))_
- You give it a value, and it returns a constant function that gives that value. _(javascriptallonge.pdf (source-range-c98ab3e6-01312))_
- The identity function is a function that evaluates to whatever parameter you pass it. _(javascriptallonge.pdf (source-range-c98ab3e6-01315))_
- Given two values, we can say that K always returns the first value: K(x)(y) => x (that's not valid JavaScript, but it's essentially how it works). _(javascriptallonge.pdf (source-range-c98ab3e6-01318))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01314)_

```
const K = (x) => (y) => x;
const fortyTwo = K(42);
fortyTwo(6)
//=> 42
fortyTwo("Hello")
//=> 42
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01317)_

```
K(6)(7)
//=> 6
K(12)(24)
//=> 12
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01320)_

```
Therefore, K(I)(x)(y) => y:
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01321)_

```
K(I)(6)(7)
//=> 7
K(I)(12)(24)
//=> 24
```

### Atom 5: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01323)_

```
K("primus")("secundus")
//=> "primus"
K(I)("primus")("secundus")
//=> "secundus"
```

### Atom 6: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01325)_

```
const first = K,
second = K(I);
first("primus")("secundus")
//=> "primus"
second("primus")("secundus")
//=> "secundus"
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-making-data-out-of-functions-the-kestrel-and-the-idiot-203dea45]]
