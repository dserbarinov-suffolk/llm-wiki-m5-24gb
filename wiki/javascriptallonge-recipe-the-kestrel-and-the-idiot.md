---
page_id: javascriptallonge-recipe-the-kestrel-and-the-idiot
page_kind: recipe
summary: the kestrel and the idiot: reusable source-backed pattern with 7 statement(s) and 6 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-01
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: the-kestrel-and-the-idiot
projection_coverage: recipe-javascriptallonge-recipe-the-kestrel-and-the-idiot@18d311882fdffb6569874fe1f3380207
---

# the kestrel and the idiot

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-copy-on-write-making-data-out-of-functions-the-kestrel-and-the-idiot-301fbaf6]].
- Evidence roles: decision, explanation, constraint, example.

## Applicability And Rationale

- You give it a value, and it returns a constant function that gives that value. _(javascriptallonge.pdf (source-range-0e12e052-01333))_
- For example, (x) => 42 is a constant function that always evaluates to 42. _(javascriptallonge.pdf (source-range-0e12e052-01333))_
- The kestrel, or K , is a function that makes constant functions. _(javascriptallonge.pdf (source-range-0e12e052-01333))_
- A constant function is a function that always returns the same thing, no matter what you give it. _(javascriptallonge.pdf (source-range-0e12e052-01333))_
- The identity function is a function that evaluates to whatever parameter you pass it. _(javascriptallonge.pdf (source-range-0e12e052-01336))_
- Given two values, we can say that K always returns the first value: K(x)(y) => x (that's not valid JavaScript, but it's essentially how it works). _(javascriptallonge.pdf (source-range-0e12e052-01339))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-01335)_

```
const K = (x) => (y) => x;
const fortyTwo = K(42);
fortyTwo(6)
//=> 42
fortyTwo("Hello")
//=> 42
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-01338)_

```
K(6)(7)
//=> 6
K(12)(24)
//=> 12
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-01341)_

```
Therefore, K(I)(x)(y) => y:
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-01342)_

```
K(I)(6)(7)
//=> 7
K(I)(12)(24)
//=> 24
```

### Atom 5: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-01344)_

```
K("primus")("secundus")
//=> "primus"
K(I)("primus")("secundus")
//=> "secundus"
```

### Atom 6: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-01346)_

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
- Source section: [[javascriptallonge-section-copy-on-write-making-data-out-of-functions-the-kestrel-and-the-idiot-301fbaf6]]
