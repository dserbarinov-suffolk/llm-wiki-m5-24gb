---
page_id: javascriptallonge-we-ll-keep-it-simple
page_kind: concept
summary: topic-concept: 7 supported fragment(s) and 0 related link(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: page-projection-pgp_8db888df42f85277@ccc1bf2e19305f7ef5edac1402af937a
---

# We'll keep it simple:

Source: [[javascriptallonge]]

## Statements

- Again, this is not particularly horrendous, but like the recursive example, we're explicitly greenspunning the natural linear state. (javascriptallonge.pdf p.230)
- In a generator, we write ' do this, then this, then this.' In an iterator, we have to wrap that up and explicitly keep track of what step we're on. (javascriptallonge.pdf p.230)
- So we see the same thing: The generation version has state, but it's implicit in JavaScript's linear control flow. (javascriptallonge.pdf p.230)

## Rules

- In a generator, we write ' do this, then this, then this.' In an iterator, we have to wrap that up and explicitly keep track of what step we're on. (javascriptallonge.pdf p.230)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

```
// Iteration
let a, b, state = 0;
const fibonacci = () => {
switch (state) {
case 0:
state = 1;
return a = 0;
case 1:
state = 2;
return b = 1;
case 2:
[a, b] = [b, a + b];
return b
}
};
while (true) {
console.log(fibonacci());
}
//=>
0
1
1
2
3
5
8
13
```

<a id="atom-2"></a>
**Atom:** code block

```
21
34
55
89
144
...
```

<a id="atom-3"></a>
**Atom:** rule

```
Whereas the iteration version must make that state explicit.
```
