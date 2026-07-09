---
page_id: javascriptallonge-backwardnes
page_kind: concept
summary: backwardness: 4 accepted assertion(s) and 3 technical atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-state-tps_36ce370fd79798e0@193bb36bb7d9f85373a8f4cabc114b33
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
