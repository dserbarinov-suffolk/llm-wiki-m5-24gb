---
page_id: javascriptallonge-recipe-object-assign
page_kind: recipe
summary: Object.assign: reusable source-backed pattern with 1 statement(s) and 7 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-01
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: object-assign
projection_coverage: recipe-javascriptallonge-recipe-object-assign@ae4c149bfe9dfb6c8a83e6d45825495c
---

# Object.assign

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-recipes-with-data-object-assign-bd2a6434]].
- Evidence roles: decision, constraint, example.

## Applicability And Rationale

- Both needs can be met with Object.assign , a standard function. _(javascriptallonge.pdf (source-range-0e12e052-01472))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-01469)_

```
const inventory = {
apples: 12,
oranges: 12
};
inventory.bananas = 54;
inventory.pears = 24;
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-01471)_

```
for (let fruit in shipment) {
inventory[fruit] = shipment[fruit]
}
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-01473)_

```
Object.assign({}, {
apples: 12,
oranges: 12
})
//=> { apples: 12, oranges: 12 }
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-01475)_

```
const inventory = {
apples: 12,
oranges: 12
};
const shipment = {
bananas: 54,
pears: 24
}
Object.assign(inventory, shipment)
```

### Atom 5: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-01476)_

```
//=> { apples: 12,
//
oranges: 12,
//
bananas: 54,
//
pears: 24 }
```

### Atom 6: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-01478)_

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

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-recipes-with-data-object-assign-bd2a6434]]
