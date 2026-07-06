---
page_id: javascriptallonge-section-generating-iterables-5c843adb
page_kind: source
summary: Generating Iterables: 16 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-generating-iterables-5c843adb@1cd2469b4a66c55e4e44e98b615c2165
---

# Generating Iterables

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-summary-c843b152]] - previous source section: summary
- [[javascriptallonge-section-recursive-iterators-6eddd213]] - next source section: recursive iterators

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
