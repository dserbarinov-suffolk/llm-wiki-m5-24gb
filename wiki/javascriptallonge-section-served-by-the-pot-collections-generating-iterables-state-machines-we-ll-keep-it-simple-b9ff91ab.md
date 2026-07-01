---
page_id: javascriptallonge-section-served-by-the-pot-collections-generating-iterables-state-machines-we-ll-keep-it-simple-b9ff91ab
page_kind: source
summary: Served by the Pot: Collections / Generating Iterables / state machines / We'll keep it simple:: 7 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-01
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-served-by-the-pot-collections-generating-iterables-state-machines-we-ll-keep-it-simple-b9ff91ab@fb9f7c4f58992a71975651de147b5203
---

# Served by the Pot: Collections / Generating Iterables / state machines / We'll keep it simple:

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-served-by-the-pot-collections-generating-iterables-state-machines-c4cec34a]] - broader source section: Served by the Pot: Collections / Generating Iterables / state machines

## Statements

- Again, this is not particularly horrendous, but like the recursive example, we're explicitly greenspunning the natural linear state. In a generator, we write 'do this, then this, then this.' In an iterator, we have to wrap that up and explicitly keep track of what step we're on. _(javascriptallonge.pdf (source-range-0e12e052-01654))_
- So we see the same thing: The generation version has state, but it's implicit in JavaScript's linear control flow. Whereas the iteration version must make that state explicit. _(javascriptallonge.pdf (source-range-0e12e052-01655))_
- In a generator, we write 'do this, then this, then this.' In an iterator, we have to wrap that up and explicitly keep track of what step we're on. _(javascriptallonge.pdf (source-range-0e12e052-01654))_

## Technical atoms

### Technical frame 1: Served by the Pot: Collections / Generating Iterables / state machines / We'll keep it simple:

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01654))_

> Again, this is not particularly horrendous, but like the recursive example, we're explicitly greenspunning the natural linear state. In a generator, we write 'do this, then this, then this.' In an iterator, we have to wrap that up and explicitly keep track of what step we're on.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01651))_

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

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01654))_

> Again, this is not particularly horrendous, but like the recursive example, we're explicitly greenspunning the natural linear state. In a generator, we write 'do this, then this, then this.' In an iterator, we have to wrap that up and explicitly keep track of what step we're on.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01653))_

```
21
34
55
89
144
...
```

### Technical frame 3: Served by the Pot: Collections / Generating Iterables / state machines / We'll keep it simple:

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01654))_

> Again, this is not particularly horrendous, but like the recursive example, we're explicitly greenspunning the natural linear state. In a generator, we write 'do this, then this, then this.' In an iterator, we have to wrap that up and explicitly keep track of what step we're on.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01655))_

> Whereas the iteration version must make that state explicit.
