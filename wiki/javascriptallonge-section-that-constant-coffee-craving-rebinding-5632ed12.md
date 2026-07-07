---
page_id: javascriptallonge-section-that-constant-coffee-craving-rebinding-5632ed12
page_kind: source
summary: That Constant Coffee Craving / rebinding: 5 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-that-constant-coffee-craving-rebinding-5632ed12@ddcc23b023b2e00741f85f3d505ab089
---

# That Constant Coffee Craving / rebinding

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-that-constant-coffee-craving-are-consts-also-from-a-shadowy-planet-12b08c07]] - previous source section: That Constant Coffee Craving / are consts also from a shadowy planet?

### Source structure

- [[javascriptallonge-section-that-constant-coffee-craving-614e2fd3]] - broader source section: That Constant Coffee Craving

## Statements

- JavaScript does not permit us to rebind a name that has been bound with const . We can shadow it by using const to declare a new binding with a new function or block scope, but we cannot rebind a name that was bound with const in an existing scope. _(javascriptallonge.pdf (source-range-c98ab3e6-00481))_
- This is valuable, as it greatly simplifies the analysis of programs to see at a glance that when something is bound with const , we need never worry that its value may change. _(javascriptallonge.pdf (source-range-c98ab3e6-00482))_

## Technical atoms

### Technical frame 1: That Constant Coffee Craving / rebinding

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
