---
page_id: javascriptallonge-section-served-by-the-pot-collections-generating-iterables-state-machines-we-ll-keep-it-simple-5198863e
page_kind: source
summary: Served by the Pot: Collections / Generating Iterables / state machines / We'll keep it simple:: 7 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-served-by-the-pot-collections-generating-iterables-state-machines-we-ll-keep-it-simple-5198863e@00a955f818db8407366c134c95a7f5a0
---

# Served by the Pot: Collections / Generating Iterables / state machines / We'll keep it simple:

From [[javascriptallonge]].

## Related pages

### Source structure

- [[javascriptallonge-section-served-by-the-pot-collections-generating-iterables-state-machines-34feb3a9]] - broader source section: Served by the Pot: Collections / Generating Iterables / state machines

## Statements

- Again, this is not particularly horrendous, but like the recursive example, we're explicitly greenspunning the natural linear state. In a generator, we write 'do this, then this, then this.' In an iterator, we have to wrap that up and explicitly keep track of what step we're on. _(javascriptallonge.pdf (source-range-c98ab3e6-01654))_
- So we see the same thing: The generation version has state, but it's implicit in JavaScript's linear control flow. Whereas the iteration version must make that state explicit. _(javascriptallonge.pdf (source-range-c98ab3e6-01655))_
- In a generator, we write 'do this, then this, then this.' In an iterator, we have to wrap that up and explicitly keep track of what step we're on. _(javascriptallonge.pdf (source-range-c98ab3e6-01654))_

## Technical atoms

### Technical frame 1: Served by the Pot: Collections / Generating Iterables / state machines / We'll keep it simple:

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01654))_

> Again, this is not particularly horrendous, but like the recursive example, we're explicitly greenspunning the natural linear state. In a generator, we write 'do this, then this, then this.' In an iterator, we have to wrap that up and explicitly keep track of what step we're on.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01651))_

<a id="atom-technical-atom-9528af35978571ed"></a>
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

### Technical frame 2: Served by the Pot: Collections / Generating Iterables / state machines / We'll keep it simple:

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01654))_

> Again, this is not particularly horrendous, but like the recursive example, we're explicitly greenspunning the natural linear state. In a generator, we write 'do this, then this, then this.' In an iterator, we have to wrap that up and explicitly keep track of what step we're on.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01653))_

<a id="atom-technical-atom-9cc1e4cdab7f1f0b"></a>
```
21
34
55
89
144
...
```

### Technical frame 3: Served by the Pot: Collections / Generating Iterables / state machines / We'll keep it simple:

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01654))_

> Again, this is not particularly horrendous, but like the recursive example, we're explicitly greenspunning the natural linear state. In a generator, we write 'do this, then this, then this.' In an iterator, we have to wrap that up and explicitly keep track of what step we're on.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01655))_

<a id="atom-technical-atom-beea4202e91be91d"></a>
> Whereas the iteration version must make that state explicit.
