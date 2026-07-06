---
page_id: javascriptallonge-section-object-assign-f644e66b
page_kind: source
summary: Object.assign: 8 source-backed entries and 4 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-object-assign-f644e66b@7fa9b3117bd77f25568b774037387e7c
---

# Object.assign

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-flipping-methods-bf22c9c8]] - previous source section: flipping methods
- [[javascriptallonge-section-why-ecb965c7]] - next source section: Why?

## Statements

- Both needs can be met with Object.assign , a standard function. You can copy an object by extending an empty object: _(javascriptallonge.pdf (source-range-c98ab3e6-01450))_

## Technical atoms

### Technical frame 1: Object.assign

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01450))_

> Both needs can be met with Object.assign , a standard function. You can copy an object by extending an empty object:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01449))_

<a id="atom-technical-atom-abf0399ad2cc968a"></a>
```
for (let fruit in shipment) {
inventory[fruit] = shipment[fruit]
}
```

### Technical frame 2: Object.assign

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01450))_

> Both needs can be met with Object.assign , a standard function. You can copy an object by extending an empty object:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01451))_

<a id="atom-technical-atom-03f1c054eafcb98d"></a>
```
Object.assign({}, {
apples: 12,
oranges: 12
})
//=> { apples: 12, oranges: 12 }
```

### Technical frame 3: Object.assign

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01450))_

> Both needs can be met with Object.assign , a standard function. You can copy an object by extending an empty object:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01456))_

<a id="atom-technical-atom-37ddecb7abb3e285"></a>
```
const Queue = function () {
this.array = [];
this.head = 0;
this.tail = -1
};
Queue.prototype.pushTail = function (value) {
// ...
};
Queue.prototype.pullHead = function () {
// ...
};
Queue.prototype.isEmpty = function () {
// ...
}
Into this:
const Queue = function () {
Object.assign(this, {
array: [],
head: 0,
tail: -1
})
};
Object.assign(Queue.prototype, {
pushTail (value) {
// ...
},
pullHead () {
// ...
},
isEmpty () {
// ...
```

### Technical frame 4: Object.assign

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01450))_

> Both needs can be met with Object.assign , a standard function. You can copy an object by extending an empty object:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01457))_

<a id="atom-technical-atom-b7370df8ad577cb4"></a>
```
Recipes with Data
}
});
```
