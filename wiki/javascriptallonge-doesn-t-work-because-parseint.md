---
page_id: javascriptallonge-doesn-t-work-because-parseint
page_kind: concept
summary: Doesn'T Work Because Parseint: 1 statement(s) and 4 atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-doesn-t-work-because-parseint@929b8c03e28e3a5be04c54552db9755d
---

# Doesn'T Work Because Parseint

What [[javascriptallonge]] covers about doesn't work because parseint:

## Statements

### Recipes with Basic Functions / Unary

- This doesn't work because parseInt is defined as parseInt(string[, radix]) . It takes an optional radix argument. And when you call parseInt with map , the index is interpreted as a radix. Not good! What we want is to convert parseInt into a function taking only one argument. _(javascriptallonge.pdf (source-range-c98ab3e6-00671))_


## Technical atoms

### Technical frame 1: Recipes with Basic Functions / Unary

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00671))_

> This doesn't work because parseInt is defined as parseInt(string[, radix]) . It takes an optional radix argument. And when you call parseInt with map , the index is interpreted as a radix. Not good! What we want is to convert parseInt into a function taking only one argument.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00669))_

<a id="atom-technical-atom-ac76ad6a4b453d1b"></a>
> If you pass in a function taking only one argument, it simply ignores the additional arguments.

### Technical frame 2: Recipes with Basic Functions / Unary

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00671))_

> This doesn't work because parseInt is defined as parseInt(string[, radix]) . It takes an optional radix argument. And when you call parseInt with map , the index is interpreted as a radix. Not good! What we want is to convert parseInt into a function taking only one argument.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00670))_

<a id="atom-technical-atom-882633ed7be44ad8"></a>
```
['1', '2', '3'].map(parseInt)
//=> [1, NaN, NaN]
```

### Technical frame 3: Recipes with Basic Functions / Unary

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00671))_

> This doesn't work because parseInt is defined as parseInt(string[, radix]) . It takes an optional radix argument. And when you call parseInt with map , the index is interpreted as a radix. Not good! What we want is to convert parseInt into a function taking only one argument.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00672))_

<a id="atom-technical-atom-b336a1f2d067e0fb"></a>
> Wecould write ['1', '2', '3'].map((s) => parseInt(s)) , or we could come up with a decorator to do the job for us:

### Technical frame 4: Recipes with Basic Functions / Unary

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00671))_

> This doesn't work because parseInt is defined as parseInt(string[, radix]) . It takes an optional radix argument. And when you call parseInt with map , the index is interpreted as a radix. Not good! What we want is to convert parseInt into a function taking only one argument.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00673))_

<a id="atom-technical-atom-427aee1ef7fb5c9e"></a>
```
const unary = (fn) =>
fn.length === 1
? fn
: function (something) {
return fn.call(this, something)
}
```


## Source

- [[javascriptallonge]]
