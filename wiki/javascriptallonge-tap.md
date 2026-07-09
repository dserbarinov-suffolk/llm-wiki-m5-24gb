---
page_id: javascriptallonge-tap
page_kind: concept
summary: topic-concept: 10 supported fragment(s) and 2 related link(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: page-projection-pgp_2c6bfc4e1298699b@b426d42614d06111f3c1d1a314c148b4
---

# Tap

Source: [[javascriptallonge]]

## Statements

- One is when you want to do something with a value for sideeffects, but keep the value around. (javascriptallonge.pdf p.84)
- It has some surprising applications. (javascriptallonge.pdf p.84)
- tap is a traditional name borrowed from various Unix shell commands. (javascriptallonge.pdf p.84)
- tap can do more than just act as a debugging aid. (javascriptallonge.pdf p.85)

## Rules

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


## Related pages

- [[javascriptallonge-unary]] - contextualizes: source-supported topic dependency
- [[javascriptallonge-maybe]] - contextualizes: source-supported topic dependency
