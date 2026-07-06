---
page_id: javascriptallonge-section-we-ll-keep-it-simple-2c3d018e
page_kind: source
summary: We'll keep it simple:: 7 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-we-ll-keep-it-simple-2c3d018e@20a192c07bb7a0449a09da2b6f79f8a8
---

# We'll keep it simple:

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-state-machines-d23ee359]] - previous source section: state machines
- [[javascriptallonge-section-javascript-s-generators-34e25b0e]] - next source section: javascript's generators

## Statements

- Again, this is not particularly horrendous, but like the recursive example, we're explicitly greenspunning the natural linear state. In a generator, we write 'do this, then this, then this.' In an iterator, we have to wrap that up and explicitly keep track of what step we're on. _(javascriptallonge.pdf (source-range-c98ab3e6-01628))_
- So we see the same thing: The generation version has state, but it's implicit in JavaScript's linear control flow. Whereas the iteration version must make that state explicit. _(javascriptallonge.pdf (source-range-c98ab3e6-01629))_
- In a generator, we write 'do this, then this, then this.' In an iterator, we have to wrap that up and explicitly keep track of what step we're on. _(javascriptallonge.pdf (source-range-c98ab3e6-01628))_

## Technical atoms

### Technical frame 1: We'll keep it simple:

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01628))_

> Again, this is not particularly horrendous, but like the recursive example, we're explicitly greenspunning the natural linear state. In a generator, we write 'do this, then this, then this.' In an iterator, we have to wrap that up and explicitly keep track of what step we're on.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01625))_

<a id="atom-technical-atom-6f171efc4ec96d18"></a>
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

### Technical frame 2: We'll keep it simple:

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01628))_

> Again, this is not particularly horrendous, but like the recursive example, we're explicitly greenspunning the natural linear state. In a generator, we write 'do this, then this, then this.' In an iterator, we have to wrap that up and explicitly keep track of what step we're on.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01627))_

<a id="atom-technical-atom-9d5416adef4386b7"></a>
```
21
34
55
89
144
...
```

### Technical frame 3: We'll keep it simple:

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01628))_

> Again, this is not particularly horrendous, but like the recursive example, we're explicitly greenspunning the natural linear state. In a generator, we write 'do this, then this, then this.' In an iterator, we have to wrap that up and explicitly keep track of what step we're on.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01629))_

<a id="atom-technical-atom-5b1c46c7a62a59ba"></a>
> Whereas the iteration version must make that state explicit.
