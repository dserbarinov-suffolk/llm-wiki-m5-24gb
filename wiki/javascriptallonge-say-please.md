---
page_id: javascriptallonge-say-please
page_kind: concept
summary: say 'please': 5 accepted assertion(s) and 5 technical atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-state-tps_9b935c8444bd9c57@93a5a97f0fb906212cc178589a948844
---

# say 'please'

Source: [[javascriptallonge]]

## Statements

- This follows the philosophy we used with data structures: The function doing the work inspects the data structure. (javascriptallonge.pdf p.186)
- We can reverse this: Instead of asking a pair if it is empty and then deciding what to do, we can ask the pair to do it for us. (javascriptallonge.pdf p.186)
- Now we'll need to write first and rest functions for a list, and those names will collide with the first and rest we wrote for pairs. (javascriptallonge.pdf p.186)
- We can write reverse and mapWith as well. (javascriptallonge.pdf p.187)
- We have managed to provide the exact same functionality that === and ?: provided, but using functions and nothing else. (javascriptallonge.pdf p.188)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

```
const length = (aPair) =>
aPair === EMPTY
? 0
: 1 + length(aPair(rest));
```

<a id="atom-2"></a>
**Atom:** code block

```
const length = (list) => list(
() => 0,
(aPair) => 1 + length(aPair(rest)))
);
```

<a id="atom-3"></a>
**Atom:** code block

```
const pairFirst = K,
pairRest
= K(I),
pair = V;
const first = (list) => list(
() => "ERROR: Can't take first of an empty list",
(aPair) => aPair(pairFirst)
);
const rest = (list) => list(
```

<a id="atom-4"></a>
**Atom:** code block

```
() => "ERROR: Can't take first of an empty list",
(aPair) => aPair(pairRest)
);
const length = (list) => list(
() => 0,
(aPair) => 1 + length(aPair(pairRest)))
);
We’ll also write a handy list printer:
const print = (list) => list(
() => "",
(aPair) => `${aPair(pairFirst)} ${print(aPair(pairRest))}`
);
How would all this work? Let’s start with the obvious. What is an empty list?
const EMPTYLIST = (whenEmpty, unlessEmpty) => whenEmpty()
And what is a node of a list?
const node = (x) => (y) =>
(whenEmpty, unlessEmpty) => unlessEmpty(pair(x)(y));
Let’s try it:
const l123 = node(1)(node(2)(node(3)(EMPTYLIST)));
print(l123)
//=> 1 2 3
```

<a id="atom-5"></a>
**Atom:** code block

```
const reverse = (list, delayed = EMPTYLIST) => list(
() => delayed,
(aPair) => reverse(aPair(pairRest), node(aPair(pairFirst))(delayed))
);
print(reverse(l123));
//=> 3 2 1
const mapWith = (fn, list, delayed = EMPTYLIST) =>
list(
() => reverse(delayed),
(aPair) => mapWith(fn, aPair(pairRest), node(fn(aPair(pairFirst)))(delayed))
);
print(mapWith(x => x * x, reverse(l123)))
//=> 941
```
