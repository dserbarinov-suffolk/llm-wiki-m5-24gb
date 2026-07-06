---
page_id: javascriptallonge-section-recipes-with-data-object-assign-892f42ff
page_kind: source
summary: Recipes with Data / Object.assign: 8 source-backed entries and 4 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-recipes-with-data-object-assign-892f42ff@e8e27407a7c434ed1855687f3edc4318
---

# Recipes with Data / Object.assign

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-recipes-with-data-flip-2771c636]] - previous source section: Recipes with Data / Flip
- [[javascriptallonge-section-recipes-with-data-why-8f8d45ed]] - next source section: Recipes with Data / Why?

### Source structure

- [[javascriptallonge-section-recipes-with-data-23db967a]] - broader source section: Recipes with Data

## Statements

- Both needs can be met with Object.assign , a standard function. You can copy an object by extending an empty object: _(javascriptallonge.pdf (source-range-c98ab3e6-01472))_

## Technical atoms

### Technical frame 1: Recipes with Data / Object.assign

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01472))_

> Both needs can be met with Object.assign , a standard function. You can copy an object by extending an empty object:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01471))_

<a id="atom-technical-atom-feeac7e344e4b903"></a>
```
for (let fruit in shipment) {
inventory[fruit] = shipment[fruit]
}
```

### Technical frame 2: Recipes with Data / Object.assign

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01472))_

> Both needs can be met with Object.assign , a standard function. You can copy an object by extending an empty object:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01473))_

<a id="atom-technical-atom-2ad70ef41d7fd506"></a>
```
Object.assign({}, {
apples: 12,
oranges: 12
})
//=> { apples: 12, oranges: 12 }
```

### Technical frame 3: Recipes with Data / Object.assign

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01472))_

> Both needs can be met with Object.assign , a standard function. You can copy an object by extending an empty object:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01478))_

<a id="atom-technical-atom-b61a2688fb0c4ba4"></a>
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

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01472))_

> Both needs can be met with Object.assign , a standard function. You can copy an object by extending an empty object:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01479))_

<a id="atom-technical-atom-3eca06af7a14d8ab"></a>
```
Recipes with Data
}
});
```
