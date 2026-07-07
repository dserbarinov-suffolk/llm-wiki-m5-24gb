---
page_id: javascriptallonge-section-served-by-the-pot-collections-generating-iterables-f68c47a5
page_kind: source
summary: Served by the Pot: Collections / Generating Iterables: 16 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-served-by-the-pot-collections-generating-iterables-f68c47a5@5f79de59e0a13b93efd457fcba5c17ff
---

# Served by the Pot: Collections / Generating Iterables

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-served-by-the-pot-collections-iteration-and-iterables-98745d63]] - previous source section: Served by the Pot: Collections / Iteration and Iterables
- [[javascriptallonge-section-served-by-the-pot-collections-rewriting-iterable-operations-f8a6e431]] - next source section: Served by the Pot: Collections / rewriting iterable operations

### Source structure

- [[javascriptallonge-section-served-by-the-pot-collections-e15a3403]] - broader source section: Served by the Pot: Collections
- [[javascriptallonge-section-served-by-the-pot-collections-generating-iterables-generators-and-iterables-adba5c82]] - narrower source section: Served by the Pot: Collections / Generating Iterables / generators and iterables
- [[javascriptallonge-section-served-by-the-pot-collections-generating-iterables-generators-are-coroutines-d0fde127]] - narrower source section: Served by the Pot: Collections / Generating Iterables / generators are coroutines
- [[javascriptallonge-section-served-by-the-pot-collections-generating-iterables-javascript-s-generators-60a99d41]] - narrower source section: Served by the Pot: Collections / Generating Iterables / javascript's generators
- [[javascriptallonge-section-served-by-the-pot-collections-generating-iterables-more-generators-30279cb0]] - narrower source section: Served by the Pot: Collections / Generating Iterables / more generators
- [[javascriptallonge-section-served-by-the-pot-collections-generating-iterables-recursive-iterators-6db8d95d]] - narrower source section: Served by the Pot: Collections / Generating Iterables / recursive iterators
- [[javascriptallonge-section-served-by-the-pot-collections-generating-iterables-state-machines-b395ef25]] - narrower source section: Served by the Pot: Collections / Generating Iterables / state machines
- [[javascriptallonge-section-served-by-the-pot-collections-generating-iterables-yielding-iterables-89322869]] - narrower source section: Served by the Pot: Collections / Generating Iterables / yielding iterables

## Statements

- Iterables look cool, but then again, everything looks amazing when you're given cherry-picked examples. What is there they don't do well? _(javascriptallonge.pdf (source-range-c98ab3e6-01594))_
- Let's consider how they work. Whether it's a simple functional iterator, or an iterable object with a .next() method, an iterator is something we call repeatedly until it tells us that it's done. _(javascriptallonge.pdf (source-range-c98ab3e6-01595))_
- Iterators have to arrange its own state such that when you call them, they compute and return the next item. This seems blindingly obvious and simple. If, for example, you want numbers, you write: _(javascriptallonge.pdf (source-range-c98ab3e6-01596))_
- Well, we've written our iterator as a server . It waits until given a request, and then it returns exactly one item. Then it waits for the next request. There is no concept of pushing numbers out from the iterator, just waiting until a number is pulled out of the iterator by whatever code consumes numbers. _(javascriptallonge.pdf (source-range-c98ab3e6-01599))_
- Of course, when we have some code that makes a bunch of something, we don't usually write it like that. We usually just write something like: _(javascriptallonge.pdf (source-range-c98ab3e6-01600))_
- And magically, the numbers would pour forth. We would generate numbers. Let's put that beside the code for the iterator, minus the iterable scaffolding: _(javascriptallonge.pdf (source-range-c98ab3e6-01602))_
- They're of approximately equal complexity. So why bring up generation? Well, there are some collections that are much easier to generate than to iterate over. Let's look at one: _(javascriptallonge.pdf (source-range-c98ab3e6-01604))_
- Iterables look cool, but then again, everything looks amazing when you're given cherry-picked examples. _(javascriptallonge.pdf (source-range-c98ab3e6-01594))_
- The Numbers iterable returns an object that updates a mutable variable, n , to deliver number after number. _(javascriptallonge.pdf (source-range-c98ab3e6-01598))_
- Then it waits for the next request. _(javascriptallonge.pdf (source-range-c98ab3e6-01599))_
- It waits until given a request, and then it returns exactly one item. _(javascriptallonge.pdf (source-range-c98ab3e6-01599))_
