---
page_id: javascriptallonge-section-reassignment-c80c0ca4
page_kind: source
summary: Reassignment: 18 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-reassignment-c80c0ca4@5b231b6454f0b1c6b9aa392905cfcd12
---

# Reassignment

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-building-with-mutation-616d4b06]] - previous source section: building with mutation
- [[javascriptallonge-section-mixing-let-and-const-485aff44]] - next source section: mixing let and const

## Statements

- Like some imperative programming languages, JavaScript allows you to re-assign the value bound to parameters. We saw this earlier in rebinding: _(javascriptallonge.pdf (source-range-c98ab3e6-01138))_
- JavaScript does not permit us to rebind a name that has been bound with const . We can shadow it by using const to declare a new binding with a new function or block scope, but we cannot rebind a name that was bound with const in an existing scope. _(javascriptallonge.pdf (source-range-c98ab3e6-01143))_
- Rebinding parameters is usually avoided, but what about rebinding names we declare within a function? What we want is a statement that works like const , but permits us to rebind variables. JavaScript has such a thing, it's called let : _(javascriptallonge.pdf (source-range-c98ab3e6-01144))_
- We took the time to carefully examine what happens with bindings in environments. Let's take the time to explore what happens with reassigning values to variables. The key is to understand that we are rebinding a different value to the same name in the same environment. _(javascriptallonge.pdf (source-range-c98ab3e6-01146))_
- Using let to bind 50 to age within the block does not change the binding of age in the outer environment because the binding of age in the block shadows the binding of age in the outer environment, just like const . We go from: _(javascriptallonge.pdf (source-range-c98ab3e6-01149))_
- Like evaluating variable labels, when a binding is rebound, JavaScript searches for the binding in the current environment and then each ancestor in turn until it finds one. It then rebinds the name in that environment. _(javascriptallonge.pdf (source-range-c98ab3e6-01154))_
- Using let to bind 50 to age within the block does not change the binding of age in the outer environment because the binding of age in the block shadows the binding of age in the outer environment, just like const . _(javascriptallonge.pdf (source-range-c98ab3e6-01149))_
- However, if we don't shadow age with let , reassigning within the block changes the original: _(javascriptallonge.pdf (source-range-c98ab3e6-01152))_
- Like evaluating variable labels, when a binding is rebound, JavaScript searches for the binding in the current environment and then each ancestor in turn until it finds one. _(javascriptallonge.pdf (source-range-c98ab3e6-01154))_
- It then rebinds the name in that environment. _(javascriptallonge.pdf (source-range-c98ab3e6-01154))_

## Technical atoms

### Technical frame 1: Reassignment

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01143))_

> JavaScript does not permit us to rebind a name that has been bound with const . We can shadow it by using const to declare a new binding with a new function or block scope, but we cannot rebind a name that was bound with const in an existing scope.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01142))_

<a id="atom-technical-atom-caad6a23a95ebb37"></a>
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
