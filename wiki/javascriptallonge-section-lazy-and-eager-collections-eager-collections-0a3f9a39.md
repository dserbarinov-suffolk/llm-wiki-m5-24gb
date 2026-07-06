---
page_id: javascriptallonge-section-lazy-and-eager-collections-eager-collections-0a3f9a39
page_kind: source
summary: Lazy and Eager Collections / eager collections: 10 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-lazy-and-eager-collections-eager-collections-0a3f9a39@4484d4a9bbe98250c1ff0eee9791ae74
---

# Lazy and Eager Collections / eager collections

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-lazy-and-eager-collections-lazy-collection-operations-fed63222]] - previous source section: Lazy and Eager Collections / lazy collection operations

### Source structure

- [[javascriptallonge-section-lazy-and-eager-collections-8fb68091]] - broader source section: Lazy and Eager Collections

### Topics

- [[javascriptallonge-eager-collection]] - topic hub: opens the topic page for Eager Collection

## Statements

- An eager collection, like an array, returns a collection of its own type from each of the methods. We can make an eager collection out of any collection that is gatherable , meaning it has a .from method: _(javascriptallonge.pdf (source-range-c98ab3e6-01798))_
- Here is our Pair implementation. Pair is gatherable, because it implements .from() . We mix EagerCollection(Pair) into it, and this gives it all of our collection methods, which each method returning a new list of pairs: _(javascriptallonge.pdf (source-range-c98ab3e6-01802))_
- Pair is gatherable, because it implements .from() . _(javascriptallonge.pdf (source-range-c98ab3e6-01802))_

## Technical atoms

### Technical frame 1: Lazy and Eager Collections / eager collections

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01802))_

> Here is our Pair implementation. Pair is gatherable, because it implements .from() . We mix EagerCollection(Pair) into it, and this gives it all of our collection methods, which each method returning a new list of pairs:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01799))_

<a id="atom-technical-atom-e74cc9e8b77b3936"></a>
```
const extend = function (consumer, ...providers) {
for (let i = 0; i < providers.length; ++i) {
const provider = providers[i];
for (let key in provider) {
if (provider.hasOwnProperty(key)) {
consumer[key] = provider[key]
}
}
}
return consumer
};
```

### Technical frame 2: Lazy and Eager Collections / eager collections

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01802))_

> Here is our Pair implementation. Pair is gatherable, because it implements .from() . We mix EagerCollection(Pair) into it, and this gives it all of our collection methods, which each method returning a new list of pairs:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01800))_

<a id="atom-technical-atom-c9778d1dc768be4e"></a>
```
const EagerCollection = (gatherable) =>
({
map(fn) {
const
original = this;
return gatherable.from(
(function* () {
for (let element of original) {
yield fn(element);
}
})()
);
},
reduce(fn, seed) {
let accumulator = seed;
for(let element of this) {
accumulator = fn(accumulator, element);
}
return accumulator;
},
filter(fn) {
const original = this;
return gatherable.from(
(function* () {
for (let element of original) {
if (fn(element)) yield element;
}
})()
);
},
find(fn) {
for (let element of this) {
if (fn(element)) return element;
}
},
until(fn) {
```

### Technical frame 3: Lazy and Eager Collections / eager collections

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01802))_

> Here is our Pair implementation. Pair is gatherable, because it implements .from() . We mix EagerCollection(Pair) into it, and this gives it all of our collection methods, which each method returning a new list of pairs:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01801))_

<a id="atom-technical-atom-80989863d8f69b08"></a>
```
const original = this;
return gatherable.from(
(function* () {
for (let element of original) {
if (fn(element)) break;
yield element;
}
})()
);
},
first() {
return this[Symbol.iterator]().next().value;
},
rest() {
const iteration = this[Symbol.iterator]();
iteration.next();
return gatherable.from(
(function* () {
yield * iteration;
})()
);
return gatherable.from(iterable);
},
take(numberToTake) {
const original = this;
let numberRemaining = numberToTake;
return gatherable.from(
(function* () {
for (let element of original) {
if (numberRemaining-- <= 0) break;
yield element;
}
})()
);
}
});
```
