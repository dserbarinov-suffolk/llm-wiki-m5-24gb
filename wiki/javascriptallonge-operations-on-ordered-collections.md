---
page_id: javascriptallonge-operations-on-ordered-collections
page_kind: concept
summary: operations on ordered collections: 17 accepted assertion(s) and 9 technical atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-state-tps_bf4e3b69aaec0a56@ca81b7d1e3606b0d4f2635a07ad52ad9
---

# operations on ordered collections

Source: [[javascriptallonge]]

## Statements

- Here's mapWith , it takes an ordered collection, and returns another ordered collection representing a mapping over the original: 89. (javascriptallonge.pdf p.217)
- 89 Yes, we also used the name mapWith for working with ordinary collections elsewhere. (javascriptallonge.pdf p.217)
- But for the purposes of discussing ideas, we can use the same name twice in two different contexts. (javascriptallonge.pdf p.217)
- If we were writing a library of functions, we would have to disambiguate the two kinds of mapping functions with special names, namespaces, or modules. (javascriptallonge.pdf p.217)
- An iterator is also an object, but with a .next() method that is invoked repeatedly to obtain the elements in order. (javascriptallonge.pdf p.218)
- This illustrates the general pattern of working with ordered collections: We make them iterables , meaning that they have a [Symbol.iterator] method, that returns an iterator . (javascriptallonge.pdf p.218)
- Many operations on ordered collections return another ordered collection. (javascriptallonge.pdf p.218)
- Numbers is an ordered collection. (javascriptallonge.pdf p.219)
- That in turns means it executes const iterator = Numbers[Symbol.iterator](); every time we write for (const i of Evens) , and that means that iterator starts at the beginning of Numbers . (javascriptallonge.pdf p.219)
- Thus, mapWith has the property of preserving the collection semantics of the iterable we give it. (javascriptallonge.pdf p.219)
- So, Evens is also an ordered collection, because it starts at the beginning each time we get a fresh iterator over it. (javascriptallonge.pdf p.219)
- Like mapWith , they preserve the ordered collection semantics of whatever you give them. (javascriptallonge.pdf p.221)
- Andhere's a computation performed using operations on ordered collections: We'll create an ordered collection of square numbers that end in one and are less than 1,000:. (javascriptallonge.pdf p.221)
- As we expect from an ordered collection, each time we iterate over UpTo1000 , we begin at the beginning. (javascriptallonge.pdf p.221)
- first returns the first element of an iterable (if it has one), and rest returns an iterable that iterates over all but the first element of an iterable. (javascriptallonge.pdf p.221)
- For completeness, here are two more handy iterable functions. (javascriptallonge.pdf p.221)
- like our other operations, rest preserves the ordered collection semantics of its argument. (javascriptallonge.pdf p.221)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

```
const mapWith = (fn, collection) =>
({
[Symbol.iterator] () {
const iterator = collection[Symbol.iterator]();
return {
next () {
const {done, value} = iterator.next();
return ({done, value: done ? undefined : fn(value)});
}
}
}
});
```

<a id="atom-2"></a>
**Atom:** code block

```
const Evens = mapWith((x) => 2 * x, Numbers);
for (const i of Evens) {
console.log(i)
}
//=>
0
2
4
...
for (const i of Evens) {
console.log(i)
}
//=>
0
2
4
...
```

<a id="atom-3"></a>
**Atom:** code block

```
const Evens =
{
[Symbol.iterator] () {
const iterator = Numbers[Symbol.iterator]();
return {
next () {
const {done, value} = iterator.next();
return ({done, value: done ? undefined : 2 *value});
}
}
}
};
```

<a id="atom-4"></a>
**Atom:** code block

```
const ZeroesToNines = mapWith((n) => Math.floor(10 * limit), RandomNumbers);
for (const i of ZeroesToNines) {
console.log(i)
}
//=>
5
1
9
...
for (const i of ZeroesToNines) {
console.log(i)
}
//=>
3
```

<a id="atom-5"></a>
**Atom:** code block

```
6
1
...
```

<a id="atom-6"></a>
**Atom:** rule

```
mapWith can get a new iterator from RandomNumbers each time we iterate over ZeroesToNines , but if RandomNumbers doesn't behave like an ordered collection, that's not mapWith 's fault.
```

<a id="atom-7"></a>
**Atom:** code block

```
const filterWith = (fn, iterable) =>
({
[Symbol.iterator] () {
const iterator = iterable[Symbol.iterator]();
return {
next () {
do {
const {done, value} = iterator.next();
} while (!done && !fn(value));
return {done, value};
}
}
}
});
const untilWith = (fn, iterable) =>
({
[Symbol.iterator] () {
const iterator = iterable[Symbol.iterator]();
return {
next () {
let {done, value} = iterator.next();
done = done || fn(value);
return ({done, value: done ? undefined : value});
}
}
}
});
```

<a id="atom-8"></a>
**Atom:** code block

```
const Squares = mapWith((x) => x * x, Numbers);
const EndWithOne = filterWith((x) => x % 10 === 1, Squares);
const UpTo1000 = untilWith((x) => (x > 1000), EndWithOne);
[...UpTo1000]
//=>
[1,81,121,361,441,841,961]
[...UpTo1000]
//=>
[1,81,121,361,441,841,961]
```

<a id="atom-9"></a>
**Atom:** code block

```
const first = (iterable) =>
iterable[Symbol.iterator]().next().value;
const rest = (iterable) =>
({
[Symbol.iterator] () {
const iterator = iterable[Symbol.iterator]();
iterator.next();
return iterator;
}
});
```
