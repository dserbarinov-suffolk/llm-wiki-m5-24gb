---
page_id: javascriptallonge-backwardnes
page_kind: concept
summary: topic-concept: 9 supported fragment(s) and 2 related link(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: page-projection-pgp_e6841941e35799a8@2520d1c3d5e0e5a53bb128a2f059bc75
---

# backwardness

Source: [[javascriptallonge]]

## Statements

- Our first and second functions are a little different than what most people are used to when we talk about functions that access data. (javascriptallonge.pdf p.180)
- In both cases, the functions first and second know how the data is represented, whether it be an array or an object. (javascriptallonge.pdf p.181)
- So if we wanted to use them with a two-element array, we'd need to have a piece of code that calls some code. (javascriptallonge.pdf p.181)
- Our latin data structure is no longer a dumb data structure, it's a function. (javascriptallonge.pdf p.182)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

```
const first = ([first, second]) => first,
second = ([first, second]) => second;
const latin = ["primus", "secundus"];
first(latin)
//=> "primus"
second(latin)
//=> "secundus"
```

<a id="atom-2"></a>
**Atom:** code block

```
const first = ({first, second}) => first,
second = ({first, second}) => second;
const latin = {first: "primus", second: "secundus"};
first(latin)
//=> "primus"
second(latin)
//=> "secundus"
```

<a id="atom-3"></a>
**Atom:** code block

```
const first = K,
second = K(I);
const latin = (selector) => selector("primus")("secundus");
latin(first)
//=> "primus"
latin(second)
//=> "secundus"
```


## Related pages

- [[javascriptallonge-kestrel-and-the-idiot]] - contextualizes: source-supported topic dependency
- [[javascriptallonge-vireo]] - contextualizes: source-supported topic dependency
