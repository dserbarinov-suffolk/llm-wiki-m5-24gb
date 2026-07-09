---
page_id: javascriptallonge-lazy-collection-operations
page_kind: concept
summary: lazy collection operations: 10 accepted assertion(s) and 8 technical atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-state-tps_3b8a1c45bf9ab609@da76875e7e3d20c6bdaf6e3d81bc4bb8
---

# lazy collection operations

Source: [[javascriptallonge]]

## Statements

- But it can be an excellent strategy for efficiency in algorithms. (javascriptallonge.pdf p.253)
- And the array is faster in practice, because it is a built-in data type that performs its work in the engine, while the linked list does its work in JavaScript. (javascriptallonge.pdf p.253)
- Thus, calling .map.filter.reduce produces two temporary arrays that are discarded when .reduce performs its final computation. (javascriptallonge.pdf p.253)
- They produce small iterable objects that refer back to the original iteration. (javascriptallonge.pdf p.253)
- This expression begins with a stack containing 30 elements. (javascriptallonge.pdf p.254)
- Same with .filter , we get an iterable that can iterate over the even squares, but not an actual stack or array. (javascriptallonge.pdf p.254)
- It maps to the squares of all 30 numbers, but our code for mapping an iteration returns an iterable that can iterate over the squares of our numbers, not an array or stack of the squares. (javascriptallonge.pdf p.254)
- Finally, we take the first element of that filtered , squared iterable and now JavaScript actually iterates over the stack's elements, and it only needs to square two of those elements, 29 and 28 , to return the answer. (javascriptallonge.pdf p.254)
- This is why 'pure' functional languages like Haskell combine lazy semantics with immutable collections, and why even 'impure' languages like Clojure emphasize the use of immutable collections. (javascriptallonge.pdf p.256)
- If we mutate a collection after taking an iterable, we might get an unexpected result. (javascriptallonge.pdf p.256)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

```
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
.map((x) => x * x)
.filter((x) => x % 2 == 0)
.reduce((seed, element) => seed + element, 0)
Pair.from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
.map((x) => x * x)
.filter((x) => x % 2 == 0)
.reduce((seed, element) => seed + element, 0)
```

<a id="atom-2"></a>
**Atom:** rule

```
When working with very large collections and many operations, this can be important.
```

<a id="atom-3"></a>
**Atom:** rule

```
The effect is even more pronounced when we use methods like first , until , or take :
```

<a id="atom-4"></a>
**Atom:** code block

```
Stack.from([ 0,
1,
2,
3,
4,
5,
6,
7,
8,
9,
10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
20, 21, 22, 23, 24, 25, 26, 27, 28, 29])
.map((x) => x * x)
.filter((x) => x % 2 == 0)
.first()
```

<a id="atom-5"></a>
**Atom:** code block

```
Stack.from([ 0,
1,
2,
3,
4,
5,
6,
7,
8,
9,
10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
20, 21, 22, 23, 24, 25, 26, 27, 28, 29])
.map((x) => {
console.log(`squaring ${x}`);
return x * x
})
.filter((x) => {
console.log(`filtering ${x}`);
return x % 2 == 0
})
.first()
//=>
squaring 29
filtering 841
squaring 28
filtering 784
784
```

<a id="atom-6"></a>
**Atom:** rule

```
If we write the almost identical thing with an array, we get a different behaviour:
```

<a id="atom-7"></a>
**Atom:** code block

```
[ 0,
1,
2,
3,
4,
5,
6,
7,
8,
9,
10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
.reverse()
.map((x) => {
console.log(`squaring ${x}`);
return x * x
})
.filter((x) => {
console.log(`filtering ${x}`);
return x % 2 == 0
})[0]
//=>
squaring 0
squaring 1
squaring 2
squaring 3
...
squaring 28
squaring 29
filtering 0
filtering 1
filtering 4
...
filtering 784
filtering 841
784
```

<a id="atom-8"></a>
**Atom:** code block

```
const Numbers = Object.assign({
[Symbol.iterator]: () => {
let n = 0;
return {
next: () =>
({done: false, value: n++})
}
}
}, LazyCollection);
const firstCubeOver1234 =
Numbers
.map((x) => x * x * x)
.filter((x) => x > 1234)
.first()
//=> 1331
```
