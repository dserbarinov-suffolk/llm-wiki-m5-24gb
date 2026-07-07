---
page_id: javascriptallonge-section-recipes-with-data-object-assign-8d8e0e13
page_kind: source
summary: Recipes with Data / Object.assign: 8 source-backed entries and 4 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-recipes-with-data-object-assign-8d8e0e13@1a906d8fcaf735c24fe745a5dd7d2fdc
---

# Recipes with Data / Object.assign

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-recipes-with-data-flip-b1a8ea8d]] - previous source section: Recipes with Data / Flip

### Source structure

- [[javascriptallonge-section-recipes-with-data-4b3e2c99]] - broader source section: Recipes with Data

## Statements

- Both needs can be met with Object.assign , a standard function. You can copy an object by extending an empty object: _(javascriptallonge.pdf (source-range-c98ab3e6-01450))_

## Technical atoms

### Technical frame 1: Recipes with Data / Object.assign

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01450))_

> Both needs can be met with Object.assign , a standard function. You can copy an object by extending an empty object:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01449))_

<a id="atom-technical-atom-abf0399ad2cc968a"></a>
```
for (let fruit in shipment) {
inventory[fruit] = shipment[fruit]
}
```

### Technical frame 2: Recipes with Data / Object.assign

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

### Technical frame 3: Recipes with Data / Object.assign

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

### Technical frame 4: Recipes with Data / Object.assign

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01450))_

> Both needs can be met with Object.assign , a standard function. You can copy an object by extending an empty object:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01457))_

<a id="atom-technical-atom-b7370df8ad577cb4"></a>
```
Recipes with Data
}
});
```
