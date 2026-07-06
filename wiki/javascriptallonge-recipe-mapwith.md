---
page_id: javascriptallonge-recipe-mapwith
page_kind: recipe
summary: mapWith: reusable source-backed pattern with 8 statement(s) and 7 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: mapwith
projection_coverage: recipe-javascriptallonge-recipe-mapwith@d76aeee51189db65964d7cca27f70169
---

# mapWith

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-recipes-with-data-mapwith-ed96bde6]].
- Evidence roles: decision, constraint, definition, explanation, procedure, example.

## Applicability And Rationale

- That means that you can pass a function to mapWith and get back a function that applies that mapping to any array. _(javascriptallonge.pdf (source-range-c98ab3e6-01432))_
- For example, we might need a function to return the squares of an array. _(javascriptallonge.pdf (source-range-c98ab3e6-01432))_
- If we were writing a library of functions, we would have to disambiguate the two kinds of mapping functions with special names, namespaces, or modules. _(javascriptallonge.pdf (source-range-c98ab3e6-01435))_
- But for the purposes of discussing ideas, we can use the same name twice in two different contexts. _(javascriptallonge.pdf (source-range-c98ab3e6-01435))_
- 82 Yes, we also used the name mapWith for working with ordinary collections elsewhere. _(javascriptallonge.pdf (source-range-c98ab3e6-01435))_
- It's the same idea, after all. _(javascriptallonge.pdf (source-range-c98ab3e6-01435))_

## Technical Atoms

### Atom 1: `worked-example`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01425)_

```
In JavaScript, arrays have a .map method. Map takes a function as an argument, and applies it to each of the elements of the array, then returns the results in another array. For example:
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01426)_

```
[1, 2, 3, 4, 5].map(x => x * x)
//=> [1, 4, 9, 16, 25]
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01428)_

```
const map = (list, fn) =>
list.map(fn);
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01430)_

```
const mapWith = (fn) => (list) => list.map(fn);
```

### Atom 5: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01433)_

```
const squaresOf = (list) =>
list.map(x => x * x);
squaresOf([1, 2, 3, 4, 5])
//=> [1, 4, 9, 16, 25]
```

### Atom 6: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01436)_

```
const squaresOf = mapWith(n => n * n);
squaresOf([1, 2, 3, 4, 5])
//=> [1, 4, 9, 16, 25]
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-recipes-with-data-mapwith-ed96bde6]]
