---
page_id: javascriptallonge-section-recipes-with-data-flip-2771c636
page_kind: source
summary: Recipes with Data / Flip: 17 source-backed entries and 5 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-recipes-with-data-flip-2771c636@00bfad2682309c31c7e49c35c5b6dc6d
---

# Recipes with Data / Flip

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-recipes-with-data-mapwith-ed96bde6]] - previous source section: Recipes with Data / mapWith
- [[javascriptallonge-section-recipes-with-data-object-assign-892f42ff]] - next source section: Recipes with Data / Object.assign

### Source structure

- [[javascriptallonge-section-recipes-with-data-23db967a]] - broader source section: Recipes with Data
- [[javascriptallonge-section-recipes-with-data-flip-flipping-methods-94c63baf]] - narrower source section: Recipes with Data / Flip / flipping methods
- [[javascriptallonge-section-recipes-with-data-flip-self-currying-flip-b193f390]] - narrower source section: Recipes with Data / Flip / self-currying flip

## Statements

- What we have now is a function that takes a function and 'flips' the order of arguments around, then curries it. So let's call it flipAndCurry : _(javascriptallonge.pdf (source-range-c98ab3e6-01457))_
- What we have now is a function that takes a function and 'flips' the order of arguments around, then curries it. _(javascriptallonge.pdf (source-range-c98ab3e6-01457))_

## Statements by subsection

### Recipes with Data / Flip / self-currying flip

- Sometimes we'll want to flip a function, but retain the flexibility to call it in its curried form (pass one parameter) or non-curried form (pass both). We could make that into flip : _(javascriptallonge.pdf (source-range-c98ab3e6-01461))_

### Recipes with Data / Flip / flipping methods

- When we learn about context and methods, we'll see that flip throws the current context away, so it can't be used to flip methods. A small alteration gets the job done: _(javascriptallonge.pdf (source-range-c98ab3e6-01465))_

## Technical atoms

### Technical frame 1: Recipes with Data / Flip

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01457))_

> What we have now is a function that takes a function and 'flips' the order of arguments around, then curries it. So let's call it flipAndCurry :

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01458))_

<a id="atom-technical-atom-5494cc74c8c832f8"></a>
```text
84 https://github.com/raganwald/allong.es
85 http://underscorejs.org
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 84 | https://github.com/raganwald/allong.es |
| 85 | http://underscorejs.org |

</details>

### Technical frame 2: Recipes with Data / Flip

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01457))_

> What we have now is a function that takes a function and 'flips' the order of arguments around, then curries it. So let's call it flipAndCurry :

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01459))_

<a id="atom-technical-atom-8f0036b4fbc3128d"></a>
```
const flipAndCurry = (fn) =>
(first) => (second) => fn(second, first);
Sometimes you want to flip, but not curry:
const flip = (fn) =>
(first, second) => fn(second, first);
This is gold. Consider how we define mapWith now:
var mapWith = flipAndCurry(map);
Much nicer!
```

### Technical frame 3: Recipes with Data / Flip / self-currying flip

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01461))_

> Sometimes we'll want to flip a function, but retain the flexibility to call it in its curried form (pass one parameter) or non-curried form (pass both). We could make that into flip :

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01462))_

<a id="atom-technical-atom-ace3747236bad463"></a>
```
const flip = (fn) =>
function (first, second) {
if (arguments.length === 2) {
return fn(second, first);
}
else {
return function (second) {
return fn(second, first);
};
};
};
```

### Technical frame 4: Recipes with Data / Flip / self-currying flip

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01461))_

> Sometimes we'll want to flip a function, but retain the flexibility to call it in its curried form (pass one parameter) or non-curried form (pass both). We could make that into flip :

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01463))_

<a id="atom-technical-atom-7a084c46ea593a92"></a>
> Nowif we write mapWith = flip(map) , we can call mapWith(fn, list) or mapWith(fn)(list) , our choice.

### Technical frame 5: Recipes with Data / Flip / flipping methods

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01465))_

> When we learn about context and methods, we'll see that flip throws the current context away, so it can't be used to flip methods. A small alteration gets the job done:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01466))_

<a id="atom-technical-atom-023c107967812805"></a>
```
const flipAndCurry = (fn) =>
(first) =>
function (second) {
return fn.call(this, second, first);
}
const flip = (fn) =>
function (first, second) {
return fn.call(this, second, first);
}
const flip = (fn) =>
function (first, second) {
if (arguments.length === 2) {
return fn.call(this, second, first);
}
else {
return function (second) {
return fn.call(this, second, first);
};
};
};
```
