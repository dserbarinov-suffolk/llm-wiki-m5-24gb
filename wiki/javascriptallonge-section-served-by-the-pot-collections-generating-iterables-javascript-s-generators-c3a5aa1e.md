---
page_id: javascriptallonge-section-served-by-the-pot-collections-generating-iterables-javascript-s-generators-c3a5aa1e
page_kind: source
summary: Served by the Pot: Collections / Generating Iterables / javascript's generators: 18 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-served-by-the-pot-collections-generating-iterables-javascript-s-generators-c3a5aa1e@1a3054eabc288e661663e77cd16af05b
---

# Served by the Pot: Collections / Generating Iterables / javascript's generators

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-served-by-the-pot-collections-generating-iterables-state-machines-c4cec34a]] - previous source section: Served by the Pot: Collections / Generating Iterables / state machines
- [[javascriptallonge-section-served-by-the-pot-collections-generating-iterables-generators-are-coroutines-e97b031c]] - next source section: Served by the Pot: Collections / Generating Iterables / generators are coroutines

### Source structure

- [[javascriptallonge-section-served-by-the-pot-collections-generating-iterables-8c929c4d]] - broader source section: Served by the Pot: Collections / Generating Iterables

## Statements

- It would be very nice if we could sometimes write iterators as a .next() method that gets called, and sometimes write out a generator. Given the title of this chapter, it is not a surprise that JavaScript makes this possible. _(javascriptallonge.pdf (source-range-0e12e052-01657))_
- We can write an iterator, but use a generation style of programming. An iterator written in a generation style is called a generator . To write a generator, we write a function, but we make two changes: _(javascriptallonge.pdf (source-range-0e12e052-01658))_
- When we invoke empty , we get an iterator with no elements. This makes sense, because empty never yields anything. We call its .next() method, but it's done immediately. _(javascriptallonge.pdf (source-range-0e12e052-01663))_
- Generator functions can take an argument. Let's use that to illustrate yield : _(javascriptallonge.pdf (source-range-0e12e052-01664))_
- Invoking only("you") returns an iterator that we can call with .next() , and it yields "you" . Invoking only more than once gives us fresh iterators each time: _(javascriptallonge.pdf (source-range-0e12e052-01667))_
- An iterator written in a generation style is called a generator . _(javascriptallonge.pdf (source-range-0e12e052-01658))_
- This makes sense, because empty never yields anything. _(javascriptallonge.pdf (source-range-0e12e052-01663))_
- Invoking only more than once gives us fresh iterators each time: _(javascriptallonge.pdf (source-range-0e12e052-01667))_
- Invoking only("you") returns an iterator that we can call with .next() , and it yields "you" . _(javascriptallonge.pdf (source-range-0e12e052-01667))_
- It yields the value of something , and then it's done. _(javascriptallonge.pdf (source-range-0e12e052-01671))_
