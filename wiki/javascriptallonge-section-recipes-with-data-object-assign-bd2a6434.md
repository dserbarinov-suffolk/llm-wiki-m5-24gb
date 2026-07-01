---
page_id: javascriptallonge-section-recipes-with-data-object-assign-bd2a6434
page_kind: source
summary: Recipes with Data / Object.assign: 8 source-backed entries and 4 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-01
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-recipes-with-data-object-assign-bd2a6434@b0cf60932753806ef894e4bf295038fd
---

# Recipes with Data / Object.assign

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-recipes-with-data-57848af5]] - broader source section: Recipes with Data
- [[javascriptallonge-section-recipes-with-data-flip-9096a873]] - previous source section: Recipes with Data / Flip
- [[javascriptallonge-section-recipes-with-data-why-3f8e67cf]] - next source section: Recipes with Data / Why?

## Statements

- Both needs can be met with Object.assign , a standard function. You can copy an object by extending an empty object: _(javascriptallonge.pdf (source-range-0e12e052-01472))_

## Technical atoms

### Technical frame 1: Recipes with Data / Object.assign

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01472))_

> Both needs can be met with Object.assign , a standard function. You can copy an object by extending an empty object:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01471))_

```
for (let fruit in shipment) {
inventory[fruit] = shipment[fruit]
}
```

### Technical frame 2: Recipes with Data / Object.assign

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01472))_

> Both needs can be met with Object.assign , a standard function. You can copy an object by extending an empty object:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01473))_

```
Object.assign({}, {
apples: 12,
oranges: 12
})
//=> { apples: 12, oranges: 12 }
```

### Technical frame 3: Recipes with Data / Object.assign

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01472))_

> Both needs can be met with Object.assign , a standard function. You can copy an object by extending an empty object:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01478))_

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

### Technical frame 4: Recipes with Data / Object.assign

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01472))_

> Both needs can be met with Object.assign , a standard function. You can copy an object by extending an empty object:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01479))_

```
Recipes with Data
}
});
```
