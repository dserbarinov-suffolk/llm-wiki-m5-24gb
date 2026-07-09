---
page_id: javascriptallonge-section-composing-and-decomposing-data-tail-calls-and-default-arguments-converting-non-tail-calls-to-tai-22a8069d
page_kind: source
summary: Composing and Decomposing Data / Tail Calls (and Default Arguments) / converting non-tail-calls to tail-calls: 7 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-composing-and-decomposing-data-tail-calls-and-default-arguments-converting-non-tail-calls-to-tai-22a8069d@9357fb92431ab3bf7c20bfd481098069
---

# Composing and Decomposing Data / Tail Calls (and Default Arguments) / converting non-tail-calls to tail-calls

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-composing-and-decomposing-data-tail-calls-and-default-arguments-tail-call-optimization-52c04968]] - previous source section: Composing and Decomposing Data / Tail Calls (and Default Arguments) / tail-call optimization

### Source structure

- [[javascriptallonge-section-composing-and-decomposing-data-tail-calls-and-default-arguments-b4311a56]] - broader source section: Composing and Decomposing Data / Tail Calls (and Default Arguments)

### Recipes

- [[javascriptallonge-recipe-converting-non-tail-calls-to-tail-calls]] - recipe pattern: converting non-tail-calls to tail-calls

## Statements

- The obvious solution is push the 1 + work into the call to length . Here's our first cut: _(javascriptallonge.pdf (source-range-c98ab3e6-00958))_
- This lengthDelaysWork function calls itself in tail position. The 1 + work is done before calling itself, and by the time it reaches the terminal position, it has the answer. Now that we've seen how it works, we can clean up the 0 + numberToBeAdded business. But while we're doing that, it's annoying to remember to call it with a zero. Let's fix that: _(javascriptallonge.pdf (source-range-c98ab3e6-00960))_
- This version of length calls uses lengthDelaysWork , and JavaScript optimizes that not to take up memory proportional to the length of the string. We can use this technique with mapWith : _(javascriptallonge.pdf (source-range-c98ab3e6-00963))_
- Brilliant! We can map over large arrays without incurring all the memory and performance overhead of non-tail-calls. And this basic transformation from a recursive function that does not make a tail call, into a recursive function that calls itself in tail position, is a bread-and-butter pattern for programmers using a language that incorporates tail-call optimization. _(javascriptallonge.pdf (source-range-c98ab3e6-00967))_
