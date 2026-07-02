---
page_id: javascriptallonge-section-and-also-that-constant-coffee-craving-rebinding-145a514e
page_kind: source
summary: And also: / That Constant Coffee Craving / rebinding: 5 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-and-also-that-constant-coffee-craving-rebinding-145a514e@70b8f0f7e257731cffe13d44e55bba41
---

# And also: / That Constant Coffee Craving / rebinding

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-and-also-that-constant-coffee-craving-are-consts-also-from-a-shadowy-planet-f4ab49ce]] - previous source section: And also: / That Constant Coffee Craving / are consts also from a shadowy planet?

### Source structure

- [[javascriptallonge-section-and-also-that-constant-coffee-craving-ac9d9918]] - broader source section: And also: / That Constant Coffee Craving

## Statements

- JavaScript does not permit us to rebind a name that has been bound with const . We can shadow it by using const to declare a new binding with a new function or block scope, but we cannot rebind a name that was bound with const in an existing scope. _(javascriptallonge.pdf (source-range-0e12e052-00491))_
- This is valuable, as it greatly simplifies the analysis of programs to see at a glance that when something is bound with const , we need never worry that its value may change. _(javascriptallonge.pdf (source-range-0e12e052-00492))_

## Technical atoms

### Technical frame 1: And also: / That Constant Coffee Craving / rebinding

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00491))_

> JavaScript does not permit us to rebind a name that has been bound with const . We can shadow it by using const to declare a new binding with a new function or block scope, but we cannot rebind a name that was bound with const in an existing scope.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00490))_

<a id="atom-technical-atom-7f57ec9822b0a494"></a>
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
