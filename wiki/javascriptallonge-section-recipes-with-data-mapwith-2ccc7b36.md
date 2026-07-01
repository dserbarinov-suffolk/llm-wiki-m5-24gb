---
page_id: javascriptallonge-section-recipes-with-data-mapwith-2ccc7b36
page_kind: source
summary: Recipes with Data / mapWith: 17 source-backed entries and 4 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-01
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-recipes-with-data-mapwith-2ccc7b36@fa588b9448ea982e195b67976d96882a
---

# Recipes with Data / mapWith

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-recipes-with-data-57848af5]] - broader source section: Recipes with Data
- [[javascriptallonge-section-recipes-with-data-disclaimer-3cee3bd7]] - previous source section: Recipes with Data / Disclaimer
- [[javascriptallonge-section-recipes-with-data-flip-9096a873]] - next source section: Recipes with Data / Flip

## Statements

- That means that you can pass a function to mapWith and get back a function that applies that mapping to any array. For example, we might need a function to return the squares of an array. Instead of writing a a wrapper around .map : _(javascriptallonge.pdf (source-range-0e12e052-01432))_
- 82 Yes, we also used the name mapWith for working with ordinary collections elsewhere. If we were writing a library of functions, we would have to disambiguate the two kinds of mapping functions with special names, namespaces, or modules. But for the purposes of discussing ideas, we can use the same name twice in two different contexts. It's the same idea, after all. _(javascriptallonge.pdf (source-range-0e12e052-01435))_
- If we didn't use mapWith , we'd could have also used callRight with map to accomplish the same result: _(javascriptallonge.pdf (source-range-0e12e052-01437))_
- Both patterns take us to the same destination: Composing functions out of common pieces, rather than building them entirely from scratch. mapWith is a very convenient abstraction for a very common pattern. _(javascriptallonge.pdf (source-range-0e12e052-01439))_
- For example, we might need a function to return the squares of an array. _(javascriptallonge.pdf (source-range-0e12e052-01432))_
- That means that you can pass a function to mapWith and get back a function that applies that mapping to any array. _(javascriptallonge.pdf (source-range-0e12e052-01432))_
- It's the same idea, after all. _(javascriptallonge.pdf (source-range-0e12e052-01435))_

## Technical atoms

### Technical frame 1: Recipes with Data / mapWith

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01432))_

> That means that you can pass a function to mapWith and get back a function that applies that mapping to any array. For example, we might need a function to return the squares of an array. Instead of writing a a wrapper around .map :

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01430))_

```
const mapWith = (fn) => (list) => list.map(fn);
```

### Technical frame 2: Recipes with Data / mapWith

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01435))_

> 82 Yes, we also used the name mapWith for working with ordinary collections elsewhere. If we were writing a library of functions, we would have to disambiguate the two kinds of mapping functions with special names, namespaces, or modules. But for the purposes of discussing ideas, we can use the same name twice in two different contexts. It's the same idea, after all.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01433))_

```
const squaresOf = (list) =>
list.map(x => x * x);
squaresOf([1, 2, 3, 4, 5])
//=> [1, 4, 9, 16, 25]
```

### Technical frame 3: Recipes with Data / mapWith

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01437))_

> If we didn't use mapWith , we'd could have also used callRight with map to accomplish the same result:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01436))_

```
const squaresOf = mapWith(n => n * n);
squaresOf([1, 2, 3, 4, 5])
//=> [1, 4, 9, 16, 25]
```

### Technical frame 4: Recipes with Data / mapWith

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01439))_

> Both patterns take us to the same destination: Composing functions out of common pieces, rather than building them entirely from scratch. mapWith is a very convenient abstraction for a very common pattern.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01438))_

```
const squaresOf = callRight(map, (n => n * n);
squaresOf([1, 2, 3, 4, 5])
//=> [1, 4, 9, 16, 25]
```
