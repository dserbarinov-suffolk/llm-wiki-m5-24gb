---
page_id: javascriptallonge-eager-collection
page_kind: concept
summary: Eager Collection: 1 statement(s) and 3 atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-01
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-eager-collection@bd0434725f86e7f42043eb06dac83340
---

# Eager Collection

What [[javascriptallonge]] covers about eager collection:

## Statements

### Lazy and Eager Collections / eager collections

- An eager collection, like an array, returns a collection of its own type from each of the methods. We can make an eager collection out of any collection that is gatherable , meaning it has a .from method: _(javascriptallonge.pdf (source-range-0e12e052-01798))_


## Technical atoms

### Technical frame 1: Lazy and Eager Collections / eager collections

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01802))_

> Here is our Pair implementation. Pair is gatherable, because it implements .from() . We mix EagerCollection(Pair) into it, and this gives it all of our collection methods, which each method returning a new list of pairs:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01799))_

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

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01802))_

> Here is our Pair implementation. Pair is gatherable, because it implements .from() . We mix EagerCollection(Pair) into it, and this gives it all of our collection methods, which each method returning a new list of pairs:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01800))_

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

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01802))_

> Here is our Pair implementation. Pair is gatherable, because it implements .from() . We mix EagerCollection(Pair) into it, and this gives it all of our collection methods, which each method returning a new list of pairs:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01801))_

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


## Related pages

- [[javascriptallonge-collection]] - broader topic: Collection shares technical record from Lazy and Eager Collections / eager collections: const extend = function (consumer, ...providers) { for (let i = 0; i < providers.length; ++i) { const provider = providers[i]; for (let key in provider) { if (provid ... [truncated] (3 shared atom(s))
- [[javascriptallonge-method]] - shared technical atoms: Method shares technical record from Lazy and Eager Collections / eager collections: const extend = function (consumer, ...providers) { for (let i = 0; i < providers.length; ++i) { const provider = providers[i]; for (let key in provider) { if (provid ... [truncated] (3 shared atom(s))
- [[javascriptallonge-section-lazy-and-eager-collections-eager-collections-4dcc549f]] - source section: Lazy and Eager Collections / eager collections shares source evidence from Lazy and Eager Collections / eager collections: An eager collection, like an array, returns a collection of its own type from each of the methods. We can make an eager collection out of any collection that is gath ... [truncated]; Lazy and Eager Collections / eager collections shares technical record from Lazy and Eager Collections / eager collections: const extend = function (consumer, ...providers) { for (let i = 0; i < providers.length; ++i) { const provider = providers[i]; for (let key in provider) { if (provid ... [truncated] (4 shared statement(s), 5 shared atom(s))

## Source

- [[javascriptallonge]]
