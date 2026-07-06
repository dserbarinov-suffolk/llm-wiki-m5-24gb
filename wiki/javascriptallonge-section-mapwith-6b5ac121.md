---
page_id: javascriptallonge-section-mapwith-6b5ac121
page_kind: source
summary: mapWith: 17 source-backed entries and 4 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-mapwith-6b5ac121@613c50ca77195d25bd7f6e5d72ba37ef
---

# mapWith

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-disclaimer-533cf9a5]] - previous source section: Disclaimer
- [[javascriptallonge-section-flip-869ff826]] - next source section: Flip

## Statements

- That means that you can pass a function to mapWith and get back a function that applies that mapping to any array. For example, we might need a function to return the squares of an array. Instead of writing a a wrapper around .map : _(javascriptallonge.pdf (source-range-c98ab3e6-01410))_
- 82 Yes, we also used the name mapWith for working with ordinary collections elsewhere. If we were writing a library of functions, we would have to disambiguate the two kinds of mapping functions with special names, namespaces, or modules. But for the purposes of discussing ideas, we can use the same name twice in two different contexts. It's the same idea, after all. _(javascriptallonge.pdf (source-range-c98ab3e6-01413))_
- If we didn't use mapWith , we'd could have also used callRight with map to accomplish the same result: _(javascriptallonge.pdf (source-range-c98ab3e6-01415))_
- Both patterns take us to the same destination: Composing functions out of common pieces, rather than building them entirely from scratch. mapWith is a very convenient abstraction for a very common pattern. _(javascriptallonge.pdf (source-range-c98ab3e6-01417))_
- For example, we might need a function to return the squares of an array. _(javascriptallonge.pdf (source-range-c98ab3e6-01410))_
- That means that you can pass a function to mapWith and get back a function that applies that mapping to any array. _(javascriptallonge.pdf (source-range-c98ab3e6-01410))_
- It's the same idea, after all. _(javascriptallonge.pdf (source-range-c98ab3e6-01413))_

## Technical atoms

### Technical frame 1: mapWith

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01410))_

> That means that you can pass a function to mapWith and get back a function that applies that mapping to any array. For example, we might need a function to return the squares of an array. Instead of writing a a wrapper around .map :

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01408))_

<a id="atom-technical-atom-de80fe53ccb92d9a"></a>
```
const mapWith = (fn) => (list) => list.map(fn);
```

### Technical frame 2: mapWith

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01413))_

> 82 Yes, we also used the name mapWith for working with ordinary collections elsewhere. If we were writing a library of functions, we would have to disambiguate the two kinds of mapping functions with special names, namespaces, or modules. But for the purposes of discussing ideas, we can use the same name twice in two different contexts. It's the same idea, after all.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01411))_

<a id="atom-technical-atom-6fa43cc7fa012a5e"></a>
```
const squaresOf = (list) =>
list.map(x => x * x);
squaresOf([1, 2, 3, 4, 5])
//=> [1, 4, 9, 16, 25]
```

### Technical frame 3: mapWith

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01415))_

> If we didn't use mapWith , we'd could have also used callRight with map to accomplish the same result:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01414))_

<a id="atom-technical-atom-ad79e58ca2eb2d70"></a>
```
const squaresOf = mapWith(n => n * n);
squaresOf([1, 2, 3, 4, 5])
//=> [1, 4, 9, 16, 25]
```

### Technical frame 4: mapWith

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01417))_

> Both patterns take us to the same destination: Composing functions out of common pieces, rather than building them entirely from scratch. mapWith is a very convenient abstraction for a very common pattern.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01416))_

<a id="atom-technical-atom-17a145781107cfb2"></a>
```
const squaresOf = callRight(map, (n => n * n);
squaresOf([1, 2, 3, 4, 5])
//=> [1, 4, 9, 16, 25]
```
