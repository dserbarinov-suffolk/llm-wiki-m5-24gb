---
page_id: javascriptallonge-tap
page_kind: concept
summary: Tap: 4 accepted assertion(s) and 3 technical atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-state-tps_e77d8f478ee0a1a9@60de64cd9a2ef6e63eff61818d2c2878
---

# Tap

Source: [[javascriptallonge]]

## Statements

- One is when you want to do something with a value for sideeffects, but keep the value around. (javascriptallonge.pdf p.84)
- It has some surprising applications. (javascriptallonge.pdf p.84)
- tap is a traditional name borrowed from various Unix shell commands. (javascriptallonge.pdf p.84)
- tap can do more than just act as a debugging aid. (javascriptallonge.pdf p.85)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

```
const K = (x) => (y) => x;
```

<a id="atom-2"></a>
**Atom:** code block

```
const tap = (value) =>
(fn) => (
typeof(fn) === 'function' && fn(value),
value
)
```

<a id="atom-3"></a>
**Atom:** code block

```
const tap = (value, fn) => {
const curried = (fn) => (
typeof(fn) === 'function' && fn(value),
value
);
return fn === undefined
? curried
: curried(fn);
}
Now we can write:
tap('espresso')((it) => {
console.log(`Our drink is '${it}'`)
});
//=> Our drink is 'espresso'
'espresso'
Or:
tap('espresso', (it) => {
console.log(`Our drink is '${it}'`)
});
//=> Our drink is 'espresso'
'espresso'
```
