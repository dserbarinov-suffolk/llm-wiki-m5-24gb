---
page_id: javascriptallonge-doesn-t-work-because-parseint
page_kind: concept
summary: Doesn'T Work Because Parseint: 1 statement(s) and 4 atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-doesn-t-work-because-parseint@8815663e9917baf05b794daba65abceb
---

# Doesn'T Work Because Parseint

What [[javascriptallonge]] covers about doesn't work because parseint:

## Statements

### Unary

- This doesn't work because parseInt is defined as parseInt(string[, radix]) . It takes an optional radix argument. And when you call parseInt with map , the index is interpreted as a radix. Not good! What we want is to convert parseInt into a function taking only one argument. _(javascriptallonge.pdf (source-range-c98ab3e6-00659))_


## Technical atoms

### Technical frame 1: Unary

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00659))_

> This doesn't work because parseInt is defined as parseInt(string[, radix]) . It takes an optional radix argument. And when you call parseInt with map , the index is interpreted as a radix. Not good! What we want is to convert parseInt into a function taking only one argument.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00657))_

<a id="atom-technical-atom-d5fabd01b550e940"></a>
> If you pass in a function taking only one argument, it simply ignores the additional arguments.

### Technical frame 2: Unary

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00659))_

> This doesn't work because parseInt is defined as parseInt(string[, radix]) . It takes an optional radix argument. And when you call parseInt with map , the index is interpreted as a radix. Not good! What we want is to convert parseInt into a function taking only one argument.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00658))_

<a id="atom-technical-atom-4b6036094b29bdd3"></a>
```
['1', '2', '3'].map(parseInt)
//=> [1, NaN, NaN]
```

### Technical frame 3: Unary

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00659))_

> This doesn't work because parseInt is defined as parseInt(string[, radix]) . It takes an optional radix argument. And when you call parseInt with map , the index is interpreted as a radix. Not good! What we want is to convert parseInt into a function taking only one argument.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00660))_

<a id="atom-technical-atom-04629f69a8da264e"></a>
> Wecould write ['1', '2', '3'].map((s) => parseInt(s)) , or we could come up with a decorator to do the job for us:

### Technical frame 4: Unary

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00659))_

> This doesn't work because parseInt is defined as parseInt(string[, radix]) . It takes an optional radix argument. And when you call parseInt with map , the index is interpreted as a radix. Not good! What we want is to convert parseInt into a function taking only one argument.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00661))_

<a id="atom-technical-atom-2cf055315b880cc0"></a>
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
