---
page_id: javascriptallonge-section-served-by-the-pot-collections-generating-iterables-state-machines-b395ef25
page_kind: source
summary: Served by the Pot: Collections / Generating Iterables / state machines: 15 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-served-by-the-pot-collections-generating-iterables-state-machines-b395ef25@9d561b09c152cb079a7511c684ec6aa7
---

# Served by the Pot: Collections / Generating Iterables / state machines

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-served-by-the-pot-collections-generating-iterables-recursive-iterators-6db8d95d]] - previous source section: Served by the Pot: Collections / Generating Iterables / recursive iterators
- [[javascriptallonge-section-served-by-the-pot-collections-generating-iterables-javascript-s-generators-60a99d41]] - next source section: Served by the Pot: Collections / Generating Iterables / javascript's generators

### Source structure

- [[javascriptallonge-section-served-by-the-pot-collections-generating-iterables-f68c47a5]] - broader source section: Served by the Pot: Collections / Generating Iterables

## Statements

- Some iterables can be modelled as state machines. Let's revisit the Fibonacci sequence. Again. One way to define it is: _(javascriptallonge.pdf (source-range-c98ab3e6-01616))_
- The first element of the fibonacci sequence is zero. _(javascriptallonge.pdf (source-range-c98ab3e6-01617))_
- The second element of the fibonacci sequence is one. _(javascriptallonge.pdf (source-range-c98ab3e6-01618))_
- Every subsequent element of the fibonacci sequence is the sum of the previous two elements. _(javascriptallonge.pdf (source-range-c98ab3e6-01619))_
- The thing to note here is that our fibonacci generator has three states: generating 0 , generating 1 , and generating everything after that. This isn't a good fit for an iterator, because iterators have one functional entry point and therefore, we'd have to represent our three states explicitly, perhaps using a state pattern 90 : _(javascriptallonge.pdf (source-range-c98ab3e6-01623))_
- The thing to note here is that our fibonacci generator has three states: generating 0 , generating 1 , and generating everything after that. _(javascriptallonge.pdf (source-range-c98ab3e6-01623))_
- This isn't a good fit for an iterator, because iterators have one functional entry point and therefore, we'd have to represent our three states explicitly, perhaps using a state pattern 90 : _(javascriptallonge.pdf (source-range-c98ab3e6-01623))_

## Statements by subsection

### Served by the Pot: Collections / Generating Iterables / state machines / We'll keep it simple:

- Again, this is not particularly horrendous, but like the recursive example, we're explicitly greenspunning the natural linear state. In a generator, we write 'do this, then this, then this.' In an iterator, we have to wrap that up and explicitly keep track of what step we're on. _(javascriptallonge.pdf (source-range-c98ab3e6-01628))_
- So we see the same thing: The generation version has state, but it's implicit in JavaScript's linear control flow. Whereas the iteration version must make that state explicit. _(javascriptallonge.pdf (source-range-c98ab3e6-01629))_
- In a generator, we write 'do this, then this, then this.' In an iterator, we have to wrap that up and explicitly keep track of what step we're on. _(javascriptallonge.pdf (source-range-c98ab3e6-01628))_
