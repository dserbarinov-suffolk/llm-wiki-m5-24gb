---
page_id: javascriptallonge-section-rebinding-a5966b8c
page_kind: source
summary: rebinding: 5 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-rebinding-a5966b8c@e7edc9aeec1f48964f9e9851b07c3957
---

# rebinding

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-are-consts-also-from-a-shadowy-planet-7101c1ad]] - previous source section: are consts also from a shadowy planet?
- [[javascriptallonge-section-naming-functions-2b780968]] - next source section: Naming Functions

## Statements

- JavaScript does not permit us to rebind a name that has been bound with const . We can shadow it by using const to declare a new binding with a new function or block scope, but we cannot rebind a name that was bound with const in an existing scope. _(javascriptallonge.pdf (source-range-c98ab3e6-00481))_
- This is valuable, as it greatly simplifies the analysis of programs to see at a glance that when something is bound with const , we need never worry that its value may change. _(javascriptallonge.pdf (source-range-c98ab3e6-00482))_

## Technical atoms

### Technical frame 1: rebinding

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00481))_

> JavaScript does not permit us to rebind a name that has been bound with const . We can shadow it by using const to declare a new binding with a new function or block scope, but we cannot rebind a name that was bound with const in an existing scope.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00480))_

<a id="atom-technical-atom-f19e49dc8394a693"></a>
```
evenStevens = (n) => {
if (n === 0) {
return true;
}
else if (n == 1) {
return false;
}
else {
return evenStevens(n - 2);
}
}
//=> ERROR, evenStevens is read-only
```
