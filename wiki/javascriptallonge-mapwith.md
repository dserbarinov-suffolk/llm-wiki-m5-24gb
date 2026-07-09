---
page_id: javascriptallonge-mapwith
page_kind: concept
summary: topic-concept: 19 supported fragment(s) and 1 related link(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: page-projection-pgp_0e37c367b06f9361@9c220425bbb4fbc6065ddf6ab951396d
---

# mapWith

Source: [[javascriptallonge]]

## Statements

- For example, we might need a function to return the squares of an array. (javascriptallonge.pdf p.193)
- That means that you can pass a function to mapWith and get back a function that applies that mapping to any array. (javascriptallonge.pdf p.193)
- If we were writing a library of functions, we would have to disambiguate the two kinds of mapping functions with special names, namespaces, or modules. (javascriptallonge.pdf p.193)
- 82 Yes, we also used the name mapWith for working with ordinary collections elsewhere. (javascriptallonge.pdf p.193)
- But for the purposes of discussing ideas, we can use the same name twice in two different contexts. (javascriptallonge.pdf p.193)
- If we didn't use mapWith , we'd could have also used callRight with map to accomplish the same result:. (javascriptallonge.pdf p.194)
- mapWith is a very convenient abstraction for a very common pattern. (javascriptallonge.pdf p.194)

## Rules

- That means that you can pass a function to mapWith and get back a function that applies that mapping to any array. (javascriptallonge.pdf p.193)
- If we were writing a library of functions, we would have to disambiguate the two kinds of mapping functions with special names, namespaces, or modules. (javascriptallonge.pdf p.193)
- But for the purposes of discussing ideas, we can use the same name twice in two different contexts. (javascriptallonge.pdf p.193)
- If we didn't use mapWith , we'd could have also used callRight with map to accomplish the same result:. (javascriptallonge.pdf p.194)

## Technical atoms

<a id="atom-1"></a>
**Atom:** example

```
In JavaScript, arrays have a .map method. Map takes a function as an argument, and applies it to each of the elements of the array, then returns the results in another array. For example:
```

<a id="atom-2"></a>
**Atom:** code block

```
[1, 2, 3, 4, 5].map(x => x * x)
//=> [1, 4, 9, 16, 25]
```

<a id="atom-3"></a>
**Atom:** code block

```
const map = (list, fn) =>
list.map(fn);
```

<a id="atom-4"></a>
**Atom:** code block

```
const mapWith = (fn) => (list) => list.map(fn);
```

<a id="atom-5"></a>
**Atom:** code block

```
const squaresOf = (list) =>
list.map(x => x * x);
squaresOf([1, 2, 3, 4, 5])
//=> [1, 4, 9, 16, 25]
```

<a id="atom-6"></a>
**Atom:** code block

```
const squaresOf = mapWith(n => n * n);
squaresOf([1, 2, 3, 4, 5])
//=> [1, 4, 9, 16, 25]
```

<a id="atom-7"></a>
**Atom:** code block

```
const squaresOf = callRight(map, (n => n * n);
squaresOf([1, 2, 3, 4, 5])
//=> [1, 4, 9, 16, 25]
```


## Related pages

- [[javascriptallonge-why]] - contextualizes: source-supported topic dependency
